---
name: maintain-project-context
description: Maintain PROJECT.md when asked to update project context, confirmed preferences, a student's AI model and agent entrypoint, current data and focus, the Data Artifacts index, or contributions with commit references. Use for scoped project-memory updates; data-documentation skills can still update their own artifact rows directly.
---

# Maintain Project Context

Keep `PROJECT.md` useful for the next task by recording confirmed context and
traceable evidence. Edit the relevant sections in place; preserve unrelated
content and the existing table formats. This is a Markdown maintenance task,
so it does not require an R/Python choice unless new data documents or analysis
are also requested.

## Read the relevant evidence

- Read the request, [project rules](../../AGENTS.md), and the actual project-root
  `PROJECT.md`. Use the existing filename rather than creating a duplicate for
  a spelling or capitalization variant in the request.
- For data rows, read [data handoff rules](../../FINDING-RULES.md#資料銜接與檔案驗證),
  the named files, and their linked documentation and producing code as needed.
- For contributions, read the supplied contribution descriptions, relevant
  artifacts, and targeted Git history and diffs if available. Read `TEAM.md` only
  when needed to resolve identities or confirmed roles. Use finalized reports
  only when they provide evidence relevant to the requested update.

Use the latest explicit user correction over older project context. Preserve
unknowns as pending; ask only about ambiguity that prevents the requested update,
and continue independent sections. A request to update one section does not
require completing every blank in the file. Report prose defaults to zh-TW;
preserve formal English field names and an explicit language preference.

When student names or actual responsibilities are missing from the conversation
and project records, explicitly ask for them before attributing this task or
updating author/role fields. Ask only for the missing part; do not infer it from
Git authors, computer accounts, filenames, examples, or who supplied an artifact.
Keep unanswered fields pending while independent updates proceed. Preserve
established authorship; the current student is not automatically the original author.

The course default is 3–4 students per group. At initial group setup, ask for the
members' names, confirmed actual work, and which member is speaking when unknown.
Use the supplied actual roster, one member per row; do not turn the default or
placeholder rows into confirmed people or infer roles from group size.

## Maintain the existing sections

| Section | What to record |
| --- | --- |
| Research Question | The student's own initial idea and confirmed question/scope. Preserve a tentative idea as tentative; do not fill an empty field by inventing a topic from the data. Keep hypotheses or proposed changes labeled as proposals until confirmed. |
| Team | Student-supplied or confirmed names, IDs, GitHub accounts, and roles in `Name / Student ID / GitHub Account / Role`. Record confirmed actual work along with the role in `Role`; ask for missing name/work rather than assigning duties. Do not infer roles from commit history. |
| Student Preferences | Explicit tool/artifact choices and other preferences. Keep the zh-TW teacher default distinct from the student's explicit language choice. |
| AI Agent Context | Preserve the five columns `Student`, `AI tool / client`, `Model`, `Agent entrypoint`, and `Source`. Record only the confirmed current student's actual tool, model or known family, selected entrypoint, and evidence source under AGENTS.md's Model and Agent Selection. Update that student's matching row; do not copy another member's or the teacher's setup. Exact model versions may remain unconfirmed. |
| Repository Context | Preserve `Field / Details` with `Remote repository`, `Target branch`, `Setup status`, and `Last push verification`. Record student-supplied or read-only verified project repository information, with evidence source and verification limits. A configured remote or cached tracking ref alone does not verify a push. Keep template placeholders during teacher maintenance; absence of a repository in the teacher's template is not an unfinished student setup. |
| Data and Current Focus | Preserve the `Field / Details` table and its four fields: `Data sources / documentation`, `Unit of observation`, `Current task / target variables`, `Assignment constraints`. Link local sources where available; distinguish observed data from plans and confirmed tasks from suggestions. |
| Data Artifacts | Maintain the exact seven-column index described below from actual files and checks. |
| Key Contributions | Keep `Name / Contribution / Commit reference`; one contribution per row, each requiring a supporting commit. Clearly mark uncommitted work, unverified references, and unresolved attribution as pending. |

Update a matching field or row instead of appending a duplicate. Preserve useful
student notes and established terminology. Keep current focus concise; detailed
data definitions belong in data documents and findings belong in their artifacts.

For AI agent context, use reliable current runtime information to establish the
actual model/client; a saved preference or a request to switch is not evidence
that a switch happened. Keep desired future choices in Student Preferences when
relevant. If the student is not identified, select the applicable entrypoint for
this session without attributing a table row. Never create student records from
the teacher's template-maintenance session.

During proposal development, keep brief research-context notes for the current
discussion stage, the students' confirmed choices, and the next unresolved
question. Preserve the distinction between AI suggestions, Demo assumptions,
and student decisions; an AI-written draft does not itself confirm its design.
Refresh these notes when the design or discussion stage changes, not for a
wording-only edit.

## Data Artifacts

Keep `Dataset | Role | Data file | Documentation | Processing notebook |
Verification | SHA-256`, with one row per actual data file and separate rows for
train and test. Use exact project-relative links; resolve them before writing.

- Inspect the selected on-disk file before adding or re-verifying its row.
  Record its SHA-256 from bytes, schema, row count, and relevant unit/key/role
  checks. A hash alone establishes identity, not analysis readiness. Reuse
  existing evidenced checks for an unchanged version, retaining their original
  dates and limits; do not represent them as newly executed.
- Register an existing but unverified file honestly as `pending` or `failed`,
  with the actual checks and limitations. An empty project keeps an empty table.
  Do not invent a ready row for a planned file. If an already indexed file is
  now missing, retain its known identity and mark it missing/pending; the old
  hash is a recorded value, not a new verification.
- Keep verified source, document, producing notebook, and role consistent.
  Use `not applicable (source)` for an original input's producing notebook and
  `not available` for genuinely unavailable external producing code. Missing
  documentation is `pending`, not a link to a file that has not been created.
- For a hash mismatch, resolve whether the new version is intended using the
  request and provenance before accepting it. For an unresolved mismatch, retain
  the recorded hash, note the observed mismatch in `Verification`, and ask about
  that version only. For an authorized replacement, recheck and update the row;
  identify known documents/findings still bound to the prior path or hash.
- A project-index update does not update notebook inputs, outputs, or findings.
  When document maintenance is part of the task, use
  [maintain-data-documentation](../maintain-data-documentation/SKILL.md).
  Otherwise report affected artifacts for follow-up. Do not run processing or
  analysis notebooks just to populate this table.

## Key Contributions and commit evidence

The course requires **all contributions to be recorded in commits**, including
documentation and project-context maintenance. A contribution record is incomplete
without a verified commit that supports it. Update the table as work progresses.
For external/non-file work, a committed substantive description or external index
can record the contribution; do not imply the external artifact itself is in Git.

Include substantive context maintenance as well as supplied contributions,
reusing its matching pending row when present. Updating a contribution's status
or reference alone does not create another contribution row; this avoids an
endless chain of index-only records. If its contributor or actual work is unknown,
ask the student for the missing information; until answered, write `待確認` in
unresolved fields and keep the attribution pending. Do not assign a student or
leave the pending work only in chat. Preserve earlier completed contributions.

Write what the member actually contributed, such as a named data transformation,
analysis, documentation revision, or deliverable. Preserve jointly credited work
when supplied. Do not turn commit counts or changed-line totals into evaluation.

For each supplied or discovered commit reference:

1. Check the relevant project's Git context read-only before searching. Confirm
   that the repository is the student's project, not an enclosing teacher/template
   repository. Inspect the commit and relevant changed files, for example with
   `git show --stat <sha>` and
   `git show <sha> -- <relevant-path>`. Use a supplied period or task to bound a
   broader search. A subject line alone is insufficient evidence for the claim.
2. Verify that the referenced change supports the contribution description.
   A commit records changes; it does not prove sole authorship, effort, runtime
   correctness, acceptance, or completion. Use explicit identity mappings in
   the user's information or `Team`/`TEAM.md`; do not infer a student's identity
   or role from an unfamiliar Git author. Label unresolved attribution pending.
3. Record the actual verified SHA. Mark remote delivery verified only with fresh
   read-only evidence that the intended remote branch contains that commit;
   knowing a remote URL or opening a commit page alone does not establish delivery
   to the target branch. Use a verified web commit link with that delivery status.
   A verified local commit awaiting push is
   `<SHA>（已本機 commit，待 push）`; if remote status cannot be checked, use
   `<SHA>（本機已核對，遠端待核對）`. Use remote information only when needed
   and never copy credentials from a remote URL into the document. Local
   tracking refs may be stale; do not infer current GitHub delivery from them.
4. With no Git history or uncommitted work, record the supported work as
   `待提交（貢獻紀錄未完成）`. An inaccessible or unverified reference is
   `待核對（貢獻紀錄未完成）`. Include an artifact link in the contribution cell
   if available, but it cannot replace the commit reference. Do not invent a SHA
   or fabricate a URL. A missing reference remains outstanding even when the
   local artifact is ready for review.

Follow [the project Git workflow](../../AGENTS.md#course-repository-and-git-workflow): students first create their
own repository, then use VS Code themselves to clone, stage, commit, push, pull,
and sync. The AI prepares artifacts, suggests a commit message, and checks Git
status/history read-only. A general completion/submission request or earlier Git
authorization does not replace these student actions. Do not create/init a
repository, change remotes, stage, commit, push, pull, sync, or fetch for them.

Leave new work pending until the student makes its commit, then inspect the
actual commit and update the existing row. Distinguish local commit evidence
from verified remote delivery. Do not create empty commits or attach unrelated
commits just to satisfy the table. A commit cannot contain its own hash: reference
the artifact commit in a later index update for the student's next commit.
Do not add a new row or demand another commit solely to record that index update's
own hash. If the student repository is not set up, continue independent discussion
and read-only checks, and wait before writing course deliverables. An existing
repository without commits keeps contribution references pending. Teacher
template maintenance retains repository placeholders without attributing missing
setup or contributions to students.

## Check and hand off

Review the edited sections for table alignment, duplicate rows, valid local
links, and agreement with the supplied information and inspected evidence.
Preserve existing content outside the requested scope. Describe what changed,
what was actually checked, and any pending input or affected prior artifacts.

This skill does not finalize weekly reports or synchronize `BACKLOG.md`,
`DECISIONS.md`, or `RISKS.md`; use the existing weekly workflow if that work is
also requested. Hand off the changed files and a suggested commit message for
the student's VS Code workflow. Report artifact readiness, local commit evidence,
and verified remote delivery separately; a table edit itself is still a local
change until the student commits and pushes it.
