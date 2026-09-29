---
name: proposal-writer
description: Coach students through discussion, drafting, and revision of a six-section course proposal from their own idea. Elicit reasoning and resolve research choices in small steps, then write supported sections and assemble Markdown in report/. Do not turn a topic alone into a fully invented proposal.
---

# Proposal Writer

Help students develop and express their own research design through discussion.
Turn the resulting choices and available evidence into a proposal following the
course template. Keep the students involved in the reasoning as sections take
shape, rather than only asking for a topic before writing the entire proposal.

## What to inspect

Read only what the current task needs:

- the student's request, notes, and explicit preferences in `PROJECT.md`;
- the [proposal template](../../templates/report/econ-5516-proposal-template.md),
  including its section order and relevant example images;
- an existing proposal in `report/` when revising it;
- an existing `TEAM.md` or supplied team notes when needed to establish roles;
- supplied source descriptions, data documentation, and a few actual data rows
  when available;
- relevant findings or references only when they support the proposed question,
  method, or a claim already made by the group.

The template is a worked example. Its Oscar topic, names, dates, author metadata,
model, data values, and images are not the student's project. Preserve the
structure while replacing example content with the student's own material.

## Output targets

Develop supported sections incrementally and assemble a substantive Markdown
proposal in `report/`, such as `report/proposal.md`, once its research choices
have adequate student input. A discussion-only request need not create a file.
Use a requested or existing filename when provided; otherwise choose a descriptive
name. No meeting-date prefix is required. Do not overwrite the reusable template.

Keep any project-specific images in `report/assets/<proposal-basename>/` and link
to them relatively from the proposal. Reuse existing project evidence when
appropriate; do not copy the example's formula or screenshot into a new project.

A proposal uses Markdown by default. It does not require a notebook or Google
Doc; export HTML only when separately and explicitly requested. Honor an
explicitly requested alternative format while preserving
the proposal structure. A request for an outline or a particular section should
receive that scoped result rather than an unsolicited full proposal.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Require the student's starting idea

