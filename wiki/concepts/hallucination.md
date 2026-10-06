---
title: Hallucination
type: concept
tags: [ai-tools, ai-literacy, llm]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]", "[[2026-10-06-claude-101-notes]]", "[[2026-10-06-claude-platform-notes]]"]
related: ["[[ai-fluency]]", "[[retrieval-augmented-generation]]", "[[prompting-fundamentals]]", "[[lightweight-evals]]", "[[ai-fluency-glossary]]"]
confidence: medium
status: seed
---

# Hallucination

An error in which an AI **confidently** states something that sounds plausible but is wrong
([[ai-fluency-vocabulary-cheat-sheet]]). The confidence is the dangerous part: nothing in the
tone signals that the answer is wrong.

## Explanation

**Countermeasures named across sources:**
- **Ground it:** [[retrieval-augmented-generation]] connects the model to external sources "to
  improve accuracy and reduce hallucinations" ([[ai-fluency-vocabulary-cheat-sheet]]). Turning
  on web search does the same for quick facts ([[claude-101-course-notes]]). But grounding is
  not proof: "finding something on the internet doesn't make it true", so double-check Claude's
  searched work too ([[claude-platform-101-course-notes]]).
- **Ask for evidence:** request sources or a confidence level ([[prompting-fundamentals]],
  [[claude-101-course-notes]]).
- **Verify what matters.** This is **Product Discernment** (checking accuracy) and
  **Deployment Diligence** (vouching for what you share) in [[ai-fluency]]. The Claude 101
  table lists "confident but wrong" as a core failure, fixed by verifying
  ([[claude-101-course-notes]]).
- **Know the cutoff:** questions about events after the model's knowledge cutoff invite
  invented answers. Assessment: search, don't trust memory ([[ai-fluency-glossary]]).

## How it connects

- [[lightweight-evals]] find where a task hallucinates before you rely on it.
- Assessment: this KB's rule that every claim cites a raw source is a defence against
  hallucination in the agent's own writing ([[llm-wiki-pattern]]).

## Contradictions & open questions

- Neither source explains *why* models hallucinate. A technical source would fill that gap.

## Sources

- [[ai-fluency-vocabulary-cheat-sheet]]
- [[claude-101-course-notes]]
- [[claude-platform-101-course-notes]]
