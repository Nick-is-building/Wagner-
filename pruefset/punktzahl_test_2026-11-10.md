# Punktzahl statt Ja/Nein: Schwellen, Stichprobe, Sonnet-Kosten (A04)

Stand: 10.11.2026, Claude Code (Opus 5.5). Auftrag `auftraege/A04_punktzahl.md`. Kostenlos, kein API-Aufruf. Prompt unverändert.

Dateien:
- Punktzahl: `scripts/punktzahl.py` → `ergebnisse/punktzahl_pruefset.tsv`, `ergebnisse/punktzahl_zufall.tsv`
- Kosten: `scripts/sonnet_kosten.py` → `ergebnisse/sonnet_kosten.txt`
- Bewertung der 20 Beispiele: `pruefset/stichprobe_v02_bewertung.md`

## 1. Prüfset korrigiert

`pruefset/pruefset.csv`: FW01010098 von „gut“ auf „grenzfall“. Der alte Wert steht mit Grund in der Spalte „begruendung“. Jetzt 8 gut, 2 gut (schon weitergeführt), 21 Grenzfall, 20 ungeeignet.

## 2. Skriptfehler behoben

`scripts/weiter_regel.py`: „unklar“ zählt jetzt, wenn irgendein Feld der Antwort ein Zitat hat. Das gilt auch für `offener_schritt_beleg`.

Folge: Alle 146 v0.2-Antworten haben mindestens ein Zitat. Die Regel „unklar ohne Zitat gilt nein“ greift damit praktisch nie mehr.

v0.2-Regel nach der Korrektur (Tabellen in neuen Dateien `ergebnisse/haiku_v02_*_a04.tsv`; die A03-Tabellen bleiben unverändert):
- Prüfset: gut 8 von 8, Grenzfall 13 von 21 (62 %), ungeeignet 11 von 15
- Zufall: 56 von 100 (vorher 52)
- Testregel weiterhin nicht bestanden

Beobachtet: 33 von 85 gefüllten `offener_schritt_beleg` sind kein wörtliches Zitat, sondern Haikus eigener Kommentar, etwa „Der Auszug endet mitten im Satz …“.

## 3. Punktzahl

Umsetzung wie im Auftrag. Drei Auslegungen von mir:
- **Hindernis-Muster:** Der höchste Wert zählt (H1 bis H3 → +2, sonst H4 bis H7 → +1). Mehrere Muster werden nicht addiert.
- **v0.1 hat zwei Durchläufe:** Es zählt der höhere Wert. v0.1 kennt die Felder Kern und Abbruchgrund nicht, sie zählen dort 0.
- **„Teilerfolg vorhanden“:** `teilerfolg.text` ist nicht leer.

## 4. Schwellen

### Rangliste der 8 guten und 21 Grenzfälle (Punkte v0.1 / v0.2)

| ID | Klasse | v0.1 | v0.2 |
|---|---|---|---|
| FR-TI3/018 | gut | 6 | 7 |
| 101123089 | gut | 4 | 7 |
| 10.55776/I5180 | gut | 7 | 6 |
| TJ01000218 | gut | 3 | 5 |
| FV10342 | gut | 2 | 2 |
| GA106/09/0814 | gut | 1 | 2 |
| GA203/99/P017 | gut | 3 | 1 |
| 101069261 | gut | 2 | 0 |
| 10.55776/P33931 | Grenzfall | 4 | 5 |
| 10.55776/P16969 | Grenzfall | 4 | 5 |
| 181662 | Grenzfall | 5 | 5 |
| PZ-CH/32 | Grenzfall | 2 | 4 |
| 841640 | Grenzfall | 4 | 4 |
| 1ET310330507 | Grenzfall | 2 | 3 |
| GA13-10527S | Grenzfall | 4 | 3 |
| TA04010165 | Grenzfall | 2 | 3 |
| UDSKLI2016_06_01 | Grenzfall | 2 | 3 |
| RIV/00216305:26110/22:PR36166 | Grenzfall | 3 | 3 |
| 966654 | Grenzfall | 5 | 2 |
| 712708 | Grenzfall | 2 | 2 |
| RIV/62156489:43210/24:43925736 | Grenzfall | 3 | 2 |
| RIV/46504711:_____/21:N0000005 | Grenzfall | 2 | 2 |
| 175273 | Grenzfall | 2 | 1 |
| 101069244 | Grenzfall | 1 | 1 |
| GPP204/10/P331 | Grenzfall | 3 | 0 |
| 665275 | Grenzfall | 0 | 0 |
| 666588 | Grenzfall | 2 | 0 |
| TA02020998 | Grenzfall | 0 | −1 |
| FW01010098 | Grenzfall | 0 | −2 |

