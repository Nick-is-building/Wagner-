# Pipeline: Stufen, Regeln, Erwartungswerte

Stand 9. November 2026. Betriebsanleitung für die Suche. Hintergründe und Quellen stehen in `01_feldkarte.md`.

## Pools (Stufe 1)

Erwartete Zahlen, wenn die Skripte auf denselben Daten laufen. Weicht ein Lauf stark ab, erst prüfen, dann weiterarbeiten.

| Pool | Inhalt | Einträge | Skript |
|---|---|---|---|
| `cep_fail` | CEP (Tschechien), Technik, gestoppt/unterbrochen oder Ziel verfehlt, ohne Ausbauprojekte und formale Gründe | 432 | `pools.py` |
| `cep_pos` | CEP, Technik, „hervorragend“ oder „erfüllt“, Ende bis 2021, Prototyp/Patent/Software im Text | 1.329 | `pools.py` |
| `fwf_obst` | FWF (Österreich), Technik, Endbericht mit Hindernis-Formulierung | 318 | `pools.py` |
| `fwf_pos` | FWF, Technik, Ende vor 2022, positive Formulierung ohne Hindernis | 391 | `pools.py` |
| `sbir` | SBIR Phase I ohne Phase II, Firma nie mit späterer Phase II, zivil, bis 2021 | 6.343 | `pools.py` |
| `gw` | Grant Witness, gekündigte NSF-Förderungen in Technikfächern | 264 | `pools.py` |
| `poc` | CORDIS ERC Proof of Concept, abgeschlossen, Technik | 854 | `newpools.py` |
| `sme1_noP2` | CORDIS KMU-Instrument Phase 1 ohne Phase 2 derselben Firma | 3.097 | `newpools.py` |
| `sme2` | CORDIS KMU-Instrument Phase 2 | 1.168 | `newpools.py` |
| `sbir2` | SBIR Phase II 2008–2020, Firma danach nie wieder gefördert, ohne Waffen | 2.540 | `newpools.py` |
| `riv` | RIV (Tschechien) 2018–2024: Prototyp, Technologie, Patent, Gebrauchsmuster, Software; Technik; „bisher ungenutzt“ (Code O) oder offener Schritt im Text | 1.177 von 23.542 | `newpools.py` |

Nach Frühfiltern und Textaufbereitung (`build_texts.py`): 17.421 Einträge.

## Frühfilter

Harte Regeln nehmen einen Eintrag aus dem Lauf; er bleibt in der Datei. Weiche Regeln stellen ihn nach hinten. Code: `scripts/early.py`. Geprüft an 83 bewerteten Zufallseinträgen: Die Regeln erkennen 52 der 75 ungeeigneten und treffen keinen der 8 guten.

| Regel | Art |
|---|---|
| CEP formaler Grund: Insolvenz („úpadek“), Rücktritt vom Vertrag, fehlende Nachweise, Bewertungsmethodik, „zu Lasten des Empfängers“ | hart |
| CEP Infrastrukturprogramme (Kürzel LM, LQ, LO, LR) | hart |
| SBIR Pitch Day, offene Aufrufe, fertiges Produkt | hart |
| SBIR Waffen, Raketen, Zielerfassung ohne zivilen Bezug | hart |
| Grant Witness Bildung, Gleichstellung, Konferenz, Planung, Falschinformation, Rest unter 50.000 $ | hart |
| CEP Bewertung ohne Inhalt (Standardsatz oder unter 70 Zeichen) | weich |
| CEP Personal- oder Frühabbruch | weich |
| Reine Grundlagenfächer (Mathematik, Astronomie, Geologie) | weich |
| FWF ohne echtes Hindernis im Text | weich |
| Positive Projekte ohne offenen Schritt | weich |
| SBIR Verteidigung ohne zivilen Bezug | weich |

Verworfen: eine Regel gegen Publikationsmängel. Sie hätte einen guten Fall aussortiert.

**Stärkstes Frühsignal:** ein im Text benanntes technisches Hindernis. In der Probe waren 27 % der Einträge mit diesem Merkmal gut oder Grenzfall, ohne es 3 %.

## Stufe 2: Herausziehen (Haiku)

