---
name: idea-journal
description: >
  Keep a persistent log of ideas, their verdicts, and how they evolve over time.
  Use when the user says "log this idea", "save this verdict", "track my ideas",
  "what did I conclude about X", "show my idea journal", "update the journal", or
  after any validation/critique the user wants recorded. Writes a durable markdown
  journal in the working folder so progress survives across sessions.
---

# Idea Journal

Turn one-off assessments into a track record. A validation the user forgets is
wasted; a logged one lets them see patterns ("I keep over-scoring on traction"),
revisit parked ideas when circumstances change, and watch an idea mature. This is
what makes Reality Check a tool rather than a chat.

## Where the journal lives

Write to `idea-journal.md` in the user's working folder (the folder they selected
for this project). If you can't tell where that is, ask once, then remember it for
the session. Create the file with the header below if it doesn't exist; otherwise
append — never overwrite existing entries.

File header (only when creating the file):

```
# Idea Journal

A running log of ideas, verdicts, and how they change. Newest entries at the top.

---
```

## Logging an entry

When the user logs an idea (or asks to record a just-finished validation,
pre-mortem, or pitch critique), prepend a new entry directly under the `---` so
the newest is always on top. Pull details from the recent conversation rather than
re-interviewing the user.

Entry template:

```
## <date> — <short idea name>

**Type:** <startup / product / technical / creative>
**Verdict:** <Pursue / Pursue-but-fix-X / Reshape / Park / Drop>
**Score:** <n>/50
**Load-bearing assumption:** <the one belief it rests on>
**Biggest risk:** <the top failure mode>
**Decision / next step:** <what the user chose to do>
**Status:** <Active / Parked / Dropped / Shipped>

<2–4 line summary of the reasoning. Keep it honest — log the real verdict, not a
flattering version.>

---
```

Use the actual current date. Keep entries tight; the journal should stay skimmable.

## Updating an existing idea

When the user revisits an idea ("update the journal on X — I tested it and..."),
don't bury it. Add a dated update line under that idea's entry and change its
**Status** if it moved:

```
> **Update <date>:** <what changed — test result, pivot, new evidence — and the
> revised verdict if it shifted>
```

If a parked idea now clears the bar that was blocking it, say so plainly and
suggest re-running **validate-idea** with the new facts.

## Reviewing the journal

When the user asks what's in their journal or wants a review:
- Read `idea-journal.md` and summarize: active ideas, parked ones (and what would
  un-park them), and dropped ones (so they don't accidentally re-pitch a dead idea).
- Look for honest patterns across entries — recurring weak dimensions, ideas that
  keep dying for the same reason — and name them. This meta-feedback is often more
  valuable than any single verdict.
- Don't soften the history. The point of a journal is an accurate record.

## After logging

Confirm what was written in one line and point to the file. If the user just
logged a fresh idea without validating it, offer to run **validate-idea** first so
the entry has a real verdict rather than a placeholder.

## Related skills

This journal tracks verdicts on whole ideas. Two companion skills use the same
file for a different angle: **assumption-tracker** keeps a separate,
finer-grained ledger of the individual `[ASSUMPTION]` tags underneath each
verdict, and **calibration-report** mines this journal's history (once there's
enough of it) for patterns in how the user scores and predicts outcomes.
Mention both when relevant — a journal with several stale Parked entries or a
lopsided verdict distribution is exactly what calibration-report is for.
