# 2. Proofs and failures: closing gaps, getting out of dead ends

This chapter covers three things: how I tried to close the gaps in the proofs, what I did when every road was blocked, and what failed. The full index is in [`catalog/failures_index.md`](../../catalog/failures_index.md).

Terms as in [Chapter 1](01_history.md): a *note* is a numbered research write-up, a *worker* is a [Claude Code](https://claude.com/claude-code) agent doing a delimited job, an *audit* is a check by an agent other than the author, the *ledgers* ([FAILED](../../data/ledgers/FAILED_E05.md), [PROVED](../../data/ledgers/PROVED_E05.md), and so on) hold the state of the research, and *Rikai* is my textbook site. The *all-λ problem* is the full-sequence problem of showing $h\to\infty$ for all $\lambda$. The *named condition* is an unproved condition singled out as the remaining target, and a *feasibility estimate* is a rough estimate of whether a target is worth attacking.

## 1. Aiming for a proof without gaps

An AI writes proofs fast. The problem is whether they are correct.

The most time in this research went to verifying the AI's output. Up to nearly 100 notes appeared in a day, far too many for me to read alone. So I built many layers of verification, and in the end I read the papers that remain myself.

### How the layers stack

1. **Have another worker break it.** An AI other than the one that wrote the proof rederives the result from the statement alone, without reading the argument. Errors at the joints come out here.
2. **Blind check.** For a lemma written by the auditor, only the statement is handed to another worker, who rebuilds the proof.
3. **Check that the difficulty is conserved.** For a proof that claims to be closed, first check into which term the obstruction that had stopped earlier schemes has moved, and whether it was really dealt with.
4. **Multi-layer verification.** A result whose rate jumps by orders of magnitude goes through 5 layers: blind rederivation, the dependency chain, the check from the opposite side, numerics from an independent implementation, and a check of the reading.
5. **Scoring the papers.** From the start of the paper-writing on October 22, I had auditors with different roles score out of 5. After the recasting, three roles scored: a reader who looks at the rigor of the operator theory, a referee, and a reader who looks at simplification. I iterated until all 6 scorers (3 each for Papers I and II) exceeded 4.5. The first-round scores of 3.9 to 4.2 became 4.6 to 4.7.
6. **Rewriting for Rikai.** Described below.
7. **Another AI's eyes.** An AI other than Claude was given the role of referee, and every point it raised was checked by Claude's audits.
8. **Checking against sources.** Each cited sentence is matched against the original.
9. **My own proofreading.** I read the papers in full, checked the proofs, and proofread repeatedly.

Among the notes, those with an audit type in the name number more than 150.

### Rewriting for Rikai

What worked was rewriting the content of the papers from scratch as research notes on the textbook site [Rikai](https://rikai.mugen-giken.com/) (these notes are for administrators only and not public; the public background articles include [the Pauli–Fierz model](https://rikai.mugen-giken.com/physics/fock-space/pauli-fierz-model), [fibers and the dipole approximation](https://rikai.mugen-giken.com/physics/fock-space/pauli-fierz-fibers-dipole) and [the effective mass of fiber families](https://rikai.mugen-giken.com/physics/fock-space/fiber-effective-mass), in Japanese). For Papers I and II this comes to 7 notes and about 8,200 lines. The density is one a master's student can read, with every step written out. I followed each revision of the papers, and rewrote it 6 times, up to following the CMP version the day after submission.

Auditing workers read with the same premises as the research notes, so they skim over the obvious places. A rewriting worker rederives, so it gets stuck there. Some flaws actually found:

- A remark in Paper II said "whether $h\to\infty$ as $\alpha\to\infty$ is open", but a theorem of the same paper gives $h\gtrsim0.5865\sqrt\alpha$.
- The definition of the side $n_e$ of the electron box did not match between Papers I and II, so a step of Paper I could not be cited as it stood.
- Nothing guaranteed that the window constants hold simultaneously.
- Translation covariance was used without a lemma.
- The power of the distance, $b^{-1/3}$, did not match the count in the text ($b^{-1/2}$).
- A dropped factor, an inconsistent dimension of a constant, a missing domain in a lemma.

All of these survived in a manuscript that had passed the audits. Even if the conclusion does not change, in a paper these are gaps. Every proofreading turned up the next one, so I proofread many times.

### The gaps still remained

I write the Lemma 8.2 gap ([Chapter 1](01_history.md)) once more here. It was pointed out on October 26 and confirmed by audit on the 28th.

This lemma passed the independent-audit layer, passed the top-tier model's "no gaps", passed my own read-through, and went onto arXiv. What found it was yet another AI in the referee role. When I audited the point, the verdict was that the gap is real but the claim is not false and can be repaired.

So I do not write "there is absolutely no gap". What I can write is that I did what could be done to remove gaps, and closed every gap that was found. Before submitting to CMP, I ran again a joint audit of the revised places and 3 independent audits of the full text, and the day after submission I had the Rikai notes follow. The rest is left to refereeing.

### Could it be done elementarily?

The AI's proofs were hard to follow. This truly cost me effort.

Before asking whether they are correct, they were unreadable. The tools are heavy, intermediate steps are left as they were, symbols are used in several senses, and why a step is taken is not written. Since I check things myself, a proof I cannot read is a problem for me. It is the same for readers.

For three days from October 23, I looked into whether it could be done more elementarily.

- Without changing the papers, I had alternative proofs examined paper by paper. The skeleton did not move; only 6 places were replaced, all at the level of lemmas.
- I loosened the condition to keeping only the core of the main theorem, tested about 90 hypotheses, and put them through the joint audit. Six simplifications passed.
- I audited, one by one, 52 simplification proposals from another AI. Some had real insight. The proposal to prove the Neumann floor by an average and the Poincaré inequality, and the one to bound the upper limit by Agmon's inequality for periodic functions, lightened Paper I the most. On the other hand, of the 3 proposals marked "fully verified", one was wrong and two had an effect of about a tenth of what was claimed.
- In the independent audit by the top-tier model, one lemma was replaced by a short alternative proof using only rotation covariance and Schur's lemma.

Examples of simplifications adopted:

| Place | Before | After |
|---|---|---|
| Upper bound of Paper I | Five tools, including a Slepian-type comparison theorem | Jensen's inequality for coherent states |
| Floor of the lower bound of Paper I | Temple's inequality, the Poisson equation, Calderón–Zygmund | A few lines of computation on forms |
| Constructiveness of Paper II | Explicit $\lambda_1$, interval-arithmetic programs, tracking of constants | Dropped. Made the proof nonconstructive |
| Gauge removal in Paper II | Surgery | Detour via Leray's subspace |
| Shell estimate in Paper II | Shell weights, counting, 2 design conditions, 5 constants | One Agmon argument with a soft minimum |

I also added to the introduction of Paper II a reading guide saying what each step hands to the next.

I also learned where the difficulty stays even if the proposition is weakened: three places, namely the non-concentration of the band-limited field, the Agmon argument for the rarity of shells, and the tails at the seams of the functional-integral lemmas. Much of the unreadability came from the arrangement, stacked in the order of research, rather than from the sophistication of the tools. What can be removed was removed, and what remains is truly hard. I went as far as being able to say that.

## 2. When every road is blocked

There were many moments when both the AI and I were stuck. Here are the ways out.

| Phase | What was going on | What I did |
|---|---|---|
| 09-20 Q3 stagnation | For 3 weeks results grew but the question did not move | Instead of instructing, I asked "honestly, how is it?". Had it write a self-assessment and changed the setup |
| 10-06 after freezing Q3 | The routes to the power closed both rigorously and numerically | Reordered the questions from weak to strong |
| 10-18 all 8 trial-family schemes failed | Every scheme closed in the same way | Had it write the common point in one line. Declined a downgrade of the line; left the overall policy to the top-tier model |
| 10-19 the edge condition | A condition from the jump of the sharp cutoff remained | Moved the problem setting itself. Solved first with a smooth-cutoff family |
| 10-20 all λ | The wall of being outside the reach of positivity | Went via a different limit (the strong-coupling functional) |
| 10-21 all angles below 10% feasibility | The AI proposed weakening the target | Declined. Tried even the low-probability angles and had the reasons for closure recorded |
| 10-22 all-out attack did not reduce it | The named condition remained | Judged "the way of naming is wrong" and had 3 workers produce a strategy review |
| 10-22 the exponent jumps from 1/1750 to 6/7 | It had passed audit | Suspected the jump was too big. Five layers of verification showed why (a hidden ceiling of the estimator had simply come to the surface) |

The patterns fall into several types.

**Change the question.** An AI keeps attacking the target it is given. It has difficulty changing how the question is posed. That was the human's job.

**Make it write one line.** Writing in one line what the closed schemes share shows the nature of the wall. The wall of being pushed back to information about the state (September 21) and the wall of being outside the reach of positivity (October 20) are of the same type, and being able to write that led to the turn of going via a different limit instead of extending the reach.

**Doubt the consumer side.** Checking literally the side I had assumed needed a strong input sometimes weakened the requirement itself.

**Do not retreat.** The AI's proposals follow discipline and lean toward saving resources. For both all λ and $\iota$, I declined them. Whether they closed because we continued, or because they were problems that would close, I do not know. In the same period 45 candidates with feasibility estimates of 2% or below were closed.

**Ask several, from different angles.** Having 3 workers review from separate entrances produced, on comparison, the conclusion "the way the condition was named was itself wrong", which a single worker's review does not give.

**Doubt.** Once something passes an audit, the AI has no reason to stop. It was the human who stopped it.

## 3. Record of failures

The about 450 entries of FAILED are about 100 in September and about 350 in October, mostly near the end.

### What the closed schemes had in common

1. Ask first whether it also holds for the dipole model. An inequality that does not use recoil quantitatively holds for the solvable model too. If the solvable model does not have the target property, that input cannot reach it.
2. Before strengthening the supply, question the consumer.
3. Check in advance the direction the tool returns. Positivity, convexity, and Gaussianity often return the opposite of the direction needed.
4. Doubt that a single constant or average can pay for it. The worst point and the tails of distributions do not appear in the average.
5. Difficulty is conserved. Changing the scheme often just moves it to another term.
6. Write the scope of a closure narrowly. Closures written broadly as "impossible in principle" were overturned in audits many times (F30, F44, F63, F64, F383).

### Types of AI errors

The AI's errors concentrated at the joints more than in simple miscalculation.

| Type | Example |
|---|---|
| Overlooking what a constant depends on | Theorem 295-E: the constant swung with a power of the coupling and was not uniform |
| Mismatch with the form on the using side | Proposition 351-C: correct when only the supply side is read, but does not match the quantity on the using side |
| Wrong direction of an inequality | Note 373: the verdict that the difficulty had moved was in the wrong direction |
| Circularity | Note 258: the confluence route written by the top-tier model collapsed with a counterexample and a circularity |
| A lemma that should have passed is false | Lemma 571-H (ii): a verifier-backed line was literally false (F403) |
| Only moving the difficulty | Corollary 639-T′: F449 |
| Overclaimed novelty | Proposition 486-U: correct but already in prior work. "No precedent" was written without stating the scope of the search |
| Missed literature | Note 684: wrote "an upper bound cannot be proved" in exhaustive form, but there was a result of [Fröhlich–Pizzo](https://doi.org/10.1007/s00220-009-0960-8) |
| Overrated self-assessment | Another AI's "fully verified" and "ready for immediate submission" |
| Misreporting a citation | The introduction of Paper II described a result of [Lieb–Loss (2002)](https://doi.org/10.1023/A:1019870931077) inaccurately (corrected in the pre-submission check) |

Within a single note everything looks coherent, so the author worker's self-check does not find these. Confidence of prose has nothing to do with correctness.

### Operational accidents

Failures outside mathematics took just as much time.

- A session edited from a stale working copy and erased additions made by other sessions.
- LaTeX written through a shell heredoc lost half of its `\\`.
- An AI that tried to write a long proof in one go stopped at the output limit, and not a single file remained.
- A command that stops processes by image name also killed jobs of other work.
- The handoff file read at startup swelled to 76KB.

Every one of these became a rule or a hook in [Chapter 4](04_working_with_ai.md).
