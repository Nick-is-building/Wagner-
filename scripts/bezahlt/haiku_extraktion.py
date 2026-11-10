"""Haiku-Extraktion am Prüfset (A02). BEZAHLT: ruft die Claude-API auf.

Aufruf (vom Projektordner aus):
  python3 scripts/bezahlt/haiku_extraktion.py --dry-run
  python3 scripts/bezahlt/haiku_extraktion.py --freigabe 2026-11-09-A02 --max-usd 0.50

Eingabe:  ergebnisse/pruefset_eingabe.jsonl (id, pool, titel, text_a, text_b)
Prompt:   prompts/haiku_extraktion.md, Abschnitt "Systemanweisung" (wird nicht verändert)
Ausgabe:  ergebnisse/haiku_pruefset.jsonl, eine Zeile je Antwort und Durchlauf (1, 2).
          Die Felder der Haiku-Antwort stehen oben in der Zeile (für scripts/zitat_check.py),
          dazu durchlauf, _usage, _kosten_usd; bei Fehlern _fehler. Fehlerzeilen werden beim
          Neustart wiederholt, erfolgreiche übersprungen (fortsetzbar).
Schlüssel: ANTHROPIC_API_KEY aus .env (wird nie ausgegeben).
"""
import argparse, json, os, re, sys, time

MODELL = 'claude-haiku-5-5'
PREIS_IN, PREIS_OUT = 0.10, 0.50          # $ je Million Token (Quelle: auftraege/A02)
MAX_TOKENS = 2000
ZEICHEN_JE_TOKEN = 3.0                    # grobe, vorsichtige Schätzung für tschechisch/deutsch/englisch
AUSGABE_SCHAETZ = 1000                    # beobachtet im Testaufruf: rund 1000 je Antwort (A02 schätzte 400)
PROMPT = 'prompts/haiku_extraktion.md'
EINGABE = 'ergebnisse/pruefset_eingabe.jsonl'
AUSGABE = 'ergebnisse/haiku_pruefset.jsonl'

REGEL_1 = ('- Im Zweifel bei technisches_hindernis und offener_schritt lieber "ja" als "nein":\n'
           '  Ein falsches Ja kostet wenig, ein falsches Nein verliert einen Kandidaten.')
REGEL_2 = ('- Lies den Text vom Ende her. Achte besonders auf Nebensätze, die erklären, '
           'warum etwas nicht klappte.')

ENV_LADEN = '.env'


def lade_env():
    if os.path.exists(ENV_LADEN):
        for line in open(ENV_LADEN):
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"\''))


def systemanweisung(durchlauf):
    md = open(PROMPT, encoding='utf-8').read()
    m = re.search(r'## Systemanweisung\s+```\n(.*?)\n```', md, re.S)
    if not m:
        sys.exit('Systemanweisung in prompts/haiku_extraktion.md nicht gefunden.')
    s = m.group(1)
    schema = re.search(r'## Antwortschema\s+```json\n(.*?)\n```', md, re.S)
    if not schema:
        sys.exit('Antwortschema in prompts/haiku_extraktion.md nicht gefunden.')
    if REGEL_1 not in s:
        sys.exit('Regel "Im Zweifel ja" nicht im Prompt gefunden; Prompt wurde geändert, Skript prüfen.')
    if durchlauf == 2:
        s = s.replace(REGEL_1, REGEL_2)
    return s + '\n\nSchema:\n' + schema.group(1)


def nutzertext(r):
    return (f"ID: {r['id']}\nQuelle: {r.get('pool','')}\nTitel: {r.get('titel','')}\n"
            f"Ziel/Zusammenfassung: {r.get('text_a','')}\nBewertung/Bericht/Nutzung: {r.get('text_b','')}")


def kosten(tin, tout):
    return (tin * PREIS_IN + tout * PREIS_OUT) / 1e6


def freigabe_ok(fid):
    for line in open('ENTSCHEIDUNGEN.md', encoding='utf-8'):
        if line.startswith('|') and f'| {fid} |' in line.replace('||', '|'):
            return True
    return False


