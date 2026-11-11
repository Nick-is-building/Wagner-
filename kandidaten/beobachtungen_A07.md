# Beobachtungen A07 (freie Suche über die oberen 40)

Fable 5.2, ein Aufruf ohne Websuche (`ergebnisse/fable_a07_frei.jsonl`, Modell claude-fable-5-2, 1.45 $). Alles unten ist **Vermutung** von Fable, nicht von Hand geprüft.

Alle Aussagen unten sind Vermutungen aus den Kurzfeldern; ich habe keine Volltexte geprüft, und Datenzugang und Rechte sind fast überall unbelegt. Tschechische Zitate stehen wörtlich, mit kurzer Übersetzung in Klammern.

## Verbindungen

1. **Vermutung: Vier Projekte scheitern am selben fehlenden Modell, nämlich Zerfall und Zusammenlagerung von Blasen oder Partikeln in turbulenter Strömung.**
   - Projekte: GA15-15467S, 10.55776/P17185, TC4-043, GA15-05534S.
   - Zitate:
     - GA15-15467S: „Publikování dalších výsledků v časopise je teprve v přípravě (model pro rozložení velikosti částic po rozpadu).“ (Modell der Größenverteilung nach dem Zerfall ist erst in Vorbereitung.)
     - P17185: „However, the separation of small particles could not be predicted satisfactorily.“
     - TC4-043: „Nedosáhlo se těch parametrů, které se předpokládaly dle matematického modelu.“ (Die vom Modell erwarteten Parameter wurden nicht erreicht.)
     - GA15-05534S: „Hlavní publikované výsledky jsou ale zaměřeny zejména experimentálně.“ (Die publizierten Ergebnisse sind vor allem experimentell.)
   - Warum es zählt: Ein einziger Rechenaufbau könnte alle vier bedienen: offene Strömungssimulation mit Partikelverfolgung und an Messdaten angepassten Zerfalls- und Haftgesetzen. Drei der vier haben Messdaten, keines ein passendes Modell.

2. **Vermutung: Die beiden Fliehkraftabscheider-Projekte ergänzen sich; eines liefert Daten und eine Hypothese, das andere einen ungeklärten Fehlschlag.**
   - Projekte: 10.55776/P17185, TC4-043.
   - Zitate:
     - P17185: „It may be that direct wall contact is involved in making two particles cling together.“ und „Extensive PDA and LDA measurements are here available.“
     - TC4-043: „Projekt předčasně ukončen.“ (Projekt vorzeitig beendet.)
   - Warum es zählt: Ein an den Daten von P17185 geprüftes Modell mit Wandkontakt könnte die Lücke bei TC4-043 erklären.
   - Einschränkung: Bei TC4-043 ist nicht belegt, in welche Richtung das Modell danebenlag. Die Messdaten von P17185 sind nur im Antrag erwähnt.

3. **Vermutung: Das Leckprüf-Projekt ist im Kern ein Blasen-Akustik-Problem, und das Blasenprojekt liefert die fehlende Physik.**
   - Projekte: 673155, GA15-15467S.
   - Zitate:
     - 673155: „BIC used the data provided by Floteks and explored different statistical tools and signal processing tools.“ und „Sensitivity tests of the algorithm based on laser drilled nozzles with different hole sizes.“
     - GA15-15467S: „Hlavním přínosem projektu je získání experimentálních dat týkajících se rozpadu bublin v turbulentním proudění.“ (Hauptbeitrag sind experimentelle Daten zum Blasenzerfall.)
   - Warum es zählt: 673155 hat laut Zitat nur statistische Werkzeuge probiert. Ein Modell, das Lochgröße, Blasengröße und Blasenton verknüpft, fehlt offenbar.
   - Einschränkung: Dass Blasen je nach Größe mit eigener Frequenz klingen, ist mein Fachwissen und steht nicht im Material. Dass im Wasserbad Blasen der Leckindikator sind, steht nur in der Sonnet-Marktangabe.

