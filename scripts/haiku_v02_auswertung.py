"""Auswertung Haiku v0.2 (A03). Kostenlos, liest nur lokale Dateien. Regel: scripts/weiter_regel.py.

Test A: ergebnisse/haiku_v02_pruefset.jsonl -> ergebnisse/haiku_v02_pruefset.tsv
Test B: ergebnisse/haiku_v02_zufall.jsonl   -> ergebnisse/haiku_v02_zufall.tsv,
        ergebnisse/haiku_v02_stichprobe.md (10 Durchgekommene, 10 Ausgesiebte, Startwert 2026)
Zusammenfassung nach stdout. Je ID zählt die letzte Zeile ohne _fehler.
Optional: python3 scripts/haiku_v02_auswertung.py ZIEL_PRUEFSET.tsv ZIEL_ZUFALL.tsv (Tabellen aus A03 bleiben dann unberührt).
"""
import csv, json, random, sys
from collections import defaultdict
sys.path.insert(0, 'scripts')
import weiter_regel as W

RIV_O = W.riv_o_ids()


def antworten(pfad):
    a = {}
    for l in open(pfad, encoding='utf-8'):
        z = json.loads(l)
        if '_fehler' not in z:
            a[z['id']] = z
    return a


def bewerte(eintraege, antw):
    zeilen = []
    for r in eintraege:
        i = r['id']
        a = antw.get(i)
        if a is None:
            zeilen.append(dict(r, weiter=None, gruende=['keine gültige Antwort'], f={}, a=None)); continue
        w, g = W.weiter(a, riv_o=i in RIV_O)
        zeilen.append(dict(r, weiter=w, gruende=g, f=W.felder(a), a=a, riv_o=i in RIV_O))
    return zeilen


def tsv(pfad, zeilen, extra):
    with open(pfad, 'w', encoding='utf-8') as f:
        f.write('\t'.join(['id', 'pool'] + extra + ['weiter', 'kern', 'th', 'os', 'art', 'rechen', 'gruende']) + '\n')
        for z in zeilen:
            f.write('\t'.join([z['id'], z['pool']] + [str(z.get(e, '')) for e in extra] +
                    ['ja' if z['weiter'] else ('FEHLT' if z['weiter'] is None else 'NEIN')] +
                    [str(z['f'].get(k, '')) for k in ('kern', 'th', 'os', 'art', 'rechen')] + ['; '.join(z['gruende'])]) + '\n')


def zit(d):
    return (d or {}).get('zitat') if isinstance(d, dict) else None


def block(z):
    a = z['a'] or {}
    s = [f"### {z['id']} ({z['pool']})", f"- Titel: {z['titel']}"]
    if a.get('titel_en'): s.append(f"- Titel englisch (Haiku): {a['titel_en']}")
    s.append(f"- Weiter: {'ja' if z['weiter'] else 'nein'} ({'; '.join(z['gruende'])})")
    if z['a'] is None:
        s.append(f"- Text A (gekürzt): {z['text_a'][:400]}")
        s.append(f"- Text B (gekürzt): {z['text_b'][:400]}")
    else:
        f = z['f']
        s.append(f"- Werte: Kern {f['kern']} · Hindernis {f['th']} · offener Schritt {f['os']} · Grund {f['art']} · Rechenanteil {f['rechen']}")
        for name, q in [('Ziel', zit(a.get('ziel'))), ('Erreicht', zit(a.get('erreicht'))),
                        ('Unerledigter Kern', zit(a.get('unerledigter_kern'))), ('Hindernis', zit(a.get('hindernis'))),
                        ('Abbruchgrund', zit(a.get('abbruchgrund_art'))), ('Offener Schritt', a.get('offener_schritt_beleg'))]:
            if q: s.append(f"- {name}: „{q}“")
    return '\n'.join(s)


def test_a():
    ps = {r['id']: r for r in csv.DictReader(open('pruefset/pruefset.csv', encoding='utf-8'))}
    ein = [json.loads(l) for l in open('ergebnisse/pruefset_eingabe.jsonl', encoding='utf-8')]
    zeilen = bewerte(ein, antworten('ergebnisse/haiku_v02_pruefset.jsonl'))
    for z in zeilen: z['klasse'] = ps[z['id']]['klasse']
    tsv(sys.argv[1] if len(sys.argv) > 1 else 'ergebnisse/haiku_v02_pruefset.tsv', zeilen, ['klasse'])
    s = defaultdict(lambda: [0, 0, 0])
    for z in zeilen:
        s[z['klasse']][0] += bool(z['weiter']); s[z['klasse']][1] += 1; s[z['klasse']][2] += z['weiter'] is None
    print('Test A (Prüfset):')
    for k, (w, n, fe) in s.items(): print(f'  {k}: {w} von {n} weiter' + (f', {fe} ohne Antwort' if fe else ''))
    g, gr = s['gut'], s['grenzfall']
    print(f"  Testregel: gut {g[0]}/{g[1]} (alle nötig), Grenzfall {gr[0]}/{gr[1]} = {gr[0]/gr[1]:.0%} (≥ 80 % nötig) -> "
          f"{'BESTANDEN' if g[0]==g[1] and gr[0] >= 0.8*gr[1] else 'NICHT BESTANDEN'}")
    for z in zeilen:
        if z['klasse'] in ('gut', 'grenzfall') and not z['weiter']: print(f"  durchgefallen: {z['id']} ({z['klasse']}): {'; '.join(z['gruende'])}")


