# Beobachtungen aus Häppchen 1 (A06 Phase 7b)

Fable 5.2, ein Aufruf über die oberen 100 (`ergebnisse/fable_a06_frei.jsonl`, antwortendes Modell claude-fable-5-2, Kosten 2.52 $, ohne Websuche).
Alles unten ist **Vermutung** von Fable, nicht von Hand geprüft. Zitate und IDs stammen aus dem Material, das Fable bekam.
Hinweis zum Auftrag: Fable weicht bei Biologie-Themen auf ältere Modelle aus. In diesem Aufruf gab es kein Ausweichen.

Grundlage sind nur die gelieferten Felder; die Originaltexte und die abgeschnittenen OpenAlex-Felder habe ich nicht gesehen. Alle Funde sind Vermutungen.

## Funde

**1. Messdaten liegen vor, das Modell fehlt** (Art 1 und 3)
- **Vermutung:** Fünf Projekte haben den teuren Laborteil erledigt und sind am Rechenteil hängen geblieben. Das ist der Teil, den Nick heute leisten kann.
- **Projekte:** 10.55776/P17185, GA15-15467S, GA15-05534S, GP14-35225P, 10.55776/M2441.
- **Zitate:**
  - P17185: „the separation of small particles could not be predicted satisfactorily"
  - GA15-15467S: „Publikování dalších výsledků v časopise je teprve v přípravě (model pro rozložení velikosti částic po rozpadu)."
  - GA15-05534S: „Hlavní publikované výsledky jsou ale zaměřeny zejména experimentálně."
  - GP14-35225P: „Odpovídající rozložení zbytkového napětí však nebylo analyzováno a nebyl vytvořen model"
  - M2441: „Future work should be aimed to link the properties that can be modelled -using computational tools- with the final properties of the materials"
- **Warum es zählt:** Code-Agenten und gemietete Rechenleistung treffen genau diesen Rest. Offen ist überall, ob die Rohdaten zugänglich sind.
- **Erster Schritt:** Je Projekt die veröffentlichten Daten auflisten (GA15-15467S hat 3 Arbeiten, GA15-05534S hat 14) und das Projekt mit den besten Daten wählen.

**2. Zerfall und Agglomeration: drei Teile einer Rechnung** (Art 2)
- **Vermutung:** Blasenzerfall, Granulatbruch und Agglomeration im Zyklon nutzen denselben Rechenrahmen (Populationsbilanz mit Zerfalls- und Haftkernen). Ein Werkzeug, das diese Kerne aus Messdaten anpasst, fehlt in allen dreien. Die Physik ist verschieden; nur der Rahmen ist gemeinsam.
- **Projekte:** GA15-15467S, GA15-05534S, 10.55776/P17185.
- **Zitate:**
  - GA15-15467S: „Hlavním přínosem projektu je získání experimentálních dat týkajících se rozpadu bublin v turbulentním proudění."
  - P17185: „Agglomerates of types 2 and 3 were unexpected. The mechanism of their formation is unknown."
- **Warum es zählt:** Ein gemeinsames Anpass-Werkzeug hätte Kunden in der Verfahrenstechnik; ein Einzelprojekt eher nicht.
- **Erster Schritt:** Offenen Populationsbilanz-Löser aufsetzen und die Zerfallskerne an den publizierten Blasendaten anpassen.

**3. Eisenpulver-Brenner plus Feinabscheidung, mit Kleinprototyp** (Art 5)
- **Vermutung:** Ein Eisenpulver-Kreislauf muss das feine Oxid wieder einfangen (mein Fachwissen, nicht im Material). Dann gehören der Brenner und der Zyklon zusammen, und beide brauchen dieselbe Partikel-Strömungs-Simulation.
- **Projekte:** 101123027, 10.55776/P17185.
- **Zitate:**
  - 101123027: „Full CFD simulation using OpenFOAM was hindered by the loss of a key expert"
  - P17185: „However, the separation of small particles could not be predicted satisfactorily."
- **Warum es zählt:** Nur 2 von 100 Kandidaten haben bei Haiku den ersten Schritt „prototyp_klein". Hier wäre ein Prototyp im Budget denkbar: 3D-gedruckter Mini-Zyklon, Prüfstaub, zwei günstige Feinstaubsensoren. Die Sensoren sind ungenau, das ist die offene Annahme.
- **Erster Schritt:** Partikel-Simulation eines Mini-Zyklons in OpenFOAM, parallel beim ICONIC-Konsortium nach dem Stand der Abscheidung fragen.

