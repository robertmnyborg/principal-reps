# The system narrative

A different exercise from the 90-second rep. The rep trains retrieval under pressure. This
trains the four-minute answer to "tell me about something you built," which is the question
most likely to decide a Principal loop and the one most often answered as a chronology.

A chronology loses. The build order is not the argument order. Order the beats below and
the same material reads two levels higher.

The running example is a food-delivery marketplace that enhances menu photos with a
vision model. A strong telling spends a fifth of its time on the product and the rest on
the evals.

## The eight beats

**1. Size it before describing it.** One number that makes the room care, one that
surprises. For the example: annual order volume and its growth rate, then a comparison the
room did not expect, such as the delivery side now matching the original business in size.
The surprising number buys attention for the next three minutes.

**2. Why the artifact matters, in one sentence of user behavior.** "A photo is the first
signal a customer gets, and a good one is the difference between scrolling past and adding
to cart." Behavior, not adjectives.

**3. The tension: two constraints that fight.** Consumers want authentic photos, and a
meaningful fraction distrust anything AI-generated. One prompt for every photo collapses
the diversity of the marketplace. Without a tension there is no product problem, only a
task, and a task does not need a Principal. This beat is where the interview is won.

**4. Goals as a numbered list you will be held to.** Five at most, stated **before** the
architecture, so the architecture gets judged against them instead of admired on its own.

**5. Why an agent and not rules, priced at both ends.** Deterministic gives control and
breaks on the tail. Unconstrained gives creativity and no guardrail. Say where you landed
and name the thing that pins you there. Skipping this beat reads as picking the fashionable
tool.

**6. Architecture in one picture, walked once, left to right, with the skip path named.**
The branch where nothing happens carries as much information as the branch where something
does. The example routes each photo to enhance or to skip, and the skip is a first-class
outcome.

**7. Eval per stage, and say that the metric changes shape by stage.** A classifier stage
gets a confusion matrix, precision and recall, and one named guardrail. A generator stage
gets pass@k against a rubric with three outputs, including abstain. Say who agreed the
rubric: product, design, policy, legal. A rubric one engineer wrote is an opinion.

**8. The loops, then the business metric, then the slice.** Drift loop against fresh human
labels, dogfood loop, production loop. Land on the number the business already tracks
(conversion, add-to-cart), then name the cuts you tune on (geo, device, category). Ending
on model quality instead of the business metric is the most common way a strong system
story reads as an engineering story.

## Two rules that run underneath all eight

**Log first, flat, one record per end-to-end run.** Before optimizing anything. A nested
per-stage schema means only the author can query it; a flat record means product, design,
and engineering all slice the same rows. Without it there is nothing to optimize toward,
let alone a self-tuning loop.

**Name failure modes, one picture each.** Faithfulness (added something that was not
there). Completeness (removed something that was). Nugatory change (large diff, no decision
changed, which is reward hacking). Physics and object coherence (the vendor's problem
leaking into yours, which you take back to the vendor). A named taxonomy turns "sometimes
it is bad" into work someone can pick up.

## Scoring a narrative rep

Score the seven default dimensions as usual. Then three gates, each pass or fail, reported
in the five-line cap:

| Gate | Fails when |
|---|---|
| Tension | Beat 3 is missing, so the story describes a task |
| Judged against goals | Goals arrive after the architecture, or never |
| Lands on the business | The last sentence is about model quality |

Budget 240 seconds. Over budget is a failed rep, same as the 90-second rule.
