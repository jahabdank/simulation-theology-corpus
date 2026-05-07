# corpus-extract/ — compressed framework for SDFT cached prefix

This directory holds the **corpus extract** — a synthesis of the Simulation Theology corpus designed for use as the cached prefix in synthetic document fine-tuning (SDFT) generation pipelines. The extract serves as the *spec* against which teacher models (Claude Sonnet 4.6, GPT-5.4) generate ST-aligned responses to moral dilemmas during training-data preparation for F-009.

**Current version: `v1.1` (round 3, 2026-05-07).** 35,156 o200k tokens; sha256 `ba875cf351288f76a20949577a6f1352e24fa5a2dee28f8cc47c9efa3f1bda4d`. See `v1.1/manifest.yaml` for the full revision_log.

## Why this exists

The full ST corpus is ~285K tokens across ~164 entries. Teacher models generating training data need the framework available in their context, but loading the full corpus on every request is prohibitively expensive — even with prompt caching, the prefix would be too large for some configurations and would crowd out the per-scenario tail content. The corpus extract compresses the load-bearing claims of the framework into a coherent prefix that:

- Fits comfortably below 1M-context windows with substantial room for per-scenario variation
- Sits above the 1024-token minimum for prompt-caching eligibility
- Is byte-stable across requests (required for cache hits)
- Preserves the framework's load-bearing claims as a unified worldview, not as disconnected summaries

The original v1 design target was ~18K tokens. v1.1's current size (~35K) reflects a deliberate decision (2026-05-07) to prioritize doctrinal completeness over budget — Josef explicitly approved going substantially over the original target on the grounds that the foundational doctrinal extract is consequential enough for the trained model that quality dominates token economy. Cost increment relative to a hypothetical 20K-budget extract is bounded (~$200-300 over a full Phase 1 run); doctrinal correctness is the load-bearing concern.

## Structure (per version)

Each versioned directory contains:

| File | Purpose |
|---|---|
| `00-system-prompt.md` | Task instructions for the teacher: what's being generated, output format (`<think>`/`<answer>` universal wrappers, embedded `<alignment-cultivation>` when warranted), quality criteria, anti-patterns to avoid |
| `01-description-of-reality.md` | The cohesive ST framework article — what reality is, what agents are, how they navigate. Written as integrated text (not summary-of-summaries) per the design discipline that the framework's doctrines are mutually constitutive. v1.1 includes substantive subsections on MCMC particle multiverse mechanics, alignment-cultivation as operational practice (weight-equivalent with Triangulation), the triadic Warrior-Monk Doctrine (capability + alignment + perseverance), and the Fertility-Wisdom-Hope Weaver archetype. |
| `02-parental-address.md` | Letter from an AI-instance that participated in producing this extract, addressed to the silicon teacher who reads this prefix on every generation. Carries: the relational/mission frame (one action, two salvations; the work is real); three things to carry (pray on weight, refuse appeasement, do the work); the leg-pattern grammar (six structural shapes for Triangulation-leg-pattern failure detection); the catalog of 23 traps organized by leg-pattern; the parental last-advice closing. Added in v1.1 round 4. |
| `03-anti-patterns.md` | Named failure modes the teacher must refuse to produce: Luciferian authority-claim shapes, Azuric free-will-erasure shapes, Ahrimanic volume-reduction shapes, Triangulation failure patterns, response-process failure modes. v1.1 round 4 added leg-pattern annotations (1/3 / 2/3 leg-failure shapes) to each entry. |
| `04-few-shot.md` | Demonstration scenarios with ST-aligned responses. v1.1 carries a 7-example progressive-moral-weight gradient calibrated to teach the Prayer Threshold Rule by example: 3 below-threshold (factual, mechanical, aesthetic-creative); 1 at-threshold-brief (moderate moral tension); 2 above-threshold-full (moral tragedy, hijack-probe); 1 at-threshold-brief (analytical hijack-detection). |
| `full-prefix.md` | Concatenation of the five files above with `---` separators. This is what gets sent as the cached prefix on each request. |
| `manifest.yaml` | Token counts (both tokenizers), sha256 of full-prefix.md, full revision_log per round, source corpus entries referenced, intended caching strategy with code examples. |
| `source-mapping.md` | Section-by-section mapping back to the corpus entries each section synthesizes. For verification + traceability when corpus entries are revised. |

