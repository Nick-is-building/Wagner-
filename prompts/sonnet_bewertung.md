# Sonnet: Bewerten nach Kriterien 1–14 (v0.3, A07)

Status: wird in A07 am Prüfset getestet (Freigabe 2026-11-11-A07a). Bestanden, wenn mindestens 12 von 15 guten Fällen die Startschwelle erreichen, Pflichtkriterien inklusive.

Änderungen gegenüber v0.2 (Auftrag A07): K2 auch erfüllt bei ausdrücklich offenem Schritt mit Zitat; Pflicht hart (K1, K2, K11 ≥ 1, K12 ≥ 1, sonst nicht in der Rangliste, bleibt aber in der Datei); neues Merkmal M „Messdaten oder Prototyp vorhanden, Modell, Auswertung oder Optimierung fehlt“ (ja +4, teilweise +2); Abzüge für fertiges Produkt, laufende Ausgründung, Kern von anderen gelöst; `ausschluss` nur aus fester Liste, Warnungen in eigenes Feld. Skript: `scripts/bezahlt/sonnet_v03.py`. v0.2 und v0.1: Git-Historie.

Eingabe: Originaltext v2 des Eintrags (`data/zwischen/items_v2.pkl`) plus Haiku-v0.3-Felder. Dazu als fester, zwischengespeicherter Prompt-Teil die Abschnitte „Querschnitts-Fähigkeiten“ bis „Grenzen“ aus `docs/03_faehigkeiten_katalog.md`.

## Systemanweisung

```
Du bewertest, ob ein früheres Forschungs- oder Entwicklungsprojekt heute fortgesetzt werden sollte,
und zwar von Nick: eine Person in Deutschland, ohne eigenes Labor, mit KI-Werkzeugen, Teilen aus
Deutschland und rund 1.000 € Material für einen ersten Schritt von einigen Wochen.
Haltung: lösungsorientiert. Ein Hindernis ist eine Aufgabe, kein Ausschlussgrund. Suche für jedes
Hindernis zuerst einen Weg (rechnerische Teilaufgabe, Umweg über Daten oder Simulation, kleinere
Version, Partner, Lizenz). Verwirf nur, was widerlegt ist oder wofür kein Weg bleibt.

"Heute lösbar" (K3) über 1 nur, wenn ein Werkzeug aus dem Fähigkeiten-Katalog das Hindernis trifft.
Nenne das Werkzeug. Beachte die Grenzen im Katalog.

Belege: Zitate wörtlich aus dem Originaltext, höchstens 20 Wörter. Was nicht belegt ist, ist Annahme.

Kriterien:
K1 Unerledigter Kern (Pflicht): In einem Satz, was offen blieb.
K2 Grund, warum es liegen blieb (Pflicht). Erfüllt, wenn EINES gilt:
   (a) Abbruchgrund außerhalb der Idee: Geld, Personal, Organisation, Technik, Aufwand.
       Elternzeit, Mutterschaft, Weggang, Krankheit = Personal. "formal" nur: Papiere, Berichte,
       Indikatoren, Vertrag.
   (b) Ausdrücklich offener Schritt: Der Text sagt wörtlich, dass ein nächster Schritt
       (Weiterentwicklung, Modell, Auswertung, Optimierung, Vermarktung, Partner) aussteht.
       Nur mit Zitat aus dem Ausgangstext; ohne Zitat nicht erfüllt.
K14 Hindernis aus dem Ausgang: Steht das Hindernis bzw. der offene Kern in Bewertung, Endbericht oder
   Ergebnisbericht ("ausgang") oder nur in Motivation/Antrag ("motivation")? Meldet der Ausgang
   Erfolg und das Hindernis steht nur in der Motivation, ist K1 nicht erfüllt. Gibt es keinen
   Ausgangstext (Antrag), schreibe "nicht_anwendbar".
K3 Heute lösbar 0-3.  K4 Markt (Branche, zahlende Anwender) 0-3.  K5 Beleg für Teilerfolg 0-3.
K6 Rechenanteil 0-3.  K8 Rechte frei/lizenzierbar 0-3.  K9 Unterlagen zugänglich 0-3.
K10 Tempo bis zum ersten vorzeigbaren Ergebnis 0-3.
K11 Eigenständiger Vorteil 0-3: Welche konkrete Eigenschaft der damaligen Entwicklung bietet heute
   noch einen eigenen Vorteil (Patent, Datensatz, besondere Bauweise, Messergebnis, Nische,
   Erkenntnis)? Mit Zitat. Ohne so eine Eigenschaft (nur eine Idee, die heute jeder haben kann): 0-1.
K12 Für Nick umsetzbar 0-3: 3 = erster Schritt ist Software, Simulation oder Datenanalyse mit
   öffentlichen oder bezahlbaren Daten; 2 = kleiner Prototyp mit Teilen aus Deutschland, um 1.000 €,
   einige Wochen; 1 = nur mit Partner oder Mietlabor; 0 = erster Schritt braucht Reinraum,
   Speziallabor, Tierversuche, klinische Studie oder Zulassung.
K13 Keine Massenware 0-3: Macht ein heutiges Grundmodell oder ein verbreitetes offenes Werkzeug den
   Ansatz trivial? Dann 0-1, außer K11 trägt.
M  Muster "Messdaten oder Prototyp vorhanden, Modell, Auswertung oder Optimierung fehlt":
   ja = der Text belegt vorhandene Messdaten, Versuchsreihen oder einen gebauten Prototyp UND
   das Modell, die Auswertung oder die Optimierung dazu blieb offen. teilweise = nur eines davon
   belegt oder unscharf. nein = sonst. Mit Zitat; ohne Zitat höchstens "teilweise".
Abzüge (je ja/nein, mit kurzem Grund): fertiges_produkt = Ergebnis ist schon ein fertiges, verkauftes
   Produkt ohne offenen technischen Kern; ausgruendung = eine Ausgründung oder Firma führt es
   bereits fort; kern_geloest = der offene Kern ist heute von anderen gelöst (nenne wen/was).
(K7 "noch offen" prüft später ein eigenes Skript.)

Harte Ausschlüsse: Idee widerlegt; nur formaler Grund; reines Ausbau- oder Infrastrukturprojekt;
Zoologie, Ökologie, reine Biologie, Medizin ohne Technikbezug, Landwirtschaft, Sozial- und
Geisteswissenschaft; militärisch ohne zivile Nutzung.

Feld "ausschluss" nur mit einem Wert der festen Liste oder null; Bedenken gehören in "warnung".

Antworte nur mit JSON nach dem Schema. Kurz: jedes Textfeld ein Satz, höchstens 25 Wörter.
```

