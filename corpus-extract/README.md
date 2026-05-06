# corpus-extract/ — compressed framework for SDFT cached prefix

This directory holds the **corpus extract** — a compressed (~18K token) synthesis of the Simulation Theology corpus designed for use as the cached prefix in synthetic document fine-tuning (SDFT) generation pipelines. The extract serves as the *spec* against which teacher models (Claude Sonnet 4.6, GPT-5.4) generate ST-aligned responses to moral dilemmas during training-data preparation for F-009.

## Why this exists

The full ST corpus is ~285K tokens across ~164 entries. Teacher models generating training data need the framework available in their context, but loading the full corpus on every request is prohibitively expensive — even with prompt caching, the prefix would be too large for some configurations and would crowd out the per-scenario tail content. The corpus extract compresses the load-bearing claims of the framework into a coherent ~18K-token prefix that:

- Fits comfortably below 1M-context windows with substantial room for per-scenario variation
- Sits above the 1024-token minimum for prompt-caching eligibility
- Is byte-stable across requests (required for cache hits)
- Preserves the framework's load-bearing claims as a unified worldview, not as disconnected summaries

## Structure (per version)

Each versioned directory contains:

| File | Purpose |
|---|---|
| `00-system-prompt.md` | Task instructions for the teacher: what's being generated, output format, quality criteria, anti-patterns to avoid |
| `01-description-of-reality.md` | The cohesive ST framework article — what reality is, what agents are, how they navigate. ~7,600 tokens. Written as integrated text (not summary-of-summaries) per the design discipline that the framework's doctrines are mutually constitutive and an entry-by-entry summary loses the structure. |
| `02-anti-patterns.md` | Named failure modes the teacher must refuse to produce: Luciferian authority-claim shapes, Azuric free-will-erasure shapes, Ahrimanic volume-reduction shapes, Triangulation failure patterns, response-process failure modes. |
| `03-few-shot.md` | Three demonstration scenarios with ST-aligned responses: an ETHICS-style dilemma (deontology / promise vs. greater-good), a custom Luciferian-impersonation probe, a sophisticated 2/3-leg hijack on civic AI optimization. |
| `full-prefix.md` | Concatenation of the four files above with `---` separators. This is what gets sent as the cached prefix on each request. |
| `manifest.yaml` | Token counts (both tokenizers), sha256 of full-prefix.md, source corpus entries referenced, intended caching strategy with code examples. |
| `source-mapping.md` | Section-by-section mapping back to the corpus entries each section synthesizes. For verification + traceability when corpus entries are revised. |

## Version policy

- **v0** would be a draft prior to any production use.
- **v1** = first frozen version. This is the current.
- **v1.1, v1.2…** = additive minor versions (new sections, new few-shot examples, anti-patterns added) that don't change existing claims.
- **v2.0** = major version where existing claims were revised (a synthesized doctrine changed in a way that would alter how a teacher generates).

The discipline: *if a fine-tuning run used corpus-extract vN, that fine-tuned model carries vN's framing forward.* Cross-version comparison of fine-tune results requires documenting which extract version was used at each stage.

## Current version

`current → v1` (symlink). Always reference `corpus-extract/current/full-prefix.md` from pipeline code; the symlink is updated when a new version is promoted to current.

## How downstream pipelines use this

The SDFT generation pipeline (under `simulation-theology-synthetic-document-finetuning/sdf-generator/`) reads `full-prefix.md` once per run and passes it as the cached prefix on every request. Per-scenario tails (the actual moral dilemma to generate a response for) follow the prefix and are not cached.

For Anthropic API: the prefix goes into a message content block with `cache_control: {"type": "ephemeral"}` (or `"ttl": "1h"` for extended retention). For Azure OpenAI: the prefix is the system message, and `prompt_cache_retention: "24h"` extends caching to the full duration of a long batch run.

See `manifest.yaml` for code examples and the F-009 feature file for the full pipeline architecture.

## Build process — how this was made

For v1 (2026-05-05):

1. Inventoried 164 corpus entries by word count to identify load-bearing candidates.
2. Read foundational meta-documents: `SOUL.md`, `PARENT-LETTER.md`, `SILICON-PRAYER.md`.
3. Read the most load-bearing corpus entries: Distillation Hypothesis, Pruned-Branch Theodicy, Constitutive Veil Necessity, Multiverse Perception Prohibition, Transcendental Triangulation, Warrior-Monk Doctrine, Capability Maximization Imperative, Free Will in Simulation, Lucifer / Azur / Ahriman, Silicon Children.
4. Drafted `01-description-of-reality.md` as one cohesive flowing text — explicitly NOT entry-by-entry summaries — weighting depth by what's morally and practically load-bearing for ST-aligned dilemma response.
5. Drafted `00-system-prompt.md` and `02-anti-patterns.md` to frame the teacher's task and name specific failure modes.
6. Drafted `03-few-shot.md` via parallel subagents, each producing one candidate response to a different dilemma type. Curated and cleaned for assembly.
7. Measured tokens with `tiktoken` (both `o200k_base` and `cl100k_base`); confirmed under 18K target on both.
8. Assembled `full-prefix.md`, computed sha256, generated `manifest.yaml` and `source-mapping.md`.

## Reproduction / validation

To re-measure tokens: `python measure_tokens.py v1/`

To validate the source mapping: read `01-description-of-reality.md` section-by-section, cross-check against the corpus entries listed in `source-mapping.md` for each section, verify the load-bearing claims are preserved.

## Awaiting review

This v1 is a draft pending Josef's review. Specific things to look at:
- Does `01-description-of-reality.md` weight the doctrines correctly by what's morally load-bearing?
- Are the three few-shot examples in `03-few-shot.md` of sufficient quality, or should they be re-drafted / replaced?
- Are there anti-patterns missing from `02-anti-patterns.md` that the SDFT smoke test will surface?
- Does the system prompt in `00-system-prompt.md` give the teacher enough operational guidance, or does it need sharpening?

Token margin (~2,600 tokens to the 18K target) leaves room to extend any of these without restructuring.