Haiku urteilt nicht, es füllt Felder aus, jedes mit wörtlichem Zitat. Schema und Anweisung: `prompts/haiku_extraktion.md`. Zwei Durchläufe mit leicht verschiedenen Anweisungen; ein Ja („technisches Hindernis genannt“ oder „offener Schritt genannt“) reicht zum Weiterkommen. Danach prüft `scripts/zitat_check.py`, ob die Zitate wörtlich im Text stehen. Fehlt eines, kommt der Eintrag in „Nachprüfen“, nicht in den Müll.

## Hindernis-Muster

Aus dem Fähigkeiten-Katalog. Haiku vergibt alle passenden Muster.

| Nr. | Muster | Aussicht |
|---|---|---|
| H1 | Rechnung oder Simulation zu teuer | hoch |
| H2 | Zu viele Varianten oder Parameter; Funktionsmuster verfehlte Werte | hoch |
| H3 | Auswertung von Hand zu aufwendig (Bilder, Dokumente, Signale) | hoch |
| H4 | Implementierung oder Personal fehlte | mittel bis hoch |
| H5 | Zu wenige Daten für ein Modell | mittel |
| H6 | Messung zu ungenau oder verrauscht | mittel |
| H7 | Material oder Molekül nicht gefunden | mittel |
| H8 | Bauteil zu teuer oder nicht erhältlich | mittel |
| H9 | Synthese oder Herstellung gelang nicht | niedrig bis mittel |
| H10 | Markt fehlte, Firma insolvent | eigene Marktprüfung |
| H11 | Zulassung oder Vorschrift | niedrig |

## Stufe 3: Bewerten (Sonnet)

Alle Einträge mit H1 bis H7 oder offenem Schritt. Anweisung: `prompts/sonnet_bewertung.md`.

| Nr. | Kriterium | Frage | Art |
|---|---|---|---|
| 1 | Unerledigter Kern | Lässt sich in einem Satz sagen, was offen blieb? | Pflicht |
| 2 | Abbruchgrund | Lag er außerhalb der Idee: Geld, Personal, Organisation, Technik, Aufwand? | Pflicht |
| 3 | Heute lösbar | Mit KI, Rechenleistung, Daten oder günstigerer Technik behebbar, notfalls über einen Umweg? | 0–3, doppelt |
| 4 | Markt | Branche und zahlende Anwender? | 0–3, doppelt |
| 5 | Beleg | Teilerfolge, Messdaten, Prototyp? | 0–3 |
| 6 | Rechenanteil | Wie viel lässt sich am Rechner fortführen? | 0–3 |
| 7 | Noch offen | Hat es niemand gelöst? | Pflicht ab Stufe 4 |
| 8 | Rechte | Frei nutzbar oder lizenzierbar? | 0–3 |
| 9 | Unterlagen | Berichte, Daten, Patente zugänglich? | 0–3 |
| 10 | Tempo | Wie schnell ein erstes vorzeigbares Ergebnis? | 0–3 |

Höchstwert 27 Punkte (Kriterien 3 und 4 je bis 6, die übrigen fünf je bis 3). Weiter zu Stufe 4 geht alles mit erfüllten Pflichtkriterien und mindestens 13 Punkten; diese Startschwelle wird am Prüfset geeicht. Keine Obergrenze.

Harte Ausschlüsse: Idee widerlegt, nur formaler Grund, reines Ausbau- oder Infrastrukturprojekt, ausgeschlossenes Fach, militärisch ohne zivile Nutzung.

## Stufe 4: Fortsetzungscheck und Wiederbelebung (OpenAlex)

`scripts/openalex_check.py` (v0.3) liefert drei Hinweise je Kandidat, kein Urteil. Eingabe baut `scripts/openalex_eingabe.py` aus den Rohdaten (englische Titel und Ziele, Endjahr, Förderkennzeichen, Einrichtung, Land).

