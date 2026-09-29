---
name: beamer-slides
description: Use only when the user wants to initialize a new Beamer deck, slide outline, or first-pass set of frames from a paper draft, theory sketch, or research notes, especially when starting a presentation from scratch in deliverable/slides/. When generating frames, include a `% message:` comment that states the slide's intended message, insert `% -----------------` between frames for easy navigation, and keep figure/table slides sparse by using takeaway titles, at most two visible sentences, and LaTeX presenter-note comments for the spoken interpretation. Do not use this skill for revising an existing deck; use `revise-beamer-slides` instead.
---

# Beamer Slides Initialization

Use this skill only when the user is starting a new deck or asking for an initial slide structure from the paper or other project notes.

The goal is to create a clean first-pass presentation that has a coherent research narrative, uses the right level of detail, and is easy to extend later.

When this skill generates new frames, include a `% message:` comment for each frame to state the intended takeaway of that slide.

When a frame centers on a figure or table, keep the visible slide content sparse: prefer a takeaway-style frame title, limit the body text to at most two sentences, and place the fuller spoken interpretation in LaTeX presenter-note comments inside the frame.

This skill is for initialization. If the user already has a `.tex` deck in `deliverable/slides/` and wants to edit it in place, follow inline comments, or turn rough slide stubs into polished slides, use `revise-beamer-slides` instead.

Match the user's established Beamer style from prior decks whenever possible, both visually and content-wise.

## Boundary with Revise Beamer Slides

Use `revise-beamer-slides` instead when:

- the user already has an existing Beamer deck
- the user places `%` instructions or rough slide notes inside a `.tex` file
- the user wants localized edits rather than a new talk structure
- the user wants slide purpose comments preserved while the body is rewritten

## What to inspect

Inspect only the files needed for the task:

- the most relevant LaTeX file in `deliverable/paper/`, since it contains the latest project framing, notation, and key results
- directly relevant notes in `references/` only when they materially affect framing
- any talk purpose, audience, time limit, or outline provided by the user
- older slide decks when the user provides them as style references

For initialization work, treat the draft paper in `deliverable/paper/` as the primary source of project content.

## Output targets

Default output is one of the following, depending on the user's request:

- a new Beamer slide outline
- a new deck skeleton or preamble for `deliverable/slides/`
- a first-pass set of Beamer frames
- a compact speaking-flow outline for a new meeting, workshop, or seminar talk

When generating more than one frame in LaTeX, place a separator comment of the form `% -----------------` between `\end{frame}` and the next `\begin{frame}`.

## Message comments

For each newly generated frame, add a LaTeX comment of the form `% message: ...` that states the slide's main message in one sentence.

- Treat the `% message:` comment as the slide-level intent, not as presenter notes or a full paragraph.
- Keep it specific enough that a later revision can tell what the slide is trying to accomplish.
- Place the `% message:` comment directly inside the frame near the top, typically immediately after `\begin{frame}{...}` or immediately after `\frametitle{...}` when that style is used.
- Preserve concise wording; one sentence is the default.

When useful, prefer a pattern like:

```tex
\begin{frame}{Introduction}
% message: motivate why learning preferences from incomplete rankings matters in economics, marketing, and personalization.
...
\end{frame}

% -----------------

\begin{frame}{This Paper}
% message: summarize the paper's core modeling contribution.
...
\end{frame}
```

## Presenter-note comments

When a slide shows a figure or table, keep the on-slide interpretation short and move the fuller speaking script into LaTeX comments.

- Use a comment block such as `% presenter notes:` followed by `% - ...` lines.
- Place the presenter-note block near the top of the frame, typically right below the `% message:` comment.
- Use presenter notes to say what to point at, what the result means, and what caveat or comparison to mention orally.
- Keep presenter notes concise and speaker-facing; they are not part of the visible slide text.

When useful, prefer a pattern like:

