> Kopie vom 9. November 2026. Original im Chat: https://claude.ai/artifact/A6L26syDXiuRsw1gsa3zoz
> Änderungen trägt der Chat in beide Fassungen ein.

# Feldkarte: Aufgegebene Forschung

Nov 8, 2026 · @Nick

Nicht fortgeführte Forschung lässt sich systematisch finden, auf zwei Wegen: über Register, die Abbrüche selbst kennzeichnen, und über Berichte mit unerreichten Zielen. Am 8. November 2026 habe ich die Quellen selbst abgerufen oder ihren Zugang getestet, um zu sehen, ob wir die Daten wirklich beziehen können. Bester Einstieg ist jetzt Tschechien: Das Register CEP liegt komplett als offene Datei vor, mit 569 gestoppten und rund 1.370 Projekten mit verfehltem Ziel, meist mit Begründungstext. Dazu kommen die EU-Datenbank CORDIS, der österreichische FWF, das US-Programm SBIR und Japans KAKEN. GEPRIS und das ukrainische NRAT lassen sich nur von Hand lesen; Russland, China und Kasachstan fallen weg. Das Ziel bleibt, einen Ansatz selbst fortzuführen; die Suche ist das Werkzeug dafür.

## Abbruchgründe

Ein abgebrochenes Projekt ist nur dann ein Kandidat, wenn der Grund für den Abbruch heute weggefallen ist. Sechs Typen, drei davon sind unser Kern.

| Abbruchgrund | Typisches Beispiel | Für uns | Was heute hilft |
| --- | --- | --- | --- |
| Auswertung zu aufwendig | Zu viele Messdaten, Fotos, Akten; Sprachbarriere | Kern | KI liest, übersetzt, extrahiert und verknüpft |
| Technik fehlte | Rechenleistung, Simulation, Sensorik oder Messgenauigkeit reichten nicht | Kern, wenn heute am Rechner lösbar | Rechenleistung, Simulation, gelernte Modelle als Ersatz für teure Rechnungen |
| Geld oder Strukturen fielen weg | Ende der Förderung, Auflösung von Instituten nach 1991 oder 1990 | Kern, wenn die Wissenschaft intakt war | Öffentliche Daten, günstige Rechenzeit, KI statt Personal |
| Krieg oder politischer Umbruch | Ukraine seit 2022, DDR-Institute nach 1990 | gut, mit Sorgfalt | wie oben; Kooperation mit den ursprünglichen Forschenden prüfen |
| Geheimhaltung | eingestufte Vorhaben | nur, wenn öffentlich zugänglich und zivil oder defensiv | keine Sonderwege |
| Idee widerlegt | negatives Ergebnis | nein, außer der Grund war ein heute behebbarer Messfehler | Nachrechnen mit besseren Methoden |

Die Prüffrage für jeden Kandidaten lautet: Was genau fehlte damals, und gibt es das heute nachweislich, möglichst am Rechner?

## Was als nicht fortgeführt zählt

Ein beendetes Projekt ist nicht automatisch ein aufgegebenes. Wir suchen deshalb nach **nicht fortgeführten Forschungsansätzen** und ordnen jeden Kandidaten einer von fünf Klassen zu. B und C sind oft wertvoller als A: Ein Projekt kann offiziell erfolgreich abgeschlossen sein, und trotzdem fand die eigentlich spannende Weiterentwicklung nie statt.

| Klasse | Bedeutung | Beleg, den wir brauchen |
| --- | --- | --- |
| A Nachweislich abgebrochen | vor dem geplanten Ende beendet, Ziel nicht erreicht | Statusvermerk im Register oder Bericht |
| B Abgeschlossen, nicht weiterverfolgt | Ergebnis oder Ansatz liegt vor, aber keine Folgearbeit | keine Folgeprojekte, Folgepublikationen oder Zitationen, die daran anknüpfen |
| C Zurückgestellt | Fortsetzung war geplant, scheiterte an einem benannten Hindernis | Aussage im Bericht, z. B. zu fehlender Rechenleistung oder fehlenden Daten |
| D Status ungeklärt | Hinweis auf eine Lücke, aber kein Beleg für einen Abbruch | bleibt im Register, bis ein Beleg auftaucht |
| E Bewilligt, nie begonnen | Idee hat die Begutachtung bestanden, wurde aber nie umgesetzt | Status „zurückgelegt“ (FWF: 284, davon 162 mit Beschreibung) oder „abgelehnte Bewilligung“ (ARC: 43) |

## Zwei Suchwege

Wir suchen auf zwei Wegen, die sich ergänzen. Der erste findet Kandidaten schnell, der zweite liefert Grund und heutigen Hebel.

**Weg 1: Status-Suche.** Manche Register kennzeichnen selbst, was nicht zu Ende kam. Am klarsten ist Tschechien: Das Register CEP führt 569 gestoppte Projekte und bewertet abgeschlossene Projekte mit Code und kurzem Begründungstext. CORDIS führt 3.379 EU-Projekte als „TERMINATED“, die meisten davon Einzelstipendien. KAKEN kennt den Status „Discontinued“. Der FWF zeigt in seiner Schnittstelle nur 284 zurückgelegte Projekte, die nie begonnen wurden; abgebrochene laufende Projekte erkennt man dort nicht. Stufenprogramme zeigen, welche Phase-I-Ideen keine Phase II bekamen (SBIR). Der Haken: Außer in Tschechien habe ich zu keinem Statusvermerk eine Begründung gefunden.

**Weg 2: Ziel-Lücken-Suche.** Wir lesen Abschluss- und Zwischenberichte und extrahieren vier Felder: *ursprüngliches Ziel → unerledigter Teil → damaliges Hindernis → heutige Lösungsmöglichkeit*. Forschende müssen dafür nichts als gescheitert bezeichnen. Es reicht ein Satz wie „wegen begrenzter Rechenkapazität nicht untersucht“ oder „die Daten reichten nicht aus“. Danach prüfen wir mit dem Prüfprotokoll, ob jemand die Frage inzwischen beantwortet hat.

Weg 1 liefert Kandidaten mit Etikett, Weg 2 liefert den Inhalt. Am stärksten sind Fälle, die auf beiden Wegen auftauchen.

## Quellen mit frei beziehbaren Daten

Diese Quellen habe ich am 8. November 2026 selbst abgerufen. Die Zahlen stammen aus den heruntergeladenen Dateien, nicht aus Webseiten. Alle sind ohne Antrag zugänglich; nur KAKEN braucht eine kostenlose Registrierung. Komplett geladen habe ich CEP, CORDIS, FWF und SBIR; bei den übrigen habe ich Schnittstelle oder Einzeldateien getestet.

