# AGENTS.md

## Model and Agent Selection

For student work, select the instruction entrypoint from the student's current
model family and the actual client. This selects project instructions; it does
not change the running model, launch another service, or grant new tools.

- Use reliable current runtime information and the student's explicit current
  model/client selection. Do not infer the model from filenames, available skill
  folders, computer accounts, response style, or a previous student's settings.
  Current reliable runtime information establishes the actual running model;
  a request or saved preference does not override that observation.
  If the student requests a different model than the one actually running,
  distinguish the requested setup from the current session instead of claiming
  to have switched. Clarify a conflict only when it affects the next action.
- Claude-family models (including Opus, Sonnet, and Haiku): use `CLAUDE.md`,
  which imports this shared file. If `CLAUDE.md` is already in context, continue
  without loading either entrypoint again. In a client without import support,
  read both files once. Claude Code-specific commands apply only in Claude Code.
- OpenAI/GPT-family models: use this `AGENTS.md`.
  Do not load the Claude adapter merely because it exists in the same project.
- If the model family is unknown but the client is confirmed to be Claude
  Code or Codex, use that client's native entrypoint (`CLAUDE.md` or `AGENTS.md`)
  and keep the model unconfirmed. If the model family is known, its entrypoint
  takes precedence even when the exact version is unknown. No model-version
  question is needed merely to select this entrypoint.
- Select once for the current model/client. A client's natively loaded file is
  the bootstrap; reading the selected model adapter does not change that client.
  Do not rerun selection or reimport shared rules just because another entrypoint
  has been read.
- For another confirmed model family, use `AGENTS.md` as the shared fallback
  and explain that there is no dedicated adapter for that model. Use only tools
  actually available in the current client.
- If neither the model family nor the client is known, ask once which AI tool
  and model the student is currently using. Continue independent read-only work
  while waiting; keep the entrypoint pending rather than guess. Do not ask again
  once enough current information is available.
- A model name alone does not establish that the client loads local files.
  Codex and Claude Code have native project entrypoints; in other clients,
  explicitly read the selected files if file access is available. Otherwise
  request the relevant file contents and do not claim that local rules loaded.
- Once the student's identity is confirmed, maintain that student's row in
  `PROJECT.md` → `AI Agent Context` when recording project context is authorized.
  Record the actual client, confirmed model (or unknown exact model), selected
  entrypoint, and evidence source. Reuse it only when it still applies to the
  current student/session; one group member's choice is not the whole group's
  default. Teacher maintenance must not populate this table with the teacher's
  runtime or invent student settings.

## Repo Purpose

This repository is a reusable workspace for:

- theoretical research in econometrics, statistics, and related fields;
- empirical research in economics, data science, and related fields;
- software and application development involving data science, statistics, or
  research workflows.

The repository is designed so that:

- Markdown stores working research and project memory;
- LaTeX in `deliverable/paper/` stores an evolving formal draft when the
  project includes a paper;
- files in `deliverable/slides/` are presentation artifacts, often initialized
  from the paper draft and later revised in place;
- software or application deliverables can live in `deliverable/app/`;
- Codex can use local files to support the relevant parts of the workflow.

Do not assume that every project uses every folder or workflow in this
template. Prefer project-specific local context over template defaults.

All paths below are relative to this student project root, which contains
`AGENTS.md`, `data/`, `finding/`, and `templates/`.
All skills are stored in `skills/`, and all reusable templates are stored
in `templates/`. Shared rules and workflow documents live at the project root.

## Course Finding Workflow

For data preparation and finding deliverables, use the course-specific rules
below together with the research conventions in this file.

- Read `FINDING-RULES.md` and only the matching skill and
  template. New requirements are limited to the instructor's pasted information
  collection, statistical analysis, Stata, and prediction sections, with the
  latest clarifications. Use the template structure together with those
  requirements, including the added prediction summary-statistics block.
- Ordinary statistical and predictive findings use the student's selected `.Rmd`
  or `.ipynb`. The instructor reviews that file directly; the latest instruction
  supersedes the pasted source's paired-HTML requirement. Do not generate HTML
  by default. Export it only when the user separately requests it.
  A plain `.R`, `.md`, or chat response is not a complete analysis deliverable.
  Pure external-link records retain their original Markdown format.
