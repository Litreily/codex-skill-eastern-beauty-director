#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BLOG_DIR="${BLOG_DIR:-/mnt/e/litreily/workspace/blog/BlogSources}"
POST_DIR="${POST_DIR:-$BLOG_DIR/source/_posts}"
DATE_VALUE="${1:-$(TZ=Asia/Shanghai date +%F)}"

find_node18() {
  if command -v node >/dev/null 2>&1 && node -e 'process.exit(Number(process.versions.node.split(".")[0]) >= 18 ? 0 : 1)' >/dev/null 2>&1; then
    command -v node
    return 0
  fi

  local candidate
  for candidate in "$HOME"/.nvm/versions/node/*/bin/node; do
    if [[ -x "$candidate" ]] && "$candidate" -e 'process.exit(Number(process.versions.node.split(".")[0]) >= 18 ? 0 : 1)' >/dev/null 2>&1; then
      echo "$candidate"
      return 0
    fi
  done

  echo "Node.js 18+ is required for image compression." >&2
  return 1
}

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
  "$(find_node18)" compress-images.mjs
fi

if [[ "${HEXO_DEPLOY:-0}" == "1" ]]; then
  cd "$BLOG_DIR"
  if [[ "${HEXO_GENERATE:-0}" != "1" ]]; then
    "$(find_node18)" compress-images.mjs
  fi
  hexo deploy
fi
