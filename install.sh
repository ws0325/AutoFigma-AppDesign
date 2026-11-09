#!/usr/bin/env bash
# Install the figma-app-design-builder skill for Claude Code (macOS / Linux).
#
# One line, straight from GitHub:
#   curl -fsSL https://raw.githubusercontent.com/ws0325/AutoFigma-AppDesign/main/install.sh | bash
# Or from a cloned copy of this repository:
#   bash install.sh
#
# Options (environment variables):
#   SKILL_SCOPE=project   install into ./.claude/skills of the current folder instead of ~/.claude/skills
#   REPO=owner/name       GitHub repository to download from when run outside the repository
set -euo pipefail

SKILL="figma-app-design-builder"
REPO="${REPO:-ws0325/AutoFigma-AppDesign}"
BRANCH="${BRANCH:-main}"

if [ "${SKILL_SCOPE:-user}" = "project" ]; then
  DEST_ROOT="$(pwd)/.claude/skills"
else
  DEST_ROOT="${HOME}/.claude/skills"
fi
DEST="${DEST_ROOT}/${SKILL}"

# 1. Find the skill folder: next to this script, or download the repository.
SCRIPT_DIR=""
if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi
TMP=""
if [ -n "$SCRIPT_DIR" ] && [ -d "$SCRIPT_DIR/skills/$SKILL" ]; then
  SRC="$SCRIPT_DIR/skills/$SKILL"
else
  TMP="$(mktemp -d)"
  echo "Downloading ${REPO}@${BRANCH}..."
  curl -fsSL "https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz" | tar -xz -C "$TMP"
  SRC="$(find "$TMP" -maxdepth 3 -type d -path "*/skills/$SKILL" | head -n 1)"
  [ -n "$SRC" ] || { echo "Skill folder not found in the download." >&2; exit 1; }
fi

# 2. Copy (replacing an older version).
mkdir -p "$DEST_ROOT"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"
find "$DEST" -name "__pycache__" -type d -prune -exec rm -rf {} +
[ -n "$TMP" ] && rm -rf "$TMP"
echo "Installed to $DEST"

# 3. Python image library used by the grid script.
PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c "import sys; sys.exit(0 if sys.version_info[0] == 3 else 1)" 2>/dev/null; then PY="$c"; break; fi
done
if [ -n "$PY" ]; then
  if "$PY" -c "import PIL" 2>/dev/null; then
    echo "Pillow already installed."
  else
    echo "Installing Pillow (for scripts/grid_extract.py)..."
    if ! "$PY" -m pip install --user --quiet pillow 2>/dev/null; then
      # Homebrew / Debian 12+ Pythons are "externally managed" and refuse pip --user.
      if command -v brew >/dev/null 2>&1 && brew install --quiet pillow >/dev/null 2>&1; then
        echo "Installed Pillow with Homebrew."
      else
        echo "Could not install Pillow automatically. Use a virtual environment:"
        echo "  $PY -m venv ~/.venvs/figma-skill && ~/.venvs/figma-skill/bin/pip install pillow"
        echo "and run the skill's scripts with ~/.venvs/figma-skill/bin/python"
      fi
    fi
  fi
else
  echo "Python 3 not found. Install it from https://www.python.org/ and then run: python3 -m pip install pillow"
fi

echo
echo "Done. Restart Claude Code, then try:  design me a fitness app"
