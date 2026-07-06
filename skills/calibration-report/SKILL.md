---
name: calibration-report
description: >
  Analyze the user's own idea-journal history for patterns in how they score
  and predict outcomes — where they're systematically over-optimistic or
  overly harsh. Use when the user asks "how's my track record", "am I
  biased", "review my calibration", "what do I keep getting wrong", "how
  accurate have my verdicts been", or wants a meta-review across several past
  ideas rather than a single one. Needs real history in idea-journal.md to
  say anything meaningful — says so plainly rather than inventing a pattern
  from a thin sample.
---

# Calibration Report

Every other skill in this plugin calibrates a verdict against the idea. This
one calibrates the *user* against their own track record. The value compounds:
the more ideas logged in `idea-journal.md`, the sharper this gets — it is the
one skill that gets more useful the longer the plugin is used.

## Prerequisite: enough data

Read `idea-journal.md` in the working folder. If it doesn't exist, or has
fewer than 5 entries, or fewer than 3 entries with a **Status** update (Parked/
Dropped/Shipped — i.e. an actual outcome, not just an initial verdict), say so
directly: there isn't enough history for a reliable pattern yet, and a
pattern claimed from 2-3 points would be exactly the kind of invented
confidence this plugin exists to avoid. Offer to run this again once more
entries have outcomes.

## Method

1. **Pull every entry**: idea type, score, verdict, load-bearing assumption,
   and — critically — the current **Status** and any **Update** lines that
   record what actually happened.

2. **Compare predicted to actual, where an outcome exists.** For each entry
   with a real outcome (parked/dropped for a stated reason, or shipped and
   later reported back on), check whether the original score and verdict
   matched what happened. Look specifically for:
   - A rubric dimension that's consistently scored high on ideas that later
     failed *for that exact reason* (e.g., Traction scored 7+ on three ideas
     that were later parked for lack of traction).
   - A verdict that's consistently one notch more optimistic than the outcome
     (e.g., "Pursue, but fix X" on things that quietly got dropped).
   - The reverse pattern is just as real and worth naming: scoring everything
     low, or defaulting to Drop/Reshape regardless of the idea, which is its
     own failure to calibrate.

3. **Check the verdict distribution**, even without outcomes yet. If nearly
   every entry is "Pursue," the plugin (or the user prompting it) may be
   drifting back toward the agreeableness this whole tool exists to resist —
   say so. Same if everything lands on "Drop": that's not rigor, it's a
   different kind of miscalibration.

4. **Name one pattern, specifically**, with the entries that support it. Don't
   list every minor wobble — the value is in the single most useful thing to
   watch for next time, not an exhaustive audit.

## Output structure

```
CALIBRATION REPORT
Based on <n> journal entries, <n> with a real outcome.

THE PATTERN
The one recurring bias, stated plainly, with the entries that show it.

VERDICT DISTRIBUTION
<n> Pursue / <n> Fix-first / <n> Reshape / <n> Park / <n> Drop — and whether
that spread itself looks calibrated or skewed.

WHAT TO DISCOUNT NEXT TIME
The specific adjustment: e.g. "treat your own Traction scores as roughly one
point lower than they read" — concrete, not a vague "be more careful."

NOT ENOUGH SIGNAL FOR
Anything you noticed but can't support with enough entries yet — name it
without claiming it as a confirmed pattern.
```

If the data only supports "not enough signal yet," say exactly that and stop
there — a thin sample dressed up as a finding is the failure mode this skill
is built to avoid, not commit.
