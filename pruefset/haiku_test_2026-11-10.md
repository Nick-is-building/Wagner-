# Haiku-Prompt v0.1 am Prüfset (A02 Schritt 4)

Stand: 10.11.2026, ausgewertet von Claude Code (Opus 5.5). Prompt unverändert (`prompts/haiku_extraktion.md` v0.1).

Grundlage: `ergebnisse/haiku_pruefset_ok.jsonl` (46 Einträge × 2 Durchläufe = 92 Antworten), `ergebnisse/zitat_check.jsonl`. Tabelle je Eintrag: `ergebnisse/haiku_auswertung.tsv`, erzeugt mit `scripts/haiku_auswertung.py`.

Regel (aus dem Prompt): Ein Eintrag kommt weiter, wenn einer der beiden Durchläufe `technisches_hindernis` oder `offener_schritt` mit „ja“ oder „unklar“ beantwortet.

## Ergebnis: nicht bestanden

| Klasse | im Lauf | kommen weiter | Anforderung | erfüllt? |
|---|---|---|---|---|
| gut | 9 | 8 | alle | nein (1 fehlt) |
| gut (schon weitergeführt) | 2 | 0 | siehe Frage unten | – |
| Grenzfall | 20 | 19 (95 %) | ≥ 80 % | ja |
| ungeeignet | 15 | 12 (80 %) | keine | – |

5 ungeeignete Einträge des Prüfsets (51) fehlen gewollt in der Eingabe (Stufe 1 entfernt sie, siehe A01): 2451885, 2122640, B152-017-0286, FX211-CSO1-0097, F191-009-1502.

Zählt man die zwei „schon weitergeführten“ guten Fälle zur Klasse „gut“, kommen 8 von 11 weiter.

## Durchgefallene gute und Grenzfälle

**GA203/99/P017** (gut; Monte-Carlo-Simulation von Polymeren). Beide Durchläufe: Hindernis „nein“, offener Schritt „nein“.
- Zitat: „Projekt ukončen předčasně na žádost řešitelky - mateřská dovolená.“ (Abbruch auf Wunsch der Projektleiterin, Mutterschaft)
- Vermuteter Grund: Haiku hält sich an die Regel. Der Abbruchgrund ist nicht technisch, ein offener Schritt steht nicht im Text. „Gut“ ist der Fall wegen des Inhalts (Rechnung, die heute billig ist), nicht wegen eines genannten Hindernisses. Haiku gibt `rechenanteil: hoch` in beiden Durchläufen.

**IAA400550614** (gut, schon weitergeführt; dapE/argE-Hemmstoffe). Beide „nein“.
- Zitat: „nebyly výsledky dosud adekvátním způsobem publikovány“ (Ergebnisse nicht angemessen veröffentlicht)
- Vermuteter Grund: Der Text nennt nur einen formalen Grund. Nach Prompt-Regel richtig.

**10.55776/P24116** (gut, schon weitergeführt; Georeferenzierung von Luftbildern). Beide „nein“, alle Felder `null`.
- Zitat aus der Eingabe: „Georeferencing … is a pretty time-consuming operation. It is therefore the biggest bottleneck“
- Vermuteter Grund: Das Hindernis steht als Ausgangslage im Text, nicht als Grund für ein verfehltes Ziel. Der Prompt definiert Hindernis nur als „warum ein Ziel nicht erreicht wurde“. Beobachtet: `text_b` wiederholt den Schluss von `text_a`; über das Ergebnis des Projekts steht in der Eingabe nichts.

**RIV/46504711:_____/21:N0000005** (Grenzfall; Kohlenstoff-Nanoröhren in Alkydlack). Beide „nein“, alle Felder `null`.
- Zitat: „Vodivost vzorků na skle je homogenní v celém povrchu, hodnoty odporu se pohybují ~200 kΩ.“
- Vermuteter Grund: Der Text beschreibt nur ein erreichtes Ergebnis. Dass es nicht kommerziell genutzt wird (Prüfset-Begründung), steht nicht im Text.

## Weitere Beobachtungen

- **Trennschärfe gering:** 12 von 15 ungeeigneten kommen weiter. 8 davon nur über „unklar“, ohne ein „ja“ (Tabelle). Würde man nur „ja“ zählen, fielen aber auch 4 gute heraus (FV10342, FW01010098, TJ01000218, GA106/09/0814 haben nur „unklar“). „Unklar“ trägt also die guten Fälle mit.
- **Durchläufe ergänzen sich wenig:** Kein Eintrag kommt nur durch Durchlauf 2 weiter, der in Durchlauf 1 nicht schon weiter war (aus der Tabelle abgelesen).
- **Zitat-Check:** 5 Antworten mit Feldern ohne Beleg (175273, GA105/08/1072, GP201/03/P149, 101123089, 181662). Keine davon ändert das Ergebnis „weiter“. Nicht von Hand geprüft. Die Zuordnung zum Durchlauf folgt der Reihenfolge in der Datei, weil `zitat_check.py` keine Durchlaufnummer schreibt.
- **Rechenanteil:** „hoch“ vergibt Haiku für 7 Einträge (GA203/99/P017, 10.55776/I5180, GPP204/10/P331, 841640, FR-TI3/421, 10.55776/P34177, RIV/00216305:26110/22:PR36166, letzterer nur in Durchlauf 2).

## Vorschläge an den Planungs-Chat (keine Änderung vorgenommen)

1. **Zusätzliche Weiter-Regel „Rechenanteil hoch“.** Am Prüfset geprüft: rettet GA203/99/P017 (gut 9 von 9), lässt dazu nur 10.55776/P34177 (ungeeignet) zusätzlich durch. Die übrigen „hoch“-Fälle sind schon weiter.
2. **Abbruch aus persönlichem Grund bei unfertigem Ziel** (Elternzeit, Krankheit, Wechsel der Leitung) als eigenes Feld oder als offenen Schritt werten: Die Arbeit ist nicht widerlegt, nur liegen geblieben. Das trifft GA203/99/P017 direkt.
3. **Hindernis auch als Ausgangslage erfassen** („bottleneck“, „zeitaufwendig“, „von Hand“), nicht nur als Grund für ein verfehltes Ziel. Hätte P24116 erfasst. Risiko: mehr ungeeignete kommen weiter; vorher am Prüfset testen.
4. **Frage zur Testregel:** Sollen die zwei „schon weitergeführten“ Fälle bei Haiku weiterkommen müssen? Laut Prüfset-Begründung soll sie der Fortsetzungscheck finden, nicht Haiku. Dann wäre die Anforderung „gut“ 9 von 9.
5. **RIV-Einträge** beschreiben oft nur Ergebnisse. Für den Grenzfall N0000005 hilft kein Prompt; die Information steht nicht im Text.
6. `zitat_check.py` sollte die Durchlaufnummer mitschreiben.
