import pickle,re,collections
d=pickle.load(open('data/zwischen/pools.pkl','rb'))
R=lambda p: re.compile(p,re.I)
# --- CEP ---
FORMAL2=R(r'úpad|odstoupil\w* od smlouvy|doložen|doložit|metodik\w* hodnocení|k tíži příjemce')
PERSON=R(r'odjezd|změn\w* řešitele|mateřsk|odchod\w* řešitel|úmrt|zahraniční\w* pobyt')
NOINFO=lambda h: len(re.sub(r'\s+',' ',h).strip())<70 or re.fullmatch(r'\s*Řešitel nesplnil zadání, smlouva však byla dodržena\.?\s*',h) is not None
EARLY0=R(r'po \d+ měsíc|nebyly dosaženy žádné')
INFRA2=lambda r: r['kod_projektu'].startswith(('LM','LQ','LO','LR'))
PURE=lambda r: (r['hlavni_obor'] in {'BA','BN','DB','DC','DD','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP'})
TECHOBST_CZ=R(r'nepodařil|nedosa[žh]|vyjma parametr|parametr\w* (nebyl|ne)|účinnost|stabilit|životnost|výtěžn|nezdařil|technick\w* (problém|potíž)|nebyl\w* (vyroben|ověřen|dosažen)|nefunk|selhal|výrob\w* prototyp')
OPEN_CZ=R(r'další\w* (vývoj|výzkum|ověř)|pokračov|do budoucna|zatím|potenciál|bude (třeba|nutné)|perspektiv|komercializ|uplatnění na trhu')
def cep_hard(r):
    h=r['slovni_hodnoceni_cesky']
    if FORMAL2.search(h): return 'formal2'
    if INFRA2(r): return 'infra2'
    return None
def cep_soft(r):
    h=r['slovni_hodnoceni_cesky']; s=[]
    if NOINFO(h): s.append('noinfo')
    if PERSON.search(h) or EARLY0.search(h): s.append('person/early')
    if PURE(r): s.append('pure')
    return s
# --- FWF ---
APPLIED={'Computer Sciences','Electrical Engineering, Electronics, Information Engineering','Chemistry','Other Technical Sciences','Mechanical Engineering','Materials Engineering','Chemical Process Engineering','Environmental Engineering, Applied Geosciences','Civil Engineering','Medical Engineering','Nanotechnology','Industrial Biotechnology','Electrical Engineering'}
OBSTRUE=R(r'(could not|was not possible|failed to|unfortunately|limited by|computationally (too )?expensive|bottleneck|only minute|too (slow|costly|expensive)|not (yet )?(feasible|achieved|released)|lack of (data|computing|resources))')
def fwf_txt(r): return re.sub(r'<[^>]+>',' ',r['_str.prfinalreport.en'] or '')
def fwf_soft(r):
    s=[]
    if not set(r['_list.researchfields.en'])&APPLIED: s.append('pure-field')
    if not OBSTRUE.search(fwf_txt(r)): s.append('no-real-obstacle')
    return s
# --- SBIR ---
DOD=lambda r: r['Agency'].startswith('Department of Defense')
CIVIL=R(r'commercial|civilian|dual[- ]use|industr|medical|automotive|consumer|energy|manufactur')
SBHARD=R(r'pitch day|open topic|\bCSO\b|already in use|existing (product|commercial)|patented .{0,40}product|commercially viable, and tested')
WEAP=R(r'missile|interceptor|warhead|battlespace|targeting|munition|weapon|lethal')
def sb_hard(r):
    t=r['Award Title']+' '+r['Abstract']+' '+r['Topic Code']
    if SBHARD.search(t): return 'pitch/product'
    if DOD(r) and WEAP.search(t) and not CIVIL.search(r['Abstract']): return 'weapon-only'
    return None
def sb_soft(r):
    s=[]
    if DOD(r) and not CIVIL.search(r['Abstract']): s.append('dod-no-civil')
    return s
# --- GW ---
GWHARD=R(r'^(Conference|Planning|Workshop|REU Site|RET Site|Collaborative Research: Conference)|equit|inclusi|broadening participation|minoritized|underserved|diversity|misinformation|fact-check|social media|STEM (education|identity)|students?\b.{0,40}(learning|education)')
def gw_hard(r):
    if r['Division']=='Engineering Education and Centers': return 'education'
    if GWHARD.search(r['Grant Title']+' '+r['Grant Abstract'][:600]): return 'social/edu/conf'
    try:
        if float(r['Funds Remaining Before Disruption'] or 0)<50000: return 'little-left'
    except: pass
    return None

def run():
    out={}
    for tag in d:
        c=collections.Counter(); keep_hard=0; front=0
        for r in d[tag]:
            if tag.startswith('cep'):
                h=cep_hard(r); s=cep_soft(r) if not h else []
                if tag=='cep_pos' and not h and not OPEN_CZ.search(r['slovni_hodnoceni_cesky']+' '+r['cile_reseni_originalni']): s=s+['no-open-cue']
                if tag=='cep_fail' and not h and TECHOBST_CZ.search(r['slovni_hodnoceni_cesky']): f=1
                else: f=0
            elif tag.startswith('fwf'):
                h=None; s=fwf_soft(r); f= 0 if s else 1
            elif tag=='sbir':
                h=sb_hard(r); s=sb_soft(r) if not h else []; f=0 if (h or s) else 1
            else:
                h=gw_hard(r); s=[]; f=0 if h else 1
            if h: c['HART:'+h]+=1
            else:
                keep_hard+=1
                for x in s: c['weich:'+x]+=1
                if not s: c['ohne_weich']+=1
                if tag=='cep_fail' and f and not s: front+=1
        out[tag]=(len(d[tag]),keep_hard,c,front)
    return out
if __name__=='__main__':
    for tag,(n,k,c,f) in run().items():
        print(f'\n{tag}: {n} -> nach harten Regeln {k} ({100*k/n:.0f}%)' + (f' | cep_fail mit techn. Hindernis & ohne weich: {f}' if tag=='cep_fail' else ''))
        for x,v in sorted(c.items()): print('   ',x,v)