def test_b():
    ein = [json.loads(l) for l in open('ergebnisse/zufall100_eingabe.jsonl', encoding='utf-8')]
    zeilen = bewerte(ein, antworten('ergebnisse/haiku_v02_zufall.jsonl'))
    tsv(sys.argv[2] if len(sys.argv) > 2 else 'ergebnisse/haiku_v02_zufall.tsv', zeilen, [])
    s = defaultdict(lambda: [0, 0])
    for z in zeilen: s[z['pool']][0] += bool(z['weiter']); s[z['pool']][1] += 1
    print('Test B (100 Zufallseinträge):')
    for k, (w, n) in sorted(s.items(), key=lambda x: -x[1][1]): print(f'  {k}: {w} von {n} weiter ({w/n:.0%})')
    w = sum(v[0] for v in s.values()); print(f'  gesamt: {w} von {len(zeilen)} weiter; ohne Antwort: {sum(z["weiter"] is None for z in zeilen)}')
    import os
    if os.path.exists('ergebnisse/haiku_v02_stichprobe.md'):
        print('  Stichprobe existiert schon (A03), nicht überschrieben.'); return
    rnd = random.Random(2026)
    durch = rnd.sample([z for z in zeilen if z['weiter']], min(10, sum(1 for z in zeilen if z['weiter'])))
    raus = rnd.sample([z for z in zeilen if z['weiter'] is False], min(10, sum(1 for z in zeilen if z['weiter'] is False)))
    with open('ergebnisse/haiku_v02_stichprobe.md', 'w', encoding='utf-8') as f:
        f.write('# Haiku v0.2: Stichprobe aus Test B (A03)\n\nZufällig gezogen (Startwert 2026) aus `ergebnisse/haiku_v02_zufall.tsv`. '
                'Zitate wörtlich aus der Haiku-Antwort. RIV-Einträge mit Code O: Regel aus dem Nachtrag zu A03.\n'
                'Spalte zum Bewerten: gut / Grenzfall / ungeeignet, je Eintrag vom Planungs-Chat.\n\n')
        f.write('## 10 Durchgekommene\n\n' + '\n\n'.join(block(z) for z in durch) + '\n\n')
        f.write('## 10 Ausgesiebte\n\n' + '\n\n'.join(block(z) for z in raus) + '\n')


def riv_teil():
    """Die 11 RIV-Code-O-Einträge (Nachtrag A03) und Hochrechnung auf alle RIV-Code-O-Einträge in items.pkl."""
    import math, pickle
    ps = [json.loads(l) for l in open('ergebnisse/pruefset_eingabe.jsonl', encoding='utf-8')]
    zf = [json.loads(l) for l in open('ergebnisse/zufall100_eingabe.jsonl', encoding='utf-8')]
    za = bewerte([r for r in ps if r['id'] in RIV_O], antworten('ergebnisse/haiku_v02_pruefset.jsonl'))
    zb = bewerte([r for r in zf if r['id'] in RIV_O], antworten('ergebnisse/haiku_v02_zufall.jsonl'))
    print('RIV Code O (Nachtrag):')
    for z in za + zb:
        ohne_kern = z['f']['rechen'] in ('mittel', 'hoch') or z['f']['th'] in W.POS
        print(f"  {z['id']} [{'Prüfset' if z in za else 'Zufall'}]: {'weiter' if z['weiter'] else 'NICHT weiter'}"
              f" ({'; '.join(z['gruende'])}) | kern {z['f']['kern']}, th {z['f']['th']}, rechen {z['f']['rechen']}"
              f" | ohne Kern-Bedingung: {'weiter' if ohne_kern else 'nicht'}")
    w = sum(bool(z['weiter']) for z in za + zb)
    print(f'  weiter: {w} von {len(za)+len(zb)}')
    items = pickle.load(open('data/zwischen/items.pkl', 'rb'))
    N = sum(1 for it in items if it[1] == 'riv' and it[0] in RIV_O)
    k, n = sum(bool(z['weiter']) for z in zb), len(zb)
    def wilson(k, n, zq=1.96):
        p = k / n; d = 1 + zq*zq/n; m = (p + zq*zq/(2*n)) / d; h = zq*math.sqrt(p*(1-p)/n + zq*zq/(4*n*n)) / d
        return m - h, m + h
    lo, hi = wilson(k, n)
    print(f'  Hochrechnung (nur Zufallsstichprobe, {k} von {n}): rund {round(N*k/n)} von {N} RIV-Code-O-Einträgen,'
          f' 95-%-Bereich (Wilson) {round(N*lo)} bis {round(N*hi)}')
    k2 = sum(1 for z in zb if z['f']['rechen'] in ('mittel', 'hoch') or z['f']['th'] in W.POS)
    print(f'  Variante ohne Kern-Bedingung: {k2} von {n} -> rund {round(N*k2/n)} von {N}')


if __name__ == '__main__':
    test_a()
    test_b()
    riv_teil()
