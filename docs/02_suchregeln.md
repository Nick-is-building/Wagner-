> Kopie vom 9. November 2026. Original im Chat: https://claude.ai/artifact/6RAD84rKmFRnVyjDuU2Y5o
> Änderungen trägt der Chat in beide Fassungen ein.

# Suchregeln und Suchprotokoll

Nov 8, 2026 · @Nick

Wir suchen nach Gelegenheiten, bei denen ein wenig beachtetes, wichtiges Problem, passende Daten und eine zahlende oder klar profitierende Seite zusammentreffen. Dieses Regelwerk legt fest, wie wir suchen, bewerten und dokumentieren. Es baut auf Nicks sechs Schritten auf und ergänzt fünf Dinge: die Business-Seite, die Frage „Warum hat das noch niemand gemacht?“, unseren KI-Hebel als Suchfilter, die Prüfung der Datenrechte und zwei Protokolle.

**Gewichtung (entschieden am 8. Nov. 2026):** Wissenschaft und Business zählen insgesamt gleich, aber je nach Phase unterschiedlich. In der Suchphase wiegt die Wissenschaft stärker (×2 gegenüber ×1,5). Sobald ein Kandidat steht, kehrt sich das beim Ausbau um: Dann zählen Verwertung und Geschäftsaufbau stärker. Business bleibt in jeder Phase Pflicht.

## Grundregeln

Zehn Regeln gelten für jede Suche, egal in welchem Feld.

1. **Problem zuerst, Daten kontrolliert umgekehrt.** Wir starten bei Fragen und Widersprüchen. Auffällige Datensätze dürfen eine Frage auslösen, werden aber nach denselben Kriterien bewertet und nicht gesammelt.
2. **Jeder Kandidat braucht zwei Werte.** Einen Erkenntniswert (was wissen wir danach, was vorher niemand wusste?) und einen Verwertungspfad (Paper, Datensatz plus Modell, Dienst oder Produkt, und wer davon profitiert oder zahlt).
3. **„Warum hat das noch niemand gemacht?“ wird beantwortet, bevor wir weitergehen.** Gute Gründe: Sprachbarriere, kürzlich freigegebene Daten, Feldgrenzen, die niemand überschreitet, oder Arbeit, die erst durch KI bezahlbar wurde. Schlechte Gründe: Die Daten taugen nichts, die Frage ist unwichtig, oder sie ist längst in einer anderen Sprache beantwortet.
4. **Wir suchen dort, wo bisher menschliche Lesearbeit der Engpass war:** Übersetzen, Digitalisieren, Extrahieren, Verknüpfen. Dort verschiebt KI die Grenze am stärksten. Die Idee dahinter ist alt: Don Swanson zeigte schon 1986, dass sich aus zwei getrennten Literaturen ein unbemerkter Zusammenhang ableiten lässt (Fischöl und Raynaud-Syndrom).
5. **Machbarkeit wird früh geprüft, nicht am Ende.** Wir arbeiten mit Rechnern, Daten, APIs und GPU-Mietzeit. Labore, Feldmessungen und Studien mit Menschen sind derzeit nicht machbar und führen zum Ausschluss.
6. **Rechte vor Analyse.** Ob wir Daten nutzen und kommerziell verwerten dürfen, klären wir, bevor wir Zeit in die Auswertung stecken.
7. **Erst kartieren, dann spezialisieren.** Feld, Subbereiche, wichtige Gruppen, woran sie gerade arbeiten, wie viele daran arbeiten, was offen ist. Alles im aktuellen Zeitrahmen.
8. **Erkunden und Bestätigen bleiben getrennt.** Was wir beim Stöbern finden, ist eine Hypothese. Bestätigt wird an zurückgehaltenen Daten oder nach Vorregistrierung.
9. **Alles wird protokolliert.** „Gibt es nicht“ sagen wir nur, wenn das Suchprotokoll zeigt, wo und wie gesucht wurde.
10. **Klare Rollen.** Claude schlägt Richtungen vor, recherchiert, rechnet und baut. Nick entscheidet über Richtung, Geld, Auftritt unter seinem Namen und alles Rechtliche. Starke Funde gehen vor jeder Entscheidung in eine unabhängige Gegenprüfung.

