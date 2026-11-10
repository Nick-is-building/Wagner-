# Tagebuch

## Stand (höchstens sechs Zeilen, immer aktuell halten)

- Daten: auf der VM geladen (1,3 GB `data/roh`), Stufe 1 gelaufen: 17.421 Einträge, 46 Prüfset-Einträge; stimmt mit dem Chat überein (A01 erledigt).
- Prüfset: 51 Einträge (8 gut, 2 gut schon weitergeführt, 21 Grenzfall, 20 ungeeignet; FW01010098 in A04 auf Grenzfall). OpenAlex-Check v0.3 auf 31 Fällen.
- Prompts: Haiku v0.1 und v0.2 nicht bestanden. Punktzahl (A04) trennt nicht: S1 = S2 = 0 Punkte, alle 17.421 kämen durch. Bericht `pruefset/punktzahl_test_2026-11-10.md`.
- Nächster Schritt: A05 in einer neuen Sitzung (Auftrag kommt vom Planungs-Chat).
- Ausgegeben bisher: rund 0,23 $ API (A02 0,13 $, A03 0,10 $).

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

### 2026-11-10 06:10 UTC · Code (Opus 5.5) · A05 Phase 0 · Auftrag und Regeln
- Gebaut/geändert: `auftraege/A05_luecken_schliessen.md` (Auftrag wörtlich), `CLAUDE.md` (Abschnitte Haltepunkte, Sitzungsbudget 5 $), `ENTSCHEIDUNGEN.md` (Rolle Planungs-Chat; Freigaben 2026-11-10-A05 und -A06).
- Getestet: nicht nötig (nur Text).
- Hat nicht geklappt: nichts.
- Nächster Schritt: A05 Phase 1 (CORDIS-Berichte, build_texts v2).

### 2026-11-10 05:40 UTC · Code (Opus 5.5) · A02 bis A04 · Sitzungsabschluss und Lehren
- Gebaut: Haiku-Skripte v0.1/v0.2, Weiter-Regel, Punktzahl, Kostenschätzung; Berichte `pruefset/haiku_test_2026-11-10.md`, `haiku_test_v02_2026-11-10.md`, `punktzahl_test_2026-11-10.md`. Alles committet; JSONL und Logs lokal.
- Beobachtet: Haiku v0.1 und v0.2 nicht bestanden; Punktzahl trennt nicht (S1 = S2 = 0, alle 17.421 kämen durch). 2,1 Zeichen je Token (geeicht an 146 Aufrufen), nicht 4.
- Lehre: Texte sind zu kurz abgeschnitten (500 bis 600 Zeichen je Feld, mitten im Satz, `scripts/build_texts.py`).
- Lehre: 17 von 20 Zufallseinträgen sind Anträge ohne Aussage über den Ausgang; dort findet kein Prompt ein Hindernis.
- Lehre: GA203/99/P017 (Mutterschaft) wurde als „formal“ statt „Personal“ eingestuft; Abbruchgründe brauchen Beispiele im Prompt.
- Lehre: Sonnet-Ausgabe muss kürzer werden; sie ist der größte Kostenhebel (alle Einträge: 177 bis 334 $ mit Cache je nach Länge).
- Hat nicht geklappt: Warte-Schleife aus A03 endete nie (`pgrep -f` fand sich selbst), am Ende beendet. Einmal A03-Ergebnisse überschrieben, aus Git wiederhergestellt.
- Kosten: gesamt rund 0,23 $ API (A02 0,13 $, A03 0,10 $, A04 0 $).

### 2026-11-10 05:20 UTC · Code (Opus 5.5) · A04 · Punktzahl, Schwellen, Stichprobe, Sonnet-Kosten
- Gebaut/geändert: `pruefset/pruefset.csv` (FW01010098 → Grenzfall, Grund in der Zeile), `scripts/weiter_regel.py` (Zitat aus beliebigem Feld), `scripts/punktzahl.py`, `scripts/sonnet_kosten.py`; Berichte `pruefset/punktzahl_test_2026-11-10.md`, `pruefset/stichprobe_v02_bewertung.md`.
- Getestet: Skripte laufen auf den vorhandenen Antworten; Regeländerung an zwei Hand-Beispielen.
- Beobachtet: S1 = S2 = 0 (v0.2) bzw. 1 (v0.1) → 100 von 100 Zufallseinträgen drin. Stichprobe (1 Prüfer): unter 10 Ausgesiebten 0 B, 3 G; unter 10 Durchgekommenen 4 C; Punktzahl trennt nicht besser als die v0.2-Regel. Eichung 2,10 Zeichen je Token; Sonnet auf alle 17.421 rund 250 $ mit Cache (1.000 Token Ausgabe), Prüfset rund 1 $.
- Hat nicht geklappt: `haiku_v02_auswertung.py` hat beim ersten Lauf die A03-Stichprobe und -Tabellen überschrieben; aus Git wiederhergestellt, Skript hat jetzt eine Sperre. 33 von 85 `offener_schritt_beleg` sind keine Zitate; die Zitat-Regel greift nach der Korrektur nie (alle 146 Antworten haben ein Zitat).
- Kosten: 0 $.
- Nächster Vorschlag: Haiku-Prompt nachbessern, dann Sonnet am Prüfset. Keine Erlaubnis.