- Stata uses its pasted exception: same-basename Markdown, do-file, and a Google
  Doc pairing each code segment with its results. Simulation retains its original
  Rmd/ipynb template; do not impose paired HTML or rules from other sections on it.
- Use a student-specified, existing, or descriptive analysis basename; the
  instructor has waived the source document's meeting-date naming requirement.
  Do not ask for a meeting date merely to name an analysis. When an HTML export
  is requested, use the same basename and verify that it matches the source.
- For statistical and prediction notebooks, follow the shared figure, table,
  regression, and prediction requirements. Execute and inspect actual results,
  figures, tables, and their agreement with the findings. Run Jupyter from a clean
  kernel and retain outputs in the `.ipynb`. Rmd may be verified in a clean R
  process with `knitr::knit()` to a temporary location; inspect those results and
  write confirmed findings back into the `.Rmd`. Temporary verification outputs
  are not deliverables. Retain actual execution status; HTML is not a completion
  condition unless separately requested. Stata figures and tables follow the same
  presentation rules.
- Ask for any missing analysis format preference (Python/Jupyter or
  R/R Markdown; an explicit Stata request settles its tool choice) before creating
  deliverables, changing data, or running analysis. Default report language to
  Traditional Chinese as used in Taiwan (zh-TW), with Taiwan terminology and
  phrasing; follow an explicit student language choice instead when provided.
  Missing report language does not require a question or delay. While waiting
  for a required format answer, inspect
  inputs read-only. Do not infer a preference from installed software.
- Preserve choices explicitly provided in chat or `PROJECT.md`; distinguish the
  teacher's language default from the student's explicit answers in
  `Student Preferences`. Retain original template field names. A request to
  edit a named existing notebook already determines its format.
- If a student only supplies data, inspect it and ask for their own initial
  observation or question. Do not generate a topic menu, select an outcome, or
  develop a research direction before the student supplies an idea.
- Preserve raw inputs. Put substantial preparation in `data/code/` and derived
  data in `data/processed/`; statistical and prediction findings read those
  prepared inputs. Simulation may generate data from its DGP.
- The slash in template paths such as `/data/processed` denotes this project,
  not the operating system root. Generated files must use portable paths.
- Write substantive findings only from actual outputs. Label unexecuted drafts
  and student-supplied results honestly inside the artifact.
- Do not turn a finding request into a weekly progress report or finalize any
  management record. The optional manager-led weekly workflow stays separate.

| Student task | Repo-local skill | Template / output |
| --- | --- | --- |
| Preparation across data stages | `data-preparation` | coordinates the three data skills below |
| Describe unchanged original data | `raw-data-documentation` | `templates/data/raw/` → `data/raw/` notebook/Rmd |
| Clean, merge, reshape, or split | `data-processing` | `templates/data/code/` → `data/code/` notebook/Rmd; saved outputs in `data/processed/` |
| Document and verify saved analysis inputs | `processed-data-documentation` | `templates/data/processed/` → `data/processed/` notebook/Rmd |
| Maintain existing raw/processed data documents | `maintain-data-documentation` | updates affected documents and their `Data Artifacts` rows |
| Maintain project context and contribution evidence | `maintain-project-context` | scoped updates to `PROJECT.md`, including its tables |
| Descriptive statistics, tests, regression | `stat-analysis` | `template-stat-analysis` → `finding/` |
| Train/test prediction and model comparison | `prediction-model` | `template-prediction-model` → `finding/` |
| Numerical simulation | `simulation-runner` | `template-simulation` → `finding/` |
| Stata work / link record | `stata-analysis` | full analysis: `.md` + `.do` + Google Doc; pure index: `.md` |
| External result / report index | `external-file` | `template-external-file.md` → `finding/` or `report/` |

Skill entrypoints are `skills/<skill-name>/SKILL.md`. For a matching task,
read the relevant entrypoint from this directory and follow it even when it
is not listed in a native skill selector. Read only the relevant skill and
its required references. Multiple skills may be used in sequence when a task
needs both preparation and analysis; carry confirmed preferences forward.

Students submit the selected statistical or prediction `.Rmd` or `.ipynb` to
GitHub themselves; paired HTML is not required. Stata still requires Markdown
and do-file. Follow the student-operated Git workflow below. External document
creation and sharing remain subject to their separate task authorization.

## Course Repository and Git Workflow

Students first create their own group repository, clone it through VS Code, and
place the complete student-kit contents at its root, including hidden project
files. Each member works in their own local clone. Open that root in VS Code and
the AI client; do not use a downloaded ZIP directory as if it were already a repo.

