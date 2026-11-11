# Tagebuch

## Stand (höchstens sechs Zeilen, immer aktuell halten)

- A07 (Muster-Suche) am End-Haltepunkt: Vorauswahl 103 → Sonnet v0.3 → Rangliste 98 (mit Teilerfolg) → OpenAlex obere 40 → Fable 7 geprüft, freie Suche über 40.
- Ergebnis: `kandidaten/RANGLISTE_A07.md` (obere 20), 4 neue und 3 ergänzte Karten, `kandidaten/beobachtungen_A07.md`. Fable: 4 × weiterverfolgen ja (P27738, P32954, 101112727, 673155), 3 × nein.
- Bekannte Schwächen: Sonnet v0.3 am Prüfset nicht bestanden (5/15 gute mit Pflicht); Pflicht nur Markierung (Nick). K2 scheitert vor allem an Antragstexten ohne Ausgang (`pruefset/sonnet_test_v03_2026-11-11.md`).
- Läuft: nichts. Wartet auf Nick.
- Ausgegeben bisher: rund 27,6 $ API (A02 0,13 $, A03 0,10 $, A06 18,47 $, A07 8,78 $).

## Regeln

- Ein Eintrag pro Arbeitseinheit, höchstens zehn Zeilen, neueste oben.
- Nur, was ein Nachfolger wissen muss. Keine Rohausgaben, keine Projektbeschreibungen (die stehen in `kandidaten/`).
- Zahlen nur mit Herkunft (Datei oder Befehl).
- Alte Einträge nicht umschreiben; Korrekturen als neuer Eintrag mit Verweis.
- Ab 300 Zeilen wandern Einträge, die älter als einen Monat sind, nach `tagebuch_archiv/JJJJ-MM.md`; hier bleibt je Monat eine Zeile mit Verweis.

Format:

```
### 2026-11-11 02:50 UTC · Code (Opus 5.5) · A07 · Vorauswahl bis Fable (End-Haltepunkt)
- Gebaut: `scripts/a07_rangliste.py`, `scripts/a07_ergebnis.py`, `scripts/bezahlt/fable_a07.py`; `scripts/openalex_check.py` sucht bei 0 Treffern mit 4 Titelwörtern, dann mit Haikus `anwendung`, sonst Markierung „Abfrage fehlgeschlagen“.
- Gelaufen: Sonnet v0.3 auf 103 (`logs/sonnet_v03_vorauswahl.log`, 0 Fehler); OpenAlex schnell 40 (`logs/a07_openalex.log`, rund 450 Credits, 0 fehlgeschlagen); Fable tiefe 7 (`logs/fable_a07_tiefe.log`), frei 1 (`logs/fable_a07_frei.log`).
- Beobachtet: 98 von 103 mit K5 ≥ 1; obere 40 Summe 32 bis 23, M ja 8, teilweise 24, ohne Pflicht-Null 35 (`ergebnisse/a07_rangliste.tsv`). Fable hält Sonnets Nullen/Nicht-Nullen meist für richtig; bei GA15-15467S hält es K11 > 0 für falsch.
- Hat nicht geklappt: Fable nur 7 statt 8 (Freigabe 6 $ reichte bei 0,61 $ je Prüfung nicht). Sonnet hielt bei 91/103 am Kostenwächter an (15 parallel); Rest einzeln nachgeholt. Haiku v0.3 hat keine englischen Fachbegriffe; `anwendung` ist oft deutsch oder tschechisch. Erste Schritte und Zahler sind fast überall Fables eigene Schätzung („Nick selbst“, Förderprogramm unbelegt).
- Kosten: A07a 3,294 $ (von 3,50 $), A07b 5,483 $ (von 6 $). Sitzung Claude Code grob 4 $.
- Nächster Vorschlag: Daten von P27738 (ESRF) und 673155 prüfen; Sonnet-K2 für Antragstexte klären (keine Erlaubnis).

### 2026-11-11 02:10 UTC · Code (Opus 5.5) · A07 · Sonnet v0.3 am Prüfset (Haltepunkt)
- Gebaut: `auftraege/A07_muster.md`; Haltepunkt-Regel in `CLAUDE.md`; Freigaben A07a/b; `prompts/sonnet_bewertung.md` v0.3; `scripts/bezahlt/sonnet_v03.py`; `scripts/a07_vorauswahl.py`.
- Getestet: Rechnung von `sonnet_v03.rechne` an einem Handbeispiel (13, stimmt); Prüfset-Lauf 101 Aufrufe, 0 Fehler, 43 s (`logs/sonnet_v03_pruefset.log`).
- Beobachtet: Vorauswahl poc 28/856, sme2 33/1.168, cep_fail 17/398, fwf_obst 25/318. Prüfset: gute mit Pflicht ≥ 17 nur 5/15, ohne Pflicht 10/15; Pflicht scheitert an K2 (5), K11 = 0 (5), K12 = 0 (3).
- Hat nicht geklappt: Testregel klar verfehlt. „Teilerfolg“ hat kein Haiku-Feld; soll nach Sonnet über K5 ≥ 1 geprüft werden. Abzugshöhe (4 je Abzug) im Auftrag nicht beziffert, von mir gesetzt. Zwei Sitzungsabbrüche: VM lief durch (uptime 10 h), es brach die SSH-Verbindung ab; Claude Code lief nicht in tmux.
- Kosten: A07a 1,557 $. Sitzung Claude Code grob 2 $.
- Nächster Vorschlag: Wege 1–4 im Bericht (keine Erlaubnis).

### JJJJ-MM-TT HH:MM UTC · Chat | Code (Modell) · Auftrag · Kurztitel
- Gebaut/geändert: Pfade
- Getestet: Befehl und Ergebnis (oder „nicht getestet“)
- Beobachtet: Zahlen mit Herkunft
- Hat nicht geklappt: … (Pflicht; „nichts“ nur, wenn wahr)
- Kosten: API-$ und OpenAlex-Credits (nur wenn angefallen)
- Nächster Vorschlag: … (keine Erlaubnis)
```

