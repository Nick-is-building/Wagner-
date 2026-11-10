"""Kostenschätzung Sonnet-Lauf je Schwelle (A04). Kostenlos, kein API-Aufruf.

Token: Zeichen je Token geeicht an den echten Eingabe-Token der Haiku-v0.2-Läufe (_usage.in gegen
Zeichen von Systemanweisung + Nutzertext). Annahme: Sonnet zählt ähnlich wie Haiku.
Fester Teil: Systemanweisung + Antwortschema aus prompts/sonnet_bewertung.md + Katalog-Abschnitte
Querschnitt, Fachgebiete, Übersetzungstabelle, Grenzen (docs/03_faehigkeiten_katalog.md).
Variabler Teil: Eintragstext wie bei Haiku + Haiku-Antwort als JSON (ohne _-Felder).
Preise Sonnet 5.5 (A04): 2 $ / 10 $ je Mio Token; Batch -50 %; Cache-Lesen 10 % des Eingabepreises.
Cache-Schreiben ist nicht eingerechnet (einmalig je Cache-Zeitfenster, klein).
"""
import json, re, csv, sys
sys.path.insert(0, 'scripts/bezahlt')
import importlib.util
spec = importlib.util.spec_from_file_location('h', 'scripts/bezahlt/haiku_v02.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)

N = 17421
P_IN, P_OUT, CACHE = 2.0, 10.0, 0.10

# Eichung
sysm = h.systemanweisung()
ein = {}
for p in ('ergebnisse/pruefset_eingabe.jsonl', 'ergebnisse/zufall100_eingabe.jsonl'):
    for l in open(p, encoding='utf-8'):
        r = json.loads(l); ein[r['id']] = r
zeichen = token = 0
for p in ('ergebnisse/haiku_v02_pruefset.jsonl', 'ergebnisse/haiku_v02_zufall.jsonl'):
    for l in open(p, encoding='utf-8'):
        a = json.loads(l)
        if '_usage' in a:
            zeichen += len(sysm) + len(h.nutzertext(ein[a['id']])); token += a['_usage']['in']
zjt = zeichen / token
print(f'Eichung: {zeichen:,} Zeichen / {token:,} Token = {zjt:.2f} Zeichen je Token (146 Haiku-Aufrufe)')

# Fester Teil
md = open('prompts/sonnet_bewertung.md', encoding='utf-8').read()
anw = re.search(r'## Systemanweisung\s+```\n(.*?)\n```', md, re.S).group(1)
schema = re.search(r'## Antwortschema\s+```json\n(.*?)\n```', md, re.S).group(1)
kat = open('docs/03_faehigkeiten_katalog.md', encoding='utf-8').read()
abschn = ''.join(re.search(rf'(## {t}.*?)(?=\n## )', kat, re.S).group(1) for t in
                 ('Querschnitts-Fähigkeiten', 'Fähigkeiten je Fachgebiet', 'Übersetzungstabelle', 'Grenzen'))
fest = (len(anw) + len(schema) + len(abschn)) / zjt
print(f'Fester Teil: Anweisung {len(anw):,} + Schema {len(schema):,} + Katalog {len(abschn):,} Zeichen = rund {fest:,.0f} Token')

# Variabler Teil: Mittel über die 100 Zufallseinträge
var = []
for l in open('ergebnisse/haiku_v02_zufall.jsonl', encoding='utf-8'):
    a = json.loads(l)
    hj = json.dumps({k: v for k, v in a.items() if not k.startswith('_')}, ensure_ascii=False)
    var.append((len(h.nutzertext(ein[a['id']])) + len(hj)) / zjt)
v = sum(var) / len(var)
hout = [json.loads(l)['_usage']['out'] for p in ('ergebnisse/haiku_v02_zufall.jsonl',) for l in open(p)]
print(f'Variabler Teil: im Mittel rund {v:,.0f} Token je Eintrag; Haiku-Ausgabe zum Vergleich im Mittel {sum(hout)/len(hout):,.0f} Token')

def kosten(n, aus):
    ohne = n * ((fest + v) * P_IN + aus * P_OUT) / 1e6
    mit = n * ((fest * CACHE + v) * P_IN + aus * P_OUT) / 1e6
    return ohne, mit

zeilen = [('S1 = S2 = 0 Punkte (v0.2)', 100), ('zum Vergleich: ab 1 Punkt', 70), ('ab 2 Punkten', 37), ('ab 3 Punkten', 13)]
print('\n| Schwelle | Anteil Zufall | Einträge (hochgerechnet) | Ausgabe je Eintrag | ohne Cache | mit Cache | Batch mit Cache |')
print('|---|---|---|---|---|---|---|')
for name, proz in zeilen:
    n = round(N * proz / 100)
    for aus in (600, 1000, 1500):
        o, m = kosten(n, aus)
        print(f'| {name} | {proz} von 100 | {n:,} | {aus} | {o:,.0f} $ | {m:,.0f} $ | {m/2:,.0f} $ |')
hk = [json.loads(l)['_kosten_usd'] for l in open('ergebnisse/haiku_v02_zufall.jsonl')]
print(f'\nVorstufe Haiku v0.2 auf alle {N:,}: im Mittel {sum(hk)/len(hk):.5f} $ je Eintrag -> rund {N*sum(hk)/len(hk):,.1f} $ (ohne Batch)')
