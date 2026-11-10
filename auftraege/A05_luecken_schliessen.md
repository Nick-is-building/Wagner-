# A05: Lücken schließen (Texte, Prüfset, Haiku v0.3, Sonnet am Prüfset)

Status: Auftrag von Nick, 10. November 2026, direkt an Claude Code (Rolle Planungs-Chat eingeschlossen). Phasen 0 bis 3 kostenlos; Phase 4 bezahlt (Freigabe 2026-11-10-A05, Obergrenze 0,50 $); Phase 5 bezahlt (Freigabe 2026-11-10-A06, Obergrenze 2,00 $, nur wenn Phase 4 besteht).

Auftragstext (wörtlich):

Neue Sitzung, von Nick. Lies zuerst CLAUDE.md, in TAGEBUCH.md den ‚Stand‘ und die obersten drei Einträge, OFFENE_PUNKTE.md, pruefset/punktzahl_test_2026-11-10.md und pruefset/stichprobe_v02_bewertung.md. Fasse in fünf Zeilen zusammen, wo wir stehen.

Deine Rolle ab jetzt: Du übernimmst auch die Rolle des Planungs-Chats. Du planst, baust, wertest aus und bewertest selbst. Die Entscheidungsrechte aus CLAUDE.md bleiben: An den Haltepunkten unten hältst du an, und Geld gibst du nur im Rahmen der Freigaben aus.

Lege zuerst auftraege/A05_luecken_schliessen.md mit diesem ganzen Text an. Dann arbeite die Phasen nacheinander ab.

Phase 0, Regeln (kostenlos): Ergänze CLAUDE.md um zwei Abschnitte:
Haltepunkte: Jeder Auftrag nennt sie, dort immer anhalten.
Sitzungsbudget: Schätze nach jedem größeren Teilschritt grob die bisherigen Kosten dieser Claude-Code-Sitzung und halte bei 5 $ an.

Phase 1, Daten und Texte (kostenlos):
CORDIS-Ergebnisberichte laden: cordis-h2020reports-csv.zip und cordis-h2020reports-json.zip von https://cordis.europa.eu/data/, dazu die HORIZON-Fassungen.
Aus dem JSON nur die Berichte entpacken, deren Projekt in den Pools poc, sme1_noP2 oder sme2 liegt. Die Zuordnung Projekt-ID zu rcn steht in reportSummaries.csv. Das ganze JSON ist entpackt über 500 MB; das Zip danach löschen.
Behalte je Projekt die Felder summary, workPerformed und finalResults, vom letzten Bericht des Projekts.
Erwartete Abdeckung: sme1_noP2 rund 3.078 von 3.097, sme2 rund 1.158 von 1.168, poc rund 650 von 854. Neues Skript scripts/cordis_berichte.py und Aufruf in daten_laden.sh.
build_texts.py v2:
Texte nicht mehr nach 500 bis 600 Zeichen abschneiden. Höchstens rund 4.000 Zeichen je Eintrag.
Vorrang hat der Teil, der den Ausgang beschreibt: CEP-Bewertung, FWF-Endbericht, CORDIS workPerformed und finalResults, RIV-Nutzung und Parameter.
Neues Feld texttyp: ‚ergebnis‘, wenn ein Ausgangstext vorliegt (CEP, FWF, RIV, CORDIS mit Bericht), sonst ‚antrag‘ (SBIR, CORDIS ohne Bericht, Grant Witness).
Zähle je Pool und Texttyp.

Phase 2, Prüfset erweitern (kostenlos), von mir ausdrücklich beauftragt:
Ziel: mindestens 20 gute und 20 Grenzfälle, gemischt über die Pools. Heute sind es 8 gute, fast alle aus CEP. Aus den Antrags- und CORDIS-Pools fehlen gute Fälle fast ganz.
Ziehe Vorschläge aus allen Pools: aus den Einträgen mit Hindernis-Signal und zufällig. Lies je Vorschlag den vollen Text.
Bewerte mit den Kriterien aus docs/04_pipeline.md und dem Fähigkeiten-Katalog. Bleib lösungsorientiert: Ein Hindernis ist kein Ausschlussgrund.
Jeden Vorschlag bewertet zusätzlich ein Subagent unabhängig, ohne deine Begründung zu sehen. Sind beide uneins, wird es ein Grenzfall. Alles als ‚vorläufig, Doppelbewertung Claude‘ markieren.
Auch 5 Rückblick-Fälle suchen, wenn möglich: früher abgebrochen, später mit KI oder günstiger Rechenleistung gelöst (Muster: die Luftbilder P24116). Dafür darf scripts/openalex_check.py laufen.
Haltepunkt 1: Kurzfassung der neuen Prüfset-Einträge zeigen, je Eintrag eine Zeile. Erst nach meinem Okay weiter.

