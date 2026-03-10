#!/usr/bin/env bash
set -euo pipefail

TARGET_USER="aaeon"
TARGET_HOST="10.15.10.216"
TARGET_PATH="/mnt/storage/gs_cron_jobs"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

rsync -a --delete \
  --exclude ".git" \
  --exclude "__pycache__" \
  --exclude ".venv" \
  --exclude ".env-example" \
  "$REPO_ROOT/" \
  "$TARGET_USER@$TARGET_HOST:$TARGET_PATH/"

echo "Deployed to $TARGET_USER@$TARGET_HOST:$TARGET_PATH"
