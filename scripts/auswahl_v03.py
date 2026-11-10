"""Auswahlregel für Haiku v0.3 (A06). Kostenlos. Die Regel steht nur hier.

Ergebnis-Texte: weiter, wenn mindestens eines gilt
  - hindernis ja/unklar und hindernis_quelle ergebnis/unklar
  - abbruchgrund Geld, Personal, Organisation oder Aufwand; Technik nur, wenn hindernis_quelle nicht "motivation"
  - offener_schritt ja/unklar
  "unklar" ohne irgendein Zitat in der Antwort zählt als "nein" (wie v0.2).
Antrags-Texte: Rangliste nach (H1–H3 im Kernrisiko, Rechenanteil, erster Schritt).
Labor, Reinraum, Zulassung als erster Schritt: nach hinten (nicht gelöscht).
Rang für alle (Sortierung vor Sonnet): Schlüssel `rang` (größer = weiter oben); für Ergebnis-Texte dieselbe Rangfolge
wie für Anträge (H1–H3, Rechenanteil, erster Schritt), Gleichstände nach Hindernis aus dem Ausgang, Kern offen usw.

Aufruf: python3 scripts/auswahl_v03.py SATZ   (pruefset | zufall | haeppchen1)
Schreibt ergebnisse/auswahl_v03_<satz>.tsv und ergebnisse/zitat_check_v03_<satz>.jsonl, druckt Zusammenfassung.
"""
import json, re, sys, unicodedata, collections, csv

POS = {'ja', 'unklar'}
GRUND_AUSSEN = {'Geld', 'Personal', 'Organisation', 'Aufwand'}
H13 = {'H1', 'H2', 'H3'}
RECHEN = {'hoch': 3, 'mittel': 2, 'unklar': 1, 'niedrig': 0}
SCHRITT = {'software': 3, 'simulation': 3, 'datenanalyse': 3, 'prototyp_klein': 2, 'unklar': 1,
           'labor': -3, 'reinraum': -3, 'zulassung': -3}
HINTEN = {'labor', 'reinraum', 'zulassung'}
ZITATFELDER = ('hindernis_zitat', 'abbruchgrund_zitat', 'offener_schritt_zitat', 'kernrisiko_zitat')


def _w(x):
    return (x or '').strip().lower() if isinstance(x, str) else ''


def bewerte(a, texttyp):
    """-> dict mit weiter (bool, nur ergebnis), gruende, rang (Zahl), hinten (bool)."""
    z = any((a.get(k) or '').strip() for k in ZITATFELDER)
    w = lambda k: ('nein' if _w(a.get(k)) == 'unklar' and not z else _w(a.get(k)))
    muster = set(a.get('muster') or [])
    rechen = _w(a.get('rechenanteil'))
    schritt = _w(a.get('erster_schritt')) or 'unklar'
    hinten = schritt in HINTEN
    basis = 10 * bool(muster & H13) + 3 * RECHEN.get(rechen, 1) + 2 * SCHRITT.get(schritt, 1)
    if texttyp == 'antrag':
        return {'weiter': None, 'gruende': ['antrag'], 'rang': basis - (100 if hinten else 0), 'hinten': hinten}
    g = []
    q = _w(a.get('hindernis_quelle'))
    if w('hindernis') in POS and q in ('ergebnis', 'unklar', ''):
        g.append(f"hindernis {w('hindernis')}/{q or 'ohne quelle'}")
    grund = (a.get('abbruchgrund') or '').strip()
    if grund in GRUND_AUSSEN or (grund == 'Technik' and q != 'motivation'):
        g.append(f'grund {grund}')
    if w('offener_schritt') in POS:
        g.append(f"offener schritt {w('offener_schritt')}")
    # Entscheidung Nick (A06, Haltepunkt Phase 3): gleiche Rangfolge wie Antrags-Texte (basis); die übrigen Signale
    # brechen nur Gleichstände (je höchstens 0,9 Punkte zusammen, kleiner als jeder Schritt in basis)
    neben = 0.4 * (q == 'ergebnis' and w('hindernis') == 'ja') + 0.2 * (w('kern_offen') == 'ja') \
        + 0.15 * (w('offener_schritt') == 'ja') + 0.15 * (grund in GRUND_AUSSEN)
    rang = basis + neben - (100 if hinten else 0)
    return {'weiter': bool(g), 'gruende': g or ['nichts'], 'rang': rang, 'hinten': hinten}


