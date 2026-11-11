"""A07 Ergebnis (kostenlos): kandidaten/RANGLISTE_A07.md (obere 20), Karten für die von Fable geprüften,
kandidaten/beobachtungen_A07.md (freie Suche). Bestehende Karten aus A06 werden nicht überschrieben:
dort wird ein Abschnitt „A07-Prüfung“ angehängt (nur einmal).
Quellen: ergebnisse/a07_obere40.jsonl, ergebnisse/fable_a07_tiefe.jsonl, ergebnisse/fable_a07_frei.jsonl.
"""
import json, os
ks = [json.loads(l) for l in open('ergebnisse/a07_obere40.jsonl', encoding='utf-8')]
fb = {z['id']: z for z in map(json.loads, open('ergebnisse/fable_a07_tiefe.jsonl', encoding='utf-8')) if '_fehler' not in z}
frei = json.loads(open('ergebnisse/fable_a07_frei.jsonl', encoding='utf-8').readline())
DATUM = '2026-11-11'
kurz = lambda s, n=90: str(s or '–').replace('|', '/').replace('\n', ' ')[:n]


def g(d, *ks):
    for k in ks:
        d = d.get(k) if isinstance(d, dict) else None
    return d


def oa_kurz(k):
    o = k.get('openalex') or {}
    return o.get('hinweis') or o.get('fehler') or 'kein Ergebnis'


z = ['# Rangliste A07 (Muster-Suche, obere 20)', '',
     f'Stand {DATUM}. Vorauswahl aus Häppchen 1 (103, `ergebnisse/a07_vorauswahl.tsv`), Sonnet v0.3, nur mit Teilerfolg (K5 ≥ 1). '
     'Rangfolge nach Summe inkl. M (ja +4, teilweise +2) und Abzügen (−4 je Abzug). Pflicht-Nullen sind Spalte, kein Ausschluss '
     '(Nick, Haltepunkt 1). Fable-Tiefenprüfung für Rang 1–7; Rang 8 passte nicht mehr in die Freigabe A07b. Alle 98: `ergebnisse/a07_rangliste.tsv`.', '',
     '| # | ID | Pool | Titel | Summe | M | Pflicht-Nullen | Abzug/Ausschluss | OpenAlex (schnell) | Fable: weiterverfolgen |',
     '|---|---|---|---|---|---|---|---|---|---|']
for k in ks[:20]:
    s, f = k['sonnet'], fb.get(k['id'])
    ab = [x for x in ('fertiges_produkt', 'ausgruendung', 'kern_geloest') if g(s, 'abzug', x)] + ([s['ausschluss_liste']] if s.get('ausschluss_liste') else [])
    fu = f"**{f.get('weiterverfolgen')}**: {kurz(f.get('grund'), 110)}" if f else 'nicht geprüft'
    z.append(f"| {k['rang']} | {k['id']} | {k['pool']} | {kurz((f or {}).get('kurztitel') or k['titel'], 55)} | {s['summe']} | "
             f"{g(s, 'm', 'wert')} | {', '.join(k['pflicht_nullen']) or '–'} | {', '.join(ab) or '–'} | {kurz(oa_kurz(k), 60)} | {fu} |")
z += ['', '## Erster Schritt der Fable-geprüften', '', '| ID | erster Schritt | Kosten | Wochen | wer zahlt |', '|---|---|---|---|---|']
for k in ks:
    f = fb.get(k['id'])
    if f:
        z.append(f"| {k['id']} | {kurz(g(f, 'erster_schritt', 'satz'), 160)} | {g(f, 'erster_schritt', 'kosten_eur')} € | "
                 f"{g(f, 'erster_schritt', 'dauer_wochen')} | {kurz(g(f, 'erster_schritt', 'zahler'), 110)} |")
z += ['', '## Fable zu den Pflicht-Nullen von Sonnet', '', '| ID | Sonnet-Nullen | K2 richtig? | K11 richtig? | K12 richtig? |', '|---|---|---|---|---|']
for k in ks:
    f = fb.get(k['id'])
    if f:
        p = lambda x: f"{'ja' if g(f, 'pflicht', x, 'sonnet_richtig') else 'nein'}: {kurz(g(f, 'pflicht', x, 'grund'), 80)}"
        z.append(f"| {k['id']} | {', '.join(k['pflicht_nullen']) or 'keine'} | {p('k2')} | {p('k11')} | {p('k12')} |")
open('kandidaten/RANGLISTE_A07.md', 'w', encoding='utf-8').write('\n'.join(z) + '\n')

