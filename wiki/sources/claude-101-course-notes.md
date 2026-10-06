---
title: "Claude 101 — course notes (Anthropic Academy)"
type: source
tags: [ai-tools, claude, prompting, productivity]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[claude]]", "[[prompting-fundamentals]]", "[[ai-fluency]]", "[[claude-projects]]", "[[claude-skills]]", "[[claude-connectors]]", "[[claude-artifacts]]", "[[choosing-a-claude-surface]]"]
confidence: medium
status: seed
author: the user (own notes on Anthropic's "Claude 101" course)
published: unknown (course date not recorded; notes saved 2026-10-06)
url: n/a (Anthropic Academy on Skilljar; exact course URL not recorded)
source_type: note
---

# Claude 101 — course notes (Anthropic Academy)

The user's own notes on Anthropic Academy's **Claude 101** course (12 lessons, taken in one
sitting, "some bits are rushed"). The notes cover what [[claude]] is, how to prompt and iterate,
the feature set ([[claude-projects]], [[claude-artifacts]], [[claude-skills]],
[[claude-connectors]], enterprise search, Research) and the product surfaces
([[claude-cowork]], [[claude-code]], [[claude-in-chrome]], Claude Tag, Claude Design, Claude for
M365). It is the KB's first source on *using* AI tools, as distinct from the
[[llm-wiki-pattern]], which is about *building with* them.

## Key claims

- Claude is positioned as a "thinking partner", trained with Constitutional AI, and
  "steerable" on tone and behaviour. Its context window is 200K+ tokens (~500 pages), or 1M on
  paid plans with supported models ([[claude]]).
- A good prompt has three parts: **set the stage → define the task → specify rules**.
  Iteration (follow-ups, feedback, redirects, a fresh chat) is "the main point really"
  ([[prompting-fundamentals]]).
- The 3-part prompt is the *Description* D of the **4D AI Fluency framework** (Dakan + Feller):
  Delegation, Description, Discernment, Diligence ([[ai-fluency]]).
- Evals need no tooling: take 5–10 past examples of a task, prompt for the same thing, compare
  the results, then adjust ([[lightweight-evals]]).
- Desktop work comes in three shapes: turn-by-turn → Chat, hand-off → [[claude-cowork]],
  building software → the Code tab ([[claude-code]]) ([[choosing-a-claude-surface]]).
- Projects switch to **RAG automatically** near the context limit, which gives ~10x capacity.
  File names matter because Claude uses them to find documents ([[claude-projects]]).
- "Projects = knowledge (the what), skills = process (the how)", and the two stack
  ([[claude-skills]], [[claude-projects]]).
- Connectors are built on [[model-context-protocol]]. Claude sees only what the connecting
  user can see ([[claude-connectors]]).
- Pick the tool by the question: Research for multi-step reports, web search for quick facts,
  Thinking for pure reasoning, enterprise search ("Ask {Org}") for internal knowledge
  ([[choosing-a-claude-surface]]).
- Ask for the **deliverable**, not the content ("make a 1-pg doc for leadership" rather than
  "summarise Q3") ([[claude-artifacts]]).

## Notable quotes

> conversation = where you make it, artifacts tab = where it lives

> projects = knowledge (the what) · skills = process (the how)

> am i feeding whole tasks to it one question at a time just out of habit?? probably yes
> *(the user's own reflection)*

## Assessment

These are a learner's notes on vendor training material. They are reliable as a record of
what the course teaches, but the course is Anthropic describing its own product. Plan
availability, beta labels and limits (context sizes, the ~10x RAG figure, which plans get
which feature) are **time-sensitive** and should be treated as of the course date (confidence
medium). The durable content is the method: the prompt structure, iterating, the 4Ds,
lightweight evals, and picking the surface by the shape of the work.

**Links to the existing wiki:** the projects-vs-skills split mirrors this KB's own wiki
(knowledge) vs. `CLAUDE.md` schema (process) ([[llm-wiki-pattern]]). Projects' automatic
switch to RAG is a working example of the hybrid that [[retrieval-augmented-generation]]
anticipates.

**What the user flagged for themselves:** try Claude on 2–3 calendar items; status reports
and decoding an inherited spreadsheet are the most useful role use cases; take the final quiz
for the certificate.

## Wiki changes

- Created: [[claude]], [[claude-code]], [[claude-cowork]], [[claude-in-chrome]],
  [[model-context-protocol]], [[prompting-fundamentals]], [[ai-fluency]],
  [[lightweight-evals]], [[claude-projects]], [[claude-skills]], [[claude-connectors]],
  [[claude-artifacts]], [[choosing-a-claude-surface]]
- Updated: [[retrieval-augmented-generation]] (Projects' automatic RAG fallback),
  [[llm-wiki-pattern]] (knowledge-vs-process parallel; the KB runs on Claude Code),
  [[overview]], [[index]]

## Raw

[[2026-10-06-claude-101-notes]]
