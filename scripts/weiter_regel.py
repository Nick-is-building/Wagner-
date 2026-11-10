"""Weiter-Regel für Haiku v0.2 (A03). Kostenlos. Wird von scripts/bezahlt/haiku_v02.py und
scripts/haiku_v02_auswertung.py importiert; die Regel steht nur hier.

Weiter, wenn unerledigter_kern nicht "nein" ist UND mindestens eines gilt:
  technisches_hindernis ja/unklar, abbruchgrund_art Geld/Personal/Organisation,
  offener_schritt ja/unklar, rechenanteil hoch.
RIV-Einträge mit Nutzungscode O (druh_moznosti_vyuziti), Nachtrag A03: gehen an Haiku; Code O setzt
  offener_schritt auf "ja". Weiter nur, wenn die Regel oben gilt UND zusätzlich rechenanteil mittel/hoch
  oder technisches_hindernis ja/unklar. (Auslegung: Die Kern-Bedingung gilt auch hier, weil "Code O setzt
  offener_schritt auf ja" sonst keine Wirkung hätte.)
"unklar" ohne Zitat zählt als "nein" (Prompt-Regel v0.2, hier technisch durchgesetzt).
"""
import pickle

POS = {'ja', 'unklar'}
ART_WEITER = {'Geld', 'Personal', 'Organisation'}


def riv_o_ids(pfad='data/zwischen/newpools.pkl'):
    n = pickle.load(open(pfad, 'rb'))
    return {r['kod_vysledku'] for r in n['riv'] if r['druh_moznosti_vyuziti'] == 'O'}


def _wert(w, zitat):
    w = (w or '').strip().lower() if isinstance(w, str) else None
    if w == 'unklar' and not (zitat or '').strip():
        return 'nein'
    return w or 'nein'


def felder(a):
    """Bereinigte Werte einer Haiku-Antwort (dict) für die Regel."""
    k = a.get('unerledigter_kern') or {}
    art = a.get('abbruchgrund_art') or {}
    return {
        'kern': _wert(k.get('wert'), k.get('zitat')),
        'th': _wert(a.get('technisches_hindernis'), (a.get('hindernis') or {}).get('zitat')),
        'os': _wert(a.get('offener_schritt'), a.get('offener_schritt_beleg')),
        'art': art.get('wert') if (art.get('wert') != 'unklar' or (art.get('zitat') or '').strip()) else None,
        'rechen': (a.get('rechenanteil') or '').strip().lower(),
    }


def weiter(a, riv_o=False):
    """True/False und Liste der Gründe. riv_o=True für RIV-Einträge mit Nutzungscode O."""
    f = felder(a)
    if riv_o:
        f['os'] = 'ja'
    if f['kern'] == 'nein':
        return False, ['kern nein']
    g = []
    if f['th'] in POS: g.append(f"hindernis {f['th']}")
    if f['art'] in ART_WEITER: g.append(f"grund {f['art']}")
    if f['os'] in POS: g.append(f"offener schritt {f['os']}")
    if f['rechen'] == 'hoch': g.append('rechenanteil hoch')
    if riv_o:
        if not (f['rechen'] in ('mittel', 'hoch') or f['th'] in POS):
            return False, ['RIV O: weder rechenanteil mittel/hoch noch hindernis ja/unklar']
        g = ['RIV O'] + g
    return bool(g), g or [f"kern {f['kern']}, sonst nichts"]
