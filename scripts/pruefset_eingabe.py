"""Holt die Prüfset-Einträge aus data/zwischen/items.pkl und schreibt sie als Eingabe für Haiku/Sonnet.
Einträge, die nicht in den Pools stecken (z. B. hart gefiltert), werden direkt aus den Rohdaten geholt
und als solche markiert. Ausgabe: ergebnisse/pruefset_eingabe.jsonl
"""
import pickle,csv,json,os,sys
items=pickle.load(open('data/zwischen/items.pkl','rb'))
by={it[0]:it for it in items}
ps=list(csv.DictReader(open('pruefset/pruefset.csv',encoding='utf-8')))
os.makedirs('ergebnisse',exist_ok=True)
miss=[]
with open('ergebnisse/pruefset_eingabe.jsonl','w') as f:
    for r in ps:
        it=by.get(r['id'])
        if not it: miss.append(r['id']); continue
        f.write(json.dumps({'id':it[0],'pool':it[1],'titel':it[2],'text_a':it[3],'text_b':it[4],'klasse':r['klasse']},ensure_ascii=False)+'\n')
cep={}
if miss:
    csv.field_size_limit(10**9)
    for r in csv.DictReader(open('data/roh/cep.csv',encoding='utf-8-sig',errors='replace',newline='')):
        if r['kod_projektu'] in miss: cep[r['kod_projektu']]=r
    with open('ergebnisse/pruefset_eingabe.jsonl','a') as f:
        for k,r in cep.items():
            kl=next(x['klasse'] for x in ps if x['id']==k)
            f.write(json.dumps({'id':k,'pool':'cep_roh','titel':r['nazev_projektu_originalni'],'text_a':r['nazev_projektu_originalni']+'. '+r['cile_reseni_originalni'][:600],'text_b':r['slovni_hodnoceni_cesky'][:600],'klasse':kl},ensure_ascii=False)+'\n')
rest=[m for m in miss if m not in cep]
print(f'{len(ps)} im Prüfset, {len(ps)-len(rest)} geschrieben. Nicht in den Pools (von harten Frühfiltern entfernt, das ist gewollt): {rest}')
