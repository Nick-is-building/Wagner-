"""Gemeinsamer Läufer für bezahlte API-Aufrufe (A06). Wird von haiku_v03.py, sonnet_v02.py und fable_a06.py importiert.

Regeln aus scripts/bezahlt/README.md: Freigabe-ID muss in ENTSCHEIDUNGEN.md stehen, --max-usd wird vor jedem
Aufruf geprüft (bisherige Kosten + ungünstigster Fall aller laufenden Aufrufe), jede Antwort sofort eine Zeile JSONL,
Neustart überspringt erfolgreiche IDs und wiederholt Fehler. Kein Batch-Verfahren: direkte Aufrufe, parallel
(Standard 15), Wiederholung bei Ratenlimit und Serverfehlern übernimmt das SDK (max_retries).
Schlüssel: ANTHROPIC_API_KEY aus .env (wird nie ausgegeben).
"""
import asyncio, json, os, re, sys, time

# $ je Million Token (Eingabe, Ausgabe). Haiku/Sonnet aus docs/04_pipeline.md; Fable 5.2 wie Fable 5.1 laut
# claude-api-Referenz (Stand 2026-10-06), für 5.2 nicht bestätigt. Cache-Lesen 0,1×, Cache-Schreiben 1,25× Eingabe.
PREISE = {'claude-haiku-5-5': (0.10, 0.50), 'claude-sonnet-5-5': (2.00, 10.00),
          'claude-fable-5-2': (10.00, 50.00), 'claude-fable-5-1': (10.00, 50.00),
          'claude-opus-5-5': (4.00, 20.00), 'claude-opus-4-8': (5.00, 25.00)}
WEBSUCHE_USD = 0.01          # 10 $ je 1.000 Suchen
ZEICHEN_JE_TOKEN = 2.1       # gemessen A02/A03 an 146 Aufrufen


def lade_env():
    if os.path.exists('.env'):
        for line in open('.env'):
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"\''))


def freigabe_ok(fid):
    return any(l.startswith('|') and f'| {fid} |' in l for l in open('ENTSCHEIDUNGEN.md', encoding='utf-8'))


def tok(text):
    return len(text) / ZEICHEN_JE_TOKEN


def kosten_usage(modell, u):
    pin, pout = PREISE[modell]
    g = lambda k: (getattr(u, k, None) if not isinstance(u, dict) else u.get(k)) or 0
    st = getattr(u, 'server_tool_use', None) if not isinstance(u, dict) else u.get('server_tool_use')
    suchen = (getattr(st, 'web_search_requests', 0) if st is not None and not isinstance(st, dict)
              else (st or {}).get('web_search_requests', 0)) or 0
    return (g('input_tokens') * pin + g('cache_creation_input_tokens') * pin * 1.25
            + g('cache_read_input_tokens') * pin * 0.1 + g('output_tokens') * pout) / 1e6 + suchen * WEBSUCHE_USD


def json_aus_text(t):
    t = t.strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m:
        t = m.group(1).strip()
    obj, _ = json.JSONDecoder().raw_decode(t[t.find('{'):])
    return obj


def lies(pfad):
    """Erfolgreich erledigte IDs und bisherige Kosten einer JSONL-Ausgabe."""
    fertig, usd = set(), 0.0
    if os.path.exists(pfad):
        for l in open(pfad, encoding='utf-8'):
            z = json.loads(l)
            usd += z.get('_kosten_usd', 0.0)
            if '_fehler' not in z:
                fertig.add(z['id'])
    return fertig, usd


def pruefe_start(a):
    if not a.freigabe or a.max_usd is None:
        sys.exit('Echter Lauf braucht --freigabe und --max-usd.')
    if not freigabe_ok(a.freigabe):
        sys.exit(f'Freigabe {a.freigabe} steht nicht in ENTSCHEIDUNGEN.md; Abbruch.')
    lade_env()
    if not os.environ.get('ANTHROPIC_API_KEY'):
        sys.exit('ANTHROPIC_API_KEY ist nicht gesetzt (.env); Abbruch.')


