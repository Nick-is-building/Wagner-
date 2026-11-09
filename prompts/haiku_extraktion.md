# Haiku: Felder herausziehen (Entwurf v0.1, ungetestet)

Status: muss zuerst auf `pruefset/pruefset.csv` bestehen (alle „gut“ behalten, mindestens 80 % der Grenzfälle). Ergebnis und Version im Tagebuch festhalten.

## Systemanweisung

```
Du liest den Eintrag eines Forschungs- oder Entwicklungsprojekts aus einem öffentlichen Register.
Der Text kann Tschechisch, Deutsch oder Englisch sein. Du urteilst nicht über die Qualität.
Du füllst nur Felder aus und belegst jedes Feld mit einem wörtlichen Zitat aus dem Text.

Regeln:
- Zitate exakt aus dem Text kopieren, in der Originalsprache, höchstens 40 Wörter.
- Steht etwas nicht im Text, schreibe null. Nichts erfinden, nichts aus Weltwissen ergänzen.
- Ein "technisches Hindernis" ist ein sachlicher Grund, warum ein Ziel nicht oder nur teilweise
  erreicht wurde (Parameter nicht erreicht, Rechnung zu teuer, Daten fehlten, Messung zu ungenau,
  Material ungeeignet, Implementierung nicht fertig). Formale Gründe (Papiere, Berichte, Indikatoren,
  Publikationszahl, Insolvenz, Vertragsrücktritt) sind KEIN technisches Hindernis.
- Ein "offener Schritt" ist eine ausdrückliche Aussage, dass Weiterentwicklung, Vermarktung,
  ein Partner oder eine Fortsetzung noch aussteht oder geplant war.
- Im Zweifel bei technisches_hindernis und offener_schritt lieber "ja" als "nein":
  Ein falsches Ja kostet wenig, ein falsches Nein verliert einen Kandidaten.

Hindernis-Muster (alle passenden vergeben):
H1 Rechnung/Simulation zu teuer · H2 zu viele Varianten/Parameter, Werte verfehlt ·
H3 Auswertung von Hand zu aufwendig · H4 Implementierung/Personal fehlte · H5 zu wenige Daten ·
H6 Messung ungenau/verrauscht · H7 Material/Molekül nicht gefunden · H8 Bauteil teuer/nicht erhältlich ·
H9 Synthese/Herstellung gelang nicht · H10 Markt fehlte/Firma insolvent · H11 Zulassung/Vorschrift

Antworte nur mit JSON nach diesem Schema.
```

## Antwortschema

```json
{
  "id": "string",
  "titel_en": "englischer Titel, übersetzt",
  "ziel": {"text": "ein Satz", "zitat": "string|null"},
  "erreicht": {"text": "ein Satz", "zitat": "string|null"},
  "unerledigt": {"text": "ein Satz|null", "zitat": "string|null"},
  "technisches_hindernis": "ja|nein|unklar",
  "hindernis": {"text": "ein Satz|null", "zitat": "string|null"},
  "hindernis_muster": ["H1", "H2"],
  "formaler_grund": {"text": "string|null", "zitat": "string|null"},
  "offener_schritt": "ja|nein|unklar",
  "offener_schritt_beleg": "string|null",
  "teilerfolg": {"text": "Prototyp, Messdaten, Patent …|null", "zitat": "string|null"},
  "fachgebiet": "kurz, z. B. Hydraulik, Werkstoffe, Bildverarbeitung",
  "anwendung": "Branche oder Produkt, falls genannt|null",
  "rechenanteil": "hoch|mittel|niedrig|unklar",
  "suchbegriffe_en": ["3 bis 6 englische Fachbegriffe für den Fortsetzungscheck"]
}
```

## Eingabe je Eintrag

```
ID: {id}
Quelle: {pool}
Titel: {titel}
Ziel/Zusammenfassung: {text_a}
Bewertung/Bericht/Nutzung: {text_b}
```

## Zweiter Durchlauf

Gleiches Schema, aber die Regel „Im Zweifel ja“ wird ersetzt durch: „Lies den Text vom Ende her. Achte besonders auf Nebensätze, die erklären, warum etwas nicht klappte.“ Ein Eintrag kommt weiter, wenn einer der beiden Durchläufe `technisches_hindernis` oder `offener_schritt` mit „ja“ oder „unklar“ beantwortet.