Follow [學生先提出初步想法](../../FINDING-RULES.md#學生先提出初步想法).
Reuse a student-supplied observation, puzzle, or tentative question from the
conversation or project files. They need not have a polished title or method.
Data alone, a broad subject label, or a request to invent a topic is insufficient.

With no initial idea, ask an open question such as: 「你注意到什麼現象？你想弄清楚
什麼，為什麼？」Do not offer a topic menu, choose a dependent variable, or write
motivation, hypotheses, or a substantive proposal for the student. Explaining the
template or inspecting data structure remains possible; an incomplete-draft
request does not authorize inventing the missing idea.

Once they supply an idea, help sharpen it, assess data feasibility, compare
methods, and suggest formulations tied to that idea. Keep suggestions distinct
from the student's confirmed decisions.

## Workflow

1. For student project work, reuse confirmed names and responsibilities from the
   conversation and project records. Groups default to 3–4 students; use the
   supplied actual roster and do not invent members to match that default.
   At group-project intake, ask for each member's name and confirmed actual work
   and identify which member is speaking. Later requests only need missing
   information relevant to the task; do not collect the same roster again.
   Bundle this with the initial-idea question when both are missing. Do not infer
   identities or duties from accounts, commits, supplied files, or template names.
   Leaving pending fields does not replace asking. Record confirmed names and
   work in `PROJECT.md` → `Team`; preserve established authorship on existing work.
   Unanswered fields can remain pending in an authorized draft while independent
   work continues; group size does not assign PM/DE/DA or establish responsibilities.
   Teacher template maintenance or format-only checks keep placeholders without
   collecting the instructor's identity as though they were a student.
   Reuse confirmed preferences and apply the report-language default above. Ask
   about format only if the student wants an alternative to the Markdown template
   and the choice remains unclear. Do not ask for R or Python merely to write a
   proposal. While awaiting research-input answers, continue work that does not
   depend on them; do not decide the unresolved parts for the student. Record explicit language answers in the
   `Student Preferences` section of `PROJECT.md` without replacing an existing
   analysis-tool preference; do not record the teacher default as a student answer.
2. Establish the student's starting idea and identify the next unresolved choice.
   Reuse their notes and previously confirmed reasoning. Use the discussion guide
   below to ask one or two material questions at a time, rather than delivering a
   full design questionnaire. Let the student answer before resolving dependent
   choices or drafting later sections; do not answer your own questions for them.
3. Respond to the student's answer: briefly restate the idea, identify a concrete
   strength or gap, and help them examine the evidence or alternatives. Ask them
   to explain the choice in their own words when the reasoning remains unclear.
   Inspect actual data samples as relevant; a proposal may preview `data/raw/`.
   Keep available evidence, AI suggestions, and confirmed decisions distinct.
4. Draft the paragraph or section supported by this discussion. Preserve the
   student's meaning and leave unresolved design choices pending. Keep a concise
   note in `PROJECT.md` about confirmed choices, the current discussion stage,
   and the next unresolved question when these change; a wording-only edit does
   not require a new discussion note. When the needed design and evidence are
   established, assemble the six sections below. Substantial supplied notes can
   already satisfy this condition; do not force extra rounds or ask permission
   for ordinary wording edits. A request for an incomplete draft can preserve
   pending sections, but does not authorize inventing research decisions.
5. When revising, preserve the group's choices, useful prose, evidence, and
   comments. Resolve changes against supplied information; flag conflicting
   sources or dates rather than silently selecting one. Keep suggestions distinct
   from decisions the group has already made.
6. Check the proposal against the actual template and inputs. Verify the section
   sequence, evidence links, data examples, and agreement between the proposed
   data and method. Deliver the file path and the few unresolved inputs that
   materially affect its readiness.

## Discussion guide

Follow [Proposal 採分階段討論](../../FINDING-RULES.md#proposal-採分階段討論).
Use the following as coverage guidance, not a fixed interview that must be repeated.
Move to the student's current unresolved issue and keep each turn small.

| Area | Elicit from students before writing the affected content |
| --- | --- |
| Question and motivation | What they noticed, what they want to learn, why it matters, and what they mean by the central outcome. Help refine their own question. |
| Data and scope | What is actually available, who/what each row represents, and why the proposed place, period, and variables fit the question. Inspect evidence together; do not declare a source obtainable without checking it. |
| Method and hypothesis | What comparison would answer their question, what pattern they anticipate and why, and what alternative explanations matter. Explain a method when needed, then ask students to connect it to their design. |
| Limitations and responsibilities | Which data or design weakness worries them, how it limits interpretation, and which work members have actually agreed to handle. Do not invent assignments. |
| Assembly and review | Whether question, variables, comparison, and interpretation agree. Clarify unresolved substantive points, then assemble the supported sections and report the actual draft status. |

Offer brief explanations or a small number of alternatives grounded in the
student's idea when they need help. Do not prewrite all choices and ask only
"Is this okay?" A student's own reasoned answer or clear prior instructions may
establish the choice; a formal approval ceremony is not required.

If the instructor explicitly requests a Demo or delegated work, apply it only to
that scope and label the demonstration assumptions. Permission to demonstrate
role assignments is not permission to decide the entire study or write all six
sections. Do not treat a previous AI-generated Demo as the group's confirmed
reasoning, or as continuing authorization to take over later student work.

## Template structure

Start with the project title, group identifier, and member names/student IDs when
provided. Keep unknown identity fields marked as pending. Do not reuse the source
template's author or creation date as the student's metadata.

Preserve these six sections and their order. Translate headings consistently when
the student chooses another language, retaining the same meaning.

1. **專案敘述：研究問題、動機與研究方法（組員共同討論，PM 彙整）**
   - Keep the four subsections: **研究問題**, **研究動機**, **資料來源**,
     and **研究方法**.
   - State the question and motivation, identify intended sources and their
     availability, and explain the proposed design. Describe relevant planned
     summaries, figures, or models; use an equation only when it clarifies the
     chosen method. Do not make OLS or a causal design mandatory.
2. **已有之 raw data**
   - Show a few actual available observations or a legible supplied screenshot,
     with a source/file link and enough context to understand them. This section
     establishes whether the key data can be obtained; the template assigns the
     DE responsibility for supplying these samples.
   - If no data have been obtained, say so and identify the needed acquisition
     step. A planned source or schema is not evidence of successful collection.
     Place hypothetical data-format examples in section 3, clearly labeled.
3. **主要分析用資料需求（組員共同討論，DA 負責撰寫，DE 確認可執行）**
   - Describe the required observation unit, sample period, scope, and final
     formatted data in a table suited to the student's project. Explain the
     variable definitions and preparation needed to make the design feasible;
     specify units, coding, or matching keys where material.
   - Distinguish verified fields from proposed fields. Label schematic rows as
     hypothetical. Mark feasibility as pending until supported by the available
     evidence or the DE's confirmation.
4. **假說與預期主要結果（組員共同討論，DA 負責撰寫）**
   - Explain the hypothesis, reasoning, and anticipated patterns. Label imagined
     plots, tables, and coefficients as illustrative, never as observed results.
   - For a data-application project, include a UI schematic tied to the proposed
     users, inputs, and outputs. A simple wireframe is sufficient; building or
     deploying the app is a separate task.
5. **預期限制（組員共同討論，DA 負責撰寫）**
   - Discuss limitations relevant to this design, such as unavailable data,
     measurement, sample selection, or endogeneity. Explain their implications;
     avoid filling the section with an unrelated generic checklist.
6. **角色分工表：請列出組員之分工（PM 彙整）**
   - Keep Project manager, Data engineer, and Data analyst role entries. Students
     must fill in or explicitly confirm their assignments and responsibilities;
     ask them when this information is missing. Only organize content they have
     supplied or confirmed. Do not assign people or invent assumed duties, even
     as proposed assignments. Until answered, leave each role as
     `待學生填寫` (or its equivalent in the chosen report language). An authorized
     draft or teacher's format check may retain these pending fields without
     inventing a team.

## Writing rules

- Use the resolved report language and distinguish plans, hypotheses, and
  observed evidence. Do not manufacture data access, sample rows, citations,
  coefficients, significance, team decisions, or DE approval.
- Preserve the template's role labels and responsibility wording in its headings;
  they do not authorize filling the student's role table with assumed duties.
  Do not claim that collaboration, assignment, or approval has already occurred.
- Explain whether a design targets description, association, prediction, or a
  causal effect. State assumptions needed for the intended interpretation.
- A proposal request alone does not call for executing statistical models,
  cleaning datasets, or building an application. If the student also requests
  actual analysis, use the relevant finding skill and carry forward confirmed
  preferences; ask only for missing analysis choices.
- Keep finding-specific notebook, summary-statistic, and regression-output
  requirements with the actual analysis. Statistical and prediction findings use
  the selected Rmd/ipynb; HTML is only an explicitly requested export. Do not add
  those analysis requirements to the proposal.
- When an incomplete draft or teacher's format check is authorized, retain useful
  content with explicit pending items. Describe it as a draft rather than a
  complete, verified proposal; this exception does not authorize invented facts
  or role assignments.
- Creating the local proposal does not automatically publish a Google Doc,
  assign tasks, or finalize weekly records. Continue those additional actions
  only within the student's requested scope. Follow the shared Git workflow:
  students first create their own repository and perform stage, commit, and push
  themselves in VS Code. Supply a suggested commit message and check the actual
  status and supporting commit read-only after they act; a general completion
  request or earlier Git authorization does not authorize AI submission.

## Good output standard

A reader can understand what the group will investigate, why it matters, which
data are available and still needed, how the design addresses the question, what
patterns are hypothesized, what could limit interpretation, and who is responsible.
The six sections follow the template, project-specific claims have support, and
missing inputs are visible without requiring the reader to reconstruct the chat.

## Example prompt patterns

- Use these research notes and data samples to write our proposal in Traditional Chinese.
- Draft an English project proposal about bus access and employment using the course template.
- Update section 3 of our existing proposal with this new data dictionary.
- We have an application idea but no downloaded data yet; help us prepare a proposal draft.
