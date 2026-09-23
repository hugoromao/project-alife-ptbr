"""Align the Spanish override files against the current upstream files and report
(a) string literals the Spanish version changed in place and (b) code regions that
differ structurally and need a human look. One-off helper for bootstrapping PT-BR."""
import difflib
import json
import sys
from pathlib import Path

from lualex import code_tokens, line_of

from paths import ROOT, upstream_version_dir

UP = upstream_version_dir()
ES = ROOT / 'reference/ProjectALifeNPCs_ES/42'


def key(t):
    return ('S',) if t.kind in ('string', 'longstring') else (t.kind, t.text)


def main():
    pairs, structural = [], []
    for es_file in sorted(ES.rglob('*.lua')):
        rel = es_file.relative_to(ES)
        up_file = UP / rel
        us = up_file.read_text(encoding='utf-8')
        es = es_file.read_text(encoding='utf-8')
        ut, et = code_tokens(us), code_tokens(es)
        sm = difflib.SequenceMatcher(None, [key(t) for t in ut], [key(t) for t in et], autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                for a, b in zip(ut[i1:i2], et[j1:j2]):
                    if a.kind in ('string', 'longstring') and a.value != b.value:
                        pairs.append({'file': str(rel), 'line': line_of(us, a.start),
                                      'en': a.value, 'es': b.value})
            else:
                u_lo = line_of(us, ut[i1].start) if i1 < len(ut) else line_of(us, len(us))
                u_hi = line_of(us, ut[i2 - 1].end) if i2 > i1 else u_lo
                e_lo = line_of(es, et[j1].start) if j1 < len(et) else line_of(es, len(es))
                e_hi = line_of(es, et[j2 - 1].end) if j2 > j1 else e_lo
                structural.append({'file': str(rel), 'tag': tag,
                                   'up': us[ut[i1].start:ut[i2 - 1].end] if i2 > i1 else '',
                                   'es': es[et[j1].start:et[j2 - 1].end] if j2 > j1 else '',
                                   'up_lines': [u_lo, u_hi], 'es_lines': [e_lo, e_hi]})
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'work'
    out.mkdir(exist_ok=True)
    (out / 'es_pairs.json').write_text(json.dumps(pairs, ensure_ascii=False, indent=1), encoding='utf-8')
    (out / 'es_structural.json').write_text(json.dumps(structural, ensure_ascii=False, indent=1), encoding='utf-8')
    print(len(pairs), 'string pairs,', len(structural), 'structural regions')


if __name__ == '__main__':
    main()
