# Entscheidungen

Was Nick entschieden hat, neueste oben. Budgetfreigaben stehen hier, bevor ein bezahlter Lauf startet.

| Datum | Entscheidung | Folge |
|---|---|---|
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
