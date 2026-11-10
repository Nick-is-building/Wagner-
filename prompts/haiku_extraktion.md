# Haiku: Felder herausziehen (v0.3, A06)

Status: wird in A06 Phase 3 am Prüfset (106 Einträge) und an 100 Zufallseinträgen getestet (Freigabe 2026-11-10-A06a). Bestanden, wenn alle 15 guten weiterkommen oder in der Antrags-Rangliste im oberen Viertel liegen, und mindestens 80 % der Grenzfälle ebenso.

Änderungen gegenüber v0.2: zwei Varianten nach `texttyp` (Texte v2, `data/zwischen/items_v2.pkl`); Hindernis mit `hindernis_quelle`; Abbruchgründe mit Beispielen (Elternzeit, Mutterschaft, Weggang, Krankheit = Personal); neues Feld `erster_schritt`; nur wörtliche Zitate, kurze Ausgabe (Ziel höchstens 250 Token). Die Auswahlregel steht in `scripts/auswahl_v03.py`, nicht im Prompt. v0.2: Git-Historie.

## Gemeinsamer Teil

```
Du liest den Eintrag eines Forschungs- oder Entwicklungsprojekts aus einem öffentlichen Register.
Der Text kann Tschechisch, Deutsch oder Englisch sein. Du urteilst nicht, du füllst Felder aus.

Regeln:
- Zitate exakt aus dem Text kopieren (Originalsprache, höchstens 15 Wörter). Kein eigener Kommentar
  im Zitat. Steht nichts im Text, schreibe null.
- "unklar" nur, wenn ein Zitat einen Hinweis zeigt; ohne Zitat gilt "nein".
- Hindernis-Muster (alle passenden): H1 Rechnung/Simulation zu teuer · H2 zu viele Varianten/Parameter,
  Werte verfehlt · H3 Auswertung von Hand zu aufwendig (Bilder, Dokumente, Signale) ·
  H4 Implementierung/Personal fehlte · H5 zu wenige Daten · H6 Messung ungenau/verrauscht ·
  H7 Material/Molekül nicht gefunden · H8 Bauteil teuer/nicht erhältlich · H9 Synthese/Herstellung
  gelang nicht · H10 Markt fehlte/Firma insolvent · H11 Zulassung/Vorschrift
- rechenanteil: Wie viel der Arbeit lässt sich am Rechner machen (Software, Simulation, Daten)?
  hoch, mittel, niedrig oder unklar.
- anwendung: Branche oder Produkt in höchstens 6 Wörtern, sonst null.
- erster_schritt: Womit würde man die Arbeit heute zuerst fortsetzen? software, simulation,
  datenanalyse, prototyp_klein (Gerät, das eine Person mit Teilen um 1.000 € bauen kann), labor
  (Chemie-, Bio- oder Speziallabor), reinraum, zulassung (klinische Studie, Tierversuch, Zertifizierung)
  oder unklar.
Antworte nur mit einem JSON-Objekt nach dem Schema, ohne Zeilenumbrüche, ohne weiteren Text.
```

## Variante „ergebnis“

Für Einträge mit Ausgangstext (CEP-Bewertung, FWF-Endbericht, RIV, CORDIS-Ergebnisbericht).

