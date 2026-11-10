# A04: Punktzahl und Rangliste statt Ja/Nein (kostenlos)

Status: Auftrag von Nick, 10. November 2026. Kostenlos, keine API-Aufrufe.

Auftragstext (wörtlich):

Ziel: Statt eines wackeligen Ja/Nein von Haiku eine Punktzahl und eine Rangliste testen. Dazu Haikus Stichprobe selbst bewerten und die Sonnet-Kosten je Schwelle berechnen. Alles mit den vorhandenen Haiku-Antworten aus v0.1 und v0.2. Den Prompt nicht ändern.

1. Prüfset korrigieren: FW01010098 von „gut“ auf „grenzfall“ setzen. Grund: Der Text nennt kein Hindernis, die Einstufung beruhte auf dem Titel. Damit zählen 8 gute Fälle (ohne die zwei schon weitergeführten) und 21 Grenzfälle.
2. Skriptfehler beheben: In weiter_regel.py zählt „unklar“, wenn irgendein Feld des Eintrags ein Zitat enthält, nicht nur das Feld hindernis.
3. Punktzahl je Eintrag: Fehlende Felder zählen 0.
   +2 technisches Hindernis ja, +1 unklar
   +2 Hindernis-Muster H1, H2 oder H3; +1 H4 bis H7
   +2 Rechenanteil hoch, +1 mittel
   +1 Abbruchgrund Geld, Personal oder Organisation
   +1 offener Schritt ja (RIV-Code O zählt als ja)
   +1 Teilerfolg vorhanden
   +1 unerledigter Kern ja
   −2 Abbruchgrund formal ohne technisches Hindernis
4. Schwellen finden:
   Rang aller 8 guten und 21 Grenzfälle im Prüfset, getrennt für v0.1 und v0.2.
   Schwelle S1: niedrigste Punktzahl, ab der alle 8 guten und mindestens 80 % der Grenzfälle drin sind.
   Schwelle S2: niedrigste Punktzahl, ab der nur alle 8 guten drin sind.
   Für S1 und S2: Anteil der 100 Zufallseinträge mit mindestens dieser Punktzahl, gesamt und je Pool. Hochgerechnet auf 17.421 Einträge.
   Prüfe auch, ob ein Pool fast nie oder fast immer über der Schwelle liegt. Das deutet auf eine verzerrte Regel hin.
5. Stichprobe selbst bewerten: Lies die 20 Beispiele in ergebnisse/haiku_v02_stichprobe.md. Lies dazu für jedes den Originaltext aus ergebnisse/zufall100_eingabe.jsonl, nicht nur Haikus Zitate. Stufe jedes ein:
   B, prüfenswert: Technik oder angewandte Wissenschaft im erlaubten Fachgebiet. Ein konkreter Kern blieb offen. Das Hindernis lässt sich mit einem Werkzeug aus docs/03_faehigkeiten_katalog.md plausibel angehen. Es gibt erkennbare Anwender.
   Grenzfall: teilweise so, aber unsicher.
   C, ungeeignet: nur formaler Grund, Grundlagenforschung ohne Anwendung, fertiges Produkt, offensichtlich überholt, ausgeschlossenes Fach, militärisch ohne zivile Nutzung.
   Je Eintrag eine Zeile: ID, deine Stufe, Haikus Punktzahl, ein Satz Begründung. Danach melden:
   Wie viele B und Grenzfälle sind unter den 10 Ausgesiebten?
   Wie viele C unter den 10 Durchgekommenen?
   Hätte die Punktzahl mit S1 oder S2 besser getrennt als die Regel aus v0.2?
   Bleib lösungsorientiert: Ein Hindernis ist kein Ausschlussgrund. Markiere unsichere Urteile als unsicher. Du bist ein einzelner Prüfer, die Urteile sind vorläufig.
6. Kosten für Sonnet je Schwelle berechnen:
   Miss die echten Token-Zahlen aus den Daten: Zeichen geteilt durch 4 als Näherung, oder genauer, wenn du ein Zählwerkzeug ohne API-Aufruf hast.
   Fester Prompt-Teil: Anweisung aus prompts/sonnet_bewertung.md plus die Katalog-Abschnitte Querschnitt, Fachgebiete, Übersetzungstabelle, Grenzen.
   Variabler Teil: Text je Eintrag plus Haiku-Felder. Ausgabe: das JSON-Schema aus sonnet_bewertung.md.
   Preise Sonnet 5.5: 2 $ je Million Token Eingabe, 10 $ Ausgabe, Batch −50 %. Zwischengespeicherter Prompt-Teil beim Lesen nur 10 % des Eingabepreises.
   Tabelle: Schwelle, Anzahl Einträge, Kosten ohne und mit Zwischenspeicher. Schreib dazu, welche Annahmen unsicher sind, vor allem die Ausgabelänge.
7. Empfehlung: In wenigen Sätzen: Welche Schwelle würdest du für den ersten Sonnet-Lauf nehmen? Wie viele Einträge, was kostet es? Was sollte vorher am Prompt noch geändert werden? Begründe mit den Zahlen aus 4 bis 6. Nichts starten.
8. Abschluss: Bericht als pruefset/punktzahl_test_<datum>.md mit allen Tabellen. Die Bewertung der 20 Beispiele als pruefset/stichprobe_v02_bewertung.md. Tagebuch, „Stand“ aktualisieren, OFFENE_PUNKTE ergänzen, commit, push. Danach im Terminal eine Kurzfassung für Nick ausgeben, höchstens 25 Zeilen: Ergebnis S1/S2, Durchlassquote, Bewertung der 20 Beispiele, Kostentabelle, Empfehlung.
