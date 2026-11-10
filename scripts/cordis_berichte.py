"""CORDIS-Ergebnisberichte (H2020 und Horizon Europe) für die Pools poc, sme1_noP2, sme2.

Liest data/zwischen/newpools.pkl und data/roh/cordis_berichte/{h2020,he}/reportSummaries.csv,
entpackt aus den JSON-Zips nur die Berichte dieser Projekte nach data/roh/cordis_berichte/json/,
behält je Projekt den letzten Bericht (höchste Periodennummer, dann jüngstes Änderungsdatum)
und schreibt data/zwischen/cordis_berichte.jsonl (projectID, rcn, periode, summary, workPerformed, finalResults).
Mit --zip-loeschen werden die JSON-Zips danach gelöscht (Auftrag A05). Vom Projektordner aus aufrufen.
"""
import csv, json, os, pickle, re, sys, zipfile, collections

D = 'data/roh/cordis_berichte/'
POOLS = ('poc', 'sme1_noP2', 'sme2')
QUELLEN = (('h2020', 'cordis-h2020reports-json.zip'), ('he', 'cordis-HORIZONreports-json.zip'))

n = pickle.load(open('data/zwischen/newpools.pkl', 'rb'))
pool_ids = {p: {r['id'] for r in n[p]} for p in POOLS}
alle = set().union(*pool_ids.values())

# Projekt-ID -> Liste (periode, datum, rcn, quelle)
ber = collections.defaultdict(list)
for q, _ in QUELLEN:
    for r in csv.DictReader(open(f'{D}{q}/reportSummaries.csv', encoding='utf-8'), delimiter=';'):
        if r['projectID'] not in alle: continue
        m = re.search(r'period\s+(\d+)', r['title'])
        ber[r['projectID']].append((int(m.group(1)) if m else 0, r['contentUpdateDate'], r['rcn'], q))
letzter = {pid: max(v) for pid, v in ber.items()}

os.makedirs(D + 'json', exist_ok=True)
aus = []
for q, zname in QUELLEN:
    brauche = {f'result-rcn-{v[2]}_en.json': pid for pid, v in letzter.items() if v[3] == q}
    pfad = D + zname
    if os.path.exists(pfad):
        with zipfile.ZipFile(pfad) as z:
            namen = set(z.namelist())
            for name in brauche:
                if name in namen and not os.path.exists(D + 'json/' + name):
                    z.extract(name, D + 'json')
    for name, pid in brauche.items():
        f = D + 'json/' + name
        if not os.path.exists(f):
            print('fehlt:', name, pid); continue
        j = json.load(open(f, encoding='utf-8'))
        aus.append({'projectID': pid, 'rcn': j.get('rcn'), 'quelle': q, 'periode': j.get('periodNumber'),
                    'periodTo': j.get('periodTo'),
                    'summary': j.get('summary') or '', 'workPerformed': j.get('workPerformed') or '',
                    'finalResults': j.get('finalResults') or ''})

with open('data/zwischen/cordis_berichte.jsonl', 'w', encoding='utf-8') as f:
    for r in aus: f.write(json.dumps(r, ensure_ascii=False) + '\n')

# H2020-PoC-Berichte haben nur summary (dort steht der Ausgang); daher zählt jedes nichtleere Feld.
hat = {r['projectID'] for r in aus if (r['summary'] + r['workPerformed'] + r['finalResults']).strip()}
voll = {r['projectID'] for r in aus if (r['workPerformed'] + r['finalResults']).strip()}
for p in POOLS:
    print(f'{p}: {len(pool_ids[p] & hat)} von {len(pool_ids[p])} mit Bericht, davon {len(pool_ids[p] & voll)} mit workPerformed/finalResults')
print('Berichte geschrieben:', len(aus), '→ data/zwischen/cordis_berichte.jsonl')

if '--zip-loeschen' in sys.argv:
    for _, zname in QUELLEN:
        if os.path.exists(D + zname):
            os.remove(D + zname); print('gelöscht:', D + zname)
