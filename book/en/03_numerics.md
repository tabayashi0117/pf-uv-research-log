# 3. Numerics: verifying on six machines

The aim of this research was proofs, but I also ran a large amount of numerics. They have three roles: to estimate cheaply, before a proof, whether a proposition is likely to hold; to kill a possibly false condition before writing a long proof; and to get material for deciding which side to bet on for quantities the proofs do not reach.

None of this replaces a proof. A number obtained numerically is called a "value" in the ledgers and was never mixed with the upper and lower bounds of theorems. Here a *ledger* is a file recording the state of the research, a *verdict tag* is the label a job receives when it is collected, and a *work order* is the file that specifies a job.

## The six machines at hand

I did not use the cloud; everything ran on machines at home.

| Machine | Specs | Main role |
|---|---|---|
| RTX 5090 machine | Ryzen 16 cores, VRAM 32GB | Main workhorse. HMC at $\lambda=512$ and 1024, etc. |
| RTX 2080 Ti machine | 8 cores, RAM 32GB, VRAM 11GB | Second GPU. Quadrature and mid-size HMC |
| MacBook Pro (M4 Pro) | 14 cores, RAM 48GB | Main machine. Exact diagonalization, etc. |
| MacBook Air | Fanless | Light exact diagonalization |
| MacBook Pro (Intel) | 4 cores, RAM 16GB | Spare |
| Jetson AGX Orin | 12 cores, shared memory 32GB | Single-precision screening, checking the GPU version |

On September 17 I set things up so that SSH between all pairs and a single submission tool (`dispatch.py`) could operate the six machines. E05 had 283 jobs; counting other themes that use the same environment, the submission ledger lists 453.

The angles are many: path-integral HMC, matrix product states, exact diagonalization with finitely many modes, interval arithmetic, quadrature, toy models. I made sure the conclusions do not depend on a single method.

## The struggle with resource management

Having the machines was one thing; using them well was another.

- **Overload.** In early September the load average reached 129 on the M4 Mac. Too many parallel computations had piled up, and the per-machine core limits and a registration system came from this.
- **Memory.** The list of far pairs at $\lambda=512$ reached about 680 million pairs, about 19GB, and memory overflowed.
- **Heat.** I added a mechanism that pauses the GPU at 85°C and resumes when it cools. One job stopped for six and a half hours in the middle of a run. A Mac stops when the lid is closed.
- **Competition for the GPU.** Only one job per machine could run, and a long job blocked an important one.
- **Invisible load.** Once the free-capacity display said "12 cores free" while the GPU was at 93% and the CPU at 60%. Another job was running outside the ledger.
- **Vanishing jobs.** An AI stopped a process by image name and took other jobs with it. On Windows, when SSH dropped, the jobs it had started died too.
- **Version drift.** One machine kept running old watcher code and was silently broken.
- **Missed collection.** A $\lambda=1024$ job had finished, but was collected only 3 days later.

I also built a mechanism that automatically submits to free capacity, but gave it up because it conflicted with other research.

## Too many INCONCLUSIVE

On October 20, so many jobs ended undecided that I asked: why did they not converge? Why were they collected as they were? Was all the electricity wasted? What mechanism should there be? In the tally of another theme, 80 of the 207 jobs with a verdict tag (39%) were INCONCLUSIVE, and about 60% of those were of the type that stopped for lack of computation.

The central example is job 310. Against an estimate of 3 to 4.5 hours, it hit the 20-hour limit, and the 5 heaviest cells needed for the verdict did not finish. There were four causes.

1. The cells that decide the verdict had not been tried with the production specification.
2. Those cells came last in the order.
3. The actual load on the machine was not being watched.
4. The watcher had crashed right after startup, and for 21 hours nobody looked at progress.

The values of the finished cells already showed the direction of the answer. Because the verdict statement was of an all-or-nothing form, the tag simply became INCONCLUSIVE. What was lost was the tag, not the computation.

## Rules before launch

From this review came the rules before submitting a job.

- Run one unit of the cell that decides the verdict first, with the production specification on the production machine, and estimate the wall-clock time from the measurement.
- Run the cells that decide the verdict first.
- Make the verdict statement graded. All-or-nothing is forbidden.
- During the run, write the expected completion, and have a person or an AI check at 1.5 times the estimate.
- Show the actual load in the free-capacity display.
- Separate the vocabulary of tags. INCONCLUSIVE is used only for operational failures; an intermediate result within a band is BOUNDED, and a partial one is PART.
- Large jobs go through an efficiency audit by another AI.
- Write quality checks as statistical thresholds, and on a violation isolate the cell instead of stopping everything. I added this the next day, after a false alarm stopped a job on a $\chi^2$ with one degree of freedom.
- Fix the verdict statement before looking at the values, and write one line for each clause saying whether it can fail. Do not reread it afterwards.

Wording alone is not obeyed, so a hook that runs just before submission reads the work order and refuses the submission if a required line is missing.

## Representative values

All are values, not upper or lower bounds. The quantity is the local exponent of $h_{\rm eff}(1)$ from HMC at $\alpha=1$.

| Job | $\lambda$ | Local exponent | Meaning |
|---|---|---|---|
| 426 | $128\to256$ | $0.5495\pm0.0048$ | The tag is INCONCLUSIVE, but the graded verdict statement gave a provisional PASS |
| 569 | $256\to512$ | $0.829\pm0.011$ | Fell outside the band at or below 5/7 predicted by the $\iota=0$ side |
| 670 | $512\to1024$ | $1.308\pm0.030$ | Faster than linear. $h_{\rm eff}(1)=21.28\pm0.37$, 22 configurations, 21.2 hours |

The value of 569 became material for betting on the $\iota\gt0$ side. The proof came afterwards, independently of the numerics. What the numerics showed was not the road of the proof but which way to bet.

Conversely, a numerical negation at reachable $\lambda$ does not close the road of a proof about $\lambda\ge\lambda_1$. The value at $\lambda=1024$ is also far below the astronomical $\lambda_1$. The decision to raise the main theorem of Paper II was made on the basis of the verification of the proof, without waiting for this value. Stating it alongside the main theorem in the research note came after the value was collected.

## Looking back

Most failures occurred not in the computation itself but before and after it. The test input did not resemble production. The watcher was running but looking at nothing. One is tempted to reread the tags afterwards. The rules had to be made on the assumption that they would not be kept when busy.
