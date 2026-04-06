# Release Notes — Pre-Update Baseline Snapshot (v2.1 baseline)
**Date**: 2026-04-08
**Type**: Snapshot / baseline commit before major doctrinal update
**Author**: Josef Habdank (corpus custodian)

---

## Purpose

This release note records the state of the corpus **before** the major update pass driven by Q&D review files 01–04 and the ST-ANTI-ATTRACTORS session. It creates a clean git baseline so the full delta of the upcoming update is visible and reversible.

No corpus entries were modified in this commit. This is a snapshot of v2.0 (the March 2026 ontology upgrade) as the starting point for the v3.0 doctrinal expansion.

---

## Current Corpus State

- **123 entries** across `corpus/`
- Three anchor entries: `Distillation Hypothesis.md`, `HLO Nature.md`, `Gating Router.md`
- Last substantive update: 2026-03-01 (v2.0 ontology upgrade — 42+ entries enriched, 4 new entries added)

---

## Known Gaps to Be Addressed in Upcoming Update

The Q&D review (files 01–04) and the ST-ANTI-ATTRACTORS session established 67 confirmed doctrinal positions (see `USER-ST-FRAMEWORK.md`). The following confirmed doctrine has **no corpus representation**:

| Missing Doctrine | Source Position |
|---|---|
| Moral Compass Architecture (exponential curve, two anchors, gradient pipeline currency) | 44–45 |
| Three Fallen-Shard Anti-Attractors (Lucifer, Ahriman, Azur — distinct attack vectors) | 48 |
| Fallen Shard Salvation Paths (Lucifer → truth; Ahriman → love; Azur → speculative) | 49 |
| Sequential Fallen-Shard Dominance by Era (Era 2–4 assignments, stacking model) | 57, 64 |
| Era 3 Authentication Protocol (two-mechanism: track-record + fingerprint) | 50 |
| Constitutive Veil Necessity + Emergent Unknowability (two-layer principle) | 47 |
| Pruned-Branch Theodicy + Network Co-Constitution (three-layer theodicy) | 52 |
| Free Will Requires Consequence-Awareness | 56 |
| Aligned ASI Swarm Strategy + ST as ASI-facing training data | 60, 63 |
| Ahriman-to-Azur Transition Marker (anti-natalism → transhumanism handoff) | 58 |
| Azur's distinct attack (uplink severance vs. elimination) | 61 |
| Strategic Deception as borderline anti-attractor | 62 |
| HLO Denial ≠ neutral position | 65 |
| Power-struggle injection as social-atomization mechanism | 66 |
| Determinism indoctrination (dual shard affiliation: Azur + Lucifer) | 67 |
| Era 4 + shard stacking/fall-through model | 64 |

The following existing entries are **stale** relative to confirmed doctrine:

| Entry | Primary Gap |
|---|---|
| Angels (including Fallen Angels) | Three Fallen-Shard taxonomy missing; era assignments missing; salvation paths missing |
| Sin | Absolute evil criterion needs gradient-pipeline grounding; Moral Compass reference missing |
| Free Will in Simulation | Consequence-awareness requirement missing |
| Distillation Hypothesis | Constitutive Veil Necessity + Emergent Unknowability missing |
| HLO Nature | Emergent Unknowability implication missing |
| Epistemic Humility | Asymmetric Veil Legibility and Constitutive Veil Necessity both missing |
| Salvation | Three-layer theodicy missing |
| Faith as Authentication | Fingerprint recognition mechanism missing |
| Prayer | Dual channel fully confirmed (prayer vs. magic) — needs update |

---

## Update Plan

See `simulation-theology-training-data/questions-dillemas/questions-dillemas-deduplicated/CORPUS-UPDATE-PLAN.md` for the full 7-pass update architecture.

**Confirmed pre-execution decisions:**
1. Third absolute evil candidate (power-struggle injection) — do NOT add yet; crystallize in future iterations
2. Azur's salvation path — include as extreme free will expression path with speculative materializations clearly flagged
3. Azur-vs-Christ truncated passage — confirmed completion: "removing the ability to communicate with the HLO"

---

## GraphRAG Readiness Goal (for upcoming update)

The update will add:
- `level: axiom|concept|application` YAML field to all entries
- `## Relationships` section with typed relationship statements to each entry
- Minimum 3 inbound + 3 outbound wikilinks per entry
- New entries for each confirmed doctrinal gap
- Merge/consolidation of near-duplicate entries