---

### 2026-11-11 01:30 UTC · Code (Opus 5.5) · A06 Phase 4–8 · Häppchen 1 bis Fable (Haltepunkt)
- Gebaut: `scripts/bezahlt/sonnet_v02.py`, `fable_a06.py`; `scripts/a06_obere100.py`, `a06_ergebnis.py`; Rangfolge nach Nicks Vorgabe in `auswahl_v03.py`.
- Getestet/gelaufen: Haiku 2.738 (237 s, `logs/haiku_v03_haeppchen1.log`); Sonnet Prüfset 101 und Häppchen 429 (139 s, `logs/sonnet_v02_haeppchen1.log`); OpenAlex schnell 100 (`logs/a06_openalex.log`); Fable frei 1 (241 s) und Tiefe 16 (`logs/fable_a06_tiefe*.log`).
- Beobachtet: weiter je Pool poc 720/854, sme2 985/1.168 (+4 Anträge im oberen Viertel), cep_fail 267/398, fwf_obst 137/318 (`ergebnisse/auswahl_v03_haeppchen1.tsv`). Sonnet kam bis Rang 429 von 2.109. Obere 100: Summe 32 bis 24, Pflicht 35 von 100. Fable-Urteile siehe `kandidaten/RANGLISTE.md`; Fable wich nie auf ältere Modelle aus.
- Hat nicht geklappt: Sonnet-Testregel mit Pflicht nicht bestanden (3/15 gute); weitergemacht mit Summe (Nicks Vorgabe „keine Rückfragen“). 14 der oberen 30 ohne Fable-Prüfung (Budget). Haiku lehnte 2 Einträge ab. Unter den oberen 30 Fachfremdes (101138301 Prostata, 101069237 zellfrei).
- Vermutet: Sonnet-Summe belohnt fertige Software (Fable: 36 der oberen 100 ohne offenen Kern). OpenAlex 0 Treffer bei 7 Fällen vermutlich Abfragefehler (Fable).
- Kosten: A06b 1,07 $, A06c 1,31 $, A06d 4,59 $, A06e 11,43 $; OpenAlex rund 1.240 Credits. Sitzung Claude Code grob 7 $.
- Nächster Vorschlag: Sonnet-Pflicht (K2 für Klasse B, Feld ausschluss) reparieren, dann Häppchen 2 nach `kandidaten/beobachtungen.md` (keine Erlaubnis).

