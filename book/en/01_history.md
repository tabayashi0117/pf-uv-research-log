# 1. History: from the question to the CMP submission

Quotations of my instructions in this book are translated from Japanese.

This is a record of about eight weeks, from September 2 to October 28, 2026. I pursued the question of the ultraviolet limit of the Pauli–Fierz model (PF below) together with [Claude Code](https://claude.com/claude-code). In my research notes it is called "E05".

A paper contains only the road that worked. Here I write down the rest.

A few terms first. A *note* is one numbered research record written during the work. The *ledgers* are the files that hold the state of the research: [PROVED](../../data/ledgers/PROVED_E05.md) (claims whose proofs passed), [FAILED](../../data/ledgers/FAILED_E05.md) (approaches that did not work), and a ledger of *feasibility estimates* (rough estimates of whether a goal is worth attacking), among others. A *subagent* is a Claude Code agent entrusted with a task such as writing a proof, auditing, or running numerics, and the *lead session* (or simply the lead) designs the work, gives the instructions, and pulls the results together. An *audit* is a check of a claim by an agent other than the one that wrote it. An *unproved condition* is a condition given a name as what remains to be shown. A *value* is a number obtained numerically, as distinct from a proved bound.

## The question and the results

The question was a single one. In a model of one nonrelativistic electron coupled to the quantized electromagnetic field, what remains when the photon momentum cutoff $\Lambda$ is sent to infinity?

For the dipole approximation, which drops the phase depending on the electron position, the answer is known. As the cutoff is raised, the effective mass grows in proportion to the cutoff, so if the physical mass is held fixed, the model ends at a finite cutoff. For the full PF model without the approximation, it was not known whether the same thing happens or whether electron recoil produces different behavior. [Lieb–Loss (2002)](https://doi.org/10.1023/A:1019870931077) expected a breakdown but gave no proof, and the suggestion of [Hiroshima–Spohn (2005)](https://doi.org/10.1063/1.1852699) pointed to the opposite side.

I summarized the results in two papers (the author name is my former name, S. Futakuchi).

**Paper I**: [*The sharp leading asymptotics of the self-energy of the spinless Pauli–Fierz model*](https://arxiv.org/abs/2610.34122) ([arXiv:2610.34122](https://arxiv.org/abs/2610.34122))

For the spinless PF model with a sharp cutoff and any fixed $\alpha=e^2/4\pi\gt0$, the ground-state energy satisfies

```math
E_0(\alpha,\Lambda)=(1+o(1))\,c_\alpha\,\alpha^{2/7}\Lambda^{12/7}\qquad(\Lambda\to\infty),\quad c_\alpha=0.99338\ldots
```

[Lieb–Loss (1999)](https://arxiv.org/abs/math-ph/9908020) had squeezed $E_0$ between $\alpha^{1/2}\Lambda^{3/2}$ and $\alpha^{2/7}\Lambda^{12/7}$. So the upper power is sharp up to the constant.

**Paper II**: [*The effective mass of the Pauli–Fierz electron: a cutoff-independent lower bound and the breakdown of mass renormalization*](https://arxiv.org/abs/2610.34125) ([arXiv:2610.34125](https://arxiv.org/abs/2610.34125))

Let $h=m_{\rm eff}/m$ and $\lambda=\Lambda/m$.

- For all $\alpha\gt0$ and $\lambda\ge1$, $h\ge1+\dfrac{0.3441\,\alpha}{1+0.2985\sqrt\alpha+0.1252\,\alpha}$. This lower bound does not depend on the cutoff.
- For fixed $\alpha\gt0$ and any $\epsilon\gt0$, $h\ge\lambda^{8/7-\epsilon}$ once $\lambda$ is large enough. The effective mass grows faster than the cutoff.
- Hence $\iota_{\rm PF}(\alpha)=\inf_{\lambda}h/\lambda\gt0$, and if the physical mass $m_{\rm phys}$ is held fixed, the cutoff is confined to $\Lambda\le m_{\rm phys}/\iota_{\rm PF}(\alpha)$. This is the obstruction that Lieb–Loss predicted.

I posted both to arXiv on October 25, and submitted revised versions to [Communications in Mathematical Physics](https://link.springer.com/journal/220) (CMP) on October 28. Refereeing is still ahead.

## Overall map

| Date | What happened |
|---|---|
| 09-02 | Groundwork. I rederived the one-loop effective mass and matched it with the Hiroshima–Spohn formula as a starting point |
| 09-03 to 09-20 | Frontal attack on the growth law (Q3). Every route to an upper bound failed, and the lower-bound routes converged on a single conjecture. The results passed 100, yet the question came no closer |
| 09-20 to 09-24 | Reviewed the approach and divided the work into 3 lanes (parallel streams of work). Obtained a cutoff-uniform lower bound (the prototype of the first result of the later Paper II) |
| 09-25 to 10-05 | Tried to measure the growth law by path-integral HMC (Hamiltonian Monte Carlo), without resolution, and froze Q3 |
| 10-06 to 10-07 | Reordered the goals from weak to strong. Proved the photon-number escape in 2 days |
| 10-14 to 10-20 | Tried 8 schemes of trial-state families, and all failed. Took a detour through a smooth cutoff and improved the power of $E_0$. Obtained $h\to\infty$ on a set of $\lambda$ of density 1 |
| 10-20 to 10-22 | The wall of "all $\lambda$". FAILED grew by about 300 entries in 3 days. Broke through with Plan I, which goes via a different limit (Theorem 560-T) |
| 10-22 | The leading term of the self-energy was fixed up to the constant (Corollary 563-C). In the all-out attack on $\iota\gt0$, the first proof failed its audit and a rewrite passed (Corollary 639-T″) |
| 10-22 to 10-23 | Began writing Papers A and B, and added Paper C after $\iota\gt0$, making three manuscripts. Also obtained a constructive version and a smooth-cutoff version |
| 10-23 to 10-25 | Elementarized and simplified, recast as 2 papers, and brought in outside eyes |
| 10-25 | Posted to arXiv |
| 10-26 to 10-28 | Referee-role report and audits. Receipt of the $\lambda=1024$ value, repair of the gap in Lemma 8.2, and a check of all citations |
| 10-28 | Submitted to CMP (CIMP-D-26-02346 and 02347) |

As of October 23 there were about 730 numbered notes (about 530 excluding audits), 382 entries in the proof ledger PROVED, about 450 entries in the failure ledger FAILED, 330 entries in the feasibility-estimate ledger, and 283 compute jobs. Most of the notes were written near the end: about 500 in the five days from October 19 alone.

## September: it looked like progress, but it was not

My first job on September 2 was to rederive a quantity whose answer was known. The one-loop effective mass

```math
h=1+\frac{8\alpha}{3\pi}\ln\Bigl(1+\frac{\lambda}{2}\Bigr)
```

agreed with the Hiroshima–Spohn formula, and the coefficient of the next leading term also came out. At this point I fixed the central question as "how does $h(\lambda)$ grow as $\lambda\to\infty$" (Q3).

For the next three weeks I applied every tool I could think of: higher-order perturbation theory, a Bogoliubov-type renormalization group, internal boundary conditions, the diffusion coefficient of the path measure. Every route to an upper bound on $h$ failed. The tools that come from reflection positivity all work only on the lower-bound side. And however I rephrased the lower-bound side, it came back to the assumption on the density of shell photons (H-dens).

On September 21 there were 102 entries in PROVED and about 100 in FAILED. Still, my outlook on Q3 had not moved. More established facts is not the same as being closer to the question. This was the first big lesson, and it later became the rule "measure progress by the number of remaining unproved conditions".

On September 20 I asked the AI three questions. Can this be solved? Is the literature survey sufficient? Is the current task the best one? The answers were harsh. A solution is not near. The literature had been seen only in part. Recent results were skewed toward calibrating the yardsticks. On this basis I reorganized the work into three lanes: numerics, rigorous lower bounds, and flow equations.

The lane with the narrowed question produced a result quickly. I gave up on the growth law and aimed only at this: however high the cutoff is raised, the effective mass stays heavier than the bare mass by a fixed ratio, with no unproved assumption. From a one-photon trial state and known inequalities, a cutoff-uniform lower bound came out on September 23–24. The constant was improved later and became the first result of Paper II.

The numerics lane tried to measure the local exponent by HMC, but the region where one can measure was too far from the region one wants to decide. At the physical coupling, the one-loop logarithm and the next term cross at $\lambda\sim10^7$ to $10^9$. On October 5, I moved Q3 to the status of a conjecture and froze the rigorous decision.

## Early October: changing the question

On October 6 I reset the goals. I stopped aiming straight at the power of the growth law and listed the goals from the weakest.

- (E1) Hold the bare mass fixed and show $h\to\infty$ as $\Lambda\to\infty$ (no requirement on the rate)
- (E2) The ground state escapes from the finite-photon-number sector
- (E3) Determine the power

(E2) was solved in 2 days. The research, which had not moved for a month, started moving from here. Looking back, how the question was posed mattered more than the choice of tools.

(E1) took long. On October 18 I tried 8 schemes of trial-state families, and all 8 failed. On the 19th I could write in one line what the failed families had in common: they were all tested using only information from the same ground state. Once it was clear that the remaining condition for the sharp cutoff came only from the jump on the cutoff sphere, I added a family with a smooth cutoff and aimed there. The edge term no longer appeared at all. At the same time I improved the upper and lower bounds of the self-energy, and on the 20th $h\to\infty$ followed without any unproved condition, first on a set of $\lambda$ of logarithmic density 1 and then of natural density 1.

What remained was the outside of the density-1 set, that is, proving it for all $\lambda$ (the "all-$\lambda$ problem" below).

## The wall of all $\lambda$ (October 20–22)

This was the longest wall of the research. On the 20th alone, notes numbered "all-λ 1" through "all-λ 28" were written. Monotonicity, concavity, correlation inequalities, bootstrap, and Malliavin calculus were all tried, and every one stopped at the same place. What the failed approaches had in common fit in one line: positivity of functional integrals gives information only in the direction of a lower bound, and what the all-$\lambda$ problem needs lies beyond that.

On the 21st, the AI proposed moving the all-$\lambda$ problem to a lower-priority goal as an open problem and weakening the form of the goal. It was a reasonable proposal, since the feasibility estimate of every angle was below 10%. I declined: "Solving all λ is something we must achieve at all costs. Please keep up the all-out attack." I had it draw a map of the difficulties, work up from simpler models, and try even the low-probability angles. In the three days from October 20 to 22, FAILED grew from F157 to F451.

What broke the wall was not a tool that extends what positivity can do, but a design that goes through a different limit. When $\Lambda$ is large, the ground state is well approximated by the Lieb–Loss functional on product states. Set up the inequality on the side of that limit functional, and return to the quantum model by handling the magnetic term (the J-G chain). This is Plan I. On October 22, Theorem 560-T gave $h\to\infty$ for all $\lambda$ with no unproved assumption.

## Self-energy and $\iota\gt0$ (October 22)

The J-G chain, as it was, fixed the leading term of the self-energy up to the constant (Corollary 563-C).

The largest remaining question was whether the family of mass renormalizations continues. The literature was split. I recast it as a dichotomy, $\iota_{\rm PF}=\inf_\lambda h/\lambda$ is positive or zero, and then reduced it further to "if $h\ge c\lambda$ above some $\lambda_1$, then $\iota\gt0$". $\lambda_1$ may be astronomical. This one line made it clear that even if something turns negative within the range computation can reach, the road to a proof stays open.

The numerics pointed to the $\iota\gt0$ side ([Chapter 3](03_numerics.md)). I gave this instruction:

> Make the all-out attack on the named condition. Prove ι>0 at all costs. Try every approach you can think of. Lift the limit on the number of subagents. Bulldoze: try every road that has even a small chance, and eliminate the dead routes. Smash it.

(The named condition is the unproved condition I had given a name.)

About 60 notes were written that day. Even so, the number of unproved conditions did not decrease. In the evening I said, "The way we name the condition is probably wrong in the first place," and had three agents with different angles write a review of the overall strategy. Putting the three side by side showed that one of the unproved conditions was the price of the tools and the other was the essential obstruction rewrapped, and the essence collapsed into one (N-BL).

The first proof failed its audit. Three "not enough room" type cancellations had occurred before, and the fourth time it had merely been moved to another term (F449). The rewritten Corollary 639-T″ passed the joint audit (an audit of related claims together), the blind rederivation, the check from the opposite side, the numerical recheck, and the full inspection of the dependency chain.

I had started writing the papers on the morning of October 22. I wrote Papers A and B and was running cycles of scoring out of 5 and improvement when $\iota\gt0$ came out, so on the 23rd I added Paper C, making three (A, B, C). The same day I also obtained a constructive version in which $c$ and $\lambda_1$ can in principle be computed (Corollary 678-T), a stronger form in which $h$ grows faster than linearly (Corollary 681-S), and a smooth-cutoff version. The constructive version is what I later threw away when shortening the papers.

## Shortening the proofs (October 23–25)

The manuscripts existed, but they were not readable. The AI referee said some parts looked like "compressed research notes written by an AI". Intermediate steps of the research were left stacked up, with terms (a) to (q) and design conditions (D1) to (D7) in a row. From here I spent three days checking whether it could be done elementarily ([Chapter 2](02_proofs_and_failures.md)).

On October 24 I decided to recast the work as two papers. The AI favored keeping three and making B a short note, but I went with coherence of subject. Paper I is the old A, and Paper II is the first half of the old B plus the old C. Paper I went from 39 to 36 pages, and Paper II from 84 pages (old B and C together) to 57 (the arXiv versions are 36 and 62 pages). The strong form had been found by a different route on the 23rd; during the audit of the recasting, it turned out that $h\ge\lambda^{8/7-\epsilon}$ also follows from the proof of Paper II, so I raised it to a main theorem.

In parallel, I rewrote the content as [research notes](https://rikai.mugen-giken.com/physics/fock-space/research-2026-10-u) on the textbook site [Rikai](https://rikai.mugen-giken.com/), and ran a review by another AI as referee. On October 25 I finished the final pre-submission checks (machine matching of the bibliography, matching the content of the citations, a final review that is not shown the past audits), read the whole text myself to confirm, and posted to arXiv. I left the submission operations to the AI, but I approved the consent, the subject class, and the send one by one. The accompanying code went into a [public repository](https://github.com/tabayashi0117/pauli-fierz-uv-limit-code) containing only the files attached to the papers; I confirmed it was public on October 27.

While matching the self-energy, I noticed that the leading coefficient disagreed with the coefficient in a theorem of [Bach–Hach (2022)](https://doi.org/10.1007/s00023-021-01124-2). Our result does not use that constant. The tracing of the discrepancy is written in Appendix A of Paper I.

## After arXiv: the gaps were still there (October 26–28)

On October 26 I received the value of the $\lambda=1024$ compute job (the local exponent of $h_{\rm eff}(1)$ from HMC at $\alpha=1$ is $1.308\pm0.030$). In light of it, I stated the strong form alongside the main theorem in the research note. As corollaries I also added the result for stopping the cutoff and taking the bare mass toward 0, and a check of transplanting to spin 1/2.

The same day, October 26, a report arrived from an AI given the role of referee (not from an outside person). The assessment was severe: major revision, then re-review. It said there were no counterexamples or unrepairable breakdowns, but it asked for justification at a number of places.

I put the question of whether the points were valid through audit too. Paper I had no gap. Paper II had a real gap, in Lemma 8.2.

Commutation on a core of unbounded operators does not imply strong commutation. The paper wrote $X_{\rm in}=1\otimes\tilde X_{\rm in}$ from commutation on a core, and the steps of domain and extension of forms were missing. The same omission was in Theorem 8.8. The claim is not false, and it could be repaired by constructing a form core for the product from the exponential law for finitely many modes and a metaplectic transformation. The main theorems are unaffected. I sent the repair through a blind check as well, which found one more missing step, and I replaced it before applying.

This gap slipped through many layers of audit and appeared in v1 on arXiv. An independent audit by Claude Fable also reported "no gaps". As I say in [Chapter 2](02_proofs_and_failures.md), this is one of the most important records for me.

For CMP I also did the following.

- Exponent budget: I stated in a Remark in the paper that there is no circularity in the order design → degree → $\kappa_p^*$ → window constants → $\lambda_1$.
- A joint audit of the revised places, and 3 independent audits of the full text.
- A re-report from the referee-role AI on the revised version. It said it had "not found a defect that breaks the main theorems", while also stating that this was not an independent verification of all the proofs.
- Full check of the citations: all 91 bibliography entries exist; of 270 citation sites, 0 need correction and 7 are minor. For a dozen or so places where the original could not be consulted, I judged by the safety of the statement.

On October 28 I submitted Paper I (38 pages) and Paper II (64 pages) to CMP.

## What remains

All of the verification described here stays within the AI's audits and my own checking. Review by outside experts is still ahead.

- Part of the J-G chain settles, within this research, a question Lieb–Loss left open, and it has not been verified in the outside literature.
- $\lambda_1$ is nonconstructive and astronomically large, and says nothing about the cutoffs that can be reached.
- The value of $\iota$, the true power of $h$, and the model with an external field are unresolved. The numerical local exponent is as above, but this is a value, not a theorem.
- For the spin-1/2 model, this chain does not carry over as it stands.

## On scope

This record is limited to what concerns Papers I and II. Investigations made along the way that do not concern them are not included. Where I touch the work of other researchers, I wrote only technical facts. On the use of AI I take the same position as the disclosure statement in the papers: I, the author, am responsible for the claims and proofs. The AI is not an author.
