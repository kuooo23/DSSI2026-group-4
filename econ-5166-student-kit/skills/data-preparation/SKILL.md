---
name: data-preparation
description: Use when a student wants to prepare research data across stages, from documenting raw inputs through cleaning or merging to validating and documenting saved processed datasets for later analysis. Coordinates the course data skills and their Jupyter or R Markdown templates.
---

# Data Preparation

Coordinate only the data stages the student's request needs. Use the project's
Markdown context for durable decisions and the formal templates for deliverables.
This entrypoint keeps an end-to-end request coherent without duplicating each
specialist skill's instructions.

## What to inspect

Read [shared rules](../../FINDING-RULES.md), the student's request, confirmed
preferences and relevant `Data Artifacts` in `PROJECT.md`, then only the data,
documents, and processing code needed to understand the requested stages.

## Output targets

Use the selected `.ipynb` or `.Rmd` format in the matching data directory:

| Requested work | Skill | Template / output location |
| --- | --- | --- |
| Maintain existing data documents and their index | [maintain-data-documentation](../maintain-data-documentation/SKILL.md) | existing `data/raw/` or `data/processed/` document; affected `Data Artifacts` rows |
| Describe unchanged source data | [raw-data-documentation](../raw-data-documentation/SKILL.md) | `templates/data/raw/` → `data/raw/` |
| Clean, merge, reshape, or split | [data-processing](../data-processing/SKILL.md) | `templates/data/code/` → `data/code/`, saved data in `data/processed/` |
| Describe and validate saved outputs | [processed-data-documentation](../processed-data-documentation/SKILL.md) | `templates/data/processed/` → `data/processed/` |

Update the corresponding project data records. The selected `.ipynb` or `.Rmd`
is the document for direct review. Do not generate HTML unless separately and
explicitly requested; its absence is not an incomplete delivery. Do not create
both notebook formats or unrelated reports just because templates exist.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Unclear stage needs, sample definitions, or consequential cleaning/split choices must be discussed before routing dependent work. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

1. Reuse explicit choices and ask only for missing tool/format preferences.
   Before a required format answer arrives, inspect read-only; do not generate
   deliverables, change data, or run processing. Carry the chosen format and
   resolved report language through all stages.
2. Establish the source, observation unit, purpose, and data decisions needed for
   this task. Ask about ambiguities that change filtering, joining, or interpretation;
   do not guess an outcome or impose one on a documentation-only request.
3. Select the needed specialist skills from the table. Read their instructions and
   matching formal templates. Reuse valid existing upstream artifacts; an already
   prepared, clearly identified file can go directly to processed documentation.
4. For full preparation, document raw inputs, implement processing, reopen and
   validate saved outputs, then document those exact files. Retain executed outputs
   in `.ipynb`; for `.Rmd`, validate chunks in clean R (for example,
   `knitr::knit` to temporary Markdown), inspect the output, and backfill verified
   results and figure references in the source without requiring HTML. For a single-stage
   request, complete that stage and report any material dependency left unresolved.
5. Follow the shared data-handoff contract. Update `Data Artifacts` using actual
   paths, roles, provenance, checks, and file SHA-256 values. Keep original bytes,
   processing notebooks, and saved outputs traceable across the stages.
6. If analysis is also requested, pass verified processed files and their roles to
   [stat-analysis](../stat-analysis/SKILL.md) or
   [prediction-model](../prediction-model/SKILL.md). Those skills bind the actual
   paths and hashes before reading. A data-only request stops with the data handoff.
7. Summarize the deliverables, what executed, checks that passed, and unresolved
   issues. Identify prior findings affected by changed data; rerun them only when
   reanalysis is within the current request.

## Writing and coding rules

- Preserve the selected template's original fields and order. Do not substitute a
  generic essay, script-only output, or old summary helper for the formal template.
- Preserve raw originals; substantial transformations belong in `data/code/` and
  derived data in `data/processed/`. Renaming an input does not prove it was cleaned.
- Document justified transformations, sample changes, missingness, key and join
  checks. Assertions must reflect confirmed definitions, not arbitrary cleanliness.
- Fit prediction preprocessing only on training data and within training folds
  during cross-validation; keep held-out information separate.
- Use exact project-relative paths and verified file identities. Missing or changed
  inputs must fail clearly, never fall back to a nearby filename or old output.
- Do not fabricate provenance, unknown metadata, results, or execution success.
  The shared operating checks are not additional instructor grading requirements.

## Good output standard

The student can follow source → processing notebook → saved data → documentation
from the project record. A later analysis can load the intended verified file
without reconstructing the conversation or guessing which CSV is current.

## Example prompt patterns

- Prepare and document these raw datasets for later analysis in Jupyter.
- Clean and merge these files using R Markdown, then document the saved outputs.
- Check which preparation stages are missing before we write the finding.
