"""Baut die Eingabe-CSV für openalex_check.py aus einer Liste von IDs (eine pro Zeile oder Prüfset-CSV).
Holt englische Titel und Ziele, Endjahr, Förderkennzeichen, Einrichtung und Land aus den Rohdaten.
Aufruf: python3 scripts/openalex_eingabe.py pruefset/pruefset.csv ergebnisse/openalex_eingabe.csv [--nur gut,grenzfall]
"""
import csv, json, glob, sys, re
csv.field_size_limit(10**9)
src, dst = sys.argv[1], sys.argv[2]
nur = sys.argv[sys.argv.index('--nur') + 1].split(',') if '--nur' in sys.argv else None
if src.endswith('.csv'):
    rows = list(csv.DictReader(open(src, encoding='utf-8')))
    ids = [r['id'] for r in rows if not nur or r.get('klasse', '').split(' ')[0] in nur]
else:
    ids = [l.strip() for l in open(src) if l.strip()]
want = set(ids); out = {}
R = 'data/roh/'
for r in csv.DictReader(open(R + 'cep.csv', encoding='utf-8-sig', errors='replace', newline='')):
    k = r['kod_projektu']
    if k in want:
        out[k] = dict(titel=r['nazev_projektu_anglicky'] or r['nazev_projektu_originalni'],
                      ziel=(r['cile_reseni_anglicky'] or r['cile_reseni_originalni'])[:600],
                      ab=r['rok_ukonceni'] or r['rok_zahajeni'], foerderkennz=k, einrichtung=r['nazev_organizace'], land='CZ')
for f in glob.glob(R + 'fwf2/*.json'):
    for r in json.load(open(f))['results']:
        k = r.get('_str.grantdoi', '')
        if k in want:
            out[k] = dict(titel=r.get('_str.projecttitle.en', ''), ziel=re.sub(r'<[^>]+>', ' ', r.get('_str.prproposalsummary.en') or '')[:600],
                          ab=(r.get('_date.enddate') or '')[:4], foerderkennz=k.split('/')[-1], einrichtung='', land='AT')
for fp in ('h2020', 'he', 'fp7'):
    coord = {}
    for r in csv.DictReader(open(f'{R}cordis/{fp}/organization.csv', newline='', encoding='utf-8'), delimiter=';'):
        if r.get('role') == 'coordinator': coord[r['projectID']] = (r.get('name', ''), r.get('country', ''))
    for r in csv.DictReader(open(f'{R}cordis/{fp}/project.csv', newline='', encoding='utf-8'), delimiter=';'):
        if r['id'] in want:
            n, c = coord.get(r['id'], ('', ''))
            out[r['id']] = dict(titel=r['title'], ziel=r['objective'][:600], ab=r['endDate'][:4], foerderkennz='', einrichtung=n, land=c if len(c) == 2 else '')
for r in csv.DictReader(open(R + 'sbir.csv', encoding='utf-8', errors='replace')):
    k = r['Agency Tracking Number'] or r['Contract']
    if k in want:
        out[k] = dict(titel=r['Award Title'], ziel=r['Abstract'][:600], ab=r['Award Year'], foerderkennz='', einrichtung=r['Company'], land='US')
for l in open(R + 'riv/riv_applied.jsonl'):
    r = json.loads(l)
    if r['kod_vysledku'] in want:
        out[r['kod_vysledku']] = dict(titel=r['nazev_v_puvodnim_jazyce'], ziel=(r['popis_vysledku_anglicky'] or r['popis_vysledku_v_puv._jazyce'])[:600],
                                     ab=r['rok_uplatneni'], foerderkennz='', einrichtung=r['nazev_organizace'], land='CZ')
with open(dst, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'titel', 'ziel', 'ab', 'foerderkennz', 'einrichtung', 'land'])
    w.writeheader()
    for k in ids:
        if k in out: w.writerow(dict(id=k, **out[k]))
print(f'{len(out)} von {len(ids)} gefunden; fehlend: {[k for k in ids if k not in out]}')
