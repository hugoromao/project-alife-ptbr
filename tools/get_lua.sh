#!/usr/bin/env bash
# Build Lua 5.1 (the dialect Project Zomboid's Kahlua follows) into tools/.lua for tests.
set -euo pipefail
cd "$(dirname "$0")"
[ -x .lua/lua ] && exit 0
tmp=$(mktemp -d)
curl -sL https://www.lua.org/ftp/lua-5.1.5.tar.gz | tar xz -C "$tmp"
make -C "$tmp/lua-5.1.5" posix >/dev/null
mkdir -p .lua && cp "$tmp/lua-5.1.5/src/lua" "$tmp/lua-5.1.5/src/luac" .lua/
rm -rf "$tmp"
