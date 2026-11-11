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

## Nachtrag (Haltepunkt 1, Auftrag Nick): Sonnets Begründung bei den 10 durchgefallenen guten

Aus `ergebnisse/sonnet_v03_pruefset.jsonl`. Sonnet hat kein eigenes Begründungsfeld für K11 und K12; gezeigt sind die Felder, aus denen die Punkte folgen: `vorteil` (K11) und `erster_schritt` (K12), dazu `warnung`.

| ID | Summe | K2 (erfüllt, Weg, Art, Zitat) | K11 Punkte und Vorteil | K12 Punkte und erster Schritt | Warnung |
|---|---|---|---|---|---|
| 0839819 | 23 | nein, keiner, keiner: „–“ | 1: Phase-I-Näherungsmodelle komplexer Fabrikmodelle als Ausgangspunkt; als Belegtes nur in Beschreibung, kein Patent oder Datensatz genannt. | 2 (simulation): Stichprobenplanung mit Bayes-Optimierung und Ersatzmodell auf einer simulierten Fab (öffentliche Fab-Simulationsdaten) prototypisch umsetzen. | Reiner Antragstext ohne Ausgangsbericht; der Halbleiter-Fertigungskontext ist ohne Fabrikdaten oder Partner schwer zugän |
| 101123089 | 22 | ja, offener_schritt, Technik: „This requires collaboration with industrial partners to validate the technology in real-world applications.“ | 2: Aufgebaute Beschichtungsfolge für Extruderzylinder und -schnecke mit Palladium-Katalysator sowie Prozessdaten und Ökobilanz. | 0 (labor): Mit Prozess- und Ökobilanzdaten aus der Veröffentlichung ein Ersatzmodell für Umsatz und Verweilzeit bauen, um Extruderlänge und Zyklenzahl vorab abzu | Kern ist Hardware (Extruder, Beschichtung, Scale-up); für Nick ohne Labor und Partner kaum umsetzbar. |
| TC4-043 | 22 | ja, abbruch, Technik: „Projekt předčasně ukončen.“ | 0: Kein belegter eigenständiger Vorteil; nur ein Rechenmodell, dessen Abweichung vom Ergebnis die Chance bietet, Ursachen heute nachzurechnen. | 3 (simulation): Abscheidung per Strömungsrechnung mit Partikelverfolgung nachrechnen, Abweichung zum damaligen Rechenmodell klären und Varianten per Ersatzmodell durc | Zyklon-Abscheider sind ein reifes Feld; ein eigener Vorteil gegenüber bestehenden Lösungen ist nicht belegt. |
| GA203/99/P017 | 21 | ja, abbruch, Personal: „Projekt ukončen předčasně na žádost řešitelky - mateřská dovolená.“ | 0: Kein eigenständiger Vorteil erkennbar; nur die Methode und Fragestellung, keine Daten oder Patente. | 3 (simulation): Gitter-Monte-Carlo für selbstvermeidende Irrfahrten mit Oberflächenadsorption nachbauen und das Phasendiagramm berechnen. | Reine Grundlagenforschung ohne erkennbaren Markt; der Ausgang meldet Übereinstimmung mit den Zielen, der offene Rest ist |
| 10.55776/I5180 | 20 | nein, keiner, keiner: „–“ | 1: Datengestützte Beschleunigungsmethode für Partikelsimulation; als Veröffentlichung belegt, aber ohne belegte exklusive Rechte. | 2 (simulation): Die publizierte Beschleunigungsmethode nachbauen und mit öffentlichen Granulationsdaten abgleichen. | Ausgang meldet Erfolg (Echtzeit-Simulation erreicht); offener Kern liegt nur in der Motivation, die adaptive Regelung bl |
| 700138 | 16 | ja, offener_schritt, unklar: „Also at this time RVL began sourcing potential partners for a further large-scale project to make a prototype of the TRA“ | 1: Patentierbare Neuheiten laut Machbarkeitsstudie, Details aber vertraulich und nicht zugänglich. | 1 (unklar): Konzept und Nutzerbedarf prüfen, dann Bodenradar-Messungen an Gleis oder Tunnel mit Mietgerät und Auswertesoftware ausprobieren. | Machbarkeitsstudie mit vertraulicher Technik und ohne Daten; Hardware-Prototyp ist ein Radarsystem, kein reines Software |
| GA106/09/0814 | 15 | nein, keiner, unklar: „–“ | 0: – | 1 (simulation): Mit einem Atom-Modell (UMA) Wasserstoffbindung und Desorptionsenergie in Mg2Ni mit Be, B, C auf Zwischengitterplätzen rechnen. | Der Ausgangstext meldet nur 'Nesplnil zadání' ohne Grund; ob die Idee widerlegt oder nur nicht erreicht wurde, ist unbel |
| 174959 | 15 | nein, keiner, keiner: „–“ | 0: – | 2 (simulation): Dynamische Szenen mit bewegten Hindernissen in Robotersimulation nachbauen und Echtzeit-Tracking samt Kollisionsvermeidung mit offenen Bibliotheken te | Antrag ohne Ausgangstext; Phase-II-Ziel noch offen, aber der Ansatz ist schon eine BluHaptics-Firmensoftware (DCS), kein |
| N17A-030-0089 | 13 | nein, keiner, keiner: „–“ | 1: Proprietäre Faserarray-Lasertechnik aus DoD-Entwicklung, aber nicht zugänglich und nicht belegt als frei nutzbar. | 0 (labor): Nur Simulation der Wärmegradienten per Ersatzmodell wäre softwareseitig möglich; Kern bleibt Hochleistungs-Faserlaser-Hardware. | Antrag einer Firma mit proprietärer Faserarray-Technik; kein Ausgangstext, Hardware-Kern nicht ohne Partner nachbaubar. |
| TJ01000218 | 12 | ja, abbruch, Personal: „řešitelský tým odbornou problematiku nezvládl“ | 0: Kein belegter eigenständiger Vorteil; nur die Idee eines innen strukturierten SLM-Hartmetallwerkzeugs, die heute andere ebenfalls verfolgen können. | 0 (labor): Literatur- und Patentrecherche zum SLM von WC-Co-Pulver, danach Parameterstudie nur mit einem Dienstleister für Metall-3D-Druck und Sintern. | Der Text nennt nur ein Scheitern an Ambition und Know-how, keine konkrete technische Ursache; der offene Kern ist unscha |