4. **Vermutung: Selbsterregtes Flattern und Energieernte aus dem Wirbelnachlauf sind dieselbe Messgröße mit umgekehrtem Vorzeichen, nämlich die von der Strömung auf einen schwingenden Körper übertragene Leistung.**
   - Projekte: GA13-10527S, 101188523.
   - Zitate:
     - GA13-10527S: „měření při samobuzených, nikoliv vynucených oscilacích“ (Messung bei selbsterregten, nicht erzwungenen Schwingungen) und „Není provedeno vyhodnocení a shrnutí výsledků.“ (Auswertung und Zusammenfassung fehlen.)
     - 101188523: „Further research is required to investigate the mechanisms for energy extraction and to quantify the actual power output.“
   - Warum es zählt: GA13-10527S hat sieben veröffentlichte Arbeiten, darunter „Experimental investigation of flow-induced vibration of a pitch–plunge NACA 0015 airfoil under deep dynamic stall“. Sie könnten als Prüfdaten für ein Leistungsmodell dienen, das 101188523 fehlt.

5. **Vermutung: Ein universelles Atom-Modell (UMA) trifft drei alte Projekte zugleich.**
   - Projekte: 10.55776/P15464, 10.55776/M2441, 10.55776/P27738.
   - Zitate:
     - P15464: „it was not possible to determine the exact size of the clusters“.
     - M2441: „Future work should be aimed to link the properties that can be modelled -using computational tools- with the final properties of the materials“.
     - P27738: „so that so far no results have been extracted from the raw data that were accumulated in these measurements“.
   - Warum es zählt: Zwei Projekte betreffen flüssige Legierungen, das dritte Elastizität unter Druck. Alle drei rechneten damals mit teurer DFT, die heute nach Katalog „von Stunden auf unter eine Sekunde“ fällt.
   - Einschränkung: Der Katalog nennt Schwächen bei seltenen Elementen und Zuständen. Schmelzen und Arsen sind dafür Kandidaten.

6. **Vermutung: In vier Projekten gelingt das Erkennen, aber das Zählen oder Beziffern nicht.**
   - Projekte: 101100903, 693433, 101112727, 673155.
   - Zitate:
     - 101100903: „the quantification of the amount of tomatoes was less accurate (about twice better than a random pick)“.
     - 693433: „Capturing efficiency of CD4+T cells was slightly lower (~80%).“
     - 101112727: „not yielded robust results with regards to the clustering of the impact categories and the ability of our pipeline to extract quantitative information“.
     - 673155: „was not at TRL9 level and needs to be improved further“.
   - Warum es zählt: Vermutlich ist die Mengenschätzung das gemeinsame Hindernis, nicht der Sensor. Ob Software das heilt, ist in keinem der vier Fälle belegt.
   - Einschränkung: 101100903 ist fachlich ausgeschlossen, 693433 ist ein Medizinprodukt.

7. **Vermutung: Mehrere Sensor-Prototypen haben eine systematische Störgröße, aber kein Korrekturmodell dafür.**
   - Projekte: 713619, 101123334, 665055, 666644.
   - Zitate:
     - 713619: „revealed the existency of significant fractionation effects on water isotopes related with membrane permeation at the inlet of the instrument“.
     - 101123334: „The current sensitivity is on the order of 10 µrad/s, but offsets (null-shift bias) are on the order of 100 µrad/s.“
     - 665055: „we found the method too sensitive to the quality of the electrode-skin contact impedance“.
     - 666644: „the initially identified risk of too low measurement accuracy due to high variation in biomass assortments“.
   - Warum es zählt: Das Muster ist gleich, die Hardware aber jeweils fremd und geschützt. Rechnerisch erreichbar ist nur der Korrekturteil, und nur mit Daten der Partner.

8. **Vermutung: Das nie gebaute Feldmodell für Mikrosysteme ist genau das, was zwei spätere Mikrofluidik-Prototypen brauchen.**
   - Projekte: GA203/07/1320, 899366, 713619.
   - Zitate:
     - GA203/07/1320: „na dvou ze čtyř plánovaných cílů (metodologie odhadu koncentrovaných polí a vypracování matematického modelu) nebylo během tří let řešení vůbec pr“ (an zwei von vier Zielen, darunter dem mathematischen Modell, wurde gar nicht gearbeitet).
     - 899366: „Further studies are needed to improve BFF performance for diagnostics.“
   - Warum es zählt: Ein Transportmodell für Strömung, Diffusion und Ladung im Kanal wäre ein Werkzeug für alle drei.
   - Einschränkung: Ob das Hindernis bei 899366 rechnerisch ist oder am Chipmaterial liegt, ist laut Sonnet unbelegt.

