"""Upload (or update) the Workshop item with SteamCMD instead of the in-game uploader.

  python3 tools/publish_workshop.py <steam_login> "change note"

Needs ~/steamcmd/steamcmd.sh and a cached login: run once, in a terminal,
  ~/steamcmd/steamcmd.sh +login <steam_login> +quit
(password + Steam Guard code); later runs reuse the cached credentials.
Rebuilds the mod, writes work/workshop_item.vdf and uploads build/Workshop/<mod>/Contents
to the item in art/workshop_id.txt, public, with the build's title and description.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEAMCMD = Path.home() / 'steamcmd' / 'steamcmd.sh'
ITEM_DIR = ROOT / 'build' / 'Workshop' / 'ProjectALifeNPCs_PTBR_Hugo'


def vdf_string(text):
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    login = sys.argv[1]
    note = sys.argv[2] if len(sys.argv) > 2 else 'Atualização da tradução'
    subprocess.run(['python3', str(ROOT / 'tools' / 'build.py')], check=True)
    info = (ITEM_DIR / 'workshop.txt').read_text(encoding='utf-8').splitlines()
    title = next(l.split('=', 1)[1] for l in info if l.startswith('title='))
    description = '\n'.join(l.split('=', 1)[1] for l in info if l.startswith('description='))
    item_id = (ROOT / 'art' / 'workshop_id.txt').read_text().strip()
    vdf = ROOT / 'work' / 'workshop_item.vdf'
    fields = {
        'appid': '108600',
        'publishedfileid': item_id,
        'contentfolder': str(ITEM_DIR / 'Contents'),
        'previewfile': str(ITEM_DIR / 'preview.png'),
        'visibility': '0',
        'title': title,
        'description': description,
        'changenote': note,
    }
    vdf.write_text('"workshopitem"\n{\n' + ''.join(f'\t"{k}"\t{vdf_string(v)}\n' for k, v in fields.items()) + '}\n',
                   encoding='utf-8')
    result = subprocess.run([str(STEAMCMD), '+login', login, '+workshop_build_item', str(vdf), '+quit'],
                            capture_output=True, text=True)
    output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout + result.stderr)
    print('\n'.join(l for l in output.splitlines() if re.search(r'(?i)workshop|error|fail|success|upload|item|login', l)))
    if 'Success' not in output:
        raise SystemExit('Envio não confirmado; veja a saída acima.')


if __name__ == '__main__':
    main()
