---
name: stat-analysis
description: Use when a student wants descriptive statistics, graphs, hypothesis tests, or regression in the course finding format, delivered as the selected Jupyter or R Markdown notebook with actual results. Use the prediction skill for train/test evaluation and simulation-runner for generated-data experiments.
---

# Statistical Analysis

Turn the student's research question and data into a reproducible finding using the course's statistical-analysis template. The goal is a readable research artifact with evidence, not just a code file.

## What to inspect

Read only what the current task needs:

- the student's request, explicit preferences, and relevant `Data Artifacts` rows in `PROJECT.md`;
- [shared finding rules](../../FINDING-RULES.md);
- relevant input documentation, processing code, and existing findings;
- the [Jupyter template](../../templates/finding/template-stat-analysis.ipynb) or [R Markdown template](../../templates/finding/template-stat-analysis.Rmd), after the student chooses the format;
- a relevant paper draft or research note only when needed for the question, notation, or interpretation.

Treat Markdown as working context and the selected template as the output contract. Do not read every research skill or assume a paper draft exists.

## Output targets

Create or revise the student's chosen `.ipynb` or `.Rmd` in `finding/`; the instructor reviews this source document directly. Use the student's requested filename, preserve an existing filename, or choose a descriptive basename, such as `wage_analysis.ipynb` or `wage_analysis.Rmd`. A standalone `.R`, `.py`, `.md`, or chat answer does not satisfy this finding deliverable. Do not generate HTML by default; export it only when separately and explicitly requested. Missing HTML does not make the selected notebook deliverable incomplete.

Keep the finding's code, actual results, explanations, and supporting figures consistent when revising it. If HTML is explicitly requested, check that export against the source. Keep supporting figures under a related local asset folder if needed. Follow the shared rules for portable paths, execution status, and the course's GitHub handoff requirement. Students first create their own repository and perform stage, commit, and push themselves in VS Code; the AI prepares files and a suggested commit message, then checks status and actual references read-only after the student acts. Keep uncommitted work `待提交`, and distinguish a local commit from verified GitHub delivery.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Discuss unresolved research definitions, sample rules, and consequential model or standard-error choices before fitting; a recommendation is not a confirmed student choice. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

1. Reuse explicit choices and apply the report-language default above. Ask for any missing tool/format preference (Python/Jupyter or R/R Markdown); while awaiting that required answer, inspect inputs read-only without creating deliverables or running analysis.
2. Identify the research question, variables, observation unit, author, and intended method. If only data were supplied, ask the intended question rather than guessing an outcome.
3. Select and verify the exact prepared inputs using the data-binding rules below. Read their linked documentation and inspect the producing notebook when needed to resolve sample, variable, or lineage questions. Use [data preparation](../data-preparation/SKILL.md) for substantial cleaning, carrying forward the student's preferences; already suitable processed files do not need to be rebuilt.
4. Start from the chosen template and implement the analysis in its required order.
5. Execute the `.ipynb` in order from a clean kernel and retain actual cell outputs. For `.Rmd`, execute its chunks in a clean R session, for example with `knitr::knit` to temporary Markdown output. Inspect actual tables and figures, then put verified results and figure references into the `.Rmd` so the instructor can inspect it directly. Preserve referenced figure assets. Follow the requested execution scope and the figure, table, and regression rules below.
6. Fill the background takeaways from the verified outputs and explain the results and limitations in the resolved report language. Export HTML only if separately and explicitly requested.
7. Inspect the selected `.ipynb` or `.Rmd`, its actual outputs, and figures for complete results, readable labels, and agreement with the takeaways. Deliver its path with the actual execution status and GitHub handoff status. If execution is blocked, identify the blocker and label the document unexecuted or partial; do not invent results. Report an export problem only when that export was explicitly requested, and do not treat absent HTML as a default completion failure.

## Template contract

Preserve this order:

1. `Background`: `Author`, `Created At`, `Research Motivation and Context (why are we interested in the findings?)`, `Main Findings and Takeaways`, `Future Direction`. Within the motivation/context field, identify the exact project-relative processed input path and link its documentation; preserve the existing field order.
2. Load packages.
3. Read processed data, apply only simple filtering or a small number of derived variables, and print the first ten observations (all rows if fewer).
4. Before formal analysis, report summary statistics for **every variable actually used**, including outcome, predictors, controls, groups, and weights when applicable.
5. Keep `The actual analysis starts below`, then add the appropriate graphs, tests, models, and interpretations using the template's analysis guidance. Include code and explanatory text for the analyses actually needed; unused graph, comparison, or regression prompts are not new required analyses.

Required summary statistics:

- Numeric variables: mean, min, 25th percentile, median, 75th percentile, max, standard deviation, and number of observations.
- Categorical variables: number of observations and counts/percentages for the ten most frequent categories, or all categories if fewer.

## Data binding

