"""Shared project paths. The upstream version folder (e.g. 42.18) is detected, so an
upstream update that renames it needs no code change."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / 'upstream/ProjectALifeNPCs'


def upstream_version_dir():
    dirs = [d for d in UPSTREAM.iterdir() if d.is_dir() and (d / 'media').is_dir() and d.name != 'common']
    if not dirs:
        raise SystemExit(f'no versioned folder with media/ under {UPSTREAM}')
    return max(dirs, key=lambda d: [int(p) if p.isdigit() else 0 for p in d.name.split('.')])
