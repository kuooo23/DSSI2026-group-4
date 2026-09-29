---
name: simulation-runner
description: Use when the user wants help designing, running, inspecting, or summarizing a simulation or numerical experiment, including producing a Python/Jupyter or R/Rmd finding in the ECON 5166 simulation format.
---

# Simulation Runner

Use this skill when the user is doing simulation-based research or wants help with a numerical experiment.

The goal is to design a useful simulation, keep assumptions and parameter choices explicit, and explain what the numerical results do and do not show. Use the course simulation template when creating a finding notebook.

The instructor's supplied text contains no separate simulation delivery section. Follow the original simulation template and the student's preferences; the selected Rmd/ipynb is the document for direct review, with HTML exported only when separately and explicitly requested. The simulation structure and example metrics below come from the supplied template, while reproducibility guidance supports implementation rather than adding instructor-required fields.

## What to inspect

First read [FINDING-RULES.md](../../FINDING-RULES.md), then inspect only the files needed for the task:

- the student's simulation question, DGP, supplied code, or existing results in `finding/`
- relevant Markdown research notes and project context, including `PROJECT.md` or `ROADMAP.md` when needed
- the most relevant theory note or LaTeX draft in `deliverable/paper/`, when the simulation concerns a paper or theoretical claim
- the selected simulation template when creating or reformatting a notebook

Treat Markdown as working research memory. Treat the relevant LaTeX draft as the formal source of current theory, motivation, and notation. Do not assume every project has a paper or needs every workflow.

## Output targets

Depending on the user's request, produce:

- a Python/Jupyter notebook (`.ipynb`) or R Markdown notebook (`.Rmd`) in `finding/`, following the selected course template
- revisions to existing simulation code or findings
- a plain-language explanation of the design, results, limitations, or proposed checks

A request to inspect results or discuss a design does not require creating a notebook or a new automation layer.

Use the student's requested or existing filename; otherwise choose a descriptive basename. A meeting date is not required for naming. Record the actual creation date in `Created At` independently of the filename. Do not generate HTML by default; export it only when separately and explicitly requested. Missing HTML is not an incomplete simulation delivery. Keep any explicitly requested export consistent with the source notebook.

For narrative text, follow the student's explicit report-language choice in chat
or `PROJECT.md`; otherwise use the teacher default: Traditional Chinese as used
in Taiwan (`zh-TW`), with Taiwan-local terminology and phrasing. Do not ask for a
language choice or delay work when none is specified. If recorded, label this as
a teacher default, not an explicit student answer. Retain the template's original
field names.

## Workflow

When helping with a simulation:

1. Reuse explicit choices and apply the report-language default above. Ask only for a missing Python/Jupyter or R/Rmd preference; do not ask again for a choice already given. Never default to R. Until that required format answer arrives, only read materials: do not create formal documents or run simulations.
2. Clarify the research question, theoretical mechanism, target quantity, and minimum design needed to answer it.
3. Identify the DGP, parameter values, estimator or test, performance measures, replication count, sample sizes, and parameter grid. Distinguish supplied settings from proposed assumptions.
4. If missing DGP details, true values, error distributions, or null hypotheses determine the meaning of the experiment, obtain that information before treating the design as settled. When the student authorizes you to design the experiment, choose reasonable settings and label them as design assumptions.
5. For a new notebook, read and use the [Python template](../../templates/finding/template-simulation.ipynb) or [R template](../../templates/finding/template-simulation.Rmd) matching the confirmed preference.
6. Implement or revise the simulation within the requested scope, keeping DGP parameters and tuning choices explicit.
7. Run it when the task calls for execution and the environment supports it; inspect outputs and identify the main patterns. Use a clean kernel and retain outputs for `.ipynb`. For `.Rmd`, run chunks in clean R, for example with `knitr::knit` to temporary Markdown, inspect the output, and backfill verified results and figure references in the source without requiring HTML. Distinguish a small trial run from the full requested experiment.
8. Fill the results summary and takeaways from actual evidence, then explain limitations and useful next steps. Validate the notebook within the requested scope and state its actual execution status. If an HTML export is explicitly requested, produce and inspect it for matching results; otherwise complete the selected notebook without HTML.