**4. Engpass Mensch: Spezifikation, Testrahmen, Beweisübertragung** (Art 1 und 3)
- **Vermutung:** Mehrere Verifikationsprojekte scheiterten nicht am Algorithmus. Es fehlte die Handarbeit davor: Spezifikation schreiben, je Zielsystem anpassen, Beweise übertragen.
- **Projekte:** 101069165, 966733, 10.55776/P29498, GPP202/12/P180.
- **Zitate:**
  - 101069165: „the key gaps remaining on the way for larger adoption of synthesis technologies in industry are in the ability of engineers to write correct formal specifications"
  - 966733: „a large extend due to the unique challenges posed to the technology by the high fragmentation of the targeted ecosystem"
  - P29498: „postponing the formalization in Theorema-HOL to a potential future effort"
  - GPP202/12/P180: „Tento tříletý projekt skončil po prvním roce"
- **Warum es zählt:** Sprachmodelle und Code-Agenten zielen auf diese Handarbeit. Der Katalog belegt das nur für den Nachbau von Papern, nicht für formale Spezifikationen.
- **Erster Schritt:** 20 Anforderungen aus offenen Fallstudien per Sprachmodell in Spectra übersetzen. Der Synthese-Prüfer entscheidet, ob sie realisierbar sind.

**5. Geschäftsidee: Anforderung → Spezifikation → SPS-Code** (Art 5)
- **Vermutung:** 101069165 hat die Synthese, aber niemanden, der Spezifikationen schreibt. 822620 hat die Kette vom Prozessmodell zum Steuerungscode, aber zu wenige Nutzer. Ein Sprachmodell als Eingang könnte beide Lücken schließen.
- **Projekte:** 101069165, 822620.
- **Zitate:**
  - 822620: „Analyzing back, it seems that the adoption rate of our solution was too low."
  - 822620: „Our patented solution has been run in a range of pilot projects at real industrial facilities"
- **Warum es zählt:** Reine Software, prüfbar in der Simulation. Die Abnehmer wären Maschinenbauer und Systemintegratoren. Das Patent von 822620 und die Lizenz von Spectra sind ungeprüft.
- **Erster Schritt:** Demo für eine einfache Anlage (Förderband mit Verriegelung): Text → Spezifikation → synthetisierter Regler → IEC-61131-Code, getestet im Simulator.

**6. Produktionsplanung: Methode da, Skalierung fehlt** (Art 2)
- **Vermutung:** P32954 hat die Planungsmethode, GPP103/10/P401 die GPU-Bausteine, P34317 die ableitungsfreien Löser. Zusammen könnten sie die Skalierungsgrenze verschieben. Ob die Grenze am Rechenaufwand liegt, ist unbelegt.
- **Projekte:** 10.55776/P32954, GPP103/10/P401, 10.55776/P34317.
- **Zitate:**
  - P32954: „While the methods performed well for small production systems, further research is required to scale them to larger, more complex systems."
  - GPP103/10/P401: „návrh konstrukcí pro meta-heuristické algoritmy implementované na GPU"
  - P34317: „preliminary (and not yet released) self-tuning environment"
- **Warum es zählt:** Abnehmer wären ERP-Anbieter und Fertiger. Standard-Löser sind starke Konkurrenz.
- **Erster Schritt:** Die Simulation aus den drei P32954-Arbeiten nachbauen und messen, ab welcher Systemgröße die Laufzeit kippt.

**7. Wind: zweimal dieselbe Lücke im Analyse-Modul** (Art 1 und 2)
- **Vermutung:** Beide Projekte lieferten die Plattform, nicht die Auswertung. Das eine deckt die Planung ab, das andere den Betrieb.
- **Projekte:** 825833, 783913.
- **Zitate:**
  - 825833: „some of the modules scheduled to be functional in a second version of the tool"
  - 783913: „The delivered of the task T 5.1 Data gathering components of ZephyAnalytics has been delayed"
  - 783913: „disruptive, opensource wind modelling software package called ZephyTOOLS"
