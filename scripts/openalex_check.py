"""Fortsetzungscheck und Wiederbelebungs-Signal über OpenAlex (v0.3).

Drei Signale je Kandidat, alle nur Hinweise, kein Urteil:

A  Projektergebnisse: Arbeiten, die das Projekt als Förderung nennen (Filter awards.funder_award_id,
   klappt für FWF- und GA-ČR-Kürzel, für CORDIS-Nummern meist nicht). Dazu: Wie oft werden sie seit
   Projektende zitiert, und wie viele dieser Zitate kommen seit 2022 aus der KI-Forschung?
B  Weiterführung: spätere Arbeiten mit ähnlichem Thema ab Projektende, weltweit und zusätzlich nur
   von derselben Einrichtung. Ähnlichkeit zum Projektziel als Kosinus über Wortzählungen.
C  Wiederbelebung: Wie viele KI-Arbeiten (Teilgebiete Künstliche Intelligenz, Computer Vision)
   behandeln das Thema je Jahr? Steigend seit 2020 = Hinweis, dass das Hindernis jetzt angegangen wird.

Kosten (gemessen 9.11.2026): Filterabfrage 1 Credit, Suche 10 Credits; Tagesbudget 10.000 Credits.
Modus 'schnell' (Standard): A + weltweite Suche, rund 11 bis 13 Credits je Kandidat, also rund 750 pro Tag.
Modus 'voll': zusätzlich gleiche Einrichtung und Signal C, rund 30 bis 45 Credits; für die oberen Kandidaten.
Das Budget setzt sich um Mitternacht UTC zurück; ein abgebrochener Lauf macht am nächsten Tag weiter. Der Rest steht nach jedem
Aufruf in der Ausgabe (credits_rest).

Aufruf einzeln:
  python3 scripts/openalex_check.py --titel "..." --ziel "..." --ab 2013 [--foerderkennz GA13-10527S]
         [--einrichtung "Czech Technical University in Prague"] [--land CZ]
Aufruf als Liste (CSV mit Spalten id,titel,ziel,ab,foerderkennz,einrichtung,land[,begriffe]):
  python3 scripts/openalex_check.py --csv eingabe.csv --out ergebnisse/openalex_check.jsonl
Fortsetzbar: bereits vorhandene IDs in --out werden übersprungen.
Schlüssel: OPENALEX_API_KEY aus .env (wird nie ausgegeben).
"""
import os, re, csv, json, math, time, argparse, collections, urllib.request, urllib.parse, urllib.error

def _load_env():
    if os.path.exists('.env'):
        for line in open('.env'):
            if '=' in line and not line.lstrip().startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ.setdefault(k, v)
_load_env()
KEY = os.environ.get('OPENALEX_API_KEY', '')
API = 'https://api.openalex.org/'
KI_TEILGEBIETE = {'Artificial Intelligence', 'Computer Vision and Pattern Recognition'}
STOP = set('the of and in for to a an on with by from at as is are be this that using based new study '
           'analysis development research project system method methods its their into via'.split())
_rest = {'credits': None}
_inst_cache = {}

def get(path, params):
    params = dict(params)
    if KEY:
        params['api_key'] = KEY
    url = API + path + '?' + urllib.parse.urlencode(params)
    for versuch in range(3):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                _rest['credits'] = r.headers.get('x-ratelimit-remaining')
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and versuch < 2:
                time.sleep(5 * (versuch + 1)); continue
            raise

def toks(s):
    return [w for w in re.findall(r'[a-zA-ZÀ-ſ]{3,}', (s or '').lower()) if w not in STOP]

def cos(a, b):
    ca, cb = collections.Counter(a), collections.Counter(b)
    num = sum(ca[w] * cb[w] for w in ca if w in cb)
    den = math.sqrt(sum(v * v for v in ca.values())) * math.sqrt(sum(v * v for v in cb.values()))
    return num / den if den else 0.0

def abstract(ii):
    if not ii:
        return ''
    return ' '.join(w for _, w in sorted((p, w) for w, ps in ii.items() for p in ps))

def suchwort(titel, n=7):
    return ' '.join(toks(titel)[:n])

