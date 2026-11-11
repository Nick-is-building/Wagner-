"""Fable 5.2 für A07 (Muster-Suche). BEZAHLT (Freigabe 2026-11-11-A07b, Obergrenze 6 $ für beide Teile zusammen).

  tiefe: Tiefenprüfung der oberen --anzahl (Standard 8), höchstens --suchen Websuchen -> ergebnisse/fable_a07_tiefe.jsonl
  frei:  ein Aufruf über die oberen 40 (ohne Websuche): Verbindungen und neue Ansätze -> ergebnisse/fable_a07_frei.jsonl
Aufruf:
  python3 scripts/bezahlt/fable_a07.py tiefe --freigabe 2026-11-11-A07b --max-usd 6 --reserve-usd 1.4
  python3 scripts/bezahlt/fable_a07.py frei  --freigabe 2026-11-11-A07b --max-usd 6
Eingabe: ergebnisse/a07_obere40.jsonl (scripts/a07_rangliste.py --mit-openalex).
Aufbau wie scripts/bezahlt/fable_a06.py; neu: Urteil ja/nein, erster Schritt mit Kosten und Zahler, Urteil über Pflicht-Nullen.
"""
import argparse, asyncio, json, sys
sys.path.insert(0, 'scripts/bezahlt')
import api_lauf as L

MODELL = 'claude-fable-5-2'
AUS = {'frei': 'ergebnisse/fable_a07_frei.jsonl', 'tiefe': 'ergebnisse/fable_a07_tiefe.jsonl'}
BETAS = ['server-side-fallback-2026-07-01']


def katalog():
    k = open('docs/03_faehigkeiten_katalog.md', encoding='utf-8').read()
    return k[k.index('## Querschnitts-Fähigkeiten'):k.index('## Methoden')]


NICK = ('Nick ist eine Person in Deutschland ohne eigenes Labor; er arbeitet mit KI-Werkzeugen, kann Software, '
        'Simulation und Datenanalyse machen und kleine Prototypen mit Teilen aus Deutschland für rund 1.000 € '
        'Material in einigen Wochen bauen. Gesucht ist Forschung, die früher abgebrochen oder nicht weitergeführt '
        'wurde und deren damaliges Hindernis heute mit KI oder günstiger Rechenleistung lösbar ist. Diese Runde sucht '
        'gezielt das Muster: Messdaten oder Prototyp vorhanden, Modell, Auswertung oder Optimierung fehlt.')

TIEFE = f"""Du prüfst einen Kandidaten für Nick gründlich und lösungsorientiert. {NICK}
Ein Hindernis ist eine Aufgabe, kein Ausschlussgrund. Verwirf nur bei Widerlegung oder vollständiger Lösung durch andere, mit Beleg.
Du darfst bis zu 3 Websuchen machen. Belege nur aus Quellen, die du in diesem Aufruf tatsächlich geöffnet oder als
Suchergebnis gesehen hast, mit URL; sonst schreibe "unbelegt". Zitate aus dem Originaltext wörtlich.
Sonnet hat Pflichtkriterien bewertet; "pflicht_nullen" nennt, wo Sonnet null gab (K2 Grund, warum es liegen
blieb, oder ausdrücklich offener Schritt; K11 eigenständiger Vorteil; K12 für Nick umsetzbar).
Beantworte:
1. Noch offen oder von anderen gelöst? (offen | teilweise gelöst | gelöst | unklar), mit Beleg.
2. Passt das Muster (Messdaten oder Prototyp vorhanden, Modell/Auswertung/Optimierung fehlt)? Mit Zitat.
3. Welche konkrete Eigenschaft der damaligen Entwicklung gibt heute einen eigenen Vorteil? Mit Zitat.
4. Pflicht-Nullen: Für K2, K11 und K12 je: Hältst du Sonnets Wert (null oder nicht null) für richtig? Ein Satz Grund.
5. Konkreter erster Schritt mit Nicks Mitteln, 2 bis 4 Wochen: was genau, Kosten in Euro, und wer dafür zahlen
   würde (Nick selbst, ein Förderprogramm mit Namen, ein Kunde/Anwender, ein Partner). Mit Beleg oder "unbelegt".
6. Wer würde später für das Ergebnis zahlen? Mit Beleg oder "unbelegt".
7. Entscheidende offene Annahme und der schnellste Test dafür.
8. Klare Antwort: weiterverfolgen ja oder nein, mit Hauptgrund. Kein "mit Vorbehalt".
Antworte am Ende mit genau einem JSON-Objekt (Deutsch, sachlich, kurze Sätze):
{{"noch_offen":{{"stand":"offen|teilweise gelöst|gelöst|unklar","beleg":"...","url":"...|null"}},
"muster":{{"passt":"ja|teilweise|nein","vorhanden":"...","fehlt":"...","zitat":"..."}},
"vorteil":{{"satz":"...","zitat":"..."}},
"pflicht":{{"k2":{{"sonnet_richtig":true,"grund":"..."}},"k11":{{"sonnet_richtig":true,"grund":"..."}},"k12":{{"sonnet_richtig":true,"grund":"..."}}}},
"erster_schritt":{{"satz":"...","kosten_eur":0,"dauer_wochen":0,"zahler":"...","zahler_url":"...|unbelegt"}},
"heute":{{"entwicklung":"was das Hindernis heute beseitigt","url":"...|unbelegt"}},
"markt":{{"wer":"...","url":"...|unbelegt"}},"annahme":{{"satz":"...","test":"..."}},
"rechte_unterlagen":"...","dafuer":"...","dagegen":"...",
"weiterverfolgen":"ja|nein","grund":"Hauptgrund in einem Satz","kurztitel":"höchstens 6 Wörter"}}"""