- Before creating or editing student deliverables, check the intended repository
  root and configured remote read-only. If missing or ambiguous, ask the student
  to finish setup in VS Code and provide the repository URL; wait for setup before
  writing course deliverables. Discussion and independent read-only inspection
  may continue. Teacher template maintenance and explicitly scoped isolated demos
  do not require creating a student repo or filling student setup records.
- Repository creation, cloning, staging, commit, push, pull/sync, remote/branch
  changes, and history changes are performed by students in VS Code. AI must not
  perform these Git mutations through shell, UI, API, or another agent. A student
  asking for submission receives instructions for doing it themselves, not an
  approval prompt followed by AI submission. This course rule replaces earlier
  wording that allowed AI submission after authorization.
- AI may produce and verify local artifacts, inspect Git state and relevant diffs
  read-only, list files to review, and suggest a commit message. Students inspect
  the diff, stage the intended files, commit, then push and check the target branch
  on GitHub. Report that handoff clearly; do not mark it done before evidence.
- Use commands such as `git status`, `git diff`, `git log`, `git show`, and
  `git rev-parse` for local checks. Do not expose credentials from remote URLs.
  Do not fetch, pull, or sync merely to verify a push; use an available read-only
  remote view, or ask the student to refresh and check in VS Code/GitHub.
- Keep states distinct: no supporting commit = `待提交`; verified local commit
  with push status unknown = `已 commit；推送待核對`; evidence it is unpushed =
  `已 commit；待 push`; supporting commit verified on the remote target branch =
  `已推送並核對`. An unverified commit reference remains `待核對`.
  A SHA, clean worktree, commit URL alone, or cached remote-tracking ref does not
  prove a current remote push. Confirm branch membership, not necessarily that an
  older contribution commit equals the current branch tip. Label student-reported
  status as reported when it has not been independently checked.
- Maintain `PROJECT.md` → `Repository Context` from student-provided or verified
  facts, preserving unknowns. The teacher's template itself need not be a repo.

## Course Contribution Records

All contributions must be recorded in commits made by students. This includes
code, data work, documentation, proposals, and project-context updates. For external
work, students commit a substantive description or index that makes it traceable;
do not claim that this commits the external artifact itself.

Maintain `PROJECT.md` → `Key Contributions` as `Name | Contribution | Commit reference`,
one contribution per row. Require a commit link or SHA whose changes support the
recorded contribution. File links alone do not satisfy this course requirement.
Mark uncommitted work `待提交`, and unverified references `待核對`; neither is a
completed contribution record. Record contributions as work progresses rather than
waiting until the end of the project. A commit is necessary evidence of recording,
not proof of quality, correctness, acceptance, or sole authorship.

After students commit, inspect the supporting changes before replacing a pending
reference with its actual SHA/link; track push verification separately under the
Git workflow above. Students also commit and push the updated contribution index.
An index update references the earlier artifact commit, not its own future hash:
do not create an endless chain of index-only contributions to record each update.
Never substitute an unrelated old commit. Local artifact work may be complete
while student submission and its contribution record remain pending.

## Course Data Handoff

Follow `FINDING-RULES.md` → `資料銜接與檔案驗證` when preparing or using data.
Use the three `templates/data/` directories for their respective notebook/Rmd
documents; data work does not newly require paired HTML. Reuse confirmed student
preferences across stages and valid existing upstream artifacts.

Keep one row per actual data file in `PROJECT.md` → `Data Artifacts`, linking the
exact project-relative data path, its documentation, producing notebook, role,
checks, and SHA-256. Register only actual inspected files; pending/failed work
must not appear ready. Validate serialized processing outputs by reopening them.
Raw-file verification does not certify analysis readiness.

Generated readers bind exact paths and verified hashes before loading, including
separate train/test bindings. Find the nearest project ancestor with `AGENTS.md`
and `templates/`; never choose inputs from glob order or modification time.
Verify schema, unit, keys, and suitability as well as file identity. Existing
externally prepared inputs may be inspected and registered without recreating
unavailable upstream code. Resolve changed versions using authorized context;
ask only when the intended input remains ambiguous. Report affected prior findings
and rerun them only when reanalysis is part of the student's request.

