"""Varianten der Weiter-Regel für Haiku v0.2 (A03), nur zur Analyse; die gültige Regel steht in weiter_regel.py.
Kostenlos. Aufruf: python3 scripts/haiku_v02_varianten.py > ergebnisse/haiku_v02_varianten.txt
"""
import json, csv, sys
from collections import Counter
sys.path.insert(0, 'scripts')
import weiter_regel as W

ps = {r['id']: r['klasse'] for r in csv.DictReader(open('pruefset/pruefset.csv', encoding='utf-8'))}
o = W.riv_o_ids()
A = [json.loads(l) for l in open('ergebnisse/haiku_v02_pruefset.jsonl', encoding='utf-8')]
B = [json.loads(l) for l in open('ergebnisse/haiku_v02_zufall.jsonl', encoding='utf-8')]


def roh(a):
    return {'kern': (a.get('unerledigter_kern') or {}).get('wert') or 'nein', 'th': a.get('technisches_hindernis') or 'nein',
            'os': a.get('offener_schritt') or 'nein', 'art': (a.get('abbruchgrund_art') or {}).get('wert'),
            'rechen': a.get('rechenanteil') or ''}


def regel(f, riv, kern=True):
    if riv: f = dict(f, os='ja')
    if kern and f['kern'] == 'nein': return False
    g = f['th'] in W.POS or f['art'] in W.ART_WEITER or f['os'] in W.POS or f['rechen'] == 'hoch'
    if riv: g = g and (f['rechen'] in ('mittel', 'hoch') or f['th'] in W.POS)
    return g


V = {'1 Auftrag (Zitat-Pflicht im Skript, Kern-Bedingung)': lambda a, r: regel(W.felder(a), r),
     '2 ohne Zitat-Pflicht im Skript (Haikus Rohwerte)': lambda a, r: regel(roh(a), r),
     '3 ohne Kern-Bedingung': lambda a, r: regel(W.felder(a), r, False),
     '4 ohne beides': lambda a, r: regel(roh(a), r, False)}
for name, fn in V.items():
    c, n = Counter(), Counter()
    for a in A: k = ps[a['id']]; n[k] += 1; c[k] += fn(a, a['id'] in o)
    b = sum(fn(a, a['id'] in o) for a in B)
    print(f"{name}: gut {c['gut']}/{n['gut']}, Grenzfall {c['grenzfall']}/{n['grenzfall']}, "
          f"ungeeignet {c['ungeeignet']}/{n['ungeeignet']} | Zufall {b}/100")