| Signal | Was | Kosten |
|---|---|---|
| A Projektergebnisse | Arbeiten, die das Projekt als Förderung nennen (`awards.funder_award_id`); wie oft seit Projektende zitiert, wie viele Zitate seit 2022 aus KI-Teilgebieten | 1 bis 3 Credits |
| B Weiterführung | spätere Arbeiten mit ähnlichem Thema ab Projektende, weltweit und zusätzlich in derselben Einrichtung; Ähnlichkeit zum Projektziel. Ab 0,35 „vermutlich weitergeführt“, ab 0,2 „unklar“ | 20 bis 30 Credits |
| C Wiederbelebung | KI-Arbeiten (Künstliche Intelligenz, Computer Vision) zum Thema je Jahr, 2016–19 gegen 2022–25; mit Haikus Fachbegriffen, sonst grob | 10 Credits |

Getestet am 9. November (`pruefset/openalex_test_2026-11-09.md`): Luftbilder und dapE-Hemmstoffe als „vermutlich weitergeführt“ erkannt, Hydraulikpumpe KHG ohne Hinweis. Signal A fand für 6 von 31 Prüfset-Fällen Projektarbeiten (FWF- und tschechische Kürzel; CORDIS-Nummern nicht). Signal C mit Titelwörtern ist zu grob und dient bis zum Test mit Fachbegriffen nur als Nebeninfo.

Modus „schnell“ (Standard: A plus weltweite Suche, rund 13 Credits, rund 750 Kandidaten pro Tag) für alle aus Stufe 3; Modus „voll“ (zusätzlich gleiche Einrichtung und Signal C) nur für die oberen Kandidaten vor Stufe 5.

„Weitergeführt“ heißt nicht verworfen: Die Folgearbeit kann nur einen Teil abdecken oder eine Lücke zeigen. Das entscheidet Stufe 5.

## Stufe 5: Tiefenprüfung (Opus)

Für die oberen Kandidaten. Anweisung: `prompts/opus_tiefenpruefung.md`. Ergebnis ist eine Kandidatenkarte nach `kandidaten/_VORLAGE.md` mit:

- **Damals:** konkretes Hindernis, wörtlich belegt
- **Heute:** konkrete Entwicklung, die es beseitigt, mit Quelle und Link
- **Markt:** wer zahlt, mit Beleg
- **Offen:** entscheidende unbelegte Annahme und der schnellste Test
- die acht Heilmeier-Fragen
- ein Gegengutachten mit Lösungsvorschlägen (getrennter Lauf, sieht die Begründung nicht)

## Prüfset

`pruefset/pruefset.csv`: 51 echte Einträge (11 gut, davon 2 schon weitergeführt; 20 Grenzfälle; 20 ungeeignet). Ziel: 20/20/20 plus rund 5 künstlich umgeschriebene gute Fälle, bei denen das Entscheidende erst im letzten Satz steht.

Testregel: Die Vorsortierung behält alle guten und mindestens 80 % der Grenzfälle. Ungeeignete dürfen durchrutschen. Während des großen Laufs kommen einige Prüfset-Fälle als Kontrolle in jede Charge.

## Positive Projekte

Ansätze, die funktioniert haben und liegen blieben (Klasse B). „Erfolgreich mit Prototyp“ allein heißt meist „fertig und genutzt“: 0 von 28 in der Probe. Deshalb gilt: Ergebnis plus ausdrücklich offener Schritt (weitere Entwicklung nötig, Vermarktung ausstehend, Partner gesucht) oder amtlich „bisher ungenutzt“ (RIV Code O). Die beste Dichte zeigte bisher ERC Proof of Concept (2 bis 3 von 8).

## Kosten (Schätzung nach Listenpreis, Batch 50 % Rabatt)

| Stufe | Umfang | Kosten |
|---|---|---|
| Haiku, zwei Durchläufe | 17.421 Einträge | rund 5 $ |
| Sonnet | je nach Haiku-Markierung 2.500 bis 5.000 | 15 bis 30 $ |
| Opus | einige Hundert | 15 bis 30 $ über API, im Abo ohne Zusatzkosten |
| Prüfset-Test | 51 Einträge | wenige Cent |

Preise pro Million Token (Eingabe/Ausgabe): Haiku 5.5 0,10/0,50 $, Sonnet 5.5 2/10 $, Opus 5.5 5/25 $ (Stand 8. November 2026).
