"""Translate the speech queue with N parallel headless `claude -p` workers.

  setsid nohup python3 tools/parallel_translate.py talk scenes radio > work/parallel.log 2>&1 &
  touch work/STOP        # every lane stops after its current batch

Each lane owns part K of N of every source (speech_queue.py --part K/N). The worker
only gets the queue text and the style guide and prints "id<TAB>portuguese" lines;
this script writes the batch, and speech_commit.py validates, commits and pushes it
(one commit at a time, see the lock there). A failed call (usage limit, network)
waits and retries, so the run survives a limit reset or an account switch (/login).
"""
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
WORK = ROOT / 'work'
PARTS = 4
MODEL = 'sonnet'
SIZES = {'talk': 150, 'scenes': 150, 'radio': 100}
RETRY_WAIT = 900
MAX_FAILURES = 30
print_lock = threading.Lock()


def log(message):
    with print_lock:
        print(time.strftime('%H:%M:%S'), message, flush=True)


def style_guide():
    text = (ROOT / 'PROGRESS.md').read_text(encoding='utf-8')
    match = re.search(r'## Guia de estilo das falas\n(.*?)(\n## |\Z)', text, re.S)
    return match.group(1).strip() if match else ''


SYSTEM = """Você traduz do inglês para o português do Brasil as falas de NPCs do mod Project A-Life
(Project Zomboid, apocalipse zumbi no Kentucky, 1993). Responda SOMENTE com as linhas traduzidas,
sem comentários, sem cabeçalho e sem blocos de código.

Guia de estilo:
""" + style_guide() + """

Regras extras:
- O contexto entre colchetes traz a intenção (ex.: reply ASK_FOOD), papel (role=), sexo (sex=f/m),
  temperamento (tmp=), postura (st=) e humor (mood=). Use-o para o tom e o gênero de quem fala.
  Linhas "...continuação" seguem a fala anterior da mesma pessoa. Em cenas, falas da mesma cena
  formam um diálogo; mantenha coerência entre elas.
- Traduza com contexto, nunca ao pé da letra. Falas curtas continuam curtas.
- Não use aspas curvas nem travessão longo; use "..." para hesitação."""


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=TOOLS, capture_output=True, text=True, **kw)


def next_batch(source, k):
    out = run(['python3', 'speech_queue.py', 'next', source, str(SIZES[source]), '--part', f'{k}/{PARTS}'])
    lines = [l for l in out.stdout.splitlines() if '\t' in l]
    return [l.replace('\t[', ' [', 1).replace(']\t', '] ', 1) for l in lines]


def translate(lines):
    prompt = ('Traduza cada linha abaixo. Formato de cada linha da resposta: o id, um TAB, a tradução. '
              'Uma linha de resposta para cada linha de entrada, na mesma ordem, sem pular nenhuma.\n\n'
              + '\n'.join(lines))
    out = subprocess.run(['claude', '-p', '--model', MODEL, '--tools', '', '--no-session-persistence',
                          '--system-prompt', SYSTEM, prompt],
                         cwd='/tmp', capture_output=True, text=True, timeout=1800)
    if out.returncode != 0:
        raise RuntimeError((out.stderr or out.stdout).strip()[:300])
    rows = []
    for line in out.stdout.splitlines():
        match = re.match(r'^\s*([0-9a-f]{7})\s*(?:\t|\s{2,}|\s*[|:]\s*|\s)(.+)$', line)
        if match:
            rows.append(f'{match.group(1)}\t{match.group(2).strip()}')
    return rows


def lane(k, sources):
    for source in sources:
        failures = 0
        while True:
            if (WORK / 'STOP').exists():
                log(f'p{k}: STOP encontrado, parando')
                return
            lines = next_batch(source, k)
            if not lines:
                log(f'p{k}: {source} concluído')
                break
            try:
                rows = translate(lines)
                if len(rows) < min(20, len(lines)):
                    raise RuntimeError(f'resposta com {len(rows)} de {len(lines)} linhas')
                if len(rows) < len(lines):
                    log(f'p{k}: {source} resposta parcial ({len(rows)} de {len(lines)}), o resto volta pra fila')
            except Exception as error:  # usage limit, timeout, network
                failures += 1
                log(f'p{k}: {source} falhou ({failures}/{MAX_FAILURES}): {error}')
                if failures >= MAX_FAILURES:
                    log(f'p{k}: desistindo')
                    return
                time.sleep(RETRY_WAIT)
                continue
            batch = WORK / f'lote_{source}_p{k}.txt'
            batch.write_text('\n'.join(rows) + '\n', encoding='utf-8')
            result = run(['python3', 'speech_commit.py', str(batch), '--queue', f'work/queue_{source}_p{k}.json'])
            saved = re.search(r'salvo \S+: (\d+) linhas \| (.*)', result.stdout)
            errors = result.stdout.count('ERRO')
            if saved:
                failures = 0
                log(f'p{k}: {source} +{saved.group(1)} (erros {errors}) | {saved.group(2)}')
            else:
                failures += 1
                log(f'p{k}: {source} nada salvo ({failures}/{MAX_FAILURES}): {result.stdout[-300:]} {result.stderr[-300:]}')
                if failures >= MAX_FAILURES:
                    return
                time.sleep(60)


def main():
    sources = [s for s in sys.argv[1:] if s in SIZES] or ['talk', 'scenes', 'radio']
    (WORK / 'STOP').unlink(missing_ok=True)
    log(f'início: {PARTS} faixas, modelo {MODEL}, fontes {sources}')
    threads = [threading.Thread(target=lane, args=(k, sources)) for k in range(1, PARTS + 1)]
    for index, thread in enumerate(threads):
        thread.start()
        time.sleep(5 * (index + 1))
    for thread in threads:
        thread.join()
    log('fim')


if __name__ == '__main__':
    main()