# --- Signal A ---------------------------------------------------------------
def projektergebnisse(kennz, ab):
    if not kennz:
        return None
    d = get('works', {'filter': f'awards.funder_award_id:{kennz}', 'per-page': 25,
                      'select': 'id,display_name,publication_year,cited_by_count'})
    werke = d.get('results', [])
    if not werke:
        return {'werke': 0}
    ids = '|'.join(w['id'].split('/')[-1] for w in werke[:20])
    nach = get('works', {'filter': f'cites:{ids},from_publication_date:{ab + 1}-01-01',
                         'group_by': 'publication_year'})
    pro_jahr = {int(g['key']): g['count'] for g in nach.get('group_by', []) if g['key'].isdigit()}
    ki = get('works', {'filter': f'cites:{ids},from_publication_date:2022-01-01',
                       'group_by': 'primary_topic.subfield.id'})
    ki_zit = sum(g['count'] for g in ki.get('group_by', []) if g['key_display_name'] in KI_TEILGEBIETE)
    return {'werke': len(werke), 'titel': [w['display_name'] for w in werke[:5]],
            'zitate_nach_ende': sum(pro_jahr.values()), 'zitate_seit_2022': sum(v for k, v in pro_jahr.items() if k >= 2022),
            'davon_ki_seit_2022': ki_zit, 'letztes_zitierjahr': max(pro_jahr) if pro_jahr else None}

# --- Signal B ---------------------------------------------------------------
def einrichtung_id(name):
    if not name:
        return None
    if name not in _inst_cache:
        d = get('institutions', {'search': name, 'per-page': 1, 'select': 'id,display_name'})
        r = d.get('results', [])
        _inst_cache[name] = (r[0]['id'].split('/')[-1], r[0]['display_name']) if r else None
    return _inst_cache[name]

def _suche(titel, ref, flt, n=7):
    d = get('works', {'search': suchwort(titel, n), 'filter': ','.join(flt), 'per-page': 25,
                      'select': 'id,display_name,publication_year,abstract_inverted_index,authorships,cited_by_count'})
    treffer = []
    for w in d.get('results', []):
        txt = (w.get('display_name') or '') + ' ' + abstract(w.get('abstract_inverted_index'))
        insts = sorted({i.get('display_name', '') for a in w.get('authorships', []) for i in a.get('institutions', [])})[:3]
        treffer.append({'sim': round(cos(ref, toks(txt)), 3), 'jahr': w.get('publication_year'),
                        'titel': w.get('display_name'), 'id': w.get('id'), 'einrichtungen': insts})
    treffer.sort(key=lambda h: -h['sim'])
    return d.get('meta', {}).get('count'), treffer[:3]

def weiterfuehrung(titel, ziel, ab, einrichtung=None, land=None, mit_einrichtung=True, begriffe=None):
    """Weltweit und, wenn bekannt, zusätzlich nur in derselben Einrichtung (findet beides:
    Weiterführung durch andere, z. B. dapE in Chicago, und durch die eigene Gruppe)."""
    ref = toks(titel + ' ' + ziel)
    basis = [f'from_publication_date:{ab}-01-01']
    n_welt, welt = _suche(titel, ref, basis)
    grundlage = 'Titel, 7 Wörter'
    # A07: 0 Treffer heißt meist zu viele Suchwörter (Akronyme, Landessprache), nicht "nicht weitergeführt".
    if not n_welt:
        n_welt, welt = _suche(titel, ref, basis, 4); grundlage = 'Titel, 4 Wörter'
    if not n_welt and begriffe:
        n_welt, welt = _suche(begriffe.replace(';', ' '), ref, basis, 5); grundlage = 'Begriffe'
    res = {'weltweit': {'treffer_gesamt': n_welt, 'top3': welt, 'grundlage': grundlage}}
    if not n_welt:
        res['abfrage_fehlgeschlagen'] = True
    inst = einrichtung_id(einrichtung) if mit_einrichtung else None
    if inst:
        n_e, eig = _suche(titel, ref, basis + [f'authorships.institutions.id:{inst[0]}'])
        res['gleiche_einrichtung'] = {'einrichtung': inst[1], 'treffer_gesamt': n_e, 'top3': eig}
    sims = [t[0]['sim'] for t in (welt, res.get('gleiche_einrichtung', {}).get('top3')) if t]
    res['top_sim'] = max(sims) if sims else 0.0
    return res