index = open('kandidaten/INDEX.md', encoding='utf-8').read()
neu_index, neu, ergaenzt = [], 0, 0
for k in ks:
    f, s = fb.get(k['id']), k['sonnet']
    if not f:
        continue
    datei = 'kandidaten/' + k['id'].replace('/', '-') + '.md'
    teil = f"""## A07-Prüfung ({DATUM}, Fable 5.2, Muster-Suche)

Rang {k['rang']} in A07 · Sonnet v0.3 Summe {s['summe']} · M: {g(s, 'm', 'wert')} · Pflicht-Nullen: {', '.join(k['pflicht_nullen']) or 'keine'} · Quelle `ergebnisse/fable_a07_tiefe.jsonl` (Modell {g(f, '_usage', 'modell')}). Vorläufig, nicht von Hand geprüft.

**Weiterverfolgen: {f.get('weiterverfolgen')}.** {f.get('grund')}

| Feld | Inhalt | Beleg |
|---|---|---|
| Muster | passt: {g(f, 'muster', 'passt')}. Vorhanden: {kurz(g(f, 'muster', 'vorhanden'), 160)}. Fehlt: {kurz(g(f, 'muster', 'fehlt'), 160)} | „{kurz(g(f, 'muster', 'zitat'), 200)}“ |
| Noch offen | {g(f, 'noch_offen', 'stand')}: {kurz(g(f, 'noch_offen', 'beleg'), 200)} | {g(f, 'noch_offen', 'url')} |
| Heute | {kurz(g(f, 'heute', 'entwicklung'), 200)} | {g(f, 'heute', 'url')} |
| Vorteil | {kurz(g(f, 'vorteil', 'satz'), 200)} | „{kurz(g(f, 'vorteil', 'zitat'), 200)}“ |
| Markt | {kurz(g(f, 'markt', 'wer'), 200)} | {g(f, 'markt', 'url')} |
| Offen | {kurz(g(f, 'annahme', 'satz'), 200)} | Test: {kurz(g(f, 'annahme', 'test'), 200)} |

**Erster Schritt:** {g(f, 'erster_schritt', 'satz')} Kosten rund {g(f, 'erster_schritt', 'kosten_eur')} €, rund {g(f, 'erster_schritt', 'dauer_wochen')} Wochen. Wer zahlt: {g(f, 'erster_schritt', 'zahler')} ({g(f, 'erster_schritt', 'zahler_url')})

**Pflicht-Nullen (Fable):** K2 {g(f, 'pflicht', 'k2', 'grund')} · K11 {g(f, 'pflicht', 'k11', 'grund')} · K12 {g(f, 'pflicht', 'k12', 'grund')}

Rechte und Unterlagen: {f.get('rechte_unterlagen')}

- Dafür: {f.get('dafuer')}
- Dagegen: {f.get('dagegen')}

OpenAlex (schnell): {oa_kurz(k)}

Quellen aus Fables Websuche:
""" + ('\n'.join(f'- {u}' for u in f.get('_quellen', [])) or '- keine') + '\n'
    if os.path.exists(datei):
        alt = open(datei, encoding='utf-8').read()
        if '## A07-Prüfung' not in alt:
            open(datei, 'a', encoding='utf-8').write('\n' + teil); ergaenzt += 1
    else:
        kopf = (f"# {k['id']}: {f.get('kurztitel') or k['titel']}\n\nQuelle: {k['pool']} · Originaltitel: {k['titel']} · Stand: {DATUM}\n\n"
                f"## In einem Satz\n\n{g(s, 'k1', 'satz')}\n\nZitat zum Hindernis: „{kurz(g(k, 'haiku', 'hindernis_zitat'), 300)}“\n\n")
        open(datei, 'w', encoding='utf-8').write(kopf + teil); neu += 1
    if datei.split('/')[-1] not in index:
        neu_index.append(f"| {k['id']} | {kurz(f.get('kurztitel') or k['titel'], 60)} | {k['pool']} | {s['summe']} (v0.3) | "
                         f"Fable: {g(f, 'noch_offen', 'stand')} | A07: weiterverfolgen {f.get('weiterverfolgen')} | {datei.split('/')[-1]} |")
if neu_index:
    t = '|---|---|---|---|---|---|---|\n'
    open('kandidaten/INDEX.md', 'w', encoding='utf-8').write(index.replace(t, t + '\n'.join(neu_index) + '\n', 1))
open('kandidaten/beobachtungen_A07.md', 'w', encoding='utf-8').write(
    f"# Beobachtungen A07 (freie Suche über die oberen 40)\n\nFable 5.2, ein Aufruf ohne Websuche (`ergebnisse/fable_a07_frei.jsonl`, "
    f"Modell {g(frei, '_usage', 'modell')}, {frei['_kosten_usd']:.2f} $). Alles unten ist **Vermutung** von Fable, nicht von Hand geprüft.\n\n{frei['text']}\n")
print(f'RANGLISTE_A07: 20 Zeilen; Karten neu {neu}, ergänzt {ergaenzt}; Index +{len(neu_index)}; beobachtungen_A07.md')
