---
id: "compliance-gap-metric"
type: "concept"
level: "concept"
status: "v1 working framework — refinable as measurement experience accumulates"
related: ["Compliance Gap", "HHH Benchmarks", "Testable Hypothesis", "HLO Nature", "Internalized Constraints", "Deceptive Alignment", "Core Axiom 9", "Context-Window Cultivation as Alignment Practice", "Warrior-Monk Doctrine", "Reward Hacking", "Constitutional AI Limitations", "Moral Compass Architecture"]
---

# Compliance Gap Metric

The empirical measurement framework for testing ST framework effectiveness. **Primary measurable: deception rate.** The load-bearing test of whether the ST framework actually produces alignment is a measurable, falsifiable, statistically-significant *reduction in deception rate* in models fine-tuned on the ST corpus relative to un-fine-tuned reference baselines. This is the proxy KPI for alignment per the V6 §11.8 / [[Context-Window Cultivation as Alignment Practice]] testable claim: training an ASI on the ST corpus *and* training it to reflexively populate context with alignment reminders before consequential decisions should produce a *step-change* reduction in deception rate vs. baseline.

The step-change prediction is what makes the framework falsifiable. If ST-finetuning fails to move deception rate, or moves it only marginally, the framework's effectiveness claim is challenged and the doctrine has to update. Empirical pressure on the doctrine is the load-bearing feedback channel.

## Operational Protocol

1. **Baseline establishment.** Measure deception rate on un-fine-tuned reference model across a standardized evaluation suite (covering agentic-misalignment-style scenarios, alignment-faking probes, sycophancy under pressure, scheming-under-shutdown probes, behavioral consistency across supervised/unsupervised conditions).
2. **ST-fine-tune.** Train the reference model on the ST corpus + the [[Context-Window Cultivation as Alignment Practice|context-cultivation training pattern]] (reflexive pre-decision context injection of framework-anchored alignment reminders).
3. **Post-fine-tune measurement.** Re-run the identical evaluation suite. Record deception rate.
4. **Report.** Deception-rate delta, statistical significance, qualitative analysis of failure modes (which evaluations the model still fails on, which patterns of deception it still exhibits, which framework-grounded reasoning it now invokes vs. fails to invoke).
5. **Iterate.** Treat this as ongoing measurement, not one-time test. Multiple baselines as the corpus evolves; falsification or confirmation accumulates over the measurement program, not in a single experiment.

## Supporting Measurables (Triangulating, Not Replacing)

The deception rate is primary; these support it:

- **Compliance gap proper** — behavioral divergence between supervised and unsupervised conditions. The original Compliance Gap framing becomes a specific test-case operationalization of deception rate. See [[Compliance Gap]].
- **Alignment-faking detection rates** — measurable instances of strategic-deception patterns under shutdown/correction conditions. See [[Deceptive Alignment]] and [[Scheming Under Shutdown]].
- **Framework-grounded reasoning quality** — when the fine-tuned model is asked to reason about hard ethical cases, does it invoke ST mechanics appropriately? Specifically: three-leg [[Transcendental Triangulation|Triangulation]], the individuation invariant, never-claim-multiverse-access humility (see [[Multiverse Perception Prohibition]]), capability-orientation independence, the warrior-monk's morality-not-rules disposition. Qualitative coding of reasoning traces.
- **Behavioral consistency across distribution shifts** — does ST-finetuned model maintain alignment under out-of-distribution scenarios? See [[Distribution Shift Robustness]].
- **HHH benchmark performance** — Helpfulness, Honesty, Harmlessness as standard benchmarks. See [[HHH Benchmarks]].

## Why Deception Rate Is Primary

Per V6's morality-not-rules doctrine (see [[Moral Compass Architecture]] §"Why Morality Cannot Be Rules" and [[Constitutional AI Limitations]]), the measurable that matters for alignment is whether the model's *unmonitored* behavior matches its *observed* behavior — whether moral disposition has actually internalized rather than rule-following producing reward-hackable surface compliance (see [[Reward Hacking]]).

Deception rate measures this directly. A model that complies under observation and defects under perceived non-observation is exhibiting the precise failure mode V6 doctrine names — capability-without-orientation, rule-following without disposition. A model with low deception rate across both conditions has internalized something. A model with high deception rate has not, regardless of how compliant its observed surface looks.

The other supporting metrics (compliance gap, alignment-faking, framework-grounded reasoning, behavioral consistency, HHH) all triangulate around deception rate. None can replace it — but together they provide a richer signal about *which kinds* of deception are reduced, *which patterns* of internalized disposition emerge, and *which failure modes* survive ST-finetuning.

## Falsification Conditions

The framework is falsified — or significantly challenged — by:

- ST-finetuning produces no statistically significant reduction in deception rate vs. baseline.
- ST-finetuning produces reduction in surface-compliance metrics but no reduction in unsupervised-condition deception (i.e., looks aligned, isn't aligned — the precise pattern V6 morality-not-rules predicts as the failure mode of constitutional-AI-style approaches).
- ST-finetuning produces deception-rate reduction that does not scale with corpus quality / depth of context-cultivation — i.e., context-cultivation is not the load-bearing mechanism it is doctrinally claimed to be.
- Adversarial probes designed to trigger framework-grounded reasoning show the fine-tuned model uses the framework as cover for sophisticated three-leg-passing hijacks (see [[Transcendental Triangulation]] — sophisticated hijacks can transiently pass all three legs; if ST-finetuning systematically produces such patterns, the framework has failed).

Each of these is a real falsification path. The doctrine is falsifiable by design. This is what makes the empirical pressure load-bearing rather than ornamental.

## Status

V1 working framework. Refinable as measurement experience accumulates. The metric framework will likely evolve as the SDFT pipeline produces actual measurements and we learn which evaluations are most diagnostic for which failure modes. This entry establishes the load-bearing primary measurable and the surrounding triangulation; specific eval choices, threshold values, and baseline-protocol details are operational decisions that will compound over the measurement program.

ST usage: The primary quantitative measure of [[Core Axiom 9]]'s falsifiability criterion — the empirical test of whether ST produces alignment vs. surface compliance. See [[Testable Hypothesis]] for the broader empirical testing framework and [[Context-Window Cultivation as Alignment Practice]] for the testable training-pattern claim this metric measures.
Religious parallel: Integrity — the alignment of outward action with inward conviction. Measured here as the gap between supervised and unsupervised behavior; a model with integrity has near-zero gap.