# --- Signal C ---------------------------------------------------------------
def wiederbelebung(titel, begriffe=None):
    """Begriffe am besten aus Haikus Feld suchbegriffe_en (Fachbegriffe). Ohne Begriffe nimmt das Skript
    drei Titelwörter; das ist grob und erzeugt Fehlalarme bei Allerweltswörtern."""
    if begriffe:
        q = ' OR '.join('"%s"' % b.strip() for b in begriffe.split(';') if b.strip())
        quelle = 'Begriffe'
    else:
        q = suchwort(titel, 3); quelle = 'Titelwörter (grob)'
    d = get('works', {'filter': f'title_and_abstract.search:{q},'
                                f'primary_topic.subfield.id:1702|1707,from_publication_date:2012-01-01',
                      'group_by': 'publication_year'})
    pro_jahr = {int(g['key']): g['count'] for g in d.get('group_by', []) if g['key'].isdigit()}
    vorher = sum(v for k, v in pro_jahr.items() if 2016 <= k <= 2019) / 4
    nachher = sum(v for k, v in pro_jahr.items() if 2022 <= k <= 2025) / 4
    return {'grundlage': quelle, 'ki_arbeiten_pro_jahr_2016_19': round(vorher, 1),
            'ki_arbeiten_pro_jahr_2022_25': round(nachher, 1),
            'anstieg': round(nachher / vorher, 1) if vorher else ('neu' if nachher else None)}

def hinweis(a, b):
    teile = []
    if a and a.get('werke'):
        teile.append(f"{a['werke']} Projektarbeiten, {a.get('zitate_seit_2022', 0)} Zitate seit 2022")
    if b.get('abfrage_fehlgeschlagen'):
        teile.append('Abfrage fehlgeschlagen (0 Treffer), NICHT als nicht weitergeführt werten')
        return '; '.join(teile)
    s = b['top_sim']
    teile.append('Thema vermutlich weitergeführt, prüfen' if s >= 0.35 else
                 'Weiterführung unklar, prüfen' if s >= 0.2 else 'kein Hinweis auf Weiterführung')
    return '; '.join(teile)

def check(titel, ziel, ab, kennz=None, einrichtung=None, land=None, begriffe=None, modus='schnell'):
    """modus 'schnell': A + weltweite Suche, rund 11 bis 13 Credits (rund 750 Kandidaten/Tag).
    modus 'voll': zusätzlich gleiche Einrichtung und Wiederbelebung, rund 30 bis 45 Credits."""
    voll = modus == 'voll'
    a = projektergebnisse(kennz, ab)
    b = weiterfuehrung(titel, ziel, ab, einrichtung, land, mit_einrichtung=voll, begriffe=begriffe)
    c = wiederbelebung(titel, begriffe) if voll else None
    return {'hinweis': hinweis(a, b), 'A_projektergebnisse': a, 'B_weiterfuehrung': b,
            'C_wiederbelebung': c, 'credits_rest': _rest['credits']}

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--titel'); ap.add_argument('--ziel', default=''); ap.add_argument('--ab', type=int)
    ap.add_argument('--foerderkennz'); ap.add_argument('--einrichtung'); ap.add_argument('--land')
    ap.add_argument('--begriffe', help='Fachbegriffe, mit Semikolon getrennt')
    ap.add_argument('--modus', choices=['schnell', 'voll'], default='schnell')
    ap.add_argument('--csv'); ap.add_argument('--out', default='ergebnisse/openalex_check.jsonl')
    ap.add_argument('--min-credits', type=int, default=200, help='bricht ab, wenn weniger Credits übrig sind')
    a = ap.parse_args()
    if not a.csv:
        print(json.dumps(check(a.titel, a.ziel, a.ab, a.foerderkennz, a.einrichtung, a.land, a.begriffe, a.modus), ensure_ascii=False, indent=1))
    else:
        fertig = set()
        if os.path.exists(a.out):
            fertig = {json.loads(l)['id'] for l in open(a.out) if l.strip()}
        with open(a.out, 'a') as out:
            for r in csv.DictReader(open(a.csv, encoding='utf-8')):
                if r['id'] in fertig:
                    continue
                if _rest['credits'] and int(_rest['credits']) < a.min_credits:
                    print('Tagesbudget fast aufgebraucht, Abbruch. Morgen erneut starten, es geht dort weiter.'); break
                try:
                    res = check(r['titel'], r.get('ziel', ''), int(r['ab']), r.get('foerderkennz') or None,
                                r.get('einrichtung') or None, r.get('land') or None, r.get('begriffe') or None, a.modus)
                except Exception as e:
                    res = {'fehler': repr(e)}
                res['id'] = r['id']
                out.write(json.dumps(res, ensure_ascii=False) + '\n'); out.flush()
                print(r['id'], res.get('hinweis', res.get('fehler')), '| Credits übrig:', _rest['credits'])
