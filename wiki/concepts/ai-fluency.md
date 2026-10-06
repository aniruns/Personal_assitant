---
title: AI Fluency (the 4Ds)
type: concept
tags: [ai-tools, ai-literacy, mental-model]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]", "[[2026-10-06-claude-101-notes]]"]
related: ["[[ai-fluency-glossary]]", "[[human-ai-interaction-modes]]", "[[prompting-fundamentals]]", "[[lightweight-evals]]", "[[hallucination]]", "[[claude]]"]
confidence: high
status: growing
---

# AI Fluency (the 4Ds)

Rick Dakan and Joseph Feller's framework (with Anthropic, 2025) for "the ability to work with
AI systems in ways that are effective, efficient, ethical, and safe"
([[ai-fluency-vocabulary-cheat-sheet]]). It has four competencies, each with three
sub-competencies. Anthropic's Claude 101 course builds its prompting advice on it
([[claude-101-course-notes]]). For every term and a self-test, see [[ai-fluency-glossary]].

## Explanation

The 4Ds and their sub-competencies ([[ai-fluency-vocabulary-cheat-sheet]]):

- **Delegation**: what humans do, what AI does, how to split it.
  - *Problem Awareness*: understand the goal and the work before involving AI.
  - *Platform Awareness*: know what different AI systems can and can't do.
  - *Task Delegation*: distribute work to use each side's strengths.
- **Description**: communicating effectively with AI.
  - *Product*: what you want (output, format, audience, style).
  - *Process*: how the AI should approach it.
  - *Performance*: how it should behave during the collaboration.
- **Discernment**: critically evaluating what the AI does.
  - *Product*: quality of the output (accuracy, appropriateness, coherence, relevance).
  - *Process*: how it got there (logic errors, lapses, bad reasoning steps).
  - *Performance*: whether its interaction style works for you.
- **Diligence**: using AI responsibly and ethically.
  - *Creation*: which systems you use and how.
  - *Transparency*: being honest about AI's role with everyone who needs to know.
  - *Deployment*: verifying and vouching for outputs you use or share.

**Structure worth noticing:** Description and Discernment mirror each other along
Product / Process / Performance, one going in and one coming out.

**Interaction modes.** The framework also distinguishes **Automation, Augmentation and
Agency** by how much the AI decides the steps ([[human-ai-interaction-modes]]).

**In the Claude 101 course:** Description is taught as the 3-part prompt
([[prompting-fundamentals]]), and Discernment as "verify anything that matters". The user
marked Discernment "!!" in their tl;dr ([[claude-101-course-notes]]).

**Assessment:** [[lightweight-evals]] are Product Discernment done systematically, and they
inform Task Delegation: which parts to hand off, and where human review stays. Checking
outputs against [[hallucination]] is Product Discernment plus Deployment Diligence. This KB's
rules, such as "attribute every claim" and "never present inference as fact", are Diligence
and Discernment applied to the agent's own writing ([[llm-wiki-pattern]]).

## How it connects

- [[prompting-fundamentals]]: Description in practice. Stage/task/rules map onto Product and
  Performance Description; the prompt-engineering techniques are in [[ai-fluency-glossary]].
- [[lightweight-evals]]: Discernment in practice.
- [[human-ai-interaction-modes]]: the other half of the framework's vocabulary.
- [[choosing-a-claude-surface]]: Platform Awareness, applied to Claude's surfaces.

## Contradictions & open questions

- Only the glossary and course notes have been ingested; the full AI Fluency course has not.
  How the 4Ds weigh differently under each interaction mode is not stated.

## Sources

- [[ai-fluency-vocabulary-cheat-sheet]]
- [[claude-101-course-notes]]
