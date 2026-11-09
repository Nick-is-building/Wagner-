# Tagebuch

## Stand (höchstens sechs Zeilen, immer aktuell halten)

- Daten: Quellen geprüft; Skripte für Laden und Stufe 1 fertig und im Chat getestet (17.421 Einträge nach Frühfiltern). Auf der VM noch nicht geladen.
- Prüfset: 51 Einträge (11 gut, 20 Grenzfall, 20 ungeeignet). OpenAlex-Test darauf gelaufen.
- Prompts: Entwürfe v0.1 für Haiku, Sonnet, Opus; ungetestet.
- Nächster Auftrag: `auftraege/A01_daten_stufe1.md` (kostenlos). Danach A02 (Prüfset-Test mit Haiku, freigegeben, Obergrenze 0,50 $).
- Ausgegeben bisher: 0 $ API.

## Regeln

- Ein Eintrag pro Arbeitseinheit, höchstens zehn Zeilen, neueste oben.
- Nur, was ein Nachfolger wissen muss. Keine Rohausgaben, keine Projektbeschreibungen (die stehen in `kandidaten/`).
- Zahlen nur mit Herkunft (Datei oder Befehl).
- Alte Einträge nicht umschreiben; Korrekturen als neuer Eintrag mit Verweis.
- Ab 300 Zeilen wandern Einträge, die älter als einen Monat sind, nach `tagebuch_archiv/JJJJ-MM.md`; hier bleibt je Monat eine Zeile mit Verweis.

Format:

```
### JJJJ-MM-TT HH:MM UTC · Chat | Code (Modell) · Auftrag · Kurztitel
- Gebaut/geändert: Pfade
- Getestet: Befehl und Ergebnis (oder „nicht getestet“)
- Beobachtet: Zahlen mit Herkunft
- Hat nicht geklappt: … (Pflicht; „nichts“ nur, wenn wahr)
- Kosten: API-$ und OpenAlex-Credits (nur wenn angefallen)
- Nächster Vorschlag: … (keine Erlaubnis)
```

---

### 2026-11-09 07:30 UTC · Chat · Setup · Regeln, Fortsetzungscheck v0.3, OpenAlex-Test am Prüfset
- Gebaut/geändert: `CLAUDE.md` nach dem Vorbild der früheren Projekte (Arbeitsbereich, Freigaben, Git, Ausfallsicherheit), `.claude/settings.json` (technische Sperren), `scripts/openalex_check.py` v0.3 mit drei Signalen, `scripts/openalex_eingabe.py`, `auftraege/A01`, `A02`.
- Getestet: OpenAlex-Check auf 31 guten und Grenzfällen (`pruefset/openalex_test_2026-11-09.md`); Luftbilder als weitergeführt erkannt, dapE erst mit weltweiter Suche.
- Beobachtet: Filterabfrage kostet 1 Credit, Suche 10; Projektarbeiten über Förderkennzeichen für 6 von 31 Fällen gefunden.
- Hat nicht geklappt: Wiederbelebungs-Signal mit Titelwörtern zu grob; braucht Haikus Fachbegriffe. CORDIS-Nummern liefern keine Projektarbeiten.
- Kosten: 0 $; rund 1.040 OpenAlex-Credits.

### 2026-11-09 · Chat · Zweite Probe, Frühfilter, neue Quellen, Katalog
- Gebaut: Frühfilter (`scripts/early.py`), vier neue Pools (`scripts/newpools.py`, 8.836 Einträge), Fähigkeiten-Katalog (`docs/03_faehigkeiten_katalog.md`), Prüfset.
- Beobachtet: 83 Zufallseinträge bewertet, 3 gut, 5 Grenzfall. Frühfilter erkennen 52 von 75 ungeeigneten, treffen keinen guten. Benanntes technisches Hindernis: 27 % gute mit, 3 % ohne.
- Hat nicht geklappt: Text-Vektoren sortieren schwächer (AUC 0,53 bis 0,61) als eine einfache Regel (0,71). Positive Projekte ohne offenen Schritt: 0 von 28 brauchbar.

### 2026-11-08 · Chat · Quellenkarte und erste Probe
- Beobachtet: Bester Einstieg ist CEP (Tschechien), Abbruch und Begründung in einer Datei. Probe mit 39 Einträgen: 5 prüfenswert, alle aus CEP.
- Hat nicht geklappt: GEPRIS und NRAT nur von Hand lesbar; Russland, China, Kasachstan gestrichen.
