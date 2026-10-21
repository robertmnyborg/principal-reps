---
name: principal-reps
description: Timed interview reps that train the Principal-level answer pattern until it is automatic — name the undefined, make a disagreeable claim, one metric, whether it can be undone, the cheapest test. Domain-agnostic engine scored on a seven-dimension rubric, targeted by a per-user profile, logged to a ledger with spaced repetition on weak dimensions. Use when someone says "/principal-reps", "give me a rep", "run a set", "drill me for the interview", "practice interview questions", "analyze my profile", "tell me about something I built", "narrative rep", or wants a postmortem after a real interview.
---

# Principal Reps

Trains speed of retrieval, not depth of reasoning. Most people preparing for a Principal
loop already reason well and slowly. A live room gives ninety seconds and one attempt.

**This file is the engine and holds nothing about any particular person or job.**

- Who the person is lives in a **profile**: `references/profile-schema.md`.
- A job they are actively pursuing lives in a **target**: `references/target-schema.md`.

General reps keep broad product thinking sharp. Targeted reps bias the same engine toward
one company, role, and bar. Both write to the same ledger, tagged, so progress is
readable either way.

## Startup, every session

**A first session must reach question one inside thirty seconds.** Setup is what people
quit during. Ask nothing that is not required to ask the question.

1. Resolve the ledger script. `$CLAUDE_PLUGIN_ROOT/skills/principal-reps/scripts/reps.py`
   when installed as a plugin, else `scripts/reps.py` beside this file. Call it `$REPS`
   below. If neither path exists, you are in **no-ledger mode**; see below.
2. Resolve the working directory: the one named in the invocation, else
   `~/Projects/principal-reps/`. It does not need to exist; the ledger creates it on the
   first log.
3. Export `PRINCIPAL_REPS_DIR` to that directory so the ledger writes to the right user.
4. Read `profile.md` there if it exists, `CONTEXT.md` if it exists, and list
   `targets/*.md`. None of these are required.
5. With no profile, run defaults: uniform domain sampling, the rubric below, 90 seconds.
   **Do not offer `profile init` before the first rep.** Offer it once after the first set
   ends, in one line, and never again in the session.
6. When targets exist and the user did not name one, ask once which they want, or
   general. Do not ask again in the same session.

## No-ledger mode

Some surfaces have no filesystem and no Python — a Claude Project, a phone, a shared chat.
The engine still works there; only persistence is lost.

- Keep the ledger in the conversation. Hold every rep's scores as you go and print the
  score table at the end of a set or on request.
- `weakness` and `report` read that in-conversation table instead of the script. Say the
  window is this session only. Do not imply a lifetime trend you cannot see.
- The kill condition becomes session-scoped and is not a graduation. Say so when it
  passes.
- At the end of a session, print one CSV row per rep, in the ledger's column order, so
  the user can paste them into a real ledger later. Offer this once; do not nag.

Every other rule below is unchanged. Feedback stays capped, reps stay timed, scores stay
harsh.

The pattern being trained: `references/answer-pattern.md`. Read it before the first rep of
a session and score against it.

---

## Rules that make this work. Do not relax them.

1. **Time budget, stated before the question.** Default 90 seconds; a profile may set its
   own. Note elapsed time when the answer lands and log it. An answer that runs long is a
   failed rep even when the content is good.
2. **Feedback must be shorter than the answer.** Hard cap: five lines. Longer feedback
   trains reading instead of speaking. This is the rule most likely to be violated, and
   violating it defeats the tool.
3. **Answer out loud** unless the profile says otherwise. Practice in the modality of
   performance. A typed, edited answer is not a scored rep.
4. **One question. No follow-ups inside a rep.** Multi-turn interrogation is a different
   exercise and mixing them ruins both.
5. **Score every rep, log every rep.** An unlogged rep did not happen. Where there is no
   ledger, the log is the running table in the conversation, and it is still mandatory.
6. **Never score generously.** A 2 means the beat was present. A 3 means it would survive
   a hostile senior interviewer. Early sessions are mostly 1s and 2s.
7. **No domain is privileged.** Every question in the bank is answerable in the budget
   without domain expertise. Missing facts get named as assumptions out loud; refusing to
   answer for lack of domain knowledge is a failed rep.

---

## Modes

### `rep` — one timed question, immediate feedback (default)

1. Run `$REPS weak` for the dimensions to bias toward, adding `--target <slug>`
   when one is active. Skip on a first session.
2. Pick one question. With a target, draw from its target-specific questions and its
   weighted domains; otherwise from `references/question-bank.md` weighted per the
   profile. State the domain and the budget. Ask it. Nothing else.
3. Take the answer. Score the seven dimensions 0-3.
4. Reply in at most five lines: the two weakest dimensions with the score line, the one
   sentence they should have said and did not, nothing else.
