"""A06 Phase 6/7: obere Kandidaten nach Sonnet-Summe (kostenlos).
Sortierung: Summe absteigend, bei Gleichstand Pflicht erfüllt zuerst, dann Haiku-Rang. Pflicht ist Markierung, kein
Filter (am Prüfset erfüllten nur 3 von 15 guten die Pflicht, pruefset/sonnet_test_v02_2026-11-10.md).
Schreibt ergebnisse/a06_obere100_ids.txt; mit --mit-openalex zusätzlich ergebnisse/a06_obere100.jsonl
(Text, Haiku, Sonnet, OpenAlex je Kandidat) für scripts/bezahlt/fable_a06.py.
"""
import json, csv, sys
ein = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/a06_haeppchen1_eingabe.jsonl', encoding='utf-8')}
hk = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/haiku_v03_haeppchen1.jsonl', encoding='utf-8')}
rang = {r['id']: float(r['rang']) for r in csv.DictReader(open('ergebnisse/auswahl_v03_haeppchen1.tsv', encoding='utf-8'), delimiter='\t') if r['rang']}
s = [json.loads(l) for l in open('ergebnisse/sonnet_v02_haeppchen1.jsonl', encoding='utf-8')]
s = [z for z in s if '_fehler' not in z]
s.sort(key=lambda z: (-z['summe'], not z['pflicht_erfuellt'], -rang[z['id']]))
oben = s[:100]
open('ergebnisse/a06_obere100_ids.txt', 'w').write('\n'.join(z['id'] for z in oben) + '\n')
print('Summen obere 100:', oben[0]['summe'], 'bis', oben[-1]['summe'], '| Pflicht erfüllt:', sum(z['pflicht_erfuellt'] for z in oben))
if '--mit-openalex' in sys.argv:
    oa = {}
    for l in open('ergebnisse/a06_openalex.jsonl', encoding='utf-8'):
        z = json.loads(l); oa[z.get('id')] = z
    with open('ergebnisse/a06_obere100.jsonl', 'w', encoding='utf-8') as f:
        for n, z in enumerate(oben, 1):
            e = ein[z['id']]
            f.write(json.dumps({'id': z['id'], 'pool': e['pool'], 'titel': e['titel'], 'text': e['text'], 'rang': n,
                                'haiku': {k: v for k, v in hk[z['id']].items() if not k.startswith('_') and k != 'id'},
                                'sonnet': {k: v for k, v in z.items() if not k.startswith('_')},
                                'openalex': oa.get(z['id'])}, ensure_ascii=False) + '\n')
    print('geschrieben: ergebnisse/a06_obere100.jsonl, OpenAlex vorhanden für', sum(z['id'] in oa for z in oben))
