# A07: Gezielte Suche nach dem Muster aus Fables freier Suche

Von Nick, 2026-11-11 (wörtlich übernommen).

Zuerst: Haltepunkte gelten immer. ‚Keine Rückfragen‘ galt nur für jene eine Nacht. Halte das in CLAUDE.md fest.

Freigaben (in ENTSCHEIDUNGEN.md eintragen): 2026-11-11-A07a Sonnet höchstens 3 $, 2026-11-11-A07b Fable höchstens 6 $.

Ziel: gezielte Suche nach dem Muster aus Fables freier Suche: ‚Messdaten oder Prototyp vorhanden, Modell, Auswertung oder Optimierung fehlt‘.

Sonnet-Prompt v0.3:
- K2 gilt als erfüllt bei einem Abbruchgrund außerhalb der Idee ODER einem ausdrücklich offenen Schritt mit Zitat aus dem Ausgangstext.
- Die Pflichtkriterien gelten hart: Wer bei K1, K2, K11 oder K12 null Punkte hat, kommt nicht in die Rangliste. Er bleibt aber in der Datei.
- Neues Merkmal M ‚Messdaten oder Prototyp vorhanden, Modell, Auswertung oder Optimierung fehlt‘ (ja, teilweise, nein, mit Zitat): ja +4, teilweise +2.
- Abzug: fertiges Produkt, laufende Ausgründung, Kern von anderen gelöst.

Vorauswahl, kostenlos: Aus den vorhandenen Haiku-Antworten von Häppchen 1 die Einträge wählen mit:
- Hindernis-Muster H1, H2, H3, H5 oder H6,
- vorhandenem Teilerfolg,
- hindernis_quelle ‚ergebnis‘,
- Art des ersten Schritts software, simulation, datenanalyse oder prototyp_klein.
- Proof of Concept nur mit Hindernis-Zitat aus dem Ergebnistext. Zählen je Pool.

OpenAlex: Für tschechische Projekte englische Titel und Fachbegriffe aus Haiku verwenden. 0 Treffer als ‚Abfrage fehlgeschlagen‘ markieren, nicht als ‚nicht weitergeführt‘.

Sonnet v0.3 am Prüfset (aus A07a): Testregel ist, dass mindestens 12 von 15 guten Fällen die Schwelle erreichen, Pflichtkriterien inklusive. Sonst Haltepunkt.

Sonnet v0.3 auf die Vorauswahl (Rest von A07a), dann OpenAlex im schnellen Modus für die oberen 40.

Fable (A07b) auf die oberen 8.
- Je Kandidat eine klare Antwort ‚weiterverfolgen: ja oder nein‘.
- Dazu der konkrete erste Schritt mit Kosten in Euro und wer dafür zahlen würde.
- Danach freie Suche über die oberen 40: Verbindungen und neue Ansätze.

Ergebnis, Haltepunkt:
- Rangliste der oberen 20, Karten für die von Fable geprüften, Kosten.
- Im Terminal eine Kurzfassung. Dazu je zwei Sätze zu 101069165, 822620 und den Funden zum Muster aus Fables freier Suche in A06: worum es geht, was fehlt.
- Tagebuch, commit, push.

## Haltepunkte (aus dem Text)

1. Sonnet v0.3 am Prüfset nicht bestanden (weniger als 12 von 15 guten an der Schwelle, Pflicht inklusive).
2. Ende: Rangliste, Karten, Kosten, Kurzfassung.