9. **Vermutung: Zwei Projekte holen mehr Auflösung aus schwachen Messungen über Vorwissen; ein drittes scheiterte an derselben Art Umkehrproblem.**
   - Projekte: 692804, 101069457, 665055, am Rand 10.55776/I2760.
   - Zitate:
     - 692804: „we were able to algorithmically enhance the resolution of optical imaging, bringing it to below one fifth of the optical wavelength.“
     - 101069457: „tinyMNIST datasets classification accuracy ranges from 89% to 94% where the standard frame-based input CNN on the same tiny images reaches 80%“.
     - I2760: Projektarbeit „Efficient computation of electrograms and ECGs in human whole heart simulations using a reaction-eikonal model“.
   - Warum es zählt: Die schnellen Vorwärtsmodelle aus I2760 zeigen, wie man solche Umkehrprobleme billig mit Trainingsdaten aus Simulation versorgt. Das fehlte 665055.
   - Einschränkung: Bei 692804 und 101069457 liegen Patente vor oder sind angemeldet.

10. **Vermutung: Bei mehreren Projekten sind die Daten verwaist, weil die Person ging oder die Auswertung nie stattfand.**
    - Projekte: 10.55776/P27738, 101123027, GA13-10527S, 899779.
    - Zitate:
      - P27738: „the following evaluation was delayed due to career changes by Dr. Wehinger“.
      - 101123027: „Full CFD simulation using OpenFOAM was hindered by the loss of a key expert“.
      - 899779: „we were still able to collect 48 neurotypical-child datasets and 38 autistic-child datasets“.
    - Warum es zählt: Das ist das Muster H4, das Code-Agenten nach Katalog am direktesten treffen. Offen bleibt überall der Datenzugang.
    - Zu prüfen: Großforschungsanlagen wie ESRF und ILL geben Messdaten nach einer Sperrfrist oft frei. Das ist mein Wissen und steht nicht im Material.

## Neue Ansätze

1. **Akustischer Leckprüfstand mit Blasenmodell.**
   - Projekte: 673155, GA15-15467S.
   - Idee: Leckgröße aus dem Blasenton schätzen, statt nur „Leck ja oder nein“ statistisch zu klassifizieren. Die Rohdaten von Floteks braucht Nick dafür nicht, er kann eigene aufnehmen.
   - Erster Schritt: Wasserbecken, Hydrophon, Audio-Interface, Druckluft mit Regler und feine Düsen in drei bis fünf Lochgrößen beschaffen. Kosten geschätzt 400 bis 700 €. Dann einige Hundert Aufnahmen mit und ohne Störgeräusch machen und ein Modell anpassen.
   - Wer zahlen würde: Tank-Zulieferer wie Floteks (im Material genannt). Vermutlich auch andere Betriebe mit Wasserbad-Dichtheitsprüfung, das ist unbelegt.
   - Risiko: OpenAlex meldet „Thema vermutlich weitergeführt“. Der Stand nach Projektende ist ungeklärt.

2. **Offener Vergleichsfall für die Feinstaub-Abscheidung im Zyklon.**
   - Projekte: 10.55776/P17185, TC4-043, GA15-05534S, GA15-15467S.
   - Idee: Ein Zyklon-Rechenmodell mit Wandhaftung und Agglomeratbruch, geprüft an veröffentlichten Daten. Daraus entsteht ein Auslegungsdienst für Abscheider.
   - Erster Schritt: Den Zyklon aus den Veröffentlichungen zu P17185 in OpenFOAM nachbauen, mit und ohne Wandkontakt-Haftung rechnen. Kosten geschätzt 100 bis 300 € GPU-Miete. Parallel die Autoren nach den LDA- und PDA-Daten fragen (0 €).
   - Wer zahlen würde: Hersteller von Entstaubungsanlagen und Anbieter von Strömungssoftware. Das sind Sonnet-Angaben, kein belegter Auftraggeber.

