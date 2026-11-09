# Bezahlte Läufe

Jedes Skript, das kostenpflichtige APIs aufruft (Claude, Gemini), liegt in diesem Ordner. `.claude/settings.json` lässt Claude Code diese Skripte nur nach Rückfrage starten.

Pflicht für jedes Skript hier:

1. Argument `--freigabe <Datum-Lauf>`; das Skript bricht ab, wenn diese Zeile nicht in `ENTSCHEIDUNGEN.md` unter „Budgetfreigaben“ steht.
2. Argument `--max-usd`; das Skript zählt die Kosten mit und hört vor der Grenze auf.
3. `--dry-run` zeigt Anzahl der Aufrufe, geschätzte Token und Kosten, ohne etwas zu senden.
4. Jede Antwort wird sofort als eine Zeile an eine JSONL-Datei unter `ergebnisse/` angehängt, auch Fehler. Ein Neustart macht dort weiter und mischt keine Läufe.
5. Lange Läufe mit `nohup` und Log unter `logs/`, damit ein Verbindungsabbruch am Tablet nichts zerstört.