## Wo wir suchen: sechs Suchfelder

Die Suchfelder sagen, *wo* wir zuerst graben. Die Felder A bis E haben gemeinsam: Die Methode existiert, aber Aufwand, Sprache oder Zeit haben die Arbeit verhindert. Dort verschiebt KI die Grenze. Feld F sucht umgekehrt dort, wo die Methode selbst an Grenzen stößt.

| Suchfeld | Was wir suchen | Prüffrage | So finden wir Kandidaten |
| --- | --- | --- | --- |
| A Aufwand statt Methode | Fragen, die früher tausende Stunden manueller Auswertung von Dokumenten gebraucht hätten | Gibt es eine anerkannte Methode, und lag es wirklich am Aufwand? | In Limitations-Abschnitten nach Sätzen suchen, in denen Autoren Aufwand als Grund nennen (z. B. „labor-intensive“, „manual coding“, „beyond the scope“) |
| B Isoliertes Wissen | Befunde, die in verschiedenen Sprachen oder Fächern liegen und sich nie begegnet sind | Gibt es zwei Wissensbestände mit kaum Überschneidung, die zusammen etwas Neues ergeben? | Literaturbasierte Entdeckung (Swanson-ABC), nicht englische Datenbanken, Fachbegriffe in mehreren Sprachen |
| C Schlafende Daten | Ältere Messreihen, Laborbücher und Erhebungen, die erst heute bezahlbar digitalisiert und neu ausgewertet werden können | Ist das Material zugänglich, und bekommen wir die Erlaubnis der Besitzer? | Datenrettung ist ein eigenes Feld mit Verzeichnissen, etwa der [Copernicus-Dienst](https://climate.copernicus.eu/coordination-data-rescue-activities) mit I-DARE und ACRE für Klimadaten; dazu Sozialdaten ([DataFirst](https://www.datafirst.uct.ac.za/node/473735)) und Nachlässe von Forschungseinrichtungen ([USDA-Bibliothek](https://drum.lib.umd.edu/items/9234302c-4231-4442-8453-fcd39f3fa603)) |
| D Abgebrochene Linien | Versuche und Datenreihen, die früh endeten und sich heute fortsetzen oder verbessern lassen | Warum wurde abgebrochen? Nur Geld, Personal oder Technik ist ein guter Grund; ein negatives Ergebnis ist es nicht. Und: Geht die Fortsetzung am Rechner oder mit öffentlichen Daten? | Nach „discontinued“, „funding ended“, „project terminated“ suchen; eingestellte Messreihen, verwaiste Datensätze und Repositories |
| E Methodentransfer (Vorschlag Claude) | Eine in Feld X etablierte Methode, die in Feld Y nie angewendet wurde, obwohl die Daten passen | Hält die Annahme der Methode im neuen Feld? | Methodenbegriffe aus Feld X in der Literatur von Feld Y suchen; null oder wenige Treffer sind ein Signal |
| F Grenzen bestehender Verfahren | Etablierte Verfahren, die unter bestimmten Bedingungen nachweislich versagen oder systematisch falsch liegen, und wo neue Daten oder Ansätze messbar helfen könnten | Ist die Schwäche in der Praxis belegt, aber in der Forschung kaum bearbeitet? Schwächen, die viele Paper offen benennen, sind meist schon umkämpft. | Fehlerberichte, Issue-Tracker, Nutzerforen und Praxisberichte mit der Literatur abgleichen: Fehlerklassen, die in der Praxis oft auftauchen und in Papern selten |

Suchfeld C ist in der Klimaforschung bereits gut besetzt; dort lohnen sich eher die Lücken, die die Verzeichnisse selbst ausweisen. In Agrar-, Sozial- und Industriedaten ist deutlich weniger los. Bei Suchfeld D fallen alle Fortsetzungen weg, die ein Labor oder Feldarbeit brauchen. Suchfeld F hat den klarsten Business-Wert, verlangt aber die meiste technische Tiefe: Eine nachweislich bessere Methode zu bauen ist schwerer, als Daten zu erschließen.

## Der Suchablauf

Neun Schritte, jeder endet mit einem festen Ergebnis. Fällt ein Kandidat an einem Tor durch, geht er mit einem Vermerk im Kandidatenregister zurück, statt still zu verschwinden.

&#91;embedded content: Suchablauf · 9 Schritte, 3 Tore\]

Die Umkehrsuche (Schritt 4) speist neue Kandidaten in Schritt 2 ein; danach laufen alle Kandidaten denselben Weg.

1. **Problemräume öffnen.** In den sechs Suchfeldern, fachübergreifend, nach ungelösten Fragen, widersprüchlichen Befunden und unverstandenen Phänomenen suchen. Jede Lücke bekommt einen Typ: Evidenz-, Wissens-, Methoden-, Populations-, Theorie-, Praxis-Wissens- oder empirische Lücke. *Ergebnis:* Kandidatenliste mit Lückentyp.
2. **Aufmerksamkeit messen und „Warum noch nicht?“ klären.** Konkurrenz auf drei Ebenen messen: im Gesamtfeld, bei der konkreten Teilfrage und beim konkreten Ansatz oder Datenbestand. Entscheidend ist die Teilfrage. Ein volles Gesamtfeld ist sogar ein Vorteil, weil Daten, Vergleichsmaßstäbe und zahlende Nutzer dort schon existieren. Dazu: Laufen Vorabveröffentlichungen oder registrierte Studien? Und ein kurzer Business-Blick: Wer hat dieses Problem, und gibt es Hinweise, dass jemand dafür zahlt? Außerdem der Grund für die Lücke nach Regel 3. *Tor:* schlechter Grund oder die Teilfrage selbst ist dicht besetzt → zurück.
3. **Gezielt Datenquellen suchen.** Regionale Archive, historische Messreihen, Institute, nicht englische Literatur und Register. *Ergebnis:* pro Kandidat zwei bis fünf Datenquellen mit Zugangsweg.
4. **Umkehrsuche.** Parallel auffällige, wenig genutzte Datensätze sammeln und fragen, welche Frage sie beantworten könnten. Auch hier gilt: zwei getrennte Wissensbestände, die kaum Überschneidung haben, sind die interessantesten (in der Literatur „scientific arbitrage“ genannt). *Ergebnis:* neue Kandidaten für Schritt 2.
5. **Rechte und Artefakte vorprüfen.** Lizenz, kommerzielle Nutzbarkeit, Zugriffsbedingungen. Dazu ein erster Blick, ob auffällige Muster aus Messwechseln stammen könnten. *Tor:* Nutzung unklar oder nur nicht kommerziell bei geplantem Business-Pfad → Nick entscheidet.
6. **Bewerten.** Mit dem Bewertungsraster unten. *Ergebnis:* Rangliste, die besten drei gehen weiter.
7. **Kurzer Datentest.** Ein bis zwei Tage pro Kandidat, nur zur Machbarkeit: Sind die Daten nutzbar, vollständig und verständlich? Reichen Menge und Auflösung, um einen Effekt der Größe, die uns interessiert, überhaupt sehen zu können? Den Bestätigungsteil der Daten fassen wir dabei nicht an. *Tor:* Daten unbrauchbar oder zu grob für die Frage → zurück, mit Befund. Ein frühes Signal ist ein Pluspunkt, sein Fehlen allein ist kein Ausschluss.
8. **Hypothesen schärfen und vorregistrieren.** Präzise Hypothesen mit vorher festgelegten Schwellen, Daten aufteilen in Erkundungs- und Bestätigungsteil. *Ergebnis:* Vorregistrierung und Versuchsplan mit Kostenschätzung.
9. **Verwertungspfad festlegen.** Was wir veröffentlichen, was wir als Datensatz plus Modell aufbauen und was davon ein Produkt oder Dienst wird. *Ergebnis:* Entscheidungsvorlage für Nick.

## Werkzeuge und Quellen

Für jeden Schritt gibt es frei nutzbare Werkzeuge. Paper-Suche (alphaXiv) und Hugging Face sind in unserer Arbeitsumgebung bereits angebunden.

| Schritt | Werkzeug oder Quelle | Wofür wir es nutzen |
| --- | --- | --- |
| 1 Lückentyp | [Taxonomie nach Miles und AHRQ-Rahmen nach Robinson](https://paperguide.ai/blog/how-to-find-research-gaps/) | Sieben Lückentypen; vier Gründe, warum Evidenz nicht reicht: zu wenig, verzerrt, widersprüchlich, nicht die richtige Information |
| 2 Aufmerksamkeit | [OpenAlex](https://help.openalex.org/data/topics/) | Frei abfragbarer Katalog; rund 4.500 Themen mit Zahl der Arbeiten und Zitationen, gruppierbar nach Jahr und Institution |
| 2 Laufende Arbeit | arXiv, medRxiv, SSRN, OSF Registries | Vorabveröffentlichungen und registrierte Studien, die eine Lücke gerade schließen |
| 1, 4 Verdeckte Verbindungen | [Literaturbasierte Entdeckung](https://peerj.com/articles/cs-235) (Swanson-ABC-Modell) | Zusammenhänge zwischen zwei Literaturen finden, die einander nicht zitieren |
| 3 Nicht englische Literatur | CNKI (China), [J-STAGE](https://jmla.pitt.edu/ojs/jmla/article/view/1448/2197) (Japan, über 3.000 Zeitschriften), SciELO (Lateinamerika, Iberien), AJOL (Afrika), Cairn (Frankreich), DOAJ mit Sprachfilter | Studien, die in englischen Datenbanken fehlen |
| 3 Datenrepositorien | [re3data](https://digitalcommons.unl.edu/libphilprac/5193), Zenodo, PANGAEA, Hugging Face | Register aller Forschungsdaten-Archive; filterbar nach Fach und Lizenz. Deutschland stellt 433 Archive (Stand 2021) |
| 9 Nachfragesignale | [TED](https://apify.com/siccscha/ted-tender-scraper), EU-Ausschreibungsportal | Wofür öffentliche Stellen tatsächlich Geld ausgeben; laut Anbieterseite offene EU-Daten, kommerziell nutzbar |
| 9 Nachfragesignale | Förderaufrufe, Stellenanzeigen, öffentliche Beschwerden (eigener Vorschlag, noch nicht geprüft) | Wer ein Problem so dringend hat, dass er dafür Geld oder Personal einsetzt |

Warum sich nicht englische Quellen lohnen, ist gut belegt. 2014 war gut ein Drittel von rund 75.000 Arbeiten zum Naturschutz nicht englisch, etwa die Hälfte davon ohne englischen Titel oder Abstract ([Amano et al. 2016](https://www.ft.lk/FT-Education/languages-still-a-major-barrier-to-global-science-new-research-finds/10515-589266)). Eine Folgestudie zeigte: Nicht englische Studien erweitern die räumliche Abdeckung der Evidenz um 12 bis 25 % und die Artenabdeckung um 5 bis 32 %. Sie haben aber oft schwächere Studiendesigns ([Amano et al. 2021](https://research.hub.ku.edu.tr/entities/publication/01934061-0682-4d44-93e0-ab91e1a270d6/full)). Das ist unser Vorteil und zugleich ein Prüfpunkt.

## Bewertungsraster

Jedes Kriterium bekommt 0 bis 3 Punkte und wird mit seinem Gewicht multipliziert; höchstens 48 Punkte. Die Gewichte gelten für die Suchphase (Wissenschaft ×2, Business ×1,5, Machbarkeit ×1); in der Ausbauphase tauschen Wissenschaft und Business ihre Gewichte.

| Bereich | Kriterium | Prüffrage | Gewicht |
| --- | --- | --- | --- |
| Wissenschaft | Bedeutung | Ändert die Antwort eine Entscheidung, eine Theorie oder eine Praxis? Wer wäre betroffen? | 2 |
| Wissenschaft | Geringe Bearbeitung | Wenig Konkurrenz bei genau dieser Teilfrage und diesem Ansatz (nicht im Gesamtfeld), keine laufenden Studien, guter Grund für die Lücke? | 2 |
| Wissenschaft | Erkenntnispotenzial | Wissen wir danach etwas, das vorher niemand wusste, auch wenn das Ergebnis negativ ausfällt? | 2 |
| Wissenschaft | Überprüfbarkeit | Kann jemand anderes den Befund mit öffentlichen Daten und unserem Code nachrechnen? | 2 |
| Business | Profitierende Seite | Gibt es eine konkrete Gruppe, die für das Ergebnis zahlen würde oder klar profitiert? | 1,5 |
| Business | Nachfragesignal | Ist der Bedarf belegt, etwa durch Ausschreibungen, Förderaufrufe, Stellen oder Beschwerden? | 1,5 |
| Business | Pull statt Push | Kommen Nutzer von selbst, über Suche, Marktplätze oder Veröffentlichungen, ohne Kaltakquise und lange Gespräche? | 1,5 |
| Business | Verteidigbarkeit | Entsteht etwas schwer Kopierbares, etwa ein eigener Datensatz plus Modell oder ein Vorsprung durch laufende Pflege? | 1,5 |
| Machbarkeit | Mittel und Zeit | Mit Rechnern, Budget von ca. 200–500 € im Monat und bis Sommer 2027 erreichbar, mit einem ersten nutzbaren Zwischenergebnis nach wenigen Monaten? | 1 |
| Machbarkeit | Daten | Gute Qualität, zugänglich, Nutzung erlaubt? | 1 |

**Pflichtregel:** Mindestens ein Business-Kriterium hat 2 oder mehr Punkte. Sonst geht der Kandidat nicht über Schritt 6 hinaus, egal wie hoch die Gesamtpunktzahl ist.

**Ausschlusskriterien**, unabhängig von der Punktzahl:

- Die Lücke ist geschlossen: Die Studie, die sie füllen würde, existiert bereits.
- Der Grund für die Lücke ist schlecht (Regel 3).
- Es braucht Labor, Feldmessungen oder Studien mit Menschen.
- Die Daten dürfen wir für den geplanten Pfad nicht nutzen.
- Wissen, Medien oder Kurse wären das Hauptgeschäft.

**Letzte Prüfung vor Schritt 8: Heilmeiers acht Fragen.** Der frühere DARPA-Direktor George Heilmeier ließ jedes Forschungsprogramm diese Fragen beantworten; DARPA führt sie bis heute als acht Fragen ([CASRAI](https://casrai.org/guides/heilmeier-catechism), Wortlaut nach [Murray Wiki, Caltech](https://murray.cds.caltech.edu/Heilmeier_Catechism)): Was wollen wir tun, ohne Fachjargon? Wie wird es heute gemacht, und wo liegen die Grenzen? Was ist neu, und warum wird es funktionieren? Wen interessiert es, und was ändert sich bei Erfolg? Welche Risiken und welcher Ertrag? Was kostet es? Wie lange dauert es? Woran messen wir Zwischen- und Endergebnis?

**Wer entscheidet was**

| Entscheidung | Schlägt vor | Entscheidet |
| --- | --- | --- |
| Suchrichtung und Felder | Claude, Nick bringt Beobachtungen ein | gemeinsam, bei Uneinigkeit Nick |
| Kandidaten weiterverfolgen oder verwerfen | Claude mit Bewertung | Nick |
| Kostenpflichtige Läufe | Claude mit Kostenschätzung | Nick |
| Datenrechte, Auftritt unter Nicks Namen | Claude bereitet vor | Nick |
| Methodik und Versuchsaufbau | Claude | Claude, Gegenprüfung vor dem Start |

## Suchprotokoll

Das Suchprotokoll ist ein Logbuch jeder Suche: wo, womit, wann, mit welchem Ergebnis. Es erfüllt drei Zwecke. Wir suchen nichts doppelt. Eine Aussage wie „dazu gibt es nichts“ ist belegt statt behauptet. Und Wissen geht beim Wechsel zwischen Chats und Claude Code nicht verloren, weil es in einer Datei steht, nicht im Gedächtnis.

Als Maßstab dient PRISMA-S, ein Standard mit 16 Punkten dafür, Literatursuchen so zu dokumentieren, dass andere sie wiederholen können ([Rethlefsen et al. 2021](https://pubmed.ncbi.nlm.nih.gov/33499930/)). Wir übernehmen davon den Kern: Quelle, Suchbegriffe, Filter, Datum und Trefferzahl. Dazu kommt, was wir tatsächlich gelesen haben, denn ein Abstract ist kein gelesener Volltext.

**Vorlage Suchprotokoll** (eine Zeile pro Suche, neueste oben)

| Datum | Schritt | Quelle | Suchbegriffe und Sprache | Filter | Treffer | Gelesen | Ergebnis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-08 | Regelwerk | Web-Suche | Methoden zur Lückensuche, Suchprotokolle, Datenrechte (en) | keine | ca. 10 je Suche | 2 Seiten voll, Rest Ausschnitte | Grundlage dieses Dokuments |

**Vorlage Kandidatenregister** (eine Zeile pro Kandidat, auch die verworfenen)

| Kandidat | Lückentyp | Warum noch nicht? | Datenquellen | Punkte | Status | Vermerk |
| --- | --- | --- | --- | --- | --- | --- |
| Beispiel: Frage X in Region Y | Populationslücke | Studien nur auf Chinesisch | CNKI, Landesarchiv Z | – | Offen | Beispielzeile, löschen |
|  |  |  |  |  |  |  |

Im Repository legen wir beide Tabellen später als Dateien an (z. B. SUCHPROTOKOLL.md und KANDIDATEN.md), damit Claude Code dieselbe Grundlage hat.

## Prüfprotokoll für Funde

Das Suchprotokoll hält fest, wie wir gesucht haben. Das Prüfprotokoll hält fest, ob ein Fund trägt. Jeder Kandidat, der Schritt 7 besteht, durchläuft diese Liste, und das Ergebnis jedes Punkts wird notiert.

- [ ] **Die schließende Studie gesucht.** Wir beschreiben die Studie, die unsere Lücke füllen würde, und suchen gezielt nach genau ihr: in Datenbanken, Vorabveröffentlichungen, Registern und grauer Literatur wie Abschlussarbeiten und Behördenberichten ([Paperguide-Leitfaden](https://paperguide.ai/blog/how-to-find-research-gaps/)). Ergebnis: Lücke besteht, wird enger oder ist geschlossen.
- [ ] **Laufende Arbeit geprüft.** OSF Registries, Studienregister, arXiv und andere Server der letzten zwölf Monate.
- [ ] **Artefakte ausgeschlossen.** Viele lange Messreihen enthalten künstliche Sprünge durch Standortwechsel, neue Instrumente oder geänderte Messpraxis; dafür gibt es eigene Testverfahren ([Atmosphere 2024](https://mdpi.com/2073-4433/15/8/957)). Wir prüfen die Metadaten der Quelle und testen auf Bruchpunkte, bevor wir ein Muster deuten.
- [ ] **Studienqualität bewertet,** besonders bei nicht englischen Quellen, die im Schnitt schwächere Designs haben.
- [ ] **Erkunden und Bestätigen getrennt.** Wer Daten schon gesehen hat, wird von ihnen beeinflusst. Deshalb Vorregistrierung vor der Bestätigung, nach der Vorlage für bereits existierende Daten mit 25 Fragen ([van den Akker et al. 2021](https://conferences.lnu.se/index.php/metapsychology/article/view/2625)), oder ein vorher abgetrennter Bestätigungsteil der Daten.
- [ ] **Datenrechte geklärt.** CC0 und CC BY erlauben kommerzielle Nutzung. Bei CC BY-NC ist schon unscharf, was als kommerziell gilt, und sie ist für Datensätze verbreitet unerwünscht ([CASRAI](https://casrai.org/compare/cc-by-vs-cc-by-nc), [Max Planck Digital Library](https://rdm.mpdl.mpg.de/after-research/licenses/)). Fällt der Business-Pfad darunter, entscheidet Nick, ob wir weitergehen.
- [ ] **Jede Quelle geöffnet.** KI-erzeugte Literaturangaben sind oft falsch: In einer Untersuchung waren 55 % der Angaben von GPT-3.5 und 18 % der Angaben von GPT-4 erfunden (Walters und Wilder 2023, zitiert nach dem Paperguide-Leitfaden). Wir zitieren nur, was wir gelesen haben.
- [ ] **Unabhängig gegengeprüft.** Ein Prüfer, der die Arbeit nicht mitgebaut hat: ein separater Agent, Gemini oder ein kalter Chat. Er bekommt Behauptung, Daten und Code, nicht unsere Begründung.
- [ ] **Ergebnis im Kandidatenregister eingetragen,** auch wenn es negativ ist. Ein sauber belegtes Nein ist ein Befund.

## Quellen und Lesenachweis

Keine tragende Regel hängt an einer ungelesenen Quelle. Die Details zu PRISMA-S und die Originalarbeiten von Robinson und Miles kenne ich nur aus Zusammenfassungen; sie liefern Begriffe, keine Zahlen, auf die wir uns verlassen.

| Quelle | Status | Lücke und Grund | Folge |
| --- | --- | --- | --- |
| [Paperguide: How to Find Research Gaps](https://paperguide.ai/blog/how-to-find-research-gaps/) (Okt. 2026) | vollständig gelesen | Anbieter mit Eigeninteresse; Zahlen anderer Studien nur aus zweiter Hand | Lückentypen, Gründe, Prüfschritte gut belegt; Walters und Wilder nur sekundär |
| [PRISMA-S](https://pubmed.ncbi.nlm.nih.gov/33499930/) | nur Zusammenfassung | die 16 Punkte im Einzelnen nicht gelesen | Vorlage nutzt nur den Kern; Abgleich mit der Checkliste offen |
| [Swanson-ABC und literaturbasierte Entdeckung](https://peerj.com/articles/cs-235) | nur Suchausschnitte | Volltext nicht abgerufen | keine, nur als Idee genutzt |
| [OpenAlex, Themen](https://help.openalex.org/data/topics/) | nur Suchausschnitte | Doku nicht vollständig | Abfragedetails prüfen wir beim ersten Einsatz |
| [Amano et al. 2016](https://www.csmonitor.com/Science/2017/0102/Language-barriers-still-burden-science-new-study-suggests), [Amano et al. 2021](https://research.hub.ku.edu.tr/entities/publication/01934061-0682-4d44-93e0-ab91e1a270d6/full) | nur Presse und Datenbankeinträge | Originalartikel nicht gelesen | Zahlen stimmen über mehrere Quellen überein |
| [Heilmeier-Fragen](https://casrai.org/guides/heilmeier-catechism) | nur Suchausschnitte | DARPA-Seite nicht direkt geöffnet | keine, Fragen in mehreren Quellen gleich |
| [re3data-Auswertung 2021](https://digitalcommons.unl.edu/libphilprac/5193), [J-STAGE-Angabe](https://jmla.pitt.edu/ojs/jmla/article/view/1448/2197) | nur Zusammenfassung bzw. Ausschnitt | Volltexte nicht gelesen | Zahlen als ungefähre Größenordnung |
| [TED-Datennutzung](https://apify.com/siccscha/ted-tender-scraper) | nur Ausschnitt einer Anbieterseite | offizielle Nutzungsbedingungen nicht gelesen | kommerzielle Nutzbarkeit vor Einsatz an der Originalquelle prüfen |
| [van den Akker et al. 2021](https://conferences.lnu.se/index.php/metapsychology/article/view/2625) | nur Zusammenfassung | Vorlage selbst nicht gelesen | keine |
| Lizenzen: [CASRAI](https://casrai.org/compare/cc-by-vs-cc-by-nc), [MPDL](https://rdm.mpdl.mpg.de/after-research/licenses/) | nur Ausschnitte | keine Rechtsberatung | rechtliche Bewertung bleibt bei Nick |
| [Homogenisierung von Messreihen](https://mdpi.com/2073-4433/15/8/957) | nur Ausschnitt | Volltext nicht gelesen | keine, nur als Beispiel für Artefakte |

Nachtrag Suchfelder: Copernicus-Datenrettung, DataFirst und der USDA-Bericht zur Datenrettung wurden nur in Suchausschnitten gelesen. Sie belegen, dass Datenrettung ein etabliertes Feld mit Verzeichnissen ist; Details zu deren Lückenlisten prüfen wir, wenn wir Suchfeld C angehen.
