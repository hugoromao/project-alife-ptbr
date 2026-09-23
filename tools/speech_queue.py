"""Queue of NPC speech to translate.

Extracts every spoken line from the upstream dialogue data (barks, talk replies,
scenes, radio), gives each unique English text a stable short id, and prints the
next untranslated lines with their context so a batch can be translated as
"id<TAB>portuguese" lines.

  python3 speech_queue.py stats
  python3 speech_queue.py next <source> [count]   # source: barks | talk | scenes | radio
      writes work/queue_current.json (id -> English) for speech_commit.py

Translations live in translations/speech/<source>/NNN.json as {english: portuguese}.
"""
import hashlib
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

from lualex import tokenize
from paths import ROOT, upstream_version_dir

SPEECH_DIR = ROOT / 'translations/speech'
SOURCES = ('barks', 'talk', 'scenes', 'radio')


def text_id(text):
    return hashlib.sha1(text.encode('utf-8')).hexdigest()[:7]


def short_gate(gate):
    parts = []
    for part in gate.split('|'):
        k, _, v = part.partition('=')
        if k in ('reg', 'role', 'st', 'sex', 'tmp', 'mood'):
            parts.append(f'{k}={v}')
    return ' '.join(parts)


def _calls(path, names):
    """Yield (name, tokens) for each top-level data call line like b(...), r(...)."""
    for line in path.read_text(encoding='utf-8').splitlines():
        m = re.match(r'^(%s)\(' % '|'.join(names), line)
        if m:
            yield m.group(1), [t for t in tokenize(line) if t.kind != 'comment']


def extract():
    """Return OrderedDict source -> list of units; a unit is a list of (en, context)."""
    data = upstream_version_dir() / 'media/lua/shared/ProjectALife/Dialogue/Data'
    out = OrderedDict((s, []) for s in SOURCES)
    for f in sorted(data.glob('ALifeDialogue_barks_*.lua')):
        for _, toks in _calls(f, ['b']):
            s = [t.value for t in toks if t.kind == 'string']
            out['barks'].append([(s[1], f'{s[0]} | {short_gate(s[2]) if len(s) > 2 else ""}')])
    for f in sorted(data.glob('ALifeDialogue_talk_*.lua')):
        for name, toks in _calls(f, ['r', 'y', 'n']):
            strs = [t for t in toks if t.kind == 'string']
            intent, text = strs[0].value, strs[1].value
            gate = strs[2].value if len(strs) > 2 else ''
            kind = {'r': 'reply', 'y': 'yes', 'n': 'no'}[name]
            unit = [(text, f'{kind} {intent} | {short_gate(gate)}')]
            for i, t in enumerate(toks):
                if t.kind == 'string' and i >= 2 and toks[i - 1].text == '=' and toks[i - 2].text == 't':
                    unit.append((t.value, '   ...continuação'))
            out['talk'].append(unit)
    for f in sorted(data.glob('ALifeDialogue_scenes_*.lua')):
        for _, toks in _calls(f, ['s']):
            args = [t for t in toks if t.kind in ('string', 'number', 'name')][1:]
            sid, topic, gate = args[0].value, args[1].value, args[3].value
            unit = []
            rest = args[4:]
            for i in range(0, len(rest) - 1, 2):
                unit.append((rest[i + 1].value, f'{sid} ({topic}; {short_gate(gate)}) fala {rest[i].text}'))
            out['scenes'].append(unit)
    for f in sorted(data.glob('ALifeDialogue_radio_*.lua')):
        for _, toks in _calls(f, ['seg']):
            strs = [t.value for t in toks if t.kind == 'string']
            sid, kind, rest = strs[0], strs[1], strs[2:]
            unit = [(rest[i + 1], f'{sid} ({kind}) {rest[i]}') for i in range(0, len(rest) - 1, 2)]
            out['radio'].append(unit)
    return out


def translated():
    done = {}
    for f in sorted(SPEECH_DIR.rglob('*.json')):
        done.update(json.loads(f.read_text(encoding='utf-8')))
    return done


def stats(units_by_source, done):
    rows = []
    seen = set()
    for source, units in units_by_source.items():
        texts = OrderedDict()
        for unit in units:
            for en, _ in unit:
                texts[en] = True
        total = len(texts)
        ok = sum(1 for en in texts if en in done)
        words = sum(len(en.split()) for en in texts)
        rows.append((source, ok, total, words))
        seen.update(texts)
    return rows


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'stats'
    units_by_source = extract()
    done = translated()
    if cmd == 'stats':
        for source, ok, total, words in stats(units_by_source, done):
            print(f'{source:8s} {ok:6d}/{total:<6d} {100 * ok / max(1, total):5.1f}%  ({words} palavras)')
        return
    if cmd == 'next':
        source = sys.argv[2]
        count = int(sys.argv[3]) if len(sys.argv) > 3 else 150
        queue, printed = OrderedDict(), 0
        for unit in units_by_source[source]:
            pending = [(en, ctx) for en, ctx in unit if en not in done and en not in queue]
            if not pending:
                continue
            if printed >= count:
                break
            for en, ctx in unit:
                if en in done or en in queue:
                    continue
                queue[en] = True
                print(f'{text_id(en)}\t[{ctx}]\t{en}')
                printed += 1
        (ROOT / 'work').mkdir(exist_ok=True)
        (ROOT / 'work/queue_current.json').write_text(json.dumps(
            {'source': source, 'items': {text_id(en): en for en in queue}}, ensure_ascii=False, indent=0), encoding='utf-8')
        print(f'# {printed} linhas; responda com "id<TAB>tradução" e rode speech_commit.py', file=sys.stderr)


if __name__ == '__main__':
    main()
