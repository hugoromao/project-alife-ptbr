#!/usr/bin/env bash
cd "$(dirname "$0")/.." && ./tools/get_lua.sh
up=$(python3 -c 'import sys; sys.path.insert(0,"tools"); from paths import upstream_version_dir; print(upstream_version_dir())')
tools/.lua/lua tools/chat_try.lua build/Workshop/ProjectALifeNPCs_PTBR_Hugo/Contents/mods/ProjectALifeNPCs_PTBR_Hugo/42 "$up" "$@"
