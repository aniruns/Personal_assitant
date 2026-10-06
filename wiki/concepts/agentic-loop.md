---
title: Agentic loop
type: concept
tags: [ai-tools, llm-agents, claude]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]", "[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude-code]]", "[[context-management]]", "[[subagents]]", "[[explore-plan-code-commit]]", "[[claude-cowork]]", "[[tool-use]]", "[[who-runs-the-agent-loop]]", "[[claude-managed-agents]]"]
confidence: medium
status: growing
---

# Agentic loop

An agent is **an LLM running in a loop** that can use tools, external services or other agents
to reach a goal ([[claude-code-101-course-notes]]): **observe → decide → act → repeat**, with
no human needed in the middle ([[claude-platform-101-course-notes]]). The loop is what separates
[[claude-code]] (and [[claude-cowork]]) from text-in, text-out chat, and it is the same loop
whether you write it yourself on the [[claude-platform]] or use a finished product.

## Explanation

- **The loop:** prompt → **gather context** (search and read files) → **take action** (edit
  files, run commands) → **verify** → either done or around again
  ([[claude-code-101-course-notes]]).
- **The loop in code** ([[claude-platform-101-course-notes]]):
  1. Send messages and the available tools to Claude.
  2. Claude replies with a final answer or a request to use a [[tool-use|tool]].
  3. **Your code** runs the tool and sends the result back as a `tool_result`.
  4. Repeat while `stop_reason == "tool_use"`; stop at `end_turn`.
- **Ownership split:** "You own the loop and the tools. Claude owns the reasoning." The same loop
  runs a toy weather demo and a production compliance agent; only the tools and plumbing change
  ([[claude-platform-101-course-notes]]). How much of the loop you hand over is
  [[who-runs-the-agent-loop]].
- **Tools are the backbone.** They let the model *do* things instead of only producing text
  ([[claude-code-101-course-notes]]).
- **The human stays in the loop.** You can interrupt, steer or add context at any point.
  Permission modes control how often the agent stops to ask: default, auto accept or plan
  ([[claude-code]]).
- **Context is the constraint.** Each pass adds file reads, tool calls and results to the
  context window. Near the limit the agent auto-compacts ([[context-management]]).
- **Failure modes:** it can misread intent, introduce bugs or over-engineer. "Stay in the loop"
  ([[claude-code-101-course-notes]]).

## How it connects

- [[explore-plan-code-commit]] — a human-level workflow wrapped around the loop that front-loads
  the cheap "gather context" phase.
- [[subagents]] — the loop can spawn other loops with their own context; this is the "other
  agents" part of the definition.
- Verification works best when the agent has something objective to check against, such as
  tests or a browser via [[claude-in-chrome]] ([[explore-plan-code-commit]]).
- Assessment: this KB's ingest operation is the same loop. Read the source (gather), write the
  pages (act), run `scripts/lint.py` (verify) ([[llm-wiki-pattern]]).

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-code-101-course-notes]]
- [[claude-platform-101-course-notes]]