## Template contract

Preserve the following content and order in a course simulation notebook.

**Background** contains these fields in order:

- Author
- Created At (`YYYY-MM-DD`)
- Model Specification
  - Method
  - Tuning Parameters
  - Optimization Method
- Main Findings and Takeaways
- Future Direction

Use an explicit pending value for an unknown author. Explain when tuning or optimization is not applicable. Do not fill findings with anticipated results.

**Results overview**, immediately after Background, presents graphs or tables showing how performance changes with sample size and parameter values. The source template gives estimator MSE and test size/power as examples; select relevant metrics rather than requiring all of them. Mark this overview pending when the simulation has not run.

**Code and analysis blocks** then follow this order:

1. Load packages.
2. Declare the DGP settings: Number of simulation, Sample size, Main parameter of interests, and Other parameters. Keep the grid and seed settings here as well.
3. Define a data-generation function accepting those parameters. End the block by generating data, with the seed set immediately before generation as the template requests.
4. Describe the model specification: method, variables, hyperparameters, and optimization method.
5. Define the estimator or test as a function taking data as input. Declare tuning defaults before the function and expose them as function arguments.
6. Use the template's open computation blocks for the grid and replications.
7. Report performance metrics for each scenario, then use these results to populate the earlier overview and Background.

Keep Python code in Python kernel cells and R code in R chunks. Retain the Rmd YAML and setup structure, updating document metadata to match the actual work.

## Writing and coding rules

The template contract above reflects the course format. The following rules support reliable implementation and interpretation; they are not additional fields in the original template.

- Prefer the simplest design that answers the research question. Make assumptions, true values, tuning choices, and computational limits explicit.
- Compare sample sizes and values of the parameters of interest. If the student restricts the scope to one scenario, honor it and explain that cross-scenario comparisons remain unavailable.
- A simulation normally generates data from its DGP; the simulation template does not impose the empirical notebooks' `data/processed`-only input rule. If observed data calibrate the DGP, record the source and calibration method.
- Use a recorded seed immediately before the initial generation. For formal replications, use an advancing RNG state or reproducible independent random streams. Do not reset the same seed inside every replication and accidentally generate identical samples. Allocate distinct streams when running in parallel.
- Keep demonstration generation and formal simulation reproducible; separate recorded seeds may be used for them. Record scenario, replication, estimate or test result, and execution status sufficiently to recompute summaries.
- Report requested, attempted, successful, and failed replications by scenario, with failure reasons. State each metric's denominator. If metrics use successful fits only, say so and also report the failure fraction; do not silently discard failures.
- Compute estimator metrics against the stated true value. Compute size under the null and power under the alternative, and state the test level. Include Monte Carlo uncertainty when it matters for interpreting differences.
- Label outputs as not executed, partially executed, or fully executed. Keep actual errors and resource limitations visible; trial-run results must not stand in for a completed grid.
- Existing result files are evidence to inspect, not proof that the current code was rerun. Record their source and any missing design information.
- Distinguish numerical evidence from formal proof. Connect findings to the relevant theory without rewriting the manuscript unless requested.
- Use the existing Markdown context when recording research notes within scope; do not introduce a separate task runner, state system, or reporting pipeline.

## Good output standard

A good simulation workflow should let a future reader quickly answer:

- What is the simulation testing, and how does it connect to the research question?
- What DGP, assumptions, parameter grid, seed policy, and methods were used?
- What actually ran, and how many replications succeeded or failed?
- What metrics and denominators support the findings?
- What do the results suggest, and what limitations remain?

Before delivery, check the template structure, parameter settings, grid, counts, denominators, and execution status for consistency. Provide the notebook path and a concise account of findings, missing information, or incomplete execution. Include an optional export path only when one was produced. Use medium detail: enough to reproduce and interpret the exercise without turning the explanation into a code dump.

## Example prompt patterns

Use this skill when the user asks things like:

- help me design a simulation for this model
- create a Python notebook in the course simulation format, with an English report
- turn this DGP into an Rmd simulation with a Chinese explanation
- inspect these simulation results and check the failure counts
- summarize what this numerical exercise shows
- suggest robustness checks or connect this simulation to my theory notes