### 2026-11-10 04:10 UTC · Code (Opus 5.5) · A03 mit Nachtrag · Haiku v0.2, Prüfset und 100 Zufallseinträge
- Gebaut/geändert: `prompts/haiku_extraktion.md` v0.2, `scripts/weiter_regel.py` (mit RIV-Nachtrag), `scripts/bezahlt/haiku_v02.py`, `scripts/zufall_eingabe.py`, `scripts/haiku_v02_auswertung.py`, `scripts/haiku_v02_varianten.py`; `zitat_check.py` mit optionalem Ausgabepfad. Bericht `pruefset/haiku_test_v02_2026-11-10.md`, Stichprobe `ergebnisse/haiku_v02_stichprobe.md`.
- Getestet: Trockenläufe, falsche Freigabe bricht ab, Regel an 8 Hand-Beispielen. Echte Läufe: `nohup … haiku_v02.py --test A/B` (Log `logs/haiku_v02.log`), danach 11 RIV (`logs/haiku_v02_riv.log`); 146 Antworten, 0 Fehler.
- Beobachtet: Prüfset gut 7/9, Grenzfall 13/20, ungeeignet 9/15. Zufall 52/100 weiter (SBIR 40/54, RIV 0/14). RIV Code O: 0 von 11 weiter, N0000005 nicht dabei; Hochrechnung rund 0 von 744 (95-%-Bereich 0 bis 223).
- Hat nicht geklappt: Test A nicht bestanden, auch in keiner Regel-Variante. GA106/09/0814 (gut) fällt nur, weil mein Skript „unklar“ ohne Zitat im Feld `hindernis` als „nein“ zählt. Zitat-Befunde (14) nicht von Hand geprüft.
- Kosten: 0,0957 $ API (Obergrenze 0,50 $); 0 OpenAlex-Credits.
- Nächster Vorschlag: Planungs-Chat: Kern-Bedingung und Zitat-Durchsetzung prüfen, Stichprobe bewerten. Keine Erlaubnis.

### 2026-11-10 02:50 UTC · Code (Opus 5.5) · A02 · Auswertung Haiku-Prüfset (Schritt 4)
- Gebaut/geändert: `scripts/haiku_auswertung.py`, Bericht `pruefset/haiku_test_2026-11-10.md`, Tabelle `ergebnisse/haiku_auswertung.tsv`. Prompt unverändert.
- Getestet: Skript läuft auf den 92 Antworten; Zahlen von Hand gegen die Tabelle geprüft.
- Beobachtet: weiter kommen gut 8 von 9, „gut (schon weitergeführt)“ 0 von 2, Grenzfall 19 von 20 (95 %), ungeeignet 12 von 15. Durchgefallen: GA203/99/P017 (Abbruch wegen Mutterschaft, nicht technisch), IAA400550614, P24116, RIV …N0000005.
- Hat nicht geklappt: Testregel nicht bestanden (ein guter Fall fehlt). Trennschärfe gering: 8 ungeeignete kommen nur über „unklar“ weiter. Die 5 Zitat-Befunde nicht von Hand geprüft.
- Kosten: 0 $.
- Nächster Vorschlag: Planungs-Chat prüft die sechs Vorschläge im Bericht (u. a. „Rechenanteil hoch“ als Weiter-Regel: gut 9/9, +1 ungeeignet). Keine Erlaubnis.

### 2026-11-10 01:30 UTC · Code (Sonnet 5.5) · A02 · Haiku-Lauf am Prüfset (Schritte 2 und 3)
- Gebaut/geändert: `scripts/bezahlt/haiku_extraktion.py` (Denken aus, `max_tokens` 2000, erstes JSON-Objekt lesen). Ausgaben (lokal): `ergebnisse/haiku_pruefset.jsonl` (alle Zeilen inkl. Fehler), `haiku_pruefset_ok.jsonl` (92 gute), `zitat_check.jsonl`. Logs `logs/haiku_pruefset*.log`. Prompt unverändert.
- Getestet: Echter Lauf, 46 Einträge × 2 Durchläufe = 92 Antworten, alle lesbar. `zitat_check.py`: 87 mit allen Zitaten belegt, 5 zum Nachprüfen.
- Beobachtet: Rund 0,13 $ gesamt (Datei: 0,1288 $, dazu zwei Testaufrufe ohne Protokoll, rund 0,002 $); Schätzung war 0,03 $. Antworten sind rund 1.000 Token lang, nicht 400.
- Hat nicht geklappt: Erster Versuch: alle 92 Antworten leer oder abgeschnitten (rund 0,07 $), weil das Modell standardmäßig „denkt“ und die 1.200 Token verbrauchte. Danach 4 Antworten mit Text hinter dem JSON, Parser angepasst, wiederholt. Fehlerzeilen bleiben in der Datei. `zitat_check.py` schreibt je ID keine Durchlaufnummer (zwei Zeilen je ID, in Reihenfolge der Datei).
- Kosten: rund 0,13 $ API (Obergrenze 0,50 $); 0 OpenAlex-Credits.
- Nächster Vorschlag: Auswertung (A02 Schritt 4) mit Opus; noch nicht gemacht.

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