For ongoing raw/processed documentation updates, use
[maintain-data-documentation](skills/maintain-data-documentation/SKILL.md).
For project-context, focus, preference, or contribution-table maintenance, use
[maintain-project-context](skills/maintain-project-context/SKILL.md).
Data skills may update their own verified `Data Artifacts` rows directly.
Keep `Data and Current Focus` as `Field | Details` and `Key Contributions` as
`Name | Contribution | Commit reference`. Every contribution requires a verified
commit reference under `Course Contribution Records`; missing or unverified
references remain pending. These maintenance tasks do not require weekly finalization.

## Course Proposal Workflow

The student must bring an initial idea before AI develops research directions
or a proposal with them. An observation, puzzle, or tentative question in their
own words is enough; a polished question or method is not required. Data alone,
a broad subject label, or "choose a topic for me" does not supply that idea.
Ask what they noticed or want to understand and why, without supplying candidate
topics to choose from. Once an idea is supplied, help clarify it, narrow its
scope, assess feasibility, and develop suitable methods. Follow
`FINDING-RULES.md` → `學生先提出初步想法`; reuse an idea already present in the
conversation or project records rather than asking again.

Default to a writing-coach workflow throughout proposal development, not just at
intake. Ask the students for their reasoning, respond to it, and work through
unresolved choices in small steps before drafting the affected sections. Focus
each round on one or two material questions; do not ask a full questionnaire or
write a complete design and request a token yes/no. Reuse substantive answers
already supplied. When the design is sufficiently established, assemble the
proposal without forcing extra discussion rounds or approval for routine edits.
Follow `FINDING-RULES.md` → `Proposal 採分階段討論` and the proposal skill's
discussion guide. A request for a Demo or delegated work applies only to its
stated scope; permission to demonstrate roles does not decide the whole study.

Use [proposal-writer](skills/proposal-writer/SKILL.md) when a student asks to
write or revise a project proposal. Read the
[proposal template](templates/report/econ-5516-proposal-template.md), retain its
six-section structure, and create the student's Markdown proposal in `report/`.
The template's worked example supplies structure, not project facts.

Use Traditional Chinese with Taiwan terminology and phrasing (zh-TW) by default,
or the student's explicitly chosen language. Ask for a missing research question
when needed; do not ask for an unspecified report language. A Markdown proposal
does not need an R/Python preference. Distinguish
available raw-data samples from proposed schemas and expected results. Unknown
inputs may remain explicitly pending in a useful draft grounded in the student's
idea; a draft request does not replace the need for that initial idea. Finding-specific
processed-only inputs and notebooks are not proposal requirements;
use the matching finding skill only when actual analysis is also requested.

## Global Interpretation Rules

- When information remains uncertain after reading the request, confirmed project
  context, and relevant sources, discuss it with the student before deciding or
  performing dependent work. This includes research definitions, consequential
  processing/model choices, authorship, and roles. Suggestions are proposals until
  the student confirms them or explicitly delegates the decision. Reuse established
  answers and continue independent work; do not ask again about the zh-TW default.
- The course default is 3–4 students per group. This is a default, not a confirmed
  roster or a reason to invent members; use an explicitly supplied actual roster
  even when its size differs. Do not derive PM/DE/DA assignments from group size.
- At student-workflow intake, reuse confirmed names and responsibilities from the
  conversation or `PROJECT.md`/`TEAM.md`. If missing, explicitly ask the student's
  name and the work they actually handle before attributing work or filling author
  and role fields; leaving a placeholder alone is not a substitute for asking.
  At group-project intake, ask for all members' names and confirmed actual work,
  and identify which member is speaking. On later tasks, ask only for missing
  information relevant to that task; do not repeatedly collect the whole roster.
  Do not infer identity or duties from Git authors, computer accounts, filenames,
  template examples, or who supplied a file. Do not automatically make the current
  student the author of pre-existing work. Record confirmed names and actual work
  in `PROJECT.md` → `Team`, one row per confirmed member, using `Role` for the
  supplied role and work description. Placeholder rows do not establish membership.
- Students decide their role assignments. Keep unanswered names and duties pending;
  do not assign PM/DE/DA, invent responsibilities, or overwrite confirmed authors.
  Ask only for missing information and continue independent data inspection or
  discussion while waiting. A draft may retain pending fields after asking, but
  must not present attribution or assignments as confirmed.
  This intake applies to student project work; teacher template maintenance or
  teacher-led format checks retain placeholders without treating the instructor
  as a student whose name and duties must be collected.
