#!/usr/bin/env bash
# Verify every host adapter contains the canonical ruleset body verbatim.
set -euo pipefail
cd "$(dirname "$0")/.."
SRC="scripts/_ruleset.txt"
FILES=(
  "AGENTS.md"
  ".cursor/rules/reality-check.mdc"
  ".windsurf/rules/reality-check.md"
  ".clinerules/reality-check.md"
  ".github/copilot-instructions.md"
  ".kiro/steering/reality-check.md"
  ".agents/rules/reality-check.md"
)
fail=0
need="$(head -1 "$SRC")"
for f in "${FILES[@]}"; do
  if grep -qF "$need" "$f"; then echo "ok   $f"; else echo "DRIFT $f"; fail=1; fi
done
exit $fail