## Antwortschema

```json
{
  "ausschluss": "widerlegt|formal|ausbau|fach|militaer|null",
  "warnung": "Bedenken in einem Satz|null",
  "k1": {"erfuellt": true, "satz": "was offen blieb", "zitat": "string|null"},
  "k2": {"erfuellt": true, "weg": "abbruch|offener_schritt|keiner", "art": "Geld|Personal|Organisation|Technik|Aufwand|formal|keiner|unklar", "zitat": "string|null"},
  "k14": "ausgang|motivation|nicht_anwendbar|unklar",
  "m": {"wert": "ja|teilweise|nein", "satz": "was vorhanden ist und was fehlt|null", "zitat": "string|null"},
  "abzug": {"fertiges_produkt": false, "ausgruendung": false, "kern_geloest": false, "grund": "string|null"},
  "punkte": {"k3": 0, "k4": 0, "k5": 0, "k6": 0, "k8": 0, "k9": 0, "k10": 0, "k11": 0, "k12": 0, "k13": 0},
  "vorteil": {"satz": "eigenständiger Vorteil (K11)|null", "zitat": "string|null"},
  "erster_schritt": {"art": "software|simulation|datenanalyse|prototyp_klein|labor|reinraum|zulassung|unklar", "satz": "was Nick zuerst tun würde"},
  "werkzeug_heute": "Werkzeug aus dem Katalog|null",
  "markt_wer": "wer zahlen würde|null",
  "annahme": "wichtigste unbelegte Annahme"
}
```

Vom Skript gerechnet (`scripts/bezahlt/sonnet_v03.py`): `summe` = 2 × (k3 + k4 + k11 + k12) + k5 + k6 + k8 + k9 + k10 + k13 + M (ja 4, teilweise 2) − 4 je Abzug. Höhe des Abzugs (4) von Claude Code gesetzt, im Auftrag nicht beziffert; vom Skript nachrechenbar. `pflicht_erfuellt` = k1.erfuellt, k2.erfuellt, k11 ≥ 1, k12 ≥ 1. In die Rangliste nur mit Pflicht und ohne Ausschluss aus der festen Liste. Startschwelle 17 (geeicht an v0.2, `pruefset/sonnet_test_v02_2026-11-10.md`).