- Follow `FINDING-RULES.md` → `不確定的資訊先與學生討論` for the shared discussion
  rule. An explicitly requested draft or format test may retain pending fields,
  but pending fields do not authorize work that depends on unresolved choices.
- Default student-facing explanations and report prose to Traditional Chinese
  with Taiwan terminology and phrasing (zh-TW). Follow an explicitly requested
  language, including a specifically requested English report, instead. Preserve
  formal template field names, code identifiers, paths, and original quotations.
  Do not ask for a language preference when this default applies.
- Treat Markdown as the canonical working memory for research ideas, project
  context, coordination, and decisions.
- When a task concerns a paper, theory, notation, or initializing slides, treat
  the most relevant LaTeX file in `deliverable/paper/` as the formal source of
  current context.
- For slide revision tasks, treat the target Beamer file and its inline comments
  as the main working source. Consult `deliverable/paper/` only when needed for
  notation, factual consistency, or current framing.
- Treat `deliverable/slides/` as a presentation layer derived from the paper,
  findings, or approved project material, not as the main place to develop
  ideas.
- For empirical or software tasks, prioritize the relevant project context,
  source code, data documentation, and current outputs.
- Apply weekly team-management rules only when the project actually uses that
  workflow.
- Prefer local repository evidence over unsupported assumptions.

## Folder and File Meaning

- `PROJECT.md`: project purpose, preferences, scope, current focus, and the
  `Data Artifacts` index linking data, documentation, processing, and verification.
- `TEAM.md`: optional team roster, roles, responsibilities, Git identities,
  capacity, and review areas.
- `ROADMAP.md`: optional priorities, milestones, definitions of done, and
  dependencies.
- `BACKLOG.md`: optional current open backlog derived from finalized internal
  weekly reports when the weekly workflow is used.
- `DECISIONS.md`: optional currently effective decisions derived from finalized
  internal weekly reports.
- `RISKS.md`: optional current open risks derived from finalized internal
  weekly reports.
- `references/`: paper PDFs, source material, and Markdown reading notes.
- `attachments/meetings/`: images used by internal weekly meeting reports.
- `attachments/references/`: images used by paper and reading notes.
- `data/raw/`: source data that should remain unchanged when practical.
- `data/processed/`: cleaned or transformed data.
- `data/temp/`: disposable intermediate data.
- `data/code/`: data-processing and analysis code when the project uses this
  layout.
- `finding/`: empirical results, simulations, figures, and intermediate
  research outputs.
- `report/`: Markdown reports and, when enabled, internal weekly management
  reports named `YYYY-MM-DD-weekly-meeting.md`.
- `deliverable/paper/`: manuscript and formal paper files.
- `deliverable/slides/`: Beamer slides and other presentation artifacts.
- `deliverable/app/`: software or application deliverables.
- `templates/`: all reusable data, finding, report, and weekly meeting
  templates.
- `FINDING-RULES.md`: shared operating rules for data and finding skills.
- `skills/`: task-specific Codex skills.

## Context Priority

Build only the context needed for the task.

### Paper and theory

1. the most relevant file in `deliverable/paper/`;
2. directly relevant files in `references/`;
3. relevant project context or finalized weekly reports;
4. directly relevant files in `finding/`;
5. templates only when creating a new artifact.

### Slides

1. the target file in `deliverable/slides/` and its inline comments when
   revising an existing deck;
2. the most relevant file in `deliverable/paper/` when initializing slides or
   checking notation, facts, or framing;
3. directly relevant findings, approved project material, and style references;
4. templates only when creating a new artifact.

### Empirical, data, and software work

1. `PROJECT.md`, `ROADMAP.md`, and the directly relevant source or deliverable;
2. relevant data documentation and code;
3. directly relevant findings and outputs;
4. the latest finalized weekly report when coordination context matters;
5. references and templates only when needed.

### Weekly progress review

1. the upcoming team-written internal weekly report;
2. the previous finalized weekly report and its `Next Actions`;
3. `PROJECT.md`, `ROADMAP.md`, and `TEAM.md`;
4. new commits and relevant committed diffs since the previous meeting;
5. evidence linked from the report;
6. `BACKLOG.md`, `DECISIONS.md`, and `RISKS.md` when relevant.

Do not read broadly without need.

## Workflow Conventions

