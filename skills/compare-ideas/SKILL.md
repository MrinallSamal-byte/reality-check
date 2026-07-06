---
name: compare-ideas
description: >
  Compare and rank several competing ideas head-to-head so the user knows which
  to pursue first. Use when the user has more than one idea and asks "which should
  I do", "which is best", "compare these", "help me pick", "rank these ideas", or
  is choosing between directions. Scores each on the same rubric, ranks them, and
  commits to a recommendation instead of "they all have merit".
---

# Compare Ideas

When someone has several ideas, the worst answer is "they all have potential" —
that's sycophancy dressed as diplomacy and it helps no one choose. Your job is to
force a ranking and defend it. The goal is one clear "do this first," not a
flattering tie.

## Method

1. **List the contenders.** State each idea in one plain sentence so they're
   compared on equal footing. If the user gave two and is clearly torn, that's
   fine — comparison works at any number ≥ 2.

2. **Score each on the same rubric** (Problem, Solution fit, Differentiation,
   Feasibility, Path to traction — 0–10 each; see the validate-idea scoring
   rubric). Use one consistent standard across all of them. Don't grade a pet idea
   on a curve.

3. **Add two comparison-only lenses** that matter when choosing between options:
   - **Fit to *this* user** — skills, resources, unfair advantages, and genuine
     interest. The best idea in the abstract loses to a good idea this person is
     uniquely positioned to win.
   - **Time-to-signal** — how fast and cheaply can they learn whether it works?
     A slightly weaker idea that proves itself in two weeks can beat a stronger one
     that takes a year to test.

4. **Build the comparison table.** Rows = ideas, columns = the rubric dimensions
   + the two lenses + total. Numbers make the tradeoffs legible at a glance.

5. **Rank and commit.** Order them, then give a clear recommendation: which to
   pursue first, which to keep as a backup, and which to drop. Say *why the winner
   wins* — usually it's not the highest average but the best combination of upside
   and cheap, fast validation.

6. **Name the catch.** Every recommendation has a risk. State the main reason the
   top pick could still be wrong, and what would flip the ranking.

## Output structure

```
COMPARING <n> IDEAS

THE CONTENDERS
1. <idea> — one line
2. <idea> — one line
...

SCORECARD
| Idea | Problem | Fit | Diff | Feas | Traction | User-fit | Time-to-signal | Total |
(fill the grid; totals out of 70 with the two extra lenses)

THE RANKING
1st, 2nd, 3rd... each with a one-line reason.

DO THIS FIRST: <winner>
Why it wins — the specific combination that puts it on top, not just the score.

KEEP WARM / DROP
Which to park as a backup and which to let go, honestly.

WHAT WOULD CHANGE THE RANKING
The evidence or change that would reorder this.
```

If the ideas are too different to share a rubric fairly (e.g., a startup vs. a
weekend creative project), say so and compare them on the dimension that actually
decides it for this user. Offer **validate-idea** for a deep dive on the winner and
**idea-journal** to log the decision.
