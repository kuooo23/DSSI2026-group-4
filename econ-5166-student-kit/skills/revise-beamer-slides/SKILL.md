---
name: revise-beamer-slides
description: Use when the user wants to revise an existing Beamer deck in deliverable/slides/, especially by following inline LaTeX comments, `% message:` comments, `GPT-*` frame tags, or `%GPT:` instructions, editing only the tagged frames, or turning rough tagged slide stubs into polished Beamer content while preserving the slide purpose as a LaTeX comment. For revised frames, add a `%revised` tag and report in chat the line number of the first revised frame. For figure/table result slides, prefer takeaway titles, keep visible text to at most two sentences, and place the fuller spoken interpretation in LaTeX presenter-note comments.
---

# Revise Beamer Slides

Use this skill when the user already has a Beamer `.tex` file and wants the deck updated in place.

The goal is to make localized, presentation-ready edits inside the existing deck. Start from the slide file itself rather than rebuilding slides from the paper.

When `GPT-*` tags are present, treat them as the edit boundary: revise tagged frames only and leave every other frame untouched.

When a frame has a `% message:` comment, treat it as the intended takeaway of that slide and revise the frame to serve that message.

When a tagged frame centers on a figure or table, prefer a sparse result-slide format: the takeaway can live in the frame title, the visible body should usually be at most two sentences, and the fuller explanation should be moved into presenter-note comments.

## Primary context

For this skill, the target `.tex` file in `deliverable/slides/` is the main working document.

Consult `deliverable/paper/` only when needed to:

- recover notation
- verify a claim or equation
- match the latest project framing

## Save-state safety

Before editing, make sure the target Beamer `.tex` file is saved to disk.

- Codex can only read and edit the on-disk file; it cannot see unsaved editor-buffer changes.
- If the user indicates the file may have unsaved changes, or if there is any reason to doubt that the on-disk file is current, stop and ask the user to save the file before proceeding.
- Do not edit the `.tex` file, add `%revised` tags, or report revised-frame line numbers until the saved file is available.

## What to inspect

Inspect only the files needed for the task:

- the target `.tex` file in `deliverable/slides/`
- `% message:` comments that describe the intended message of each frame
- `GPT-*` tags and nearby `%GPT:` comments that specify which frames are in scope and what to do
- nearby `%` comments that contain slide purpose notes or rough outlines
- older slide decks supplied by the user when they serve as style references
- the most relevant LaTeX draft in `deliverable/paper/` only when needed for notation or factual consistency

## Supported use cases

Use this skill when the user wants to:

- revise existing slides based on inline instructions, `% message:` comments, or `GPT-*` frame tags in the Beamer source
- add or fill in a `GPT-N` slide from a purpose comment and a rough outline
- lightly polish a `GPT-GS` slide for grammar and professional style
- tighten titles, bullets, equations, transitions, or local slide order within an existing deck
- convert rough slide notes into professional Beamer writing without turning them into paper prose

## GPT tag rules

Treat `GPT-*` tags as the frame-selection mechanism.

- A frame is editable only if it contains a `GPT-*` tag or has one in the LaTeX comments directly attached to that frame.
- If multiple frames are tagged, revise each tagged frame independently and do not change untagged frames.
- `GPT-N` means "new": the frame may be only a rough outline or placeholder, so you may rewrite freely within that frame to make it presentation-ready.
- `GPT-GS` means "grammar and style": the frame is already substantively developed, so limit changes to grammar, wording, and professional polish.
- If a frame has more than one tag, inspect the actual slide content and any `%GPT:` comments, then apply the tags by discretion. When signals conflict, prefer the more conservative edit unless the frame is clearly a rough stub.
- If the user defines additional `GPT-*` tags in the prompt, follow those definitions for that run.

## Comment handling rules

Treat nearby LaTeX comments, especially `% message:`, `% presenter notes:`, `%revised`, and `%GPT:` comments, as authoritative local instructions.

- Keep slide purpose comments as LaTeX comments directly above the relevant frame.
- Treat `% message:` comments as the authoritative description of what the slide is trying to communicate.
- Preserve `% message:` comments when revising a frame, and update the frame body so it matches that message more clearly.
- Preserve `% presenter notes:` blocks when they already exist, and update them when the spoken interpretation changes.
- Add a `%revised` comment to every frame that you revise, and place it with the frame's other top-of-frame comments so the edit is easy to audit later.
- When revising a dense figure or table slide, move detail from visible bullets into `% presenter notes:` comments rather than keeping all interpretation on the slide.
- Treat `%GPT:` comments as frame-local editing instructions and apply them only within the tagged frame they belong to.
- If a `GPT-*` tag appears in a comment directly above a frame, treat that frame as tagged.
- If the user provides a rough outline for a new slide, preserve the purpose comment and rewrite the outline into polished slide content.
- When a comment is just a scratch instruction, use it to revise the tagged frame and then remove or shorten it unless the user clearly wants it retained.
- When a comment mixes purpose and editing instructions, preserve the purpose and consume the editing instruction.

If a new slide is created from rough notes, prefer a pattern like:

```tex
% Purpose: Explain why the benchmark estimator fails under selective stopping.
\begin{frame}{Selective Stopping Breaks the Benchmark}
    \begin{itemize}
        \item ...
    \end{itemize}
\end{frame}
```

## Workflow

When revising slides:

