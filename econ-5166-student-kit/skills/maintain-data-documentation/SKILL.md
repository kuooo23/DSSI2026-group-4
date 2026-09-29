---
name: maintain-data-documentation
description: Maintain existing raw and processed data documentation when source notes, file versions, schemas, links, summaries, or processing lineage change. Update the associated PROJECT.md Data Artifacts records while preserving data and distinguishing text edits from computations that need refreshing.
---

# Maintain Data Documentation

Keep the existing data documents and current data index consistent with the files
they describe. This task covers documentation and verification of saved inputs;
new cleaning, merging, splitting, or analysis uses its matching skill when requested.

## Read the relevant evidence

Read [shared data-handoff rules](../../FINDING-RULES.md#資料銜接與檔案驗證), the
request, confirmed preferences and affected `Data Artifacts` rows in `PROJECT.md`,
then the affected raw/processed document and exact data files. Consult codebooks,
source notes, and producing notebooks only as needed to establish what changed.
Do not choose a version from modification time, glob order, or a similar filename.

Reuse the existing document's name, `.Rmd` or `.ipynb` format, section structure,
and relevant content. Editing an identified notebook already establishes its format.
Apply the report-language preference or the shared zh-TW default. Read a template
only when creating a missing document or restoring required fields; ask about a
missing format only when a new document needs that choice.

Reuse confirmed student names and actual responsibilities. If either is missing,
explicitly ask the student for that information before filling this update's
author or contribution fields; a pending label alone does not replace asking.
Continue independent inspection while awaiting the answer. Preserve the existing
document's supported authorship; do not infer new attribution from Git, account
names, filenames, or the person supplying the file, and do not assign duties.

Use the stage-specific guidance for the actual documentation work:

| Document being maintained | Stage skill and relevant detail |
| --- | --- |
| Original source data | [raw-data-documentation](../raw-data-documentation/SKILL.md): source metadata, variable definitions, preview and source checks |
| Saved prepared data | [processed-data-documentation](../processed-data-documentation/SKILL.md): processing lineage, role, summaries and justified assertions |

For an existing document, apply those details to the affected content; their
creation and execution steps do not require recreating or executing an unchanged
document during a text-only update.

## Decide what needs refreshing

- **Text or link correction:** update confirmed metadata, definitions, provenance,
  or links in place. Check whether an interpretation or path change also affects
  code, summaries, or assertions. If computed content still matches the documented
  file, retain it and its actual execution history; a prose edit is not a new run.
- **Changed bytes, schema, read code, or requested summary refresh:** establish the
  intended file version from the request and processing evidence, inspect the saved
  file, compute its actual SHA-256, and identify affected samples, summaries,
  assertions, and prose. Update expected paths/hashes only after that identity is
  resolved; never replace expected hashes at runtime to force a check to pass.
- **Unresolved or unavailable evidence:** ask only for information needed for the
  dependent work and continue independent corrections. Mark unknown source,
  received/creation date, author, unit, or definitions as pending. A new file date
  or column name does not establish those facts.

Keep a concise version/change note when data or processing lineage changes, with
the known prior version and limitations. If a document now targets a new version,
refresh its dependent results or clearly mark them stale/pending and remove stale
cell outputs presented as current. Preserve useful prior results only as explicitly
labeled history tied to the old version. Do not invent numerical updates.

## Recompute only documentation that needs it

Before running an existing notebook/Rmd, inspect its executable cells/chunks and
referenced local scripts for writes, downloads, processing, child notebooks, and
analysis calls. A file called “documentation” can still overwrite raw/processed
data or run the full pipeline. Documentation maintenance alone does not authorize
those side effects.

Use the stage skill's execution and verification procedure for affected summaries
and checks. Execute a self-contained, read-only documentation workflow in a clean
kernel/process against exact verified inputs; isolate or skip unrelated side-effect
code rather than running the entire pipeline. If safe isolation is not practical,
complete supported edits and mark the computation pending with its specific blocker.
Do not report a full notebook run when only selected code was checked. Retain actual
Jupyter outputs or inspect temporary Rmd execution results as the stage skill requires.
Do not add HTML exports unless requested.

Preserve raw and processed file bytes. A failed assertion describes a data issue;
it does not authorize repairs. Use [data-processing](../data-processing/SKILL.md)
only when the user's task includes the required data changes. Do not regenerate
missing upstream code just to fill a provenance field.

## Synchronize the current data index

Update the affected `PROJECT.md` → `Data Artifacts` rows in place using the shared
columns: `Dataset | Role | Data file | Documentation | Processing notebook |
Verification | SHA-256`.

- Keep one row per actual data file, including separate train and test rows with
  confirmed roles. One notebook documenting several files does not combine their
  file identities or checks. Update an existing file's row instead of duplicating it.
- Link the exact data, document, and known producer. Raw sources use
  `not applicable (source)`; an externally prepared file with unavailable producing
  code uses `not available` and retains its known source.
- Calculate hashes from actual saved bytes. Record only checks that ran, their
  execution date and material limits. A hash check alone verifies identity, not
  schema, cleaning, suitability, or a successful summary refresh. Keep pending,
  failed, and stale states visible; never relabel an old output as a new success.
- Register only inspected files. For a previously indexed file now missing, make
  its unavailability explicit and resolve the intended replacement before presenting
  it as a current usable input. Retain relevant prior lineage in the document.
- Verify links from the document's directory and from the project root for
  `PROJECT.md`; retain portable exact paths, including filenames with spaces.

Updating these data rows is part of this skill. Use
[maintain-project-context](../maintain-project-context/SKILL.md) when the request
also calls for changes to research focus, preferences, constraints, or contributions.

Search directly relevant readers for superseded paths/hashes and identify affected
findings. A refreshed documentation hash or index does not refresh prior analyses.
Rerun and update findings only when reanalysis is included in the user's request.

## Completion

Inspect the changed documents and index for agreement among data path, version,
role, lineage, summaries, and verification status. Report which files changed,
whether any computation ran, unresolved items, and known findings still based on
older data. Do not create a separate report merely to record routine maintenance.

Data documentation and index updates are contributions and need a supporting commit
for the contribution record to be complete. Record the current maintenance work in
`PROJECT.md` → `Key Contributions`, reusing a matching pending row or adding one
with the changed document links. Use the confirmed contributor name and work;
if still unanswered after asking, write `待確認` rather than assigning a student.
Uncommitted work uses
`待提交（貢獻紀錄未完成）` in `Commit reference`, not only a chat reminder.
Follow [the project Git workflow](../../AGENTS.md#course-repository-and-git-workflow): students create their own
repository first and use VS Code themselves for clone, stage, commit, push,
pull, and sync. Provide the changed-file list and a suggested commit message;
do not perform Git mutations for students under a general request or earlier
authorization. After the student commits, inspect the actual supporting changes
read-only before filling the reference. An unrelated old commit is not evidence
for this update, and a local commit does not prove a push. Use
`<SHA>（已本機 commit，待 push）` when unpushed, or
`<SHA>（本機已核對，遠端待核對）` when remote status is unknown; use a verified
remote commit link only with fresh evidence that the intended remote branch
contains the supporting commit. Cached tracking refs do not establish this.
Do not invent a SHA.
Reuse the current contribution row when filling its reference; the index-only
update goes into a later student commit without another row for its own hash.
If student repository setup is missing or ambiguous, continue only independent
discussion and read-only checks until setup is confirmed. Teacher template
maintenance and explicitly scoped isolated demos follow the shared exceptions.
Once the repository is set up, pending student commit/push does not block
otherwise authorized documentation updates; keep their submission status pending.
