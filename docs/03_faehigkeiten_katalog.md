> Kopie vom 9. November 2026. Original im Chat: https://claude.ai/artifact/4Y9KmjiJaM6E5ib8ni2tJ7
> Änderungen trägt der Chat in beide Fassungen ein.

# Fähigkeiten-Katalog: Was KI heute möglich macht

Nov 9, 2026 · @Nick

## Zweck

Der Katalog sagt den Modellen in unserer Suche, was KI und billige Rechenleistung heute können und was nicht. Ohne ihn bewertet jedes Modell „heute lösbar“ nach eigenem Gefühl und eigenem Wissensstand.

Er wird viermal genutzt:

- **Abgleich:** Jede Fähigkeit ist ein Suchtext. Wir rechnen die Ähnlichkeit zwischen ihr und den Hindernissen alter Projekte und sortieren die Projekte danach. Im Test sortierte das nur schwach (siehe Methoden).
- **Vorsortierung (Haiku):** Haiku ordnet ein genanntes Hindernis einem Hindernis-Muster aus der Übersetzungstabelle zu.
- **Bewertung (Opus):** Opus prüft Kriterium 3 „heute lösbar“ gegen konkrete Werkzeuge, Belege und Grenzen statt gegen Vermutungen.
- **Inspiration:** Wer einen Kandidaten liest, sieht, welche Werkzeuge es für diese Art Problem inzwischen gibt.

Jede Zeile nennt die Fähigkeit, ein konkretes Werkzeug oder Beispiel, den Reifegrad und einen Beleg. Reifegrad heißt hier: **erprobt** (in Industrie oder breiter Forschung im Einsatz), **brauchbar** (funktioniert mit Fachwissen und etwas Aufwand), **jung** (erste starke Ergebnisse, noch unsicher).

## Querschnitts-Fähigkeiten

Acht Werkzeuge wirken in fast jedem Fachgebiet. Am stärksten verändert haben sich Simulation, Atom-Modelle und das Lesen alter Dokumente; bei neuer Chemie ist KI dagegen noch schwach.

