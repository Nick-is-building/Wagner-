"""Kostenrechner A06 (kostenlos, sendet nichts). Listenpreise aus scripts/bezahlt/api_lauf.py (PREISE), kein Batch.

Aufruf: python3 scripts/kosten.py
Je Schritt: Anzahl Aufrufe × Kosten je Aufruf. Kosten je Aufruf werden aus vorhandenen Ausgabedateien gemessen
(Mittel von _kosten_usd), sonst aus Textlängen geschätzt (2,1 Zeichen je Token). Die Annahmen stehen in der Ausgabe.
"""
import json, os, sys, statistics
sys.path.insert(0, 'scripts/bezahlt')
import api_lauf as L


def gemessen(pfad):
    if not os.path.exists(pfad):
        return None
    k = [json.loads(l).get('_kosten_usd') for l in open(pfad, encoding='utf-8')]
    k = [x for x in k if x]
    return (statistics.mean(k), len(k)) if k else None


def zeilen(pfad):
    return sum(1 for _ in open(pfad, encoding='utf-8')) if os.path.exists(pfad) else 0


def mittel_zeichen(pfad):
    if not os.path.exists(pfad):
        return 2300
    t = [len(json.loads(l)['text']) for l in open(pfad, encoding='utf-8')]
    return statistics.mean(t)


def zeile(name, n, je, quelle, grenze):
    ges = n * je
    print(f'{name:<38} {n:>5} × {je:.4f} $ = {ges:7.3f} $  (Grenze {grenze} $; {quelle})')


h_pin, h_pout = L.PREISE['claude-haiku-5-5']
s_pin, s_pout = L.PREISE['claude-sonnet-5-5']
f_pin, f_pout = L.PREISE['claude-fable-5-2']

# Haiku: System rund 4.000 Zeichen + Text; Ausgabe 220 Token
for satz, grenze in (('pruefset', '0,50 gemeinsam mit zufall'), ('zufall', '0,50 gemeinsam'), ('haeppchen1', '2,00')):
    ein = f'ergebnisse/a06_{satz}_eingabe.jsonl'
    m = gemessen(f'ergebnisse/haiku_v03_{satz}.jsonl') or gemessen('ergebnisse/haiku_v03_pruefset.jsonl')
    if m:
        zeile(f'Haiku v0.3 {satz}', zeilen(ein), m[0], f'gemessen an {m[1]} Aufrufen', grenze)
    else:
        je = (L.tok('x' * 4000) + L.tok('x' * int(mittel_zeichen(ein)))) * h_pin / 1e6 + 220 * h_pout / 1e6
        zeile(f'Haiku v0.3 {satz}', zeilen(ein), je, 'geschätzt', grenze)

# Sonnet: Katalog (rund 14.000 Zeichen) zwischengespeichert, Anweisung 4.500 Zeichen, Text + Haiku 3.000 Zeichen, Ausgabe 650 Token
m = gemessen('ergebnisse/sonnet_v02_pruefset.jsonl')
if m:
    je_s, q = m[0], f'gemessen an {m[1]} Aufrufen'
else:
    je_s = (L.tok('x' * 14000) * s_pin * 0.1 + L.tok('x' * 7500) * s_pin + 650 * s_pout) / 1e6
    q = 'geschätzt, ohne Denken, Katalog aus Zwischenspeicher'
zeile('Sonnet v0.2 Prüfset', zeilen('ergebnisse/a06_pruefset_eingabe.jsonl'), je_s, q, '2,00')
print(f'{"Sonnet v0.2 Häppchen 1: höchstens":<38} {int(5.0 / je_s):>5} Einträge bei 5,00 $ ({q})')

# Fable: Tiefenprüfung je Kandidat rund 15.000 Token Material + bis 5 Websuchen (Ergebnisse rund 25.000 Token),
# Ausgabe mit Denken rund 6.000 Token; freie Suche: 100 Kandidaten × 900 Token + 20.000 Token Ausgabe
m = gemessen('ergebnisse/fable_a06_tiefe.jsonl')
je_f = m[0] if m else (40000 * f_pin + 6000 * f_pout) / 1e6 + 5 * L.WEBSUCHE_USD
zeile('Fable 5.2 Tiefenprüfung', 30, je_f, f'gemessen an {m[1]}' if m else 'geschätzt, Annahme siehe Code', '8,00 gemeinsam')
frei = (100 * 900 + 12000) * f_pin / 1e6 + 20000 * f_pout / 1e6
zeile('Fable 5.2 freie Suche (ein Aufruf)', 1, frei, 'geschätzt', '8,00 gemeinsam')
