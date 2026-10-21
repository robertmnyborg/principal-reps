# Principal Reps

Timed interview reps that train the Principal-level answer pattern until it is automatic.

Fifteen to twenty minutes a day. You get one question, ninety seconds, and one attempt.
You answer out loud. You get a score on seven dimensions and at most five lines of
feedback. That is the whole loop.

## The pattern being trained

**What wasn't defined, what I claim, what I'd measure, whether it can be undone, what
would prove me wrong.**

Five beats, in order, said in your head before you open your mouth. The middle of any
answer is your existing domain competence. These five are the frame that makes it read at
Principal altitude instead of Senior.

## Two ways to run it

**Claude Code plugin** — full fidelity. Keeps a ledger across sessions, does spaced
repetition on your weakest dimensions, tracks targets for specific roles you are pursuing,
and tells you when to stop.

```
/plugin marketplace add <this-repo>
/plugin install principal-reps
```

Then say `/principal-reps` and answer questions.

**Claude Project** — works on a phone, no install. Everything except persistence. See
`claude-project/SETUP.md`.

## Modes

| Mode | What it does |
|---|---|
| `rep` | One timed question, immediate feedback |
| `set 5` | Five reps back to back, no coaching until the end |
| `weakness` | Only questions loading your failing dimensions |
| `pattern` | The five beats alone, thirty seconds, ten in a row |
| `narrative` | The four-minute "tell me about something you built" story |
| `live` | Postmortem after a real interview |
| `report` | Where you stand |

## The rubric

Ambiguity, Scope, Technical, Operations, Mechanism, Cheapest test, Reversibility. Each
scored 0-3. The rubric is the author's own synthesis of what separates a Principal answer
from a Senior one. A 2 means the beat was present. A 3 means it would survive a hostile
senior interviewer. Early sessions are mostly 1s and 2s. That is the
point.

## It is built to retire itself

The kill condition is every dimension averaging 2.0 or better across your last fifteen
reps. When you pass it, stop. Run reps from the printed card and a kitchen timer instead.
A training tool you never graduate from is a habit, not a skill.