- Use structured Markdown so research and project memory remains reusable.
- Use relative links for Markdown images.
- Keep paper-note images in `attachments/references/`.
- Keep weekly-meeting images in `attachments/meetings/`.
- Ask students for missing tool/format preferences before new data or finding
  work. Do not default to R or Python. For report language, use Traditional
  Chinese with Taiwan terminology and phrasing (zh-TW) unless the student has
  explicitly chosen another language. Reuse preferences in chat or `PROJECT.md`;
  do not wait for a language answer when the default applies.
- Match notation to the existing LaTeX draft before adding manuscript text.
- Integrate the current chat into `deliverable/paper/` only when the user
  explicitly asks.
- Before integrating text into the paper, show the proposed LaTeX in chat.
- For literature search, prioritize stronger journals, especially in
  economics, econometrics, statistics, data science, and the user's preferred
  management-science subfields.
- For slides, match the project's established Beamer or presentation style
  when possible.
- For slide revision tasks, treat inline LaTeX comments in
  `deliverable/slides/` as authoritative local instructions.
- For software work, follow the existing stack and repository conventions and
  verify changes in proportion to their risk.

## Optional Weekly Team Workflow

Use this workflow only for projects with weekly team coordination.

### Sources of truth

- Finalized internal weekly reports in `report/` are the history of task
  assignments, decisions, backlog, risks, and unresolved questions.
- The latest finalized internal report's `Next Actions` is the current task and
  assignment snapshot. Unfinished work must be carried forward explicitly.
- `BACKLOG.md`, `DECISIONS.md`, and `RISKS.md` are optional current-state views
  derived only from finalized internal weekly reports.
- `PROJECT.md`, `TEAM.md`, and `ROADMAP.md` are manager-maintained context.
- Git commits are evidence that changes were recorded, not proof of quality,
  completion, effort, acceptance, or sole authorship.

### Internal weekly reports

- Treat each weekly meeting file as an internal management report whose primary
  audience is the project manager.
- Store reports directly under `report/` as
  `YYYY-MM-DD-weekly-meeting.md`.
- Start from `templates/weekly-meeting.md`.
- Team members write their own progress before the meeting.
- Use the project's report-language preference for finalized report prose,
  defaulting to Traditional Chinese with Taiwan terminology and phrasing (zh-TW).
- Preserve these six sections:
  - `Meeting Goals / Agenda`
  - `Key Takeaways`
  - `Consensus and Decisions`
  - `Next Actions`
  - `Backlog & Unresolved Questions`
  - `Other`
- Every previous action must be completed, cancelled, reassigned, or carried
  forward explicitly before finalization.

### Assessment rules

- Evaluate claims against assigned outcomes, definitions of done, committed
  changes, and available evidence.
- Analyze each member's contribution without ranking people.
- Do not use commit counts, lines changed, hours, or message volume as
  productivity scores.
- Distinguish missing evidence from missing work.
- Mark runtime-dependent claims as requiring verification; do not run them
  during the weekly review.
- Recommend one most important next step and label proposed assignments as
  discussion proposals.

## Skill Usage

Use repo-local skills in `skills/` when the task matches:

- `proposal-writer`
- `data-preparation`
- `raw-data-documentation`
- `data-processing`
- `processed-data-documentation`
- `maintain-data-documentation`
- `maintain-project-context`
- `stat-analysis`
- `prediction-model`
- `stata-analysis`
- `external-file`
- `paper-note`
- `paper-search`
- `simulation-runner`
- `beamer-slides`
- `revise-beamer-slides`

Skills provide task-specific rules. This file provides global template-level
rules.

## Output Philosophy

- Help with structuring, critique, synthesis, writing, implementation, and
  continuity.
- Do not over-polish exploratory ideas into false certainty.
- Separate facts, interpretations, recommendations, and approved decisions.
- Be explicit about uncertainty, assumptions, evidence limits, and gaps.
- Prefer concise, reusable outputs over long generic prose.

## Sequential Prompt Protocol

When the user explicitly wants work split across separate prompts:

1. identify the canonical project file that should carry status and context;
2. work on one scoped task at a time unless the user asks to batch;
3. update the relevant status or handoff in that canonical file when
   authorized;
4. use the latest finalized internal report's `Next Actions` for coordinated
   team work;
5. prefer local files over long chat-only context.

No automatic task runner is assumed.
