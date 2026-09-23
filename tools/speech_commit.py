"""Validate a translated batch and save it, so no finished work is ever lost.

  python3 speech_commit.py <batch.txt> [--no-push]

<batch.txt> has one "id<TAB>portuguese" line per entry of work/queue_current.json
(printed by speech_queue.py next). Valid lines are written to
translations/speech/<source>/NNN.json, PROGRESS.md stats are refreshed, and the
result is committed and pushed. Invalid lines are reported and left out.
"""
import json
import re
import subprocess
import sys
from collections import Counter

from paths import ROOT
from speech_queue import SPEECH_DIR, extract, stats, translated

PLACEHOLDER = re.compile(r'\{[a-z]+\}')
BRACKETED = re.compile(r'^\s*\[[^\]]+\]\s*$')
ASCII_FIX = {'’': "'", '‘': "'", '“': '"', '”': '"', '…': '...', '—': '--', '–': '-'}


def clean(text):
    for a, b in ASCII_FIX.items():
        text = text.replace(a, b)
    return text.strip()


def problems(en, pt):
    out = []
    if not pt:
        out.append('vazio')
    if Counter(PLACEHOLDER.findall(en)) != Counter(PLACEHOLDER.findall(pt)):
        out.append('marcações diferentes: %s vs %s' % (PLACEHOLDER.findall(en), PLACEHOLDER.findall(pt)))
    bad = sorted({c for c in pt if ord(c) > 0xFF or (ord(c) < 32 and c != '\n')})
    if bad:
        out.append('caracteres fora do Latin-1: %r' % bad)
    if bool(BRACKETED.match(en)) != bool(BRACKETED.match(pt)):
        out.append('colchetes de legenda diferentes')
    return out


def update_progress():
    rows = stats(extract(), translated())
    lines = ['<!-- stats -->', '| Fonte | Traduzidas | Total | % |', '|---|---:|---:|---:|']
    for source, ok, total, _ in rows:
        lines.append(f'| {source} | {ok} | {total} | {100 * ok / max(1, total):.1f}% |')
    lines.append('<!-- /stats -->')
    path = ROOT / 'PROGRESS.md'
    text = path.read_text(encoding='utf-8')
    block = '\n'.join(lines)
    if '<!-- stats -->' in text:
        text = re.sub(r'<!-- stats -->.*?<!-- /stats -->', block, text, flags=re.S)
    else:
        text = text.replace('## Etapas', '## Situação\n\n' + block + '\n\n## Etapas', 1)
    path.write_text(text, encoding='utf-8')
    return rows


def main():
    batch_file = sys.argv[1]
    push = '--no-push' not in sys.argv
    queue = json.loads((ROOT / 'work/queue_current.json').read_text(encoding='utf-8'))
    source, items = queue['source'], queue['items']
    result, errors = {}, []
    for raw in open(batch_file, encoding='utf-8').read().splitlines():
        if not raw.strip() or raw.startswith('#'):
            continue
        tid, _, pt = raw.partition('\t')
        tid, pt = tid.strip(), clean(pt.replace('\\n', '\n'))
        if tid not in items:
            errors.append(f'{tid}: id fora da fila')
            continue
        issues = problems(items[tid], pt)
        if issues:
            errors.append(f'{tid}: {"; ".join(issues)} :: {items[tid]!r} -> {pt!r}')
            continue
        result[items[tid]] = pt
    missing = [tid for tid, en in items.items() if en not in result]
    if result:
        out_dir = SPEECH_DIR / source
        out_dir.mkdir(parents=True, exist_ok=True)
        n = len(list(out_dir.glob('*.json'))) + 1
        out = out_dir / f'{n:03d}.json'
        out.write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        rows = update_progress()
        summary = ', '.join(f'{s} {ok}/{total}' for s, ok, total, _ in rows)
        subprocess.run(['git', 'add', str(out), 'PROGRESS.md'], cwd=ROOT, check=True)
        subprocess.run(['git', 'commit', '-q', '-m', f'Falas: {source} lote {n:03d} ({len(result)} linhas)\n\n{summary}\n\n'
                        'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'], cwd=ROOT, check=True)
        if push:
            subprocess.run(['git', 'pull', '-q', '--rebase'], cwd=ROOT, check=False)
            subprocess.run(['git', 'push', '-q'], cwd=ROOT, check=False)
        print(f'salvo {out.relative_to(ROOT)}: {len(result)} linhas | {summary}')
    for e in errors:
        print('ERRO', e)
    if missing:
        print(f'{len(missing)} linhas da fila sem tradução válida (continuam na fila)')


if __name__ == '__main__':
    main()