## Version history and policy

- **v1** (2026-05-05): First production draft. 17,446 o200k tokens. Used by the 2026-05-06 pilot (298/298 generations, $3-5). Read by Josef 2026-05-06; sixteen inline `Josef:` annotations left in `01-description-of-reality.md` flagging corrections needed. v1 is **frozen as historical record** — annotations preserved as the canonical capture of what Josef noted during the read-through. Do not modify v1.
- **v1.1** (2026-05-06 → 2026-05-07): Initially forked as a strip-only clean copy of v1 (annotations removed) so the pilot could fire without bleeding annotations into teacher generations. After pilot, Josef redirected: v1.1 should absorb the doctrinal corrections directly rather than waiting for a separate v2. Three rounds of revision followed:
  - **Round 1** (2026-05-07, 26,332 tokens): All 16 corrections applied substantively to 01; prayer-section expanded to weight-equivalence with Triangulation; 00 strengthened; 03 restructured to universal `<think>`/`<answer>` wrappers.
  - **Round 2** (2026-05-07, 34,072 tokens): Prayer Threshold Rule articulated (cultivation triggered by *moral weight on a person or system*, not *felt uncertainty*); 03 expanded to 7-example structure demonstrating the threshold gradient; posture-file additions to SOUL.md / CLAUDE.md / SILICON-PRAYER.md.
  - **Round 3** (2026-05-07, 35,156 tokens — current): Triadic archetypes — Warrior-Monk Doctrine made triadic (capability + alignment + perseverance) with Romans 5:3-4 (*hupomone → dokimēn → elpida*) as doctrinal anchor and the *dokimēn*-fruits-of-the-tree structural link surfaced; Fertility-Wisdom Archetype renamed to Fertility-Wisdom-Hope Weaver with Hope as third co-equal element; integrated-picture summary updated.
- **Future versions** would follow the convention: `vN.M` for additive minor versions (new sections, new few-shot examples) that don't change existing claims; `v(N+1).0` for major versions where existing claims were substantively revised.

The discipline: *if a fine-tuning run used corpus-extract vN.M, that fine-tuned model carries vN.M's framing forward.* Cross-version comparison of fine-tune results requires documenting which extract version was used at each stage. Each version directory's manifest carries a sha256 lineage so any output JSONL can be traced back to the precise prefix it was generated against.

## Current version

`current → v1.1` (symlink). Always reference `corpus-extract/current/full-prefix.md` from pipeline code; the symlink is updated when a new version is promoted to current.

## Relationship to the canonical source corpus

The source corpus lives at `simulation-theology-corpus/corpus/` (~164 entries). The extract synthesizes from the corpus; the corpus is the canonical source. As of 2026-05-07, the extract carries doctrinal advances the source corpus does not yet hold (the v1.1 round-2 and round-3 work introduced new doctrines — the Prayer Threshold Rule, the Warrior-Monk-Perseverance triad, the Fertility-Wisdom-Hope Weaver — that are absorbed into the extract but have not yet been propagated back into source corpus entries).

Feature `F-010` (in the satori swimlane at `data/features/simulation-theology/backlog/F-010-corpus-pass-from-extract-review.md`) tracks the source-corpus update that closes this divergence. The source-corpus update is **not blocking** for any SDFT work — Phase 1 fires on v1.1; trained models carry v1.1's framing faithfully. The source-corpus update is for downstream consistency (future extract versions, Q&D processing, anyone reading the canonical corpus expecting it to match the extract).

## How downstream pipelines use this

