import csv,collections,sys,random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
csv.field_size_limit(10**9)
rows=list(csv.DictReader(open(sys.argv[1],encoding='utf-8',errors='replace')))
norm=lambda s:s.strip().upper()
p1=[r for r in rows if r['Phase']=='Phase I' and len(r['Abstract'])>200]
p2=[r for r in rows if r['Phase']=='Phase II' and len(r['Abstract'])>200]
k2=set((norm(r['Company']),r['Topic Code'].strip()) for r in p2 if r['Topic Code'].strip())
p2_by_co=collections.defaultdict(list)
for r in p2: p2_by_co[norm(r['Company'])].append(r)
vec=TfidfVectorizer(stop_words='english',min_df=3,max_df=0.3,sublinear_tf=True)
vec.fit([r['Abstract'] for r in random.Random(0).sample(rows,60000) if r['Abstract']])
def maxsim(r):
    cands=[c for c in p2_by_co.get(norm(r['Company']),[]) if c['Award Year']>=r['Award Year']]
    if not cands: return None
    A=vec.transform([r['Abstract']]); B=vec.transform([c['Abstract'] for c in cands])
    return float((B@A.T).toarray().max())
withtopic=[r for r in p1 if r['Topic Code'].strip()]
matched=[r for r in withtopic if (norm(r['Company']),r['Topic Code'].strip()) in k2]
unmatched=[r for r in withtopic if (norm(r['Company']),r['Topic Code'].strip()) not in k2]
print('P1 abstract>200 with topic',len(withtopic),'matched',len(matched),'unmatched',len(unmatched))
rnd=random.Random(1)
ms=[maxsim(r) for r in rnd.sample(matched,1500)]; ms=[m for m in ms if m is not None]
print('matched pairs sim: median %.2f p10 %.2f p25 %.2f'%(np.median(ms),np.percentile(ms,10),np.percentile(ms,25)))
us=[maxsim(r) for r in rnd.sample(unmatched,4000)]
none=sum(1 for u in us if u is None); vals=[u for u in us if u is not None]
thr10=np.percentile(ms,10); thr25=np.percentile(ms,25)
print('unmatched sample 4000: company never got later P2: %d (%.0f%%)'%(none,100*none/len(us)))
print('  sim>=p25 of matched (%.2f): %.0f%%'%(thr25,100*sum(v>=thr25 for v in vals)/len(us)))
print('  sim>=p10 of matched (%.2f): %.0f%%'%(thr10,100*sum(v>=thr10 for v in vals)/len(us)))
print('  sim<0.15: %.0f%%'%(100*sum(v<0.15 for v in vals)/len(us)))
