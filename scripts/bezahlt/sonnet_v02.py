"""Sonnet-Bewertung v0.2 (A06, Kriterien 1–14). BEZAHLT. Parallel, fortsetzbar.

Aufruf (vom Projektordner aus):
  python3 scripts/bezahlt/sonnet_v02.py --satz pruefset --dry-run
  python3 scripts/bezahlt/sonnet_v02.py --satz pruefset --freigabe 2026-11-10-A06c --max-usd 2.00
  python3 scripts/bezahlt/sonnet_v02.py --satz haeppchen1 --freigabe 2026-11-10-A06d --max-usd 5.00
pruefset: alle Einträge aus ergebnisse/a06_pruefset_eingabe.jsonl.
haeppchen1: nur Einträge mit weiter=True aus ergebnisse/auswahl_v03_haeppchen1.tsv, nach Haiku-Rang von oben;
  der Läufer hört vor der Grenze auf (danach rutscht nichts nach).
Ausgabe ergebnisse/sonnet_v02_<satz>.jsonl mit summe und pflicht_erfuellt (vom Skript gerechnet).
Ohne Denken (thinking between_tools), Fähigkeiten-Katalog als zwischengespeicherter System-Teil.
"""
import argparse, asyncio, csv, json, re, sys
sys.path.insert(0, 'scripts/bezahlt')
import api_lauf as L

MODELL = 'claude-sonnet-5-5'
MAX_TOKENS = 1500
AUSGABE_SCHAETZ = 650
DOPPELT = ('k3', 'k4', 'k11', 'k12')
EINFACH = ('k5', 'k6', 'k8', 'k9', 'k10', 'k13')


def system_teile():
    md = open('prompts/sonnet_bewertung.md', encoding='utf-8').read()
    if 'v0.2' not in md.splitlines()[0]:
        sys.exit('Prompt ist nicht v0.2; Abbruch.')
    b = re.findall(r'```(?:json)?\n(.*?)\n```', md, re.S)
    kat = open('docs/03_faehigkeiten_katalog.md', encoding='utf-8').read()
    kat = kat[kat.index('## Querschnitts-Fähigkeiten'):kat.index('## Methoden')]
    return [{'type': 'text', 'text': f'{b[0]}\n\nSchema:\n{b[1]}'},
            {'type': 'text', 'text': 'Fähigkeiten-Katalog (Auszug):\n\n' + kat, 'cache_control': {'type': 'ephemeral'}}]


def haiku_felder(z):
    return {k: v for k, v in z.items() if not k.startswith('_') and k != 'id'}


def nutzertext(r, h):
    return (f"ID: {r['id']}\nQuelle: {r['pool']}\nTexttyp: {r['texttyp']}\nTitel: {r['titel']}\nText:\n{r['text']}\n\n"
            f"Haiku-Felder: {json.dumps(h, ensure_ascii=False)}")


def rechne(z):
    p = z.get('punkte') or {}
    g = lambda k: max(0, min(3, int(p.get(k) or 0)))
    z['summe'] = 2 * sum(g(k) for k in DOPPELT) + sum(g(k) for k in EINFACH)
    k1, k2 = z.get('k1') or {}, z.get('k2') or {}
    z['pflicht_erfuellt'] = bool(not z.get('ausschluss') and k1.get('erfuellt') and k2.get('erfuellt')
                                 and g('k11') >= 1 and g('k12') >= 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--satz', choices=['pruefset', 'haeppchen1'], required=True)
    ap.add_argument('--freigabe'); ap.add_argument('--max-usd', type=float)
    ap.add_argument('--parallel', type=int, default=15)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    ein = {json.loads(l)['id']: json.loads(l) for l in open(f'ergebnisse/a06_{a.satz}_eingabe.jsonl', encoding='utf-8')}
    hk = {}
    for l in open(f'ergebnisse/haiku_v03_{a.satz}.jsonl', encoding='utf-8'):
        z = json.loads(l)
        if '_fehler' not in z:
            hk[z['id']] = haiku_felder(z)
    if a.satz == 'pruefset':
        ids = list(ein)
    else:
        t = [r for r in csv.DictReader(open('ergebnisse/auswahl_v03_haeppchen1.tsv', encoding='utf-8'), delimiter='\t')
             if r['weiter'] == 'True']
        t.sort(key=lambda r: -float(r['rang']))
        ids = [r['id'] for r in t]
    aus = f'ergebnisse/sonnet_v02_{a.satz}.jsonl'
    fertig, bisher = L.lies(aus)
    offen = [i for i in ids if i not in fertig]
    sysm = system_teile()
    pin, pout = L.PREISE[MODELL]
    lsys, lkat = len(sysm[0]['text']), len(sysm[1]['text'])
    je = lambda i: (L.tok(sysm[0]['text'] + nutzertext(ein[i], hk.get(i, {}))) * pin + L.tok(sysm[1]['text']) * pin * 0.1)
    if a.dry_run:
        n = len(offen)
        schaetz = sum(je(i) + AUSGABE_SCHAETZ * pout for i in offen) / 1e6
        print(f'Trockenlauf Sonnet {a.satz}: {len(ids)} Einträge, offen {n}; System {lsys} + Katalog {lkat} Zeichen')
        print(f'Geschätzt {schaetz:.3f} $ ({schaetz/max(n,1):.4f} $ je Eintrag); bisher {bisher:.4f} $')
        return
    L.pruefe_start(a)
    worst = lambda x: (je(x['id']) + L.tok(sysm[1]['text']) * pin * 1.25 + MAX_TOKENS * pout) / 1e6
    aufgaben = [{'id': i, 'params': {'max_tokens': MAX_TOKENS, 'thinking': {'type': 'between_tools'},
                                     'system': sysm,
                                     'messages': [{'role': 'user', 'content': nutzertext(ein[i], hk.get(i, {}))}]}}
                for i in offen]
    def auswerten(z, _):
        if '_fehler' not in z:
            try:
                rechne(z)
            except Exception as e:
                z['_fehler'] = f'Punkte nicht lesbar: {e}'
    asyncio.run(L.lauf(aufgaben, aus, modell=MODELL, max_usd=a.max_usd, bisher_usd=bisher, worst_usd=worst,
                       parallel=a.parallel, auswerten=auswerten))


if __name__ == '__main__':
    main()
