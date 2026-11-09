# A01: Umgebung, Daten laden, Stufe 1, Fortsetzungscheck am Prüfset

Erteilt von Nick, 9. November 2026. Kosten: 0 $ API; rund 1.400 OpenAlex-Credits. Modell: Sonnet reicht.

## Ziel

Die VM hat dieselben Daten und Zwischenstände wie der Planungs-Chat, und die Zahlen stimmen überein.

## Schritte

1. Umgebung: `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`. Prüfen, ob `OPENALEX_API_KEY` in `.env` gesetzt ist (nur ob, nicht den Wert ausgeben).
2. Daten laden: `nohup bash scripts/daten_laden.sh > logs/daten_laden.log 2>&1 &`. Dauer einige Minuten, rund 1,5 GB. Danach `du -sh data/roh` und das Log-Ende prüfen.
3. Stufe 1: `bash scripts/stufe1.sh > logs/stufe1.log 2>&1`.
4. Zahlen vergleichen mit `docs/04_pipeline.md`, Abschnitt „Pools“: insbesondere 17.421 Einträge nach `build_texts.py` und 46 Prüfset-Einträge in `ergebnisse/pruefset_eingabe.jsonl` (5 fehlen gewollt, weil harte Frühfilter sie entfernen). Neuere Daten können leicht abweichen (CEP und SBIR werden laufend ergänzt). Abweichungen über 5 % melden, nicht selbst „reparieren“.
5. Fortsetzungscheck am Prüfset:
   `python3 scripts/openalex_eingabe.py pruefset/pruefset.csv ergebnisse/openalex_eingabe.csv --nur gut,grenzfall`
   `python3 scripts/openalex_check.py --csv ergebnisse/openalex_eingabe.csv --out ergebnisse/openalex_check.jsonl --modus voll`
   Erwartung: 31 Zeilen; P24116 und IAA400550614 beide „vermutlich weitergeführt“ (Nachtest im Chat: Treffer von Argonne 2024 und Loyola Chicago 2018 bei den dapE-Hemmstoffen). Ergebnis mit `pruefset/openalex_test_2026-11-09.md` vergleichen.
6. Tagebuch-Eintrag, „Stand“ aktualisieren, commit und push.

## Nicht Teil des Auftrags

Keine bezahlten Aufrufe, keine Änderung an Filtern, Prompts oder Prüfset.
