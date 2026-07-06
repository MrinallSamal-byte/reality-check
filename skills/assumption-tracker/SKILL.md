---
name: assumption-tracker
description: >
  Track the load-bearing assumptions from a validation over time and update
  their status as real evidence comes in. Use when the user says "track this
  assumption", "log my assumptions", "check on my assumptions", "update
  assumption status", "did that assumption hold up", "what am I still
  assuming", or just ran validate-idea/pre-mortem and the assumptions
  surfaced should be tracked going forward rather than forgotten.
---

# Assumption Tracker

Every validate-idea run tags claims `[ASSUMPTION]` and names the load-bearing
one — and then, without this skill, that tag is where the process stops. The
assumption never gets checked again. This skill closes that loop: it keeps a
running ledger of specific, falsifiable beliefs and their real-world status,
so "I assumed X" turns into "I found out X was true/false" instead of
evaporating.

## Where it lives

Write to `assumption-ledger.md` in the user's working folder — separate from
`idea-journal.md`. The journal tracks verdicts on whole ideas; this tracks the
individual beliefs those verdicts rested on, which is a finer grain and a
different lifecycle (an idea gets one verdict; an assumption gets tested,
resolved, and sometimes replaced by a new one).

Create the file with this header if it doesn't exist; otherwise append:

```
# Assumption Ledger

Falsifiable beliefs from past validations, and what actually happened when
they were tested. Newest entries at the top.

---
```

## Logging an assumption

After a validate-idea, pre-mortem, or market-scan run (or when the user asks
directly), pull the load-bearing assumption and any other named `[ASSUMPTION]`
claims worth tracking — don't re-interview the user for what's already in the
conversation. One entry per assumption:

```
## <date> — <idea name> — <short assumption summary>

**Full assumption:** <the actual belief, stated so it's checkable>
**Why it matters:** <what breaks if this is false — usually "load-bearing" or a named risk>
**Status:** Open
**Test planned:** <the cheapest way to check it, if named — from direction-roadmap or discovery-script>

---
```

Don't log vague beliefs ("this could work") — only specific, falsifiable ones.
If nothing in the validation was concrete enough to track, say so instead of
inventing an entry.

## Updating an assumption

When the user reports a result ("I talked to 10 users and...", "turns out the
API doesn't support that", "I found 3 competitors already doing this"), find
the matching entry and append:

```
> **Resolved <date>:** <what was actually found> — **Confirmed** / **Disproven** / **Weakened**.
```

If a load-bearing assumption comes back **Disproven**, say so plainly and flag
that the original verdict likely needs revisiting — offer to re-run
**validate-idea** with the new fact folded in. Don't let a disproven
load-bearing assumption sit quietly next to an unchanged "Pursue."

## Reviewing the ledger

When asked what's being tracked: list open assumptions grouped by idea, flag
any that have been open a long time with no test planned, and summarize what's
been confirmed vs. disproven recently. An idea with several disproven
assumptions and no ledger update is a signal worth naming directly.

## Output structure (for a review)

```
ASSUMPTION LEDGER

STILL OPEN
<idea> — <assumption> — <test planned, or "none yet">
...

RECENTLY RESOLVED
<idea> — <assumption> — Confirmed/Disproven — <what was found>
...

WORTH FLAGGING
Load-bearing assumptions that are open too long, or disproven ones whose
verdict hasn't been revisited yet.
```

If the user hasn't logged anything yet, say so and offer to start after the
next **validate-idea** run rather than fabricating history.
