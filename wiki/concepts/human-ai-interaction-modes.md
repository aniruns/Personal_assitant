---
title: Human–AI interaction modes
type: concept
tags: [ai-tools, ai-literacy, mental-model]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]"]
related: ["[[ai-fluency]]", "[[choosing-a-claude-surface]]", "[[agentic-loop]]", "[[claude-cowork]]", "[[claude-code]]", "[[ai-fluency-glossary]]"]
confidence: medium
status: seed
---

# Human–AI interaction modes

The AI Fluency framework's three ways a human and an AI can work together: **Automation,
Augmentation and Agency** ([[ai-fluency-vocabulary-cheat-sheet]]). They differ in who decides
the steps, and that tells you how much Delegation and Discernment the work needs.

## Explanation

| Mode | Who decides the steps | Definition ([[ai-fluency-vocabulary-cheat-sheet]]) |
|---|---|---|
| **Automation** | the human, fully | AI performs specific tasks from specific human instructions; the human defines what is done, the AI executes |
| **Augmentation** | both, iteratively | human and AI collaborate as thinking partners; back-and-forth where both contribute |
| **Agency** | the AI, within configured patterns | the human configures AI to work independently on their behalf, including interacting with other humans or AIs; sets knowledge and behaviour patterns, not exact actions |

## How it connects

- **Claude surfaces (assessment):** the "shapes of work" in [[choosing-a-claude-surface]] line
  up with these modes. Turn-by-turn Chat is augmentation. Hand-offs to [[claude-cowork]] and
  [[claude-code]] running its [[agentic-loop]] lean towards agency. Scheduled tasks and
  [[subagents]] are agency in its fullest form.
- **Configuring agency:** the sheet says that under Agency the human sets "knowledge and
  behaviour patterns". In Claude Code those patterns are [[claude-md]], skills and hooks
  ([[claude-code-extension-points]]). This KB is an instance: `CLAUDE.md` configures an agent
  that maintains the wiki on the user's behalf ([[llm-wiki-pattern]]). This is an assessment.
- **Which Ds matter most (assessment):** Description dominates in automation, Discernment in
  augmentation, and Delegation and Diligence in agency, because you aren't watching each step.
- The user's own Claude 101 reflection ("feeding whole tasks to it one question at a time")
  amounts to using augmentation where agency would do ([[claude-101-course-notes]]).

## Contradictions & open questions

- The sheet gives definitions only. Whether the modes form a progression or a menu, and how
  the 4Ds apply under each, is not stated.

## Sources

- [[ai-fluency-vocabulary-cheat-sheet]]