Phase 3, Haiku-Prompt v0.3 und Auswahlregel (kostenlos):
Zwei Prompt-Varianten nach Texttyp:
‚ergebnis‘ fragt nach Hindernis, Abbruchgrund und offenem Schritt.
‚antrag‘ fragt nach dem technischen Kernproblem oder Kernrisiko, dem Hindernis-Muster H1 bis H11 als Risiko, Rechenanteil und Anwendung. Dass ein Antragsprojekt liegen blieb, zeigen die Metadaten (keine Phase II, keine Folgeförderung), nicht der Text.
Abbruchgründe mit Beispielen definieren: Elternzeit, Mutterschaft, Weggang, Krankheit gelten als ‚Personal‘, nicht als ‚formal‘. ‚Formal‘ heißt nur: Papiere, Berichte, Indikatoren, Vertrag.
Belege nur als wörtliche Zitate, keine eigenen Kommentare. Ausgabe kompakt, Ziel höchstens 250 Token.
Auswahl:
Ergebnis-Texte mit technischem Hindernis, Abbruchgrund außerhalb der Idee oder offenem Schritt kommen alle weiter.
Antrags-Texte kommen in eine Rangliste: Kernrisiko vom Typ H1 bis H3, Rechenanteil, Anwendung.
Für die Rangliste gilt: Sonnet arbeitet sie später in Chargen von oben ab. Nach jeder Charge entscheide ich anhand der Ausbeute, ob es weitergeht. Keine feste Obergrenze, nichts wird gelöscht.
zitat_check.py: Die 14 nicht gefundenen Zitate ansehen und klären, ob das an der Normalisierung liegt (Anführungszeichen, Auslassungszeichen) oder ob Haiku umformuliert hat.
Kostenrechner scripts/kosten.py mit der gemessenen Zahl von 2,1 Zeichen je Token, den Preisen aus docs/04_pipeline.md, Batch-Rabatt und Zwischenspeicher. Er soll Haiku- und Sonnet-Kosten je Szenario ausgeben.

Phase 4, Haiku-Test v0.3 (bezahlt, Freigabe 2026-11-10-A05, Obergrenze 0,50 $):
Auf dem erweiterten Prüfset und 100 Zufallseinträgen, mit den Texten v2.
Testregel: alle guten kommen weiter oder liegen in der Rangliste im oberen Viertel, mindestens 80 % der Grenzfälle auch.
Bewerte 20 Beispiele selbst (10 durchgekommen, 10 ausgesiebt) und miss den Durchlassanteil je Pool.
Haltepunkt 2: Ergebnis zeigen.

Phase 5, Sonnet am Prüfset (bezahlt, Freigabe 2026-11-10-A06, Obergrenze 2,00 $; nur starten, wenn Phase 4 die Testregel besteht):
prompts/sonnet_bewertung.md auf kompakte Ausgabe umstellen und auf dem Prüfset laufen lassen.
Echte Ausgabelänge messen. Prüfen, ob die guten Fälle die Startschwelle von 13 Punkten erreichen.
Haltepunkt 3: Ergebnis und eine Kostenschätzung für den großen Lauf je Szenario. Zuerst Ergebnis-Texte vollständig, dann die oberen Chargen der Antrags-Texte.

Allgemein:
Trag beide Freigaben in ENTSCHEIDUNGEN.md ein.
Nach jeder Phase Tagebuch, commit, push.
SBIR-Phase-I, Grant Witness, erloschene Patente und KAKEN gehören nicht zu A05.
Kriterien, Schwellen und den Fähigkeiten-Katalog darfst du in diesem Auftrag nicht ändern. Fällt dir dort etwas auf, schreib es als Vorschlag in den Bericht.
Melde dich nach Phase 0 und 1 kurz mit den Zahlen.
