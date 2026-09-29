---
name: raw-data-documentation
description: Use when a student supplies original research data and wants a raw-data description, preview, variable definitions, or summary notebook using the course raw-data template. Produces Jupyter or R Markdown documentation while preserving the source files.
---

# Raw Data Documentation

Document what the original data contain and how they can be used. Keep the source
file intact, and distinguish observed properties from information still needed
from the student. Follow the project's Markdown memory and template workflow.

For updates to existing documentation after source notes, versions, schemas, or
links change, use [maintain-data-documentation](../maintain-data-documentation/SKILL.md)
to scope the refresh and retain this skill for raw-stage details. Text-only
maintenance does not require a new template or notebook execution.

## What to inspect

Read only the context needed for the current dataset:

- the request, explicit preferences, and relevant `Data Artifacts` in `PROJECT.md`;
- [shared rules](../../FINDING-RULES.md), especially preferences and data handoff;
- the original file, source notes, codebook, and any existing raw-data document;
- the selected [Jupyter template](../../templates/data/raw/template-doc-and-summary-stats.ipynb)
  or [R Markdown template](../../templates/data/raw/template-doc-and-summary-stats.Rmd).

## Output targets

Create or update a `.ipynb` or `.Rmd` alongside its source in `data/raw/`, using
a distinct descriptive basename such as `survey_documentation`. Preserve an
existing document name. Record the source and document in `PROJECT.md` →
`Data Artifacts`. The selected notebook is the document for direct review. Export
HTML only when separately and explicitly requested; its absence is not incomplete.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Ask about unresolved source, observation unit, dates, or variable meanings; do not invent definitions from column names. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

1. Reuse the student's explicit choices and apply the report-language default above.
   For tool preferences, ask for a missing Python/Jupyter versus R/R Markdown choice. While that
   required format answer is pending, inspect read-only; do not create outputs or
   execute the notebook.
2. Establish the source, observation unit, received date, sample period, and relevant
   variable meanings. Ask about ambiguities that affect interpretation. For a requested
   draft, mark unavailable metadata as pending instead of inventing it.
3. Preserve the original bytes under `data/raw/`. If the student supplied a file
   elsewhere, copy it only within the authorized data-documentation task, verify
   the copy, and retain the original name unless it conflicts with another source.
4. Start from the selected formal template. Preserve its field and section order:
   `Data Description` with Background, date received, Path to data
   file, Unit of observation, Sample period, Known issues, Definition for each
   variable; then packages, `Change for Your Own Data`, `Summary`, `Sample`, and
   `Summary Stats`. Fill added lineage fields with the actual file path and SHA-256.
5. Bind the notebook to the exact project-relative raw path and inspected SHA-256.
   Resolve this project root portably and check the binding before loading. Replace
   all placeholders and unrelated example outputs; do not fall back to another CSV.
6. Execute the selected format when documentation execution is requested. Show the
   actual first ten rows, relevant summaries, types, missingness, and potential key
   issues. Retain outputs in the executed `.ipynb`; for `.Rmd`, run chunks in
   clean R, for example with `knitr::knit` to temporary Markdown, inspect the
   output, and put verified results and figure references into the source. No HTML
   is needed for this verification. These checks describe the source; they do not
   certify it as cleaned.
7. Register one row per actual source file with role `raw`, its documentation,
   producer `not applicable (source)`, actual hash, and the checks that ran. Use
   the shared data-handoff rules; document next processing needs without silently
   starting a cleaning or modeling task the student did not request.

## Writing and coding rules

- Source metadata must come from the student or source material. Do not use today's
  date as the received date unless receipt today is established.
- Display meaningful variable definitions and explain percentage denominators or
  effective sample sizes when reporting summaries. Do not impose the statistical
  finding's full model/figure requirements on raw-data documentation.
- Inspect suspected duplicates or invalid values, but do not delete or repair them
  in this skill. Use [data-processing](../data-processing/SKILL.md) for authorized
  changes, with the original source retained.
- A verified raw-file identity means the documented bytes were inspected; it does
  not mean the data are ready for analysis. Keep known issues visible.
- Use relative links valid from the document's location, including filenames with
  spaces. In `PROJECT.md`, links are relative to the project root.
- Missing dependencies or unreadable inputs must remain explicit. Do not fabricate
  samples, summary results, hashes, or execution success.

## Good output standard

A reader can find the unchanged source, understand the rows and variables, inspect
actual summaries, and see what must be resolved before processing. The notebook's
read path, its documentation, and the project's data record identify the same file.

## Example prompt patterns

- Document this raw survey using Python/Jupyter and Traditional Chinese.
- Use the raw-data R Markdown template to describe these original files.
- Update this source-data notebook after I supply the codebook; keep the data intact.
