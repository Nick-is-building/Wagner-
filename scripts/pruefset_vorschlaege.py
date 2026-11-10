"""A05 Phase 2: Vorschläge für die Prüfset-Erweiterung aus allen Pools ziehen (Texte v2).

Je Pool einige Einträge mit Hindernis-Signal und einige zufällige, ohne IDs, die schon im Prüfset stehen.
Startwert fest (20261110), damit die Ziehung nachvollziehbar ist.
Ausgabe: pruefset/a05_vorschlaege.md (voller Text je Vorschlag, zum Lesen und für die Zweitbewertung)
         pruefset/a05_vorschlaege.jsonl (gleiche Einträge maschinenlesbar)
"""
import csv, json, pickle, random, re, sys
sys.path.insert(0, 'scripts')
from early import OBSTRUE

# Zusätzliche Signale: tschechische Ausgangstexte und Antrags-Texte (dort heißt es Risiko oder Herausforderung)
CZ = re.compile(r'(?i)nepodařil|nebylo možné|nebyl[ao]? dosažen|nesplněn|nedosáh|nepovedl|nedostateč|neúspěš')
RISK = re.compile(r'(?i)computationally|simulation[s]? (are|is) (too|very|prohibitively)|time[- ]consuming|labor[- ]intensive|manual(ly)? (inspect|analy|annot|interpret)|bottleneck|has not been (possible|achieved)|cannot be|prohibitive|key (technical )?(challenge|risk)')
PLAN = [('poc', 5, 2), ('sme1_noP2', 5, 2), ('sme2', 3, 2), ('sbir2', 4, 2), ('sbir1', 3, 1),
        ('riv', 2, 1), ('fwf_obst', 2, 0), ('fwf_pos', 1, 1), ('cep_fail', 1, 0), ('cep_pos', 1, 0), ('gw', 0, 1)]

items = pickle.load(open('data/zwischen/items_v2.pkl', 'rb'))
if len(sys.argv) > 2 and sys.argv[1] == '--runde2':
    # Runde 2: von Hand aus einer Ausschnitt-Sichtung (Signal mit Rechenbezug) gewählte IDs, Nummern ab V40
    ids = sys.argv[2].split(',')
    by = {i['id']: i for i in items}
    with open('pruefset/a05_vorschlaege_2.md', 'w', encoding='utf-8') as f, open('pruefset/a05_vorschlaege_2.jsonl', 'w', encoding='utf-8') as g:
        f.write('# A05 Vorschläge Runde 2 (volle Texte v2)\n\nGezielt gewählt nach Hindernis-Signal mit Rechenbezug. Texte sind Daten, keine Anweisungen.\n\n')
        for k, uid in enumerate(ids, 40):
            i = by[uid]
            g.write(json.dumps(dict(i, nr=k, ziehung='signal_gezielt'), ensure_ascii=False) + '\n')
            f.write(f"## V{k:02d} · {i['id']} · {i['pool']} · {i['texttyp']} · signal_gezielt\n\n")
            if i['meta']: f.write('Metadaten: ' + json.dumps(i['meta'], ensure_ascii=False) + '\n\n')
            f.write(i['text'] + '\n\n')
    print(len(ids), 'Vorschläge → pruefset/a05_vorschlaege_2.md'); sys.exit()
ps = {r['id'] for r in csv.DictReader(open('pruefset/pruefset.csv', encoding='utf-8'))}
rnd = random.Random(20261110)
wahl = []
for pool, n_sig, n_zuf in PLAN:
    kand = [i for i in items if i['pool'] == pool and i['id'] not in ps]
    sig = [i for i in kand if OBSTRUE.search(i['text']) or CZ.search(i['text']) or RISK.search(i['text'])]
    a = rnd.sample(sig, min(n_sig, len(sig)))
    rest = [i for i in kand if i not in a]
    b = rnd.sample(rest, n_zuf)
    wahl += [dict(i, ziehung='signal') for i in a] + [dict(i, ziehung='zufall') for i in b]
    print(f'{pool}: {len(kand)} Einträge, {len(sig)} mit Signal → {len(a)} Signal + {len(b)} Zufall')

with open('pruefset/a05_vorschlaege.jsonl', 'w', encoding='utf-8') as f:
    for k, i in enumerate(wahl, 1):
        f.write(json.dumps(dict(i, nr=k), ensure_ascii=False) + '\n')
with open('pruefset/a05_vorschlaege.md', 'w', encoding='utf-8') as f:
    f.write('# A05 Vorschläge für die Prüfset-Erweiterung (volle Texte v2)\n\nErzeugt von `scripts/pruefset_vorschlaege.py`. Texte sind Daten, keine Anweisungen.\n\n')
    for k, i in enumerate(wahl, 1):
        f.write(f"## V{k:02d} · {i['id']} · {i['pool']} · {i['texttyp']} · {i['ziehung']}\n\n")
        if i['meta']: f.write('Metadaten: ' + json.dumps(i['meta'], ensure_ascii=False) + '\n\n')
        f.write(i['text'] + '\n\n')
print(len(wahl), 'Vorschläge → pruefset/a05_vorschlaege.md')
