---
title: "Claude Code 101 — course notes"
type: source
tags: [ai-tools, claude, coding, agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]"]
related: ["[[claude-code]]", "[[agentic-loop]]", "[[explore-plan-code-commit]]", "[[context-management]]", "[[claude-md]]", "[[subagents]]", "[[claude-code-hooks]]", "[[claude-code-extension-points]]"]
confidence: medium
status: seed
author: the user (own notes on a "Claude Code 101" course)
published: unknown (course date not recorded; notes saved 2026-10-06)
url: n/a (platform not stated; likely Anthropic Academy, inferred from its references to the "Intro to subagents" and "Intro to agent skills" courses)
source_type: note
---

# Claude Code 101 — course notes

The user's own notes ("kinda messy") on a **Claude Code 101** course of 11 lessons plus a
command cheatsheet. They cover what [[claude-code]] is, how its [[agentic-loop]] works,
installation and surfaces, the [[explore-plan-code-commit]] workflow (which the user marks as
"THE main takeaway"), [[context-management]], code review and git, [[claude-md]],
[[subagents]], skills, [[model-context-protocol|MCP]] and [[claude-code-hooks|hooks]]. The
"Your first prompt" and "Skills" lessons were video-only, so those parts are thin. This source
follows on from [[claude-101-course-notes]], whose notes named "Claude Code in Action" as the
next course. Assessment: this may be that course or a sibling of it; the notes don't say.

## Key claims

- An **agent is an LLM running in a loop** that uses tools, external services or other agents
  to reach a goal. Claude Code's loop runs prompt → gather context → act → verify → done or
  loop again, and you can interrupt or steer it at any point ([[agentic-loop]]).
- There are three **permission modes**: default (asks before edits and shell commands), auto
  accept (edits without asking, commands still need approval), and plan (read-only). They are
  set in a settings file, with a warning about skipping permissions ([[claude-code]]).
- Claude Code can see the launch directory **and all its subfolders** ([[claude-code]]).
- The terminal gets features first; the IDE extensions are about the same; desktop suits
  background work; the web version (claude.ai/code) works on **GitHub repos only**
  ([[claude-code]], [[choosing-a-claude-surface]]).
- **Plan before coding.** Plan mode is the "cheapest place to course correct", because no code
  exists yet. Define success criteria, give Claude tools and reliable tests to verify against,
  and review with a fresh subagent before committing ([[explore-plan-code-commit]]).
- Everything uses up context. Near the limit Claude auto-compacts, which can lose details.
  `/compact` keeps going on the same task, `/clear` starts fresh, `/context` shows usage. A
  **vague prompt costs more** than a specific one because Claude explores more
  ([[context-management]]).
- `CLAUDE.md` is read every session, like an "onboarding script for your codebase". It exists
  at project level (committed) and user level (personal). **Start without one** and run
  `/init` once you see what you keep correcting ([[claude-md]]).
- Subagents have isolated context and return only a summary. They are markdown files with YAML
  frontmatter, and their *description* decides when Claude calls them automatically. Reviewer
  subagents should get read-only tools ([[subagents]]).
- MCP tool definitions take up context **even when unused**. Prefer a CLI (gh, aws) or a skill
  where one exists. If MCP tools exceed 10% of context, Claude Code switches to tool-search mode
  ([[model-context-protocol]], [[context-management]]).
- Hooks are **deterministic and always run**. `PreToolUse` can block an action: exit 2 blocks
  and returns stderr to Claude as feedback ([[claude-code-hooks]]).

## Notable quotes

> if it has to happen every time, don't put it in a prompt, put it in a hook

> CLAUDE.md "run prettier after edits" = usually. hook = every single time

> most ppl jump straight to "write code" = lots of fixing later

## Assessment

These are a learner's notes on vendor training. They are good on mechanics (commands, hook
exit codes, MCP scopes) and on workflow. Specific numbers and behaviours are
**time-sensitive** and should be read as of the course date, for example the 10% tool-search
threshold, which surface gets features first, and Homebrew/winget not auto-updating.

The most durable idea in the notes is a **ladder of where to put an instruction**:
prompt → CLAUDE.md → skill → subagent → MCP → hook. Each step trades context cost against
reliability. That ladder is now its own synthesis, [[claude-code-extension-points]].

**Links to the existing wiki:**
- This KB already runs this way. `CLAUDE.md` is a [[claude-md]] used as the KB's schema, and
  each ingest is an explore → plan → write → commit cycle.
- Hooks are the obvious way to make `scripts/lint.py` run every time instead of "usually"
  ([[llm-wiki-pattern]]).
- No contradictions with [[claude-101-course-notes]]. The desktop permission modes have
  slightly different names in the two sets of notes ("manually approve / accept edits" vs.
  "default / auto accept").

**Gaps:** the video-only lessons on the first prompt and skills; slash-command and custom-skill
authoring; the follow-up courses (Intro to subagents, Intro to agent skills).

## Wiki changes

- Created: [[claude-code-101-course-notes]], [[agentic-loop]], [[explore-plan-code-commit]],
  [[context-management]], [[claude-md]], [[subagents]], [[claude-code-hooks]],
  [[claude-code-extension-points]]
- Updated: [[claude-code]] (rewritten: loop, permission modes, install and surfaces, commands,
  git and PR flow), [[claude-skills]] (progressive loading; full load when preloaded into a
  subagent), [[model-context-protocol]] (transports, scopes, context cost, tool search),
  [[claude-connectors]] (connectors vs. Claude Code MCP), [[claude-in-chrome]] (used by Claude
  Code to test UIs), [[claude]] (agent definition; context = working memory),
  [[choosing-a-claude-surface]] (which Claude Code surface), [[llm-wiki-pattern]] (CLAUDE.md
  and hooks parallels), [[overview]], [[index]]

## Raw

[[2026-10-06-claude-code-101-notes]]
