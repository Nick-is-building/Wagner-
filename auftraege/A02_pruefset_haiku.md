# A02: Haiku-Prompt am Prüfset testen

Status: **freigegeben von Nick am 9. November 2026** (Freigabe-ID `2026-11-09-A02`, Obergrenze 0,50 $). Modell in Claude Code: Opus für Schritt 4 (Auswertung), sonst Sonnet.

## Ziel

Zeigen, ob `prompts/haiku_extraktion.md` v0.1 die Testregel besteht: alle 11 guten Fälle kommen weiter, mindestens 80 % der 20 Grenzfälle.

## Kostenschätzung

46 Einträge × 2 Durchläufe × rund 1.900 Token Eingabe und 400 Token Ausgabe mit Haiku 5.5 (0,10 $ / 0,50 $ je Million Token): rund 0,03 $. Mit Sicherheitsaufschlag Obergrenze `--max-usd 0.50`.

## Schritte

1. `scripts/bezahlt/haiku_extraktion.py` bauen nach den Regeln in `scripts/bezahlt/README.md` (Freigabe-Prüfung, Kostengrenze, Trockenlauf, JSONL je Antwort, fortsetzbar). Batch-API ist für 46 Einträge nicht nötig; normale Aufrufe sind hier einfacher.
2. `--dry-run` zeigen: Anzahl Aufrufe, Token, Kosten. Erst nach Freigabe echt starten.
3. `scripts/zitat_check.py` auf die Ausgabe anwenden.
4. Auswerten je Klasse: Wie viele kommen weiter (Ja oder unklar in einem der beiden Durchläufe)? Welche guten oder Grenzfälle fallen durch, mit Zitat und vermutetem Grund? Ergebnis als `pruefset/haiku_test_<datum>.md`.
5. Prompt nicht selbst ändern. Verbesserungsvorschläge in den Bericht; der Planungs-Chat entscheidet.
6. Tagebuch, commit, push.
