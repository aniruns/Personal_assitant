---
title: Context management
type: concept
tags: [ai-tools, claude, llm-agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]", "[[2026-10-06-claude-101-notes]]", "[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]", "[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude-code]]", "[[subagents]]", "[[claude-md]]", "[[model-context-protocol]]", "[[claude-skills]]", "[[agentic-loop]]", "[[claude-platform]]", "[[claude-managed-agents]]"]
confidence: medium
status: growing
---

# Context management

The context window is the agent's **working memory**, and it is finite
([[claude-code-101-course-notes]]). Formally, it is "the amount of information an AI can
consider at one time, including the conversation history and any documents you've shared",
with a maximum that varies by model ([[ai-fluency-vocabulary-cheat-sheet]]). On the API it
is also a bill: you pay for it **on every call**, and when the window is full **the request
fails**. "The goal isn't to fit everything in. It's to fit the right things in"
([[claude-platform-101-course-notes]]). Most practical advice about [[claude-code]] comes down
to the same thing.

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

**On the API** — what counts: system prompt, message history, tool definitions and results,
files, skills and thinking blocks. Four patterns, usually layered together in production
([[claude-platform-101-course-notes]]):

| # | Pattern | What it does | Fixes |
|---|---|---|---|
| 1 | **Just-in-time context** (a design choice) | load only what's needed now; let tools fetch the rest | window size |
| 2 | **Server-side compaction** | `context_management={"edits":[{"type":"compact"}]}` auto-summarises old turns past a threshold | long conversations |
| 3 | **Prompt caching** | cache stable parts (system prompt, tools, long docs) and reuse them cheaply | cost |
| 4 | **Memory tool** | Claude reads and writes a memory directory; **you** own the storage backend | statelessness across sessions |

[[claude-managed-agents]] turn caching and compaction on by default. Scoping an MCP server to a
few tools also saves context ([[model-context-protocol]]).

Assessment: the API patterns map onto Claude Code's: server-side compaction ≈ auto-compaction /
`/compact`; just-in-time ≈ selective repo search and skills' progressive loading; the memory
tool ≈ [[claude-md]].

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
- [[claude-platform-101-course-notes]] (API patterns)
