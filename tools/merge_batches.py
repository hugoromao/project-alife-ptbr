"""Merge work/pt_batch*.py dictionaries onto anchored entries and write
translations/lua/<path>.json. Entries already present in those files are kept
(hand edits win); new ones are appended.

Usage: python3 merge_batches.py [entries.json ...]
       (SCAN batches need no entries file; pass work/es_entries_clean.json only to
        redo the one-off bootstrap from the Spanish translation)
"""
import importlib.util
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'translations/lua'


def load_batches():
    pt, skip, scan = defaultdict(dict), defaultdict(list), []
    for f in sorted((ROOT / 'work').glob('pt_batch*.py')):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for name, d in mod.PT.items():
            pt[name].update(d)
        for name, pats in getattr(mod, 'SKIP_CTX', {}).items():
            skip[name].extend(pats)
        if getattr(mod, 'SCAN', False):
            scan.append((mod.PT, getattr(mod, 'DEFAULT_CTX', {})))
    return pt, skip, scan


def scan_entries(scan):
    """Create anchored entries by scanning upstream files for SCAN batch keys."""
    from anchors import literals_with_context
    from paths import upstream_version_dir
    up = upstream_version_dir()
    index = {p.name: p for p in up.rglob('*.lua')}
    entries = defaultdict(list)
    for table, default_ctx in scan:
        for name, keys in table.items():
            path = index.get(name)
            if path is None:
                print('SCAN: no upstream file', name)
                continue
            rel = str(path.relative_to(up))
            hit = set()
            for tok, ctx in literals_with_context(path.read_text(encoding='utf-8')):
                if name in default_ctx and not ctx.endswith(default_ctx[name]):
                    continue
                for key in keys:
                    en, _, suffix = key.partition('||')
                    if tok.value == en and ctx.endswith(suffix):
                        entries[rel].append({'en': en, 'ctx': ctx})
                        hit.add(key)
            for key in keys:
                if key not in hit:
                    print('SCAN: no match', name, repr(key))
    return entries


def lookup(table, en, ctx):
    for key, value in table.items():
        if '||' in key:
            k_en, k_ctx = key.split('||', 1)
            if k_en == en and ctx.endswith(k_ctx):
                return value, key
    if en in table:
        return table[en], en
    return None, None


def main():
    pt, skip, scan = load_batches()
    sources = [Path(p) for p in sys.argv[1:]]
    entries = defaultdict(list)
    for src in sources:
        for rel, xs in json.loads(src.read_text(encoding='utf-8')).items():
            entries[rel].extend(xs)
    for rel, xs in scan_entries(scan).items():
        entries[rel].extend(xs)

    used = defaultdict(set)
    missing = []
    for rel, xs in sorted(entries.items()):
        name = rel.split('/')[-1]
        table = pt.get(name, {})
        out_file = OUT / (rel + '.json')
        existing = json.loads(out_file.read_text(encoding='utf-8')) if out_file.exists() else []
        have = {(e['en'], e['ctx']) for e in existing}
        for e in xs:
            if (e['en'], e['ctx']) in have:
                _, key = lookup(table, e['en'], e['ctx'])
                used[name].add(key)
                continue
            if any(re.search(p, e['ctx']) for p in skip.get(name, [])):
                continue
            value, key = lookup(table, e['en'], e['ctx'])
            if value is None:
                missing.append((name, e['en'], e['ctx']))
                continue
            used[name].add(key)
            existing.append({'en': e['en'], 'ctx': e['ctx'], 'pt': value})
            have.add((e['en'], e['ctx']))
        if existing:
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(json.dumps(existing, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    for name, table in pt.items():
        for key in table:
            if key not in used[name]:
                print('UNUSED KEY', name, repr(key))
    for m in missing:
        print('NO PT', m[0], repr(m[1]), '[' + m[2] + ']')
    print('missing:', len(missing))


if __name__ == '__main__':
    main()
