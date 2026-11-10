"""Haiku-Extraktion v0.2 (A03). BEZAHLT: ruft die Claude-API auf. Ein Durchlauf je Eintrag.

Aufruf (vom Projektordner aus):
  python3 scripts/bezahlt/haiku_v02.py --test A --dry-run
  python3 scripts/bezahlt/haiku_v02.py --test A --freigabe 2026-11-10-A03 --max-usd 0.50
Test A: ergebnisse/pruefset_eingabe.jsonl  -> ergebnisse/haiku_v02_pruefset.jsonl
Test B: ergebnisse/zufall100_eingabe.jsonl -> ergebnisse/haiku_v02_zufall.jsonl
RIV-Einträge mit Nutzungscode O werden seit dem Nachtrag zu A03 mitgesendet (vorher übersprungen).
--max-usd gilt für beide Tests zusammen: bisherige Kosten aus beiden Ausgabedateien werden mitgezählt.
Fehlerzeilen werden beim Neustart wiederholt, erfolgreiche übersprungen (fortsetzbar).
Schlüssel: ANTHROPIC_API_KEY aus .env (wird nie ausgegeben).
"""
import argparse, json, os, re, sys, time
sys.path.insert(0, 'scripts')
import weiter_regel as W

MODELL = 'claude-haiku-5-5'
PREIS_IN, PREIS_OUT = 0.10, 0.50          # $ je Million Token (wie A02; dort an echten Aufrufen bestätigt)
MAX_TOKENS = 2000
ZEICHEN_JE_TOKEN = 3.0
AUSGABE_SCHAETZ = 1100                    # A02 beobachtet rund 1000; v0.2 hat zwei Felder mehr
PROMPT = 'prompts/haiku_extraktion.md'
TESTS = {'A': ('ergebnisse/pruefset_eingabe.jsonl', 'ergebnisse/haiku_v02_pruefset.jsonl'),
         'B': ('ergebnisse/zufall100_eingabe.jsonl', 'ergebnisse/haiku_v02_zufall.jsonl')}
VERSION_MARKE = '"unklar" ist nur erlaubt, wenn ein Zitat einen Hinweis zeigt.'


def lade_env():
    if os.path.exists('.env'):
        for line in open('.env'):
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"\''))


def systemanweisung():
    md = open(PROMPT, encoding='utf-8').read()
    m = re.search(r'## Systemanweisung\s+```\n(.*?)\n```', md, re.S)
    schema = re.search(r'## Antwortschema\s+```json\n(.*?)\n```', md, re.S)
    if not m or not schema:
        sys.exit('Systemanweisung oder Antwortschema in prompts/haiku_extraktion.md nicht gefunden.')
    if VERSION_MARKE not in m.group(1) or 'unerledigter_kern' not in schema.group(1):
        sys.exit('Prompt ist nicht v0.2; Abbruch.')
    return m.group(1) + '\n\nSchema:\n' + schema.group(1)


def nutzertext(r):
    return (f"ID: {r['id']}\nQuelle: {r.get('pool','')}\nTitel: {r.get('titel','')}\n"
            f"Ziel/Zusammenfassung: {r.get('text_a','')}\nBewertung/Bericht/Nutzung: {r.get('text_b','')}")


def kosten(tin, tout):
    return (tin * PREIS_IN + tout * PREIS_OUT) / 1e6


def freigabe_ok(fid):
    return any(l.startswith('|') and f'| {fid} |' in l for l in open('ENTSCHEIDUNGEN.md', encoding='utf-8'))


def json_aus_text(t):
    t = t.strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m:
        t = m.group(1).strip()
    obj, _ = json.JSONDecoder().raw_decode(t[t.find('{'):])
    return obj


def lies(pfad):
    fertig, usd = set(), 0.0
    if os.path.exists(pfad):
        for l in open(pfad, encoding='utf-8'):
            z = json.loads(l)
            usd += z.get('_kosten_usd', 0.0)
            if '_fehler' not in z:
                fertig.add(z['id'])
    return fertig, usd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--test', choices=['A', 'B'], required=True)
    ap.add_argument('--freigabe')
    ap.add_argument('--max-usd', type=float)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    ein, aus = TESTS[a.test]

    eintraege = [json.loads(l) for l in open(ein, encoding='utf-8')]
    senden = eintraege
    fertig, _ = lies(aus)
    bisher = sum(lies(p)[1] for _, p in TESTS.values())
    offen = [r for r in senden if r['id'] not in fertig]

    sysm = systemanweisung()
    tin = sum((len(sysm) + len(nutzertext(r))) / ZEICHEN_JE_TOKEN for r in offen)
    if a.dry_run:
        print(f'Trockenlauf Test {a.test} (nichts gesendet). Modell {MODELL}, ein Durchlauf')
        print(f'Einträge: {len(eintraege)}, '
              f'zu senden: {len(senden)}, schon erledigt: {len(fertig)}, offen: {len(offen)}')
        print(f'Eingabe: rund {tin:,.0f} Token, Ausgabe: rund {len(offen)*AUSGABE_SCHAETZ:,} Token')
        print(f'Geschätzte Kosten: {kosten(tin, len(offen)*AUSGABE_SCHAETZ):.4f} $; '
              f'ungünstigster Fall: {kosten(tin, len(offen)*MAX_TOKENS):.4f} $')
        print(f'Bisher unter A03 ausgegeben (beide Tests): {bisher:.4f} $')
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

    out = open(aus, 'a', encoding='utf-8')
    ausgegeben = bisher
    for i, r in enumerate(offen, 1):
        usr = nutzertext(r)
        worst = kosten((len(sysm) + len(usr)) / ZEICHEN_JE_TOKEN, MAX_TOKENS)
        if ausgegeben + worst > a.max_usd:
            print(f'Stopp vor Grenze: {ausgegeben:.4f} $ + bis {worst:.4f} $ > {a.max_usd} $')
            break
        zeile = {'id': r['id']}
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
                zeile['id'] = r['id']
            except Exception as e:
                zeile['_fehler'] = f'JSON nicht lesbar: {e}'
                zeile['_roh'] = text
        except Exception as e:
            zeile['_fehler'] = f'{type(e).__name__}: {e}'
        out.write(json.dumps(zeile, ensure_ascii=False) + '\n')
        out.flush()
        print(f"{i}/{len(offen)} {r['id']} {'FEHLER' if '_fehler' in zeile else 'ok'} | gesamt {ausgegeben:.4f} $")
        time.sleep(0.2)
    print(f'Fertig. Ausgegeben unter A03 laut Zählung: {ausgegeben:.4f} $')


if __name__ == '__main__':
    main()