Follow `資料銜接與檔案驗證` in [shared finding rules](../../FINDING-RULES.md). This is a data handoff check, not a requirement to repeat upstream preparation.

- Use the student's explicitly identified dataset, or a `PROJECT.md` → `Data Artifacts` row whose sample, variables, and role match the research question. Inspect the row's data file and linked documentation. Do not select the newest file or the first CSV returned by a glob. If several candidates remain materially plausible, ask which sample/version the student intends before analysis.
- Resolve the exact file under this project's `data/processed/`. Check existence, schema, required columns, observation unit, documented key/uniqueness expectations, and applicable sample role. Compute SHA-256 from the actual file bytes and compare it with the registered verified hash. A matching hash establishes file identity; documentation and schema checks establish suitability.
- If the student clearly identified a usable prepared file but its index row or hash is missing, verify the file and record its exact path, documentation, role, verification status, and actual hash in `Data Artifacts`. Use [processed-data-documentation](../processed-data-documentation/SKILL.md) when documentation needs completion. An externally prepared dataset may record its processing notebook as `not available`; do not invent upstream code or require unnecessary cleaning just to fill that field.
- If a registered hash differs, do not silently replace the expected hash or switch inputs. Determine whether the current authorized task produced or requested a new version; when supported by the provenance, reverify it and update the index and this analysis's bindings. Ask only when the intended version cannot be established. Do not continue analysis against an unresolved mismatch.
- In the generated notebook, bind each input to its verified exact project-relative path and expected SHA-256. Resolve the project root portably, check existence and hash before loading, then validate the needed schema/key assumptions before analysis. Fail clearly on missing files, changed bytes, or incompatible structure; never fall back to another file. The documented input path and the read statement must refer to the same file.
- A changed dataset can make prior findings stale. Identify existing findings known to use the previous path/hash. Update and rerun their selected notebook only when reanalysis is part of the student's task, refreshing an HTML export only if explicitly requested; otherwise report which existing findings still use the earlier data and need reanalysis. Updating `PROJECT.md` alone does not update their results.

## Figures, tables, and regression results

Apply the instructor's requirements summarized in [shared finding rules](../../FINDING-RULES.md):

- Give every figure a title, readable variable names, labeled x/y axes, and informative legend labels when a legend is needed. Replace raw names such as `click_rate` with meaningful display labels. Prevent overlapping text; use transparency, binning, or another suitable display when scatter points heavily overlap. Plot 95% confidence intervals for estimated quantities such as means. The accompanying text must explain what is plotted, the sample, the question, and the observed finding.
- Give every table a title, sample size, and readable variable labels. For two-group comparisons, report each group's mean and standard deviation, the mean difference with its direction, and the t-test p-value; explain the test's assumptions and any design limitations. Explain the sample, findings, and complex or judgment-dependent definitions.
- For regression, report the outcome mean computed on each model's actual estimation sample, alongside N. Default to heteroskedasticity-robust standard errors such as HC1; use cluster-robust errors when warranted by the sampling, assignment, or dependence structure, and identify the cluster variable and number of clusters. State the standard-error method and sample in the text.
- Name the omitted/reference group for categorical regressors. State which fixed effects are controlled for without printing every fixed-effect coefficient. Explain the specification, assumptions, and any complex variable definitions.
- Use `* p < .10`, `** p < .05`, and `*** p < .01`, consistent with the instructor's `0.90*`, `0.95**`, `0.99***` confidence-level notation. Define the stars explicitly and report p-values when useful. Regression estimates shown in figures also require 95% confidence intervals.

## Writing and coding rules

- Preserve the template's fields and sequence; do not substitute a generic essay or code-only answer.
- Data must be read from this project's `data/processed/`. Document sample exclusions and missing-value handling; put substantial preparation in `data/code/`.
- Classify variables by meaning, not just storage dtype: numeric category codes may need categorical summaries.
- State the effective numeric N and missing N. For categorical percentages, use all nonmissing observations as the denominator and report missingness separately unless the assignment specifies another convention; never use only the top-ten subtotal as the denominator.
- Use the student's method when specified. Otherwise choose a defensible approach for the confirmed question and state assumptions. Explain departures from the default standard-error choice when a different method is needed.
- Distinguish association from causation. Do not invent significance or interpret expected results as observed findings.
- Follow shared rules for unexecuted or partially executed work; unavailable dependencies do not authorize silently changing the student's programming language.

## Good output standard

A reader should be able to identify the question, data source, analysis sample, variable summaries, model, actual evidence, and limitations without reconstructing the conversation. All numerical claims should agree with the outputs. A completed delivery is the selected `.ipynb` or `.Rmd`, verified from a clean session with readable actual results and consistent figure assets. HTML is an explicitly requested optional export.

## Example prompt patterns

- Here is my cleaned data; help me produce a statistical finding in the course format.
- Use Python/Jupyter and Traditional Chinese to study the relationship between education and wages.
- Revise this R Markdown analysis to match the finding template and explain the regression output.
