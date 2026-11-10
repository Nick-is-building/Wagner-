# Tagebuch

## Stand (höchstens sechs Zeilen, immer aktuell halten)

- Daten: auf der VM geladen (1,3 GB `data/roh`), Stufe 1 gelaufen: 17.421 Einträge, 46 Prüfset-Einträge; stimmt mit dem Chat überein (A01 erledigt).
- Prüfset: 51 Einträge (11 gut, 20 Grenzfall, 20 ungeeignet). OpenAlex-Check v0.3 (voll) auf 31 Fällen gelaufen.
- Prompts: Entwürfe v0.1 für Haiku, Sonnet, Opus; ungetestet.
- Nächster Auftrag: `auftraege/A02_pruefset_haiku.md` (freigegeben, Obergrenze 0,50 $): Skript und Trockenlauf, echter Lauf erst nach Nicks Ansicht der Kosten.
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

### 2026-11-10 00:40 UTC · Code (Sonnet 5.5) · A02 · Haiku-Skript und Trockenlauf
- Gebaut/geändert: `scripts/bezahlt/haiku_extraktion.py` (Freigabe-Prüfung, `--max-usd`, `--dry-run`, JSONL je Antwort, fortsetzbar). Prompt und Prüfset unverändert.
- Getestet: `--dry-run` und die zwei Abbrüche (falsche Freigabe, fehlende Argumente) laufen. Echter API-Aufruf: nicht getestet, nichts gesendet.
- Beobachtet: Trockenlauf: 92 Aufrufe, rund 108.800 Token Eingabe (Schätzung 3 Zeichen je Token), 36.800 Ausgabe, rund 0,029 $; ungünstigster Fall 0,066 $ (Grenze 0,50 $).
- Hat nicht geklappt: Token sind nur nach Zeichenzahl geschätzt, nicht gezählt. Ob `claude-haiku-5-5` und die Preise stimmen, zeigt erst der erste echte Aufruf.
- Kosten: 0 $.
- Nächster Vorschlag: Nick sieht den Trockenlauf; bei Ja echter Lauf, danach `zitat_check.py` und Auswertung (Schritt 4 gehört laut A02 zu Opus).

### 2026-11-10 00:20 UTC · Code (Sonnet 5.5) · A01 · Daten laden, Stufe 1, Fortsetzungscheck
- Gebaut/geändert: `.venv`, `data/roh` (1,3 GB, lokal), `ergebnisse/openalex_eingabe.csv`; Logs `logs/daten_laden.log`, `logs/stufe1.log`, `logs/openalex_check.log`. Keine Skripte geändert.
- Getestet: `scripts/stufe1.sh` Exit 0; 17.421 Einträge, 46 von 51 Prüfset-Einträgen in `ergebnisse/pruefset_eingabe.jsonl` (5 gewollt entfernt). Check: `openalex_check.py --modus voll`, 31 Zeilen in `ergebnisse/openalex_check.jsonl`.
- Beobachtet: P24116 und IAA400550614 beide „Thema vermutlich weitergeführt“ (wie erwartet). Insgesamt aber 9 von 31 Zeilen „vermutlich weitergeführt“ (Chat-Test: 2 von 28, ohne weltweite Suche); neu u. a. FV10342, FW01010098, GA106/09/0814, TA02020998, 10.55776/P16969, 181662. Die 3 RIV-Zeilen stehen nur im neuen Lauf, alle „kein Hinweis“.
- Hat nicht geklappt: `.env` ist für mich gesperrt, ob `OPENALEX_API_KEY` gesetzt ist, habe ich nicht geprüft (Lauf ging durch). Vermutet: weltweite Suche in v0.3 ist zu grob (Titelwörter), nicht geprüft; Entscheidung beim Planungs-Chat.
- Kosten: 0 $ API; rund 1.050 OpenAlex-Credits (Log: 8.838 auf 7.821 Rest).
- Nächster Vorschlag: A02 (Skript, Trockenlauf).

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
