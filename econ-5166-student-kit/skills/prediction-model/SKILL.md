---
name: prediction-model
description: Use when a student wants a classification or regression prediction task, train/test evaluation, or predictive model comparison in the course finding format, with a selected Jupyter or R Markdown source containing actual results.
---

# Prediction Model

Turn the student's prediction question and prepared data into a reproducible finding using the course's prediction template. Keep training evidence and out-of-sample evidence distinct.

## What to inspect

Read only the context needed for the task:

- the request, explicit preferences, and relevant `Data Artifacts` rows in `PROJECT.md`;
- [shared finding rules](../../FINDING-RULES.md);
- relevant data documentation, split-generation code, existing models, and results;
- the [Jupyter template](../../templates/finding/template-prediction-model.ipynb) or [R Markdown template](../../templates/finding/template-prediction-model.Rmd), according to the student's preference.

Use local project evidence rather than assuming what the target, sample, or available features mean.

## Output targets

Create or revise the selected `.ipynb` or `.Rmd` with actual results under `finding/`; the instructor reviews this source document directly. Use the student's requested name, preserve an existing name, or choose a descriptive basename. No meeting-date naming convention is required. Do not generate HTML by default; export it only when separately and explicitly requested, keeping that export consistent with the source. Missing HTML does not make the selected notebook deliverable incomplete. Follow shared rules for incomplete execution.

Put substantial data preparation and split-generation code in `data/code/`, and saved training/testing inputs in `data/processed/`. Add predictions or figures only as useful supporting outputs. Follow the shared student Git workflow: students create their repository first and perform stage, commit, and push themselves in VS Code. The AI supplies files and a suggested commit message and checks actual commit evidence read-only afterward; uncommitted work remains `待提交`, and a local commit is distinct from verified GitHub delivery.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Discuss uncertain information

