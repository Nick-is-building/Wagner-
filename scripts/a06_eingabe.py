"""A06: Eingaben mit Texten v2 bauen (kostenlos). Schreibt nach ergebnisse/:
  a06_pruefset_eingabe.jsonl  Prüfset (pruefset/pruefset.csv) mit Klasse; IDs, die harte Frühfilter entfernt
                              haben, mit altem Text aus ergebnisse/pruefset_eingabe.jsonl (texttyp ergebnis), sonst ausgelassen
  a06_zufall_eingabe.jsonl dieselben 100 Zufallseinträge wie A03 (ergebnisse/zufall100_eingabe.jsonl), Text v2
  a06_haeppchen1_eingabe.jsonl Pools poc, sme2, cep_fail, fwf_obst
Felder: id, pool, titel, texttyp, text (+ klasse beim Prüfset).
"""
import pickle, csv, json, collections
it = {i['id']: i for i in pickle.load(open('data/zwischen/items_v2.pkl', 'rb'))}
alt = {json.loads(l)['id']: json.loads(l) for l in open('ergebnisse/pruefset_eingabe.jsonl', encoding='utf-8')}
HAEPPCHEN1 = ('poc', 'sme2', 'cep_fail', 'fwf_obst')

def zeile(i, **x):
    return json.dumps({'id': i['id'], 'pool': i['pool'], 'titel': i['titel'], 'texttyp': i['texttyp'], 'text': i['text'], **x}, ensure_ascii=False) + '\n'

ps = list(csv.DictReader(open('pruefset/pruefset.csv', encoding='utf-8')))
aus, ohne = 0, []
with open('ergebnisse/a06_pruefset_eingabe.jsonl', 'w', encoding='utf-8') as f:
    for r in ps:
        if r['id'] in it:
            f.write(zeile(it[r['id']], klasse=r['klasse'])); aus += 1
        elif r['id'] in alt:
            a = alt[r['id']]
            f.write(zeile({'id': a['id'], 'pool': a['pool'], 'titel': a['titel'], 'texttyp': 'ergebnis',
                           'text': f"{a['titel']}\n[Ziel/Antrag] {a['text_a']}\n[Ausgang] {a['text_b']}"}, klasse=r['klasse'])); aus += 1
        else:
            ohne.append((r['id'], r['klasse']))
print(f'Prüfset: {aus} von {len(ps)} geschrieben; ohne Text (harte Frühfilter): {ohne}')
z = [json.loads(l)['id'] for l in open('ergebnisse/zufall100_eingabe.jsonl', encoding='utf-8')]
with open('ergebnisse/a06_zufall_eingabe.jsonl', 'w', encoding='utf-8') as f:
    for i in z: f.write(zeile(it[i]))
print('Zufall:', len(z), dict(collections.Counter(it[i]['texttyp'] for i in z)))
h = [i for i in it.values() if i['pool'] in HAEPPCHEN1]
with open('ergebnisse/a06_haeppchen1_eingabe.jsonl', 'w', encoding='utf-8') as f:
    for i in h: f.write(zeile(i))
print('Häppchen 1:', len(h), dict(collections.Counter((i['pool'], i['texttyp']) for i in h)))
