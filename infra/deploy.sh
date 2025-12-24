#!/usr/bin/env bash
set -euo pipefail

APP_SLUG="clickdialog"
BASE="/opt/${APP_SLUG}"
BACK="${BASE}/backend"
FRONT="${BASE}/frontend"

echo "== Deploy ${APP_SLUG} =="

cd "${BASE}"
git pull

echo "-- Backend: deps & migrate"
cd "${BACK}"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -r requirements.txt
flask db upgrade || true

echo "-- Frontend: build"
cd "${FRONT}"
npm install
npm run build

echo "-- Restart systemd"
systemctl restart ${APP_SLUG}-backend.service

echo "OK"
