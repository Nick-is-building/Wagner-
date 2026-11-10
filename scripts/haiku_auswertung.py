"""Auswertung des Haiku-Prüfset-Laufs (A02 Schritt 4). Kostenlos, liest nur lokale Dateien.

Regel aus prompts/haiku_extraktion.md: Ein Eintrag kommt weiter, wenn einer der beiden
Durchläufe technisches_hindernis oder offener_schritt mit "ja" oder "unklar" beantwortet.
Ausgabe: Tabelle je Eintrag als TSV nach stdout, Zusammenfassung nach stderr.
"""
import csv, json, sys
from collections import defaultdict

klasse = {r["id"]: r for r in csv.DictReader(open("pruefset/pruefset.csv", encoding="utf-8"))}
eingabe = {json.loads(l)["id"] for l in open("ergebnisse/pruefset_eingabe.jsonl", encoding="utf-8")}
antw = defaultdict(dict)
for l in open("ergebnisse/haiku_pruefset_ok.jsonl", encoding="utf-8"):
    d = json.loads(l)
    antw[d["id"]][d["durchlauf"]] = d
zitat = defaultdict(list)
for l in open("ergebnisse/zitat_check.jsonl", encoding="utf-8"):
    d = json.loads(l)
    zitat[d["id"]].append(d)

POS = {"ja", "unklar"}
summe = defaultdict(lambda: [0, 0])
print("\t".join(["id", "klasse", "weiter", "th1", "os1", "th2", "os2", "muster", "zitat_status"]))
for i, r in klasse.items():
    if i not in eingabe:
        print(f"{i}\t{r['klasse']}\tnicht_in_eingabe", file=sys.stderr)
        continue
    a = antw.get(i, {})
    werte = []
    for n in (1, 2):
        x = a.get(n, {})
        werte += [x.get("technisches_hindernis"), x.get("offener_schritt")]
    weiter = any(w in POS for w in werte)
    muster = sorted({m for x in a.values() for m in (x.get("hindernis_muster") or [])})
    zs = ",".join(z["status"] for z in zitat[i])
    summe[r["klasse"]][0] += weiter
    summe[r["klasse"]][1] += 1
    print("\t".join([i, r["klasse"], "ja" if weiter else "NEIN"] + [str(w) for w in werte] + [" ".join(muster), zs]))
for k, (w, n) in summe.items():
    print(f"{k}: {w} von {n} weiter", file=sys.stderr)
