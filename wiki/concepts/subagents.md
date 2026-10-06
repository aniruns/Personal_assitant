---
title: Subagents
type: concept
tags: [ai-tools, claude, llm-agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]"]
related: ["[[claude-code]]", "[[context-management]]", "[[explore-plan-code-commit]]", "[[claude-skills]]", "[[agentic-loop]]", "[[claude-code-extension-points]]"]
confidence: medium
status: seed
---

# Subagents

Delegated agents that [[claude-code]] can launch, each with its **own isolated context**,
optionally running in parallel ([[claude-code-101-course-notes]]). They do noisy work, such as
searches, exploration and reviews, so that the main session's context stays clean.

## Explanation

- **Why:** exploration and web search fill the main context with clutter. A subagent does the
  digging and returns **only a summary** ([[claude-code-101-course-notes]],
  [[context-management]]).
- **Definition:** a markdown file with YAML frontmatter. Create one with `/agents` →
  "Create new agent", then choose the scope, purpose, tools and colour; Claude writes the name,
  description and prompt. The **description also decides when Claude calls it
  automatically** ([[claude-code-101-course-notes]]).
- **Extras:** persistent memory across conversations, and **preloaded skills** via a skill key.
  Unlike the main conversation, a preloaded skill is loaded **in full** into the subagent's
  context ([[claude-code-101-course-notes]], [[claude-skills]]).
- **Built-in example:** the explore subagent, which summarizes a codebase without Plan mode
  ([[explore-plan-code-commit]]).

## Code-review subagents

Review with a subagent before opening a PR: it has its own context and none of the main
session's bias. Give the reviewer **read-only tools** so it flags problems without editing.
Commit its config to the repo so the whole team shares the same reviewer
([[claude-code-101-course-notes]]).

## How it connects

- The "other agents" in the [[agentic-loop]] definition.
- One rung of the [[claude-code-extension-points]] ladder: the right choice when you need an
  answer, not the process that produced it.
- Follow-up: the course points to a separate "Intro to subagents" course.

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-code-101-course-notes]]
