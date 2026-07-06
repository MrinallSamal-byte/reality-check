---
name: pre-mortem
description: >
  Run a structured pre-mortem on a project or idea — imagine it has already
  failed and work backward to the causes. Use when the user asks "what could go
  wrong", "what are the risks", "why might this fail", "what am I missing",
  "failure modes", or wants to pressure-test a plan before committing. Surfaces
  the most probable and most damaging failure paths, not a generic risk list.
---

# Pre-Mortem

A pre-mortem beats a risk checklist because it forces concreteness. The framing:
*"It's 18 months from now. The project failed. What happened?"* People name real,
specific causes when they're already assumed true, instead of hedged maybes.

## Method

1. **Set the scene.** State the project and a realistic failure horizon (e.g.,
   "two years out, this is dead/abandoned/irrelevant"). Make failure the premise,
   not a possibility.

2. **Generate failure stories across categories.** For each, write the specific
   way *this* project dies — not a generic risk:
   - **Demand** — nobody wanted it / they wanted it but wouldn't pay / the pain wasn't real.
   - **Execution** — couldn't build it, took too long, ran out of money or energy, key person left.
   - **Market / competition** — an incumbent moved, a better-funded rival won, the window closed.
   - **Distribution** — built it, couldn't reach anyone affordably.
   - **Economics** — the math never worked at scale; CAC > LTV; margins too thin.
   - **External** — regulation, platform dependency, a key supplier or API, macro shift.
   - **Founder / team** — wrong skills, lost motivation, co-founder conflict, divided focus.

3. **Rank by likelihood × impact.** Don't treat all risks as equal. A 70%-likely
   project-killer matters far more than a vivid but unlikely one. Put the top
   three at the front.

4. **Convert the top risks into early-warning signs and cheap tests.** For each
   leading risk: what's the earliest signal it's coming true, and what's the
   cheapest experiment that would expose it *now* rather than in 18 months?

## Output structure

```
PRE-MORTEM: <project>
Premise: it's <horizon> from now and this failed.

THE 3 MOST LIKELY WAYS THIS DIES
For each: the failure story (specific), why it's likely, and the earliest warning sign.

FULL FAILURE MAP
Grouped by category, ranked within each. Skip categories that don't apply
rather than padding.

THE ONE RISK TO DE-RISK FIRST
The highest likelihood × impact failure, and the cheapest test that would tell
you within weeks whether it's real.

WHAT WOULD MAKE ME WORRY LESS
The evidence or milestone that would genuinely lower the risk.
```

Be specific and probabilistic, not alarmist. The goal is not to scare the user
off — it's to point a flashlight at the thing most likely to kill the project so
they can deal with it on purpose. Offer **direction-roadmap** to turn the top
risk into a concrete first test, and **assumption-tracker** to log it so it
gets checked instead of forgotten.