- **Warum es zählt:** Zeitreihen-Grundmodelle passen zum Hindernis. Der Katalog nennt nur eine Studie und verlangt gelabelte Ausfalldaten.
- **Erster Schritt:** Prüfen, ob der ZephyTOOLS-Code noch abrufbar ist, und ein Diagnose-Modul auf offenen SCADA-Daten testen.

**8. Atom-Modelle treffen zwei von vier Projekten** (Art 3)
- **Vermutung:** UMA ersetzt selbstgebaute Kraftfelder (P29893, GPP204/10/P331). Bei P23390 (Trap-Level) und P15700 (magnetische Anisotropie) geht es um elektronische Größen. Ein Atom-Modell liefert die nicht; die Sonnet-Zuordnung ist dort zu optimistisch.
- **Projekte:** 10.55776/P29893, GPP204/10/P331, 10.55776/P23390, 10.55776/P15700.
- **Zitate:**
  - P29893: „At a later stage, the force fields derived will be used to simulate the adsorption of selected gas molecules."
  - GPP204/10/P331: „Poté byl projekt ukončen z důvodu mateřské dovolené řešitelky."
  - P15700: „The energy resolution of the current computational methods is, however; too poor to reliably assign this contribution to one er more of the live possible Fe sites."
  - P23390: „demonstrating that both of them are still good candidates for a BTI defect"
- **Warum es zählt:** GPP204/10/P331 ist der sauberste Fall: klarer Abbruch, klare Frage, reine Rechnung. Der Markt ist schwach. Das P29893-Zitat stammt aus dem Antrag; bei 16 Arbeiten ist die Lücke wohl geschlossen.
- **Erster Schritt:** Au-Ausbreitung auf Si(111) mit UMA und kinetischem Monte Carlo rechnen und an wenigen DFT-Punkten gegenprüfen.

**9. Textextraktion: Hindernis gelöst, Vorsprung weg** (Art 3)
- **Vermutung:** Heutige Sprachmodelle lösen vermutlich die Hindernisse der ersten drei Projekte. Dadurch ist der Vorsprung der Projekte verloren. Wert haben nur noch ihre Prüfdaten.
- **Projekte:** 101112727, 10.55776/M1729, FW03010656, 641222.
- **Zitate:**
  - 101112727: „this has not yielded robust results with regards to the clustering of the impact categories"
  - M1729: „The existence of many false positive predications still limits the usefulness of the resulting knowledge repository."
  - FW03010656: „místo toho udělali jen sadu jednotlivých funkcí bez jakékoli integrace"
  - 101112727: „publicly available one-of-its-kind global database of impacts from multiple categories of climate extremes"
- **Warum es zählt:** Solche Projekte punkten hoch, bieten Nick aber kein Alleinstellungsmerkmal. Das ist ein Signal für die Kriterien, kein Kandidat.
- **Erster Schritt:** Ein Sprachmodell gegen die Klimafolgen-Datenbank und den M1729-Goldstandard messen. Liegt es klar vorn, die Gruppe abwerten.

**10. Selbstoptimierender Tröpfchen-Aufbau** (Art 5)
- **Vermutung:** 101081171 liefert die Messung per Kamera und nennt die Regelung als offenen Schritt. 101069237 liefert die Versuchsplanung, fand aber keinen Markt. Zusammen ergibt das einen geschlossenen Regelkreis.
- **Projekte:** 101081171, 101069237.
- **Zitate:**
  - 101081171: „there exists no other dataset containing labeled droplet images specific to microfluidics, apart from the one curated within this project"
  - 101081171: „These functionalities will be pivotal for the development of commercial software prior to market entry."
  - 101069237: „yielding a descriptive model that allowed control of the output of the network towards any cost function"
  - 101069237: „Further uptake and success is not determined by the technical or scientific quality of our results, but by a lack of a market"
- **Warum es zählt:** Der Datensatz ist ein echter Startvorteil. Ein Aufbau aus Kaufchip, Eigenbau-Spritzenpumpen und USB-Mikroskop liegt vermutlich im Budget. Ob Labore dafür zahlen, ist offen.
- **Erster Schritt:** Datensatz und Gewichte laden, Tropfenmasken ergänzen, dann Bayes-Optimierung auf Tropfengröße in der Simulation testen.

