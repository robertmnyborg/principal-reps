# Profile schema

The core skill is the engine. A profile is the per-user context that targets it. Without a
profile the engine runs with defaults: uniform domain sampling, the default rubric, a
90-second budget.

A profile never changes the rubric's meaning. It changes what gets sampled, what gets
over-weighted, and what a good answer would have drawn on.

## Location

`<workdir>/profile.md`, beside that user's `reps.csv`. One directory per user. The skill
looks for a profile in the working directory named in the invocation, then in
`~/Projects/principal-reps/`.

## Format

```markdown
---
name: <who this is>
target_role: <role and level being trained for>
target_org: <org, if the bar is org-specific; omit otherwise>
rubric: default
time_budget_sec: 90
modality: voice | typed
---

## Familiar domains
Domains with real operating experience. Weights sampling toward the rest. Never excludes.

## Background
What they can legitimately draw on, one line each, with the artifact or number where one
exists. Used to judge whether an answer under-used what the person actually has.

## Standing weaknesses
Ranked, most persistent first. Maintained from the ledger and from any long-form
descents. This is what `weakness` mode samples against.

## Anti-patterns
Personal tells, distinct from weak dimensions. A weakness is a missing beat. An
anti-pattern is a habit that actively costs points.

## Reusable lines
Formulations that survived hostile pressure. Scoring should notice when one of these
would have fit and was not used.

## Notes
Anything else that changes how a rep should be judged.
```

## Rubric override

`rubric: default` uses the seven dimensions in SKILL.md. A profile targeting a different bar sets `rubric: <path>` to a file with the
same table shape: dimension, what a 2 looks like, what a 3 looks like. The ledger's column
order must match the rubric's row order, so changing rubric means starting a new ledger.

## Analysis

`profile analyze` reads the profile plus the ledger and reports three things:

1. **Dimension gaps.** Which rubric dimensions sit below the bar, from `reps.py report`.
2. **Coverage gaps.** Which domains and question categories are under-sampled, from
   `reps.py domains`. Both are arithmetic, so read them from the script rather than
   estimating.
3. **Unused background.** Where the profile lists relevant experience the answers did not
   draw on. This is judgment, and it is the part a person cannot see about themselves.

Output is a short ranked list of what to drill next. Not a report.