Follow [the shared discussion rule](../../FINDING-RULES.md#不確定的資訊先與學生討論). Discuss an uncertain target, prediction time, predictors, split design, threshold, or model specification before using it; do not decide from the available columns alone. Reuse confirmed context and explicit delegation; continue independent work while waiting. Students fill role assignments themselves; never invent people or responsibilities. A requested draft may keep unresolved fields pending, but does not authorize dependent decisions.

## Workflow

1. Reuse explicit choices and apply the report-language default above. Ask for any missing tool/format preference (Python/Jupyter or R/R Markdown); while awaiting that required answer, inspect inputs read-only without writing deliverables or running analysis.
2. Confirm the target, prediction time, available predictors, observation unit, author, and intended evaluation. Keep `Created At` as the actual fixed creation date. Never guess the target from the final column.
3. Select and verify the exact training/testing files using the data-binding rules below. Read their linked documentation and inspect split-generation code when needed to establish their roles, samples, and lineage. If only one dataset exists, create and document an appropriate split upstream, then save and register the resulting inputs under `data/processed/`. Use [data preparation](../data-preparation/SKILL.md) when necessary and carry preferences forward; reuse suitable existing splits.
4. Start from the selected template. After loading and previewing both datasets, summarize all analysis variables separately for training and testing data. Then specify the model, fit it using training data, and perform tuning within the training sample if needed.
5. Evaluate training and held-out testing performance in separate blocks using the required metrics and plots below. Inspect real outputs, then backfill the background findings.
6. Execute the `.ipynb` from a clean kernel and retain actual cell outputs. For `.Rmd`, execute its chunks in a clean R session, for example with `knitr::knit` to temporary Markdown output; inspect actual tables and figures, then put verified results and figure references into the `.Rmd` for direct inspection. Preserve referenced figure assets. Verify structure, data separation, portability, visible results, and execution status in the selected document. Export and inspect HTML only when separately and explicitly requested. Mark failed or partial execution honestly; missing HTML alone is not an incomplete delivery.

## Template contract

Preserve this order:

1. `Background`: `Author`, `Created At`, `Path to Training Data`, `Path to Testing Data`, `Model Specification` with `Method`, `Variables`, `Tuning Parameters`, `Optimization Method`; `Main Findings and Takeaways` with `In-sample <metric>` and `Out-sample <metric>`; `Future Direction`.
2. Load packages.
3. Load training data, do limited manipulation, and print the first ten observations.
4. Load testing data, do limited manipulation, and print the first ten observations.
5. Add descriptive statistics for training and testing data, before modeling.
6. Keep `The actual modeling starts below`.
7. Describe method, target and predictors, hyperparameters, and optimization.
8. Fit/evaluate models, then report training performance and testing performance in **separate blocks**.

Replace `<metric>` with actual metric names. Keep nonapplicable specification fields with an explanation rather than deleting them.

## Data binding

Follow `資料銜接與檔案驗證` in [shared finding rules](../../FINDING-RULES.md). Verify training and testing as separate input roles before fitting or evaluating anything.

- Select the student's explicitly identified files, or `PROJECT.md` → `Data Artifacts` rows whose roles and samples match the prediction task. Read each file's linked documentation; never infer train/test identity from modification time or the first glob match. If role or version is ambiguous, ask before proceeding. Do not swap roles or use one file for both merely to make the code run.
- For each role, resolve its exact project-relative file under `data/processed/` and verify existence, schema, required predictors, observation unit, and documented key/uniqueness expectations. Verify the training target; for an intentionally unlabeled test set, document the missing target and apply the existing unavailable-metric rules. Check split overlap and independence against the documented split unit, such as entity or entity-time, rather than assuming all repeated entity IDs are invalid.
- Compute SHA-256 from each actual file and compare it with its registered verified hash. If a clearly identified, suitable processed file has no row or hash, verify and register its exact data path, documentation, processing notebook, role, verification status, and actual hash. Use [processed-data-documentation](../processed-data-documentation/SKILL.md) when needed. Externally prepared files may name their producing notebook `not available`; a missing producer is not itself a reason to recreate a valid split.
- On a hash mismatch, establish whether the authorized task produced or requested a new data version. Reverify an evidenced replacement, then update its index and the current analysis's bindings. Do not simply replace the expected hash, pick a different file, or continue with an unresolved version; ask when intent cannot be established.
- Bind each role in generated code to its exact verified project-relative path and expected SHA-256. Resolve the project root portably; check existence and bytes before loading, then check the needed schema and split assumptions. Fail clearly if an input changes or disappears. The template's `Path to Training Data` and `Path to Testing Data` must match the actual read paths, with links to the corresponding documentation; each path/hash must remain attached to its verified role.
- These identity and schema checks do not authorize using held-out outcomes to tune preprocessing, features, thresholds, or models. Preserve the training-only fitting rules below.
- When inputs change, identify existing findings known to bind to the previous path/hash. Reexecute and refresh their selected notebooks only if the requested work includes reanalysis, refreshing an HTML export only if explicitly requested; otherwise identify the affected findings as still using the earlier data. An updated data index is not evidence that their scores or result documents were regenerated.

## Descriptive statistics

- Cover the target, predictors, and other variables used in the analysis, including applicable derived, filtering, and grouping variables. Classify numeric-coded categories by meaning, not storage type.
- For each continuous variable, report `mean`, `min`, `q25`, `q50`, `q75`, `max`, `sd`, and `N` (`#obs`, nonmissing observations).
- For each categorical variable, report the top ten categories with counts and percentages. State the denominator and missing-value treatment; show all categories when fewer than ten exist.
- Label training and testing summaries separately with sample sizes and readable variable names. If test outcomes are unavailable, summarize available test predictors and explain the missing outcome summary. Do not create labels or use test distributions to choose features, thresholds, or models.

## Required performance evidence

Apply these requirements separately to the training and testing blocks. State the evaluation sample size and units, then explain what each table or figure shows.

- **Continuous target:** report both MSE and MAE; RMSE or other metrics may supplement them. Include a prediction-distribution plot, a predicted-versus-actual scatterplot, and a predicted-versus-prediction-error scatterplot. Define the error consistently, for example `actual - predicted`, and label the axes accordingly.
- **Binary target:** report Recall, Accuracy, AUC, and F1-Score, plus a labeled confusion matrix. Specify the positive class and decision threshold. Compute AUC from continuous scores oriented toward the positive class, not thresholded class labels. Select thresholds using training/validation data only.
- Explain undefined metrics, such as AUC with a single observed class, or recall with no positive outcomes. Report them as unavailable with a reason; do not invent values or silently substitute zero. With no test outcomes, provide test predictions and any feasible prediction-distribution plot, and explicitly mark label-dependent metrics and figures unavailable.
- For multiclass or other prediction tasks, explain how the binary/continuous requirements apply or need extension. Document the averaging method, score definitions, and appropriate metrics rather than applying binary metrics blindly.
- Follow the shared figure, table, and applicable regression-reporting rules. Keep model prediction distributions distinct from confidence intervals for estimated quantities; do not attach arbitrary intervals to individual predictions.

## Writing and coding rules

These reliability rules guide implementation; they are not extra source-template fields.

- Both train and test inputs come from this project's `data/processed/`. Preserve existing splits unless changing them is part of the task. Major merges, reshaping, and cleaning belong upstream.
- Account for time ordering or repeated entities when splitting; do not blindly random-split dependent observations. Document split units, sizes, dates or proportions, seed, and any overlap checks possible with available keys.
- Use only information available at prediction time. Keep test outcomes out of feature selection, hyperparameter tuning, threshold selection, and model choice.
- Fit imputation, scaling, encoding, dimension reduction, and feature selection **only on training data**; within cross-validation, fit them separately on each training fold. Apply learned transformations to validation/test data. A train-fitted preprocessing pipeline is part of model estimation, not a reason to preprocess the full sample upstream.
- Distinguish deterministic source-data corrections from learned transformations. Saving a file under `data/processed/` does not make full-sample preprocessing safe.
- Include the required metrics above and any additional metrics requested by the student. Compare with a simple baseline when useful.
- With an unlabeled test set, produce predictions but mark test metrics as unavailable without true labels. Never report training or cross-validation scores as independent test performance.
- If the sample cannot support a credible holdout, explain the proposed validation approach and the absence of independent testing instead of manufacturing an out-of-sample score.
- Use observed results only. Follow shared rules for incomplete execution and do not silently switch the student's chosen programming language.

## Good output standard

A reader should be able to identify the prediction question, data split, variable summaries, model and tuning procedure, actual training and testing metrics, and limitations. Evidence should show that test data did not influence fitting or selection. The selected `.ipynb` or `.Rmd`, actual outputs, figures, and written findings should agree. HTML is an explicitly requested optional export, not a completion requirement.

## Example prompt patterns

- Here are my train and test files; create a prediction finding in the course format.
- Use R Markdown and English to predict sales and compare out-of-sample errors.
- My test file has no labels; generate predictions and document which performance measures cannot be computed.
