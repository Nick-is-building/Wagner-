import os as _os
_ROOT=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),"..")
_ZW=_os.path.join(_ROOT,"data","zwischen"); _os.makedirs(_ZW,exist_ok=True)
_os.chdir(_os.path.join(_ROOT,"data","roh"))  # Rohdaten liegen in data/roh
import csv,json,glob,re,collections,random,pickle
csv.field_size_limit(10**9)
OLD_KEEP_GROUPS={'B','C','I','J','K'}; OLD_KEEP_CODES={'DB','DD','DH','DL','DM','EI','FS','GM'}
def tech(r):
    g=r['hlavni_obor_skupina']; o=r['hlavni_obor']; oe=r['hlavni_vedni_obor_oecd'][:3]
    if g: return (g in OLD_KEEP_GROUPS or o in OLD_KEEP_CODES) and o!='CE'
    if oe: return oe in {'101','102','103','104'} or (oe.startswith('2') and oe!='208')
    return False
infra=lambda r: r['kod_projektu'].startswith(('EG','ED','CZ.')) or bool(re.search(r'(?i)centr|infrastruktur|rekonstrukc|vybaven|pracovi[sš]t',r['nazev_projektu_originalni']))
formal=lambda r: bool(re.search(r'(?i)indikátor|užitn\w+ vzor|doložit dokumenty|dodatek smlouvy|konkurs|insolven',r['slovni_hodnoceni_cesky']))
P={}
for r in csv.DictReader(open('cep.csv',encoding='utf-8-sig',errors='replace',newline='')): P.setdefault(r['kod_projektu'],r)
P=list(P.values())
cep_fail=[r for r in P if tech(r) and (r['posledni_stav_projektu'] in ('S','P') or r['kod_hodnoceni'] in ('N','S','O')) and not infra(r) and not formal(r) and len(r['slovni_hodnoceni_cesky'])>40]
cue_pos=re.compile(r'(?i)prototyp|funkční vzor|ověřen\w* technolog|patent|užitn\w+ vzor|poloprovoz|pilotní|software')
cep_pos=[r for r in P if tech(r) and r['kod_hodnoceni'] in ('V','U') and r['rok_ukonceni'] and r['rok_ukonceni']<='2021' and not infra(r) and cue_pos.search(r['slovni_hodnoceni_cesky'])]
rows=[]
for f in glob.glob('fwf2/*.json'): rows+=json.load(open(f))['results']
NAT={'Physics, Astronomy','Mathematics','Computer Sciences','Chemistry'}
fw=[r for r in rows if r.get('_str.prfinalreport.en') and ('Technical Sciences' in (r.get('_list.researchareas.en') or []) or set(r.get('_list.researchfields.en') or [])&NAT) and 'Biology' not in (r.get('_list.researchfields.en') or [])]
cue=re.compile(r"(?i)\b(could not|couldn't|was not possible|were not possible|not yet possible|remains? (open|unclear|unsolved|elusive)|did not (work|succeed)|failed to|unfortunately|due to (the )?(lack|limited|insufficient|technical)|limited by|beyond the scope|computationally (expensive|demanding|prohibitive)|insufficient (data|resolution|computing)|future work|further (work|research|investigation) (is|will be) (needed|required|necessary)|open question|bottleneck|obstacle|turned out to be (more )?difficult)\b")
pos=re.compile(r'(?i)\b(prototype|proof[- ]of[- ](principle|concept)|patent(ed)?|first (time|demonstration)|world[- ]record|spin[- ]off|industrial partner|could be (scaled|applied|used)|great potential|promising (results|approach|candidate))\b')
fwf_obst=[r for r in fw if cue.search(r['_str.prfinalreport.en'])]
fwf_pos=[r for r in fw if (r.get('_date.enddate') or '9')<'2022' and pos.search(r['_str.prfinalreport.en']) and not cue.search(r['_str.prfinalreport.en'])]
s=list(csv.DictReader(open('sbir.csv',encoding='utf-8',errors='replace')))
norm=lambda x:x.strip().upper()
p2=[r for r in s if r['Phase']=='Phase II']
k2=set((norm(r['Company']),r['Topic Code'].strip()) for r in p2 if r['Topic Code'].strip())
py=collections.defaultdict(list)
for r in p2: py[norm(r['Company'])].append(r['Award Year'])
excl={'Department of Health and Human Services','Department of Agriculture','Environmental Protection Agency','Department of Education'}
oc=re.compile(r'(?i)open call|open topic|afwerx|af ventures|dual-purpose|commercial solution|existing (platform|product|tool)')
sbir=[r for r in s if r['Phase']=='Phase I' and r['Agency'] not in excl and r['Topic Code'].strip() and len(r['Abstract'])>200 and (norm(r['Company']),r['Topic Code'].strip()) not in k2 and not any(y>=r['Award Year'] for y in py.get(norm(r['Company']),[])) and not oc.search(r['Award Title']+' '+r['Abstract']) and r['Award Year']<='2021']
g=list(csv.DictReader(open(glob.glob('gw/*/data/nsf_disruptions.csv')[0],encoding='utf-8')))
gw=[x for x in g if x['Current Status']=='Disrupted' and x['Directorate'] in ('Engineering','Computer and Information Science and Engineering','Technology, Innovation and Partnerships','Mathematical and Physical Sciences')]
pickle.dump(dict(cep_fail=cep_fail,cep_pos=cep_pos,fwf_obst=fwf_obst,fwf_pos=fwf_pos,sbir=sbir,gw=gw),open(_os.path.join(_ZW,'pools.pkl'),'wb'))
print({k:len(v) for k,v in dict(cep_fail=cep_fail,cep_pos=cep_pos,fwf_obst=fwf_obst,fwf_pos=fwf_pos,sbir=sbir,gw=gw).items()})
