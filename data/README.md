# Daten

Rohdaten liegen in `data/roh/`, Zwischenstände in `data/zwischen/`. Beides kommt nicht ins Repository. Laden mit `bash scripts/daten_laden.sh`.

| Datei oder Ordner | Inhalt | Größe |
|---|---|---|
| `cep.csv` | CEP Tschechien, 63.151 Projekte | 158 MB |
| `ciselniky/` | offizielle CEP-Codelisten | klein |
| `sbir.csv` | SBIR/STTR USA, alle Förderungen | 351 MB |
| `cordis/{h2020,fp7,he}/` | CORDIS-Projekte, Fachgebiete, Organisationen | 588 MB mit Zip |
| `fwf2/` | alle 20.602 FWF-Projekte als JSON | 70 MB |
| `gw/` | Grant Witness (gekündigte US-Förderungen) | 57 MB |
| `riv/riv_applied.jsonl` | RIV 2018–2024, nur Prototyp, Technologie, Patent, Gebrauchsmuster, Software | 80 MB |

Codes, die man kennen muss: CEP-Bewertung „O“ = Ziel nicht erfüllt, Vertrag eingehalten; „S“ = nicht erfüllt mit Sanktion; „N“ = alter Code 1998–2007. CEP-Status „S“ = vorzeitig beendet, „P“ = unterbrochen. RIV-Nutzung „O“ = bisher ungenutzt, „N“ = für andere ohne Lizenz nutzbar.