FREI = f"""Du bekommst die oberen 40 Kandidaten einer gezielten Suche für Nick. {NICK}
Jeder Kandidat hat ID, Pool, Titel, Haiku-Felder (Zitate wörtlich aus dem Text), Sonnet-Bewertung mit Merkmal M
(Muster), Pflicht-Nullen, Abzügen und den OpenAlex-Fortsetzungscheck ("Abfrage fehlgeschlagen" heißt: unbekannt).
Suche mit eigenem Blick über alle zusammen nach:
1. Verbindungen: dasselbe Hindernis, dieselbe Messgröße oder dasselbe fehlende Modell in mehreren Projekten,
2. Teilergebnissen oder Datensätzen, die sich ergänzen,
3. einem heutigen Werkzeug, das mehrere alte Projekte zugleich löst,
4. neuen Ansätzen oder Geschäftsideen, die erst aus der Kombination entstehen, auch wenn kein Einzelfall stark ist.
Kennzeichne alles als Vermutung, mit wörtlichem Zitat aus dem Material und Projekt-ID.
Schreibe Markdown mit den Abschnitten: "## Verbindungen" (nummeriert: Vermutung, Projekte mit IDs, Zitate,
warum es zählt), "## Neue Ansätze" (nummeriert: Idee, Projekte, erster Schritt mit Kosten in Euro, wer zahlen würde),
"## Die drei stärksten Funde" (je zwei Sätze). Deutsch, sachlich, kurze Sätze."""