**11. Beschönigende Formeln** (Art 4)
- **Vermutung:** Zwei Projekte nutzen fast wortgleichen Vorlagentext. Dahinter steht vermutlich kein nutzbares Produkt.
  - 737424: „a commercial simulation tool including such features for the study of ice-ship interaction situations is simply not available" und „towards the initial steps of an innovation process"
  - 664910: „a commercial casting simulation code including such comprehensive features of computational speed and advanced physics is simply not available" und dieselbe Schlussformel.
- Weitere Formeln und was vermutlich dahintersteckt:

| ID | Formel (wörtlich) | Vermutetes Scheitern |
| --- | --- | --- |
| 713671 | „the proposed technology on its own is insufficient for a full deployment" | Ortungs-Infrastruktur fehlte |
| 966733 | „more challenges that need to be addressed before a marketable product can be defined" | Verfahren ließ sich nicht verallgemeinern |
| 101069457 | „didn't reach SOTA performance, probably, due to the usage of compressed videos" | Methode unterlegen, Schuld bei den Daten gesucht |
| 812167 | „we shifted our focus from developing a physical controller to integrated hand-tracking" | Controller aufgegeben |
| FR-TI3/018 | „Parametry vzorků zatím nedosahují hodnot zadání úkolu." | Funktionsmuster verfehlte die Werte |
| 101123091 | „currently implemented only as beta-versions" | Kernablauf unfertig trotz Erfolgsmeldung |
| 101081361 | „with some statistical confidence" | Trennschärfe gering |
| 768610 | „a few major hurdles still need to be taken" | Hürden unbenannt, kein System |
| 10.55776/P25449 | „Although our results are not perfect" | Ansatz nur als Konzept gezeigt |

- **Warum es zählt:** Diese Formeln sind Suchbegriffe. FR-TI3/018 und 966733 sind echte technische Hindernisse.
- **Erster Schritt:** Die Formeln als Liste in die Haiku-Suche für Häppchen 2 geben und Vorlagentexte per Duplikat-Suche markieren.

**12. Personalabbruch: Aufstieg oder Ausfall** (Art 1)
- **Vermutung:** Wer wegen eines besseren Angebots ging, hat das Thema wohl mitgenommen. Nach einem Ausfall liegt es eher brach.
- **Projekte:** Aufstieg: GA19-23165S, 10.55776/M2393, GA102/99/D033. Ausfall: GPP204/10/P331, GA102/98/P059, GPP202/12/P180, GA102/00/P083.
- **Zitate:**
  - GA19-23165S: „na žádost řešitele, jenž získal prestižní grant ERC.CZ."
  - M2393: „a permanent position as an Associate Professor at Aalborg University, Denmark"
  - GA102/98/P059: „z důvodu nové zákonné úpravy o pobytu cizinců"
  - GA102/00/P083: „byl však vytvořen dobrý základ pro pokračovatele."
- **Warum es zählt:** Personalabbrüche erfüllen die Pflicht oft, haben aber einen dünnen offenen Kern. Die Unterscheidung spart Prüfarbeit.
- **Erster Schritt:** Je Fall die späteren Arbeiten der Person in OpenAlex abfragen (Autor, nicht Thema).

**13. Versicherer als gemeinsamer Abnehmer** (Art 5)
- **Vermutung:** Die Klimafolgen aus Texten (101112727), die Schadenserkennung aus Fotos (768610) und die offenen Gebäudegeometrie-Bausteine (727334) ergeben zusammen eine Kette vom Ereignis zum Gebäudeschaden.
- **Projekte:** 101112727, 768610, 727334.
- **Zitate:**
  - 768610: „Our new process is of high interest, however, a few major hurdles still need to be taken."
  - 727334: „The classification and shape detection components are already released and accessible from the CGAL web site"
- **Warum es zählt:** Kein Einzelfall ist stark, der Kunde ist aber derselbe. Haiku ordnet 768610 dem Muster H11 zu; die Hürden können also rechtlich sein.
- **Erster Schritt:** Zwei Gespräche mit Schadenregulierern: Welche Hürde war 2018 gemeint?

## Die drei stärksten Funde

