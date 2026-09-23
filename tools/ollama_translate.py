"""Translate the speech queue with a local Ollama model, committing as it goes.

  setsid nohup python3 tools/ollama_translate.py scenes radio --model gemma3:12b > work/ollama.log 2>&1 &
  touch work/STOP        # stop after the current batch

Units (a scene, a radio segment) are sent whole, up to CHUNK lines per request, so the
model sees the dialogue. Each answer item echoes the first words of its English line;
items that do not line up, keep English or leave the Latin-1 range are dropped and stay
in the queue. Every BATCH lines go through speech_commit.py (validation, commit, push).
Lines the checks find doubtful are listed in work/review_<source>.tsv for review.
"""
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT
from speech_queue import extract, text_id, translated
from parallel_translate import SYSTEM

WORK = ROOT / 'work'
CHUNK = 20
BATCH = 200
URL = 'http://localhost:11434/api/chat'
ENGLISH = re.compile(r"\b(the|and|you|your|what|with|this|that|don't|I'm|it's|we're|they|there|here|just|gonna)\b",
                     re.I)


def log(message):
    print(time.strftime('%H:%M:%S'), message, flush=True)


def words(text, n=3):
    return ' '.join(re.findall(r"[a-z0-9']+", text.lower())[:n])


def ask(model, lines):
    numbered = '\n'.join(f'{i + 1}. [{ctx}] {en}' for i, (ctx, en) in enumerate(lines))
    prompt = (f'Traduza as {len(lines)} falas numeradas abaixo. O contexto entre colchetes NÃO deve ser traduzido '
              f'nem copiado. Marcações entre chaves como {{town}} ficam exatamente iguais, em inglês. Responda em JSON: {{"t": [{{"n": número, "inicio": as 3 primeiras palavras da fala '
              f'em inglês, "pt": tradução}}, ...]}}, um item por fala, na mesma ordem, sem pular nenhuma.\n\n'
              + numbered)
    item = {'type': 'object', 'properties': {'n': {'type': 'integer'}, 'inicio': {'type': 'string'},
                                             'pt': {'type': 'string'}}, 'required': ['n', 'inicio', 'pt']}
    schema = {'type': 'object', 'properties': {'t': {'type': 'array', 'items': item}}, 'required': ['t']}
    body = {'model': model, 'stream': False, 'think': False, 'format': schema, 'keep_alive': '30m',
            'options': {'temperature': 0.3, 'num_ctx': 6144},
            'messages': [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': prompt}]}
    request = urllib.request.Request(URL, json.dumps(body).encode(), {'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=1800) as response:
        return json.loads(json.loads(response.read())['message']['content'])['t']


PLACEHOLDER = re.compile(r'\{[^{}]+\}')


def restore_placeholders(en, pt):
    """The model sometimes translates {destination} to {destino}: put the originals back by position."""
    want, got = PLACEHOLDER.findall(en), PLACEHOLDER.findall(pt)
    if want != got and len(want) == len(got):
        parts = PLACEHOLDER.split(pt)
        pt = ''.join(part + (want[i] if i < len(want) else '') for i, part in enumerate(parts))
    return pt


def doubtful(en, pt):
    reasons = []
    if len(ENGLISH.findall(pt)) >= 2:
        reasons.append('inglês')
    ratio = len(pt) / max(1, len(en))
    if len(en) > 25 and (ratio < 0.5 or ratio > 2.2):
        reasons.append(f'tamanho {ratio:.1f}')
    if pt.strip().lower() == en.strip().lower() and len(en.split()) > 2:
        reasons.append('igual ao inglês')
    return reasons


def translate_chunk(model, lines):
    """lines: [(ctx, en)] -> {en: pt} for the items that line up."""
    out = {}
    try:
        items = ask(model, lines)
    except Exception as error:
        log(f'  falha no pedido: {error}')
        return out, []
    flagged = []
    for index, (ctx, en) in enumerate(lines):
        match = next((it for it in items if it.get('n') == index + 1), None)
        if match is None or words(match.get('inicio', ''), 2) != words(en, 2):
            continue
        pt = str(match.get('pt', '')).strip()
        if not pt or any(ord(c) > 0xFF for c in pt.replace('’', "'").replace('—', '-').replace('…', '...')):
            continue
        pt = restore_placeholders(en, pt)
        out[en] = pt
        reasons = doubtful(en, pt)
        if reasons:
            flagged.append((en, pt, ', '.join(reasons)))
    return out, flagged


def commit(source, results):
    queue = WORK / f'queue_{source}_local.json'
    queue.write_text(json.dumps({'source': source, 'items': {text_id(en): en for en in results}},
                                ensure_ascii=False), encoding='utf-8')
    batch = WORK / f'lote_{source}_local.txt'
    batch.write_text(''.join(f'{text_id(en)}\t{pt.replace(chr(10), " ")}\n' for en, pt in results.items()),
                     encoding='utf-8')
    result = subprocess.run(['python3', 'speech_commit.py', str(batch), '--queue', str(queue)],
                            cwd=ROOT / 'tools', capture_output=True, text=True)
    saved = re.search(r'salvo \S+: (\d+) linhas \| (.*)', result.stdout)
    log(f'{source}: +{saved.group(1)} | {saved.group(2)}' if saved else f'{source}: nada salvo {result.stdout[-300:]}')
    for line in result.stdout.splitlines():
        if line.startswith('ERRO'):
            log('  ' + line[:200])


def run(source, model):
    done = translated()
    pending = []
    for unit in extract()[source]:
        lines = [(ctx, en) for en, ctx in unit if en not in done]
        if lines:
            pending.append(lines)
    total = sum(len(u) for u in pending)
    log(f'{source}: {total} linhas pendentes em {len(pending)} unidades, modelo {model}')
    review = WORK / f'review_{source}.tsv'
    state = {'results': {}, 'finished': 0, 'start': time.time()}

    def send(chunk):
        got, flagged = translate_chunk(model, chunk)
        state['results'].update(got)
        state['finished'] += len(chunk)
        with open(review, 'a', encoding='utf-8') as f:
            for en, pt, why in flagged:
                f.write(f'{text_id(en)}\t{why}\t{en}\t{pt}\n')
        if len(state['results']) >= BATCH:
            commit(source, state['results'])
            state['results'] = {}
            rate = state['finished'] / max(1, time.time() - state['start'])
            log(f"  {state['finished']}/{total} linhas vistas, {rate * 60:.0f}/min, "
                f"faltam ~{(total - state['finished']) / max(rate, 1e-9) / 3600:.1f} h")

    seen, chunk = set(), []
    for unit in pending:
        if (WORK / 'STOP').exists():
            log('STOP encontrado, parando')
            break
        unit = [(ctx, en) for ctx, en in unit if en not in seen]
        seen.update(en for _, en in unit)
        if chunk and len(chunk) + len(unit) > CHUNK:
            send(chunk)
            chunk = []
        while len(unit) > CHUNK:  # a long unit goes alone, in CHUNK-sized pieces
            send(unit[:CHUNK])
            unit = unit[CHUNK:]
        chunk += unit
    if chunk and not (WORK / 'STOP').exists():
        send(chunk)
    results = state['results']
    if results:
        commit(source, results)


def main():
    model = sys.argv[sys.argv.index('--model') + 1] if '--model' in sys.argv else 'gemma3:12b'
    sources = [s for s in sys.argv[1:] if s in ('talk', 'scenes', 'radio')] or ['scenes', 'radio']
    (WORK / 'STOP').unlink(missing_ok=True)
    for source in sources:
        run(source, model)
    log('fim')


if __name__ == '__main__':
    main()