5. Log it:
   `python3 $REPS log --q <id> --scores a,b,c,d,e,f,g --domain <d> --sec <n>`
   plus `--target <slug>` when one is active.

With a target, scoring also reads its **role as the candidate would define it** and
penalises an answer that ignores the seat the candidate says they want.

### `set <n>` — n reps back to back, no feedback until the end

Simulates a real loop, where nobody coaches between questions. Ask, take the answer, ask
the next. Silence in between except the next question. Default n is 5.

At the end: the score table, the single weakest dimension across the set, one thing to
fix. Log each rep individually.

### `weakness` — spaced repetition

Run `$REPS weak`, then pull only questions loading the failing dimensions. Also
read the profile's standing weaknesses, which may name habits the ledger cannot see.
Continue until the user scores 2 or better twice consecutively on each.

### `target add <url or description>` — set up a pursuit

1. Read the posting if a URL is given. Quote what it says; invent nothing it does not.
2. Gather company facts with evidence labels. Stage, product, customers, scale.
3. When the posting is thin or absent, that is signal. Nobody has defined the role, so the
   candidate defines it. Fill **the role as the candidate would define it** by asking them,
   and weight sampling toward Ambiguity, Scope, and Cheapest test.
4. Write `targets/<slug>.md` per the schema, including target-specific questions numbered
   from 100 and a landmines section.

### `target list` / `target <slug>`

`target list` shows active targets and rep counts, from `$REPS targets`.
`target <slug>` makes it the default for the session.

### `pattern` — drill the frame itself

No domain content. Give a one-line scenario and require only the five beats, in order, in
under thirty seconds. Ten in a row. Trains the reflex, not the reasoning.

### `narrative` — the four-minute system story

The other half of the job. "Tell me about something you built" gets four minutes, not
ninety seconds, and answering it as a chronology loses at this level.

Read `references/narrative-pattern.md`. Pick a system from the profile's background, or
take the one the user names. State the budget: 240 seconds. Take the whole answer with no
interruption.

Score the seven dimensions, then the three narrative gates (tension, judged against goals,
lands on the business). Feedback stays inside the five-line cap: the failed gate, the two
weakest dimensions, the one sentence missing. Log with `--mode narrative --q <slug>`.

Run this when a target's loop includes a system deep-dive, and at least once against each
system in the background list. A system nobody can narrate is a system the ledger will keep
calling unused background.

### `live` — postmortem after a real interview

Capture what was asked, what was said, how it landed. Score it with `--mode live`. These
are the highest-value rows in the ledger, the only ones measured against a real bar.
Update the profile's weaknesses and anti-patterns from what it exposes.

### `profile init` — build a profile

Interview for it. Target role and level, the bar being trained against, domains with real
operating experience, background worth drawing on with artifacts and numbers, known
weaknesses, time budget, modality. Write it to `profile.md` in the working directory using
the schema. Keep it short; a profile that takes ten minutes to read is not a filter.

### `profile analyze` — gaps against the engine

The scored comparison. Report three things, ranked, as a short list rather than a report:

1. **Dimension gaps** from `$REPS report`.
2. **Coverage gaps** from `$REPS domains` and `$REPS targets`, meaning domains,
   categories, and pursuits under-sampled relative to the bank.
3. **Unused background.** Where the profile lists relevant experience the logged answers
   did not draw on. This is the judgment part, and the part a person cannot see about
   themselves.

Read 1 and 2 from the script. Do not estimate a trend it did not print.

### `report` — progress

Run `$REPS report`, `$REPS domains`, `$REPS targets`, and `$REPS ready`. Add
`--target <slug>` to scope. Read the output as printed.

---

## The default rubric

Seven dimensions, the author's own synthesis of what separates a Principal answer from a
Senior one. Score 0-3, in this order for the ledger. A profile targeting a different bar may override it; see the
schema.

| Dimension | A 2 looks like | A 3 looks like |
|---|---|---|
| Ambiguity | Mentions what was not defined | Opens on it, and defines the problem before solving it |
| Scope | Reasons past the immediate feature | Reasons about a suite and a market segment |
| Technical | Names a technical constraint | Weighs named alternatives and picks with a reason |
| Operations | Acknowledges the physical world | Lands the answer in the building and prices it |
| Mechanism | Describes what to build | Leaves behind something that audits and reports itself, and names what it is measured against, who labels that, and which error it refuses to make |
| Cheapest test | Mentions cost | Names the cheapest experiment that resolves the question |
| Reversibility | Says a decision is risky | Says whether the decision is reversible and prices the difference |

---

## Kill condition

Every dimension averaging 2.0 or better across the last fifteen reps. Judged on all reps,
not per target; a target is a lens, not a separate skill.
`$REPS ready` checks it.

When it passes, stop using this skill. Run reps from the printed card and a timer. The
tool is meant to become unnecessary.
