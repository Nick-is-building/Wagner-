"""A05 Phase 2: Erst- und Zweitbewertung zusammenführen → pruefset/a05_neue_eintraege.csv (Format wie pruefset.csv).
Regel aus dem Auftrag: Sind beide uneins, wird es ein Grenzfall. Alles „vorläufig, Doppelbewertung Claude“."""
import csv, json, re
def lese(p):
    d = {}
    for l in open(p, encoding='utf-8'):
        m = re.match(r'\|\s*(V\d\d)\s*\|\s*([^|]+?)\s*\|\s*(gut|grenzfall|ungeeignet)\s*\|\s*([^|]*?)\s*\|\s*(.*?)\s*\|\s*$', l, re.I)
        if m: d[m.group(1)] = (m.group(3).lower(), m.group(4), m.group(5))
    return d
a = lese('pruefset/a05_erstbewertung.md'); b = lese('pruefset/a05_zweitbewertung.md'); b.update(lese('pruefset/a05_zweitbewertung_2.md'))
vor = {f"V{json.loads(l)['nr']:02d}": json.loads(l) for f in ('pruefset/a05_vorschlaege.jsonl', 'pruefset/a05_vorschlaege_2.jsonl') for l in open(f, encoding='utf-8')}
QUELLE = {'poc': 'CORDIS ERC-PoC', 'sme1_noP2': 'CORDIS SME-1', 'sme2': 'CORDIS SME-2', 'sbir1': 'SBIR', 'sbir2': 'SBIR', 'riv': 'RIV',
          'fwf_obst': 'FWF', 'fwf_pos': 'FWF', 'cep_fail': 'CEP', 'cep_pos': 'CEP', 'gw': 'Grant Witness'}
RUECK = {'0810523': 'Rückblick-Kandidat: OpenAlex findet 2019 „Hand-and-finger-awareness … using deep learning“ (ergebnisse/a05_rueckblick_openalex.jsonl), nicht geprüft'}
with open('pruefset/a05_neue_eintraege.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['id', 'quelle', 'klasse', 'herkunft', 'begruendung'])
    for k in sorted(vor):
        v = vor[k]; x, y = a[k][0], b[k][0]
        kl = x if x == y else 'grenzfall'
        grund = f"vorläufig, Doppelbewertung Claude (Erst: {x}, Zweit: {y}{', uneins → grenzfall' if x != y else ''}); {a[k][1] or '–'}; {a[k][2]}"
        if v['id'] in RUECK: grund += ' ' + RUECK[v['id']]
        w.writerow([v['id'], QUELLE[v['pool']], kl, f"A05 {k} ({v['pool']}, {v['texttyp']}, {v['ziehung']})", grund])
        print(f"{k} | {v['id']} | {v['pool']} | {v['texttyp']} | {kl}{' (uneins: '+x+'/'+y+')' if x != y else ''} | {a[k][2][:95]}")