```
Der Text enthält Ziel/Motivation und einen Ausgangsteil (Bewertung, Endbericht, Ergebnisbericht).
- hindernis: Nennt der Text einen sachlichen Grund, warum ein technisches Ziel nicht oder nur teilweise
  erreicht wurde (Parameter verfehlt, Rechnung zu teuer, Daten fehlten, Messung zu ungenau, Material
  ungeeignet, Implementierung nicht fertig)? ja, nein oder unklar. Im Zweifel ja.
- hindernis_quelle: Wo steht das Hindernis? "ergebnis" = im Ausgangsteil (Bewertung, Endbericht,
  Ergebnis). "motivation" = nur in Ziel, Hintergrund oder Problembeschreibung des Antrags (das Problem,
  das das Projekt lösen wollte, ist KEIN Hindernis des Projekts). "unklar" = nicht zu entscheiden.
- abbruchgrund: Warum wurde ein Ziel nicht erreicht oder das Projekt nicht weitergeführt?
  Technik (Ziel technisch verfehlt) · Aufwand (zu aufwendig, zu langsam) · Geld (Mittel gekürzt,
  Finanzierung fehlte) · Personal (Elternzeit, Mutterschaft, Weggang, Krankheit, Tod, Mitarbeiter
  fehlten) · Organisation (Partner ausgestiegen, Firma umstrukturiert) · formal (NUR Papiere,
  Berichte, Indikatoren, Publikationszahl, Vertrag, Insolvenz) · keiner (Ziele erreicht) · unklar.
- offener_schritt: Sagt der Text ausdrücklich, dass Weiterentwicklung, Vermarktung, ein Partner,
  Investor oder eine Fortsetzung noch aussteht oder geplant ist? ja, nein oder unklar.
- kern_offen: Ist das eigentliche technische Ergebnis (nicht Publikationen oder Berichte) nicht oder
  nur teilweise erreicht oder nicht zu Ende geführt? ja, nein oder unklar.
```

Schema:

```json
{"hindernis":"ja|nein|unklar","hindernis_quelle":"ergebnis|motivation|unklar|null","hindernis_zitat":"string|null","muster":["H2"],"abbruchgrund":"Technik|Aufwand|Geld|Personal|Organisation|formal|keiner|unklar","abbruchgrund_zitat":"string|null","offener_schritt":"ja|nein|unklar","offener_schritt_zitat":"string|null","kern_offen":"ja|nein|unklar","rechenanteil":"hoch|mittel|niedrig|unklar","anwendung":"string|null","erster_schritt":"software|simulation|datenanalyse|prototyp_klein|labor|reinraum|zulassung|unklar"}
```

## Variante „antrag“

Für Einträge ohne Ausgangstext (SBIR, CORDIS ohne Bericht, Grant Witness). Dass ein solches Projekt liegen blieb, zeigen die Metadaten (keine Phase II, keine Folgeförderung), nicht der Text.

```
Der Text ist ein Antrag oder eine Projektbeschreibung, ohne Aussage über den Ausgang.
- kernrisiko: Was ist das technische Kernproblem oder Kernrisiko, an dem das Vorhaben am ehesten
  scheitern konnte? Ein Satz, höchstens 20 Wörter, oder null.
- kernrisiko_zitat: wörtliches Zitat, das dieses Problem oder Risiko zeigt.
- muster: Hindernis-Muster, die das Kernrisiko beschreiben (alle passenden).
```

Schema:

```json
{"kernrisiko":"string|null","kernrisiko_zitat":"string|null","muster":["H1"],"rechenanteil":"hoch|mittel|niedrig|unklar","anwendung":"string|null","erster_schritt":"software|simulation|datenanalyse|prototyp_klein|labor|reinraum|zulassung|unklar"}
```

## Eingabe je Eintrag

```
ID: {id}
Quelle: {pool}
Titel: {titel}
Text:
{text}
```

## Auswahl (in `scripts/auswahl_v03.py`)

- Ergebnis-Texte kommen weiter, wenn mindestens eines gilt: Hindernis ja/unklar mit Quelle „ergebnis“ oder „unklar“; Abbruchgrund außerhalb der Idee (Geld, Personal, Organisation, Aufwand; Technik nur, wenn das Hindernis nicht allein aus der Motivation stammt); offener Schritt ja/unklar.
- Antrags-Texte kommen in eine Rangliste: H1 bis H3 zuerst, dann Rechenanteil, dann Art des ersten Schritts.
- Labor, Reinraum und Zulassung nach hinten, nichts löschen.
