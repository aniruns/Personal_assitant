---
title: Claude Code
type: entity
tags: [ai-tools, claude, coding, agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[claude]]", "[[claude-cowork]]", "[[choosing-a-claude-surface]]", "[[llm-wiki-pattern]]"]
confidence: medium
status: seed
---

# Claude Code

Anthropic's agentic coding tool. You describe a feature in plain English and it reads the
codebase, edits files and runs commands. It matters here because it is the agent that
maintains this KB.

## What we know

- **Where it runs:** terminal, IDE, browser, Slack (via Claude Tag), and the **Code tab** of
  the [[claude]] desktop app ([[claude-101-course-notes]]).
- **Desktop Code tab:** shows diffs, a terminal and git. It runs either **local** (a folder on
  your machine) or **cloud** (a GitHub repo; keeps running after you close the app). Modes:
  manually approve, accept edits, plan ([[claude-101-course-notes]]).
- **Uses named in the course:** building features, debugging, understanding a codebase,
  lint, merge conflicts, release notes ([[claude-101-course-notes]]).
- From Slack, Claude Tag can **start a Claude Code session from a bug thread**
  ([[claude-101-course-notes]]).
- The course suggests non-developers skip it; "Claude Code in Action" is the follow-up course
  ([[claude-101-course-notes]]).

## Relationships

- The "build software" shape of work in [[choosing-a-claude-surface]]. [[claude-cowork]] is the
  non-code counterpart for handing off whole tasks.
- The agent behind this KB's [[llm-wiki-pattern]] workflow. `CLAUDE.md` is its project schema.

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-101-course-notes]]
