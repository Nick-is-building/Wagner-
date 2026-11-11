"""A07 Vorauswahl aus den Haiku-v0.3-Antworten von Häppchen 1 (kostenlos).

Regel (auftraege/A07_muster.md): Muster H1, H2, H3, H5 oder H6; hindernis_quelle "ergebnis";
erster_schritt software, simulation, datenanalyse oder prototyp_klein; Pool poc nur mit Hindernis-Zitat,
das die Zitatprüfung im Text gefunden hat.
"Vorhandener Teilerfolg" hat kein Haiku-Feld; das prüft Sonnet v0.3 (K5 >= 1) nach dem Lauf, siehe a07_rangliste.py.
Schreibt ergebnisse/a07_vorauswahl.tsv (alle Einträge mit Grund, auch abgelehnte) und zählt je Pool.
"""
import json, csv, collections
MUSTER = {'H1', 'H2', 'H3', 'H5', 'H6'}
SCHRITT = {'software', 'simulation', 'datenanalyse', 'prototyp_klein'}
ein = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/a06_haeppchen1_eingabe.jsonl', encoding='utf-8')}
zc = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/zitat_check_v03_haeppchen1.jsonl', encoding='utf-8')}
zeilen, n = [], collections.Counter()
for l in open('ergebnisse/haiku_v03_haeppchen1.jsonl', encoding='utf-8'):
    z = json.loads(l)
    e = ein[z['id']]
    g = []
    if '_fehler' in z:
        g.append('haiku_fehler')
    else:
        if not set(z.get('muster') or []) & MUSTER: g.append('muster')
        if z.get('hindernis_quelle') != 'ergebnis': g.append('quelle')
        if z.get('erster_schritt') not in SCHRITT: g.append('schritt')
        if e['pool'] == 'poc':
            zz = zc.get(z['id'], {})
            if not z.get('hindernis_zitat') or 'hindernis_zitat' in (zz.get('felder_ohne_beleg') or []):
                g.append('poc_ohne_zitat')
    ok = not g
    n[(e['pool'], 'gesamt')] += 1; n[(e['pool'], 'gewählt')] += ok
    zeilen.append({'id': z['id'], 'pool': e['pool'], 'texttyp': e['texttyp'], 'gewaehlt': ok, 'gruende': ','.join(g)})
with open('ergebnisse/a07_vorauswahl.tsv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(zeilen[0]), delimiter='\t'); w.writeheader(); w.writerows(zeilen)
for p in sorted({k[0] for k in n}):
    print(f'{p}: {n[(p, "gewählt")]} von {n[(p, "gesamt")]}')
print('gesamt gewählt:', sum(r['gewaehlt'] for r in zeilen))
