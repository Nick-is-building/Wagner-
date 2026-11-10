"""Prüft, ob die Zitate aus der Haiku-Ausgabe wörtlich im Originaltext stehen (Belegpflicht, kostenlos).

Aufruf: python3 scripts/zitat_check.py EINGABE.jsonl HAIKU_AUSGABE.jsonl [ZIEL.jsonl]
EINGABE: Zeilen mit id, titel, text_a, text_b (z. B. ergebnisse/pruefset_eingabe.jsonl)
AUSGABE: Haiku-JSON je Zeile mit id und Feldern {text, zitat}
Schreibt ZIEL (Standard ergebnisse/zitat_check.jsonl) und meldet, wie viele Einträge in "Nachprüfen" gehören.
"""
import json,re,sys,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKC',s or '').lower()
    s=re.sub(r'[„“”"‚‘’\'«»]','',s)
    return re.sub(r'\s+',' ',s).strip()
src={}
for l in open(sys.argv[1]):
    r=json.loads(l); src[r['id']]=norm(' '.join([r.get('titel',''),r.get('text_a',''),r.get('text_b','')]))
ok=bad=0; out=open(sys.argv[3] if len(sys.argv)>3 else 'ergebnisse/zitat_check.jsonl','w')
for l in open(sys.argv[2]):
    r=json.loads(l); t=src.get(r.get('id'),'')
    fehl=[]
    for k,v in r.items():
        if isinstance(v,dict) and v.get('zitat'):
            z=norm(v['zitat']).rstrip('.…')
            if z and z not in t: fehl.append(k)
    status='ok' if not fehl else 'nachpruefen'
    ok+=not fehl; bad+=bool(fehl)
    out.write(json.dumps({'id':r.get('id'),'status':status,'felder_ohne_beleg':fehl},ensure_ascii=False)+'\n')
print(f'{ok} Einträge mit allen Zitaten belegt, {bad} zum Nachprüfen')
