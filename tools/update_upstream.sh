#!/usr/bin/env bash
# Pull the latest Project A-Life from the Workshop, rebuild the PT-BR mod and list
# what needs attention (stale translations, new English text, changed code spots).
set -euo pipefail
cd "$(dirname "$0")/.."
WORKSHOP_ID=3803984183
if [ ! -x tools/DepotDownloader ]; then
    url=$(curl -s https://api.github.com/repos/SteamRE/DepotDownloader/releases/latest \
        | python3 -c 'import json,sys; print([a["browser_download_url"] for a in json.load(sys.stdin)["assets"] if "linux-x64" in a["name"]][0])')
    curl -sL "$url" -o /tmp/depotdownloader.zip
    python3 -c 'import zipfile; zipfile.ZipFile("/tmp/depotdownloader.zip").extract("DepotDownloader", "tools")'
    chmod +x tools/DepotDownloader
fi
tmp=$(mktemp -d)
./tools/DepotDownloader -app 108600 -pubfile "$WORKSHOP_ID" -dir "$tmp" | tail -2
new="$tmp/mods/ProjectALifeNPCs"
[ -d "$new" ] || { echo "download failed"; exit 1; }
if [ -d upstream/ProjectALifeNPCs ] && diff -rq upstream/ProjectALifeNPCs "$new" >/dev/null; then
    echo "Upstream unchanged."
else
    rm -rf upstream/ProjectALifeNPCs.prev
    [ -d upstream/ProjectALifeNPCs ] && mv upstream/ProjectALifeNPCs upstream/ProjectALifeNPCs.prev
    cp -r "$new" upstream/ProjectALifeNPCs
    echo "Upstream updated (previous copy in upstream/ProjectALifeNPCs.prev)."
    [ -d upstream/ProjectALifeNPCs.prev ] && diff -rq upstream/ProjectALifeNPCs.prev upstream/ProjectALifeNPCs | grep '\.lua\|\.json' || true
fi
rm -rf "$tmp"
cd tools && python3 build.py
