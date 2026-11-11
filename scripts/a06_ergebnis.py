"""A06 Phase 8 (kostenlos): kandidaten/RANGLISTE.md (obere 30), Karten für die oberen 10, kandidaten/beobachtungen.md.
Quellen: ergebnisse/a06_obere100.jsonl, ergebnisse/fable_a06_tiefe.jsonl, ergebnisse/fable_a06_frei.jsonl.
Karten: kandidaten/<ID, / durch - ersetzt>.md nach kandidaten/_VORLAGE.md; INDEX.md bekommt je Karte eine Zeile.
"""
import json, os, re
ks = [json.loads(l) for l in open('ergebnisse/a06_obere100.jsonl', encoding='utf-8')]
fb = {}
for l in open('ergebnisse/fable_a06_tiefe.jsonl', encoding='utf-8'):
    z = json.loads(l)
    if '_fehler' not in z:
        fb[z['id']] = z
frei = json.loads(open('ergebnisse/fable_a06_frei.jsonl', encoding='utf-8').readline())
DATUM = '2026-11-11'
kurz = lambda s, n=90: (s or '').replace('|', '/').replace('\n', ' ')[:n]


def g(d, *ks):
    for k in ks:
        d = (d or {}).get(k) if isinstance(d, dict) else None
    return d


zeilen = ['# Rangliste Häppchen 1 (A06)', '',
          f'Stand {DATUM}. Obere 30 nach Sonnet-Summe (Höchstwert 42, geeichte Startschwelle 17; Pflicht = Markierung, '
          'siehe `pruefset/sonnet_test_v02_2026-11-10.md`). Fable-Tiefenprüfung für die Kandidaten mit Urteil; '
          'die übrigen passten nicht in die Freigabe A06e. Vorteil und erster Schritt von Fable, sonst von Sonnet (markiert „S:“).', '',
          '| # | ID | Pool | Kurztitel | Punkte | Pflicht | eigenständiger Vorteil | erster Schritt | Fable-Urteil |',
          '|---|---|---|---|---|---|---|---|---|']
for k in ks[:30]:
    s, f = k['sonnet'], fb.get(k['id'])
    if f:
        vort, schritt = g(f, 'vorteil', 'satz'), f"{g(f, 'erster_schritt', 'satz')} (~{g(f, 'erster_schritt', 'kosten_eur')} €)"
        urteil, titel = f.get('urteil'), f.get('kurztitel') or k['titel']
    else:
        vort, schritt = 'S: ' + (g(s, 'vorteil', 'satz') or '–'), 'S: ' + (g(s, 'erster_schritt', 'satz') or '–')
        urteil, titel = 'nicht geprüft (Budget)', k['titel']
    zeilen.append(f"| {k['rang']} | {k['id']} | {k['pool']} | {kurz(titel, 50)} | {s['summe']} | "
                  f"{'ja' if s.get('pflicht_erfuellt') else 'nein'} | {kurz(vort, 110)} | {kurz(schritt, 110)} | {kurz(urteil, 120)} |")
fbs = [z for z in fb.values() if z.get('_fallback')]
zeilen += ['', f"Fable-Tiefenprüfungen: {len(fb)}. Ausweichen auf ein anderes Modell (Biologie-Filter u. a.): "
           f"{', '.join(z['id'] + ' ' + str(z['_fallback']) for z in fbs) if fbs else 'keines'}."]
