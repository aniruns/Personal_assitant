---
title: "AI Fluency: Key Terminology Cheat Sheet"
type: source
tags: [ai-tools, ai-literacy, glossary]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]"]
related: ["[[ai-fluency]]", "[[ai-fluency-glossary]]", "[[human-ai-interaction-modes]]", "[[prompting-fundamentals]]", "[[hallucination]]", "[[retrieval-augmented-generation]]"]
confidence: high
status: seed
author: Rick Dakan, Joseph Feller, and Anthropic
published: 2025 (copyright year; exact date not given)
url: n/a (PDF supplied by the user; presumably from Anthropic's AI Fluency course materials, not verified)
source_type: article
---

# AI Fluency: Key Terminology Cheat Sheet

A two-page Anthropic glossary, © 2025 Rick Dakan, Joseph Feller and Anthropic, released under
CC BY-NC-SA 4.0. It defines about 45 terms in four groups: the **AI Fluency framework** (the
4Ds and their 12 sub-competencies), **human–AI interaction modes**, **AI technical concepts**
and **prompt-engineering concepts**. The user saved it in order to learn the vocabulary;
every term is compiled into [[ai-fluency-glossary]], which is set up for self-testing.

## Key claims

- **AI Fluency** is "the ability to work with AI systems in ways that are effective, efficient,
  ethical, and safe" ([[ai-fluency]]).
- Each of the 4Ds splits into three sub-competencies ([[ai-fluency]]):
  - **Delegation:** Problem, Platform and Task awareness/delegation.
  - **Description:** Product, Process, Performance.
  - **Discernment:** Product, Process, Performance (the same three lenses, turned to evaluation).
  - **Diligence:** Creation, Transparency, Deployment.
- There are three modes of human–AI interaction: **Automation** (AI executes specified tasks),
  **Augmentation** (thinking partners iterating together) and **Agency** (AI configured to act
  independently on your behalf) ([[human-ai-interaction-modes]]).
- **Hallucination** is AI confidently stating something plausible but incorrect. **RAG**
  connects models to external knowledge to improve accuracy and reduce hallucinations
  ([[hallucination]], [[retrieval-augmented-generation]]).
- **Scaling laws** are an *empirical observation*, and new capabilities can emerge at scale
  thresholds without being explicitly programmed ([[ai-fluency-glossary]]).
- **Fine-tuning** is described as the stage where models learn to follow instructions, be
  helpful and avoid harmful content ([[ai-fluency-glossary]]).
- Prompt techniques named: chain-of-thought, few-shot (n-shot), role/persona, output
  constraints, think-first ([[prompting-fundamentals]]).

## Notable quotes

> "Higher" temperature produces more varied and creative outputs (think boiling water
> bubbling), while "lower" temperature produces more predictable and focused responses (think
> ice crystals).

> The human establishes the AI's knowledge and behavior patterns rather than specifying exact
> actions. *(on Agency)*

## Assessment

This is a primary source for the framework, written by its authors, so confidence is high for
the definitions. It is a glossary, though, not an argument: it says *what* each term means,
not how to practise it. The technical definitions are deliberately simplified for a
non-technical audience. For example, "Fine-tuning" folds instruction tuning and safety
training into one step, and "Neural networks" stays at an analogy.

**What it changes in the wiki:**
- Resolves the open question on [[ai-fluency]]: the authors' full names are now known, and
  the framework is no longer known only second-hand.
- Gives the wiki's existing advice proper names. Claude 101's "show an example" is
  **few-shot prompting**; "tone, format, length" splits into **output constraints** (product
  description) and **performance description**; Claude's "Thinking" is a **reasoning model**
  ([[prompting-fundamentals]]).
- Its interaction modes map onto the surfaces in [[choosing-a-claude-surface]]. This mapping
  is my assessment; the sheet doesn't make it: Chat ≈ augmentation, [[claude-cowork]] and
  [[claude-code]] lean towards agency.
- Its RAG definition (accuracy and grounding) is a different angle from the wiki's (RAG as
  the stateless foil to compiling). These are complementary, not contradictory
  ([[retrieval-augmented-generation]]).

## Wiki changes

- Created: [[ai-fluency-vocabulary-cheat-sheet]], [[ai-fluency-glossary]],
  [[human-ai-interaction-modes]], [[hallucination]]
- Updated: [[ai-fluency]] (12 sub-competencies, authors, interaction modes; → growing,
  confidence high), [[prompting-fundamentals]] (technique vocabulary), [[lightweight-evals]]
  (as product discernment), [[retrieval-augmented-generation]] (grounding definition),
  [[context-management]] (formal definition), [[claude]] (LLM family, knowledge cutoff,
  reasoning models), [[choosing-a-claude-surface]] (interaction modes), [[overview]],
  [[index]]

## Raw

[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]] (PDF, 2 pages)
