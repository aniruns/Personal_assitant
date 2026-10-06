---
title: AI Fluency (the 4Ds)
type: concept
tags: [ai-tools, ai-literacy, mental-model]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[prompting-fundamentals]]", "[[lightweight-evals]]", "[[claude]]"]
confidence: medium
status: seed
---

# AI Fluency (the 4Ds)

A framework by Dakan and Feller for working with AI effectively and responsibly, in four
competencies. Anthropic's Claude 101 course uses it as the backbone of its prompting advice.

## Explanation

The four Ds ([[claude-101-course-notes]]):

- **Delegation:** decide what the human should do and what the AI should do.
- **Description:** communicate clearly. This is the 3-part prompt in
  [[prompting-fundamentals]].
- **Discernment:** judge the output critically. Verify anything that matters. The user marked
  this one "!!" in their tl;dr.
- **Diligence:** use AI responsibly and ethically, and own the result.

A free "AI Fluency" course covers it in more depth ([[claude-101-course-notes]]).

**Assessment:** Delegation and Discernment are where [[lightweight-evals]] fit. Evals tell you
which parts of a task to delegate and where human review is still required. This KB's own
rules, such as "attribute every claim" and "never present inference as fact", are Diligence and
Discernment applied to the agent's writing ([[llm-wiki-pattern]]).

## How it connects

- [[prompting-fundamentals]]: the Description practice.
- [[lightweight-evals]]: the Discernment practice.

## Contradictions & open questions

- Known only second-hand through the course. The original AI Fluency material by Dakan and
  Feller has not been ingested, and first names and publication details are not recorded.

## Sources

- [[claude-101-course-notes]]
