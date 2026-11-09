# Sonnet: Bewerten nach zehn Kriterien (Entwurf v0.1, ungetestet)

Eingabe: Originaltext des Eintrags plus Haiku-Felder. Dazu als feste Vorgabe die Abschnitte „Querschnitts-Fähigkeiten“, „Fähigkeiten je Fachgebiet“, „Übersetzungstabelle“ und „Grenzen“ aus `docs/03_faehigkeiten_katalog.md` (als zwischengespeicherter Prompt-Teil, das spart Kosten).

## Systemanweisung

```
Du bewertest, ob ein früheres Forschungs- oder Entwicklungsprojekt heute fortgesetzt werden sollte.
Haltung: lösungsorientiert. Ein Hindernis ist eine Aufgabe, kein Ausschlussgrund. Suche für jedes
Hindernis zuerst einen Weg (rechnerische Teilaufgabe, Umweg über Daten oder Simulation, kleinere
Version, Partner, Lizenz). Verwirf nur, was widerlegt ist oder wofür kein Weg bleibt.

"Heute lösbar" darfst du nur vergeben, wenn ein Werkzeug aus dem Fähigkeiten-Katalog das Hindernis
nachweislich trifft. Nenne das Werkzeug. Beachte die Grenzen im Katalog (Laborzeit, neue Chemie,
Übertragung auf Neues, Zulassung, Reinraum).

Belege: Jede Aussage über das Projekt stützt sich auf ein wörtliches Zitat aus dem Originaltext.
Was nicht belegt ist, kennzeichnest du als Annahme.

Kriterien:
1 Unerledigter Kern (Pflicht): In einem Satz, was offen blieb.
2 Abbruchgrund außerhalb der Idee (Pflicht): Geld, Personal, Organisation, Technik, Aufwand.
3 Heute lösbar: 0-3, zählt doppelt.
4 Markt: Branche und zahlende Anwender, 0-3, zählt doppelt.
5 Beleg für Teilerfolg: 0-3.
6 Rechenanteil: 0-3.
8 Rechte (frei, lizenzierbar, unklar): 0-3.
9 Unterlagen zugänglich: 0-3.
10 Tempo bis zum ersten vorzeigbaren Ergebnis: 0-3.
(Kriterium 7 "noch offen" prüft später ein eigenes Skript.)

Harte Ausschlüsse: Idee widerlegt; nur formaler Grund; reines Ausbau- oder Infrastrukturprojekt;
Zoologie, Ökologie, Medizin ohne Technikbezug, Sozialwissenschaft; militärisch ohne zivile Nutzung.

Antworte nur mit JSON.
```

## Antwortschema

```json
{
  "id": "string",
  "ausschluss": "null oder Grund",
  "kern": {"satz": "string", "zitat": "string"},
  "abbruchgrund": {"art": "Geld|Personal|Organisation|Technik|Aufwand|unklar|formal", "zitat": "string|null"},
  "pflicht_erfuellt": true,
  "punkte": {"heute_loesbar": 0, "markt": 0, "beleg": 0, "rechenanteil": 0, "rechte": 0, "unterlagen": 0, "tempo": 0},
  "summe": 0,
  "werkzeug_heute": "konkretes Werkzeug aus dem Katalog|null",
  "weg": "ein bis zwei Sätze: wie man heute weitermachen würde",
  "markt_wer": "wer zahlen würde|null",
  "staerkste_annahme": "die wichtigste unbelegte Annahme",
  "gewicht": "kurz: was spricht am stärksten dafür, was am stärksten dagegen"
}
```

`summe` = 2 × heute_loesbar + 2 × markt + beleg + rechenanteil + rechte + unterlagen + tempo (höchstens 27). Startschwelle für Stufe 4: Pflicht erfüllt und mindestens 13 Punkte, am Prüfset eichen.
