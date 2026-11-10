#!/usr/bin/env bash
# Lädt alle Rohdaten nach data/roh (rund 1,5 GB, einige Minuten). Mehrfach aufrufbar: Vorhandenes wird übersprungen.
set -euo pipefail
cd "$(dirname "$0")/../data/roh"
get(){ [ -s "$2" ] && echo "vorhanden: $2" || { echo "lade $2"; curl -fsSL --retry 3 -o "$2" "$1"; }; }

# CEP Tschechien (Projekte) und Codelisten
get https://www.isvavai.cz/dokumenty/opendata/CEP-projekty.csv cep.csv
mkdir -p ciselniky
for c in hodnoceni-projektu stav-projektu druh-vysledku moznost-vyuziti-vysledku; do
  get "https://www.isvavai.cz/dokumenty/opendata/ciselniky/$c.jsonld" "ciselniky/$c.jsonld"; done

# SBIR/STTR USA
get https://data.www.sbir.gov/awarddatapublic/award_data.csv sbir.csv

# CORDIS EU: Horizon 2020, FP7, Horizon Europe
mkdir -p cordis
for p in h2020:h2020 fp7:fp7 HORIZON:he; do
  src=${p%%:*}; dst=${p##*:}
  get "https://cordis.europa.eu/data/cordis-${src}projects-csv.zip" "cordis/$dst.zip"
  [ -d "cordis/$dst" ] || unzip -q -o "cordis/$dst.zip" -d "cordis/$dst"
done

# FWF Österreich (öffentlicher Leseschlüssel aus der FWF-Dokumentation)
mkdir -p fwf2
FWF='Authorization: Bearer 3a03f2f39cc8a99ea0775270adb4946c425469aa7f291e7ca9f2d8424337c1af'
for off in $(seq 0 1000 21000); do
  f=fwf2/p_$off.json; [ -s "$f" ] && continue
  curl -fsS -m 120 -H "$FWF" "https://openapi.fwf.ac.at/indexes/projects/documents?limit=1000&offset=$off&fields=_str.grantdoi,_str.status.en,_str.projecttitle.en,_list.researchareas.en,_list.researchfields.en,_str.prfinalreport.en,_str.prproposalsummary.en,_date.startdate,_date.enddate" > "$f"
done

# Grant Witness (Zenodo, neueste Fassung)
mkdir -p gw
if ! ls gw/*/data/nsf_disruptions.csv >/dev/null 2>&1; then
  url=$(curl -fsS https://zenodo.org/api/records/23577373 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['files'][0]['links']['self'])")
  curl -fsSL -o gw/gw.zip "$url"; unzip -q -o gw/gw.zip -d gw
fi

# RIV Tschechien 2018-2024, beim Laden gefiltert auf Prototyp, Technologie, Patent, Gebrauchsmuster, Software
mkdir -p riv
[ -s riv/riv_applied.jsonl ] || (cd ../.. && python3 scripts/riv_stream.py 2018 2024)

# CORDIS-Ergebnisberichte H2020 und Horizon Europe; aus dem JSON nur die Pools poc, sme1_noP2, sme2 (braucht newpools.pkl)
mkdir -p cordis_berichte/h2020 cordis_berichte/he
for p in h2020:h2020 HORIZON:he; do
  src=${p%%:*}; dst=${p##*:}
  get "https://cordis.europa.eu/data/cordis-${src}reports-csv.zip" "cordis_berichte/cordis-${src}reports-csv.zip"
  [ -s "cordis_berichte/$dst/reportSummaries.csv" ] || unzip -q -o "cordis_berichte/cordis-${src}reports-csv.zip" reportSummaries.csv -d "cordis_berichte/$dst"
done
if [ -s ../zwischen/newpools.pkl ] && [ ! -s ../zwischen/cordis_berichte.jsonl ]; then
  for src in h2020 HORIZON; do get "https://cordis.europa.eu/data/cordis-${src}reports-json.zip" "cordis_berichte/cordis-${src}reports-json.zip"; done
  (cd ../.. && python3 scripts/cordis_berichte.py --zip-loeschen)
else echo "CORDIS-Berichte: übersprungen (fehlt newpools.pkl oder schon vorhanden)"; fi

du -sh . ; echo "fertig"
