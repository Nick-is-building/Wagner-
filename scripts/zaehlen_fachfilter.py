import os as _os
_ROOT=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),"..")
_ZW=_os.path.join(_ROOT,"data","zwischen"); _os.makedirs(_ZW,exist_ok=True)
_os.chdir(_os.path.join(_ROOT,"data","roh"))  # Rohdaten liegen in data/roh
import csv,json,glob,collections,sys,pickle
csv.field_size_limit(10**9)
tok=lambda s: len(s or '')/3.5
out={}
# ---- CEP
P={}
for r in csv.DictReader(open('cep.csv',encoding='utf-8-sig',errors='replace',newline='')): P.setdefault(r['kod_projektu'],r)
P=list(P.values())
flag=[r for r in P if r['posledni_stav_projektu'] in ('S','P') or r['kod_hodnoceni'] in ('N','S','O')]
OLD_KEEP_GROUPS={'B','C','I','J','K'}; OLD_KEEP_CODES={'DB','DD','DH','DL','DM','EI','FS','GM'}
def cep_tech(r):
    g=r['hlavni_obor_skupina']; o=r['hlavni_obor']; oe=r['hlavni_vedni_obor_oecd'][:3]
    if g: return g in OLD_KEEP_GROUPS or o in OLD_KEEP_CODES
    if oe: return oe in {'101','102','103','104'} or (oe.startswith('2') and oe!='208')
    return False
cep=[r for r in flag if cep_tech(r)]
cep_txt=lambda r:' '.join([r['nazev_projektu_originalni'],r['cile_reseni_originalni'],r['slovni_hodnoceni_cesky']])
out['CEP']=(len(flag),len(cep),sum(tok(cep_txt(r)) for r in cep))
pickle.dump(cep,open(_os.path.join(_ZW,'cep_tech.pkl'),'wb'))
# ---- CORDIS
def esv(p):
    m=collections.defaultdict(set)
    fs=glob.glob(f'cordis/{p}/**/euroSciVoc.csv',recursive=True)
    if fs:
        for r in csv.DictReader(open(fs[0],encoding='utf-8-sig'),delimiter=';'): m[r['projectID']].add(r['euroSciVocPath'])
    return m
TECH=('engineering and technology','natural sciences/computer and information sciences','natural sciences/physical sciences','natural sciences/chemical sciences','natural sciences/mathematics')
cnt=[0,0,0];cord=[]
for p in ['h2020','fp7','he']:
    fs=glob.glob(f'cordis/{p}/**/project.csv',recursive=True)
    r=list(csv.DictReader(open(fs[0],encoding='utf-8-sig'),delimiter=';'))
    m=esv(p)
    t=[x for x in r if x['status']=='TERMINATED']
    nf=[x for x in t if not any(k in (x.get('fundingScheme') or '') for k in ('MSCA-IF','MSCA-PF','MC-I','MC-C','MC-ERG','MC-IRG'))]
    tech=[x for x in nf if any(pp.startswith(TECH) for pp in m.get(x['id'],[]))] if m else nf
    print(p,'terminated',len(t),'non-fellowship',len(nf),'tech',len(tech),'(no euroSciVoc file)' if not m else '')
    cnt[0]+=len(t);cnt[1]+=len(nf);cord+=tech
out['CORDIS']=(cnt[1],len(cord),sum(tok(x['title']+x['objective']) for x in cord))
# ---- FWF
rows=[]
for f in glob.glob('fwf2/*.json'): rows+=json.load(open(f))['results']
NAT={'Physics, Astronomy','Mathematics','Computer Sciences','Chemistry'}
def fwf_tech(r):
    a=set(r.get('_list.researchareas.en') or []); f=set(r.get('_list.researchfields.en') or [])
    return 'Technical Sciences' in a or bool(f & NAT)
cand=[r for r in rows if r.get('_str.prfinalreport.en') or (r.get('_str.status.en')=='Withdrawn' and r.get('_str.prproposalsummary.en'))]
fw=[r for r in cand if fwf_tech(r)]
out['FWF']=(len(cand),len(fw),sum(tok((r.get('_str.prfinalreport.en') or '')+(r.get('_str.prproposalsummary.en') or '')) for r in fw))
# ---- SBIR
rows=list(csv.DictReader(open('sbir.csv',encoding='utf-8',errors='replace')))
norm=lambda s:s.strip().upper()
p2=[r for r in rows if r['Phase']=='Phase II']
k2=set((norm(r['Company']),r['Topic Code'].strip()) for r in p2 if r['Topic Code'].strip())
p2years=collections.defaultdict(list)
for r in p2: p2years[norm(r['Company'])].append(r['Award Year'])
p1=[r for r in rows if r['Phase']=='Phase I' and r['Topic Code'].strip() and len(r['Abstract'])>200 and (norm(r['Company']),r['Topic Code'].strip()) not in k2]
clean=[r for r in p1 if not any(y>=r['Award Year'] for y in p2years.get(norm(r['Company']),[]))]
excl={'Department of Health and Human Services','Department of Agriculture','Environmental Protection Agency','Department of Education'}
sb=[r for r in clean if r['Agency'] not in excl]
print('SBIR agencies in clean',collections.Counter(r['Agency'] for r in clean).most_common(8))
out['SBIR']=(len(clean),len(sb),sum(tok(r['Award Title']+r['Abstract']) for r in sb))
# ---- GW NSF
r=list(csv.DictReader(open(glob.glob('gw/*/data/nsf_disruptions.csv')[0],encoding='utf-8')))
t=[x for x in r if x['Current Status']=='Disrupted']
g=[x for x in t if x['Directorate'] in ('Engineering','Computer and Information Science and Engineering','Technology, Innovation and Partnerships','Mathematical and Physical Sciences')]
out['GW-NSF']=(len(t),len(g),sum(tok(x['Grant Title']+x['Grant Abstract']) for x in g))
tot=[0,0,0]
for k,(a,b,c) in out.items():
    print(f'{k:8s} vorher {a:6d}  nach Fachfilter {b:6d}  Token {c/1e6:5.2f} Mio  (Schnitt {c/max(b,1):.0f})'); tot[0]+=a;tot[1]+=b;tot[2]+=c
print('SUMME',tot[0],tot[1],'%.1f Mio Token'%(tot[2]/1e6))
