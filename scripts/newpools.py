import csv,json,re,collections,pickle
csv.field_size_limit(10**9)
D='data/roh/'
# ---------- CORDIS ----------
TECHP=re.compile(r'^(engineering and technology|natural sciences/(computer and information sciences|physical sciences|chemical sciences|mathematics)|medical and health sciences/(medical biotechnology|health sciences/.*medical device|basic medicine/.*imaging))')
BADP=re.compile(r'^(agricultural sciences|social sciences|humanities|natural sciences/(biological sciences|earth and related environmental sciences))')
def cordis(fp,schemes,closed_only=True):
    sv=collections.defaultdict(list)
    for r in csv.DictReader(open(f'{D}cordis/{fp}/euroSciVoc.csv',newline='',encoding='utf-8'),delimiter=';'):
        sv[r['projectID']].append(r['euroSciVocPath'])
    out=[]
    for r in csv.DictReader(open(f'{D}cordis/{fp}/project.csv',newline='',encoding='utf-8'),delimiter=';'):
        if r['fundingScheme'] not in schemes: continue
        if closed_only and r['status'] not in ('CLOSED','TERMINATED'): continue
        paths=sv.get(r['id'],[])
        tech=any(TECHP.search(p) for p in paths); bad=paths and all(BADP.search(p) for p in paths)
        if not tech or bad: continue
        r['_paths']=paths[:6]; r['_fp']=fp; out.append(r)
    return out
poc=cordis('h2020',{'ERC-POC'})+cordis('he',{'HORIZON-ERC-POC'})+cordis('fp7',{'CSA-SA(POC)'})
sme1=cordis('h2020',{'SME-1'}); sme2=cordis('h2020',{'SME-2','SME-2b'})
# SME-1 ohne spaeteres SME-2 derselben Firma: Firmen ueber organization.csv
org=collections.defaultdict(set)
for r in csv.DictReader(open(f'{D}cordis/h2020/organization.csv',newline='',encoding='utf-8'),delimiter=';'):
    if r.get('role')=='coordinator': org[r['projectID']].add(r.get('organisationID') or r.get('name'))
sme2firms=set().union(*[org[r['id']] for r in sme2]) if sme2 else set()
sme1_noP2=[r for r in sme1 if not (org[r['id']] & sme2firms)]
print('ERC PoC tech:',len(poc),'| SME-1 tech:',len(sme1),'ohne SME-2:',len(sme1_noP2),'| SME-2 tech:',len(sme2))
# ---------- SBIR Phase II ohne Folgefoerderung ----------
rows=list(csv.DictReader(open(f'{D}sbir.csv',newline='',encoding='utf-8',errors='replace')))
last=collections.defaultdict(int)
for r in rows:
    try: last[r['Company'].strip().lower()]=max(last[r['Company'].strip().lower()],int(r['Award Year']))
    except: pass
EXCL=('Department of Health','Department of Agriculture','Environmental Protection','Department of Education')
CIVIL=re.compile(r'(?i)commercial|civilian|dual[- ]use|industr|medical|automotive|consumer|energy|manufactur')
WEAP=re.compile(r'(?i)missile|interceptor|warhead|battlespace|targeting|munition|weapon|lethal')
sb2=[]
for r in rows:
    if r['Phase']!='Phase II': continue
    try: y=int(r['Award Year'])
    except: continue
    if not 2008<=y<=2020 or r['Agency'].startswith(EXCL): continue
    if last[r['Company'].strip().lower()]>y+1: continue
    a=r['Abstract'] or ''
    if len(a)<200: continue
    if r['Agency'].startswith('Department of Defense') and (WEAP.search(a+r['Award Title']) or not CIVIL.search(a)): continue
    sb2.append(r)
print('SBIR Phase II ohne Folge (zivil nutzbar):',len(sb2))
# ---------- RIV ----------
riv=[json.loads(l) for l in open(f'{D}riv/riv_applied.jsonl')]
def rtech(r):
    oe=(r['obor_oecd'] or '')[:3]
    return oe in {'101','102','103','104'} or (oe.startswith('2') and oe!='208')
OPEN=re.compile(r'(?i)zatím|dosud nebyl|dosud není|nebyl[ao]? (zatím )?(implementov|využ|nasazen)|připraven\w* (k|pro) (komercializ|prodej|nasazení)|hledá\w* (partner|zájemce|výrobce)|licenc\w* (nabíz|k dispozici)')
rivp=[]
for r in riv:
    if r['druh'] not in ('G','Z','P','R','F') or not rtech(r): continue
    t=r['zpusoby_vyuziti_vysledku']+' '+r['ekonomicke_parametry']
    r['_unused']=r['druh_moznosti_vyuziti']=='O'; r['_free']=r['druh_moznosti_vyuziti']=='N'; r['_opencue']=bool(OPEN.search(t))
    rivp.append(r)
c=collections.Counter()
for r in rivp:
    c['tech']+=1; c['unused']+=r['_unused']; c['free']+=r['_free']; c['opencue']+=r['_opencue']; c['unused_or_opencue']+=(r['_unused'] or r['_opencue'])
print('RIV tech:',dict(c)); print('  nach Art (unused or opencue):',collections.Counter(r['druh'] for r in rivp if r['_unused'] or r['_opencue']))
pickle.dump({'poc':poc,'sme1_noP2':sme1_noP2,'sme2':sme2,'sbir2':sb2,'riv':rivp},open('data/zwischen/newpools.pkl','wb'))
