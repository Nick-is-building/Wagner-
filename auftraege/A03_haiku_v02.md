# A03: Haiku-Prompt v0.2 (ein Durchlauf, Weiter-Regel im Skript)

Status: **freigegeben von Nick am 10. November 2026** (Freigabe-ID `2026-11-10-A03`, Obergrenze 0,50 $). Modell in Claude Code: Opus für die Prompt-Änderung.

Auftragstext (wörtlich, vom Planungs-Chat):

prompts/haiku_extraktion.md auf v0.2 ändern: nur noch ein Durchlauf. Neue Felder: unerledigter_kern (ja/nein/unklar mit Zitat) und abbruchgrund_art (Technik/Aufwand/Geld/Personal/Organisation/formal/unklar mit Zitat). „unklar“ ist nur noch erlaubt, wenn ein Zitat einen Hinweis zeigt; ohne Zitat gilt „nein“. Sonst bleibt der Prompt gleich.

Die Weiter-Regel kommt fest ins Skript, nicht in den Prompt: weiter, wenn unerledigter_kern nicht „nein“ ist UND mindestens eines gilt: technisches Hindernis ja/unklar, abbruchgrund_art Geld/Personal/Organisation, offener Schritt ja/unklar, Rechenanteil hoch. RIV-Einträge mit Nutzungscode O kommen ohne Haiku weiter.

Test A: Prüfset. Zählen nur die 9 guten (ohne die zwei schon weitergeführten) und die 20 Grenzfälle.

Test B: 100 Zufallseinträge aus data/zwischen/items.pkl (Startwert 2026, ohne Prüfset-IDs). Melde den Anteil, der weiterkommt, je Pool. Außerdem 10 zufällige Durchgekommene und 10 zufällige Ausgesiebte mit Titel und Haiku-Zitaten als ergebnisse/haiku_v02_stichprobe.md, damit der Planungs-Chat sie bewerten kann.

Erst Trockenlauf mit Kosten zeigen, dann starten. Bericht als pruefset/haiku_test_v02_<datum>.md. Tagebuch, commit, push.

## Nachtrag (von Nick, 10.11.2026, wörtlich)

Die RIV-Regel ist zu großzügig. Ändere scripts/weiter_regel.py: RIV-Einträge mit Nutzungscode O kommen nicht mehr ohne Prüfung weiter. Code O setzt offener_schritt auf ja. Weiter kommt so ein Eintrag aber nur, wenn Haiku zusätzlich rechenanteil mittel oder hoch ODER technisches_hindernis ja/unklar liefert. Für alle anderen Einträge bleibt die Regel gleich.
Wenn der laufende Lauf fertig ist: Schick nur die 11 bisher ungeprüften RIV-Einträge (2 Prüfset, 9 Zufall) an Haiku v0.2, innerhalb der Freigabe 2026-11-10-A03. Werte beide Tests mit der neuen Regel aus. Berichte zusätzlich: Wie viele der 11 kommen nach neuer Regel weiter, und ist der Grenzfall RIV …N0000005 dabei?
Hochrechnung: Wie viele der 744 RIV-Code-O-Einträge kämen voraussichtlich weiter, gemessen am Anteil in der Stichprobe? Haiku dafür nicht auf alle 744 schicken. Bericht ergänzen, Tagebuch, commit, push.
