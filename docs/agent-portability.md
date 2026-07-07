# Agent portability

Reality Check ships one ruleset, mirrored into the file each agent reads. For
skill/plugin hosts you install the plugin; for instruction-only hosts you copy
the matching rules file. The ruleset text is identical everywhere (kept in sync
by `scripts/check-rule-copies.sh`).

| Agent / tool            | How to use                                         | File |
| ----------------------- | -------------------------------------------------- | ---- |
| Claude (Cowork desktop) | Add from repository in the plugin UI               | `.claude-plugin/` + `skills/` + `hooks/` |
| Claude Code             | `/plugin marketplace add https://github.com/MrinallSamal-byte/Idea-Validater.git` then `/plugin install reality-check@idea-validater`   | `.claude-plugin/marketplace.json` |
| Codex / VS Code Codex   | Auto-reads `AGENTS.md` at repo root                | `AGENTS.md` |
| OpenCode / Swival       | Auto-reads `AGENTS.md`                              | `AGENTS.md` |
| Cursor                  | Copy rules file into your project / global rules   | `.cursor/rules/reality-check.mdc` |
| Windsurf                | Copy rules file                                    | `.windsurf/rules/reality-check.md` |
| Cline                   | Copy rules file                                    | `.clinerules/reality-check.md` |
| GitHub Copilot (editor) | Reads repo instructions                            | `.github/copilot-instructions.md` |
| Kiro                    | Copy to `~/.kiro/steering/` or project steering    | `.kiro/steering/reality-check.md` |
| Gemini / Antigravity    | Install as extension, or drop ruleset in `.agents/rules/` | `gemini-extension.json`, `commands/`, `skills/`, `.agents/rules/` |

If a host isn't listed, point it at `AGENTS.md` — most agents that read a root
instruction file will pick it up. Instruction-only hosts get the always-on
honesty behavior; skill hosts (Claude, Gemini) additionally get the 13 skills.

## Adapter rule

Keep adapters thin. When a host supports skills or hooks, point it at the
existing `skills/` and `hooks/` files. When a host only supports project
instructions, its copied rule text must stay byte-identical to
`scripts/_ruleset.txt` — `scripts/check-rule-copies.sh` (run in CI) fails on
drift.

One placement rule: the Claude hook lives at `hooks/claude-hooks.json`, not
`hooks/hooks.json`, because Gemini CLI auto-loads `hooks/hooks.json` from
installed extensions and the file uses Claude's hook schema. Keep host-specific
hook files on paths only that host's manifest points at.
