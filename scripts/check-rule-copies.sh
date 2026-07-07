#!/usr/bin/env bash
# Verify every host adapter contains the canonical ruleset body verbatim
# (whole body, CRLF-normalized) — grepping only the first line would let a
# drifted body pass. Then verify the files that paraphrase the ruleset (the
# always-on hook and the core skill) still carry its load-bearing phrases,
# so a reword can't silently drop a rule.
set -euo pipefail
cd "$(dirname "$0")/.."

SRC_TEXT="$(tr -d '\r' < scripts/_ruleset.txt)"
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
for f in "${FILES[@]}"; do
  body="$(tr -d '\r' < "$f")"
  case "$body" in
    *"$SRC_TEXT"*) echo "ok    $f" ;;
    *) echo "DRIFT $f"; fail=1 ;;
  esac
done

INVARIANTS=(
  "load-bearing"
  "[FACT]"
  "strongest case"
  "verdict"
  "earned"
)
for p in "${INVARIANTS[@]}"; do
  grep -qF "$p" skills/validate-idea/SKILL.md \
    || { echo "MISSING invariant \"$p\" in skills/validate-idea/SKILL.md"; fail=1; }
done

# The always-on hook injects the canonical ruleset by reading AGENTS.md, so it
# can't drift — but it must actually point at it (both command variants).
grep -c "AGENTS.md" hooks/claude-hooks.json | grep -q "^2$" \
  || { echo "hooks/claude-hooks.json must read AGENTS.md in both command and commandWindows"; fail=1; }

exit $fail
