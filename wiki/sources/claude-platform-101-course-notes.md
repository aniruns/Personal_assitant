---
title: "Claude Platform 101 — course notes"
type: source
tags: [ai-tools, claude, api, agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude-platform]]", "[[tool-use]]", "[[agentic-loop]]", "[[model-selection]]", "[[extended-thinking]]", "[[claude-managed-agents]]", "[[context-management]]", "[[who-runs-the-agent-loop]]"]
confidence: medium
status: seed
author: the user (own notes on a "Claude Platform 101" course)
published: unknown (course date not recorded; notes saved 2026-10-06)
url: n/a (Anthropic Academy on Skilljar, per the notes' own header)
source_type: note
---

# Claude Platform 101 — course notes

The user's notes on **Claude Platform 101**, an Anthropic Academy (Skilljar) course of 13
lessons plus a quiz. It is the developer-side sequel to [[claude-101-course-notes]] (chat
surfaces) and [[claude-code-101-course-notes]] (the coding agent). The course follows one
arc: a single API call → [[tool-use|tools]] → the [[agentic-loop|agent loop]] → [[extended-thinking|thinking]],
built-in tools, [[claude-skills|skills]] and [[model-context-protocol|MCP]] →
[[context-management]] → [[claude-managed-agents]], with [[claude-code]] writing most of the
code. Unlike the earlier notes, these are tidy and include code. The header itself warns that
model names and beta strings change over time.

## Key claims

- The [[claude-platform]] is Anthropic's infrastructure for using Claude **from code**: REST
  API, SDKs, CLIs and the Console. It has three layers: **primitives** (Messages API, tools,
  files, web search, code execution, MCP, skills), **infrastructure** (managed agents, retries,
  queues, observability) and **controls** (dashboards, evals). Course shorthand: *build with
  primitives, scale on infrastructure, run with control.*
- The goal is "not a chatbot" but Claude wired into an existing product, such as a "Draft
  reply" button in a help desk ([[claude-platform]]).
- Every call needs `model`, `max_tokens` and `messages`, plus an optional `system` prompt. The
  response is a **list of typed blocks** (text, tool calls, thinking), not a string
  ([[claude-platform]]).
- **The right model is the cheapest one whose output you'd actually ship.** Test 20–30 real
  examples on Haiku first and move up only if needed. In a real app, route each task to its own
  model ([[model-selection]]).
- An agent is Claude in a loop: **observe → decide → act → repeat**. You loop while
  `stop_reason == "tool_use"` and stop at `end_turn`. "You own the loop and the tools. Claude
  owns the reasoning" ([[agentic-loop]]).
- **Claude decides when to call a tool; your code runs it.** Vague tool descriptions are "the #1
  reason agents misfire". The SDK's tool runner builds schemas from real functions and runs the
  loop for you ([[tool-use]]).
- **Adaptive thinking** has no token budget. Depth is set by `output_config.effort`, not next
  to `thinking`. Use it for hard reasoning, not classification or extraction
  ([[extended-thinking]]).
- **Server tools** (web search, web fetch, code execution) are run by Anthropic and need no
  loop. **Client tools** (memory, bash) run in your environment with an SDK-supplied schema
  ([[tool-use]]).
- "**Tools = your stuff · Skills = your processes · MCP = everyone else's stuff**." MCP's
  selling point is that the *provider* maintains the integration ([[model-context-protocol]],
  [[claude-skills]]).
- Context is paid for on **every call**, and a full window makes the request **fail**. Layer
  four patterns: just-in-time loading, server-side compaction, prompt caching and the memory
  tool ([[context-management]]).
- [[claude-managed-agents]]: Anthropic hosts the loop in an isolated container. The primitives
  are **Agent → Environment → Session → Events**. Open the event stream *before* the kickoff
  message. "You define what 'done' looks like. Claude works until it gets there."
- With Claude Code, a good prompt names **the file, the pattern and the end state**: "Stub the
  file, delegate it, review the diff" ([[claude-code]]).

## Notable quotes

> You own the loop and the tools. Claude owns the reasoning.

> the right model is the **cheapest one whose output you'd actually ship.**

> Tools = your stuff · Skills = your processes · MCP = everyone else's stuff

> finding something on the internet doesn't make it true.

## Assessment

These are clean, well-structured notes on vendor training. The mechanics are concrete
(parameter names, stop reasons, event names, gotchas). Model names (Fable, Opus 4.7,
`claude-haiku-4-5`), beta headers and the "on by default" status of managed agents are
**time-sensitive**, as the notes themselves warn.

**What's new to the wiki:** the whole API layer. Until now the wiki only knew Claude through
products (chat, Cowork, Claude Code). The most durable idea is the **spectrum of who runs the
loop**: your own `while` loop → the SDK tool runner → managed agents, with Claude Code and
Cowork as Anthropic-built loops on your machine. That is now its own synthesis,
[[who-runs-the-agent-loop]].

**Fit with the existing wiki:**
- *Confirms:* the agent = LLM-in-a-loop definition ([[claude-code-101-course-notes]]); skills'
  progressive loading; MCP's context cost (here also fixable by enabling only some tools).
- *Extends:* [[context-management]] gets four API-side patterns; [[hallucination]] gets the
  warning that search grounding isn't proof; [[claude-skills]] gets the API route.
- *Tension:* 20–30 test examples for model choice vs. 5–10 for [[lightweight-evals]]
  ([[claude-101-course-notes]]). They serve different purposes; flagged on both pages.

**Links to this KB:** the KB is already a hand-run agent loop. The memory tool ("you own the
storage backend") is close to what `wiki/` is for this agent ([[llm-wiki-pattern]]).

**Gaps:** prompt caching mechanics (what is cacheable, prices), the evals/dashboards "controls"
layer, batch processing, and the files API, all named but not covered.

## Wiki changes

- Created: [[claude-platform-101-course-notes]], [[claude-platform]], [[claude-managed-agents]],
  [[tool-use]], [[extended-thinking]], [[model-selection]], [[who-runs-the-agent-loop]]
- Updated: [[agentic-loop]] (API loop, stop reasons, ownership split), [[context-management]]
  (retitled from "(Claude Code)"; API patterns), [[claude-skills]] (API route; tools vs skills),
  [[model-context-protocol]] (provider-maintained; API connection and tool scoping),
  [[claude]] (model tiers; API access), [[claude-code]] (`/claude-api` skill; file/pattern/end
  state), [[lightweight-evals]] (20–30-example tension), [[hallucination]] (search isn't
  proof), [[choosing-a-claude-surface]] (building from code), [[claude-code-extension-points]]
  (API counterparts), [[overview]], [[index]]

## Raw

[[2026-10-06-claude-platform-notes]]