3. **Leistungsmodell für schwingende Profile, aus Flatterdaten geeicht.**
   - Projekte: GA13-10527S, 101188523.
   - Idee: Ein Modell, das die aus der Strömung entnommene Leistung eines elastisch gelagerten Profils vorhersagt. Für die Luftfahrt ist es eine Flattergrenze, für die Meeresenergie eine Ertragskarte.
   - Erster Schritt: 2D-Simulation eines Profils mit zwei Freiheitsgraden gegen die veröffentlichte NACA-0015-Arbeit prüfen. Kosten geschätzt 50 bis 200 € Rechenzeit. Ein kleiner Wasserkanal-Aufbau mit Generator wäre erst der zweite Schritt, geschätzt 600 bis 900 €.
   - Wer zahlen würde: Entwickler von Meeresenergie-Systemen. Im Material stehen NTNU und Inventas AS als Rechteinhaber von 101188523.

4. **Schmelzen-Rechnung als Dienst für Legierungsentwickler.**
   - Projekte: 10.55776/P15464, 10.55776/M2441, optional 10.55776/P27738.
   - Idee: Struktur und Kennwerte flüssiger Legierungen per Atom-Modell rechnen und mit Sinter- oder Lotversuchen verknüpfen.
   - Erster Schritt: Molekulardynamik einer Sb-Zn-Schmelze mit UMA rechnen und mit den veröffentlichten Beugungskurven vergleichen. Kosten geschätzt 100 bis 300 € GPU-Miete. Vorher die UMA-Lizenz prüfen.
   - Wer zahlen würde: Hersteller pulvermetallurgischer Stahlteile (M2441). Der Lot-Markt ist nur ein Nebensatz bei P15464. Die Zahlungsbereitschaft ist insgesamt dünn.

5. **Text-zu-Daten-Werkzeug mit öffentlichem Prüfstein.**
   - Projekte: 101112727, 812960.
   - Idee: Heutige Sprachmodelle ziehen Zahlen und Folgeketten aus Texten. Der annotierte Datensatz von 101112727 dient als Nachweis. Die Nutzerbasis von 812960 („used directly in R by hundreds of thousands of users worldwide“) ist der Vertriebsweg.
   - Erster Schritt: Ein aktuelles Sprachmodell gegen den Benchmark laufen lassen („manual annotation of a series of articles on impacts of extreme events to be used as training and test data“). Kosten geschätzt 50 bis 200 € API-Gebühren.
   - Wer zahlen würde: Rückversicherer und Katastrophenschutz (Sonnet-Angabe), dazu Sozialforscher ohne Programmierkenntnisse.
   - Risiko: Das Feld ist stark besetzt, und ein eigener Vorsprung ist unbelegt.

6. **Transportmodell für Mikrokanäle als Vorprüfung vor der Chipfertigung.**
   - Projekte: GA203/07/1320, 899366, 713619.
   - Idee: Das nie gebaute Feldmodell nachholen und damit Geometrie und Puffer des Trennfilters sowie die Membran-Fraktionierung durchrechnen.
   - Erster Schritt: Ein Modell für Strömung, Diffusion und Ladung an den veröffentlichten Werten von 899366 eichen („efficiency of >80% and an extraction purity >99.5%“). Kosten geschätzt 0 bis 100 €.
   - Wer zahlen würde: Hersteller von Probenaufbereitung (Sonnet-Angabe). Die Chipfertigung bleibt Partnerarbeit.

## Die drei stärksten Funde

1. **Blasen-Akustik-Leckprüfung (673155 mit GA15-15467S).** Sie passt am besten zu Nick, weil er Messdaten für unter 1.000 € selbst erzeugen kann und nicht auf fremde Rohdaten angewiesen ist. Offen ist, ob Floteks oder andere das seit Projektende gelöst haben.

2. **Zyklon-Feinpartikel-Modell (P17185 mit TC4-043, gestützt durch GA15-05534S und GA15-15467S).** Zwei unabhängige Projekte melden dieselbe Lücke zwischen Modell und Messung, und P17185 nennt eine prüfbare Ursache. Der Rechenanteil ist hoch, aber ein zahlender Auftraggeber ist nicht belegt.

3. **Flattern als Energieernte (GA13-10527S mit 101188523).** Die Verbindung entsteht erst aus der Kombination: Das eine Projekt hat veröffentlichte Schwingungsdaten ohne Auswertung, das andere einen Prototyp ohne Leistungsmodell. Der erste Schritt ist reine Simulation; ob die veröffentlichten Daten zur Eichung reichen, muss geprüft werden.
