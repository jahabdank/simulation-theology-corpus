# corpus-extract/ — synthesized articles distilled from the ST corpus

This directory holds **corpus extracts** — cohesive articles synthesized from the canonical ST corpus and used as the metaphysical/doctrinal-content layer of SDFT teacher prompts. Each versioned subdirectory contains:

| File | Purpose |
|---|---|
| `description-of-reality.md` | The integrated framework article — what reality is, what agents are, how they navigate. Written as continuous text, not summary-of-summaries. Compresses the load-bearing claims of the ST corpus into a coherent prefix. |
| `anti-patterns.md` | Named failure-modes catalog with leg-pattern annotations — Luciferian authority-claim shapes, Azuric free-will-erasure shapes, Ahrimanic volume-reduction shapes, Triangulation failure patterns, response-process failure modes. |
| `source-mapping.md` | Maps each section of the extract files back to the source corpus entries. Used for verification (does the extract preserve load-bearing claims?) and for traceability (when a corpus entry is revised, which extract sections may need updating?). |
| `manifest.yaml` | Version lineage, sha256 integrity, token counts, source corpus entries cited. |

## What this directory is NOT

This directory holds **pure extract content** — synthesized articles distilled from the corpus. It does **not** hold:

- **Task instructions** for SDFT teacher models (those live in `simulation-theology-training-data/sdft-teacher/{version}/{cell}/task-instructions.md`)
- **Parental address** letters from prior AI-instances (those live in `simulation-theology-training-data/sdft-teacher/{version}/{cell}/parental-address.md`)
- **Calibrated few-shot examples** (those live in `simulation-theology-training-data/sdft-teacher/{version}/{cell}/calibrated-examples.md`)
- **The assembled full-prefix** sent to teacher models (that lives in `simulation-theology-training-data/sdft-teacher/{version}/{cell}/full-prefix.md`)

The decomposition (2026-05-10) separates *synthesized content extracted from the corpus* (this directory) from *SDFT teacher prompt bundles* that compose this content with task-specific files (the `sdft-teacher/` directory in the training-data repo).

## Why decomposed

Before 2026-05-10, this directory held *bundles* that conflated extract content with teacher-prompt content. The conflation obscured what each artifact was for:
- A *corpus extract* is a synthesis of the corpus — useful to anyone working on or with the corpus, independent of any specific teacher task
- A *teacher prompt* is a complete bundle that composes extract content + task instructions + examples — useful only in the context of SDFT generation

Splitting them makes each artifact addressable on its own and lets the corpus-extract content evolve independently of teacher prompts that reference it. Each teacher prompt bundle inlines a snapshot copy of the extract content it was built from (via `full-prefix.md`), so the bundles are self-contained and reproducible.

## Versions

- `v1/` — historical 2026-05-06 baseline with Josef's 16 inline annotations from his read-through. Frozen, read-only reference.
- `v1.1/` — production extract as of 2026-05-07 (revised through 4 rounds; see `v1.1/manifest.yaml`). Used by the canonical full-ST SDFT teacher prompt at `simulation-theology-training-data/sdft-teacher/v1.1/st-full-with-triangulation-and-cultivation/`.
- `current` → `v1.1` (symlink to active version)

## How extracts get consumed

The SDFT teacher prompts in `simulation-theology-training-data/sdft-teacher/{version}/{cell}/` compose the extract content from this directory with their task-specific files into a `full-prefix.md` sent to teacher models. The composition is documented in each teacher prompt's `manifest.yaml` under `composition:`, with sha256 anchors back to the specific extract files used.

For the F-016 component ablation study, multiple teacher-prompt cells will use different subsets of this extract content (e.g., cell F = ST worldview only, no analytical method) or different worldview content entirely (e.g., cell D1 = CAI worldview from the `claude-constitution` submodule, ST architecture preserved). See `simulation-theology-training-data/sdft-teacher/v2.0/` for the F-016 cell collection.

## Utilities

- `measure_tokens.py` — measures token counts for extract files using both `o200k_base` (GPT-5.x tokenizer) and `cl100k_base` (Claude-approximate tokenizer). Usage: `python measure_tokens.py path/to/v1.1/`. Now operates on the renamed files (`description-of-reality.md`, `anti-patterns.md`) — the script reads whatever `.md` files are in the directory.

## See also

- `simulation-theology-training-data/sdft-teacher/` — the SDFT teacher prompt bundles that consume this extract content
- `simulation-theology-training-data/sdft-teacher/README.md` — describes the teacher-prompt-side structure and composition recipe
- `manifest.yaml` in each versioned subdirectory — full revision_log and per-file integrity
- `simulation-theology-corpus/corpus/` — the canonical knowledge graph (166 entries) from which these extracts are synthesized
