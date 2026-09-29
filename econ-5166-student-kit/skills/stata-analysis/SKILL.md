---
name: stata-analysis
description: Use when the student wants course Stata analysis, code, execution, or a record of existing Stata results. Produce the Stata-specific same-basename Markdown, do-file, and Google Doc delivery, or just the requested local record or code.
---

# Stata Analysis

Use this skill when documenting a Stata analysis for the course project.

The goal is to make Stata code and its actual results readable together while
preserving a concise local Markdown record. Follow the instructor's Stata-specific
format: a Markdown entry point, a do-file, and a Google Doc that places results
below the corresponding code. Do not require R/Python conversion or another
format-confirmation step when the student has already chosen Stata.

## What to inspect

Read the [shared course rules](../../FINDING-RULES.md) first.
Then inspect only the files needed for the task:

- the student's request and explicit preferences in `PROJECT.md`
- the relevant existing Markdown record in `finding/`
- Stata output, code, or a document excerpt supplied for this task
- relevant analysis data in `data/processed/` when code or execution is requested

When creating or updating the local record, read the
[Stata analysis template](../../templates/finding/template-stata-analysis.md).
The original template has only `Background` and a Google Doc link.
Do not infer additional instructor-required fields from these operating instructions.

Only when the student chooses R/Python or requests conversion, read the relevant
analysis skill and its selected Rmd/ipynb template:

- [stat-analysis](../stat-analysis/SKILL.md) for descriptive statistics, tests, and regression
- [prediction-model](../prediction-model/SKILL.md) for predictive modeling
- [simulation-runner](../simulation-runner/SKILL.md) for simulation results

## Output targets

Choose the output from the task, not the input file extension:

- **Existing-result or link registration:** a local Markdown record in `finding/`
  with the original `Background` and Google Doc link fields. This task needs no
  execution and no empty notebook.
- **Substantive Stata analysis finding:** a same-basename `.md`, `.do`, and Google
  Doc. Keep `Background` and the real Google Doc link in the Markdown file. Put
  the do-file contents in the Google Doc, with actual statistical output, tables,
  and figures directly below the corresponding code passages. This is the
  instructor's Stata-specific format alongside the general Rmd/ipynb format.
- **Explicit Stata code or execution request:** the requested `.do` file and,
  if run, its actual log. Respect a code-only request. When the student also wants
  a formal analysis finding, use the substantive-analysis route above.

Use the student's requested or existing filename; otherwise choose a descriptive
basename with the applicable extensions. Use that same basename as the Google
Doc title. A meeting date is not required for naming. Correct an existing analysis
in place and create a new file for an extension. Preserve an existing record's
useful content and links.

The instructor requires the `.md` and `.do` files to be submitted to GitHub.
Students create their own repository first and stage, commit, and push these
files themselves in VS Code under the shared Git workflow. The AI prepares the
files and a suggested commit message, then checks actual Git evidence read-only
afterward; a local commit does not prove GitHub delivery.

Google Doc actions retain their separate authorization rules. When Google Doc
creation is not authorized or the connection is
unavailable, prepare reviewable document content locally, leave a missing URL as
`待提供` or its report-language equivalent, and report the Google Doc delivery as
unfinished. Reuse authorization already given for the Google Doc in the
conversation; do not request it again. A local draft or link-only record is not
a completed substantive finding.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Discuss unresolved research definitions, sample rules, consequential model choices, and document metadata before dependent work; reuse an explicit Stata choice. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

When helping with Stata material:

1. Identify which output route matches the request. Reuse confirmed preferences
   and apply the report-language default above; ask only for material missing
   choices. An explicit request
   for Stata settles the tool and its dedicated delivery format; a `.dta` file
   alone does not. Ask for the analysis-tool preference only when it is unknown.
   Pure link registration uses Markdown and needs no analysis-tool questionnaire.
   While awaiting required answers, only inspect existing files.
2. Identify the analysis being recorded and the evidence available. Use the student's
   research question, data description, and existing output; do not invent findings.
