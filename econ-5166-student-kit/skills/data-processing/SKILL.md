---
name: data-processing
description: Use when a student wants to clean, merge, reshape, or split source datasets and produce a reproducible Jupyter or R Markdown processing notebook using the course data/code template, with verified outputs linked to later analysis.
---

# Data Processing

Turn confirmed source data into explicitly named processed datasets. Make each
transformation reproducible and document the relationship between input files,
processing code, saved outputs, and their intended analysis roles.

## What to inspect

- the request, confirmed preferences, and relevant `Data Artifacts` in `PROJECT.md`;
- [shared rules](../../FINDING-RULES.md), including data handoff and verification;
- relevant raw-data documents, source files, and existing processing code;
- existing downstream documents only when needed to preserve their input contract;
- the selected [Jupyter template](../../templates/data/code/template-data-processing-code.ipynb)
  or [R Markdown template](../../templates/data/code/template-data-processing-code.Rmd).

## Output targets

Write or update the selected `.ipynb` or `.Rmd` in `data/code/`. Save derived data
under `data/processed/`, and update the corresponding `Data Artifacts` records.
For a complete preparation request, use
[processed-data-documentation](../processed-data-documentation/SKILL.md) to document
each output. A code-only request may leave execution and output verification pending.
The selected notebook is the document for direct review. Export HTML only when
separately and explicitly requested; its absence is not incomplete.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Ask about unresolved duplicate conflicts, missing-value rules, join keys, sample exclusions, output roles, or split design before applying those choices. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

1. Carry known choices forward and apply the report-language default above. For tool preferences, ask
   for a missing format choice. Until that required answer arrives, inspect inputs
   read-only without changing data, creating deliverables, or executing processing.
2. Establish the observation unit, candidate keys, intended sample, variable meanings,
   output roles, and transformations. Resolve choices that materially change the
   sample, such as which conflicting duplicate to retain or what missing values mean.
   Do not require an outcome for a cleaning task that does not depend on one.
3. Select exact inputs using the student's request or verified project records. Check
   each path, actual bytes, schema, and relevant key assumptions. Preserve raw originals;
   documented multi-stage inputs may also be verified processed files. Reuse suitable
   existing processing code rather than rebuilding it without need.
4. Start from the matching template, keeping `README`, Author, Created At, Last
   Modified At, purpose, input, and output descriptions in their original order.
   Describe each named input/output, its role, and its documentation. Bind inputs to
   their verified project-relative paths and SHA-256 values in executable code.
5. Implement justified cleaning, merges, reshaping, or split creation. Replace the
   template's deliberate transformation stop with real work; do not pass through an
   input and call it cleaned. Document row counts and the reasons for sample changes.
6. Before writing, check intended output paths, distinctness from inputs, and containment
   in this project's `data/processed/`. Do not silently overwrite unrelated existing
   files. Execute the processing when requested, then reopen every serialized output
   and check schema, counts, keys, and task-specific constraints against the intended
   result. Compute SHA-256 from those saved bytes, not from an in-memory data frame.
   Retain outputs in the executed `.ipynb`; for `.Rmd`, run chunks in clean R
   (for example, `knitr::knit` to temporary Markdown), inspect the output, and
   backfill verified processing and read-back results in the source. This
   verification does not require HTML.
7. Record each actual output's role, path, producing notebook, linked documentation,
   checks, and hash in `Data Artifacts`. Complete requested output documentation using
   the saved files. If execution fails, keep the attempted output pending/failed;
   an older file left on disk is not proof the new processing succeeded.
8. Identify downstream notebooks known to use changed outputs. Rerun and refresh
   findings only when reanalysis is requested; otherwise report their earlier-data
   status and the exact processed files ready for future analysis.

## Writing and coding rules

- Follow the shared root/path/hash contract. Support spaces in filenames and multiple
  named inputs/outputs; never select the first glob result or latest modified CSV.
- Check join cardinality and unmatched keys; do not let an unintended many-to-many
  merge silently multiply rows. Use assertions based on confirmed definitions.
- Explain deduplication, type conversion, missingness, and exclusions. Missing data
  are not automatically invalid, and arbitrary imputation is not data cleaning.
- For prediction, establish and document the split unit before fitted preprocessing.
  Fit learned transformations only on training data, and inside each training fold
  for cross-validation. Apply training-fitted transformations to held-out data.
- Preserve original variables when useful for auditing. Keep large transformations
  here; downstream finding notebooks should load the verified saved outputs.
- Register only files actually written and inspected. A hash confirms identity,
  while schema, keys, roles, and relevant checks establish usability.
- Keep unknown provenance, unavailable dependencies, and partial execution explicit.
  Do not invent successful assertions or substitute another programming language without permission.

## Good output standard

The selected notebook can reproduce the named outputs from the documented inputs.
Saved-file checks support the data record, and a later analysis can identify its
intended dataset and version without relying on the earlier conversation.

## Example prompt patterns

- Merge these student and exam files into one student-level dataset using Jupyter.
- Turn this cleaning code into the course R Markdown processing template.
- Prepare and document train/test files, keeping all fitted preprocessing inside training.
