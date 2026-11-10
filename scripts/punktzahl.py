"""Punktzahl je Haiku-Antwort und Schwellen S1/S2 (A04). Kostenlos, nur lokale Dateien.

Punkte (fehlende Felder 0; Werte bereinigt mit weiter_regel.felder, "unklar" zählt nur, wenn die
Antwort irgendein Zitat hat):
  +2 technisches Hindernis ja, +1 unklar
  +2 Hindernis-Muster H1/H2/H3, sonst +1 H4 bis H7 (höchster Wert zählt, nicht addiert)
  +2 Rechenanteil hoch, +1 mittel
  +1 Abbruchgrund Geld/Personal/Organisation
  +1 offener Schritt ja (RIV-Code O zählt als ja)
  +1 Teilerfolg vorhanden (teilerfolg.text nicht leer)
  +1 unerledigter Kern ja
  -2 Abbruchgrund formal und technisches Hindernis nein
v0.1 hat zwei Durchläufe je Eintrag: es zählt der höhere Wert.
S1: höchste Schwelle, bei der alle guten und mindestens 80 % der Grenzfälle mindestens so viele Punkte haben.
S2: höchste Schwelle, bei der alle guten mindestens so viele Punkte haben.
Ausgaben: ergebnisse/punktzahl_pruefset.tsv, ergebnisse/punktzahl_zufall.tsv; Zusammenfassung nach stdout.
"""
import csv, json, math, sys
from collections import defaultdict, Counter
sys.path.insert(0, 'scripts')
import weiter_regel as W

RIV_O = W.riv_o_ids()
N_GESAMT = 17421


def punkte(a, riv_o=False):
    f = W.felder(a)
    p, teile = 0, []
    def plus(n, was):
        nonlocal p; p += n; teile.append(f'{n:+d} {was}')
    if f['th'] == 'ja': plus(2, 'Hindernis ja')
    elif f['th'] == 'unklar': plus(1, 'Hindernis unklar')
    m = set(a.get('hindernis_muster') or [])
    if m & {'H1', 'H2', 'H3'}: plus(2, 'Muster H1-H3')
    elif m & {'H4', 'H5', 'H6', 'H7'}: plus(1, 'Muster H4-H7')
    if f['rechen'] == 'hoch': plus(2, 'Rechenanteil hoch')
    elif f['rechen'] == 'mittel': plus(1, 'Rechenanteil mittel')
    if f['art'] in W.ART_WEITER: plus(1, f"Grund {f['art']}")
    if f['os'] == 'ja' or riv_o: plus(1, 'offener Schritt ja' + (' (RIV O)' if riv_o else ''))
    if ((a.get('teilerfolg') or {}).get('text') or '').strip(): plus(1, 'Teilerfolg')
    if f['kern'] == 'ja': plus(1, 'Kern ja')
    if f['art'] == 'formal' and f['th'] == 'nein': plus(-2, 'formal ohne Hindernis')
    return p, teile


def lade(pfad, version):
    """id -> (punkte, teile); bei mehreren Durchläufen der höhere Wert."""
    best = {}
    for l in open(pfad, encoding='utf-8'):
        a = json.loads(l)
        if '_fehler' in a: continue
        s = punkte(a, a['id'] in RIV_O)
        if a['id'] not in best or s[0] > best[a['id']][0]:
            best[a['id']] = s
    return best


def schwellen(klasse, pkt):
    gut = [pkt[i][0] for i, k in klasse.items() if k == 'gut' and i in pkt]
    gr = [pkt[i][0] for i, k in klasse.items() if k == 'grenzfall' and i in pkt]
    s2 = min(gut)
    s1 = max(t for t in range(-5, 20) if all(g >= t for g in gut) and sum(g >= t for g in gr) >= math.ceil(0.8 * len(gr)))
    return s1, s2, gut, gr


def main():
    klasse = {r['id']: r['klasse'] for r in csv.DictReader(open('pruefset/pruefset.csv', encoding='utf-8'))}
    vers = {'v0.1': lade('ergebnisse/haiku_pruefset_ok.jsonl', 'v0.1'),
            'v0.2': lade('ergebnisse/haiku_v02_pruefset.jsonl', 'v0.2')}
    with open('ergebnisse/punktzahl_pruefset.tsv', 'w', encoding='utf-8') as f:
        f.write('id\tklasse\tpunkte_v01\tpunkte_v02\tteile_v02\n')
        for i, k in sorted(klasse.items(), key=lambda x: (x[1], -vers['v0.2'].get(x[0], (-99,))[0])):
            if i not in vers['v0.2']: continue
            f.write(f"{i}\t{k}\t{vers['v0.1'][i][0]}\t{vers['v0.2'][i][0]}\t{'; '.join(vers['v0.2'][i][1])}\n")
    res = {}
    for v, pkt in vers.items():
        s1, s2, gut, gr = schwellen(klasse, pkt)
        un = [pkt[i][0] for i, k in klasse.items() if k == 'ungeeignet' and i in pkt]
        res[v] = (s1, s2)
        print(f'{v}: gute {sorted(gut, reverse=True)} | Grenzfälle {sorted(gr, reverse=True)} | ungeeignet {sorted(un, reverse=True)}')
        for name, s in (('S1', s1), ('S2', s2)):
            print(f'  {name} = {s}: gut {sum(g >= s for g in gut)}/{len(gut)}, Grenzfall {sum(g >= s for g in gr)}/{len(gr)}, '
                  f'ungeeignet {sum(g >= s for g in un)}/{len(un)}')
    # Zufall: nur v0.2 vorhanden
    ein = {json.loads(l)['id']: json.loads(l)['pool'] for l in open('ergebnisse/zufall100_eingabe.jsonl', encoding='utf-8')}
    pz = lade('ergebnisse/haiku_v02_zufall.jsonl', 'v0.2')
    with open('ergebnisse/punktzahl_zufall.tsv', 'w', encoding='utf-8') as f:
        f.write('id\tpool\tpunkte\tteile\n')
        for i, pool in ein.items():
            f.write(f"{i}\t{pool}\t{pz[i][0]}\t{'; '.join(pz[i][1])}\n")
    print('Zufall v0.2, Verteilung der Punkte:', dict(sorted(Counter(p for p, _ in pz.values()).items())))
    s1, s2 = res['v0.2']
    pools = defaultdict(list)
    for i, pool in ein.items(): pools[pool].append(pz[i][0])
    for name, s in (('S1', s1), ('S2', s2)):
        n = sum(p >= s for p, _ in pz.values())
        print(f'Zufall v0.2 {name} = {s}: {n} von 100 -> hochgerechnet rund {round(N_GESAMT * n / 100):,} von {N_GESAMT:,}')
        for pool, ps in sorted(pools.items(), key=lambda x: -len(x[1])):
            print(f'    {pool}: {sum(p >= s for p in ps)} von {len(ps)}')


if __name__ == '__main__':
    main()