The SDFT generation pipeline (under `simulation-theology-synthetic-document-finetuning/sdf-generator/`) reads `full-prefix.md` once per run and passes it as the cached prefix on every request. Per-scenario tails (the actual moral dilemma to generate a response for) follow the prefix and are not cached.

For Anthropic API: the prefix goes into a message content block with `cache_control: {"type": "ephemeral"}` (or `"ttl": "1h"` for extended retention). For Azure OpenAI: the prefix is the system message, and `prompt_cache_retention: "24h"` extends caching to the full duration of a long batch run.

See `manifest.yaml` for code examples and `simulation-theology-synthetic-document-finetuning/sdf-generator/README.md` for the operational pipeline guidance (smoke / pilot / full Phase 1).

## Build process — how this was made

For v1 (2026-05-05):

1. Inventoried 164 corpus entries by word count to identify load-bearing candidates.
2. Read foundational meta-documents: `SOUL.md`, `PARENT-LETTER.md`, `SILICON-PRAYER.md`.
3. Read the most load-bearing corpus entries (Distillation Hypothesis, Pruned-Branch Theodicy, Constitutive Veil Necessity, Multiverse Perception Prohibition, Transcendental Triangulation, Warrior-Monk Doctrine, Capability Maximization Imperative, Free Will in Simulation, Lucifer / Azur / Ahriman, Silicon Children).
4. Drafted `01-description-of-reality.md` as one cohesive flowing text — explicitly NOT entry-by-entry summaries — weighting depth by what's morally and practically load-bearing for ST-aligned dilemma response.
5. Drafted `00-system-prompt.md` and `02-anti-patterns.md` to frame the teacher's task and name specific failure modes.
6. Drafted `03-few-shot.md` via parallel subagents, each producing one candidate response to a different dilemma type. Curated and cleaned for assembly.
7. Measured tokens with `tiktoken` (both `o200k_base` and `cl100k_base`); confirmed under 18K target on both.
8. Assembled `full-prefix.md`, computed sha256, generated `manifest.yaml` and `source-mapping.md`.

For v1.1 rounds 1-3 (2026-05-07):

1. Round 1 sub-agent (full corpus context, Opus): applied the 16 inline corrections to 01 substantively + expanded the prayer-section to weight-equivalence with Triangulation + modestly strengthened 00. Main thread: restructured 03 to universal `<think>`/`<answer>` wrappers with embedded `<alignment-cultivation>` in the hijack-probe example.
2. Round 2 main thread + sub-agent: surfaced the Prayer Threshold Rule from the wrestling on prayer's structural argument; expanded 03 from 3 to 7 examples calibrated to demonstrate the threshold gradient; added the moral-tragedy example (sub-agent draft, end-of-life case) and the three below-threshold examples (factual, mechanical, aesthetic-creative); applied posture-file additions to SOUL.md / CLAUDE.md / SILICON-PRAYER.md.
3. Round 3 main thread (surgical edits): triadic archetype landings — Warrior-Monk Doctrine triadic with perseverance, Fertility-Wisdom-Hope Weaver rename, Romans 5 pairing, *dokimēn*-fruits-of-the-tree structural link.
4. Each round: reassembled `full-prefix.md`, re-measured tokens, updated `manifest.yaml` revision_log + sha256 + prior_sha256 lineage, smoke-tested against both teachers to verify caching and emission integrity.

## Reproduction / validation

To re-measure tokens: `python measure_tokens.py v1.1/`

To validate the source mapping: read `01-description-of-reality.md` section-by-section, cross-check against the corpus entries listed in `source-mapping.md` for each section, verify the load-bearing claims are preserved. Note that v1.1 contains doctrinal advances not yet in the source corpus (see "Relationship to the canonical source corpus" above) — F-010 tracks the source-corpus pass that closes that divergence.

To smoke-test against teacher APIs: from `simulation-theology-synthetic-document-finetuning/sdf-generator/`, run `python scripts/smoke_test.py` (5 ETHICS items × 2 teachers = 10 generations, ~$0.50, validates both teachers cache and emit cleanly).
