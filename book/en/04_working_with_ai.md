# 4. Working with AI: the setup I ended up with

This chapter describes the form that settled after much trial and error. The actual rules are in [`rules/`](../../rules/).

## 1. Division of labor

| Who | What they do |
|---|---|
| Me | Posing the question, prioritizing goals, doubting, registering main theorems, proofreading the papers, deciding on submission and publication |
| Lead session (the AI that oversees the whole) | Design, task instructions, pulling results together, linking the ledgers |
| Subagents (the AIs doing the work) | Writing out proofs, audits, numerics, checking literature |

Writing out proofs and computing were done by the AI. What to ask, what to claim, where not to stop, and what to doubt, I decided. The principle at the boundary is that the human decides "what to claim" and leaves "how to show it" to the AI. Any change to the wording, quantifiers, or reading of a main theorem requires my approval.

The core was [Claude Code](https://claude.com/claude-code), and other AIs were used for part of the review. A proposal from outside, from whichever AI, was treated as input that had not passed an audit, and was checked in Claude's audit types, separating the wording, the mathematics, and the effect.

Our judgments sometimes diverged. The AI's recommendations leaned toward saving resources, and mine toward not letting go of the question. I declined the proposal to downgrade the all-λ problem (proving $h\to\infty$ for all $\lambda$). On the number of papers, I did not take the lead's three-paper plan and went with two, which other AIs' reviews had also favored.

## 2. Types of agents

| Type | Job |
|---|---|
| [Audit type](../../rules/監査の型.md) (Claude Opus, high effort) | Audits only |
| Writing type (Claude Opus, medium effort) | Proofs, kill-checks (cheap tests that try to kill a proposition before long work), design groundwork, numerics design |
| Mechanical type (Claude Sonnet) | Applying instructed fixes verbatim, linking ledgers |
| Hard-case type (Claude Fable) | Only when I explicitly call it. Rethinking overall policy and independent audits of the papers |

I tried quite a lot to get here.

- In September I fixed Opus at high effort throughout.
- From October 2 I trialed medium effort, and confirmed that differential audits (audits of only the changed parts) saved 20% with almost no reversed verdicts. On October 15 I decided "high is for audits only". On the premise that audits catch errors of the writing step, I concentrated effort on the audits, whose role is to stop errors.
- I also tried delegating to Sonnet, and adopted it only for mechanical application.
- The cap on simultaneous launches moved from 3 and 8 to 6 and 48, then 12, then 4 and 16, and on October 20 it was abolished for this research.
- If the work is cut into small pieces, the usage quota runs out quickly. It settled on handing over 4 to 8 hours per family of unproved conditions and grouping audits by chunk. Agents lost to the usage-quota limit, across the research as a whole, exceeded 33 by early October.

## 3. Ledgers

An AI session does not remember the earlier conversation. So all of the state of the research was put in files. These are the ledgers.

| Ledger | What it holds | How it is written |
|---|---|---|
| [PROVED](../../data/ledgers/PROVED_E05.md) | The master copy of claims whose proofs passed | Append. The body is not changed; corrections pile up as annotations |
| [FAILED](../../data/ledgers/FAILED_E05.md) | Approaches that did not work, with the reason, the scope, and the condition for reopening | Append only |
| [Feasibility estimates](../../data/ledgers/成算_E05.md) | Rough estimates | Append |
| [NUMERICS_FACTS](../../data/ledgers/NUMERICS_FACTS_E05.md) | Numerical facts, one per line | Append, shared across themes |
| Remaining-conditions ledger | Unproved conditions remaining for the main goal | Rewrite |
| [STATEMENT](../../data/ledgers/STATEMENT_G3_E05.md) | The official statements of the main theorems and goals | Changes require my approval |
| STATUS | Current position | Fully rewritten each time, 8KB limit |

The principle fits in one sentence. What must not disappear is append-type, what must be short is rewrite-type, and the full text of a proposition is kept in one place only.

Claims carry a three-level grading: candidate (just written), self-audited (the agent that wrote it tried to break it and it survived), and verifier-backed (passed an independent audit by another agent). But verifier-backed means "checked", not a guarantee of "correct". False entries have actually been found.

FAILED records whether what was abandoned was a scheme, a goal, or the truth of a proposition, and also what is not abandoned. I decided that if the reason for failure is recorded, it counts as an achievement. Because "tried and failed" could count as an achievement, the policy of trying everything was possible.

Progress is measured by the number of remaining unproved conditions. The number of notes written or audits done only creates a feeling of progress.

## 4. Feasibility estimates

This is a rule introduced on September 13. Before a new goal or proposition, a task instruction, a decision to abandon, or a long numerical computation, write at least two independent rough arguments, such as dimensional analysis, the one-loop value, a toy model, a numerical estimate within 5 minutes, or extrapolation from a similar problem. If both are negative, or if not even one can be made, do not proceed to rigorous work.

The ledger has the form "ID / goal / two arguments / verdict / conditions that would break it / date", and the verdict is one of "has prospect", "no prospect", or "conditional". I have not tallied the hit rate.

What worked best was killing false goals cheaply. For example, for "is the power 2/3 or 5/7?", a two-line estimate stopped the plan to decide it numerically: the difference is only $\lambda^{1/21}$, invisible at reachable $\lambda$.

Conversely, the high points of this research lay where the feasibility estimate was low. On October 17 I split the remaining items into "items heading toward a solution" and "basic-research items", and in the basic-research items even angles below 10% feasibility counted as progress if the reason for failure was recorded. All λ was solved after continuing to measure with this yardstick. The feasibility estimate is also a tool for stopping, but I decided whether to stop.

An AI tends to continue rough calculations as if they were proof steps. So values of feasibility estimates are kept only in the feasibility-estimate ledger and never in PROVED. This too was checked by machine.

## 5. All-out attack and its trigger

"All-out attack" is not a term defined in the rules. It is the wording of my instructions, and the actual trigger was my specifying a goal to attack.

| Date | Goal | Content |
|---|---|---|
| 10-20 | The all-λ condition | 8 families at once |
| 10-21 | All λ | "Try everything you can. Everything." 11 agents launched at once |
| 10-22 | $\iota\gt0$ | No limit on the number of agents; about 60 notes |

Before the human trigger I also placed mechanical triggers.

- If three abandonments in a row occur on the same item, write the common point in one line and rebuild the candidate table.
- If the periodic patrol detects a stagnation such as the ledger not moving for 6 hours, enter an overall review.
- If every angle is found to have low feasibility, the lead proposes resetting the goal. Whether to accept is my decision.

What moved things after the all-out attack was less the attack itself than the review saying "the way of naming is different" (the way the unproved conditions were set up is different). Brute force worked for eliminating bad roads and making a map.

## 6. Harness and hooks

I replaced most rules that were not kept with hooks (automatically run checks). An AI that reads the text of a rule does not follow it when busy or when the context is long. When I had given the same instruction three times, I stopped instructing and built a mechanism.

In the end there were 10 Claude Code hooks and 2 git hooks.

| When | Hook | What it prevents |
|---|---|---|
| Startup | Sync | Working from a stale state |
| Startup | Literature intake | Missing the import of sources that were obtained |
| Startup | Recording the session ID | Losing track of whose work it is |
| Before edit or instruction | `fresh-remote` | Rolling back additions by other sessions |
| Before edit or instruction | `inbox` | Unprocessed rule changes |
| Before edit or instruction | `require-outlook` | Instructions lacking a feasibility estimate, a check of whether it is already solved, or a ledger item |
| Before edit or instruction | `require-jobgate` | Jobs that do not satisfy the pre-launch rules |
| After work | Literature post-processing | Leftover not-yet-obtained lists |
| After work | Post-processing of job submission | The lead not waking when a job completes |
| Before stopping | `require-ready-empty` | Stopping with instructions still to give, or stopping without patrolling when few agents are running |
| commit, push | NUM check | Duplicate numbers of numerical facts |

The mechanism that keeps the lead from stopping worked best.

The lead would stop merely because it was waiting for a computation, and each time I said "list what can be done now and start on it". So I made three layers.

1. **The instruction queue READY.** When the lead tries to stop, a hook reads the table, and if instructions remain to be given, it does not let it stop (October 19).
2. **The periodic patrol [`g-patrol`](../../rules/g-patrol.md).** Every hour it goes through receiving job results, jobs waiting to be submitted, READY, replenishment, review of stagnation, and checkpoints (October 21).
3. **The hook before stopping.** If fewer than 3 agents are running and there is no patrol record in the last 20 minutes, it does not let it stop.

The subagents' working habits also come mostly from accidents. Subagents do not touch git. They do not write to ledgers directly either, but put finished text in an inbox. Task instructions are written in files, not in conversation. A work log gets its skeleton first, and one write is about 150 lines.

Revisions of the rules came to [87](../../rules/規約の改訂履歴.md) between September 2 and October 27. There are arguably too many. Few rules turned out to be off the mark, and reviewing them is the next task.

## 7. How I verified the enormous output

In the five days from October 19, about 500 notes were written, and I cannot read all of them. This is where I struggled most, and it is still not completely solved.

I did three things.

**Narrow what I read.** Reports were reduced to the verdict table and the recommendation, and items for approval were written one line per item. I set six criteria for notification, and promotions of individual lemmas are not reported. Negative progress is reported with the same weight as positive progress, because AI reports lean toward the side of results.

**Have machines match.** Fix instructions quote the file and the surrounding text verbatim, and the number applied is counted. Numerical results are tied to their outputs by hash. The formulas and numbers of the Japanese version were matched against the English version by script.

**Read the outcome.** I do not read all the notes. Instead, I read in full the papers that remain at the end, checked the proofs, and proofread repeatedly. I did not read the several hundred notes.

Since the auditors are AIs, audits read the same notes and share blind spots. As Lemma 8.2 showed, more layers reduce the blind spots, but they do not reach zero. This is no substitute for confirmation by human experts, so I submitted the papers.

## 8. Looking back

What worked:

- Separate the AI that writes from the AI that breaks.
- Reorder the questions from weak to strong.
- Count reasons for failure as achievements.
- Make rules a mechanism, not wording.
- Create occasions to ask the AI to "evaluate honestly".
- Rewrite the paper in another form and read it myself.

What was wasted:

- The September skew toward calibration.
- Treating an equivalent rephrasing as a new goal.
- Burning the usage quota on finely cut tasks.
- Making the paper in the order of the research, which took several days to recast.

I do not much feel that using AI makes research easier. Proofs come out fast, but the work needed before one can say they are correct has, if anything, increased. I hope this record can serve as an example of that.