| Fähigkeit | Was heute geht | Beispiel | Reife | Grenze |
| --- | --- | --- | --- | --- |
| Ersatzmodelle für Strömungs- und Festigkeitsrechnung | Ein neuronales Modell ersetzt nach dem Training die teure Simulation; Netze mit über 100 Mio. Zellen laufen auf einer GPU | [AB-UPT von Emmi AI](https://www.emmi.ai/news/ab-upt-scaling-neural-surrogates-100m-cfd-meshes), Fahrzeug-Aerodynamik; kommerziell z. B. Ansys SimAI | brauchbar, in der Autoindustrie erprobt | braucht zuerst einige Hundert echte Simulationen zum Lernen; Emmi nennt keine gemessene Beschleunigung |
| Universelle Atom-Modelle | Ersetzen quantenchemische Rechnungen (DFT): „von Stunden auf unter eine Sekunde“, über 100.000 Atome auf einer 80-GB-GPU | [UMA von Meta](https://huggingface.co/papers/2506.23971.md), trainiert auf rund 500 Mio. Strukturen; Materialien, Moleküle, Katalysatoren, MOFs | brauchbar; kommerziell nutzbare Lizenz mit Auflagen | Genauigkeit nur nahe an DFT, nicht gleich; seltene Elemente und Zustände schwächer |
| Bayes-Optimierung | Findet gute Prozessparameter mit wenigen Versuchen; ein Benchmark nutzt 35 Versuche als Budget | [Benchmark in Frontiers 2025](https://www.frontiersin.org/journals/manufacturing-technology/articles/10.3389/fmtec.2025.1614335/full) | erprobt | Messrauschen senkt die Zuverlässigkeit stark; vorher Parameter auf wenige wichtige reduzieren |
| Bildmodelle | Vortrainierte Modelle als Startpunkt für Prüfung, Segmentierung, Bildabgleich | [DINOv3 in der Industrieprüfung](https://arxiv.org/html/2605.23472); CNN-Abgleich alter Luftbilder ([TU Wien](https://meetingorganizer.copernicus.org/EGU23/EGU23-17437.html)) | brauchbar | DINOv3 hilft nur mit Feinabstimmung; bei Röntgenbildern war ImageNet-Vortraining besser |
| Zeitreihen-Grundmodelle | Restlebensdauer und Ausfälle aus Sensordaten vorhersagen, mit wenig eigenem Training | [Chronos-2 bei Nokia](https://arxiv.org/html/2606.11990v2): halber Fehler gegenüber dem besten trainierten Vergleichsmodell | brauchbar | nur eine Studie mit zwei Gerätetypen; braucht gelabelte Ausfalldaten |
| Alte Dokumente lesen | Gescannte Berichte und große Tabellen zuverlässig in Daten umwandeln | [DIW-Studie](https://www.diw.de/de/diw_01.c.1014976.de/publikationen/externe_referierte_aufsaetze/2026_0014/confidence-based_end-to-end_extraction_of_large_historical_economic_tables_with_llms.html): 99,5 % der Zellen sicher erkannt, 0,015 % Fehler bei diesen | erprobt seit Ende 2025 | Vorgänger-Modelle vor Ende 2025 scheiterten an großen Tabellen |
| Code-Agenten | Methoden aus alten Papern nachbauen und laufen lassen | [Codex baute 4 Paper zum wissenschaftlichen ML nach](https://huggingface.co/papers/2607.02134.md): 37 von 39 Kennzahlen im Toleranzbereich, 2 bis 7 Stunden je Lauf | brauchbar | geprüft nur gegen die eigene Abnahme, nicht unabhängig; Kosten nicht angegeben |
| Rechenleistung | Eine H100-GPU kostet zur Miete rund 2,90 bis 5,20 $ pro Stunde (Runpod, AWS, geprüft August 2026) | [Preisvergleich](https://intuitionlabs.ai/pdfs/h100-rental-prices-compared-1-49-6-98-hr-across-15-cloud-providers-2026.pdf); Rechenleistung pro Dollar verdoppelte sich 2006 bis 2021 etwa alle 2,5 Jahre ([Epoch AI](https://epoch.ai/blog/trends-in-gpu-price-performance)) | erprobt | die Epoch-Reihe endet 2021; die Fortschreibung bis heute ist eine Schätzung |

Faustregel für die Bewertung: Ein Projekt von 2010 bekommt heute für dasselbe Geld grob 50- bis 100-mal mehr Rechenleistung, allein durch günstigere Hardware. Dazu kommen die Werkzeuge oben. Ein Hindernis wie „Simulation zu teuer“ oder „zu wenige Messdaten für ein Modell“ ist deshalb fast immer neu zu prüfen.

## Fähigkeiten je Fachgebiet

Am reifsten sind Materialsimulation, Strömungsrechnung, Bildauswertung und Software; noch jung sind Photonik-Entwurf, analoge Schaltungen und Synthese neuer Moleküle. Die letzte Spalte ist der Suchschlüssel für den Abgleich mit alten Projekten.

| Fachgebiet | Was neu geht | Beleg | Reife | Alte Hindernisse, die das trifft |
| --- | --- | --- | --- | --- |
| Materialien | Eigenschaften per Atom-Modell statt DFT rechnen; neue Kristalle mit Zieleigenschaft erzeugen | [UMA](https://huggingface.co/papers/2506.23971.md); [MatterGen](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai): Ziel 200 GPa Kompressionsmodul, gemessen 169 GPa am synthetisierten TaCr2O6, Code unter MIT-Lizenz | brauchbar | Rechnung zu teuer; zu viele Kandidaten; Stabilität oder Phase unklar; Wasserstoffspeicher, Katalysatoren, Legierungen |
| Chemie und Synthese | Syntheseweg für bekannte Reaktionstypen vorschlagen | [RSC 2026](https://pubs.rsc.org/en/content/articlelanding/2026/dd/d6dd00072j): bei neuen Reaktionstypen unter 1 % exakte Treffer | jung bei neuer Chemie | Ausbeute zu gering; Route unbekannt; nur teilweise lösbar, Laborarbeit bleibt |
| Strömung und Struktur | Tausende Varianten statt einiger Dutzend durchrechnen; Form direkt aus CAD bewerten | [AB-UPT](https://www.emmi.ai/news/ab-upt-scaling-neural-surrogates-100m-cfd-meshes) | brauchbar, Auto-Aerodynamik erprobt | Simulation zu teuer; Optimierung brach ab; zu wenige Varianten geprüft; Turbinen, Kompressoren, Wärmetauscher |
| Elektronik und Chipentwurf | Logiksynthese und Zeitverhalten mit ML vorhersagen und optimieren | [NSF-Workshopbericht](https://arxiv.org/pdf/2601.14541v3): bis 69,3 % weniger Zellfläche (AISYN), 6,3-mal kürzere Laufzeit (INVICTUS) | brauchbar digital, jung analog | Entwurfsraum zu groß; Verifikation zu aufwendig; analoge Schaltungen bleiben weitgehend Handarbeit |
| Photonik und Antennen | Strukturen rückwärts aus der gewünschten Wirkung entwerfen | [PeerJ-Review 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12192857/): 32 Arbeiten, meist nur simuliert | jung | Struktur nicht optimierbar; Fertigungsabweichungen; Ergebnis braucht Reinraum zur Prüfung |
| Fertigung und Prozess | Prozessfenster mit wenigen Versuchen finden; Qualität per Kamera überwachen | [Bayes-Benchmark](https://www.frontiersin.org/journals/manufacturing-technology/articles/10.3389/fmtec.2025.1614335/full); [DINOv3-Studie](https://arxiv.org/html/2605.23472) | erprobt | Parameter nicht gefunden; Ausschuss zu hoch; Funktionsmuster verfehlte Werte (wie bei der Plasmadüse) |
| Energie und Batterien | Lebensdauer aus kurzen Tests hochrechnen | [RSC-Review 2026](https://pubs.rsc.org/en/content/articlehtml/2026/eb/d6eb00101g): Alterungstest von 280 auf 140 Tage verkürzt, 13 bis 77 % bessere Hochrechnung | brauchbar | Alterungstests zu lang; Übertragung auf neue Zellchemien bleibt schwach |
| Wartung und Sensorik | Restlebensdauer aus Sensordaten vorhersagen | [Chronos-2 bei Nokia](https://arxiv.org/html/2606.11990v2) | brauchbar | zu wenig Daten für ein eigenes Modell; Signale zu verrauscht |
| Mess- und Bildtechnik | Bilder segmentieren, abgleichen und ausmessen; alte Scans lesen | [TU Wien](https://meetingorganizer.copernicus.org/EGU23/EGU23-17437.html); [DIW](https://www.diw.de/de/diw_01.c.1014976.de/publikationen/externe_referierte_aufsaetze/2026_0014/confidence-based_end-to-end_extraction_of_large_historical_economic_tables_with_llms.html) | erprobt | Auswertung von Hand; Bildzuordnung scheiterte; Fotogrammetrie zu ungenau |
| Robotik | Greifen und Hantieren mit einem allgemeinen Modell, das auf neue Aufgaben angepasst wird | [LingBot-VLA](https://arxiv.org/abs/2601.18692): 20.000 Stunden Daten von 9 Roboterbauarten, offen veröffentlicht | jung bis brauchbar | Programmieraufwand je Aufgabe; unsortierte Teile; Erfolgsquoten nennt die Arbeit nicht |
| Software und Algorithmen | Verfahren aus Papern nachbauen, Code und Tests schreiben | [Codex-Replikationen](https://huggingface.co/papers/2607.02134.md) | brauchbar | Implementierung zu aufwendig; Entwickler ging; Software nie fertig |
| Medizintechnik | Bildauswertung als zugelassenes Produkt | [FDA-Liste](https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/list-artificial-intelligence-enabled-medical-devices): rund drei Viertel der Einträge von Mitte 2025 bis Mitte 2026 stammen aus der Radiologie | erprobt | Auswertung manuell; aber Zulassung kostet Jahre, siehe Grenzen |

## Übersetzungstabelle: altes Hindernis, heutiger Weg

Haiku ordnet jedes genannte Hindernis einem dieser elf Muster zu. Die Spalte „Aussicht“ steuert die Reihenfolge der Bewertung, sie schließt nichts aus.

| Nr. | Hindernis-Muster | Typische Formulierung | Heutiger Weg | Aussicht |
| --- | --- | --- | --- | --- |
| H1 | Rechnung oder Simulation zu teuer | computationally expensive; výpočetně náročné; zu wenig Rechenzeit | Ersatzmodell, Atom-Modell, gemietete GPU | hoch |
| H2 | Zu viele Varianten oder Parameter | optimum not found; parametr nebyl dosažen; Funktionsmuster verfehlte Werte | Bayes-Optimierung, Ersatzmodell, Rückwärtsentwurf | hoch |
| H3 | Auswertung von Hand zu aufwendig | manual analysis; ruční vyhodnocení; bottleneck | Bild-, Dokument- und Signalmodelle | hoch |
| H4 | Implementierung oder Personal fehlte | developer left; odchod řešitele; software not finished | Code-Agenten, Nachbau aus Paper und Bericht | mittel bis hoch |
| H5 | Zu wenige Daten für ein Modell | insufficient data; nedostatek dat | vortrainierte Grundmodelle, Feinabstimmung, Trainingsdaten aus Simulation | mittel |
| H6 | Messung zu ungenau oder verrauscht | noise; přesnost nedostatečná | ML-Signalverarbeitung, Kombination mehrerer Sensoren | mittel |
| H7 | Geeignetes Material oder Molekül nicht gefunden | no suitable material; materiál nevyhovoval | Erzeugen und Vorprüfen am Rechner, danach wenige Laborversuche | mittel |
| H8 | Bauteil zu teuer oder nicht erhältlich | výrobce nenalezen; component unavailable | heutige Preise neu prüfen, 3D-Druck, günstige Rechenchips | mittel; KI hilft wenig direkt |
| H9 | Synthese oder Herstellung gelang nicht | only minute quantities; low yield; výtěžnost | Routenvorschläge für bekannte Reaktionstypen, Prozessoptimierung | niedrig bis mittel; Labor bleibt |
| H10 | Markt fehlte, Firma insolvent | úpadek; no market; nebude mít odbyt | KI löst das nicht; Markt heute neu prüfen | offen, eigene Marktprüfung |
| H11 | Zulassung oder Vorschrift | approval; certification; legislativní | KI löst das nicht | niedrig |

Ein Projekt kann mehrere Muster tragen. Haiku vergibt alle passenden mit wortwörtlichem Zitat. Die Bewertung beginnt mit H1 bis H3.

## Grenzen

KI verkürzt die Rechen- und Auswertearbeit, nicht die Arbeit im Labor, in der Werkstatt oder bei der Zulassung. Ein Kandidat ist umso stärker, je größer sein Rechenanteil ist (Kriterium 6).

- **Laborzeit bleibt.** Was am Rechner entworfen wird, muss gebaut und gemessen werden. Bei MatterGen lag der gemessene Wert 15 % unter dem Ziel.
- **Neue Chemie ist schwach.** Bei unbekannten Reaktionstypen treffen Syntheseplaner unter 1 % exakt.
- **Übertragung auf Neues ist das Hauptproblem.** Batterie-, Chip- und Bildmodelle verlieren an Genauigkeit bei neuen Zellchemien, Fertigungsknoten oder Bildarten wie Röntgen.
- **Veröffentlichte Zahlen sind oft zu optimistisch.** Zufällige Testaufteilungen und eigene Abnahmekriterien überschätzen die Leistung; viele Studien nutzen nur einen Durchlauf.
- **Zulassung und Normen** (Medizin, Luftfahrt, Bau) dauern Jahre und kosten mehr als jede Rechnung.
- **Hardware mit Reinraum oder Spezialanlage** (Photonik, Halbleiter) lässt sich nicht am Rechner fertigstellen.
- **Lizenzen prüfen.** Manche Modelle sind offen, aber mit Auflagen; UMA etwa nennt geografische und Nutzungsbeschränkungen.

Für die Bewertung heißt das: „Heute lösbar“ gilt nur für den Teil des Hindernisses, den ein Werkzeug aus diesem Katalog nachweislich trifft. Der Rest steht als offene Annahme in der Belegpflicht.

## Methoden: schneller und sicherer entdecken

Fünf erprobte Verfahren lassen sich direkt übernehmen. Den größten Hebel haben das Lernen aus unseren eigenen Urteilen und der Rückblick-Test mit bekannten Fällen.

| Verfahren | Was es zeigt | Was wir übernehmen |
| --- | --- | --- |
| Mehrere Modelle als Ensemble sortieren lassen | Sechs Sprachmodelle in 23 Cochrane-Übersichten: Ensembles erreichten volle Trefferquote bei 38 bis 99 % weniger Lesearbeit; die Präzision blieb bei seltenen Treffern niedrig ([Sanghera et al., JAMIA 2025](https://www.phc.ox.ac.uk/publications/publication_modal/2093498)) | In der Vorsortierung reicht eine Ja-Stimme von zwei Modellen, damit ein Eintrag weiterkommt. Die Autoren verlangen eine Prüfung je Fachgebiet: dafür ist unser Prüfset da. |
| Aktives Lernen | Ein Modell lernt aus jedem Urteil und sortiert den Rest neu. Die Ersparnis hängt davon ab, wie häufig Treffer sind; die Faustregel „50 Nieten hintereinander, dann aufhören“ verfehlte das Ziel in 39 % der Fälle ([Systematic Reviews 2020](https://link.springer.com/doi/10.1186/s13643-020-01521-4)) | Aus den Urteilen der Probe und von Opus lernt ein kleines Modell auf den Text-Vektoren und sortiert alle Pools neu. Wir hören nie nach einer Nieten-Serie auf; ohne Obergrenze bleibt alles in der Liste. |
| Querverbindung zwischen Fachgebieten | Bei rund 80 % der besonders spät entdeckten Arbeiten („Sleeping Beauties“) kommen mindestens drei Viertel der Zitate aus anderen Fächern ([Ke et al. 2015](https://ar5iv.arxiv.org/html/1505.06454)) | Genau das ist der Fähigkeiten-Abgleich: Ein Hindernis aus Fach A trifft auf ein Werkzeug aus Fach B. Zusätzliches Signal: alte Themen, die neuerdings aus der KI-Forschung zitiert werden (braucht OpenAlex). |
| Trends mit Ein- und Wiederanstieg | Patent-Themen mit signifikantem Wachstum werden per Regression erkannt und am Rückblick geprüft ([DiTTO-LLM](https://ar5iv.labs.arxiv.org/html/2509.09724)) | Themen suchen, die anstiegen, abbrachen und heute wieder wachsen; die Zeitreihen geben CEP, CORDIS und SBIR schon her. |
| Rückblick-Test | DiTTO-LLM prüft seine Methode an vergangenen Zeiträumen | Fälle wie die Luftbilder (alt abgebrochen, später mit KI gelöst) sind ideale Prüfset-Beispiele: Findet unsere Kette sie, würde sie auch heutige finden. |

Den Abgleich per Text-Vektoren haben wir am selben Tag getestet. Er sortiert gute Kandidaten nur schwach nach oben (AUC 0,53 bis 0,61 mit zwei lokalen Modellen). Eine einfache Suche nach benannten technischen Hindernissen schafft 0,71, und die Vektoren verbessern sie nicht. Die Grundlage sind allerdings nur 6 gute Fälle. Der Katalog wirkt deshalb vor allem als Vorgabe in den Anweisungen für Haiku und Opus, nicht als Vektor-Abgleich.

## Quellen und Lesenachweis

Geöffnet und ausgewertet am 9. November 2026:

- [UMA: A Family of Universal Models for Atoms](https://huggingface.co/papers/2506.23971.md)
- [MatterGen, Microsoft Research](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai)
- [AB-UPT, Emmi AI](https://www.emmi.ai/news/ab-upt-scaling-neural-surrogates-100m-cfd-meshes)
- [DINOv3 vs. ImageNet in der Industrieprüfung](https://arxiv.org/html/2605.23472)
- [Extrapolation von Retrosynthese-Modellen, RSC 2026](https://pubs.rsc.org/en/content/articlelanding/2026/dd/d6dd00072j) (nur Kurzfassung)
- [Chronos-2 für Restlebensdauer](https://arxiv.org/html/2606.11990v2)
- [Bayes-Optimierung in der Fertigung, Frontiers 2025](https://www.frontiersin.org/journals/manufacturing-technology/articles/10.3389/fmtec.2025.1614335/full) (rund 93 % gelesen)
- [Inverse Design in der Silizium-Photonik, PeerJ 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12192857/) (rund 90 % gelesen, Schluss fehlt)
- [LingBot-VLA](https://arxiv.org/abs/2601.18692) (nur Kurzfassung)
- [ML für Batterien, RSC 2026](https://pubs.rsc.org/en/content/articlehtml/2026/eb/d6eb00101g)
- [NSF-Workshop KI für Chipentwurf](https://arxiv.org/pdf/2601.14541v3)
- [Codex repliziert Paper zum wissenschaftlichen ML](https://huggingface.co/papers/2607.02134.md) (rund 90 % gelesen)
- [DIW: Tabellen aus historischen Scans](https://www.diw.de/de/diw_01.c.1014976.de/publikationen/externe_referierte_aufsaetze/2026_0014/confidence-based_end-to-end_extraction_of_large_historical_economic_tables_with_llms.html) (nur Zusammenfassung)
- [TU Wien: Orientierung von Luftbildern, EGU 2023](https://meetingorganizer.copernicus.org/EGU23/EGU23-17437.html)
- [Epoch AI: GPU-Preis-Leistung](https://epoch.ai/blog/trends-in-gpu-price-performance)
- [H100-Mietpreise](https://intuitionlabs.ai/pdfs/h100-rental-prices-compared-1-49-6-98-hr-across-15-cloud-providers-2026.pdf) (Datumsangaben im Dokument widersprüchlich)
- [FDA-Liste KI-Medizinprodukte](https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/list-artificial-intelligence-enabled-medical-devices) (nur Teil der Liste geladen, Gesamtzahl nicht geprüft)
- [Sanghera et al., LLM-Ensembles beim Screening](https://www.phc.ox.ac.uk/publications/publication_modal/2093498) (Zusammenfassung)
- [Aktives Lernen beim Screening, Systematic Reviews 2020](https://link.springer.com/doi/10.1186/s13643-020-01521-4)
- [Ke et al.: Sleeping Beauties](https://ar5iv.arxiv.org/html/1505.06454)
- [DiTTO-LLM](https://ar5iv.labs.arxiv.org/html/2509.09724)

Nicht lesbar: ein Aufsatz zu selbstfahrenden Laboren (KIST, Firewall) und eine PMC-Studie zu Sleeping Beauties (Browserprüfung). Zu selbstfahrenden Laboren steht deshalb keine Zahl im Katalog.
