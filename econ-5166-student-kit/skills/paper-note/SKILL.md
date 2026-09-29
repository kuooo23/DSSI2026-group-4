---
name: paper-note
description: Use when the user wants to turn a paper into a structured Markdown note in references/, update an existing paper note, extract figures for note-taking, or connect a paper to ongoing research ideas.
---

# Paper Note

Use this skill when working on paper reading notes in `references/`.

The goal is to produce Markdown notes that are easy for both the user and Codex to reuse later. The note should capture the paper faithfully, separate summary from interpretation, and make the paper's relevance to current research explicit.

## What to inspect

Inspect only the files needed for the task:

- the target note in `references/` if it already exists
- related note files in `references/` if the user asks for comparison or links
- any local Markdown note, excerpt, PDF text, or citation provided by the user
- the most relevant LaTeX file in `deliverable/paper/` when it provides important project context

## Output location

Create or update a note in `references/`.

Preferred filename: match the paper file name when one already exists. Use a slug that includes author name, year, abbreviated journal name if useful, and a short title.

Examples:

- `rust-1987-rust-models-of-arithmetic.md`
- `hotz-miller-1993-conditional-choice-probabilities.md`

If the exact title is too long, shorten the slug while keeping it recognizable.

## Figure handling

If the workflow includes pasted figures from papers, store them under:

`attachments/references/<paper-slug>/`

Use relative Markdown links from files inside `references/`.

Example:

```md
![Figure 1](../attachments/references/hotz-miller-1993/fig-1.png)
```

Do not create or move figures unless the task requires it. Prefer reusing existing attached files.

## Default note structure

Use this structure unless the user asks for a different format or an existing note already uses a stable structure.

```md
# Title

## Citation

## Relevance to My Work

## Summary
```

## Citation metadata

When citation metadata is needed:

- prefer local `.bib` files, DOI metadata, publisher pages, Crossref, or Semantic Scholar
- use Google Scholar only as a fallback for BibTeX lookup
- if no stable citation key is available, keep the entry empty


Adjust section names when needed:
- for theory papers, emphasize setup, assumptions, mechanism, proof idea, and relevance
- for empirical papers, emphasize identification, data, estimation, evidence, and limitations

If the note would benefit from more detail, expand `## Summary` into concise subsections such as:

- Main Question
- Result
- Model / Setup
- Assumptions
- Identification or Mechanism
- Intuition
- Evidence / Method
- Limitations
- Questions
- Related Papers

If a section is not applicable, keep the structure compact and omit it instead of filling it with weak content.

## Writing rules

- Separate the paper's claims from your interpretation.
- Be faithful to the source; do not overstate results.
- Prefer concise, reusable notes over long prose.
- Preserve user-written comments when updating an existing note.
- Do not overwrite an existing note structure unless the user asks for a rewrite.
- Include technical detail only when it is central to understanding the contribution.
- Focus questions on research value: what is unclear, fragile, extendable, or relevant.

## Update behavior

When updating an existing note:

- preserve the existing filename if reasonable
- retain the user's original comments, questions, and custom structure where possible
- fill missing sections instead of rewriting everything
- remove duplication if the note became repetitive
- preserve relative links to local attachments when they already exist
- keep the note readable as a long-term research memory file

## Related paper linking

When the user asks for connections across papers:

- identify closely related papers from local notes first
- mention whether the connection is about question, method, assumptions, identification, or result
- keep links short and useful rather than producing a literature dump

## Good output standard

A good paper note should let a future reader quickly answer:

- What is the paper trying to do?
- What is the main result?
- What assumptions matter most?
- Why does the result work?
- What is weak, unclear, or extendable?
- Why does this matter for my research?

Default to medium detail: detailed enough to be useful later, short enough to skim quickly.

## Example prompt patterns

Use this skill when the user asks things like:

- summarize this paper into a Markdown note
- turn my reading notes into a structured paper summary
- update the note in `references/` for this paper
- extract the key assumptions and intuition from this theory paper
- connect this paper to my other notes
- help me write a reading note from this PDF
