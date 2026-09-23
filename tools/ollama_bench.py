"""Compare local Ollama models on speech lines that already have a translation.

  python3 tools/ollama_bench.py qwen3:8b aya-expanse:8b

Writes work/bench_<model>.txt (EN / reference / model) and prints speed per model.
"""
import json
import re
import sys
import time
import urllib.request

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from paths import ROOT
from speech_queue import extract, text_id, translated
from parallel_translate import SYSTEM


def sample():
    units, done = extract(), translated()
    picked = []
    for source, want in (('scenes', 45), ('radio', 20)):
        count = 0
        for unit in units[source]:
            if count >= want:
                break
            if all(en in done for en, _ in unit):
                for en, ctx in unit:
                    picked.append((text_id(en), ctx, en, done[en]))
                    count += 1
    return picked


def ask(model, lines):
    numbered = '\n'.join(f'{i + 1}. {line}' for i, line in enumerate(lines))
    prompt = (f'Traduza as {len(lines)} falas numeradas abaixo. O contexto entre colchetes NÃO deve ser traduzido '
              f'nem copiado. Responda em JSON: {{"t": [...]}} com exatamente {len(lines)} traduções, na mesma ordem.\n\n'
              + numbered)
    schema = {'type': 'object', 'properties': {'t': {'type': 'array', 'items': {'type': 'string'},
              'minItems': len(lines), 'maxItems': len(lines)}}, 'required': ['t']}
    body = {'model': model, 'stream': False, 'think': False, 'format': schema,
            'options': {'temperature': 0.3, 'num_ctx': 6144},
            'messages': [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': prompt}]}
    request = urllib.request.Request('http://localhost:11434/api/chat', json.dumps(body).encode(),
                                     {'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=3600) as response:
        return json.loads(response.read())


def main():
    items = sample()
    lines = [f'[{ctx}] {en}' for tid, ctx, en, _ in items]
    for model in sys.argv[1:]:
        start = time.time()
        answer = ask(model, lines)
        elapsed = time.time() - start
        text = answer['message']['content']
        try:
            outs = json.loads(text)['t']
        except Exception:
            outs = []
        got = {tid: out.strip() for (tid, _, _, _), out in zip(items, outs)}
        tokens = answer.get('eval_count', 0)
        speed = tokens / max(1e-9, answer.get('eval_duration', 1) / 1e9)
        out = ROOT / f'work/bench_{model.replace(":", "_")}.txt'
        with open(out, 'w', encoding='utf-8') as f:
            for tid, ctx, en, ref in items:
                f.write(f'[{ctx}]\nEN: {en}\nREF: {ref}\nOUT: {got.get(tid, "<<faltou>>")}\n\n')
        words = sum(len(en.split()) for _, _, en, _ in items)
        print(f'{model}: {len(got)}/{len(items)} linhas, {elapsed:.0f}s, {tokens} tokens, {speed:.1f} tok/s, '
              f'~{words / elapsed:.1f} palavras EN/s -> {out.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
