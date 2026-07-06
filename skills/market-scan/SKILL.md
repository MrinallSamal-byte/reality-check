---
name: market-scan
description: >
  Research whether an idea's market is real using live web search instead of
  guessing. Use when the user asks "who else does this", "are there competitors",
  "is the market real", "how big is the market", "has this been tried before", or
  needs the competitive landscape for an idea. Reports what was actually found and
  is explicit about what could not be verified.
---

# Market Scan

Find out what's really out there before forming an opinion. The failure mode this
skill exists to prevent is confident claims about a market built on nothing. Use
live web search; do not rely on memory for anything that changes over time
(who exists, funding, pricing, market size).

## Method

1. **Frame the search.** From the idea, derive the category, the job-to-be-done,
   and the likely customer. Search for each — products rarely call themselves what
   the founder calls them.

2. **Search in layers** (use the web search tool for each):
   - **Direct competitors** — products doing the same thing.
   - **Indirect / substitutes** — what people use *instead* today, including
     spreadsheets, manual processes, and "nothing." The substitute is often the
     real competitor.
   - **Prior attempts** — companies that tried this and died. Why they failed is
     gold; search "[category] shut down", "why [startup] failed".
   - **Market size & trend** — is this growing, flat, or shrinking? Look for real
     figures and note the source and date.
   - **Recent activity** — funding, launches, acquisitions in the last 1–2 years.
     A crowded, well-funded space and a dead-silent space are both warnings, for
     opposite reasons.

3. **Verify before stating.** Every concrete claim (a competitor exists, a number,
   a shutdown) must trace to a source you actually found. If you couldn't verify
   it, say "couldn't confirm" rather than asserting it.

## Output structure

```
MARKET SCAN: <idea in a phrase>

THE SHORT ANSWER
Is the market real, crowded, empty, or dying? One honest paragraph.

DIRECT COMPETITORS
Name — what they do — how they're positioned — (link). Note the strongest one.

WHAT PEOPLE USE TODAY INSTEAD
The real incumbent is often a substitute, not a competitor.

PRIOR ATTEMPTS & WHY THEY DIED
What's been tried and what killed it. The most useful section.

MARKET SIZE & DIRECTION
Figures with sources and dates. Flag anything you couldn't verify.

WHAT THIS MEANS FOR THE IDEA
The honest read. An empty market may mean "no demand," not "open field."
A crowded market may mean "validated demand," not "too late." Say which, and why.

COULDN'T VERIFY
List what you searched for but couldn't pin down, so the user knows the gaps.
```

Always include a **Sources** section with the links you actually used. If web
search is unavailable, say so plainly and switch to reasoning from general
knowledge — clearly labeled as unverified — rather than pretending to have looked.
Then offer to run **validate-idea** with these findings folded in.
