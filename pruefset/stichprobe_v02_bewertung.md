# Bewertung der Stichprobe aus Haiku v0.2 (A04 Schritt 5)

Stand: 10.11.2026, Claude Code (Opus 5.5), **ein einzelner Prüfer, vorläufig**.

Grundlage: die 20 Beispiele in `ergebnisse/haiku_v02_stichprobe.md` (10 nach der v0.2-Regel aus A03 durchgekommen, 10 ausgesiebt). Je Eintrag gelesen: Originaltext aus `ergebnisse/zufall100_eingabe.jsonl` und Haikus Zitate. Punktzahl aus `ergebnisse/punktzahl_zufall.tsv` (Regel aus A04).

Stufen: **B** prüfenswert · **G** Grenzfall · **C** ungeeignet. „(unsicher)“ heißt: Das Urteil hängt an etwas, das der Text nicht sagt.

Gemeinsame Einschränkung: 17 der 20 Texte sind Anträge oder Zusammenfassungen (SBIR, EU-KMU-Instrument, PoC, NSF). Sie beschreiben, was geplant war, nicht was geschah. Ob ein Kern offen blieb, folgt dort höchstens aus dem Pool, zum Beispiel KMU-Phase 1 ohne Phase 2 (`sme1_noP2`, `scripts/newpools.py`), nicht aus dem Text. Nur die 3 Einträge aus RIV und CEP berichten ein Ergebnis. Die Felder sind außerdem nach 500 bis 600 Zeichen mitten im Satz abgeschnitten (`scripts/build_texts.py`).

## 10 Durchgekommene (v0.2-Regel)

| ID | Stufe | Punkte | Begründung |
|---|---|---|---|
| 650447 | G (unsicher) | 0 | Medizintechnik (elektrochemischer NO-Sensor für Asthma), klare Anwender; aber kein Hindernis genannt, kaum Rechenanteil, Zulassung als Grenze. |
| FX20D-TCSO1-0448 | G (unsicher) | 0 | 3D-Druck von Flugzeugteilen, Prozessparameter wären ein Fall für Bayes-Optimierung; Auftraggeber Luftwaffe, zivile Nutzung (eVTOL) möglich, Ergebnis unbekannt. |
| 245590 | G | 0 | Akustische Datenübertragung im Bohrloch für CO2-Speicher; Wellenleiter-Simulation passt zu Ersatzmodellen, Anwender klar; Ausgang der Phase I unbekannt. |
| F093-025-1044a | C | 1 | Lagebild-Software für Einsatzkräfte der Luftwaffe, Phase II, laut Text schon im Einsatz erprobt; Datenintegration ohne offenen technischen Kern. |
| 1648466 | C (unsicher) | 1 | Spielzeug-Roboterhaustier; Produktentwicklung ohne genanntes technisches Hindernis, die erste Generation entsteht laut Text schon in Phase I. |
| N201-X02-0598 | G | 2 | Gebäude-Zustandsüberwachung mit Vorhersage; Zeitreihen-Modelle aus dem Katalog passen, Anwender klar; vor allem Integration, Hindernis nicht genannt. |
| 2126637 | C (unsicher) | 1 | Roboter gegen invasive Pflanzen im Wald; Technik erlaubt, aber Anwendung Ökologie und Forst, also ausgeschlossenes Feld. |
| 673107 | G | 1 | Energierückgewinnung aus Aufzügen mit Ultrakondensatoren; klarer Markt (4,5 Mio. Aufzüge in der EU), aber kein Hindernis genannt und wenig Rechenanteil. |
| 727227 | B (unsicher) | 2 | ERC-Verfahren zur automatischen Erkennung feiner Linienstrukturen in Bildern soll Industriesoftware werden; passt zu Bildmodellen und Code-Agenten, Anwender genannt (Neurowissenschaft, Kartografie); unsicher, ob nicht längst weitergeführt. |
| 720219 | C | 0 | Online-Plattform zur Vermittlung zwischen Modemarken und Herstellern; Geschäftsmodell ohne technischen Kern. |

## 10 Ausgesiebte (v0.2-Regel)

| ID | Stufe | Punkte | Begründung |
|---|---|---|---|
| RIV/75081431:_____/22:00002522 | C | 2 | DC/DC-Netzteil für Fahrzeugsensoren; fertiges, einfaches Bauteil ohne offenen Kern. |
| 0945327 | G (unsicher) | 0 | Maskenlose holografische Nanolithografie mit räumlichem Lichtmodulator; Muster-Berechnung wäre rechnerisch angehbar, aber Reinraum als Grenze, Text nur ein Satz. |
| 829467 | C | 1 | VirtualGrasp (Gleechi), bestehendes Firmenprodukt für Handanimation in VR; kein abgebrochener Kern erkennbar. |
| 237106 | G | 1 | Photonische Kristall-Beschichtung für Szintillatoren; Rückwärtsentwurf und Simulation passen, Anwender Detektorhersteller; Ergebnis der Phase I unbekannt. |
| FV40363 | C | 2 | Software für 3D-gedruckte Beinprothesen; laut Text alle Ziele erreicht. |
| TH02020798 | C | 1 | Datensammlung beim Training von Kraftwerksbedienern; Ziele erfüllt, eher Methodik und Ausbildung als Technik. |
| 237433 | C (unsicher) | 1 | Mikrobieller Katalysator für eine Chemikalie; Biotechnologie am Rand des Ausschlusses „reine Biologie“, kein Hindernis genannt. |
| N192-064-0762 | G (unsicher) | 0 | Kartierung über Wasser ohne GPS per Bildverarbeitung; Bildmodelle passen, zivile Vermessung denkbar; Auftraggeber Marine, Ergebnis unbekannt. |
| 2315480 | C | 0 | Sozialwissenschaftliche Studie zu Schwarzen Frauen in der Informatik; ausgeschlossenes Fach. |
| A2-8226 | C | 4 | Elektronenmikroskopie-Messverfahren für Infrarot-Detektoren; das alte Hindernis ist laut Text in Phase I gelöst, Phase II läuft (Armee). |

## Zählung

- **Unter den 10 Ausgesiebten:** 0 B, 3 G (0945327, 237106, N192-064-0762).
- **Unter den 10 Durchgekommenen:** 4 C (F093-025-1044a, 1648466, 2126637, 720219), 1 B, 5 G.
- Die v0.2-Regel ließ 6 von 9 B+G durch und 4 von 11 C.

## Hätte die Punktzahl besser getrennt?

Nein. S1 und S2 liegen bei 0 Punkten (`pruefset/punktzahl_test_2026-11-10.md`), damit kommen alle 20 durch. Das trennt gar nicht.

Zum Vergleich, nicht beauftragt:
- Bei einer Schwelle von 1 Punkt kämen 4 von 9 B+G durch, aber 9 von 11 C.
- Bei 2 Punkten wären es 2 von 9 B+G und 3 von 11 C.

In diesen 20 Fällen trennt die Punktzahl also schlechter als die v0.2-Regel. Grund: Die Punkte belohnen Teilerfolg und RIV-Code O; beides haben fertige Ergebnisse (RIV, CEP) eher als offene Anträge. Bei 20 Fällen und einem Prüfer ist das ein Hinweis, kein Beleg.
