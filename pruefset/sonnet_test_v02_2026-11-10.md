# Sonnet v0.2 am Prüfset (A06 Phase 5, Freigabe 2026-11-10-A06c)

Lauf 2026-11-10, `scripts/bezahlt/sonnet_v02.py --satz pruefset`: 101 Aufrufe, 0 Fehler, 35 s, 1,31 $ (0,013 $ je Eintrag). Ausgabe Median 626 Token; Katalog bei 86 von 101 Aufrufen aus dem Zwischenspeicher. Datei `ergebnisse/sonnet_v02_pruefset.jsonl`.

## Summen (Höchstwert 42)

| Klasse | n | Pflicht erfüllt | Summen absteigend |
|---|---|---|---|
| gut | 15 | 3 | 32 25 25 24 23 23 23 19 19 18 18 17 17 15 14 |
| Grenzfall | 46 | 6 | 27 27 26 25 23 22 … 10 |
| ungeeignet | 38 | 2 | 27 27 24 24 24 23 22 22 19 … 5 |
| gut, schon weitergeführt | 2 | 0 | 28 8 |

## Testregel und Eichung

- Mit Pflicht als Filter erreichen nur 3 von 15 guten (20 %) irgendeine Schwelle. Nicht bestanden.
- Nur nach Summe: Schwelle 17 → 12 von 15 guten (80 %), 30 von 46 Grenzfällen, 19 von 38 ungeeigneten. Startschwelle damit **17** (geeicht nach Summe).
- Trennung schwach: Gute Ø höher, aber ungeeignete reichen bis 27.

## Warum die Pflicht scheitert (beobachtet an den 12 guten ohne Pflicht)

- K2 „Abbruchgrund außerhalb der Idee“ bei 8 guten nicht erfüllt. Betroffen vor allem Projekte, die erfolgreich waren und nur einen offenen Schritt haben (ERC PoC, SBIR). Für diese Klasse B gibt es keinen Abbruchgrund.
- K11 = 0 bei 3 guten (TJ01000218, GA203/99/P017, GA106/09/0814), K12 = 0 bei 2 (N17A-030-0089, 101081888).
- Sonnet schreibt Warnungen in `ausschluss`, z. B. „… nur als Warnung, nicht als harter Ausschluss gesetzt“; das Skript wertet jeden Text dort als Ausschluss (GA203/99/P017, 101081888).

## Entscheidung im Lauf (Claude Code, unter Nicks Vorgabe „keine Rückfragen bis Phase 8“)

Pflicht wird als Markierung geführt, nicht als Filter; Rangfolge nach Summe. Kriterien nicht geändert.

## Vorschläge (nicht umgesetzt)

1. K2 für Klasse B (Ergebnis erreicht, offener Schritt ausdrücklich) als erfüllt werten oder durch „Grund, warum es liegen blieb“ ersetzen.
2. Feld `ausschluss` nur mit fester Liste füllen lassen (`widerlegt|formal|ausbau|fach|militaer|null`), Warnungen in ein eigenes Feld.
3. Mehr Trennschärfe: K4 (Markt) und K11 zeigen wenig Unterschied zwischen gut und ungeeignet; prüfen, ob Denken (thinking) bei Sonnet hilft (kostet rund das Doppelte).
