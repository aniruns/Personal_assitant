---
title: Context management (Claude Code)
type: concept
tags: [ai-tools, claude, llm-agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]", "[[2026-10-06-claude-101-notes]]", "[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]"]
related: ["[[claude-code]]", "[[subagents]]", "[[claude-md]]", "[[model-context-protocol]]", "[[claude-skills]]", "[[agentic-loop]]"]
confidence: medium
status: seed
---

# Context management (Claude Code)

The context window is the agent's **working memory**, and it is finite
([[claude-code-101-course-notes]]). Formally, it is "the amount of information an AI can
consider at one time, including the conversation history and any documents you've shared",
with a maximum that varies by model ([[ai-fluency-vocabulary-cheat-sheet]]). Most practical advice about [[claude-code]] comes down to
keeping that memory full of what matters.

## Explanation

**What uses up context:** prompts, file reads, tool calls and their results. Tool definitions
count too: MCP tools sit in context even when unused. Claude Code searches the repo
selectively instead of loading all of it ([[claude-code-101-course-notes]]). The raw window is
200K+ tokens, or 1M on some paid plans ([[claude]]).

**Commands** ([[claude-code-101-course-notes]]):

| Command | Effect | When |
|---|---|---|
| auto-compaction | Summarizes the session and drops clutter near the limit; **can lose details** | automatic |
| `/compact` | Summarizes what has happened so far and carries on | same task, running out of room |
| `/clear` | Wipes the session | new task; avoids bias from the old one |
| `/context` | Shows what is using space, with a breakdown graphic | diagnosing |

**Tips** ([[claude-code-101-course-notes]]):
- **Be specific.** A vague prompt looks small but costs more, because Claude explores and
  reasons more to fill the gaps.
- **Turn off unused MCP servers.** If a CLI exists (gh, aws), it is cheaper than the MCP server.
  If MCP tools exceed ~10% of context, Claude Code switches to on-demand tool search, which is
  less reliable ([[model-context-protocol]]).
- **Prefer skills.** Only a skill's name and description sit in context; the body loads when
  needed ([[claude-skills]]).
- **Delegate "just give me the answer" tasks to [[subagents]]**, e.g. "where are the auth
  endpoints?" The subagent does the digging and returns only a summary.
- **Persist cross-session knowledge in [[claude-md]]**, not in a long-running chat.

## How it connects

- [[claude-code-extension-points]] ranks every way of adding behaviour by its context cost.
- Assessment: the same pressure drives this KB's design. `index.md` lets the agent read a
  catalogue instead of every page, and the compiled wiki means a query doesn't have to re-read
  raw sources ([[llm-wiki-pattern]]). [[claude-projects]]' automatic RAG switch is the claude.ai
  answer to the same constraint.

## Contradictions & open questions

- Exactly what auto-compaction keeps and drops isn't documented in the notes.

## Sources

- [[claude-code-101-course-notes]]
- [[claude-101-course-notes]] (context-window size)
- [[ai-fluency-vocabulary-cheat-sheet]] (definition)
