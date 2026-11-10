"""Haiku-Extraktion v0.3 (A06). BEZAHLT. Zwei Prompt-Varianten nach texttyp, Texte v2, parallel.

Aufruf (vom Projektordner aus):
  python3 scripts/bezahlt/haiku_v03.py --satz pruefset --dry-run
  python3 scripts/bezahlt/haiku_v03.py --satz pruefset --freigabe 2026-11-10-A06a --max-usd 0.50
Sätze: pruefset, zufall (beide Freigabe A06a, Grenze gilt gemeinsam), haeppchen1 (A06b).
Eingabe ergebnisse/a06_<satz>_eingabe.jsonl (scripts/a06_eingabe.py), Ausgabe ergebnisse/haiku_v03_<satz>.jsonl.
"""
import argparse, asyncio, json, re, sys
sys.path.insert(0, 'scripts/bezahlt')
import api_lauf as L

MODELL = 'claude-haiku-5-5'
MAX_TOKENS = 700
AUSGABE_SCHAETZ = 220
SAETZE = {'pruefset': ['pruefset', 'zufall'], 'zufall': ['pruefset', 'zufall'], 'haeppchen1': ['haeppchen1']}


def systemanweisungen():
    md = open('prompts/haiku_extraktion.md', encoding='utf-8').read()
    if 'v0.3' not in md.splitlines()[0]:
        sys.exit('Prompt ist nicht v0.3; Abbruch.')
    b = re.findall(r'```(?:json)?\n(.*?)\n```', md, re.S)
    gemein, erg, erg_s, ant, ant_s = b[0], b[1], b[2], b[3], b[4]
    return {'ergebnis': f'{gemein}\n\n{erg}\n\nSchema:\n{erg_s}', 'antrag': f'{gemein}\n\n{ant}\n\nSchema:\n{ant_s}'}


def nutzertext(r):
    return f"ID: {r['id']}\nQuelle: {r['pool']}\nTitel: {r['titel']}\nText:\n{r['text']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--satz', choices=list(SAETZE), required=True)
    ap.add_argument('--freigabe'); ap.add_argument('--max-usd', type=float)
    ap.add_argument('--parallel', type=int, default=15)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    ein, aus = f'ergebnisse/a06_{a.satz}_eingabe.jsonl', f'ergebnisse/haiku_v03_{a.satz}.jsonl'
    eintraege = [json.loads(l) for l in open(ein, encoding='utf-8')]
    fertig, _ = L.lies(aus)
    bisher = sum(L.lies(f'ergebnisse/haiku_v03_{s}.jsonl')[1] for s in SAETZE[a.satz])
    offen = [r for r in eintraege if r['id'] not in fertig]
    sysm = systemanweisungen()
    pin, pout = L.PREISE[MODELL]
    tin = sum(L.tok(sysm[r['texttyp']] + nutzertext(r)) for r in offen)
    worst = lambda x: (L.tok(sysm[x['texttyp']] + nutzertext(x)) * pin + MAX_TOKENS * pout) / 1e6
    if a.dry_run:
        print(f'Trockenlauf {a.satz} (nichts gesendet), Modell {MODELL}: {len(eintraege)} Einträge, offen {len(offen)}')
        print(f'Eingabe rund {tin:,.0f} Token, Ausgabe rund {len(offen)*AUSGABE_SCHAETZ:,} Token')
        print(f'Geschätzt {(tin*pin + len(offen)*AUSGABE_SCHAETZ*pout)/1e6:.4f} $; ungünstigster Fall '
              f'{sum(worst(r) for r in offen):.4f} $; bisher unter dieser Freigabe {bisher:.4f} $')
        return
    L.pruefe_start(a)
    typ = {r['id']: r['texttyp'] for r in offen}
    aufgaben = [{'id': r['id'], 'eintrag': r, 'params': {
        'max_tokens': MAX_TOKENS, 'thinking': {'type': 'disabled'}, 'system': sysm[r['texttyp']],
        'messages': [{'role': 'user', 'content': nutzertext(r)}]}} for r in offen]
    def auswerten(z, _):
        z['_texttyp'] = typ[z['id']]
    asyncio.run(L.lauf(aufgaben, aus, modell=MODELL, max_usd=a.max_usd, bisher_usd=bisher,
                       worst_usd=lambda x: worst(x['eintrag']),
                       parallel=a.parallel, auswerten=auswerten))


if __name__ == '__main__':
    main()
