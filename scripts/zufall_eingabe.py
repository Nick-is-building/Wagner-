"""Test B (A03): 100 Zufallseinträge aus data/zwischen/items.pkl, Startwert 2026, ohne Prüfset-IDs.
Kostenlos. Ausgabe: ergebnisse/zufall100_eingabe.jsonl (id, pool, titel, text_a, text_b).
Schreibt nicht über eine vorhandene Datei, damit die Stichprobe fest bleibt.
"""
import pickle, csv, json, os, random, sys, collections
AUS = 'ergebnisse/zufall100_eingabe.jsonl'
if os.path.exists(AUS):
    sys.exit(f'{AUS} existiert schon; nicht überschrieben.')
items = pickle.load(open('data/zwischen/items.pkl', 'rb'))
ps = {r['id'] for r in csv.DictReader(open('pruefset/pruefset.csv', encoding='utf-8'))}
rest = [it for it in items if it[0] not in ps]
wahl = random.Random(2026).sample(rest, 100)
with open(AUS, 'w', encoding='utf-8') as f:
    for it in wahl:
        f.write(json.dumps({'id': it[0], 'pool': it[1], 'titel': it[2], 'text_a': it[3], 'text_b': it[4]}, ensure_ascii=False) + '\n')
print(f'{len(items)} Einträge, {len(items)-len(rest)} Prüfset-IDs ausgeschlossen, 100 gezogen:',
      dict(collections.Counter(it[1] for it in wahl)))
