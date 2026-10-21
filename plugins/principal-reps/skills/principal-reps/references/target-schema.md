# Target schema

A **profile** is who the person is. A **target** is one job they are actively pursuing.
General reps keep broad thinking sharp. Targeted reps bias the same engine toward one
company, role, and bar.

Targets never replace the bank or the rubric. They weight sampling, add a small set of
role-specific questions, and change what a scorer treats as a strong answer.

## Location

`<workdir>/targets/<slug>.md`. One file per pursuit. Multiple targets can be active. The
ledger records the target on every rep, so progress is tracked per target and overall.

## Format

```markdown
---
slug: <kebab-case, used in the ledger>
company: <name>
role: <title as posted, or "unspecified">
source: <URL or where this came from>
status: researching | applied | interviewing | closed
posting: full | thin | none
bar: <the rubric to score against; default means the engine's>
---

## What the posting actually says
Quoted or summarised. If there is no posting, say so plainly. Do not invent
responsibilities.

## What the company is
Facts with evidence labels. Stage, product, customers, scale, public numbers. Verified,
reported, or unverified, every one.

## What they screen for
Stated values and observed emphasis. Where this is inferred rather than stated, mark it.

## The role as the candidate would define it
For a thin or absent posting, this is the substance of the target. The candidate proposes
the seat. Sampling and scoring key off this, not off a job description that does not
exist.

## Domain weighting
Which bank domains to over-sample for this target, and why.

## Target-specific questions
Questions a real interviewer at this company would plausibly ask. Numbered from 100 to
keep them clear of the shared bank.

## Landmines
Questions the candidate would rather not be asked, with the honest answer prepared.
```

## How modes use a target

- `rep --target <slug>` and `set --target <slug>` sample from target questions and the
  weighted domains, and score with the target's bar.
- Scoring reads **The role as the candidate would define it** and penalises an answer that
  ignores the seat the candidate claims to want.
- `live` postmortems against this target update its landmines section.
- Without `--target`, reps stay general and log with an empty target.

## The thin-posting case

A general-interest or talent-pool posting carries no responsibilities. Treat that as
signal, not as a gap. Nobody has defined the role, which means the candidate defines it,
and defining an undefined role is the Ambiguity dimension performed rather than described.
For these targets, weight sampling toward Ambiguity, Scope, and Cheapest test, and make the
candidate open every answer by naming the seat.
