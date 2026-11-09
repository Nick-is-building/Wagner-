# Projekt Wagner

Wir suchen Forschung, die früher abgebrochen oder nicht weitergeführt wurde und deren Hindernis heute mit KI und günstiger Rechenleistung lösbar ist, und führen den besten Ansatz selbst fort.

- Anweisungen für Claude Code: [CLAUDE.md](CLAUDE.md)
- Stand und Verlauf: [TAGEBUCH.md](TAGEBUCH.md)
- Was ansteht: [OFFENE_PUNKTE.md](OFFENE_PUNKTE.md)
- Entscheidungen und Budget: [ENTSCHEIDUNGEN.md](ENTSCHEIDUNGEN.md)
- Aufträge an Claude Code: [auftraege/](auftraege/)
- Grundlagen: [docs/](docs/), Ablauf in [docs/04_pipeline.md](docs/04_pipeline.md)

## Schnellstart auf der VM

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
bash scripts/daten_laden.sh   # rund 1,5 GB Rohdaten nach data/roh
bash scripts/stufe1.sh        # Pools, Frühfilter, Texte, Prüfset-Eingabe
```

`.env` enthält die Schlüssel und kommt nie ins Repository. Vorlage: `.env.example`.

Die Online-Dokumente im Chat (Feldkarte, Suchregeln, Fähigkeiten-Katalog, Übergabe-Prompt) liegen hier als Kopie vom 9. November 2026 in `docs/`. Bei Widerspruch gilt die neuere Fassung; Änderungen trägt der Chat in beide ein.
