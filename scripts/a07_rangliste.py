"""A07 Rangliste aus Sonnet v0.3 auf die Vorauswahl (kostenlos).
Regel (Nick, Haltepunkt 1): Rangfolge nach Summe (inkl. M und Abzügen); Pflicht-Nullen als Spalte, kein Ausschluss.
Teilerfolg (Vorauswahl-Regel) über K5 >= 1: ohne Teilerfolg nicht in der Rangliste, bleibt mit Grund in der Datei.
Gleichstand: M-Wert, dann Pflicht erfüllt. Ausschluss aus der festen Liste wird angezeigt, nicht gefiltert.
Schreibt ergebnisse/a07_rangliste.tsv (alle 103), ergebnisse/a07_obere40_ids.txt;
mit --mit-openalex ergebnisse/a07_obere40.jsonl (Text, Haiku, Sonnet, OpenAlex) für scripts/bezahlt/fable_a07.py.
"""
import json, csv, sys
ein = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/a06_haeppchen1_eingabe.jsonl', encoding='utf-8')}
hk = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/haiku_v03_haeppchen1.jsonl', encoding='utf-8')}
S = [json.loads(l) for l in open('ergebnisse/sonnet_v03_vorauswahl.jsonl', encoding='utf-8')]
S = [z for z in S if '_fehler' not in z]
MW = {'ja': 2, 'teilweise': 1}


def nullen(z):
    p = z.get('punkte') or {}
    n = []
    if not (z.get('k1') or {}).get('erfuellt'): n.append('K1')
    if not (z.get('k2') or {}).get('erfuellt'): n.append('K2')
    if not int(p.get('k11') or 0): n.append('K11')
    if not int(p.get('k12') or 0): n.append('K12')
    return n


for z in S:
    z['_k5'] = int((z.get('punkte') or {}).get('k5') or 0)
    z['_m'] = str((z.get('m') or {}).get('wert') or 'nein').lower()
    z['_nullen'] = nullen(z)
    z['_abzug'] = [k for k in ('fertiges_produkt', 'ausgruendung', 'kern_geloest') if (z.get('abzug') or {}).get(k)]
S.sort(key=lambda z: (-z['summe'], -MW.get(z['_m'], 0), not z['pflicht_erfuellt']))
rang, n = {}, 0
for z in S:
    if z['_k5'] >= 1:
        n += 1; rang[z['id']] = n
with open('ergebnisse/a07_rangliste.tsv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['rang', 'id', 'pool', 'summe', 'm', 'pflicht_nullen', 'abzuege', 'ausschluss', 'k5', 'grund_nicht_in_liste', 'titel'])
    for z in S:
        w.writerow([rang.get(z['id'], ''), z['id'], ein[z['id']]['pool'], z['summe'], z['_m'], ','.join(z['_nullen']),
                    ','.join(z['_abzug']), z.get('ausschluss_liste') or '', z['_k5'],
                    '' if z['id'] in rang else 'kein Teilerfolg (K5 = 0)', ein[z['id']]['titel'][:90]])
oben = [z for z in S if z['id'] in rang][:40]
open('ergebnisse/a07_obere40_ids.txt', 'w').write('\n'.join(z['id'] for z in oben) + '\n')
print(f'{len(S)} bewertet, {len(rang)} mit Teilerfolg in der Rangliste; obere 40 Summe {oben[0]["summe"]} bis {oben[-1]["summe"]}; '
      f'M ja {sum(z["_m"]=="ja" for z in oben)}, teilweise {sum(z["_m"]=="teilweise" for z in oben)}; '
      f'ohne Pflicht-Null {sum(not z["_nullen"] for z in oben)}; mit Abzug {sum(bool(z["_abzug"]) for z in oben)}; '
      f'Ausschluss {sum(bool(z.get("ausschluss_liste")) for z in oben)}')
if '--mit-openalex' in sys.argv:
    oa = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/a07_openalex.jsonl', encoding='utf-8')}
    with open('ergebnisse/a07_obere40.jsonl', 'w', encoding='utf-8') as f:
        for z in oben:
            e = ein[z['id']]
            f.write(json.dumps({'id': z['id'], 'pool': e['pool'], 'titel': e['titel'], 'text': e['text'], 'rang': rang[z['id']],
                                'pflicht_nullen': z['_nullen'],
                                'haiku': {k: v for k, v in hk[z['id']].items() if not k.startswith('_') and k != 'id'},
                                'sonnet': {k: v for k, v in z.items() if not k.startswith('_')},
                                'openalex': oa.get(z['id'])}, ensure_ascii=False) + '\n')
    print('geschrieben: ergebnisse/a07_obere40.jsonl, OpenAlex für', sum(z['id'] in oa for z in oben))
