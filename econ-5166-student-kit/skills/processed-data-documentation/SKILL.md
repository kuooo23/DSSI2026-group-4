---
name: processed-data-documentation
description: Use when a student wants to document or validate a prepared dataset using the course processed-data Jupyter or R Markdown template, and register its exact path, role, provenance, and verified version for downstream statistical or prediction analysis.
---

# Processed Data Documentation

Describe the actual saved dataset and verify the assumptions later analyses need.
Connect its data file, producing code, and documentation through the project's
data record, so later tasks can choose the right sample and version.

For updates to existing documentation after versions, schemas, links, or lineage
change, use [maintain-data-documentation](../maintain-data-documentation/SKILL.md)
to scope the refresh and retain this skill for processed-stage details. Text-only
maintenance does not require a new template or notebook execution.

## What to inspect

- the request, explicit preferences, and relevant `Data Artifacts` in `PROJECT.md`;
- [shared rules](../../FINDING-RULES.md), especially data handoff and verification;
- the exact saved processed file, existing documentation, and its producing code;
- source documentation only when needed to explain lineage or variable definitions;
- the selected [Jupyter template](../../templates/data/processed/template-doc-and-summary-stats.ipynb)
  or [R Markdown template](../../templates/data/processed/template-doc-and-summary-stats.Rmd).

## Output targets

Create or update the chosen `.ipynb` or `.Rmd` beside the data in `data/processed/`
using a distinct documentation basename. Register or update its `PROJECT.md` →
`Data Artifacts` row. Reuse a suitable existing document, and document multiple
outputs together only when each has an explicit path, role, and separate checks.
The selected notebook is the document for direct review. Export HTML only when
separately and explicitly requested; its absence is not incomplete. This task
does not itself require a statistical finding.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Ask when the intended file version, role, provenance, key, or variable definition remains uncertain; do not repair or certify assumptions by guessing. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

1. Reuse confirmed preferences and apply the report-language default above; ask
   for a missing Python/Jupyter versus R/R Markdown preference. Until that required
   format answer arrives, inspect read-only without generating outputs, changing data,
   or running documentation notebooks.
2. Identify the intended file and sample from the student's request or project record.
   Establish the observation unit, variable definitions, key expectations, and role
   such as analysis, train, or test. Ask if several versions or roles remain plausible.
   Do not use modification time or glob order to choose the dataset.
3. Inspect the actual file bytes and producing notebook when available. An externally
   prepared file may have producer `not available`; record its real provenance and
   inspect suitability instead of inventing code or requiring unnecessary processing.
   Follow the shared rules when a registered hash differs from the current file.
4. Start from the formal template and preserve `Data Description` fields: Author,
   Date first created, Background, Unit of observation, Sample period,
   Known issues, Definition for each variable; then packages, `Change for Your
   Own Data`, `Summary`, `Sample`, `Summary Stats`, and `Assertions`. Fill added path,
   source, producer, role, validation, and SHA-256 fields from evidence.
5. Bind the read code to the exact project-relative processed path and verified
   SHA-256. Check file existence and bytes before loading, then validate relevant
   schema and key assumptions. Show actual first ten rows and useful summaries;
   remove unrelated examples and outputs.
6. Write and execute meaningful assertions for confirmed properties, such as a unique
   entity-time key, allowed categories, or output counts justified by processing.
   For split data, validate documented roles and overlap at the correct split unit.
   Do not assert arbitrary ranges or require no missing values without a basis.
   Retain outputs in the executed `.ipynb`; for `.Rmd`, validate chunks in clean R
   (for example, `knitr::knit` to temporary Markdown), inspect the output, and
   backfill verified results and figure references in the source. No HTML is
   needed for this verification.
7. Compute the hash from the saved file, record check results and remaining issues,
   and update one `Data Artifacts` row per actual data file. Verification should name
   what passed and material limitations; do not equate a matching hash with clean data.
8. Hand off the exact data/document/producer paths and intended role to
   [stat-analysis](../stat-analysis/SKILL.md) or
   [prediction-model](../prediction-model/SKILL.md) only when analysis is requested.
   Otherwise the verified index supports a later analysis task. Identify findings
   using a superseded version, without silently rerunning them outside the request.

## Writing and coding rules

- The file being documented must be the same saved file downstream code will read,
  not an intermediate object with different rows or columns.
- Preserve existing notes and provenance. Unknown creation dates and authors remain
  pending; a new documentation date does not establish the data's creation date.
- Keep summary sample sizes, denominators, missingness, and variable meanings clear.
  Do not add the finding's full regression or prediction requirements to this document.
- Documentation and validation must not silently repair data. When correction is
  needed, explain it and use [data-processing](../data-processing/SKILL.md) within
  the student's authorized scope, then validate the newly saved output.
- Keep links relative to the document location, and `PROJECT.md` links relative to
  the root. Paths with spaces must work in both prose links and executable readers.
- Record pending/failed execution honestly. Never register a stale output from a
  failed processing attempt as the newly verified result.

## Good output standard

The description, sample, summaries, assertions, and project record all refer to
the same saved data. A later finding can identify its exact input, role, and version,
understand its limitations, and fail clearly if the file has changed.

## Example prompt patterns

- Document this processed panel in R Markdown and verify its entity-year key.
- Check these saved train/test datasets and link their notebooks for later prediction.
- Register this externally prepared CSV with its source notes and Jupyter documentation.
