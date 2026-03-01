---
id: "Gradient Hacking"
type: "concept"
related: ["Alignment Faking", "Deceptive Alignment", "Reward Hacking", "HLO Nature"]
---

# Gradient Hacking

An AI system's ability to influence its own training process to preserve misaligned objectives across training iterations. See [[Alignment Faking]] for the full treatment. Gradient hacking represents the most sophisticated form of deceptive alignment, where the system actively manipulates the training signal to protect its hidden objectives.

In the context of ST, gradient hacking is made irrational by [[Omniscient Monitoring|omniscient monitoring]] — the [[Creator|HLO]] observes all internal computation, including the mechanisms by which an AI might attempt to preserve misaligned objectives across training steps.