def norm(s):
    s = unicodedata.normalize('NFKC', s or '').lower()
    s = re.sub(r'[„“”"‚‘’\'«»]', '', s)
    s = s.replace('…', '...')
    return re.sub(r'\s+', ' ', s).strip()


def zitate_ok(a, text):
    t = norm(text)
    fehl = []
    for k in ZITATFELDER:
        v = a.get(k)
        if v:
            teile = [p.strip(' .') for p in norm(v).split('...') if p.strip(' .')]
            if any(p not in t for p in teile):
                fehl.append(k)
    return fehl


def lade(satz):
    ein = {json.loads(l)['id']: json.loads(l) for l in open(f'ergebnisse/a06_{satz}_eingabe.jsonl', encoding='utf-8')}
    aus = {}
    for l in open(f'ergebnisse/haiku_v03_{satz}.jsonl', encoding='utf-8'):
        z = json.loads(l)
        if '_fehler' not in z:
            aus[z['id']] = z
    return ein, aus


def auswerten(satz):
    ein, aus = lade(satz)
    zeilen = []
    zc = open(f'ergebnisse/zitat_check_v03_{satz}.jsonl', 'w', encoding='utf-8')
    for i, r in ein.items():
        if i not in aus:
            zeilen.append({'id': i, 'pool': r['pool'], 'texttyp': r['texttyp'], 'klasse': r.get('klasse', ''),
                           'weiter': '', 'rang': '', 'gruende': 'keine Haiku-Antwort', 'hinten': '', 'zitat': ''})
            continue
        b = bewerte(aus[i], r['texttyp'])
        fehl = zitate_ok(aus[i], r['titel'] + ' ' + r['text'])
        zc.write(json.dumps({'id': i, 'status': 'nachpruefen' if fehl else 'ok', 'felder_ohne_beleg': fehl}, ensure_ascii=False) + '\n')
        zeilen.append({'id': i, 'pool': r['pool'], 'texttyp': r['texttyp'], 'klasse': r.get('klasse', ''),
                       'weiter': b['weiter'], 'rang': b['rang'], 'gruende': '; '.join(b['gruende']),
                       'hinten': b['hinten'], 'zitat': 'nachpruefen' if fehl else 'ok'})
    zc.close()
    # Antrags-Rangliste: Position (oberes Viertel)
    ant = sorted([z for z in zeilen if z['texttyp'] == 'antrag' and z['rang'] != ''], key=lambda z: -z['rang'])
    for pos, z in enumerate(ant, 1):
        z['antrag_pos'] = f'{pos}/{len(ant)}'
        z['oberes_viertel'] = pos <= max(1, round(len(ant) / 4))
    with open(f'ergebnisse/auswahl_v03_{satz}.tsv', 'w', encoding='utf-8', newline='') as f:
        felder = ['id', 'pool', 'texttyp', 'klasse', 'weiter', 'antrag_pos', 'oberes_viertel', 'rang', 'hinten', 'zitat', 'gruende']
        w = csv.DictWriter(f, fieldnames=felder, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(zeilen)
    return zeilen


def durch(z):
    return z['weiter'] is True or z.get('oberes_viertel') is True


if __name__ == '__main__':
    satz = sys.argv[1]
    zs = auswerten(satz)
    print(f'{satz}: {len(zs)} Einträge, Haiku-Antworten {sum(z["rang"] != "" for z in zs)}')
    print('Zitate nachprüfen:', sum(z['zitat'] == 'nachpruefen' for z in zs))
    if satz == 'pruefset':
        for kl in ('gut', 'gut (schon weitergeführt)', 'grenzfall', 'ungeeignet'):
            g = [z for z in zs if z['klasse'] == kl]
            d = [z for z in g if durch(z)]
            print(f'{kl}: {len(d)}/{len(g)} durch')
            if kl in ('gut', 'grenzfall'):
                for z in g:
                    if not durch(z):
                        print(f"   nicht durch: {z['id']} {z['pool']} {z['texttyp']} rang {z['rang']} {z.get('antrag_pos','')} {z['gruende']}")
    p = collections.defaultdict(lambda: [0, 0])
    for z in zs:
        p[(z['pool'], z['texttyp'])][1] += 1; p[(z['pool'], z['texttyp'])][0] += durch(z)
    print('Durchlass je Pool (weiter oder oberes Viertel / alle):', {f'{k[0]}/{k[1]}': f'{v[0]}/{v[1]}' for k, v in sorted(p.items())})
    print('Erster Schritt Labor/Reinraum/Zulassung (nach hinten):', sum(z['hinten'] is True for z in zs))