| Quelle | Was drinsteht (gezählt) | Zugang, getestet | Für uns |
| --- | --- | --- | --- |
| [CEP, IS VaVaI](https://www.isvavai.cz/opendata) (Tschechien) | 63.151 Projekte 1985–2026 mit Zielen, Status, Bewertung und Bewertungstext; 569 gestoppt, 29 unterbrochen; Ziel nicht erfüllt: 928 bei eingehaltenem Vertrag, 157 mit Sanktion, 287 mit altem Code N (1998–2007) | eine CSV-Datei (161 MB) im nationalen Open-Data-Katalog, Stand 9.10.2026, ohne Konto | sehr hoch: Abbruch und Begründung in einer Datei; keine Volltextberichte |
| [CORDIS](https://cordis.europa.eu/data/cordis-h2020projects-csv.zip) (EU) | Horizon 2020: 35.389 Projekte, 2.132 „TERMINATED“; FP7: 25.785, davon 190; Horizon Europe: 23.954, davon 1.057; Berichtszusammenfassungen als eigene Datei | CSV-Pakete ohne Konto; Nachnutzung nach dem Weiterverwendungsbeschluss der Kommission (2011/833/EU) | hoch: 1.852 der H2020-Abbrüche sind Einzelstipendien; die übrigen 280 umfassen 113 ERC- und 56 KMU-Projekte; Horizon Europe bringt rund 100 weitere außerhalb der Stipendien |
| [FWF Open API](https://www.fwf.ac.at/fileadmin/Website/Dokumente/Entdecken/Forschungsradar/Open_API/fwf_open_api_documentation_1.1_v2.pdf) (Österreich) | 20.602 Projekte; 10.485 mit öffentlicher Endbericht-Zusammenfassung; 284 „zurückgelegt“, also bewilligt und nie begonnen, 162 davon mit Projektbeschreibung | API mit öffentlichem Leseschlüssel, CC0; alle Projekte geladen | hoch für Weg 2 und für nie begonnene Ideen; vorzeitig abgebrochene laufende Projekte sind nicht erkennbar |
| [SBIR/STTR](https://www.sbir.gov/awards) (USA) | 144.660 Phase-I- und 63.071 Phase-II-Förderungen 1983–2024, je mit Antragszusammenfassung; keine Abschlussberichte | eine CSV-Datei (368 MB) ohne Konto | hoch für Business: 38.257 Phase-I-Projekte ohne Phase II bei gleicher Firma und gleichem Thema, gezählt unter den 61.603 mit Themenkürzel; laut Textabgleich wurden 16–30 % davon wohl unter anderem Thema fortgesetzt, rund 35 % stammen von Firmen ohne jede spätere Phase II; Rechte bei den Firmen |
| [KAKEN](https://support.nii.ac.jp/ja/kaken/about/terms) (Japan) | Projekte, Jahres- und Abschlussberichte; Status u. a. „Discontinued“ und „Suspended“ | Projektseiten laut robots.txt erlaubt, Sitemap vorhanden; [API](https://support.nii.ac.jp/ja/kaken/api/api_outline) mit kostenloser App-ID; Inhalte CC-BY-kompatibel, Berichte bis 2015 teils mit Autorenrecht | hoch; Zahl der Abbrüche noch nicht gezählt |
| [NASA NTRS](https://sti.nasa.gov/harvesting-data-from-ntrs/) (USA) | über 500.000 Einträge, technische Berichte seit 1915 | API ohne Schlüssel, Jahresdateien zum Massendownload; Regierungswerke frei, einzelne Einträge nicht | hoch für Technik, Weg 2 |
| [Aufgegebene US-Patentanmeldungen](https://doi.org/10.7910/DVN/Q4Q32F) | „wirklich aufgegebene“ veröffentlichte Anmeldungen 2000–2017 (Cotropia und Schwartz) | eine Datei (6,7 MB), CC0, nicht gesperrt | hoch für Business |
| [TIB RENATE](https://oa.tib.eu/renate/) (Deutschland) | Abschlussberichte öffentlich geförderter Projekte als PDF | einzelne PDFs frei, Lizenz je Bericht (Beispiel CC BY-ND); Suche für Bots gesperrt; die Sitemap ist abrufbar und listet alle Einträge; Massenabruf der PDFs nicht getestet | mittel bis hoch: deutsche Volltexte |
| [Gateway to Research](https://gtr.ukri.org/resources/gtrapi2.html) (UK) | 158.710 Projekte mit Zusammenfassung, technischer Zusammenfassung und Kernbefunden | API ohne Schlüssel, Open Government Licence | mittel: Status nur aktiv oder abgeschlossen |
| [IDRC Digital Library](https://idl-bnc-idrc.dspacedirect.org/) (Kanada) | Entwicklungsforschung in Afrika, Asien, Lateinamerika; 2.956 Treffer für „final technical report“ | DSpace mit Harvesting-Schnittstelle, ohne Konto; Rechte beim IDRC, als Open Access gekennzeichnet, eine allgemeine Nachnutzungslizenz nicht gefunden | mittel bis hoch: bester gefundener Weg nach Afrika |

Ebenfalls frei, aber ohne Abbruchvermerk und ohne Berichte, also nur für Abgleiche: [SNSF](https://data.snf.ch/datasets) (91.800 Projekte), [ARC Australien](https://dataportal.arc.gov.au/NCGP/API/grants) (34.977, darunter 43 abgelehnte Bewilligungen), [RAD-on Polen](https://radon.nauka.gov.pl/opendata/polon/projects) (48.731 Projekte mit Zusammenfassung), die NSF-Schnittstelle der USA und das kenianische [Nationale Repositorium](https://repository.nrf.go.ke/) mit rund 2.650 Einträgen.

Bei der zweiten Prüfrunde neu dazugekommen:

| Quelle | Was drinsteht (gezählt) | Zugang, getestet | Für uns |
| --- | --- | --- | --- |
| [Grant Witness](https://grantwitness.org/) (USA) | 2025/26 gekündigte oder eingefrorene Bundesförderungen: NIH 5.776 Fälle (1.161 weiterhin gekündigt), NSF 2.031 (1.400 weiterhin gekündigt), dazu EPA, CDC, SAMHSA und AHRQ; je mit Abstract, Restsumme und ursprünglicher Laufzeit | Archiv auf [Zenodo](https://zenodo.org/records/23577373), CC0, wöchentlich aktualisiert; komplett geladen | hoch: frischer Abbruch aus politischen Gründen, nicht wegen der Idee; Themen oft Gesundheit und Sozialwissenschaft |
| [USPTO-Gebührenereignisse](https://catalog.data.gov/dataset/patent-grant-maintenance-fee-events-september-1-1981-present-7d26f) | alle US-Patente seit 1981 mit Gebührenzahlungen und Verfall wegen Nichtzahlung | Textdateien, gemeinfrei, wöchentlich; Download noch nicht getestet | hoch für Business: zeigt, welche Technik ihr Inhaber aufgegeben hat; verfallene Patente sind frei nutzbar, sofern keine anderen Rechte greifen |
| [OSTI](https://www.osti.gov/api/v1/docs) (US-Energieministerium) | 314.529 technische Berichte mit Volltext | API ohne Schlüssel getestet | hoch für Technik, Weg 2 |
| [OpenAlex](https://help.openalex.org/api/) | weltweiter Katalog wissenschaftlicher Publikationen | Grundnutzung frei, CC0; kostenloser Schlüssel erhöht das Tageslimit, Mehrnutzung kostet | Werkzeug für den Fortsetzungscheck, keine Quelle |

## Quellen nur von Hand, mit Antrag oder gestrichen

Zwei der früher hoch eingestuften Quellen, GEPRIS und NRAT, lassen sich nur von Hand lesen. Russland, China und Kasachstan fallen weg. Für den Test zählen diese Quellen nicht; für eine Tiefenrecherche in einem festen Fachgebiet bleiben die lesbaren nutzbar.

| Quelle | Was die Prüfung ergab | Folge |
| --- | --- | --- |
| GEPRIS, DFG (Deutschland) | robots.txt sperrt alle Programme außer Suchmaschinen; keine API; Seiten sind abrufbar | von Hand lesen; für eine Massenauswertung müsste Nick die DFG um Erlaubnis bitten |
| NRAT (Ukraine) | einzelne Seiten über den Web-Reader lesbar; automatischer Abruf aus der Cloud wird vom Server abgebrochen; Downloads mit Konto und [Download-Limit](https://nrat.ukrintei.ua/naczionalnyj-repozytarij-akademichnyh-tekstiv-u-2020-roczi/?pdf=11073) | von Hand über Nicks Browser; Massenabruf nicht möglich |
| TÜBİTAK über TR Dizin (Türkei) | laut [TÜBİTAK](https://tubitak.gov.tr/en/node/14510) Abschlussberichte seit 1965 frei im Volltext, Verteidigungsprojekte ausgenommen; unser Reader wird per robots.txt abgewiesen | von Hand; Massenabruf bei ULAKBİM anfragen |
| Archiv der BBAW, DDR-Akademie | [Benutzung](https://archiv.bbaw.de/en/the-academy-archive/utilisation-order) nach Zulassung durch das Archiv, Anfragen nur per E-Mail | Archivarbeit vor Ort in Berlin |
| NTIS und ScienceON (Südkorea) | robots.txt sperrt alles; offizielle Schnittstelle nur nach Einzelfreigabe; ScienceON aus der Cloud nicht erreichbar | erst nach Antrag; Volltextzugang ungeprüft |
| GRB (Taiwan) | Website bei der Prüfung im Wartungsmodus und aus der Cloud nicht erreichbar; der [offene Datensatz](https://data.gov.tw/en/datasets/18707) ist nur ein Verzeichnis | ungeprüft, später erneut versuchen |
| RGC (Hongkong) | Abschlussberichte ab 2010/11 sollen laut einer [Auskunft](https://www.accessinfo.hk/request/open_access_and_open_data_polici) öffentlich sein; keine zentrale Abrufstelle gefunden | ungeprüft |
| [NASA NIAC](https://www.nasa.gov/niac-funded-studies/) | ältere Berichte derzeit offline wegen einer Prüfung auf Barrierefreiheit; Archiv 1998–2007 aus der Cloud gesperrt | eingeschränkt; teils über NTRS |
| rosrid.ru (Russland) | robots.txt verbietet automatischen Zugriff; Rechtslage bei russischen Quellen bewertet Nick | gestrichen |
| [NSTRS](https://www.nstrs.cn) (China) | Zusammenfassungen frei; Volltext nur nach Klarnamen-Registrierung, nur Ansicht, kein Download | gestrichen |
| НЦГНТЭ (Kasachstan) | kein öffentlicher Zugang gefunden | gestrichen |
| Nexus, NRF (Südafrika) | nur über den kostenpflichtigen Anbieter [Sabinet](https://sabinet.co.za/wp-content/uploads/2025/08/16376_Specialised-Reference-Databases_Final.pdf); Website nicht erreichbar | gestrichen |
| FAPESP (Brasilien) | nur Zusammenfassungen und Laufzeiten, kein Abbruchvermerk, keine Berichte | gestrichen |
| NCN (Polen) | Bewertungen der Abschlussberichte laut [Ratsbeschluss](https://www.ncn.gov.pl/sites/default/files/pliki/uchwaly-rady/2016/uchwala61_2016.pdf) nicht öffentlich | nur über RAD-on |
| Rospatent-Urheberscheine, ungenutzte Hochschulpatente | Volltexte teils kommerziell; zu Hochschulpatenten gibt es keinen Datensatz, nur eine Schätzung | keine Quellen; Hochschulpatente bleiben als Idee |
| ClinicalTrials.gov | Schnittstelle frei, Pflichtfeld zum Abbruchgrund | nur als Vergleich |

Ebenfalls geprüft: Die Abschlussberichte der chinesischen NSFC (kd.nsfc.cn) sperren automatischen Zugriff per robots.txt. Der Förderkatalog des Bundes (über 300.000 Vorhaben) ist durchsuchbar; einen Export oder eine Schnittstelle habe ich nicht gefunden. Die IATI-Datenbank zu Entwicklungsprojekten braucht einen kostenlosen Schlüssel, den Nick beantragen müsste. Taiwans GRB war erneut im Wartungsmodus. Für die ESA-Studien aus dem Programm Ariadna fand ich keine Gesamtliste.

## Wer schon daran arbeitet

Sieben Stränge und Projekte berühren die Idee. Am nächsten kommt GRAIL, aber keiner macht genau das, was wir vorhaben. Jeder liefert aber einen Baustein.

| Strang | Was dort gemacht wird | Was fehlt für unsere Frage |
| --- | --- | --- |
| [Sleeping Beauties](https://pmc.ncbi.nlm.nih.gov/articles/PMC4475978) (Bibliometrie) | Ke et al. werteten 22 Mio. Arbeiten aus: Späte Anerkennung ist kein Ausnahmefall. In der Physik wurden 16 % solcher Arbeiten erst durch [Patentzitate](https://revistapesquisa.fapesp.br/en/sleeping-beauties/) geweckt | arbeitet mit Zitationen veröffentlichter, meist englischer Arbeiten; abgebrochene Projekte ohne Veröffentlichung fehlen |
| [Wiederbelebung aufgegebener Wirkstoffe](https://www.nature.com/articles/490015a) (Pharma) | rund 30.000 von der Industrie zurückgestellte Wirkstoffe; ein US-Programm gab 58 davon von acht Firmen an Forschende frei | das Modell funktioniert, ist aber auf Wirkstoffe beschränkt und gut besetzt |
| Literaturbasierte Entdeckung mit KI | Agenten sollen bekannte Befunde nachentdecken: [Plato-Bio](https://arxiv.org/pdf/2607.23975) fand den Fischöl-Raynaud-Zusammenhang mit Stichtag 1986 wieder; im Benchmark [FIRE-Bench](https://arxiv.org/pdf/2602.02905) erreichen die besten Agenten unter 50 F1 | testet das Wiederfinden bekannter Ergebnisse, nicht das Fortführen abgebrochener Arbeit |
| Textanalyse von Projektregistern | Sprachmodelle klassifizieren Projekte für [Forschungsstatistik](<https://www.dst.dk/ext/2072016640565/0/direktion/4-16-Using-Large-Language-Models-to-Streamline-and-Enhance-R-D-Surveys-(pdf)--pdf>) oder werten [Projektabschlussberichte](https://publications.iadb.org/en/metadata/30849/text-analysis-project-completion-reports) aus | zielt auf Portfolio-Übersichten, nicht auf den Inhalt einzelner Projekte |
| Wiederbelebung sowjetischer Programme | Middlebury CNS baute eine [Datenbank mit über 50 früheren Waffenprojekten](https://nonproliferation.org/?p=31200), die Russland wiederbeleben könnte | militärisch, für uns nur als Abgrenzung; zeigt aber, dass die Methode funktioniert |
| GRAIL (Grant Reuse and Abandoned Ideas Library) | Vorbereitungsprojekt vom 6. Mai bis 30. November 2026, koordiniert vom Journal of Trial and Error: eine Infrastruktur, in der Forschende abgelehnte Anträge, später auch aufgegebene Manuskripte und Rückblicke zum Ruhestand hinterlegen | sammelt freiwillig Eingereichtes, durchsucht keine bestehenden Register und setzt nichts selbst fort; möglicher späterer Partner |
| Fu et al. 2025, Journal of Informetrics | untersucht mit Daten des Hongkonger RGC 2010–2020 und selbst gemeldeten Erfüllungsgraden, was unvollständig erfüllte Projekte zum Fortschritt beitragen | misst Wirkung im Nachhinein, sucht keine fortsetzbaren Projekte; bestätigt aber, dass die Frage relevant ist |

Dazu kommt, dass Staaten selbst alte Projekte wieder aufgreifen. In Protvino lässt das Kurchatov-Institut prüfen, ob sich ein seit den 1990ern stillliegender Beschleuniger fertigbauen lässt; die Pläne von 1983 gibt es nur auf Papier ([bb.lv nach Moscow Times](https://en.bb.lv/article/technologies/2025/12/04/in-russia-they-want-to-restart-the-soviet-hadron-collider-that-never-operated-40-years-ago-79694)).

Quellen zu den beiden neuen Zeilen: [GRAIL bei der EOSC Association](https://eosc.eu/horizon-europe-projects/grail), [Fu et al. 2025](https://hub.hku.hk/handle/10722/363886).

## Offene Stelle und Empfehlung

Die offene Stelle ist ein **Screening nicht fortgeführter Ansätze**: über Register mit Statusvermerk (Weg 1) und über Berichte mit unerreichten Zielen (Weg 2). Jeder Fund wird darauf geprüft, ob er sich heute mit Rechenleistung und KI fortsetzen lässt. GRAIL ist am nächsten dran, setzt aber auf freiwillige Einreichungen und führt nichts fort. Der Status bleibt vorläufig, weil ich noch nicht auf Russisch, Ukrainisch oder Chinesisch nach Forschung zu diesem Thema gesucht habe.

**Ziel und Werkzeug.** Das eigentliche Ziel ist, einen außergewöhnlichen, nicht fortgeführten Ansatz zu finden und selbst zum Erfolg zu führen. Die Suchmethode ist das Werkzeug dafür. Sie kann später selbst zum Produkt werden, etwa als Datensatz mit Modell oder als Scouting-Dienst. Wir bauen sie aber nur so weit aus, wie das Ziel es braucht.

**Rechte bei technischen Kandidaten**, vor allem aus SBIR und Patenten, prüfen wir in zwei Schritten. Erstens die Forschungsfreiheit: Dürfen wir Idee und Daten untersuchen? Zweitens die Verwertbarkeit: Dürfen wir eine Lösung darauf verkaufen, ohne fremde Rechte zu verletzen? Ein aufgegebenes oder abgelaufenes Patent bedeutet nicht automatisch Handlungsfreiheit. Rechtsstände lassen sich im [Register des Europäischen Patentamts](https://www.epo.org/en/service-support/faq/searching-patents/about-patent-information/how-can-i-find-out-if-particular) nachsehen; die Bewertung liegt bei Nick.

**Stärken** (hohes Gewicht): Vier große Quellen liegen komplett und frei zum Download vor: CEP, CORDIS, FWF und SBIR. Zwei davon kennzeichnen Abbrüche, CEP sogar mit Begründung. Die Sprachbarriere schützt vor Konkurrenz und ist zugleich unser Hebel. SBIR und die aufgegebenen Patentanmeldungen (CC0) führen direkt zu Anwendungen.

**Schwächen** (ebenso hohes Gewicht): Außer in CEP habe ich zu keinem Statusvermerk eine Begründung gefunden. Der FWF-Vermerk erfasst fast nur nie begonnene Projekte, und die CORDIS-Abbrüche sind überwiegend Einzelstipendien, deren Abbruchgründe vermutlich oft persönlich sind (ungeprüft). Die textreichen Quellen GEPRIS und NRAT lassen sich nur von Hand lesen. SBIR enthält nur Antragstexte, keine Ergebnisse; die Rechte liegen bei Firmen, knapp die Hälfte stammt vom Verteidigungsministerium. Nur ein Teil wird sich am Rechner fortsetzen lassen.

**Machbarkeitstest: vier frei beziehbare Quellen**

| Quelle | Was der Test zeigen soll |
| --- | --- |
| CEP Tschechien | Wie oft nennt der Bewertungstext eines gestoppten oder gescheiterten Projekts einen inhaltlichen Grund, der heute behebbar ist? Zugleich der Test, ob Weg 2 in einer anderen Sprache funktioniert |
| CORDIS EU | Welche der rund 280 Abbrüche außerhalb der Stipendien haben einen fachlichen Grund, und was sagen die Berichtszusammenfassungen? |
| FWF Österreich | Wie gut lassen sich Ziel, unerledigter Teil und Hindernis aus den Endbericht-Zusammenfassungen ziehen, und taugen die 162 nie begonnenen Ideen etwas? |
| SBIR USA | Wie viele Phase-I-Ansätze ohne Phase II sind technisch interessant und rechtlich offen? |

GEPRIS und NRAT sind aus dem Test herausgenommen, weil sie nur von Hand lesbar sind. Sie kommen dazu, sobald ein Fachgebiet feststeht.

Gefunden wird über eine vollständige maschinelle Vorsortierung aller markierten Einträge (siehe Analyse unten). Zufällige Stichproben dienen nur dazu, die Vorsortierung zu eichen und die Häufigkeit zu schätzen; gezielte Verdachtsfälle werten wir getrennt aus, sonst überschätzen wir, wie häufig gute Gelegenheiten sind. Der Test beantwortet fünf Fragen:

1. Wie viele Einträge zeigen glaubwürdige Hinweise auf nicht fortgeführte Arbeit?
2. Wie oft lässt sich der Grund bestimmen?
3. Wie oft sind Daten und Unterlagen zugänglich?
4. Wie viele lassen sich heute realistisch fortsetzen?
5. Wie viele bleiben nach der Prüfung des Forschungsstands interessant?

**Hauptkennzahl:** belastbare, fortsetzbare Gelegenheiten pro 100 geprüfte Einträge, je Quelle. Eine Kostenschätzung kommt vor dem Start.

## Vorbilder aus Industrie und Forschung

Profis, die nach seltenen Gelegenheiten suchen, arbeiten mit einem Trichter: vieles billig bewerten, wenig gründlich prüfen, früh abbrechen. Die Zahlen zeigen, wie selten Treffer sind: Ein Risikokapitalfonds prüft im Median 100 Deals pro Investition.

| Vorbild | Was dort gemacht wird | Was wir übernehmen |
| --- | --- | --- |
| Risikokapital ([Gompers u. a., NBER](https://www.nber.org/digest/dec16/how-do-venture-capitalists-make-decisions)) | Median-Fonds prüft 100 Deals pro Investition, IT-Fonds 151; die Auswahl gilt als wichtigster Hebel | Erwartung festlegen: Von rund 100 gründlich geprüften Kandidaten trägt vielleicht einer. Wir planen den Trichter so, dass genug Kandidaten oben hineinkommen |
| Roivant, Pharma ([Analyse](https://adus.substack.com/p/how-does-roivant-work)) | lizenziert Wirkstoffe, die Konzerne zurückgestellt haben; Erfolge bei belegtem Wirkprinzip (Relugolix, Vibegron), Fehlschläge bei schwachen Vordaten (Intepirdine) | zwei Pflichtfragen: Gibt es einen Beleg, dass der Ansatz damals funktionierte? Lag der Abbruchgrund außerhalb der Idee (Geld, Strategie, Technik)? |
| Every Cure, Arzneimittel-Neuverwendung ([MATRIX](https://docs.dev.everycure.org/getting_started/first_steps/matrix_pipeline/)) | bewertet alle Wirkstoff-Krankheit-Paare maschinell und erstellt daraus eine Rangliste | alle markierten Einträge maschinell vorsortieren, nicht nur Stichproben |
| Systematische Reviews mit KI ([otto-SR](https://www.medrxiv.org/content/10.1101/2025.06.13.25329541.full.pdf), [Doppelmodell-Studie](https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf)) | ein Modell erreichte beim Vorsortieren 96–97 % Sensitivität, menschliche Doppelreviews 82–87 %; zwei Modellfamilien mit Oder-Regel 99 %, aber nur rund 50 % Spezifität | die maschinelle Vorsortierung wird an einer Stichprobe geeicht, die Claude im Chat bewertet; bei Grenzfällen kann eine zweite Modellfamilie (Gemini) mitentscheiden; eine Stichprobe der Aussortierten wird nachgeprüft |
| DARPA ([Heilmeier-Fragen](https://murray.cds.caltech.edu/Heilmeier_Catechism)) | sieben Fragen vor jedem neuen Programm, u. a. heutige Grenzen, was neu ist, Kosten, Dauer, Zwischenprüfungen | jeder Endkandidat beantwortet die sieben Fragen schriftlich |
| Analysemethoden der Nachrichtendienste ([Tradecraft Primer](https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf)) | Kernannahmen offenlegen und prüfen; Gegenposition bewusst stark machen (Devil's Advocacy) | Kernannahme mit Abbruchregel unten; jeder Endkandidat bekommt ein Gegengutachten aus einem kalten Chat |

Die Studien zu KI-Reviews stammen aus der Medizin und vergleichen mit menschlichen Referenzurteilen; auf Forschungsregister übertragen sind die Zahlen eine Orientierung, kein Nachweis.

## Analyse: Probe, Ablauf, Kriterien

Die Analyse läuft maschinell, ohne Obergrenze für gute Kandidaten und ohne Handarbeit für Nick. Eine kostenlose Probe zeigt, wo die Ausbeute liegt: am ehesten in den tschechischen Begründungstexten, kaum in ungefilterten FWF-Berichten und SBIR-Anträgen.

### Probe vom 9. November

Claude hat hier im Chat 39 Zufallseinträge aus dem fachgefilterten Pool gelesen und bewertet; Zusatzkosten entstanden nicht.

| Quelle | Gelesen | Näher prüfenswert | Beispiele | Lehre |
| --- | --- | --- | --- | --- |
| CEP | 25 | 5 | Monte-Carlo-Simulation von Polymeren an Grenzflächen, 1999 wegen Elternzeit gestoppt; Keimbildungsdaten fehlten wegen aufwendiger Apparatur, Projekt endete mit Weggang des Forschers; Wasserstoffspeicher Mg2Ni, Ziel verfehlt; Schneidwerkzeug aus dem 3D-Drucker mit inneren Kühlkanälen; Fotogrammetrie für Schmiedeteile | viele Fehlschläge haben formale Gründe (Indikatoren, Papiere, Insolvenz) oder sind Ausbauprojekte; Biochemie rutschte durch den Filter |
| FWF | 6 | 0 | – | Endberichte sind öffentliche Erfolgsmeldungen; nur Berichte mit Hindernis-Formulierung lohnen |
| SBIR | 8 | 0–1 | Getriebe aus metallischem Glas für Kälte im All | Anträge ohne Ergebnis; offene Aufrufe und fertige Software-Produkte gehören aussortiert; ob etwas taugte, zeigt erst der Fortsetzungscheck |

Hochgerechnet stecken im gefilterten CEP-Pool rund 90 bis 100 näher prüfenswerte Projekte. Wie viele davon die Tiefenprüfung bestehen, zeigt erst Schritt 4. Die Probe ist klein und von einem einzigen Prüfer; sie zeigt die Richtung, keine verlässlichen Quoten.

### Zweite Probe vom 9. November

Claude hat 83 Zufallseinträge aus den vorgefilterten Pools gelesen (Zufallsstartwert 2026, ohne Zusatzkosten). B heißt näher prüfenswert, Grenzfall heißt unsicher, aber nicht verwerfen.

| Pool | Gelesen | B | Grenzfall | Beispiele | Lehre |
| --- | --- | --- | --- | --- | --- |
| CEP Fehlschläge | 20 | 2 | 1 | Plasmadüse zur Oberflächenbehandlung, Parameter der zweiten Düse verfehlt; Hemmstoffe gegen die Bakterienenzyme dapE und argE, Teilerfolge unveröffentlicht; 5-kW-Brennstoffzelle, auf Wunsch des Empfängers abgebrochen | Gute Fälle nennen ein konkretes technisches Hindernis |
| CEP positiv (Prototyp, Patent) | 20 | 0 | 0 | – | Fast alles abgeschlossene Firmenentwicklung: gebaut, genutzt, nichts offen |
| FWF mit Hindernis-Formulierung | 12 | 1 | 2 | Automatische Georeferenzierung archäologischer Luftbilder („größter Engpass“); Bakterienzucker nur in Spuren herstellbar; Hypericin-Abkömmlinge mit Absorption außerhalb des Laserfensters | Ein Drittel der Treffer sind echte Hindernisse, der Rest Erzählsätze |
| FWF positiv | 8 | 0 | 0 | – | Reine Erfolgsberichte, meist Grundlagenphysik |
| SBIR Phase I ohne Phase II | 15 | 0 | 2 | Faserablage dünner Verbundlagen (NASA); weiche Tastsensor-Haut für Raumanzüge | Anträge nennen Pläne, keine Ergebnisse; warum Phase II fehlt, bleibt offen |
| Grant Witness NSF | 8 | 0 | 0 | – | 5 von 8 sind Bildung, Gleichstellung oder Falschinformation |
| **Summe** | **83** | **3** | **5** |  |  |

A-Kandidaten gab es keine. Zwei B-Fälle hat Claude sofort auf „noch offen“ geprüft:

- **Luftbilder:** Die TU Wien hat das Hindernis inzwischen gelöst. Ein CNN-Abgleich mit heutigen Orthofotos orientiert Aufklärungsbilder aus dem Zweiten Weltkrieg automatisch, bei über 60 % der Bilder mit weniger als 1 mm Restfehler ([EGU 2023](https://meetingorganizer.copernicus.org/EGU23/EGU23-17437.html)). Das bestätigt die Grundthese (altes Hindernis, heute mit KI lösbar), der Fall ist aber schon weitergeführt.
- **dapE-Hemmstoffe:** Die Loyola University Chicago entwickelt solche Hemmstoffe bis 2025 weiter ([PMC 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10815964/), [PMC 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11720106/)). Das Feld lebt, ist aber besetzt.

Beide kommen ins Prüfset, als Fälle, die der Fortsetzungscheck finden muss.

**Stärkstes Frühsignal:** ein im Text benanntes technisches Hindernis. Von den 22 Einträgen mit diesem Merkmal waren 6 gut oder Grenzfall (27 %), von den 61 ohne es nur 2 (3 %). Die Zahlen sind klein und stammen von einem Prüfer, der Unterschied ist aber deutlich. Haiku soll dieses Feld deshalb zuerst ausfüllen, mit Zitat, und die Bewertung beginnt mit diesen Einträgen.

**Positive Projekte neu fassen:** „Erfolgreich abgeschlossen mit Prototyp“ heißt meist „fertig und genutzt“ (0 von 28). Neue Bedingung: Ergebnis plus ausdrücklich offener Schritt (weitere Entwicklung nötig, Potenzial, Vermarktung ausstehend). Damit bleiben im CEP 117 von 1.329, im FWF 4 von 391. Bessere Quellen für positive Fälle sind vermutlich RIV-Ergebnisse vom Typ Funktionsmuster oder Prototyp ohne Folgeprojekt und SBIR-Phase-II-Projekte ohne Phase III; beides ist noch nicht geprüft.

**SBIR zuletzt:** Nach den Frühfiltern bleiben 4.596 SBIR-Einträge, mehr als alle anderen Pools zusammen, bei der geringsten Dichte. SBIR läuft deshalb als letzter Pool. Ob NASA-Abschlussberichte zu Phase I im NTRS die fehlenden Ergebnisse liefern, ist ungeprüft.

### Frühfilter

Harte Regeln nehmen einen Eintrag aus dem Lauf, er bleibt aber in der Datei und lässt sich zurückholen. Weiche Regeln stellen ihn nur nach hinten. Geprüft an den 83 bewerteten Einträgen: 8 gut oder Grenzfall, 75 ungeeignet.

| Regel | Art | Wirkung auf die Pools | Gute in der Probe getroffen | Ungeeignete getroffen |
| --- | --- | --- | --- | --- |
| CEP: formaler Grund erweitert (Insolvenz „úpadek“, Rücktritt vom Vertrag, fehlende Nachweise, Bewertungsmethodik, „zu Lasten des Empfängers“) | hart | −47 | 0 | 3 |
| CEP: Infrastrukturprogramme LM, LQ, LO, LR | hart | −6 | 0 | 1 |
| SBIR: Pitch Day, offene Aufrufe, fertiges Produkt | hart | −48 | 0 | 2 |
| SBIR: Waffen, Raketen, Zielerfassung ohne zivilen Bezug | hart | −182 | 0 | 1 |
| Grant Witness: Bildung, Gleichstellung, Konferenz, Planung, Falschinformation, Restmittel unter 50.000 $ | hart | −209 von 264 | 0 | 7 |
| CEP: Bewertung ohne Inhalt (nur Standardsatz oder unter 70 Zeichen) | weich | 37 | 0 | 2 |
| CEP: Personal- oder Frühabbruch (Weggang, Leiterwechsel, nach wenigen Monaten ohne Ergebnis) | weich | 16 | 0 | 3 |
| Reine Grundlagenfächer (Mathematik, Astronomie, Geologie; FWF ohne angewandtes Fach) | weich | CEP 45, FWF 260 | 0 | 8 |
| FWF: kein echtes Hindernis im Text | weich | 479 | 0 | 11 |
| Positive ohne offenen Schritt | weich | CEP 1.191 | 0 | 17 |
| SBIR: Verteidigung ohne zivilen Bezug | weich | 1.517 | 0 | 2 |

Zusammen erkennen die Regeln 52 der 75 ungeeigneten Einträge (69 %) und treffen keinen der 8 guten. Verworfen wurde eine Regel gegen Publikationsmängel („nicht publiziert“): Sie hätte die Enzym-Hemmstoffe aussortiert.

Wirkung auf die Pools: Die harten Regeln nehmen 492 von 9.077 Einträgen heraus. Ohne weiche Markierung bleiben 5.241 vorn, davon 4.596 SBIR. Ohne SBIR sind es 645 Einträge, die zuerst durch Haiku und Opus laufen. Die Bewertungen der Probe liegen als Datei bereit und gehen ins Prüfset ein.

### Neue Quellen vom 9. November

Vier neue Pools bringen 8.836 Einträge dazu, alle schon geladen und fachgefiltert. Sie sind von vornherein näher am Markt: Es sind Projekte, die ein funktionierendes Ergebnis Richtung Anwendung bringen sollten.

| Pool | Was es ist | Einträge (Technik) | Erster Eindruck aus der Stichprobe |
| --- | --- | --- | --- |
| ERC Proof of Concept | EU-Geld, um ein Laborergebnis marktreif zu machen; abgeschlossen | 854 | 2 bis 3 von 8 näher prüfenswert, höchste Dichte bisher (z. B. Holzherkunfts-Test, lösungsmittelfreie Suzuki-Kupplung im Durchlauf) |
| EU-KMU-Instrument Phase 1 ohne Phase 2 | Machbarkeitsstudien von Firmen, danach keine Folgeförderung | 3.097 | 0 bis 1 von 8; viel Software und Geschäftsmodelle ohne Hindernis |
| EU-KMU-Instrument Phase 2 | Entwicklung bis zum Produkt | 1.168 | noch nicht gelesen |
| SBIR Phase II ohne Folgeförderung | US-Firmenprojekte mit Prototyp, Firma danach nie wieder gefördert (2008–2020, ohne Waffen) | 2.540 | etwa 1 von 8; manche Firmen waren erfolgreich und brauchten kein Geld mehr (z. B. Inpria, 2021 verkauft) |
| RIV-Ergebnisse „bisher ungenutzt“ oder mit offenem Schritt | Tschechische Prototypen, geprüfte Technologien, Patente und Software, die laut Meldung noch niemand nutzt oder die auf Vermarktung warten (2018–2024) | 1.177 von 23.542 | 1 bis 2 von 10 Grenzfälle; viele Funktionsmuster ohne Hindernis-Angabe |

Wichtig an RIV: Jedes Ergebnis hat ein amtliches Feld zur Nutzung. „O“ heißt „bisher ungenutzt“, „N“ heißt „für andere ohne Lizenz nutzbar“. Das löst die Rechtefrage oft sofort. RIV ist als offene Datei erst ab 2018 verfügbar; ältere Jahre liefert der Server nicht.

Die Rohdaten für RIV belegen 56 MB, weil das Skript beim Herunterladen nur die Ergebnisarten Prototyp, Technologie, Patent, Gebrauchsmuster und Software behalten hat.

### Test: Sortieren per Fähigkeiten-Katalog

Der Text-Abgleich mit dem [Fähigkeiten-Katalog](https://claude.ai/artifact/4Y9KmjiJaM6E5ib8ni2tJ7) sortiert schwächer als erhofft. Am stärksten trennt weiterhin die einfache Suche nach einem benannten technischen Hindernis. Gemessen an den bewerteten Einträgen der Zufallsprobe (1,0 = perfekt, 0,5 = Zufall):

| Verfahren | Trennschärfe (AUC) |
| --- | --- |
| Suche nach benanntem Hindernis (Regel) | 0,71 |
| Text-Vektoren, Modell MiniLM | 0,61 |
| Text-Vektoren, schnelles Modell potion | 0,53 |
| Regel plus MiniLM | 0,71 |

Grundlage sind nur 6 gute und 50 ungeeignete Einträge, die Zahlen schwanken also stark. Beim Lesen der Ranglisten fanden sich trotzdem neue gute Fälle: Unter den obersten 10 tschechischen Fehlschlägen waren 3 gute (zufällig gezogen etwa 1 bis 2 von 10), bei den anderen Pools etwa 1 von 10. Beispiele: eine Hydraulikpumpe mit neuer Kinematik, deren Funktionsmuster die Vorgabe noch nicht erreichte; Sprühgranulation, deren Partikelsimulation nur offline lief; Messung während des 3D-Drucks für eine Regelung.

Folgerung: Ob ein echtes technisches Hindernis genannt ist, erkennt ein Sprachmodell besser als Vektoren. Das ist billig: Haiku über alle rund 17.400 Einträge kostet geschätzt 2 bis 3 $ pro Durchlauf im Batch. Eine Vorsortierung per Vektoren lohnt sich dafür nicht. Der Katalog geht stattdessen als Vorgabe in die Anweisungen.

### Prüfset, Stand 9. November

Das Prüfset hat 51 echte Einträge: 11 gute (davon 2 schon von anderen weitergeführt), 20 Grenzfälle und 20 ungeeignete. Bei den guten fehlen noch rund 9 zum Ziel von 20. Die Datei mit Begründung je Eintrag liegt bereit.

### Angepasste Reihenfolge und Kosten

1. **Frühfilter (Skript, 0 $):** wie oben.
2. **Haiku über alle Einträge (rund 5 $ für zwei Durchläufe im Batch):** Hindernis mit Zitat, Hindernis-Muster H1 bis H11 aus dem Katalog, offener Schritt bei positiven Projekten. Zwei Durchläufe mit verschiedenen Anweisungen; ein Ja reicht zum Weiterkommen.
3. **Sonnet für alles mit Muster H1 bis H7 oder offenem Schritt (geschätzt 15 bis 30 $ im Batch, je nachdem wie viele Haiku markiert):** Bewertung nach den zehn Kriterien, mit Katalog.
4. **Fortsetzungscheck per Skript (0 $, braucht kostenlosen OpenAlex-Schlüssel):** für alle, die Sonnet über die Schwelle hebt.
5. **Opus für die oberen einige Hundert (geschätzt 15 bis 30 $ über die API, oder ohne Zusatzkosten über Claude Code im Abo):** Umweg-Suche, Belegpflicht, Plan.

Vorher läuft Schritt 2 und 3 auf dem Prüfset (wenige Cent). Alle Beträge sind Schätzungen nach Listenpreis und brauchen Nicks Freigabe.

### Ablauf

1. **Fach- und Vorfilter (Skripte, 0 $):** Behalten werden Technik, IT, Physik, Chemie, Mathematik, Materialien, Ingenieurwesen, Energie, Industrie und Handwerk, außerdem Medizintechnik, Biotechnik und Lebensmitteltechnik. Raus sind Biologie, Ökologie, Zoologie, Medizin, Landwirtschaft, Sozial- und Geisteswissenschaften. Gemessen: 27.216 markierte Einträge, 14.748 nach dem Fachfilter; dazu kommen positive Projekte (siehe Suchkriterien unten). Die vorgefilterten Pools umfassen 9.077 Einträge einschließlich positiver Projekte. Die Frühfilter (siehe unten) nehmen 492 heraus und stellen weitere nach hinten; vorn bleiben 5.241, ohne SBIR 645. Nichts wird endgültig gelöscht.
2. **Herausziehen (Haiku 5.5):** Haiku urteilt nicht, sondern füllt je Eintrag Felder aus: Ziel, unerledigter Teil, Hindernis und dessen Typ, Beleg für Teilerfolge, Fachgebiet, Marktbezug, Rechenanteil, jeweils mit wörtlichem Zitat. Das läuft über alle Einträge.
3. **Bewerten (Opus 5.5):** Jeder Eintrag, der nach Schritt 2 plausibel ist, wird nach den zehn Kriterien unten bewertet, mit Umweg-Suche für jedes Hindernis. Es gibt keine Obergrenze; weiter kommt alles über der Schwelle.
4. **Fortsetzungscheck und Tiefenprüfung (Claude Code mit Opus-Subagenten):** je Kandidat ein Subagent. Er sucht Folgearbeiten (OpenAlex), Patente, spätere Förderungen und Firmenspuren, klärt Rechte und Unterlagen und skizziert einen ersten Fortsetzungsplan.
5. **Entscheidung:** Nick wählt aus der fertigen Liste. Endkandidaten bekommen ein Gegengutachten mit Lösungsvorschlägen.

Nick sucht nichts von Hand. Die Eichung von Schritt 2 und 3 übernimmt Claude im Chat, so wie bei der Probe.

**Prüfhaltung: lösungsorientiert.** Ein Hindernis ist kein Ausschlussgrund, sondern eine Aufgabe. Für jedes Hindernis suchen wir zuerst einen Weg: eine rechnerische Teilaufgabe, einen Umweg über öffentliche Daten oder Simulation, eine kleinere Version, einen Partner oder eine Lizenz. Verworfen wird nur, was widerlegt ist oder wofür nach dieser Suche kein Weg bleibt; jeder Verwurf wird begründet und bleibt wieder aufnehmbar.

### Kriterien

| Nr. | Kriterium | Frage | Art |
| --- | --- | --- | --- |
| 1 | Unerledigter Kern | Lässt sich in einem Satz sagen, was offen blieb? | Pflicht |
| 2 | Abbruchgrund | Lag er außerhalb der Idee: Geld, Personal, Organisation, Technik, Aufwand? | Pflicht |
| 3 | Heute lösbar | Ist das Hindernis mit KI, Rechenleistung, Daten oder günstigerer Technik behebbar, notfalls über einen Umweg? | Punkte, doppelt |
| 4 | Markt | Gibt es eine Branche und zahlende Anwender? | Punkte, doppelt |
| 5 | Beleg | Gibt es Teilerfolge, Messdaten oder Prototypen? | Punkte |
| 6 | Rechenanteil | Wie viel lässt sich am Rechner fortführen? | Punkte |
| 7 | Noch offen | Hat es inzwischen niemand gelöst? | Pflicht ab Schritt 4 |
| 8 | Rechte | Frei nutzbar oder lizenzierbar? | Punkte |
| 9 | Unterlagen | Sind Berichte, Daten oder Patente zugänglich? | Punkte |
| 10 | Tempo | Wie schnell ist ein erstes vorzeigbares Ergebnis erreichbar? | Punkte |

Harte Ausschlüsse: Idee widerlegt, nur formaler Grund, reines Ausbau- oder Infrastrukturprojekt, ausgeschlossenes Fachgebiet, militärisch ohne zivile Nutzung.

### Suchkriterien für positive Projekte

Nicht nur Fehlschläge zählen. Mindestens so wertvoll sind Ansätze, die funktioniert haben und trotzdem liegen blieben (Klasse B). Diese Signale weisen darauf hin; gezählt ist, was sich am 9. November in den geladenen Daten messen ließ.

| Signal | Quelle | Gemessen |
| --- | --- | --- |
| Bestnote „hervorragend“ oder „Ziel erfüllt“, Ende vor 2022, Technikfach, kein Ausbauprojekt | CEP | 17.989 Projekte, davon 4.951 hervorragend |
| Prototyp, Patent, Gebrauchsmuster, Pilotanlage oder Software im Bewertungstext | CEP; dazu die Ergebnisdatenbank RIV, die Ergebnisse den Projekten zuordnet | 1.329 Projekte, davon 309 hervorragend; RIV noch nicht ausgewertet |
| Positive Formulierungen wie Prototyp, Machbarkeitsnachweis, erstmals gezeigt, Patent, Ausgründung, Industriepartner, großes Potenzial | FWF-Endberichte | 423 von 2.972 Technikberichten bis 2021 |
| Mitten in der Laufzeit gekündigt, viel Geld übrig | Grant Witness, NSF-Technik | 165 von 264 mit mehr als 100.000 $ Rest |
| Phase I bewilligt, keine Phase II; gleiches Thema später erneut ausgeschrieben, der Bedarf besteht also weiter | SBIR | Neuausschreibungen noch nicht gezählt |
| Patent wegen Nichtzahlung verfallen, aber häufig zitiert | USPTO-Gebührendaten plus Zitationsdaten | noch nicht gezählt |
| Machbarkeitsprojekt (ERC Proof of Concept) ohne erkennbare Ausgründung | CORDIS | noch nicht gezählt |
| Folgeantrag abgelehnt oder Anschlussfinanzierung fehlte | Textsignal in allen Quellen | – |

Bei positiven Projekten ist der Fortsetzungscheck besonders wichtig, denn viele gute Ansätze liefen unter anderem Namen weiter. Die Reihenfolge für Haiku: zuerst die 1.329 tschechischen Projekte mit Prototyp oder Patent, dann der Rest. Die 17.989 Einträge kosten mit Haiku rund 2–3 $ zusätzlich. Die RIV-Ergebnisdateien sind je Jahr rund 250 MB groß; wir filtern sie beim Herunterladen und behalten nur Patente, Prototypen, Pilotanlagen und Software.

### Prüfset

Zufallsproben allein reichen nicht. Wenn starke Kandidaten selten sind, steckt in 100 Zufallseinträgen vielleicht kein einziger. Dann wissen wir nur, dass die Vorsortierung Durchschnittsfälle erkennt. Die größte Gefahr ist ein außergewöhnlich guter Kandidat, der unbemerkt aussortiert wird.

Deshalb baut Claude im Chat vor dem großen Lauf ein Prüfset aus rund 60 echten Einträgen:

- **20 eindeutig gute:** gezielt über die Signale oben gesucht, dazu die prüfenswerten Fälle aus der Probe.
- **20 eindeutig ungeeignete:** formaler Grund, Ausbauprojekt, widerlegte Idee, ausgeschlossenes Fach.
- **20 schwierige Grenzfälle:** Die Bedeutung ergibt sich erst aus mehreren Sätzen; das Hindernis steht nur indirekt da; Tschechisch mit Fachjargon; gute Idee schlecht beschrieben; glänzende Beschreibung ohne Substanz.

Dazu kommen rund 5 umgeschriebene Fassungen guter Fälle, in denen das Entscheidende erst im letzten Satz steht. Sie sind als künstlich markiert. Testregel: Die Vorsortierung muss alle eindeutig guten Fälle behalten und mindestens 80 % der Grenzfälle. Ungeeignete dürfen durchrutschen, das kostet nur spätere Prüfzeit. Besteht Haiku den Test nicht, ändern wir die Anweisung oder lassen die betroffenen Fälle von Sonnet sortieren. Während des großen Laufs mischen wir einige Prüfset-Fälle als Kontrollen in jede Charge. So fällt sofort auf, wenn die Vorsortierung unterwegs schlechter wird.

### Belegpflicht

Keine Bewertung ohne Beleg. Damit wird aus einer vagen Projektbeschreibung keine überzeugend klingende, aber unbegründete Fortsetzungsidee.

- **Beim Herausziehen (Haiku):** Jedes Feld trägt ein wörtliches Zitat aus dem Originaltext. Ein Skript prüft kostenlos, ob das Zitat dort wirklich steht. Fehlt es oder stimmt es nicht, landet der Eintrag in „Nachprüfen“, nicht im Müll.
- **Bei jedem Kandidaten, den Opus als vielversprechend einstuft, Pflicht:**
  - **Damals:** welches konkrete Hindernis bestand, mit wörtlichem Beleg aus den Originalunterlagen.
  - **Heute:** welche konkrete technische oder wissenschaftliche Entwicklung das Hindernis beseitigen könnte, mit überprüfbarer Quelle und Link.
  - **Markt:** wer dafür zahlen würde, mit Beleg.
  - **Offen:** welche entscheidende Annahme noch nicht belegt ist, und wie wir sie am schnellsten prüfen.

Fehlt ein Beleg, bleibt der Kandidat in der Liste, aber mit dem Vermerk „unbelegt“. Er wird nicht gelöscht. Die Gegenprüfung kontrolliert gezielt diese vier Felder.

### Kosten

Grundlage sind die gemessenen Textmengen: 14.748 Einträge mit rund 10,8 Mio. Token, dazu rund 800 Token Anweisung je Eintrag und rund 300 Token Antwort. Mit den 17.989 positiven CEP-Projekten kommen rund 5,4 Mio. Token dazu: Haiku kostet dann rund 5 $ statt 2–3 $, die Opus-Stufe wächst geschätzt auf 30–40 $. Günstiger Start: zuerst die Fehlschläge und die 1.329 positiven Projekte mit Prototyp oder Patent.

| Variante | Umfang | Kosten, grob | Einschätzung |
| --- | --- | --- | --- |
| Nur Haiku, Batch | alle 14.748 | rund 2–3 $ | sehr günstig; gut im Herausziehen, schwächer im Urteil |
| Haiku, dann Opus für alle Plausiblen, Batch | 14.748 plus geschätzt 1.000–1.500 | rund 15–20 $ | empfohlen: Opus bekommt nur, was ein Urteil verdient |
| Nur Opus, Batch | alle 14.748 | rund 85–110 $ | bestes Urteil, aber das meiste Geld geht ins Aussortieren |
| Opus-Subagenten in Claude Code mit API-Schlüssel | wie oben, ohne Batch | über 200 $ | teuerste Variante, weil jeder Subagent Anweisungen und Dateien neu liest |
| Claude Code mit Abo statt API-Schlüssel | beliebig | keine Zusatzkosten, verbraucht Nutzungslimits | hängt vom Abo ab; erst an 200 Einträgen messen, wie viel Limit das kostet |

Preise laut [Anthropic-Preisliste](https://platform.claude.com/docs/en/about-claude/pricing), Stand 8. November 2026; Batch heißt 50 % Rabatt. Den Anteil der Plausiblen habe ich aus der Probe geschätzt. Claude Code kann außerdem kostenlos lokal arbeiten: Skripte für Filter und Dubletten, Ähnlichkeitssuche mit einem offenen Modell auf der VM, die OpenAlex-API für den Fortsetzungscheck und Websuche für einzelne Kandidaten.

### Speicher

| Bestand | Größe |
| --- | --- |
| CEP (Tschechien) | 165 MB |
| SBIR (USA) | 368 MB |
| CORDIS, drei Pakete | 126 MB gepackt, rund 460 MB entpackt |
| FWF, alle Projekte als JSON | rund 70 MB |
| Grant Witness | 13 MB gepackt, 57 MB entpackt |
| Ergebnisse je Eintrag | unter 100 MB, geschätzt |
| Volltexte nur für Kandidaten, etwa 1.000 PDFs | rund 2 GB, geschätzt |

Der Kern belegt rund 1 GB, mit Volltexten für Kandidaten 3 bis 5 GB. Große Volltextquellen wie OSTI mit 314.529 Berichten laden wir nie komplett; das wären geschätzt mehrere Hundert GB. Rohdaten gehören nicht ins Repository, dort liegen nur Code, Raster und kleine Ergebnisdateien.

## Quellen und Lesenachweis

Am 8. November 2026 habe ich die Daten direkt abgerufen und ausgezählt: FWF (alle 20.602 Projekte), SBIR, CEP, CORDIS (Horizon 2020 und FP7), SNSF und ARC komplett; GtR, NTRS, RAD-on, IDRC, NSF und das kenianische Repositorium als Stichprobe. Bei GEPRIS, KAKEN, NTIS, TIB und rosrid.ru habe ich die robots.txt gelesen. Nicht geprüft sind die Lizenz der CEP-Daten und der Volltextzugang in Korea, Taiwan und Hongkong. Die CEP-Codes stammen aus der offiziellen Codeliste: „O“ heißt „Ziel nicht erfüllt, Vertrag eingehalten“, nicht „mit Vorbehalt“, wie ich zuerst aus Stichproben geschlossen hatte. Die Arbeit von Fu et al. war gesperrt. Die Aussage, dass niemand Register auf fortsetzbare Ansätze screent, bleibt vorläufig.

| Quelle | Was ich gelesen oder abgerufen habe | Folge |
| --- | --- | --- |
| [FWF Open API, Dokumentation](https://www.fwf.ac.at/fileadmin/Website/Dokumente/Entdecken/Forschungsradar/Open_API/fwf_open_api_documentation_1.1_v2.pdf) | vollständig; alle Projekte abgerufen | Status-Werte: beendet, laufend, Start ausständig, zurückgelegt |
| [FWF, Hinweise zu Projektdaten](https://www.fwf.ac.at/en/discover/notes-on-project-data) | vollständig | „prematurely terminated“ fasst nie begonnene und abgebrochene Projekte zusammen |
| [IS VaVaI Open Data](https://www.isvavai.cz/opendata) | Seite und Schema vollständig; Projektdatei komplett | Zahlen in der Quellentabelle |
| [MŠMT-Seminar 2013](https://msmt.gov.cz/file/28407_1_1) | Ausschnitt | Seite inzwischen nicht mehr erreichbar; ersetzt durch die offizielle Codeliste (unten) |
| [CORDIS-Datenpakete](https://cordis.europa.eu/data/cordis-h2020projects-csv.zip) | Horizon 2020 und FP7 komplett | Abbrüche nach Förderlinie gezählt |
| [SBIR-Award-Daten](https://data.www.sbir.gov/awarddatapublic/award_data.csv) | komplett | Abgleich Phase I zu Phase II über Firma und Themenkürzel, nur Hinweis |
| [GtR-API](https://gtr.ukri.org/resources/gtrapi2.html) | vollständig; Stichprobe von 100 Projekten | keine |
| [NTRS, Harvesting](https://sti.nasa.gov/harvesting-data-from-ntrs/) | Ausschnitt; API ohne Schlüssel getestet | keine |
| [KAKEN-Nutzungsbedingungen](https://support.nii.ac.jp/ja/kaken/about/terms), [API](https://support.nii.ac.jp/ja/kaken/api/api_outline) | vollständig; robots.txt gelesen | App-ID beantragt Nick |
| [Harvard Dataverse, Cotropia und Schwartz](https://doi.org/10.7910/DVN/Q4Q32F) | Metadaten über die API | CC0, eine Datei |
| [SNSF](https://data.snf.ch/datasets), [ARC](https://dataportal.arc.gov.au/NCGP/API/grants), [RAD-on](https://radon.nauka.gov.pl/opendata/polon/projects) | Dateien komplett bzw. API-Stichprobe | kein Abbruchvermerk |
| [IDRC Digital Library](https://idl-bnc-idrc.dspacedirect.org/), [Kenia NRR](https://repository.nrf.go.ke/) | Trefferzahl bzw. Sammlungsübersicht | Lizenz IDRC ungeprüft |
| [NASA NIAC](https://www.nasa.gov/niac-funded-studies/) | erste 100.000 Zeichen der Seite | ältere Berichte zurzeit offline |
| [TÜBİTAK](https://tubitak.gov.tr/en/node/14510), [NSTRS](https://www.nstrs.cn), [GRB-Datensatz](https://data.gov.tw/en/datasets/18707) | TÜBİTAK nur Ausschnitt, die anderen vollständig | siehe zweite Quellentabelle |
| NRAT, [RGC-Auskunft](https://www.accessinfo.hk/request/open_access_and_open_data_polici), [NCN-Beschluss](https://www.ncn.gov.pl/sites/default/files/pliki/uchwaly-rady/2016/uchwala61_2016.pdf), [Sabinet](https://sabinet.co.za/wp-content/uploads/2025/08/16376_Specialised-Reference-Databases_Final.pdf), [BBAW](https://archiv.bbaw.de/en/the-academy-archive/utilisation-order) | NRAT: eine Registerkarte vollständig, Berichte nur Ausschnitte; Rest Ausschnitte | Zugangsaussagen, nicht tragend für Zahlen |
| GRAIL (EOSC Association), Fu et al. 2025 | GRAIL vollständig, Fu et al. nur Repositoriumseintrag | Abgrenzung |
| Volkskammer-Protokoll 1990, Nature 2013, Williams et al. 2015, Ke et al. 2015, FIRE-Bench, Plato-Bio, Middlebury CNS, bb.lv | nur Ausschnitte oder Zusammenfassungen | Beispiele, nicht tragend |

Zum Vorgehen gelesen: die otto-SR-Studie und die Doppelmodell-Studie (beide über eine Zusammenfassung des Volltexts), die NBER-Zusammenfassung zu Risikokapital, die Heilmeier-Fragen, den Tradecraft Primer, die Roivant-Analyse und die MATRIX-Dokumentation vollständig; zu Stage-Gate nur eine Zusammenfassung. Die oft zitierte Zahl „3.000 Rohideen pro Markterfolg“ konnte ich an keiner geöffneten Quelle bestätigen und habe sie weggelassen. Den SBIR-Textabgleich (TF-IDF, Stichprobe von 4.000) habe ich selbst gerechnet.

Zweite Prüfrunde: die offiziellen CEP-Codelisten für [Bewertung](https://www.isvavai.cz/dokumenty/opendata/ciselniky/hodnoceni-projektu.jsonld) und [Status](https://www.isvavai.cz/dokumenty/opendata/ciselniky/stav-projektu.jsonld) vollständig; das [Grant-Witness-Archiv](https://zenodo.org/records/23577373) und das Horizon-Europe-Paket von CORDIS komplett geladen und gezählt; die CORDIS-Lizenz über die Schnittstelle des EU-Datenportals; den [USPTO-Katalogeintrag](https://catalog.data.gov/dataset/patent-grant-maintenance-fee-events-september-1-1981-present-7d26f), die [OSTI-Dokumentation](https://www.osti.gov/api/v1/docs) und die [OpenAlex-Hilfe](https://help.openalex.org/api/) vollständig; die [Gemini-Preisseite](https://ai.google.dev/gemini-api/docs/pricing) zu 100.000 von 106.069 Zeichen; die TIB-Sitemap und die Startseite des Förderkatalogs.