### Ergebnis

Gelesen habe ich S1 und S2 als die höchste Schwelle, die die Bedingung noch erfüllt. Jede niedrigere erfüllt sie ohnehin.

| | S1 | S2 | gut / Grenzfall / ungeeignet ab S1 |
|---|---|---|---|
| v0.1 | 1 | 1 | 8/8 · 18/21 · 13/15 |
| v0.2 | 0 | 0 | 8/8 · 19/21 · 12/15 |

**S1 und S2 fallen zusammen und liegen ganz unten.** Grund sind die schwächsten guten Fälle:
- **101069261 (v0.2: 0 Punkte):** Kern und offener Schritt sind „unklar“, das bringt keine Punkte. Der Text ist mitten im Satz abgeschnitten.
- **GA203/99/P017 (v0.2: 1 Punkt):** Haiku stuft „mateřská dovolená“ (Mutterschaft) als „formal“ ein, nicht als „Personal“. Das kostet −2 Punkte und den +1 für Personal.
- **GA106/09/0814 (2 Punkte)**

### Alle Schwellen im Überblick (nicht beauftragt, zur Einordnung)

| ab Punkten | v0.1 gut/Grenz/ung | v0.2 gut/Grenz/ung | Zufall v0.2 (von 100) | SBIR (54) | sme1_noP2 (17) | RIV (14) |
|---|---|---|---|---|---|---|
| 0 | 8 · 21 · 15 | 8 · 19 · 12 | 100 | 54 | 17 | 14 |
| 1 | 8 · 18 · 13 | 7 · 16 · 12 | 70 | 35 | 11 | 14 |
| 2 | 7 · 17 · 8 | 6 · 14 · 8 | 37 | 19 | 6 | 8 |
| 3 | 5 · 9 · 4 | 4 · 10 · 7 | 13 | 8 | 2 | 1 |
| 4 | 3 · 6 · 1 | 4 · 5 · 1 | 5 | 4 | 0 | 0 |

### Zufall bei S1 = S2 = 0 (v0.2)

100 von 100, in jedem Pool alle Einträge (sbir1 27, sbir2 27, sme1_noP2 17, riv 14, sme2 5, cep_pos 5, cep_fail 3, poc 1, gw 1). Hochgerechnet auf 17.421 Einträge sind das 17.421. Für v0.1 gibt es keine Zufallsdaten; v0.1 lief nur am Prüfset.

### Verzerrung je Pool

- **Bei 0 Punkten liegt jeder Pool immer drüber.** Die Schwelle filtert nichts.
- **Bei 1 Punkt liegt RIV immer drüber (14 von 14).** Code O bringt automatisch +1 für den offenen Schritt. Ein Registereintrag über ein fertiges Ergebnis bringt fast immer +1 für den Teilerfolg. Beides misst die Quelle, nicht die Eignung.
- **Ab 3 Punkten fällt RIV fast ganz heraus (1 von 14), sme1_noP2 ebenfalls (2 von 17).** Anträge nennen selten ein Hindernis.

Vermutet: Die Punkte messen eher die Textart (Ergebnisbericht oder Antrag) als die Eignung.

## 5. Stichprobe selbst bewertet

Details: `pruefset/stichprobe_v02_bewertung.md` (ein Prüfer, vorläufig).

- **Unter den 10 Ausgesiebten:** 0 B, 3 Grenzfälle.
- **Unter den 10 Durchgekommenen:** 4 C (dazu 1 B, 5 Grenzfälle).
- **Vergleich der Trennung:**
  - v0.2-Regel: 6 von 9 B/Grenzfall durch, 4 von 11 C durch.
  - Punktzahl mit S1/S2 = 0: alle durch, keine Trennung.
  - ab 1 Punkt (nur zum Vergleich): 4 von 9 B/Grenzfall, aber 9 von 11 C.
- **Also: Die Punktzahl trennt hier nicht besser als die v0.2-Regel, eher schlechter.**

17 der 20 Texte sind Anträge ohne Aussage über den Ausgang. Dort kann weder Regel noch Punktzahl ein Hindernis finden.

## 6. Sonnet-Kosten

**Token-Eichung:** 657.814 Zeichen entsprechen 312.646 echten Eingabe-Token aus 146 Haiku-Aufrufen, also **2,10 Zeichen je Token**. Die Näherung „Zeichen geteilt durch 4“ hätte die Kosten etwa halbiert. Annahme: Sonnet zählt wie Haiku.

