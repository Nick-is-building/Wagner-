# Sonnet v0.3 am Prüfset (A07, Freigabe 2026-11-11-A07a)

Lauf 2026-11-11, `scripts/bezahlt/sonnet_v03.py --satz pruefset`: 101 Aufrufe, 0 Fehler, 43 s, 1,557 $ (Log `logs/sonnet_v03_pruefset.log`, Datei `ergebnisse/sonnet_v03_pruefset.jsonl`). Summe neu: v0.2-Summe + M (ja 4, teilweise 2) − 4 je Abzug; Pflicht = K1, K2, K11 ≥ 1, K12 ≥ 1; Startschwelle 17.

## Ergebnis: nicht bestanden (Haltepunkt)

| Klasse | n | Pflicht erfüllt | ≥ 17 mit Pflicht | ≥ 17 ohne Pflicht |
|---|---|---|---|---|
| gut | 15 | 6 | **5** (Regel: 12) | 10 |
| Grenzfall | 46 | 9 | 8 | 23 |
| ungeeignet | 38 | 6 (4 ohne Ausschluss) | 3 | 13 |
| gut, schon weitergeführt | 2 | 0 | 0 | 1 |

Zum Vergleich v0.2: Pflicht bei 3 von 15 guten. Die K2-Änderung hat geholfen (Weg „offener_schritt“ bei 2 guten), reicht aber nicht.

## Die 10 guten unter der Regel

| ID | Summe | woran es scheitert |
|---|---|---|
| 0839819 | 23 | K2 nicht erfüllt |
| 101123089 | 22 | K12 = 0 |
| TC4-043 | 22 | K11 = 0 |
| GA203/99/P017 | 21 | K11 = 0 |
| 10.55776/I5180 | 20 | K1 und K2 nicht erfüllt; Abzug „Kern gelöst“ |
| 700138 | 16 | Summe unter 17 (Pflicht erfüllt) |
| GA106/09/0814 | 15 | K2 nicht erfüllt, K11 = 0 |
| 174959 | 15 | K2 nicht erfüllt, K11 = 0; Abzug „Ausgründung“ |
| N17A-030-0089 | 13 | K2 nicht erfüllt, K12 = 0 |
| TJ01000218 | 12 | K11 = 0, K12 = 0 |

Gründe gezählt (Mehrfachnennung): K2 nicht erfüllt 5, K11 = 0 5, K12 = 0 3, K1 nicht erfüllt 1.

## Beobachtet

- Merkmal M: bei keinem der 10 gescheiterten guten „ja“ oder „teilweise“.
- K11 = 0 trifft dieselben guten wie in v0.2 (TJ01000218, GA203/99/P017, GA106/09/0814). Sonnet sieht dort keinen eigenständigen Vorteil; die Prüfset-Bewertung sah das anders.
- Selbst ohne Pflicht nur 10 von 15. Die Trennung nach Summe ist schwach: ungeeignete bis 25, gute ab 12.

## Nicht gelaufen

Sonnet auf die Vorauswahl (103 Einträge, `ergebnisse/a07_vorauswahl.tsv`), OpenAlex, Fable. Rest der Freigabe A07a: 1,44 $; Trockenlauf Vorauswahl schätzt 1,78 $ (bei A06 lagen echte Kosten 7 bis 30 % darunter).

## Mögliche Wege (Entscheidung Nick, keine Erlaubnis)

1. Pflicht als Markierung lassen (wie A06), Rangfolge nach Summe; 10 von 15, also auch dann unter 12.
2. K11 und K12 aus der Pflicht nehmen und nur K1/K2 hart halten; nachgerechnet wäre das kostenlos aus der vorhandenen Datei.
3. Prüfset-Bewertung der 5 K11-Fälle gegenlesen: Sonnet oder Prüfset falsch?
4. Trotz Nichtbestehen die Vorauswahl laufen lassen (rund 1,2 bis 1,8 $), weil sie klein und schon vorgefiltert ist.