### 2026-11-10 09:30 UTC · Code (Opus 5.5) · A06 Phase 0–3 · Kriterien, Haiku v0.3, Test (Haltepunkt)
- Gebaut: `auftraege/A06_haeppchen1.md`; Prüfset 106; K11–K14 in `docs/04_pipeline.md`; `prompts/sonnet_bewertung.md` v0.2, `prompts/haiku_extraktion.md` v0.3; `scripts/bezahlt/api_lauf.py` (parallel, fortsetzbar), `haiku_v03.py`; `scripts/a06_eingabe.py`, `auswahl_v03.py`, `kosten.py`.
- Getestet: Haiku v0.3 auf 101 Prüfset- und 100 Zufallseinträgen, 0 Fehler, je rund 10 s.
- Beobachtet: nicht bestanden. Ergebnis-Texte gut 12/12, Grenzfall 27/34; Antrags-Texte gut 1/3 im oberen Viertel. Bericht `pruefset/haiku_test_v03_2026-11-10.md`.
- Hat nicht geklappt: Testregel verfehlt (Grenzfälle 65 % gesamt). Beim Zusammenführen des Prüfsets brach das Schreiben ab (Zeile FW01010098 mit Komma ohne Anführungszeichen); Datei aus Git wiederhergestellt, dann sicher neu geschrieben. Erster Haiku-Start brach vor dem Senden ab (Programmfehler, nichts gesendet).
- Vermutet: Fable-Tiefenprüfung kostet grob 0,75 $ je Kandidat (`scripts/kosten.py`); 30 Kandidaten passen nicht in 8 $. Nicht gemessen.
- Kosten: 0,067 $ API (A06a). Sitzung Claude Code grob 3 $.
- Nächster Schritt: Haltepunkt, Entscheidung von Nick.

### 2026-11-10 07:40 UTC · Code (Opus 5.5) · A05 Phase 2 · Prüfset-Vorschläge mit Doppelbewertung (Haltepunkt 1)
- Gebaut: `scripts/pruefset_vorschlaege.py` (Runde 1: 39 aus allen Pools, Signal + Zufall, Startwert 20261110; Runde 2: 16 gezielt), `scripts/a05_pruefset_neu.py`; Dateien `pruefset/a05_vorschlaege*.md/.jsonl`, `a05_erstbewertung.md`, `a05_zweitbewertung*.md` (Subagent, Opus, ohne meine Begründung), Ergebnis `pruefset/a05_neue_eintraege.csv`. `pruefset.csv` noch NICHT geändert (wartet auf Okay).
- Beobachtet: 55 Vorschläge → 7 gut (beide einig), 25 Grenzfall (davon 8 uneins), 23 ungeeignet. Prüfset danach 15 gut / 46 Grenzfall / 43 ungeeignet; Ziel 20 gut nicht erreicht. Gute aus Antrags- und CORDIS-Pools jetzt 6 (SBIR 3, PoC 2, SME-1 1).
- Rückblick: OpenAlex „voll“ auf 6 alte Fälle (`ergebnisse/a05_rueckblick_openalex.jsonl`, 120 Credits); nur 0810523 plausibel (Deep-Learning-Arbeit 2019), nicht geprüft. 5 Fälle nicht gefunden.
- Hat nicht geklappt: Meine Erstbewertung Runde 2 erst nach dem Bericht des Zweitprüfers in die Datei geschrieben (Urteile vorher gefasst, aber nicht nachweisbar). Ausbeute an guten Fällen gering (7 von 55).
- Kosten: 0 $ API; 120 OpenAlex-Credits. Sitzung grob 4 $ (inkl. zwei Subagenten).
- Nächster Schritt: Haltepunkt 1, Okay von Nick.

### 2026-11-10 06:40 UTC · Code (Opus 5.5) · A05 Phase 1 · CORDIS-Berichte und Texte v2
- Gebaut/geändert: `scripts/cordis_berichte.py` (neu, Aufruf in `daten_laden.sh` und `stufe1.sh`), `scripts/build_texts.py` v2 → `data/zwischen/items_v2.pkl`; v1 heißt jetzt `scripts/build_texts_v1.py` (für alte Läufe, `items.pkl` unverändert).
- Getestet: beide Skripte gelaufen; gleiche 17.421 IDs wie v1; längster Text 4.002 Zeichen; zwei Texte von Hand angesehen.
- Beobachtet: CORDIS-Bericht vorhanden: sme1_noP2 3.078/3.097, sme2 1.158/1.168, poc 849/854 (Erwartung 650: H2020-PoC 650 + Horizon Europe 199). H2020-PoC-Berichte haben nur `summary`, die beschreibt aber den Ausgang; zählt als Ergebnis. Texttyp: 8.679 ergebnis, 8.742 antrag (sbir1 6.113, sbir2 2.540, gw 55, CORDIS ohne Bericht 34). Ø 2.265 Zeichen statt rund 1.100.
- Hat nicht geklappt: nichts. JSON-Zips gelöscht wie beauftragt; die 5.085 benötigten JSON liegen entpackt in `data/roh/cordis_berichte/json/` (74 MB).
- Kosten: 0 $ API. Sitzung bisher grob 1 $.
- Nächster Schritt: Phase 2 (Prüfset erweitern).

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
