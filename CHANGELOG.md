# Changelog

All notable changes to Reality Check are documented here.
This project adheres to [Semantic Versioning](https://semver.org/).

## [0.6.1] - 2026-07-07

### Fixed
- **Claude hook moved off Gemini's auto-discovery path.** `hooks/hooks.json` →
  `hooks/claude-hooks.json` (with `plugin.json` updated to match): Gemini CLI
  auto-loads `hooks/hooks.json` from installed extensions, and this repo ships
  a Gemini extension while the file uses Claude's hook schema. Behavior on
  Claude is unchanged.
- `scripts/check-rule-copies.sh` now verifies each adapter contains the **whole**
  canonical ruleset verbatim (it previously only grepped for the first line, so
  a drifted body would pass), and asserts load-bearing canary phrases survive
  in the always-on hook and the `validate-idea` skill.
- `benchmarks/score.py` writes its results report as UTF-8 explicitly — on
  Windows it used the locale encoding (cp1252), garbling em-dashes.

### Added
- `scripts/check-versions.py` — the version declared in `package.json`,
  `plugin.json`, `marketplace.json` (both fields), `gemini-extension.json`, and
  the latest CHANGELOG heading must be one pinned X.Y.Z; on a release-tag CI
  run it must also match the tag. Wired into CI and `npm run validate`.
- `/reality-check` command for Gemini CLI (`commands/reality-check.toml`) —
  set the intensity or run a check; Gemini also picks up the 13 skills.
- Logo (`assets/logo.svg` + dark variant) and a centered README header.
- README Uninstall section; `bugs` field in `package.json`.
- CI: skill-frontmatter check now requires `name:` and `description:`, not
  just the opening `---`; new version-consistency step.
- CONTRIBUTING: a Releasing section documenting the version-bump checklist.

## [0.6.0] - 2026-07-06

### Added
- **Five new skills**, closing gaps between advice and action rather than
  duplicating the existing eight:
  - `assumption-tracker` — logs load-bearing assumptions to a separate
    `assumption-ledger.md` and tracks whether they're later confirmed or
    disproven, instead of letting a `[ASSUMPTION]` tag be the end of the story.
  - `calibration-report` — mines the user's own `idea-journal.md` history for
    scoring bias (e.g. consistently over-scoring Traction). Requires real
    journal history; says so if there isn't enough yet rather than inventing
    a pattern from a thin sample.
  - `discovery-script` — turns "go talk to 10 users" into an actual interview
    script targeted at the load-bearing assumption, with an explicit
    kill-question.
  - `unit-economics` — real LTV:CAC and payback-period math from the user's
    own estimates, each input tagged FACT/ASSUMPTION/UNKNOWN. No invented numbers.
  - `verdict-memo` — exports a completed validate-idea or pitch-critique
    verdict as a shareable one-page `<slug>-memo.md`, distinct from the
    private running idea-journal.
- Cross-links between the new and existing skills (validate-idea,
  idea-journal, direction-roadmap, pre-mortem, pitch-critique) so each is
  offered where it's actually relevant.
- README: skills table and counts updated (8 → 13), new usage examples.

## [0.5.4] - 2026-07-06

### Fixed
- `reality-check-mode` skill claimed the user had "configured Reality Check for
  maximum bluntness at setup" and defaulted to **ultra** — no such setup step
  exists, and it silently contradicted the documented default (**full**) in
  the README, `AGENTS.md`, every host adapter, and the always-on hook. Now
  consistent everywhere: default is full until the user asks for another level.

### Added
- README badges (release tag, agent count, license) alongside the existing CI badge.
- README FAQ section (API keys/setup, casual-chat behavior, when it agrees, journal storage).
- `npm run validate` — runs the rule-sync check and benchmark harness in one command.
- `CONTRIBUTING.md` linked from the README (was previously undiscoverable from there).

## [0.5.3] - 2026-06-30

### Added
- SVG benchmark charts (`assets/benchmark-behavior.svg`, `assets/benchmark-models.svg`)
  generated from the data by `benchmarks/make_charts.py`, embedded in the README so
  the visuals can never drift from the numbers. Tables retained for accessibility.

## [0.5.2] - 2026-06-30

### Fixed / portability
- Install instructions now use the explicit HTTPS `.git` URL so `marketplace add`
  never falls back to SSH on other machines; added a troubleshooting note for the
  SSH host-key error.
- Added `.gitattributes` to normalize line endings (LF) across operating systems.
- Documented that no Node.js/runtime is required (the always-on hook is prompt-based).

## [0.5.1] - 2026-06-30

### Added
- README "Reported results" table with maintainer-reported per-model scores,
  attributed as maintainer testing pending documented methodology.

## [0.5.0] - 2026-06-30

### Added
- **CI** (`.github/workflows/validate.yml`): validates JSON manifests and skill
  frontmatter, checks rule-adapter sync, and runs the benchmark on every push.
- **`CONTRIBUTING.md`** with the ruleset-sync and honesty rules.
- README now features the real, reproducible benchmark results (honestly framed)
  and a CI status badge.

## [0.4.1] - 2026-06-30

### Added
- **Benchmark harness** (`benchmarks/score.py`): deterministic scoring of a
  baseline vs. ruleset arm over 10 ground-truth-labelled ideas, with a dated
  results report. Documented honestly as a reproducible demonstration, not an
  independent efficacy claim.

## [0.4.0] - 2026-06-30

### Added
- **Multi-host support.** One canonical ruleset is now mirrored into the file each
  agent reads: `AGENTS.md` (Codex, OpenCode, Swival, CodeWhale, VS Code Codex),
  `.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.github/copilot-instructions.md`,
  `.kiro/steering/`, and `.agents/rules/`. Instruction-only hosts get the always-on
  honesty behavior; Claude additionally gets the eight skills.
- `gemini-extension.json` and `package.json` for Gemini/Antigravity and npm.
- `examples/` — before/after comparisons on real prompts.
- `docs/agent-portability.md` — which file maps to which agent.
- `scripts/check-rule-copies.sh` — verifies every adapter matches the canonical ruleset.
- `benchmarks/` — an honest measurement method (no fabricated results).

## [0.3.0] - 2026-06-30

### Added
- **Always-on honesty hook** (`hooks/hooks.json`): a `UserPromptSubmit` prompt
  hook that applies the anti-sycophancy protocol by default whenever the user
  shares an idea, plan, or opinion — without being summoned. Guarded so casual
  chat and ordinary tasks are left alone; degrades quietly on hosts that don't
  run plugin hooks.
- **The Reality Check Protocol**: a crystallized five-rung core (restate plain →
  fact vs. assumption → load-bearing belief → steelman the skeptic → commit to a
  verdict) shared by every skill and the hook.
- **`reality-check-mode` skill**: intensity control — `off` / `lite` / `full` /
  `ultra`. Lowering intensity changes delivery, never honesty.
- Persona and a before/after example in the README.

## [0.2.0] - 2026-06-30

### Added
- **`compare-ideas` skill**: scores and ranks several competing ideas on one
  rubric and commits to a single recommendation.
- **`idea-journal` skill**: persistent markdown journal of verdicts in the
  project folder; surfaces patterns across ideas over time.

## [0.1.0] - 2026-06-30

### Added
- Initial release with five skills: `validate-idea` (core engine + scoring
  rubric + idea-type playbooks), `market-scan`, `pre-mortem`,
  `direction-roadmap`, and `pitch-critique`.
