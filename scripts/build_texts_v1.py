# Texte v1 (bis A04): Felder nach 500 bis 600 Zeichen abgeschnitten -> data/zwischen/items.pkl. Abgelöst durch build_texts.py (v2), bleibt für alte Läufe.
import pickle,re,json,sys
sys.path.insert(0,'scripts')
import early as E
sq=lambda s,n=600: re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s or '')).strip()[:n]
items=[]  # (uid, pool, title, chunkA, chunkB)
d=E.d
for r in d['cep_fail']+d['cep_pos']:
    if E.cep_hard(r): continue
    pool='cep_fail' if r in d['cep_fail'] else 'cep_pos'
    items.append((r['kod_projektu'],pool,r['nazev_projektu_originalni'],sq(r['nazev_projektu_originalni']+'. '+r['cile_reseni_originalni']),sq(r['slovni_hodnoceni_cesky'])))
for pool in ('fwf_obst','fwf_pos'):
    for r in d[pool]:
        fr=sq(r.get('_str.prfinalreport.en'),5000)
        ob=' '.join(s for s in re.split(r'(?<=[.!?])\s+',fr) if E.OBSTRUE.search(s) or E.OB.search(s) if hasattr(E,'OB')) if False else ' '.join(s for s in re.split(r'(?<=[.!?])\s+',fr) if E.OBSTRUE.search(s))
        items.append((r['_str.grantdoi'],pool,r['_str.projecttitle.en'],sq(r['_str.projecttitle.en']+'. '+(r.get('_str.prproposalsummary.en') or '')),sq(ob or fr[-600:])))
for r in d['sbir']:
    if E.sb_hard(r): continue
    a=sq(r['Abstract'],1500)
    items.append((r['Agency Tracking Number'] or r['Contract'],'sbir1',r['Award Title'],sq(r['Award Title']+'. '+a[:500]),a[500:1100]))
for r in d['gw']:
    if E.gw_hard(r): continue
    a=sq(r['Grant Abstract'],1500)
    items.append((r['Award ID'],'gw',r['Grant Title'],sq(r['Grant Title']+'. '+a[:500]),a[500:1100]))
n=pickle.load(open('data/zwischen/newpools.pkl','rb'))
for pool in ('poc','sme1_noP2','sme2'):
    for r in n[pool]:
        o=sq(r['objective'],1500)
        items.append((r['id'],pool,r['title'],sq(r['title']+'. '+o[:500]),o[500:1100]))
for r in n['sbir2']:
    a=sq(r['Abstract'],1500)
    items.append((r['Agency Tracking Number'] or r['Contract'],'sbir2',r['Award Title'],sq(r['Award Title']+'. '+a[:500]),a[500:1100]))
for r in n['riv']:
    if not (r['_unused'] or r['_opencue']): continue
    items.append((r['kod_vysledku'],'riv',r['nazev_v_puvodnim_jazyce'],sq(r['nazev_v_puvodnim_jazyce']+'. '+r['popis_vysledku_v_puv._jazyce']),sq(r['technicke_parametry']+' '+r['zpusoby_vyuziti_vysledku'])))
import collections
print(len(items),collections.Counter(i[1] for i in items))
pickle.dump(items,open('data/zwischen/items.pkl','wb'))