async def _ein_aufruf(client, modell, params, beta=False):
    """Ein Aufruf per Stream; setzt bei pause_turn (Server-Werkzeuge) fort. Gibt (Antworten-Liste) zurück."""
    msgs = list(params['messages'])
    antworten = []
    api = client.beta.messages if beta else client.messages
    for _ in range(6):
        async with api.stream(**{**params, 'messages': msgs}) as s:
            r = await s.get_final_message()
        antworten.append(r)
        if r.stop_reason != 'pause_turn':
            break
        msgs = msgs + [{'role': 'assistant', 'content': r.content}]
    return antworten


async def lauf(aufgaben, aus, *, modell, max_usd, bisher_usd, worst_usd, parallel=15, beta=False,
               auswerten=None, json_erwartet=True):
    """aufgaben: Liste von dicts mit 'id' und 'params' (Argumente für messages.stream ohne model).
    worst_usd(aufgabe) -> ungünstigste Kosten eines Aufrufs. auswerten(zeile, antworten) darf Felder ergänzen."""
    import anthropic
    client = anthropic.AsyncAnthropic(max_retries=8, timeout=900)
    sem = asyncio.Semaphore(parallel)
    lock = asyncio.Lock()
    stand = {'usd': bisher_usd, 'reserviert': 0.0, 'n': 0, 'fehler': 0, 'gestoppt': False}
    out = open(aus, 'a', encoding='utf-8')
    t0 = time.time()

    async def eins(a):
        w = worst_usd(a)
        async with sem:
            async with lock:
                if stand['usd'] + stand['reserviert'] + w > max_usd:
                    stand['gestoppt'] = True
                    return
                stand['reserviert'] += w
            zeile = {'id': a['id']}
            try:
                antworten = await _ein_aufruf(client, modell, {'model': modell, **a['params']}, beta=beta)
                k = sum(kosten_usage(r.model if r.model in PREISE else modell, r.usage) for r in antworten)
                letzte = antworten[-1]
                zeile['_usage'] = {'in': sum(r.usage.input_tokens for r in antworten),
                                   'out': sum(r.usage.output_tokens for r in antworten),
                                   'cache_read': sum((r.usage.cache_read_input_tokens or 0) for r in antworten),
                                   'cache_write': sum((r.usage.cache_creation_input_tokens or 0) for r in antworten),
                                   'stop': letzte.stop_reason, 'modell': letzte.model}
                zeile['_kosten_usd'] = k
                text = ''.join(b.text for b in letzte.content if b.type == 'text')
                if letzte.stop_reason == 'refusal':
                    zeile['_fehler'] = 'refusal'
                    zeile['_roh'] = text
                elif json_erwartet:
                    try:
                        zeile.update(json_aus_text(text))
                        zeile['id'] = a['id']
                    except Exception as e:
                        zeile['_fehler'] = f'JSON nicht lesbar: {e}'
                        zeile['_roh'] = text
                else:
                    zeile['text'] = text
                if auswerten:
                    auswerten(zeile, antworten)
            except Exception as e:
                k = 0.0
                zeile['_fehler'] = f'{type(e).__name__}: {str(e)[:300]}'
            async with lock:
                stand['reserviert'] -= w
                stand['usd'] += k
                stand['n'] += 1
                stand['fehler'] += '_fehler' in zeile
                out.write(json.dumps(zeile, ensure_ascii=False) + '\n')
                out.flush()
                if stand['n'] % 25 == 0 or stand['n'] == len(aufgaben):
                    print(f"{stand['n']}/{len(aufgaben)} | Fehler {stand['fehler']} | gesamt {stand['usd']:.4f} $ | "
                          f"{time.time()-t0:.0f} s", flush=True)

    await asyncio.gather(*(eins(a) for a in aufgaben))
    out.close()
    if stand['gestoppt']:
        print(f'Stopp vor Grenze {max_usd} $: nicht alle Aufgaben gesendet.')
    print(f"Fertig: {stand['n']} Aufrufe, {stand['fehler']} Fehler, Kosten laut Zählung gesamt {stand['usd']:.4f} $, "
          f"{time.time()-t0:.0f} s")
    return stand