```tex
\begin{frame}{Region Preferences Are Heterogeneous, Not One-Dimensional}
% message: the figure shows regional preferences do not collapse to one simple axis.
% presenter notes:
% - Start with the headline: the pattern is not just old world versus new world.
% - Point to the strongest positive cluster and name the regions involved.
% - Then note the weaker correlation for Bordeaux and Burgundy once observables are controlled for.
% - Close by explaining why the distinct Marlborough pattern matters substantively.

This heatmap shows that regional tastes cluster along multiple dimensions rather than a single old-world versus new-world line.

\begin{center}
\includegraphics[width=0.72\textwidth]{figures/region-correlation.pdf}
\end{center}
\end{frame}
```

## Workflow

When initializing slides:

1. identify the talk purpose, audience, and time constraint if known
2. inspect the most relevant LaTeX draft in `deliverable/paper/` to recover the current project framing
3. extract the smallest set of points needed for a coherent slide narrative
4. organize the presentation into a logical sequence
5. decide the main message of each frame and encode it in a `% message:` comment
6. write concise Beamer-ready slide content
7. trim unnecessary detail so each slide has one clear job
8. leave room for later deck-specific revisions rather than overbuilding the first draft

## Style guide from prior slides

Use the user's prior slides as the default style reference.

### Visual conventions

- Default to `\documentclass[10pt]{beamer}`.
- Prefer `\usetheme{default}` with `\usecolortheme{orchid}` unless the user clearly uses something else.
- Keep title and frametitle styling simple and academic rather than decorative.
- Use black or near-black title text and a thin horizontal rule under frame titles when matching the user's usual style.
- Prefer square main bullets, circular sub-bullets, light use of `\vs`, and uncluttered layouts.
- Do not force `itemize` on every content slide; use bullet icons only when the slide genuinely contains a list, and especially when introducing sub-points under a main statement.
- Keep layouts clean and sparse; avoid flashy visual effects or crowded multi-panel slides unless clearly needed.
- Prefer generous whitespace and visible margins around the main content rather than densely filling the frame.

### Default preamble conventions

When creating a new Beamer deck that follows the user's usual style, a preamble close to this setup is a reasonable default:

```tex
\documentclass[10pt]{beamer}

\mode<presentation> {
\usetheme{default}
\usecolortheme{orchid}
}

\usepackage{setspace}
\usepackage{booktabs,caption}
\captionsetup{justification=centering}
\usepackage[flushleft]{threeparttable}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{mathtools}
\usepackage{bbm}
\usepackage{bm}
\usepackage{amsfonts}
\usepackage{verbatim}
\usepackage{comment}
\usepackage{enumitem}
\usepackage[natbib=true, bibstyle=authoryear, citestyle=authoryear-comp]{biblatex}

\setitemize{label=\usebeamerfont*{itemize item}%
  \usebeamercolor[fg]{itemize item}
  \usebeamertemplate{itemize item}}
\setbeamertemplate{frametitle continuation}[from second][(Cont'd)]
\setbeamertemplate{itemize item}[square]
\setbeamertemplate{itemize subitem}[circle]
\setbeamerfont{itemize/enumerate subbody}{size=\scriptsize}
\setbeamertemplate{bibliography item}{}

\setbeamercolor{lower separation line head}{bg=black}
\setbeamertemplate{frametitle}{
    \vskip0.3cm
    \usebeamerfont*{frametitle}\insertframetitle
    \vskip-0.5ex
    \begin{beamercolorbox}[colsep=0.75pt, wd=\textwidth]{lower separation line head}
    \end{beamercolorbox}
}
\setbeamercolor{title}{fg=black}
\setbeamercolor{frametitle}{fg=black,bg=black!20}
\setbeamercolor{section in head/foot}{bg=black}
\setbeamercolor{author in head/foot}{bg=black}
\setbeamercolor{date in head/foot}{bg=black}

\newcommand{\vs}{\vspace{1em}}
```

Keep the preamble lightweight when possible, and add packages only when the slide content actually needs them.

