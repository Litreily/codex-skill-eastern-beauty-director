#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BLOG_DIR="${BLOG_DIR:-/mnt/e/litreily/workspace/blog/BlogSources}"
POST_DIR="${POST_DIR:-$BLOG_DIR/source/_posts}"
DATE_VALUE="${1:-$(date +%F)}"

cd "$REPO_DIR"

OUT_FILE="$(python3 scripts/daily_eastern_beauty_generator.py \
  --date "$DATE_VALUE" \
  --output-dir "$POST_DIR")"

echo "Generated daily Eastern Beauty prompt post:"
echo "$OUT_FILE"

if [[ "${HEXO_GENERATE:-0}" == "1" ]]; then
  cd "$BLOG_DIR"
  hexo clean
  hexo generate
fi

if [[ "${HEXO_DEPLOY:-0}" == "1" ]]; then
  cd "$BLOG_DIR"
  hexo deploy
fi
