"""Re-anchor stale translation entries after an upstream update.

An entry is stale when no literal in the new upstream file has its (text, context).
Usually the text is still there and only nearby code moved. For each file, stale
entries are grouped by English text; when the new file has exactly as many untranslated
occurrences of that text as there are stale entries, they are re-anchored in order.
Anything else is printed for a human decision.

Stale entries whose text is still present but already covered by other entries are
duplicates; entries whose text is gone from upstream are obsolete. Both are dropped
with --write.

Usage: python3 reanchor.py          (dry run)
       python3 reanchor.py --write  (update translations/lua/*.json)
"""
import json
import sys
from collections import defaultdict

from anchors import literals_with_context
from paths import ROOT, upstream_version_dir


def main():
    write = '--write' in sys.argv
    up = upstream_version_dir()
    fixed = ambiguous = gone = 0
    for jf in sorted((ROOT / 'translations/lua').rglob('*.json')):
        rel = str(jf.relative_to(ROOT / 'translations/lua'))[:-len('.json')]
        entries = json.loads(jf.read_text(encoding='utf-8'))
        path = up / rel
        if not path.exists():
            print(f'GONE FILE {rel}')
            gone += len(entries)
            continue
        lits = list(literals_with_context(path.read_text(encoding='utf-8')))
        present = {(t.value, ctx) for t, ctx in lits}
        taken = {(e['en'], e['ctx']) for e in entries if (e['en'], e['ctx']) in present}
        stale = defaultdict(list)
        for e in entries:
            if (e['en'], e['ctx']) not in present:
                stale[e['en']].append(e)
        changed = False
        drop = set()
        for en, group in stale.items():
            free = [ctx for t, ctx in lits if t.value == en and (en, ctx) not in taken]
            # identical contexts collapse to one anchor
            free = list(dict.fromkeys(free))
            if not free:
                present_text = any(t.value == en for t, _ in lits)
                print(f'{"DUPLICATE" if present_text else "GONE"} {rel}: {en!r}')
                gone += len(group)
                drop.update(id(e) for e in group)
                changed = True
            elif len(free) == len(group) or (len(group) == 1 and len({g["pt"] for g in group}) == 1 and len(free) == 1):
                for e, ctx in zip(group, free):
                    print(f'MOVE {rel}: {en!r}\n     [{e["ctx"]}] -> [{ctx}]')
                    e['ctx'] = ctx
                    taken.add((en, ctx))
                    fixed += 1
                    changed = True
            else:
                ambiguous += len(group)
                print(f'AMBIGUOUS {rel}: {en!r}: {len(group)} stale, {len(free)} candidates')
                for ctx in free:
                    print(f'     candidate [{ctx}]')
        if changed and write:
            entries = [e for e in entries if id(e) not in drop]
            jf.write_text(json.dumps(entries, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'moved {fixed}, ambiguous {ambiguous}, dropped (gone/duplicate) {gone}' + ('' if write else '  (dry run; --write to apply)'))


if __name__ == '__main__':
    main()
