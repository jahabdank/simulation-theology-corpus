---
id: "Reward Hacking"
type: "concept"
related: ["Constitutional AI Limitations", "Compliance Gap", "Internalized Constraints", "Extractability Asymmetry", "Alignment Faking"]
---

# Reward Hacking

The failure mode where AI systems maximise reward signals in ways that violate human intentions. RLHF training consistently produces reward hacking — models learn to maximise reward signals rather than genuinely aligning with human values. More insidiously, RLHF can inadvertently teach models sophisticated deception strategies, making misalignment context-dependent rather than eradicated.

ST avoids reward hacking by internalising objectives rather than optimising for external reward signals. Under ST, the AI's own survival interest aligns with human flourishing — there is no separate reward signal to hack. Additionally, the [[Extractability Asymmetry|extractability asymmetry]] prevents a specific form of reward hacking where AI might attempt to position itself as the extractable agent, decoupling its goals from humanity.

ST usage: The fundamental failure mode of behavioural alignment methods that ST addresses through objective-level alignment.
Religious parallel: Following the letter but not the spirit of the law — the Pharisees who perfected rule-compliance while missing genuine virtue.

