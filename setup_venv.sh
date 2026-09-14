#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/prepare-assets.py
printf '%s\n' 'Run: .venv/bin/python -m mkdocs serve'
