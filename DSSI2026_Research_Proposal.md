# Race and Mortgage Approval Outcomes: A Pooled Comparison Across Selected U.S. States

**Course / Group:** ECON 5166 / Group 4  
**Draft date:** November 17, 2026  
**Status:** Draft for team review; research motivation and mortgage-data provenance and period remain to be confirmed. The existing project record lists 楊捷睎 as Data Analyst; the team has assigned 張亭婕 as Project Manager and 郭千翠 as Data Engineer for this proposal.

**Members**

- 楊捷睎 (B12104043)
- 郭千翠 (B13303122)
- 張亭婕 (B13303085)

## 1. Project Description: Research Question, Motivation, and Research Method

### Research Question

Among mortgage application records classified as White, Black, or Asian in the available state-group datasets, are approval outcomes associated with applicant race before controlling for income, state, or other loan characteristics?

The question follows the current project context. It is an unadjusted comparison of associations, not a test of discrimination or a causal effect.

### Research Motivation

**To be completed by the team.** The project records the research question but does not yet document the group's observation, concern, or reason for studying it. The team should explain in its own words what prompted the question and why comparing approval outcomes matters. No motivation is inferred from the template example or from the data alone.

### Data Sources

The primary inputs are four existing, 15-column, state-group mortgage-application CSV files in [`data/processed/`](econ-5166-student-kit/data/processed/):

1. [`state_VT-ME-WV_white_high_15_columns.csv`](econ-5166-student-kit/data/processed/state_VT-ME-WV_white_high_15_columns.csv)
2. [`state_HI-DC-CA_white_low_15_columns.csv`](econ-5166-student-kit/data/processed/state_HI-DC-CA_white_low_15_columns.csv)
3. [`state_MA-CO-DC_income_high_15_columns.csv`](econ-5166-student-kit/data/processed/state_MA-CO-DC_income_high_15_columns.csv)
4. [`state_NM-LA-MS_income_low_15_columns.csv`](econ-5166-student-kit/data/processed/state_NM-LA-MS_income_low_15_columns.csv)

The project documentation reports a combined 1,076,414 rows before removing a duplicated District of Columbia source. The two DC extracts were reported to match row by row; retaining the DC records from the MA–CO–DC file removes 8,387 duplicate-source rows, leaving 1,068,027 observations for the existing pooled analysis. The resulting geography is ten states plus DC. The mortgage files' original source, collection period, and upstream processing code have not been established in the repository; the period must not be described as 2024 based on the separate ACS files.

The files contain `state_code`, `county_code`, `derived_ethnicity`, `derived_race`, `derived_sex`, `action_taken`, `loan_type`, `loan_purpose`, `loan_amount`, `loan_to_value_ratio`, `property_value`, `occupancy_type`, `income`, `debt_to_income_ratio`, and `applicant_age`. For the recorded baseline model, `action_taken` codes 1 and 2 are treated as approved and code 3 as denied. The race comparison uses White as the reference group and indicators for Black and Asian applicants.

The repository also contains 2024 ACS 1-Year PUMS housing files for ten states and the District of Columbia, plus the Census ACS B02001 state-level race table and associated source documentation. Derived income-quartile and White-population-share files are used in existing state-group analyses. The PUMS records describe housing units and households, while B02001 is state-level; neither is mortgage-application data. No verified record-level join key is documented, so these sources will not be merged into the primary model.

### Research Method

The proposed primary analysis is a pooled binary logistic regression:

`logit[P(Approved_i = 1)] = β0 + β1 Black_i + β2 Asian_i`

White applicants are the reference category. The binary outcome is coded 1 for `action_taken` 1 or 2, and 0 for `action_taken` 3. Other action outcomes and race categories outside the three represented groups are not included. The recorded analysis retains observations with missing income because income is not a predictor in this unadjusted model. Inference uses HC1 heteroskedasticity-robust standard errors. The model estimates unadjusted associations; HC1 does not account for clustering by state or lender.

The team can summarize approval proportions by race and report odds ratios, confidence intervals, and a joint Wald test of `β1 = β2 = 0`. The existing, executed analysis is documented in [`pooled_race_logistic_regression.ipynb`](econ-5166-student-kit/finding/pooled_race_logistic_regression.ipynb). The proposal does not claim that the currently available files represent a verified year or a representative national sample.

## 2. Existing Raw Data

No raw mortgage-application source extracts or source documentation are currently recorded in the repository. The files used for the existing mortgage analysis are processed state-group CSVs, and their original source and collection period remain unverified. Accordingly, the examples below are actual rows in the available processed files, **not raw-source observations**. They demonstrate that the model's outcome and race fields are present, but do not establish provenance or the ability to reproduce the upstream collection.

| File / geography | `derived_ethnicity` | `derived_race` | `action_taken` | `loan_amount` | `income` | `debt_to_income_ratio` | `applicant_age` |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| HI / county 15003, from `state_HI-DC-CA_white_low_15_columns.csv` | Hispanic or Latino | Asian | 1 | 555,000.0 | 113 | 30%-<36% | 25-34 |
| MA / county 25023, from `state_MA-CO-DC_income_high_15_columns.csv` | Not Hispanic or Latino | Black or African American | 1 | 605,000.0 | 147 | 45 | 25-34 |

The repository also contains raw ACS PUMS housing files and an ACS B02001 state-level table. These are separate datasets and are not raw mortgage-application records.

## 3. Data Requirements for the Main Analysis

