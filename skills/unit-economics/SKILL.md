---
name: unit-economics
description: >
  Sanity-check the basic unit economics of an idea — CAC vs. LTV, payback
  period, margin — with real (if rough) numbers instead of a rubric mention.
  Use when the user asks "do the unit economics work", "check my CAC and
  LTV", "will this make money", "what should I charge", "does the math work
  at scale", or when validate-idea's Path-to-traction or Feasibility scoring
  depends on the economics actually working out. Uses the user's own
  estimates, flags which inputs are guesses, and never invents numbers to
  fill a gap.
---

# Unit Economics

The scoring rubric asks "does one customer make more than they cost to
acquire and serve?" — but a rubric line isn't math. This skill does the actual
back-of-envelope calculation instead of gesturing at it.

## Method

1. **Gather the inputs.** Ask for whatever isn't already stated:
   - Price (per unit, per month, whatever the model is)
   - Gross margin (or cost to serve, if margin isn't known)
   - Expected customer lifetime (or churn rate — lifetime ≈ 1 / monthly churn)
   - Estimated CAC (cost to acquire one customer through the stated channel)

   If the user has no real number for one, don't invent a precise-looking
   fake — say what a defensible first estimate looks like for their category
   (e.g., "SMB SaaS CAC via cold outreach commonly runs $200-$800; you'll
   only know your real number after the first channel test") and mark it
   `[ASSUMPTION]`, not `[FACT]`.

2. **Do the math, shown, not just the answer:**
   - `LTV = price × gross margin × expected lifetime`
   - `LTV:CAC ratio = LTV / CAC`
   - `Payback period (months) = CAC / (price × gross margin)`

3. **Read the ratio honestly.** Rough, widely-used rules of thumb — not
   universal law, say so:
   - Below 1:1 — the math doesn't work; every customer loses money.
   - 1:1 to 3:1 — thin; works only with a very fast payback or cheap capital.
   - 3:1 or better — a commonly-cited healthy range, but a long payback period
     can still sink a cash-constrained team even at a good ratio.
   - Payback under ~12 months is the more commonly binding constraint for
     early-stage/self-funded teams than the ratio itself.

4. **Name the single input that would change the verdict most** if the
   user's guess for it is wrong — usually CAC, since it's the least-known
   number and the most sensitive to channel choice.

## Output structure

```
UNIT ECONOMICS: <idea>

INPUTS
| Input | Value | Source |
|---|---|---|
Tag each [FACT] / [ASSUMPTION] / [UNKNOWN].

THE MATH
LTV = ...
LTV:CAC = ...
Payback period = ... months

DOES IT WORK RIGHT NOW?
Plain verdict against the rules of thumb above, calibrated to how thin the
inputs are — a 1.2:1 ratio built on three guesses is not "the math works,"
it's "the math is unknown."

THE INPUT THAT MATTERS MOST
Which number, if it's off, flips the verdict — and what it would take to
actually know it (usually: run the channel, don't guess longer).
```

If every input is a guess, the honest verdict is "unknown, not proven" — never
round an all-assumption calculation up to a confident "yes, this works."
Offer **validate-idea** if this surfaces a Feasibility or Path-to-traction gap
that changes the original verdict.
