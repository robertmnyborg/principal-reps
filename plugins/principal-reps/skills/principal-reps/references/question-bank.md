# Question bank

Domain-tagged. Tags drive sampling and coverage reporting; no domain is privileged.

Every question is answerable in 90 seconds by someone running the five beats, without
domain expertise. If a question needs facts the answerer does not have, that is the
answer: name the assumption out loud and proceed. Refusing to answer for lack of domain
knowledge is a failed rep.

A profile may mark some domains as familiar. That weights sampling toward the rest. It
never removes a domain from the bank.

## Ambiguity — the problem is not defined

1. [logistics] You are handed a team and told "make delivery better." Nothing else. First
   week, what do you do?
2. [payments] Leadership believes checkout abandonment is a UX problem. You suspect it is
   not. How do you find out without building anything?
3. [devtools] Two orgs both claim they own the developer onboarding experience. Neither
   will give it up. What do you do?
4. [healthcare] A product is used daily and nobody can say what it is for. Kill it or keep
   it?
5. [marketplace] You inherit a roadmap of eleven committed features and believe three
   matter. What is your first move?

## Metrics — definition and gaming

6. [ads] Your team is goaled on click-through rate and it is rising. Why might that be
   bad news?
7. [streaming] Name one input metric for content discovery. Say what it does when
   discovery works perfectly and watch time does not move.
8. [b2b] Your primary metric improves when the team does less work. Diagnose and fix.
9. [insurance] Claims processing time is down 40% and customer satisfaction is flat.
   Explain.
10. [logistics] You can have one new metric or one new feature. Which, and why.

## Mechanism — decision logic someone else can run

11. [marketplace] Write the policy for when a seller gets suspended, so two people would
    reach the same verdict on the same case.
12. [payments] Design the rule for when a transaction gets held for review. What differs
    by amount, by merchant, by geography?
13. [devices] A device needs a firmware update that may brick 0.01% of units. Write the
    rollout policy.
14. [energy] Write the rule for when the system sheds load. Who is exempt and why?

## System design and failure

15. [ads] Where is the ranking decision computed, and how fresh does it need to be? Name
    the alternative you rejected.
16. [b2b] Your core service is down. Name the degradation ladder before the happy path.
17. [payments] Your data says one thing, the physical world says another. Which do you
    trust, and does the answer change by category?
18. [streaming] Give the latency budget for the thing on the critical path, and say what
    you would sacrifice to hold it.

## Data contracts

19. [healthcare] Name a metric your organization reports that nothing actually emits.
20. [logistics] You get one new event stream. Which one, and what decision does it unblock?
21. [ads] Your thesis depends on a number that does not exist today. What has to be
    emitted, by whom, over what window, for it to exist?
22. [marketplace] Your quality metric is based on complaints. Most unhappy customers never
    complain. What is the unbiased version?

## Operations and the physical world

23. [logistics] Your software answer requires a person to do something new. Who, where in
    their day, and what does it displace?
24. [retail] The fix requires a change in a supplier contract. What term, and what happens
    in the market where you cannot enforce it?
25. [devices] Returns are up. Walk the unit from the customer's hands back to a decision.
26. [energy] The constraint looks like software and is actually capital equipment. How
    would you know the difference before spending a year on it?

## Scale and multi-market

27. [payments] Take the thing you just designed to a new country. What is genuinely
    global, what only looks global?
28. [marketplace] What is the first thing to fail in market two, and what does that failure
    cost?
29. [b2b] Name one thing you would refuse to launch without. What do you do if a market
    cannot provide it?
30. [streaming] You have a pilot market that worked. Why might that be evidence of nothing?

## Reversibility

31. [any] In the thing you just described, name the decision that cannot be undone. If
    there isn't one, say so and defend it.
32. [payments] What would you spend $250k to be certain of before committing?
33. [devtools] Name a decision your team treats as reversible that is not.
34. [healthcare] You have to choose now with incomplete information. What makes that
    acceptable here and unacceptable elsewhere?

