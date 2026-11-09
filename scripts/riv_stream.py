import csv,sys,io,urllib.request,os,json
csv.field_size_limit(10**9)
KEEP={'G','Z','P','F','R'}
F=['kod_vysledku','dodavatel','nazev_v_puvodnim_jazyce','druh','poddruh','obor','obor_oecd','rok_uplatneni','kod_duvernosti','popis_vysledku_v_puv._jazyce','popis_vysledku_anglicky','klicova_slova','ico','nazev_organizace','kategorie','pravni_forma','cislo_patentu_nebo_vzoru','nazev_vlastnika','druh_moznosti_vyuziti','technicke_parametry','ekonomicke_parametry','pozadavek_na_licencni_poplatek','zpusoby_vyuziti_vysledku','adresa_www_stranky_s_vysledkem','seznam_navaznosti_na_va']
out=open('data/roh/riv/riv_applied.jsonl','a')
for y in range(int(sys.argv[1]),int(sys.argv[2])+1):
    url=f'https://www.isvavai.cz/dokumenty/opendata/RIV-{y}.csv'
    try:
        r=urllib.request.urlopen(url,timeout=120)
    except Exception as e:
        print(y,'ERR',e,flush=True); continue
    rd=csv.DictReader(io.TextIOWrapper(r,encoding='utf-8',newline=''))
    n=k=0
    for row in rd:
        n+=1
        if row.get('druh') in KEEP:
            k+=1; out.write(json.dumps({f:row.get(f,'') for f in F},ensure_ascii=False)+'\n')
    out.flush(); print(y,'rows',n,'kept',k,flush=True)