def json_aus_text(t):
    t = t.strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m:
        t = m.group(1).strip()
    obj, _ = json.JSONDecoder().raw_decode(t[t.find('{'):])   # erstes Objekt, Text danach ignorieren
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--freigabe')
    ap.add_argument('--max-usd', type=float)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()

    eintraege = [json.loads(l) for l in open(EINGABE, encoding='utf-8')]
    auftraege = [(r, d) for d in (1, 2) for r in eintraege]

    fertig, bisher_usd = set(), 0.0
    if os.path.exists(AUSGABE):
        for l in open(AUSGABE, encoding='utf-8'):
            z = json.loads(l)
            bisher_usd += z.get('_kosten_usd', 0.0)
            if '_fehler' not in z:
                fertig.add((z['id'], z['durchlauf']))
    offen = [(r, d) for r, d in auftraege if (r['id'], d) not in fertig]

    # Schätzung je offenem Aufruf
    sys_zeichen = {d: len(systemanweisung(d)) for d in (1, 2)}
    tin = sum((sys_zeichen[d] + len(nutzertext(r))) / ZEICHEN_JE_TOKEN for r, d in offen)
    tout = len(offen) * AUSGABE_SCHAETZ
    schaetz = kosten(tin, tout)
    worst = kosten(tin, len(offen) * MAX_TOKENS)

    if a.dry_run:
        print(f'Trockenlauf (nichts gesendet). Modell {MODELL}')
        print(f'Einträge: {len(eintraege)}, Durchläufe: 2, Aufrufe gesamt: {len(auftraege)}, '
              f'schon erledigt: {len(fertig)}, offen: {len(offen)}')
        print(f'Eingabe: rund {tin:,.0f} Token (Schätzung {ZEICHEN_JE_TOKEN} Zeichen je Token), '
              f'Ausgabe: rund {tout:,.0f} Token ({AUSGABE_SCHAETZ} je Antwort)')
        print(f'Geschätzte Kosten: {schaetz:.4f} $ (Preise {PREIS_IN} / {PREIS_OUT} $ je Mio Token)')
        print(f'Ungünstigster Fall (jede Antwort {MAX_TOKENS} Token lang): {worst:.4f} $')
        print(f'Bisher laut Ausgabedatei ausgegeben: {bisher_usd:.4f} $')
        return

    if not a.freigabe or a.max_usd is None:
        sys.exit('Echter Lauf braucht --freigabe und --max-usd.')
    if not freigabe_ok(a.freigabe):
        sys.exit(f'Freigabe {a.freigabe} steht nicht in ENTSCHEIDUNGEN.md; Abbruch.')

    lade_env()
    if not os.environ.get('ANTHROPIC_API_KEY'):
        sys.exit('ANTHROPIC_API_KEY ist nicht gesetzt (.env); Abbruch.')
    import anthropic
    client = anthropic.Anthropic()

    os.makedirs('ergebnisse', exist_ok=True)
    out = open(AUSGABE, 'a', encoding='utf-8')
    ausgegeben = bisher_usd
    for i, (r, d) in enumerate(offen, 1):
        sysm, usr = systemanweisung(d), nutzertext(r)
        # Obergrenze vor dem Aufruf: schlechtester Fall dieses Aufrufs
        worst_call = kosten((len(sysm) + len(usr)) / ZEICHEN_JE_TOKEN, MAX_TOKENS)
        if ausgegeben + worst_call > a.max_usd:
            print(f'Stopp vor Grenze: {ausgegeben:.4f} $ + bis {worst_call:.4f} $ > {a.max_usd} $')
            break
        zeile = {'id': r['id'], 'durchlauf': d}
        try:
            resp = client.messages.create(model=MODELL, max_tokens=MAX_TOKENS, thinking={"type": "disabled"},
                                          system=sysm, messages=[{'role': 'user', 'content': usr}])
            u = resp.usage
            k = kosten(u.input_tokens, u.output_tokens)
            ausgegeben += k
            zeile['_usage'] = {'in': u.input_tokens, 'out': u.output_tokens, 'stop': resp.stop_reason}
            zeile['_kosten_usd'] = k
            text = ''.join(b.text for b in resp.content if b.type == 'text')
            try:
                zeile.update(json_aus_text(text))
                zeile['id'], zeile['durchlauf'] = r['id'], d
            except Exception as e:
                zeile['_fehler'] = f'JSON nicht lesbar: {e}'
                zeile['_roh'] = text
        except Exception as e:
            zeile['_fehler'] = f'{type(e).__name__}: {e}'
        out.write(json.dumps(zeile, ensure_ascii=False) + '\n')
        out.flush()
        print(f"{i}/{len(offen)} {r['id']} D{d} {'FEHLER' if '_fehler' in zeile else 'ok'} | gesamt {ausgegeben:.4f} $")
        time.sleep(0.2)
    print(f'Fertig. Ausgegeben laut Zählung: {ausgegeben:.4f} $')


if __name__ == '__main__':
    main()