**Fund 1 (mit 2 und 3):** Das Muster „Messdaten da, Modell fehlt" trifft genau Nicks Profil, weil der Laborteil bezahlt ist und der Rest Rechnung ist. Im Partikel-Cluster ist zusätzlich ein Kleinprototyp im Budget denkbar.

**Fund 5:** Die Kombination aus 101069165 und 822620 hat ein klar benanntes Hindernis, das Sprachmodelle direkt angehen. Sie ist reine Software und der Erfolg lässt sich maschinell prüfen.

**Fund 10:** Der Tröpfchen-Datensatz ist der einzige belegte Startvorteil im Häppchen, der mit einem günstigen Aufbau zusammenpasst. Schwach bleibt die Marktfrage, die 101069237 schon einmal negativ beantwortet hat.

## Vorschlag für Häppchen 2

**Was Häppchen 1 zeigt**
- „Pflicht ja" je Pool: cep_fail 14 von 20, sme2 4 von 6, fwf_obst 6 von 23, poc 11 von 51.
- 36 von 100 haben keinen offenen Kern (k1 nicht erfüllt) und stehen trotzdem in den oberen 100. Die Summe belohnt offenbar fertige Software.
- Nur 2 von 100 zielen auf einen Prototyp. Nicks Budget von 1.000 € bleibt ungenutzt.
- 7 OpenAlex-Abfragen liefern 0 Treffer (z. B. 693579, 101069402, FR-TI3/018). Das ist vermutlich ein Abfragefehler und kein Befund.
- Viele Toptreffer sind themenfremd: bei 790340 ein Hochschul-Studiengang, bei 101123027 Bakterien.

**Pools**
- **Mehr:** cep_fail und riv. Bei riv gezielt nach Ergebnisart suchen: Funktionsmuster, Prototyp, Software, Gebrauchsmuster, „bisher ungenutzt".
- **Neu, gefiltert:** gw, nur Technik, Informatik, Physik. Der Abbruchgrund liegt dort klar außerhalb der Idee; die Teams sind aber noch aktiv.
- **Probe von je 200:** sbir1 und sme1_noP2. Dort gibt es vermutlich nur Antragstexte ohne Ergebnis. Nur behalten, wenn ein Hindernis-Zitat vorliegt.
- **Weniger:** poc, nur noch mit Hindernis-Zitat aus dem Ergebnistext. cep_pos und fwf_pos nur mit hartem Zitat für einen offenen Schritt.

**Suchbegriffe**
- **Tschechisch:** „nebylo dosaženo", „nepodařilo se", „nebyl vytvořen model", „nebyla dokončena", „parametry nedosahují", „předčasně ukončen", „výpočetně náročné", „ruční vyhodnocení", „funkční vzorek".
- **Englisch:** „could not be predicted", „not satisfactorily", „did not reach", „further research is required to scale", „beta version", „not yet released", „loss of a key", „computational cost", „manual preparation".
- **Formeln aus Fund 11** als eigene Liste.
- **Zwillingssuche zu den Clustern:** Zyklon, Blasen, Granulat, Populationsbilanz; SPS, IEC 61131, formale Spezifikation; Wind-SCADA; Tröpfchen-Mikrofluidik.

**Kriterien**
- **Harte Schwelle:** offener Kern mit Zitat aus dem Ergebnistext (k14 = ausgang). Zitate aus dem Antrag zählen nicht.
- **Bonus** für „Messdaten vorhanden, Modell fehlt".
- **Bonus** für benannte Daten oder Prüfsätze (wie 101081171, 10.55776/P30930, 10.55776/P27351).
- **Bonus** für einen Prototyp im Budget: Sensorik, Messtechnik, kleine Mechanik und Strömung; Muster H2, H6, H8.
- **Abzug** bei Ausgründung, bei „backbone of a commercial product" und bei Vorlagentext.
- **Abzug**, wenn ein heutiges Grundmodell die Aufgabe ohne das Projekt löst (Fund 9; ebenso Handverfolgung: 812167, 790469, 664800).
- **Personalabbruch** nach Aufstieg oder Ausfall trennen und bei Aufstieg die Autor-Abfrage vorschalten.
- **OpenAlex:** Titel vorher ins Englische übersetzen, mit Fachbegriffen statt Akronymen suchen und 0 Treffer als „Prüfung fehlgeschlagen" werten.