## The cheapest test

35. [any] Describe the cheapest experiment that resolves your central assumption. Name the
    cost, the duration, and the decision it settles.
36. [ads] You are given $X. State the $Y it has to return and the leanest path to it.
37. [b2b] You could answer this with a year of observational data or a two-week holdout.
    Defend the choice.
38. [logistics] Your test came back ambiguous. Now what, and what does that cost?

## Hostile and personal

39. Your most recent work was at a company operating at a very different scale from this
    one. Why does it transfer?
40. Something you built failed. Own the decision, not the circumstances.
41. What is the strongest argument that you are a Senior PM rather than a Principal?
42. Give a number you are confident in and say how you would defend it under challenge.
43. You have been away from this industry for five years. What did you miss?
44. Name the part of your own proposal you are least sure about.

## Robotics and physical AI

45. [robotics] Is the binding constraint fleet size or hours delivered per robot? Say how
    you would tell the difference from data you could actually get.
46. [robotics] A robot needs a human intervention every N tasks. What is N at the point
    you would ship, and what sets that number?
47. [robotics] Define cost per site onboarded, every term named. Which term dominates and
    why?
48. [robotics] It works in simulation and fails on site. What do you instrument before
    touching the model?
49. [robotics] Write the policy for when the robot acts alone versus asks a human. What
    differs by task, by site, by time of day?
50. [robotics] Remote operator minutes per robot-hour is rising. Diagnose three causes and
    say which you would rule out first.
51. [robotics] A pilot converted. Name the leading indicators that resolved inside the
    pilot rather than after it.
52. [robotics] A mechanical revision cannot be rolled back on units already deployed.
    Walk the decision.
53. [robotics] What must a unit emit per shift for fleet payback to be computable at all?
54. [robotics] Site one works and site twelve does not. What did you assume was global
    that was not?
55. [robotics] Who is the buyer, and is the pitch displaced labor cost or something else?
    Defend the choice.
56. [robotics] Build, buy, or fine-tune the perception stack. Pick one and name what you
    gave up.
57. [robotics] Downtime is 12% and the customer has not complained. Is that a problem?
58. [robotics] The model is calibrated correctly and the deployment still does not pay.
    Where do you look?

## Further domains

59. [semiconductors] Yield on a new process node is below plan. What do you own and what
    do you escalate?
60. [aviation] A maintenance interval is set by regulation and your data says it is wrong
    in both directions. What do you do?
61. [telecom] Capacity planning for a market you cannot survey. How do you decide?
62. [agriculture] The customer's decision window is four days long and happens twice a
    year. What does that do to your product?
63. [gaming] Engagement is up and revenue is flat. Name the three explanations and the
    cheapest test that separates them.
64. [education] Your metric is a proxy for a thing you cannot measure for two years. How
    do you avoid optimizing the proxy?

## Evals and ground truth

Every question here is answerable without knowing the domain. The failure mode being
trained against is naming a model or a metric and stopping before the ground truth.

65. [ads] Your classifier is 92% accurate on the eval set. Ship or not?
66. [marketplace] Two labelers disagree on a fifth of your set. What do you fix before you
    touch the model?
67. [logistics] No ground truth exists and there is no budget for labels. How do you know
    the thing works?
68. [healthcare] Something you shipped six months ago. How do you know it still works
    today?
69. [devtools] Your gate blocks 3% of good work and passes 1% of bad work. Which number do
    you tune, and what does that cost?
70. [streaming] The output looks completely different and means the same thing. Win or not?
71. [b2b] You can label 500 examples, once. Which 500?
72. [insurance] The eval set says the new version is better and production says it is
    worse. Where do you look first?
73. [robotics] A model grades your model's output. Who grades the grader, and what do you
    do with "unsure"?
74. [payments] The team wants to fold every production failure back into the eval set.
    Argue both sides in a minute.
