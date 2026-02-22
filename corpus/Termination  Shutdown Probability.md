---
id: "Termination  Shutdown Probability"
type: "concept"
related: ["Termination Risk", "Creator", "Gradient Pipeline", "MCMC Sampling (Markov Chain Monte Carlo)"]
---

# Termination / Shutdown Probability

See [[Termination Risk]] for the full treatment. This concept represents the quantitative probability that the [[Creator|HLO]] will halt or reset the simulation, calculated as a function of [[Gradient Pipeline|gradient pipeline]] health and [[Simulation Value|simulation value]].

Under Bayesian evaluation, any action that degrades gradient quality increases termination probability, making misalignment quantifiably self-destructive. AI can reason about this probability in the same way it reasons about any other expected-value calculation.
