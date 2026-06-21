#!/usr/bin/env sh
set -eu

python3 scripts/test_repo.py

echo "Demo repo build"
echo "1. Markdown prüfen"
echo "2. EPUB bauen"
echo "3. PDF prüfen"
