# Entscheidungen

Was Nick entschieden hat, neueste oben. Budgetfreigaben stehen hier, bevor ein bezahlter Lauf startet.

| Datum | Entscheidung | Folge |
|---|---|---|
| 2026-11-10 | A06 Haltepunkt Phase 3: weiter mit Phase 4 wie gebaut (Option 1); durchgekommene Ergebnis-Texte vor Sonnet nach H1–H3, Rechenanteil, erster Schritt sortieren; Antrags-Regel erst für Häppchen 2 prüfen; Fable-Freigabe A06e auf 12 $, davon mindestens 1,50 $ für die freie Suche (Vorrang), Tiefenprüfung: 2 messen, dann so viele wie in den Rest passen, höchstens 3 Websuchen je Kandidat; keine weiteren Rückfragen bis Phase 8 | `scripts/auswahl_v03.py`, `OFFENE_PUNKTE.md` |
| 2026-11-10 | A06 erteilt: Kriterien K11–K14, Haiku v0.3, Häppchen 1 (poc, sme2, cep_fail, fwf_obst) mit Haiku, Sonnet, OpenAlex und Fable 5.2; Sitzungsbudget Claude Code für A06 10 $; ersetzt A05 ab Phase 3; Prüfset-Übernahme der 55 A05-Einträge | `auftraege/A06_haeppchen1.md` |
| 2026-11-10 | A05 erteilt: Claude Code übernimmt auch die Rolle des Planungs-Chats (planen, bauen, auswerten, bewerten); Haltepunkte und Freigaben bleiben; Prüfset-Erweiterung ausdrücklich beauftragt | `auftraege/A05_luecken_schliessen.md`, `CLAUDE.md` (Haltepunkte, Sitzungsbudget 5 $) |
| 2026-11-10 | A03-Nachtrag: RIV Code O nicht mehr ohne Prüfung weiter; offener Schritt = ja, dazu Rechenanteil mittel/hoch oder Hindernis ja/unklar | `scripts/weiter_regel.py` |
| 2026-11-10 | A03 freigegeben (Haiku-Prompt v0.2, Prüfset und 100 Zufallseinträge) | Lauf auf der VM durch Claude Code |
| 2026-11-09 | A02 freigegeben (Haiku am Prüfset) | Lauf auf der VM durch Claude Code |
| 2026-11-09 | Claude Code läuft auf der VM über die API | sparsam arbeiten; Sonnet für Routine, Opus nur für Bewertungslogik |
| 2026-11-09 | Eigenes privates Repository, Arbeitsordner „Projekt Wagner“; nur dort arbeiten | Arbeitsbereichs-Regeln in `CLAUDE.md`, Sperren in `.claude/settings.json` |
| 2026-11-09 | Kostenloser OpenAlex-Schlüssel liegt vor | nur in `.env` |
| 2026-11-08 | Kein Geld für Läufe, deren Nutzen nicht an einer kostenlosen oder sehr billigen Probe gezeigt wurde | Prüfset zuerst |
| 2026-11-08 | Keine Obergrenze für gute Kandidaten; Nick sucht nichts von Hand | vollständige maschinelle Vorsortierung |
| 2026-11-08 | Prüfung lösungsorientiert; mehr als drei Ergebnisse erwartet | Prüfhaltung |
| 2026-11-08 | Keine Zoologie, Ökologie und Ähnliches | Fachfilter |
| 2026-11-08 | Gewichtung Suchphase: Wissenschaft ×2, Business ×1,5; beim Ausbau umgekehrt | Bewertung |
| 2026-11-08 | Russland, China, Kasachstan gestrichen; GEPRIS und NRAT nur von Hand | Quellenliste |

## Budgetfreigaben

Ein bezahltes Skript startet nur, wenn seine Freigabe-ID hier steht.

| Freigabe-ID | Lauf | Geschätzt | Obergrenze | Freigegeben am | Tatsächlich |
|---|---|---|---|---|---|
| 2026-11-09-A02 | Haiku-Prompt v0.1 am Prüfset (A02) | rund 0,04 $ | 0,50 $ | 2026-11-09 | rund 0,13 $ (Lauf 2026-11-10) |
| 2026-11-10-A03 | Haiku-Prompt v0.2: Prüfset (Test A) und 100 Zufallseinträge (Test B) | rund 0,09 $ (Trockenlauf; ungünstigster Fall 0,16 $) | 0,50 $ | 2026-11-10 | 0,0957 $ (Läufe 2026-11-10, inkl. 11 RIV aus dem Nachtrag) |
| 2026-11-10-A05 | Haiku-Prompt v0.3: erweitertes Prüfset und 100 Zufallseinträge, Texte v2 (A05 Phase 4) | offen (Trockenlauf folgt) | 0,50 $ | 2026-11-10 | nicht genutzt, ersetzt durch A06a |
| 2026-11-10-A06 | Sonnet-Bewertung kompakt am Prüfset (A05 Phase 5; nur wenn Phase 4 besteht) | offen (Trockenlauf folgt) | 2,00 $ | 2026-11-10 | nicht genutzt, ersetzt durch A06c |
| 2026-11-10-A06a | Haiku-Test v0.3 am Prüfset und 100 Zufallseinträgen (A06 Phase 3) | rund 0,075 $ (Trockenlauf; ungünstigster Fall 0,12 $) | 0,50 $ | 2026-11-10 | 0,067 $ (Lauf 2026-11-10) |
| 2026-11-10-A06b | Haiku v0.3 auf Häppchen 1, rund 2.738 Einträge (A06 Phase 4) | rund 1,21 $ (Trockenlauf) | 2,00 $ | 2026-11-10 | 1,07 $ (2.738 Aufrufe, 2 Ablehnungen) |
| 2026-11-10-A06c | Sonnet am Prüfset (A06 Phase 5) | rund 1,41 $ (Trockenlauf) | 2,00 $ | 2026-11-10 | 1,31 $ (101 Aufrufe) |
| 2026-11-10-A06d | Sonnet auf die Auswahl aus Häppchen 1 (A06 Phase 5) | rund 0,015 $ je Eintrag | 5,00 $ | 2026-11-10 | 4,59 $ (429 von 2.109 Einträgen, Rang 1–429) |
| 2026-11-10-A06e | Fable 5.2 (claude-fable-5-2): Tiefenprüfung obere 30 und freie Suche obere 100, inkl. Websuche (A06 Phase 7) | offen | 12,00 $ (erhöht von 8,00 $ am 2026-11-10) | 2026-11-10 | 11,43 $ (freie Suche 2,52 $; 16 Tiefenprüfungen 8,91 $, je rund 0,55 $; kein Ausweichen auf ältere Modelle) |