The primary analysis requires one record per eligible mortgage application with a recorded race category and an outcome that can be classified as approved or denied. The current files provide the following schema and coverage according to [`PROJECT.md`](econ-5166-student-kit/PROJECT.md) and their inspected headers:

| Requirement | Definition / current evidence | Status and preparation |
| --- | --- | --- |
| Observation unit | One row in a state-group mortgage CSV; intended to represent an application record | Application-level interpretation is recorded in project notes, but a unique application identifier is unavailable and within-file duplicates have not been ruled out. |
| Geography | VT, ME, WV; HI, DC, CA; MA, CO, DC; NM, LA, MS | Combine the four files and retain DC from the MA–CO–DC source only; this removes the documented 8,387-row overlap. |
| Period | Application year or years | Not available in the documented schema; the period and source must be confirmed before temporal claims are made. |
| Sample size | 81,303; 524,988; 287,517; and 182,606 rows in the four files, respectively | 1,076,414 rows before the documented duplicate-DC-source removal; 1,068,027 in the existing pooled analysis. These counts do not verify uniqueness of all remaining records. |
| Dependent variable | `action_taken`: 1 or 2 = approved; 3 = denied | Create a binary outcome. Exclude other outcomes as specified in the existing analysis. |
| Main independent variables | `derived_race`: White, Black or African American, Asian | Use White as the reference group; include Black and Asian indicators. Other race categories are outside the current analysis scope. |
| Other available fields | `income`, `loan_type`, `loan_purpose`, `loan_amount`, `loan_to_value_ratio`, `property_value`, `occupancy_type`, `debt_to_income_ratio`, `applicant_age`, `derived_sex`, `derived_ethnicity`, state and county | Available in the inspected 15-column files. They are not predictors in the recorded baseline model. Income missingness does not trigger exclusion in that model. |
| Final analysis file | Pooled eligible observations from the four processed state-group files | Retain the source file and state for traceability; remove the duplicated DC source records as documented. A complete source lineage and a unique application key remain unavailable. |

The ACS files are not required to estimate the race-only model. Their 2024 period and housing-unit, household, or state-level units do not establish the period or source of the mortgage applications. The existing ACS-derived income thresholds and White-population-share measures may describe how some state groups were assembled, but they do not justify merging ACS observations to mortgage records.

## 4. Hypothesis and Expected Main Results

The recorded research question is non-directional. The corresponding statistical hypotheses are:

- **Null hypothesis:** `βBlack = βAsian = 0`; approval odds do not differ between the represented race groups in the unadjusted model.
- **Alternative hypothesis:** At least one of the two race coefficients differs from zero.

The team's directional expectations and reasoning have not been recorded and should be added after discussion. No directional result is asserted here as an advance prediction.

For context, the repository already contains an executed pooled analysis on 1,068,027 observations. Its reported odds ratios are 0.4461 for Black relative to White applicants (95% CI 0.4399–0.4524; HC1 p < 1e-300) and 1.0206 for Asian relative to White applicants (95% CI 1.0072–1.0342; HC1 p = 0.002557). The joint Wald test is reported as p < 1e-300. These are **existing exploratory estimates**, not expected future results or causal effects. The team should verify that the analysis period, source, and sample definition are appropriate before presenting them as definitive findings.

The study's potential value is a transparent description of unadjusted approval-outcome differences in the available records. It cannot, on this design alone, identify why differences occur or establish discriminatory treatment.

## 5. Expected Limitations

1. **Unverified provenance and time period:** The mortgage files' source, collection dates, and upstream construction are not documented. The available ACS data cannot fill this gap.
2. **Record linkage and duplication:** No unique application key is available. The documented DC source overlap was removed, but this does not prove that the remaining files contain no duplicate applications.
3. **Limited and selected sample:** The data cover selected states and DC and only the three race categories used by the existing model. They may not represent all U.S. applications or applicants.
4. **Unadjusted comparison:** Income, state, lender, loan type, loan purpose, and other application characteristics may be associated with both race and approval. The baseline model does not adjust for these differences and should not be interpreted causally.
5. **Inference and dependence:** HC1 standard errors address heteroskedasticity but do not account for within-state or within-lender dependence. The current files do not document lender identifiers for such adjustment.
6. **Measurement and missingness:** The race and ethnicity fields are derived categories, and some loan and applicant fields contain missing values. The recorded race-only model does not use income, but the missingness and coding may affect interpretation and future adjusted analyses.
7. **No verified survey weights:** The mortgage files' sampling or weighting design is not documented; estimates should be described as applying to the available records, not as population estimates.

## 6. Team Roles and Responsibilities

The project contribution record in `econ-5166-student-kit/PROJECT.md` lists 楊捷睎 as Data Analyst. For this proposal, the team has assigned 張亭婕 as Project Manager and 郭千翠 as Data Engineer. Proposal-specific responsibilities beyond these role assignments should be confirmed by the team.

| Course role | Member | Confirmed responsibility |
| --- | --- | --- |
| Project Manager | 張亭婕 (B13303085) | Project Manager for this proposal; specific responsibilities to be confirmed. |
| Data Engineer | 郭千翠 (B13303122) | Data Engineer for this proposal; specific responsibilities to be confirmed. |
| Data Analyst | 楊捷睎 (B12104043) | Data Analyst is listed in `econ-5166-student-kit/PROJECT.md`; proposal-specific responsibilities to be confirmed. |
