---
title: Prompting fundamentals
type: concept
tags: [ai-tools, prompting]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[ai-fluency]]", "[[lightweight-evals]]", "[[claude]]", "[[claude-artifacts]]"]
confidence: medium
status: seed
---

# Prompting fundamentals

How to ask an AI assistant for work and get it back right: a three-part prompt followed by
deliberate iteration. This is the practical core of the *Description* D in [[ai-fluency]].

## Explanation

**Talk to it like a coworker:** natural and concise, with no magic words needed
([[claude-101-course-notes]]).

**Three-part prompt** ([[claude-101-course-notes]]):
1. **Set the stage.** Who you are, the goal, relevant context.
2. **Define the task.** What it should *do* (write, analyse, build…).
3. **Specify rules.** Tone, format, length, examples.

*Course example:* a marketing lead at an indie streaming startup asks for market research
for a Series A deck, with citations, as a 5-page report with an executive summary. The
example covers all three parts.

**Common failures and fixes** ([[claude-101-course-notes]]):

| Problem | Fix |
|---|---|
| Too generic | Add context: audience, constraints, history |
| Wrong length | State it ("2 paras", "<100 words") |
| Ignored format | **Show** an example; don't only describe it |
| Confident but wrong | Verify what matters; ask for sources or confidence; turn on web search |
| Wrong tone | Describe it in plain words and give a sample |

**Iteration is "the main point"** ([[claude-101-course-notes]]):
- The first draft is a starting point.
- Specific feedback beats vague feedback: "cut the first 2 paras, end on an action" works
  better than "shorter".
- Moves: follow up, give feedback, redirect, or edit and resend your message (pencil icon).
  If it has gone off the rails, start a new chat with fresh context.

**Ask for the deliverable, not the content.** "Make a 1-page doc for leadership" works better
than "summarise Q3". Say who it is for, and build the deliverable at the *end* of a
conversation, once the context is established ([[claude-artifacts]], [[claude-101-course-notes]]).

**Standing context** reduces how much each prompt has to carry: account-wide instructions,
memory, [[claude-projects]] instructions and [[claude-skills]] ([[claude-101-course-notes]]).

## How it connects

- [[ai-fluency]]: the broader framework this belongs to.
- [[lightweight-evals]]: how to check whether a prompt is good enough.
- `CLAUDE.md` in this KB is standing context of the same kind, set once for every session
  ([[llm-wiki-pattern]]).

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-101-course-notes]]