3. For a pure record, create or update `finding/*.md` with the original fields.
   Fill `Background` from the supported context and use the supplied Google Doc
   URL. If missing, write `待提供` or its report-language equivalent as plain text.
4. For substantive Stata work, prepare or revise the do-file and assemble the
   Google Doc content in do-file order. Put each actual result immediately below
   the code that produced it, with explanatory text that makes the analysis
   self-contained. Follow the shared descriptive-statistics, figure, table, and
   regression rules. Preserve source labels for supplied results and mark gaps
   pending instead of inventing missing output.
5. Run Stata only when
   execution is within the request, first checking for an available Stata runtime.
   Honor code-only requests without running. Report the actual execution state
   and update findings only from genuine outputs.
6. Create or update the Google Doc when authorized and tools are available;
   otherwise finish its reviewable local content and identify the remaining
   external step. Check that the `.md`, `.do`, and Google Doc title share a
   basename and that the Markdown link points to the actual document. Validate
   code/result correspondence and report execution, document, and GitHub
   submission status separately.
7. If the student instead requests R/Python conversion, use the matching analysis
   skill for the selected Rmd/ipynb with actual results; export HTML only when
   separately and explicitly requested. Attribute any supplied Stata results
   and do not claim they were reproduced by formatting the new document. Implement and run an actual R/Python reproduction only within the
   requested scope, and explain any differences from the supplied results.

## Writing and coding rules

- Keep the record useful as long-term Markdown research memory. Distinguish the
  original template fields from optional detail added for the student's request.
- A background description can be drafted without results, but expected results
  must not be written as observed findings.
- Attribute supplied results to their source. Label them as student-provided and
  not rerun unless they have actually been rerun.
- Preparing a `.do` file is not execution. If Stata is unavailable, say so plainly,
  retain useful requested code, and mark execution as pending. Do not invent a log,
  estimates, significance levels, or successful execution; do not silently switch tools.
- When execution is requested, read analysis data from project `data/processed/`.
  Substantial merging, reshaping, deduplication, or missing-data treatment belongs
  in the [data-preparation](../data-preparation/SKILL.md) workflow in `data/code/`,
  not hidden in the findings record.
- Apply the shared course rules for figures, tables, and regression reporting to
  substantive Stata results in the Google Doc.
  Missing statistics in supplied output remain missing until supported by data
  and actual computation; do not infer them from significance symbols or prose.
- Missing data, model definitions, or output should remain explicit open questions,
  rather than being filled with guessed choices.
- Recording a Google Doc link does not authorize creating, uploading, sharing, or
  changing access to an external document, or sending messages.
  Carry out those external-document actions when authorized within the existing task or conversation;
  do not repeat an already settled permission question. Otherwise keep the work
  local and report the relevant external-delivery status as pending. Git operations
  remain the student's responsibility in VS Code, including under earlier Git
  authorization or a general request to complete the analysis. Mark uncommitted
  work `待提交` and report local commit and verified push status separately.

## Good output standard

A future reader should quickly understand:

- What analysis does this record refer to?
- Where is its source document, or which link is still missing?
- Which findings are supported by supplied or actually executed results?
- Was Stata run, and what remains unfinished?
- For a substantive Stata finding, do the `.md`, `.do`, and Google Doc share a
  basename, and does each code passage have its actual result below it?
- Are supplied results attributed and all remaining external steps identified?

Keep the note concise. Include technical detail when it helps interpret the actual
work, without turning this minimal course template into an invented specification.

## Example prompt patterns

- create a course Stata analysis record for these results
- update the background and document link in my Stata note
- summarize this Stata output in my existing finding record
- record this analysis locally while I obtain the Google Doc link
- run this Stata analysis and document the actual outputs
- write a Stata do-file and its finding record without executing it
- prepare the Google Doc content from this do-file and log, with results below the corresponding code
- turn these Stata results into an Rmd finding using the statistical analysis template
- use my Stata log as supplied evidence in an ipynb finding