| Teil | Token je Aufruf | Herkunft |
|---|---|---|
| Fester Teil | rund 6.700 | Sonnet-Anweisung, Schema, vier Katalog-Abschnitte (14.113 Zeichen) |
| Variabler Teil | rund 1.400 | Mittel über die 100 Zufallseinträge: Eintragstext plus Haiku-JSON |
| Ausgabe | 600 / 1.000 / 1.500 | Annahme; Haiku-Ausgabe bei ähnlichem Schema im Mittel 862 Token |

Preise: 2 $ / 10 $ je Million Token. Zwischenspeicher (Cache): fester Teil zu 10 % des Eingabepreises. Batch: −50 %.

| Schwelle | Einträge (hochgerechnet) | Ausgabe | ohne Cache | mit Cache | Batch mit Cache |
|---|---|---|---|---|---|
| S1 = S2 = 0 | 17.421 | 600 | 387 $ | 177 $ | 88 $ |
| S1 = S2 = 0 | 17.421 | 1.000 | 457 $ | 247 $ | 123 $ |
| S1 = S2 = 0 | 17.421 | 1.500 | 544 $ | 334 $ | 167 $ |
| ab 2 Punkten (zum Vergleich) | 6.446 | 1.000 | 169 $ | 91 $ | 46 $ |
| ab 3 Punkten (zum Vergleich) | 2.265 | 1.000 | 59 $ | 32 $ | 16 $ |
| Prüfset (46 Einträge) | 46 | 1.000 | 1,2 $ | 0,7 $ | – |

Weitere Zeilen: `ergebnisse/sonnet_kosten.txt`.

Dazu kommt die Vorstufe: Haiku v0.2 auf alle 17.421 Einträge kostet rund 11 $ (0,00065 $ je Eintrag, gemessen).

**Unsichere Annahmen:**
- **Ausgabelänge.** Größter Hebel; zwischen 600 und 1.500 Token verdoppeln sich die Kosten mit Cache fast. Das Sonnet-Schema hat freie Textfelder (`weg`, `gewicht`, `staerkste_annahme`) ohne Längengrenze. Erst ein echter Prüfset-Lauf zeigt den Wert.
- **Denken.** Wenn Sonnet standardmäßig „denkt“ wie Haiku in A02, kommen Denk-Token als Ausgabe dazu.
- **Token-Eichung.** Sie stammt von Haiku und gemischten Texten (tschechisch, englisch, deutsch).
- **Nicht eingerechnet:** Cache-Schreiben und ob Batch und Cache zusammen voll wirken.
- **Hochrechnung.** Sie stützt sich auf 100 Einträge; bei 37 % ist der Bereich grob ±10 Prozentpunkte.

## 7. Empfehlung

Ich würde **weder S1 noch S2 nehmen**. Beide liegen bei 0 Punkten und schicken alle 17.421 Einträge an Sonnet (rund 250 $ mit Cache, 123 $ als Batch). Die Punktzahl hat in der Stichprobe nicht besser getrennt als die v0.2-Regel.

Der erste Sonnet-Lauf sollte nach den Projektregeln ohnehin **das Prüfset sein: 46 Einträge, rund 0,7 bis 1,2 $**. Er misst auch die echte Ausgabelänge, die unsicherste Zahl oben.

Für einen späteren großen Lauf wäre „ab 2 Punkten“ der Kompromiss: rund 6.400 Einträge, rund 91 $ mit Cache oder 46 $ als Batch. Er verliert heute aber 2 von 8 guten Fällen (GA203/99/P017, 101069261). Beide Verluste lassen sich auf behebbare Fehler zurückführen.

Vorher am Haiku-Prompt ändern (Entscheidung beim Planungs-Chat):
1. **Abbruchgründe mit Beispielen definieren:** Mutterschaft, Krankheit oder Wechsel der Leitung sind „Personal“. Abbruch auf eigenen Antrag ohne Grund ist „unklar“, nicht „formal“.
2. **`offener_schritt_beleg` muss ein Zitat sein** (33 von 85 sind keines).
3. **Texte nicht nach 500 bis 600 Zeichen mitten im Satz abschneiden.** Die Eingabe ist billig: 1.400 Token kosten bei Haiku rund 0,00014 $.
4. **Anträge anders fragen:** Bei SBIR-, KMU- und PoC-Texten gibt es keinen Ausgang, nur Plan und Risiko. Dort sollte Haiku das technische Risiko und den offenen Schritt erfassen. Ob es eine Fortsetzung gab, sagt der Pool, nicht der Text.

Am Sonnet-Prompt: Längengrenzen für die freien Felder (z. B. höchstens 40 Wörter). Das senkt den größten Kostenposten.