### Content conventions

- Start from a simple talk arc: motivation, research question, this paper, findings, setup, method, results, limitations, conclusion.
- Use slide titles that are direct and informative, such as `Introduction`, `This Paper`, `Summary of Findings`, `Related Literature`, or a short statement of the main point.
- On result slides with figures or tables, it is often good to put the takeaway directly in the frame title.
- Give each frame a `% message:` comment that states what the audience should take away from the slide.
- Prefer short declarative slide text over dense prose.
- If a sentence wraps and leaves only one or two words on the last line, shorten or rephrase it.
- Keep one main message per slide.
- Avoid starting the slide body with a displayed equation. Introduce the math with a short verbal setup, claim, or intuition line first, then show the equation.
- At the top level, often use a short statement, equation, block, or compact paragraph instead of an `itemize` environment.
- Use bullet icons only for parallel points or subordinate details; avoid turning each sentence into its own bullet.
- If bullets are used, keep the list short, often two to four items.
- Use figures, tables, and equations only when they carry the main point of the slide.
- For figure and table slides, keep the visible body text to at most two sentences total; move extra interpretation into presenter-note comments.
- When presenting technical material, pair formal notation with one sentence of intuition.
- When presenting results, state the substantive conclusion first in unbulleted form and put nuance in bullets underneath only if the hierarchy helps.

### Beamer writing conventions

- Prefer concise frame content that can be pasted directly into an existing deck.
- Add a `% message:` comment near the top of every newly generated frame.
- Insert `% -----------------` between consecutive frames so the user can scan and locate frames quickly in the `.tex` file.
- Use `\vs` or light vertical spacing when it improves readability and matches the surrounding style.
- Keep notation consistent with the project draft in `deliverable/paper/`.
- Prefer readable tables and centered figures over overloaded slide text.
- Avoid turning slide text into a paragraph copied from the paper draft.
- Avoid defaulting to one-bullet-per-sentence formatting.
- As a house style, text inside `\item` should start with lower case.

## Slide design rules

- Prefer one clear idea per slide.
- Keep slide text concise and presentation-friendly.
- Do not overcrowd slides. Prefer a slide with breathing room and clear margins over a slide that tries to say everything at once.
- Avoid math-first layouts where the first visible content under the title is a standalone equation. Give the audience one line of orientation before the notation whenever possible.
- For slides built around a figure or table, prefer the graphic plus at most two visible sentences rather than a graphic plus a long bullet list.
- Avoid awkward wrapped lines with only one or two trailing words. Tighten the sentence rather than accepting the orphaned ending.
- Use equations only when they are central to the point of the slide.
- Do not paste long paragraphs from the paper draft into slides.
- Emphasize motivation, intuition, identification, main result, and takeaway.
- Keep notation consistent with the LaTeX draft in `deliverable/paper/`.
- Default to Beamer-friendly LaTeX output when the user asks for slide content.
- If a draft slide becomes dense, cut secondary detail, shorten prose, or split ideas across slides rather than shrinking margins or packing in more bullets.

## Good output standard

A good slide draft should let a future presenter quickly answer:

- What is the main message of the talk?
- Why does each slide exist?
- Does each frame have a clear `% message:` comment that states its intended takeaway?
- Are consecutive frames separated by `% -----------------` so the deck is easy to navigate in source form?
- Do figure and table slides keep the visible text to at most two sentences and put the fuller script in presenter-note comments?
- What is the audience supposed to remember?
- Which technical details are essential and which can be omitted?
- Does each slide still have breathing room, with visible margins and non-crowded content?

Default to concise output: enough detail to build a deck, but not so much that the slides become a second paper.

## Example prompt patterns

Use this skill when the user asks things like:

- turn this draft into Beamer slides
- make slides for this theory section
- outline a seminar talk from my paper draft
- convert these notes into presentation frames
- build an initial deck for a workshop talk from this paper
- create a first-pass set of slides in `deliverable/slides/` from this draft