def kandidat_text(k, voll=True):
    s = k['sonnet']
    teile = [f"ID: {k['id']} · Pool: {k['pool']} · Rang {k['rang']} · Sonnet-Summe {s.get('summe')} · "
             f"pflicht_nullen: {', '.join(k.get('pflicht_nullen') or []) or 'keine'}", f"Titel: {k['titel']}"]
    if voll:
        teile.append(f"Originaltext:\n{k['text']}")
    h = {x: y for x, y in k['haiku'].items() if y not in (None, [], '')}
    teile.append('Haiku: ' + json.dumps(h, ensure_ascii=False))
    sv = {x: s.get(x) for x in ('k1', 'k2', 'k14', 'm', 'abzug', 'punkte', 'vorteil', 'erster_schritt', 'werkzeug_heute', 'markt_wer', 'annahme', 'ausschluss', 'warnung')}
    teile.append('Sonnet: ' + json.dumps(sv, ensure_ascii=False))
    teile.append('OpenAlex (Hinweis, kein Urteil): ' + json.dumps(k.get('openalex') or 'kein Ergebnis', ensure_ascii=False)[:1500 if voll else 400])
    return '\n'.join(teile)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('teil', choices=['frei', 'tiefe'])
    ap.add_argument('--anzahl', type=int, default=8)
    ap.add_argument('--suchen', type=int, default=3)
    ap.add_argument('--freigabe'); ap.add_argument('--max-usd', type=float)
    ap.add_argument('--reserve-usd', type=float, default=0.0, help='für den anderen Teil freihalten')
    ap.add_argument('--parallel', type=int, default=10)
    ap.add_argument('--worst-usd', type=float, help='ungünstigste Kosten je Aufruf, aus Messung (statt Schätzformel)')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    ks = [json.loads(l) for l in open('ergebnisse/a07_obere40.jsonl', encoding='utf-8')]
    bisher = sum(L.lies(p)[1] for p in AUS.values())
    aus = AUS[a.teil]
    fertig, _ = L.lies(aus)
    pin, pout = L.PREISE[MODELL]
    kat = katalog()
    if a.teil == 'frei':
        inhalt = '\n\n---\n\n'.join(kandidat_text(k, voll=False) for k in ks)
        aufgaben = [] if 'frei' in fertig else [{'id': 'frei', 'params': {
            'max_tokens': 32000, 'betas': BETAS, 'fallbacks': 'default', 'output_config': {'effort': 'high'},
            'system': [{'type': 'text', 'text': FREI}, {'type': 'text', 'text': 'Fähigkeiten-Katalog:\n\n' + kat}],
            'messages': [{'role': 'user', 'content': inhalt}]}}]
        worst = lambda x: (L.tok(FREI + kat + inhalt) * pin + 20000 * pout) / 1e6
        json_erw = False
    else:
        wahl = [k for k in ks[:a.anzahl] if k['id'] not in fertig]
        tools = [{'type': 'web_search_20260209', 'name': 'web_search', 'max_uses': a.suchen}]
        aufgaben = [{'id': k['id'], 'params': {
            'max_tokens': 32000, 'betas': BETAS, 'fallbacks': 'default', 'output_config': {'effort': 'medium'},
            'tools': tools,
            'system': [{'type': 'text', 'text': TIEFE},
                       {'type': 'text', 'text': 'Fähigkeiten-Katalog:\n\n' + kat, 'cache_control': {'type': 'ephemeral'}}],
            'messages': [{'role': 'user', 'content': kandidat_text(k)}]}} for k in wahl]
        # ungünstig: Material + 3 Suchen à 15.000 Token Ergebnisse, zweimal gelesen, 12.000 Token Ausgabe
        worst = lambda x: ((L.tok(TIEFE + kat + x['params']['messages'][0]['content']) + a.suchen * 15000) * 2 * pin
                           + 12000 * pout) / 1e6 + a.suchen * L.WEBSUCHE_USD
        json_erw = True
    if a.worst_usd:
        worst = lambda x: a.worst_usd
    if a.dry_run:
        print(f'Trockenlauf Fable {a.teil}: {len(aufgaben)} Aufrufe, ungünstigster Fall {sum(worst(x) for x in aufgaben):.2f} $; '
              f'bisher unter A07b {bisher:.4f} $')
        return
    L.pruefe_start(a)

    def auswerten(z, antworten):
        fb = [b for r in antworten for b in r.content if b.type == 'fallback']
        if fb:
            z['_fallback'] = [f'{b.from_.model} -> {b.to.model}' for b in fb]
        z['_websuchen'] = sum(1 for r in antworten for b in r.content if b.type == 'server_tool_use')
        z['_quellen'] = sorted({c.url for r in antworten for b in r.content if b.type == 'web_search_tool_result'
                                and isinstance(b.content, list) for c in b.content if getattr(c, 'url', None)})[:40]
        if a.teil == 'tiefe' and '_fehler' not in z:
            z['_text'] = ''.join(b.text for b in antworten[-1].content if b.type == 'text')

    asyncio.run(L.lauf(aufgaben, aus, modell=MODELL, max_usd=a.max_usd - a.reserve_usd, bisher_usd=bisher,
                       worst_usd=worst, parallel=a.parallel, beta=True, auswerten=auswerten, json_erwartet=json_erw))


if __name__ == '__main__':
    main()
