---
title: Lightweight evals
type: concept
tags: [ai-tools, evaluation, prompting]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]", "[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]"]
related: ["[[prompting-fundamentals]]", "[[ai-fluency]]"]
confidence: medium
status: seed
---

# Lightweight evals

A tooling-free way to test whether an AI can handle a task you already do: compare its output
with your own past work on the same inputs.

## Explanation

Steps ([[claude-101-course-notes]]):
1. Collect 5–10 examples of a task you already do.
2. Write prompts that should produce something similar.
3. Compare: is the key information there, is the tone right, what is missing?
4. Adjust the prompts, add examples, and decide where human review stays mandatory.

*Example from the course:* re-run a dataset you already analysed by hand. Claude "maybe gets
the numbers right but misses the bigger patterns" ([[claude-101-course-notes]]).

## How it connects

- Tests the prompts built with [[prompting-fundamentals]].
- In [[ai-fluency]] terms, this is **Product Discernment** made systematic (accuracy,
  appropriateness, coherence, relevance), feeding **Task Delegation**: what to hand off and
  where review stays mandatory ([[ai-fluency-vocabulary-cheat-sheet]]).
- A cheap way to find where a task [[hallucination|hallucinates]].
- Could be applied to this KB: re-ingest a source and compare the result with the existing
  pages. (Assessment; not tried.)

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-101-course-notes]]
- [[ai-fluency-vocabulary-cheat-sheet]]
