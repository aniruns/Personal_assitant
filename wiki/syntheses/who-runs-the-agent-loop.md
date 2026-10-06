---
title: Who runs the agent loop — from your own while-loop to managed agents
type: synthesis
tags: [ai-tools, claude, llm-agents, decision-guide]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-platform-notes]]", "[[2026-10-06-claude-code-101-notes]]", "[[2026-10-06-claude-101-notes]]"]
related: ["[[agentic-loop]]", "[[tool-use]]", "[[claude-managed-agents]]", "[[claude-platform]]", "[[claude-code]]", "[[claude-cowork]]", "[[choosing-a-claude-surface]]", "[[human-ai-interaction-modes]]"]
confidence: medium
status: seed
question: "Every Claude agent is the same loop — so what actually differs between building one myself, using the tool runner, managed agents, Claude Code and Cowork?"
---

# Who runs the agent loop

Every Claude agent is the same [[agentic-loop]]: Claude picks a tool, something runs it, the
result goes back, repeat until done. What differs is **who owns the loop, the tools and the
sandbox**. The Platform course frames this as a spectrum (manual loop → tool runner → managed
agents) ([[claude-platform-101-course-notes]]). Assessment: [[claude-code]] and
[[claude-cowork]] are the same loop, already built by Anthropic and run on your machine, so
they sit on the same spectrum.

## Analysis

| Option | Who runs the loop | Who runs the tools | Where it runs | You get | You give up |
|---|---|---|---|---|---|
| **Manual loop** (`while stop_reason == "tool_use"`) | your code | your code | your servers | full control of every step | you write schemas, dispatch, retries |
| **SDK tool runner** | the SDK, in your process | your real functions | your servers | no loop or schema boilerplate | fine-grained control between steps |
| **Server tools only** (web search, fetch, code exec) | none needed — one response | Anthropic | Anthropic | zero plumbing | limited to Anthropic's tools |
| **[[claude-managed-agents]]** | Anthropic | Anthropic's bundled toolset + MCP | isolated Anthropic container | long runs, resilience, caching and compaction by default, graders | the loop, the sandbox, resumability; you consume events |
| **[[claude-code]] / [[claude-cowork]]** | Anthropic's client app | built-in tools + MCP + your hooks | your machine (or cloud for Claude Code web) | a finished agent; you steer it in real time | building your own product on it |

Sources: rows 1–4 from [[claude-platform-101-course-notes]]; row 5 from
[[claude-code-101-course-notes]] and [[claude-101-course-notes]].

**Across all rows, the same split holds:** "You own the loop and the tools. Claude owns the
reasoning" ([[claude-platform-101-course-notes]]). Moving down the table hands more of the
"you own" side to Anthropic.

## Implications / so what

- **Pick by run length and control:** a short, product-embedded task → tool runner; a long,
  multi-tool, must-survive-failures job → managed agents; interactive work at your desk →
  Claude Code or Cowork.
- **Human-in-the-loop moves around.** In Claude Code you steer live (permission modes); in
  managed agents a **permissions policy** holds actions for approval; in a manual loop you
  write the gate yourself. Assessment: these are the same control expressed at three levels,
  and it maps onto the [[human-ai-interaction-modes]] (augmentation → agency).
- **Definitions of "done" move too:** `stop_reason == "end_turn"` in a manual loop; a
  rubric + grader in managed agents; tests and success criteria in
  [[explore-plan-code-commit]].
- **This KB** is the bottom row: Claude Code runs the loop, `CLAUDE.md` is the system prompt,
  and `scripts/lint.py` is the verifier ([[llm-wiki-pattern]]).

## Contradictions & open questions

- Where the Claude Agent SDK (the library under Claude Code) fits isn't in any source yet;
  it would sit between the tool runner and Claude Code.
- No source compares the cost of the options.

## Draws on

- [[claude-platform-101-course-notes]], [[claude-code-101-course-notes]],
  [[claude-101-course-notes]], [[agentic-loop]], [[tool-use]], [[claude-managed-agents]],
  [[claude-code]], [[claude-cowork]]
