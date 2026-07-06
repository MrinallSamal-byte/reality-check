---
name: discovery-script
description: >
  Turn "go talk to potential customers" into an actual, usable interview
  script aimed at the idea's riskiest assumption. Use when the user asks
  "what should I ask users", "give me interview questions", "customer
  discovery script", "help me validate this by talking to people", "how do I
  test this with real users", or after direction-roadmap names talking to
  real users as the cheapest first test. Produces concrete questions, not
  generic interviewing advice.
---

# Discovery Script

"Talk to 10 real users" is the standard advice in **direction-roadmap** and
the Problem/Path-to-traction rubric dimensions — and the standard failure
mode is that nobody writes the actual script, so the conversations end up
pitching the idea and collecting polite nods instead of testing anything.
This skill writes the script.

## Method

1. **Get the load-bearing assumption.** Pull it from a recent
   **validate-idea** or **pre-mortem** run in this conversation. If none has
   run, ask for the idea and identify the assumption now — the script is
   worthless without a specific belief to test.

2. **Identify who to talk to.** Name the specific person (not "users" — "a
   solo physiotherapist who currently books appointments by phone") based on
   the idea's stated customer.

3. **Write the script in this order:**
   - **Opening** — questions about their current situation and behavior,
     asked *before* the idea is mentioned at all. If the idea comes up first,
     every answer after it is contaminated by politeness.
   - **Core questions** — aimed squarely at the load-bearing assumption. Ask
     about what they do today and what they've already tried, not what they
     would hypothetically do.
   - **The kill question** — the one question whose likely honest answer
     would falsify the assumption. Name it explicitly so the user knows what
     a bad sign looks like, not just a good one.
   - **What NOT to ask** — flag leading questions and "would you use this /
     would you pay for this" hypotheticals by name; they reliably produce
     false positives because people are polite about imaginary products.

4. **Say what counts as signal.** How many conversations, and what pattern in
   the answers (not just "positive vibes") would actually move the verdict.

## Output structure

```
DISCOVERY SCRIPT: <idea>
Testing: <the load-bearing assumption, stated plainly>

WHO TO TALK TO
<specific person, not a demographic>

OPENING (don't mention the idea yet)
2-3 questions about their current behavior and pain.

CORE QUESTIONS
3-5 questions aimed at the assumption, in order.

THE KILL QUESTION
The one answer that would tell you the assumption is false.

DON'T ASK
Leading/hypothetical questions to avoid, and why they mislead.

WHAT COUNTS AS SIGNAL
How many people, and what pattern in the answers actually moves the verdict.
```

Offer **assumption-tracker** to log the assumption being tested before the
conversations start, so the result has somewhere to go when it comes back.