1. confirm that the target Beamer `.tex` file is saved on disk; if unsaved editor changes may exist, stop and ask the user to save before proceeding
2. inspect the target Beamer file and locate all frames with `GPT-*` tags, plus their nearby `% message:` comments, `%GPT:` comments, purpose notes, and placeholders
3. set the edit scope to those tagged frames only
4. infer the local editing intent from the `% message:` comment first, then from tags and nearby comments before reading broader project context
5. use the existing deck and any user-provided prior decks as the primary style anchors
6. consult the paper draft only if needed for notation, claims, or terminology
7. for figure or table result slides, prefer a takeaway-style title, keep the visible body to at most two sentences, and move the fuller speaking script into `% presenter notes:` comments
8. for `GPT-N`, turn rough outlines into concise, professional slide writing; for `GPT-GS`, make only light grammar-and-style edits unless the slide is clearly too dense to serve its stated message
9. add a `%revised` comment to every frame that was edited during the task
10. preserve slide purpose comments, `% message:` comments, `% presenter notes:` comments, and `%revised` comments as LaTeX comments directly above or inside the frame where they already belong
11. keep edits local and conservative unless the user explicitly asks for a broader reorganization

## Style guide from prior slides

Use the user's prior decks as the default style reference.

When no stronger local style signal is present, prefer the academic Beamer style reflected in the user's examples:

- `\documentclass[10pt]{beamer}`
- `\usetheme{default}` with `\usecolortheme{orchid}`
- black or near-black frametitle text with a thin horizontal rule below it
- square main bullets, circular sub-bullets, and light use of `\vs`
- top-level claims or explanations often appear without bullet icons, while bullets are mainly used for subordinate structure
- concise, formal slide writing rather than manuscript paragraphs
- generous whitespace and visible margins around the main content rather than densely filling the frame

## Editing rules

- Stop immediately if the target Beamer file may have unsaved editor changes. Ask the user to save first rather than risking an overwrite.
- Edit only frames selected by `GPT-*` tags. Never make opportunistic changes to untagged frames, even for consistency, cleanup, or style matching.
- Preserve the deck's existing preamble, macros, and frame structure unless the requested edit requires changing them.
- Let the `% message:` comment determine the slide's intended takeaway; revise the tagged frame so the visible content supports that message more clearly.
- For `GPT-GS`, prefer a minimal diff and preserve the slide's structure, claims, equations, and ordering unless a tiny local change is needed for correctness or professionalism.
- For `GPT-N`, local restructuring within the tagged frame is allowed if it improves the slide.
- Prefer direct, informative frame titles over vague labels.
- On figure and table result slides, a takeaway-style frame title is often better than a neutral label.
- Keep one main message per slide.
- Do not overcrowd slides. Prefer a slide with breathing room and clear margins over a slide that tries to say everything at once.
- Avoid math-first layouts when revising a slide. If the first visible content under the title is a displayed equation, prefer adding a short lead-in sentence or claim before the equation unless the user clearly wants a math-first presentation.
- For figure and table slides, keep the visible body text to at most two sentences total and move the rest of the interpretation into `% presenter notes:` comments.
- If a sentence wraps and leaves only one or two words on the last line, shorten or rephrase it as part of the revision.
- Every revised frame should include a `%revised` tag near the top of the frame.
- Do not put every sentence in an `itemize` list; when a frame has one main claim plus explanation, prefer a short unbulleted statement, equation, or block.
- Use bullet icons for parallel points or sub-items, and keep such lists short, often two to four items.
- As a house style, text inside `\item` should start with lower case.
- If a tagged frame becomes dense, cut secondary detail, shorten prose, or simplify the structure rather than shrinking margins or packing in more bullets.
- Only add another frame to relieve overcrowding when the user asks for it explicitly or when a `GPT-N` frame clearly calls for a new slide; otherwise keep the revision inside the tagged frame.
- Keep equations only when they are central to the slide's purpose.
- Match notation to the existing deck first, then to the paper if clarification is needed.
- Do not rebuild the whole talk from scratch unless the user explicitly asks.

## Good output standard

A good revision should let the user quickly answer:

- Did the edit follow the tag and any `%GPT:` instruction?
- Does the revised frame now clearly deliver the `% message:` comment?
- Does each edited frame now carry a `%revised` tag?
- Is the new slide professional and presentation-ready?
- Does the slide still have breathing room, with visible margins and non-crowded content?
- Does the slide give the audience verbal orientation before any displayed math, rather than opening the body with notation alone?
- On figure and table slides, is the visible text sparse while the spoken interpretation is preserved in `% presenter notes:` comments?
- Do wrapped sentences avoid one-word or two-word trailing lines when a shorter phrasing would fix the layout?
- Is the slide purpose still visible as a LaTeX comment?
- Does the revised frame match the style of the surrounding deck?

Default to targeted, reusable edits rather than a full deck rewrite.

## Response convention

After finishing a slide-revision task, report in chat which line of the target `.tex` file contains the first revised frame.

- If you stop because the file may have unsaved editor changes, say that clearly in chat and do not report a revised-frame line number.
- If at least one frame was revised, give the path and the line number of the first revised frame in the final response.
- If multiple frames were revised, still report the first one explicitly; additional line references are optional.
- If no frame was revised, say that clearly rather than inventing a line number.

## Boundary with Beamer Slides

Use `beamer-slides` instead when the user wants to create a new deck or initial slide outline from the paper draft.

Use `revise-beamer-slides` when the user already has a deck and wants to work through in-file comments, `GPT-*` tags, purpose notes, or rough slide stubs.

## Example prompt patterns

Use this skill when the user asks things like:

- update this `deliverable/slides/main.tex` using my inline comments
- update only the `GPT-N` and `GPT-GS` frames in `deliverable/slides/main.tex`
- revise tagged frames so they better match the `% message:` comments
- revise tagged frames according to the `%GPT:` comments
- revise these existing slides based on the `% TODO` notes
- add a new slide from the purpose comment and rough outline I left in the file
- rewrite this frame so it sounds more professional but keep the purpose comment
- polish these placeholder bullets inside my current Beamer deck
