#!/usr/bin/env bash
# Stufe 1: Pools bauen, Frühfilter anwenden, Texte für Stufe 2 aufbereiten. Vom Projektordner aus aufrufen.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/pools.py
python3 scripts/newpools.py
python3 scripts/early.py
python3 scripts/build_texts_v1.py
python3 scripts/cordis_berichte.py
python3 scripts/build_texts.py
python3 scripts/pruefset_eingabe.py
