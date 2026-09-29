---
name: paper-search
description: Use when the user wants help finding relevant papers, building a reading list, comparing related literature, locating papers by topic or method, or identifying how a paper fits into an existing research project.
---

# Paper Search

Use this skill when the user wants to search for literature or organize a literature search into a usable research workflow.

The goal is not just to list papers. The goal is to help the user find papers that are relevant, explain why they matter, and connect them to local notes in `references/` when possible.

## What to inspect

Inspect only the files needed for the task:

- relevant notes in `references/`
- the latest finalized `report/YYYY-MM-DD-weekly-meeting.md` if recent
  discussions define the search direction
- any local project notes, prompts, or research questions provided by the user
- the most relevant LaTeX file in `deliverable/paper/` when it helps identify the project's current framing, terminology, or literature needs

Use local notes first to understand the topic, terminology, and existing literature map.

If the task requires current or external literature lookup, browse the web carefully and cite sources.

## Search workflow

When searching for papers:

1. clarify the research question, method, model, or topic from local context if available
2. identify the most useful search dimensions, such as topic, method, application, identification strategy, or theoretical mechanism
3. search for relevant papers
4. organize the results into a useful structure rather than a raw list
5. explain why each paper is relevant
6. compare the papers when helpful
7. suggest which papers should be read first

## Preferred output formats

Default to one of these formats depending on the request:

- a short ranked reading list
- a grouped literature map
- a comparison table in Markdown
- a list of candidate papers with one- or two-sentence relevance notes
- a recommendation for which paper notes should be created next in `references/`

## Preferred table format

When presenting structured information, use a clear academic-style Markdown table format that prioritizes clarity, comparability, and citation traceability.

For literature or reference summaries, default to these columns when applicable:

| Column | Purpose |
|---|---|
| **Article Title** | Full title of the paper or work. |
| **Authors** | List of authors. |
| **Journal / Outlet** | Publication venue. |
| **Year** | Publication year. |
| **Role in Discussion** | Why the work is cited or how it supports the argument. |
| **Link / DOI** | Direct link, DOI, or official webpage. |

Add columns only when they materially improve the comparison. Useful optional columns include:

- **Method / Model**
- **Data / Empirical Context**
- **Research Domain**
- **Key Contribution**

### Writing style within tables

- Use concise phrases rather than full paragraphs.
- Use clear academic terminology.
- Avoid unnecessary narrative.
- Keep interpretive cells to one or two lines when possible.

Example for `Role in Discussion`:

| Role in Discussion |
|---|
| Classic review of conjoint analysis used to motivate preference measurement methods. |

### Ordering of rows

Organize rows in the way that best supports the argument. Preferred orderings are:

1. chronological order
2. conceptual grouping
3. importance hierarchy

### Citation integration

- Ensure the works listed match the citations used in the surrounding discussion.
- Prefer peer-reviewed sources when available.
- Include stable links or DOIs when possible.
- When summarizing literature for a manuscript, prioritize works that directly support the paper's theoretical framing, empirical design, or methodological contribution.

### Readability requirements

- Prefer five to eight columns when possible.
- Avoid overly long cell content.
- Use consistent terminology across rows.
- Keep one concept per column.
- If a table becomes too large, split it into multiple thematic tables or summarize only the most relevant works.

Use tables when summarizing literature reviews, comparing models or algorithms, listing datasets or empirical studies, or organizing methodological differences.

Tables should complement the text, not replace explanation.

## Writing rules

- Prioritize relevance over comprehensiveness.
- Prioritize high-quality journals when selecting papers.
- Explain why each suggested paper belongs on the list.
- Distinguish clearly between foundational papers, closely related papers, and peripheral papers.
- Prefer papers that match the user's actual question, not just keyword overlap.
- When the evidence is uncertain, say so clearly.
- Keep the search output concise and decision-oriented.

## Journal-quality preference

When choosing which papers to emphasize, prioritize papers from stronger journals whenever this is a useful proxy for relevance and reliability.

Default ranking preference:

- highest priority: `Excellent`, `A+`, `A`
- secondary priority: `B+`, `B`

Use lower-ranked outlets only when:

- they are highly relevant to the exact question
- they are standard references in a niche subfield
- they provide useful technical or empirical details that stronger-journal papers do not cover

Do not use journal rank mechanically. A directly relevant paper in a lower-ranked outlet can still be worth including, but the default search and recommendation strategy should focus more on higher-quality journals.

