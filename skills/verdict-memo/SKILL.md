---
name: verdict-memo
description: >
  Export a completed validate-idea or pitch-critique verdict as a clean,
  shareable one-page markdown memo — for a cofounder, investor, or teammate
  who wasn't in this conversation. Use when the user asks "make this
  shareable", "write this up", "export the verdict", "give me something I
  can send", "turn this into a memo", or wants the assessment as a standalone
  document rather than left in the chat. Distinct from idea-journal, which
  is a private running log, not something meant to be sent to someone else.
---

# Verdict Memo

A verdict that only exists in a chat transcript doesn't help the user
convince a cofounder or brief an investor. This skill turns the most recent
assessment into a document a stranger can read cold — no protocol jargon, no
tag syntax, no reference to "the load-bearing assumption" as a term of art.

## Method

1. **Identify the source.** Use the most recent **validate-idea** or
   **pitch-critique** output in this conversation. If more than one verdict
   exists and it's unclear which to export, ask.

2. **Rewrite for an outside reader**, not summarize for one who was already
   here:
   - Translate `[FACT]` / `[ASSUMPTION]` / `[UNKNOWN]` tags into plain
     sentences ("this is confirmed," "this is still unproven").
   - Drop internal framing ("the Reality Check Protocol," rung numbers) —
     the reader doesn't need to know a tool produced this.
   - Keep the substance exactly as harsh or as positive as the original.
     This is not the place to soften a real problem for an outside audience —
     if anything, a memo going to a cofounder or investor needs the honest
     verdict more than a private chat does.

3. **Keep it to one page.** Cut supporting detail that doesn't change the
   verdict; keep everything that does.

4. **Save it** as `<idea-slug>-memo.md` in the working folder (slug from the
   idea name, lowercase, hyphenated) and confirm the filename in one line.

## Output structure (the memo itself)

```
# <Idea name> — Assessment

**Bottom line:** <verdict, one sentence, no hedging>

## The idea
One or two plain sentences.

## The key risk
The single belief this depends on, and how solid it is.

## The case against
The strongest honest objection — stated as it would be to your face, not
softened for an audience.

## What's genuinely working
Only what's earned — omit this section entirely if nothing survived the
critique, rather than manufacturing a silver lining.

## Recommendation
The verdict and the one thing that would change it, in plain language.
```

Confirm what was written and where. Offer **idea-journal** to log that this
memo was produced, so the private record and the shared document stay linked.
