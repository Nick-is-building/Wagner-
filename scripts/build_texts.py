"""Texte v2 (A05): ein Text je Eintrag, höchstens rund 4.000 Zeichen, nicht mitten im Satz abgeschnitten.

Vorrang hat der Ausgang (CEP-Bewertung, FWF-Endbericht, CORDIS workPerformed/finalResults bzw. PoC-summary,
RIV-Nutzung und Parameter). Der Antrags- bzw. Zieltext bekommt den Rest, mindestens 800 Zeichen.
Wird ein Teil zu lang, bleiben zuerst Sätze mit Hindernis-Signal (early.OBSTRUE), dann der Rest in Reihenfolge.
Feld texttyp: 'ergebnis', wenn ein Ausgangstext vorliegt, sonst 'antrag'.
Gleiche Einträge und harte Frühfilter wie v1 (scripts/build_texts_v1.py).
Ausgabe: data/zwischen/items_v2.pkl (Liste von dicts) und Zählung je Pool und Texttyp.
"""
import collections, json, pickle, re, sys
sys.path.insert(0, 'scripts')
import early as E

MAX = 4000
MIN_ANTRAG = 800
clean = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s or '')).strip()
SATZ = re.compile(r'(?<=[.!?;])\s+')


def kuerze(text, n):
    """Höchstens n Zeichen aus ganzen Sätzen; Sätze mit Hindernis-Signal zuerst, Ausgabe in Originalreihenfolge."""
    text = clean(text)
    if len(text) <= n: return text
    s = SATZ.split(text)
    wahl, rest = set(), n
    for pri in (True, False):
        for i, x in enumerate(s):
            if i in wahl or bool(E.OBSTRUE.search(x)) != pri: continue
            if len(x) + 1 <= rest: wahl.add(i); rest -= len(x) + 1
    if not wahl:  # ein einziger Riesensatz
        return text[:n].rsplit(' ', 1)[0] + ' …'
    out, last = [], -1
    for i in sorted(wahl):
        if last >= 0 and i != last + 1: out.append('…')
        out.append(s[i]); last = i
    if last != len(s) - 1: out.append('…')
    return ' '.join(out)


def baue(uid, pool, titel, antrag, ausgang, meta=None):
    titel, antrag, ausgang = clean(titel), clean(antrag), clean(ausgang)
    platz = MAX - len(titel) - 40
    a_n = min(len(antrag), max(MIN_ANTRAG, platz - len(ausgang)))
    g_n = platz - a_n
    a, g = kuerze(antrag, a_n), kuerze(ausgang, g_n)
    teile = [titel]
    if a: teile.append('[Ziel/Antrag] ' + a)
    if g: teile.append('[Ausgang] ' + g)
    return {'id': uid, 'pool': pool, 'titel': titel, 'texttyp': 'ergebnis' if g else 'antrag',
            'text': '\n'.join(teile), 'meta': meta or {}}


items = []
d = E.d
for r in d['cep_fail'] + d['cep_pos']:
    if E.cep_hard(r): continue
    pool = 'cep_fail' if r in d['cep_fail'] else 'cep_pos'
    g = r['slovni_hodnoceni_cesky']
    if clean(g): g = f"Bewertung {r['kod_hodnoceni']}: {g}"
    items.append(baue(r['kod_projektu'], pool, r['nazev_projektu_originalni'], r['cile_reseni_originalni'], g,
                      {'kod_hodnoceni': r['kod_hodnoceni']}))
for pool in ('fwf_obst', 'fwf_pos'):
    for r in d[pool]:
        items.append(baue(r['_str.grantdoi'], pool, r['_str.projecttitle.en'], r.get('_str.prproposalsummary.en'),
                          r.get('_str.prfinalreport.en')))
for r in d['sbir']:
    if E.sb_hard(r): continue
    items.append(baue(r['Agency Tracking Number'] or r['Contract'], 'sbir1', r['Award Title'], r['Abstract'], '',
                      {'phase': r['Phase'], 'jahr': r['Award Year'], 'agentur': r['Agency']}))
for r in d['gw']:
    if E.gw_hard(r): continue
    items.append(baue(r['Award ID'], 'gw', r['Grant Title'], r['Grant Abstract'], ''))
n = pickle.load(open('data/zwischen/newpools.pkl', 'rb'))
ber = {}
for l in open('data/zwischen/cordis_berichte.jsonl', encoding='utf-8'):
    b = json.loads(l); ber[b['projectID']] = b
for pool in ('poc', 'sme1_noP2', 'sme2'):
    for r in n[pool]:
        b = ber.get(r['id'])
        g = ''
        if b:
            if (b['workPerformed'] + b['finalResults']).strip():
                g = 'Durchgeführte Arbeiten: ' + clean(b['workPerformed']) + ' Ergebnisse: ' + clean(b['finalResults'])
            else:
                g = b['summary']  # H2020-PoC: der Abschlussbericht hat nur summary
        items.append(baue(r['id'], pool, r['title'], r['objective'], g,
                          {'bericht_periode': b['periode'] if b else None}))
for r in n['sbir2']:
    items.append(baue(r['Agency Tracking Number'] or r['Contract'], 'sbir2', r['Award Title'], r['Abstract'], '',
                      {'phase': r['Phase'], 'jahr': r['Award Year'], 'agentur': r['Agency']}))
for r in n['riv']:
    if not (r['_unused'] or r['_opencue']): continue
    g = ' '.join(x for x in (
        f"Nutzungsart {r['druh_moznosti_vyuziti']}.",
        'Technische Parameter: ' + clean(r['technicke_parametry']) if clean(r['technicke_parametry']) else '',
        'Nutzung: ' + clean(r['zpusoby_vyuziti_vysledku']) if clean(r['zpusoby_vyuziti_vysledku']) else '',
        'Wirtschaftliche Parameter: ' + clean(r['ekonomicke_parametry']) if clean(r['ekonomicke_parametry']) else '') if x)
    items.append(baue(r['kod_vysledku'], 'riv', r['nazev_v_puvodnim_jazyce'], r['popis_vysledku_v_puv._jazyce'], g,
                      {'druh_moznosti_vyuziti': r['druh_moznosti_vyuziti'], 'druh': r['druh']}))

pickle.dump(items, open('data/zwischen/items_v2.pkl', 'wb'))
c = collections.Counter((i['pool'], i['texttyp']) for i in items)
laenge = collections.defaultdict(list)
for i in items: laenge[i['pool']].append(len(i['text']))
print(f'{len(items)} Einträge → data/zwischen/items_v2.pkl')
print(f"{'Pool':<11}{'ergebnis':>9}{'antrag':>8}{'gesamt':>8}{'Ø Zeichen':>11}")
for p in sorted(laenge, key=lambda p: -len(laenge[p])):
    print(f"{p:<11}{c[(p, 'ergebnis')]:>9}{c[(p, 'antrag')]:>8}{len(laenge[p]):>8}{sum(laenge[p]) // len(laenge[p]):>11}")
t = collections.Counter(i['texttyp'] for i in items)
print(f"{'gesamt':<11}{t['ergebnis']:>9}{t['antrag']:>8}{len(items):>8}{sum(len(i['text']) for i in items) // len(items):>11}")
