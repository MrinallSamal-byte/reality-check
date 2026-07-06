# Contributing

Reality Check is one ruleset mirrored across many hosts, plus a set of Claude
skills. Keep changes small and the ruleset honest.

## Editing the ruleset

The single source of truth is `scripts/_ruleset.txt`. If you change it, update
every adapter so they stay byte-identical, then verify:

```
bash scripts/check-rule-copies.sh
```

CI fails if any adapter drifts.

## Adding a host adapter

Drop the ruleset into the file the host reads (see `docs/agent-portability.md`),
add it to the `FILES` list in `scripts/check-rule-copies.sh`, and document it in
the README "Works with" table.

## Benchmarks

`benchmarks/score.py` is deterministic. If you add ideas or change scoring, keep
the honesty caveats in `benchmarks/README.md` accurate. Do **not** add measured
claims you can't reproduce — fabricated numbers are the one thing this project
will not ship.

## Before opening a PR

```
npm run validate
```

Equivalent to running both checks by hand:

```
python3 benchmarks/score.py
bash scripts/check-rule-copies.sh
```
