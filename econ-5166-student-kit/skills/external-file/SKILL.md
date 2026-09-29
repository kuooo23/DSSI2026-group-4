---
name: external-file
description: Use when the student wants to record or update an external analysis, report, or presentation in a local Markdown index using the ECON 5166 external-file templates. This skill documents links and update history; it does not automatically create, upload, publish, or share external files.
---

# External File

Use this skill when an analysis, report, or presentation lives outside the project
and needs a local record that the student and Codex can find and reuse later.

The goal is a faithful Markdown index and update history. Keep the record connected
to the actual external artifact without implying that the artifact was accessed,
created, or shared when it was not.

This skill covers information collection and pure link registration. When the
student requests statistical or prediction analysis in R/Python, use
[stat-analysis](../stat-analysis/SKILL.md) or
[prediction-model](../prediction-model/SKILL.md) to produce the selected
Rmd/ipynb template with actual results; export HTML only when separately and
explicitly requested. For a simulation, use
[simulation-runner](../simulation-runner/SKILL.md) with its original Rmd/ipynb
template; do not generate HTML unless explicitly requested. For substantive Stata work, use
[stata-analysis](../stata-analysis/SKILL.md) and its `.md` + `.do` + Google Doc
format. An external-file index can accompany an analysis; it cannot replace the
required analysis deliverables.

## What to inspect

Read the [shared course rules](../../FINDING-RULES.md) first.
Then inspect only the files needed for the task:

- the student's request and explicit preferences in `PROJECT.md`
- an existing local index for the same external file
- the URL, metadata, document content, or presentation material the student supplied
- related local notes only when they explain the artifact's purpose

Read the matching template when creating or updating its record:

- analysis material: [finding external-file template](../../templates/finding/template-external-file.md)
- reports or presentations: [report external-file template](../../templates/report/template-external-file.md)

Do not load unrelated project files or require analysis data just to register a link.

## Output targets

Create or update a Markdown record in `finding/` or `report/`, according to the
artifact's role. For information collection, the instructor requires the Markdown
file to have the same name as the external artifact. Use its basename without the
original extension, followed by `.md`: `policy-review.pdf` becomes
`policy-review.md`. For an online document without an extension, use its actual
title. Ask for the title or filename when unknown; use the actual external name
without adding a date or other prefix. If that name already contains a date,
retain it. Preserve existing relative links and historical content when
updating or correcting a record.

Use the selected template's original field order, including:

- `Author`
- `Date created` in `YYYYMMDD` format
- `File link`
- `File Description`
- `External file update log`

The order of description and link differs between templates; follow the actual file.
The report template also requests a full transcript for presentations.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Ask for unresolved authorship, original filename/date, artifact role, or source/link information; an explicitly requested incomplete index may retain pending fields. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

When creating or updating an external-file record:

1. Confirm that this is a pure record rather than a request to perform analysis.
   The local index format is Markdown; apply the report-language default above.
   Ask only for a missing external title/filename or metadata material to this task.
   Reuse known answers.
   Ask about the analysis tool only when handing off substantive analysis and no
   preference is known; carry an explicit Stata, Python/Jupyter, or R/R Markdown
   choice to the matching skill. While awaiting required answers, only inspect
   existing material.
2. Identify whether the artifact belongs with findings or reports and inspect the
   matching template. Reuse the current record when one already exists.
3. Fill the original fields from supplied or verified information. If the author,
   original creation date, or URL is unknown, mark it as pending rather than guessing.
4. Describe the artifact using material that is actually available. If a link cannot
   be read, distinguish the student's description from independently inspected content.
5. Preserve the update history. Add an entry only for a change that actually occurred,
   distinguishing a local-index update from a change to the external artifact.
6. For a presentation under the report template, include the supplied transcript or
   one the student explicitly asked to draft. If material is insufficient, mark the
   transcript as pending; do not invent an existing speech.

## Writing rules

- Keep the original template fields. Extra summaries, tags, or sections are optional
  task-specific additions, not new instructor-required fields.
- Use a real supplied or verified URL. Without one, put `待提供` or the report-language
  equivalent in the link field as plain text; do not leave a plausible-looking fake URL.
- The date of creating the local index is not necessarily the external file's creation
  date. Record unknown original dates as pending rather than replacing them with today.
- Preserve student-written descriptions, comments, filenames, and historical entries
  when updating a record. Apply the same-name rule to new records; resolve an
  existing naming mismatch within the current task while preserving links and
  history. Revise only what the current task needs.
- The full-transcript requirement applies to presentations in the report template;
  do not extend it to every external file. Label newly drafted material as a draft.
- Do not claim to have read a document or verified sharing settings without access.
  A useful index can still record supplied metadata with its limitations made clear.
- The template's sharing reminder does not authorize changing permissions. This
  workflow does not automatically create, upload, publish, or share external files,
  or send messages. Report local-record and external-delivery status separately.
- Follow the shared Git workflow: students create their own repository first and
  stage, commit, and push the local index themselves in VS Code. Provide the
  changed-file list and a suggested commit message, then check status and actual
  commit evidence read-only after they act. Keep uncommitted work `待提交`;
  a local commit does not establish that the index was pushed or that the external
  artifact was uploaded.

## Good output standard

A future reader should quickly answer:

- What is the external artifact, and why is it relevant?
- Who created it and when, or which metadata is still missing?
- Where is the real link, and was its content actually inspected?
- What changed, and is a required presentation transcript available?
- Does the Markdown filename match the actual external artifact's basename?

Keep the record short enough to skim and reliable enough to serve as project memory.

## Example prompt patterns

- register this Google Doc as an external finding
- add a local record for our presentation
- update the report link and its change history
- document this external file while its URL is still pending
- attach my supplied presentation transcript to the report record
