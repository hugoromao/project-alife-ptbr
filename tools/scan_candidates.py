"""List display-looking string literals in upstream files that have no translation entry yet."""
import json
import re
import sys
from pathlib import Path

from anchors import literals_with_context

from paths import ROOT, upstream_version_dir

UP = upstream_version_dir()
LOG = re.compile(r'(print|log|Log|error|debugLog|warn|DebugLog|trace|assert|require|getTexture|getSoundManager|playSound|sendClientCommand|sendServerCommand|Events)\b')


def translated(rel):
    f = ROOT / 'translations/lua' / (rel + '.json')
    return {(e['en'], e['ctx']) for e in json.loads(f.read_text(encoding='utf-8'))} if f.exists() else set()


def candidates(rel):
    src = (UP / rel).read_text(encoding='utf-8')
    done = translated(rel)
    for t, ctx in literals_with_context(src):
        v = t.value
        if (v, ctx) in done or LOG.search(ctx):
            continue
        if not re.search(r'[A-Za-z]{2,}', v):
            continue
        if re.fullmatch(r'[a-z]+[A-Z][A-Za-z0-9]*|[A-Z][a-z]+[A-Z][A-Za-z0-9]*|[a-z0-9_]+|[A-Z0-9_]+_[A-Z0-9_]+|[\w]+(\.[\w]+)+|[\w/.-]+/[\w/.-]+|Iso\w+|Base\.\w+', v):
            continue
        yield src.count('\n', 0, t.start) + 1, v, ctx


if __name__ == '__main__':
    for rel in sys.argv[1:]:
        rows = list(candidates(rel))
        print('#####', rel, len(rows))
        for line, v, ctx in rows:
            print(line, repr(v)[:160], '   [' + ctx[-38:] + ']')