For management-science searches, emphasize stronger journals within the relevant subfield rather than using one global list. Relevant subfields include `IS`, `IT`, `marketing`, `OR`, and `transportation`.

For economics and econometrics searches, treat the following as especially high-priority outlets based on the user's ranking preferences:

- `Excellent`: American Economic Review, Econometrica, Journal of Finance, Journal of Political Economy, Quarterly Journal of Economics, Review of Economic Studies
- `A+`: American Economic Journal: Applied Economics, American Economic Journal: Economic Policy, American Economic Journal: Macroeconomics, American Economic Journal: Microeconomics, Economic Journal, Economic Theory, European Economic Review, Experimental Economics, Games and Economic Behavior, International Economic Review, Journal of Business and Economic Statistics, Journal of Development Economics, Journal of Econometrics, Journal of Economic Theory, Journal of Financial Economics, Journal of Human Resources, Journal of International Economics, Journal of Labor Economics, Journal of Monetary Economics, Journal of Political Economy, Journal of Public Economics, Quantitative Economics, RAND Journal of Economics, Review of Economics and Statistics, Review of Finance, Review of Financial Studies, Theoretical Economics
- `A`: Econometric Theory, Economica, Journal of Applied Econometrics, Journal of Economic Dynamics and Control, Journal of Economics and Management Strategy, Journal of Industrial Economics, Journal of Mathematical Economics, Journal of Money, Credit and Banking, Journal of Population Economics, Journal of Risk and Uncertainty, Macroeconomic Dynamics, Scandinavian Journal of Economics, Social Choice and Welfare

For management science, use the following inferred tiers based on the rank order in the user's supplied subfield lists. These tiers are working heuristics for search prioritization, not official labels from the source ranking.

### Information Systems (IS)

- `Excellent`: MIS Quarterly
- `A+`: Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, Information Systems Journal
- `A`: Journal of Strategic Information Systems, European Journal of Information Systems, Journal of Information Technology, Information & Management, Decision Support Systems

### Information Technology (IT)

- `Excellent`: IEEE Transactions on Knowledge and Data Engineering
- `A+`: IEEE Transactions on Software Engineering, INFORMS Journal on Computing, ACM Computing Surveys
- `A`: IEEE Transactions on Systems, Man, and Cybernetics: Systems, IEEE Transactions on Cybernetics, IEEE Transactions on Pattern Analysis and Machine Intelligence

### Marketing

- `Excellent`: Journal of Marketing, Journal of Consumer Research
- `A+`: Journal of Marketing Research, Marketing Science, Journal of the Academy of Marketing Science
- `A`: Journal of Retailing, Journal of Consumer Psychology, International Journal of Research in Marketing, Journal of Service Research, Journal of Product Innovation Management
- `B+`: Quantitative Marketing and Economics, Journal of Advertising, Journal of Business Research, Marketing Letters, Journal of Public Policy and Marketing, Journal of Business Ethics, European Journal of Marketing, Journal of Interactive Marketing, Industrial Marketing Management, Journal of International Marketing, Psychology and Marketing

### Operations Research (OR) / Operations Management

- `Excellent`: Management Science
- `A+`: Operations Research, Manufacturing and Service Operations Management, Journal of Operations Management, Production and Operations Management
- `A`: European Journal of Operational Research, Decision Sciences, INFORMS Journal on Computing, Journal of Supply Chain Management, IISE Transactions, Naval Research Logistics


### Transportation

- `Excellent`: Transportation Research Part B: Methodological
- `A+`: Transportation Research Part C: Emerging Technologies, Transportation Science, Transportation Research Part A: Policy and Practice
- `A`: Transportation Research Part E: Logistics and Transportation Review, Accident Analysis and Prevention, Transportation Research Part D: Transport and Environment

Do not add a `Journal Tier` column to tables unless the user explicitly asks for it. Use the ranking preference to guide selection and ordering, not to make the table heavier by default.

## Linking to local research memory

When local notes already exist:

- identify which papers are already covered in `references/`
- point out missing but nearby papers
- connect new search results to existing local notes when useful
- avoid recommending papers the user already has unless comparison is the point

## Good output standard

A good search result should help the user quickly answer:

- Which papers are most relevant?
- Why are they relevant?
- Which papers should I read first?
- How do these papers differ?
- What gaps remain in my current reading set?

## Example prompt patterns

Use this skill when the user asks things like:

- find papers on this topic
- what are the key papers for this question
- help me search the literature on this model
- compare papers related to this identification strategy
- suggest what I should read next based on my notes
- build a reading list for this project