open('kandidaten/RANGLISTE.md', 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')

index = open('kandidaten/INDEX.md', encoding='utf-8').read()
neu_index = []
for k in ks[:10]:
    f, s = fb.get(k['id']), k['sonnet']
    if not f:
        continue
    datei = 'kandidaten/' + k['id'].replace('/', '-') + '.md'
    zit = g(k, 'haiku', 'hindernis_zitat') or g(s, 'k1', 'zitat') or 'kein Zitat'
    hm = f.get('heilmeier') or []
    quellen = '\n'.join(f'- {u}' for u in f.get('_quellen', [])) or '- keine'
    karte = f"""# {k['id']}: {f.get('kurztitel') or k['titel']}

Quelle: {k['pool']} · Originaltitel: {k['titel']} · Stand: {DATUM} · Punkte Stufe 3: {s['summe']}/42 (Pflicht {'ja' if s.get('pflicht_erfuellt') else 'nein'}) · Rang {k['rang']} in Häppchen 1

Erstellt aus der Fable-5.2-Tiefenprüfung (A06 Phase 7a, `ergebnisse/fable_a06_tiefe.jsonl`; antwortendes Modell: {g(f, '_usage', 'modell')}). Vorläufig, nicht von Hand geprüft.

## In einem Satz

{g(s, 'k1', 'satz')} Urteil Fable: {f.get('urteil')}

## Belege

| Feld | Inhalt | Beleg |
|---|---|---|
| Damals | {kurz(g(s, 'k1', 'satz'), 200)} | „{kurz(zit, 200)}“ |
| Heute | {kurz(g(f, 'heute', 'entwicklung'), 200)} | {g(f, 'heute', 'url')} |
| Markt | {kurz(g(f, 'markt', 'wer'), 200)} | {g(f, 'markt', 'url')} |
| Offen | {kurz(g(f, 'annahme', 'satz'), 200)} | Test: {kurz(g(f, 'annahme', 'test'), 200)} |
| Eigenständiger Vorteil | {kurz(g(f, 'vorteil', 'satz'), 200)} | „{kurz(g(f, 'vorteil', 'zitat'), 200)}“ |

## Noch offen?

{g(f, 'noch_offen', 'stand')}: {g(f, 'noch_offen', 'beleg')} {g(f, 'noch_offen', 'url') or ''}

OpenAlex (schnell): {kurz(json.dumps(k.get('openalex') or {}, ensure_ascii=False), 400)}

## Rechte und Unterlagen

{f.get('rechte_unterlagen')}

## Erster Schritt

{g(f, 'erster_schritt', 'satz')} Kosten rund {g(f, 'erster_schritt', 'kosten_eur')} €, Dauer rund {g(f, 'erster_schritt', 'dauer_wochen')} Wochen.

## Heilmeier-Fragen

""" + '\n'.join(f'{i}. {re.sub(r"^[0-9]+[.)]? *", "", h)}' for i, h in enumerate(hm, 1)) + f"""

## Gewicht

- Stärkstes Argument dafür: {f.get('dafuer')}
- Stärkstes Argument dagegen: {f.get('dagegen')}

## Quellen aus Fables Websuche

{quellen}

## Gegengutachten

Noch nicht erstellt (nicht Teil von A06).
"""
    open(datei, 'w', encoding='utf-8').write(karte)
    if datei.split('/')[-1] not in index:
        neu_index.append(f"| {k['id']} | {kurz(f.get('kurztitel') or k['titel'], 60)} | {k['pool']} | {s['summe']}/42 | "
                         f"Fable: {g(f, 'noch_offen', 'stand')} | Tiefenprüfung ({kurz(f.get('urteil'), 60)}) | {datei.split('/')[-1]} |")
if neu_index:
    kopf = '|---|---|---|---|---|---|---|\n'
    open('kandidaten/INDEX.md', 'w', encoding='utf-8').write(index.replace(kopf, kopf + '\n'.join(neu_index) + '\n', 1))

b = f"""# Beobachtungen aus Häppchen 1 (A06 Phase 7b)

Fable 5.2, ein Aufruf über die oberen 100 (`ergebnisse/fable_a06_frei.jsonl`, antwortendes Modell {g(frei, '_usage', 'modell')}, Kosten {frei['_kosten_usd']:.2f} $, ohne Websuche).
Alles unten ist **Vermutung** von Fable, nicht von Hand geprüft. Zitate und IDs stammen aus dem Material, das Fable bekam.
Hinweis zum Auftrag: Fable weicht bei Biologie-Themen auf ältere Modelle aus. In diesem Aufruf {'gab es ein Ausweichen: ' + str(frei.get('_fallback')) if frei.get('_fallback') else 'gab es kein Ausweichen'}.

{frei['text']}
"""
open('kandidaten/beobachtungen.md', 'w', encoding='utf-8').write(b)
print(f'RANGLISTE: 30 Zeilen, {sum(k["id"] in fb for k in ks[:30])} mit Fable-Urteil; Karten neu: {len(neu_index)}; beobachtungen.md geschrieben')
