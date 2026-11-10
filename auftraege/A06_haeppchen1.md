# A06: Kriterien schärfen, Häppchen 1 mit Fable

Status: Auftrag von Nick, 10. November 2026, direkt an Claude Code. Ersetzt A05 ab Phase 3. Freigaben 2026-11-10-A06a bis -A06e (siehe `ENTSCHEIDUNGEN.md`). Haltepunkte: Phase 3 (wenn die Testregel nicht besteht), Phase 5 (wenn weniger als 80 % der guten die Startschwelle erreichen), Phase 8 (Ende).

Auftragstext (wörtlich):

Auftrag A06 von Nick: Kriterien schärfen, Häppchen 1 mit Fable. Ersetzt A05 ab Phase 3. Lege auftraege/A06_haeppchen1.md mit diesem ganzen Text an.
Freigaben (mit dieser Nachricht erteilt, in ENTSCHEIDUNGEN.md eintragen):
2026-11-10-A06a: Haiku-Test v0.3 am Prüfset, höchstens 0,50 $
2026-11-10-A06b: Haiku auf Häppchen 1, höchstens 2 $
2026-11-10-A06c: Sonnet am Prüfset, höchstens 2 $
2026-11-10-A06d: Sonnet auf die Auswahl aus Häppchen 1, höchstens 5 $
2026-11-10-A06e: Fable 5.2 (claude-fable-5-2) für Tiefenprüfung und freie Suche, höchstens 8 $ einschließlich Websuche
Sitzungsbudget Claude Code: 10 $
Vor jedem bezahlten Schritt mit scripts/kosten.py schätzen. Über der Obergrenze anhalten.
Tempo: Kein Batch-Verfahren. Direkte API-Aufrufe parallel, zum Beispiel 10 bis 20 gleichzeitig, mit Wiederholung bei Ratenlimit. Ergebnis je Eintrag sofort als JSONL, fortsetzbar. Ziel: jeder Lauf in Minuten, nicht in Stunden.
Phase 0, Abschluss von gestern:
Übernimm die 55 Einträge aus pruefset/a05_neue_eintraege.csv ins Prüfset (15 gute, 46 Grenzfälle, 43 ungeeignete).
Ergänze CLAUDE.md um die Abschnitte ‚Haltepunkte‘ und ‚Sitzungsbudget‘.
Phase 1, neue Kriterien (in docs/04_pipeline.md und prompts/sonnet_bewertung.md): Erkenntnis aus der Prüfung von fünf Kandidaten im Planungs-Chat: Die Suche funktioniert, aber drei von fünf scheiterten an fehlenden Kriterien.
K11 Eigenständiger Vorteil (Pflicht): Welche konkrete Eigenschaft der damaligen Entwicklung bietet heute noch einen eigenen Vorteil? Zum Beispiel Patent, Datensatz, besondere Bauweise, Messergebnis, Nische, Erkenntnis. Mit Zitat. Ohne so eine Eigenschaft bleibt nur eine Idee, die heute jeder haben kann: dann niedrig.
K12 Für Nick umsetzbar (Pflicht): Der erste Schritt ist Software, Simulation, Datenanalyse oder ein Prototyp, den eine Person mit KI-Anleitung, Teilen aus Deutschland und rund 1.000 € Material in einigen Wochen bauen kann. Daten öffentlich oder bezahlbar kaufbar. Nicht umsetzbar, wenn der erste Schritt Reinraum, Speziallabor, Tierversuche, klinische Studien oder Zulassung braucht.
K13 Keine Massenware: Macht ein heutiges Grundmodell oder ein verbreitetes offenes Werkzeug den Ansatz trivial? Dann niedrig, außer K11 trägt.
K14 Hindernis aus dem Ausgang: Das Hindernis stammt aus Bewertung, Endbericht oder Ergebnisbericht, nicht aus der Motivation. Beispiel I5180: Das Hindernis stand in der Motivation, der Endbericht meldet Erfolg.
Gewichtung: K11 und K12 je 0–3 und doppelt, K13 0–3. Pflicht für die Auswahl: K1, K2, K11 und K12 mindestens 1. Höchstwert neu rechnen, Startschwelle am Prüfset eichen.
Elternzeit, Mutterschaft, Weggang und Krankheit gelten als Abbruchgrund ‚Personal‘, nicht ‚formal‘.
Phase 2, Haiku v0.3 bauen (kostenlos):
Zwei Varianten nach texttyp:
‚ergebnis‘: Hindernis mit hindernis_quelle (ergebnis, motivation oder unklar), Abbruchgrund, offener Schritt.
‚antrag‘: technisches Kernrisiko als H1 bis H11.
In beiden: Rechenanteil, Anwendung, art_des_ersten_schritts (software, simulation, datenanalyse, prototyp_klein, labor, reinraum, zulassung, unklar). Belege nur wörtlich, höchstens 250 Token. Texte v2.
Auswahlregel:
Ergebnis-Texte kommen weiter mit Hindernis aus hindernis_quelle ‚ergebnis‘ oder ‚unklar‘, mit Abbruchgrund außerhalb der Idee oder mit offenem Schritt.
Antrags-Texte kommen in eine Rangliste: H1 bis H3 zuerst, dann Rechenanteil, dann die Art des ersten Schritts.
Labor, Reinraum und Zulassung nach hinten, nichts löschen.
Phase 3, Haiku-Test (A06a): Prüfset und die 100 Zufallseinträge.
Weiter, wenn alle 15 guten durchkommen oder im oberen Viertel der Rangliste liegen und mindestens 80 % der Grenzfälle auch.
Sonst Haltepunkt.
Phase 4, Häppchen 1, Haiku (A06b):
Pools poc, sme2, cep_fail, fwf_obst (rund 2.700 Einträge).
Danach zitat_check und Auswahl. Zählen je Pool.
Phase 5, Sonnet:
Erst am Prüfset (A06c). Weiter, wenn mindestens 80 % der guten Fälle die Startschwelle erreichen.
Dann auf die Auswahl aus Häppchen 1 (A06d), sortiert nach Haiku, von oben bis zur Obergrenze.
Phase 6, Fortsetzungscheck: openalex_check.py im schnellen Modus für die oberen 100 nach Sonnet-Punkten.
Phase 7, Fable (A06e):
7a Tiefenprüfung der oberen 30: Fable bekommt je Kandidat Originaltext, Haiku- und Sonnet-Ergebnis, OpenAlex-Treffer und den Fähigkeiten-Katalog. Es darf je Kandidat bis zu 5 Websuchen machen. Auftrag:
Noch offen oder von anderen gelöst?
Welche konkrete Eigenschaft gibt heute einen eigenen Vorteil?
Was wäre ein erster Schritt mit Nicks Mitteln, mit Kosten in Euro?
Wer würde zahlen?
Was ist die entscheidende offene Annahme?
Lösungsorientiert: Ein Hindernis ist eine Aufgabe, kein Ausschlussgrund. Belege nur aus geöffneten Quellen, sonst ‚unbelegt‘.
7b Freie Suche über die oberen 100 zusammen, in einem langen Aufruf: Fable soll mit eigenem Blick suchen nach:
demselben Hindernis in mehreren Projekten,
Teilergebnissen, die sich ergänzen,
einem heutigen Werkzeug, das mehrere alte Projekte zugleich löst,
beschönigenden Formeln, hinter denen ein technisches Scheitern steckt,
neuen Ansätzen oder Geschäftsideen, die erst aus der Kombination entstehen, auch wenn kein Einzelfall stark ist.
Alles als Vermutung kennzeichnen, mit Zitat und Projekt-ID. Dazu: Wie sollten wir Häppchen 2 schneiden (Pools, Suchbegriffe, Kriterien), damit die Ausbeute steigt?
Fable weicht bei Biologie-Themen auf ältere Modelle aus. Das im Bericht vermerken, nicht umgehen.
Phase 8, Ergebnis für Nick (Haltepunkt):
kandidaten/RANGLISTE.md mit den oberen 30, je eine Zeile: ID, Pool, Kurztitel, Punkte, eigenständiger Vorteil, erster Schritt, Fable-Urteil.
Für die oberen 10 eine Kandidatenkarte nach kandidaten/_VORLAGE.md, mit Fables Tiefenprüfung.
kandidaten/beobachtungen.md mit Fables freien Funden und dem Vorschlag für Häppchen 2.
Tagebuch, ‚Stand‘, ENTSCHEIDUNGEN mit den tatsächlichen Kosten, commit, push.
Im Terminal ausgeben: die oberen 30 in Kurzform, die drei stärksten Funde aus 7b und den Vorschlag für Häppchen 2. Nicht weitermachen.

## Anmerkungen von Claude Code beim Anlegen

- CLAUDE.md enthält „Haltepunkte“ und „Sitzungsbudget“ schon seit A05 Phase 0 (Commit 479a486). Für A06 gilt das Sitzungsbudget 10 $ aus diesem Auftrag; CLAUDE.md bleibt bei 5 $ als Grundregel.
- `scripts/kosten.py` existierte noch nicht (war A05 Phase 3); wird in A06 Phase 2 gebaut.
- `claude-fable-5-2` laut Modell-Liste der API vorhanden (angelegt 2026-11-09).
- Freigabe-ID 2026-11-10-A06 (ohne Buchstaben, Sonnet am Prüfset aus A05) ist durch A06c ersetzt; die neuen IDs tragen Buchstaben.
