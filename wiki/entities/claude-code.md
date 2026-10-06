---
title: Claude Code
type: entity
tags: [ai-tools, claude, coding, agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]", "[[2026-10-06-claude-code-101-notes]]"]
related: ["[[claude]]", "[[agentic-loop]]", "[[explore-plan-code-commit]]", "[[context-management]]", "[[claude-md]]", "[[subagents]]", "[[claude-code-hooks]]", "[[claude-code-extension-points]]"]
confidence: medium
status: growing
---

# Claude Code

Anthropic's agentic coding tool. It reads a codebase, edits files, runs commands and connects
to your dev tools ([[claude-code-101-course-notes]]). It matters here for two reasons: it is
the subject of a course the user has taken, and it is the agent that maintains this KB.

## What it is

- **Agent, not chat.** Unlike claude.ai, it has direct access to files, the terminal and the
  codebase, so there is no copy-pasting back and forth: "it just does the work." Under the hood
  it runs an [[agentic-loop]]: gather context → act → verify → repeat
  ([[claude-code-101-course-notes]]).
- **Can:** explain code, trace bugs, refactor across files, run builds, tests and installs,
  and search the web for docs ([[claude-code-101-course-notes]]). The Claude 101 course adds
  lint, merge conflicts and release notes ([[claude-101-course-notes]]).
- **Three things to keep in mind** ([[claude-code-101-course-notes]]):
  1. The context window is finite working memory, so Claude Code searches selectively instead
     of loading the whole repo ([[context-management]]).
  2. It asks permission by default.
  3. It *can* get things wrong (misread intent, introduce bugs, over-engineer), so stay in the
     loop.

## Permission modes

| Mode | Behaviour |
|---|---|
| Default | asks before edits and shell commands |
| Auto accept | edits without asking; commands still need approval |
| Plan | read-only; builds a plan first |

Cycle through them with Shift+Tab. They are configurable in the settings file, and the course
warns: "careful w skipping perms!!" ([[claude-code-101-course-notes]]). The desktop Code tab
calls the same three modes "manually approve / accept edits / plan"
([[claude-101-course-notes]]).

## Install & surfaces

- **Install:** a curl one-liner on macOS, Linux and WSL; PowerShell, curl in CMD, or winget on
  Windows. **Homebrew and winget installs don't auto-update.** Run `claude` in the project
  directory and sign in with Pro, Max, Enterprise or an API key. Claude Code can then see
  **that directory and every subfolder** ([[claude-code-101-course-notes]]).
- **Surfaces** ([[claude-code-101-course-notes]], [[claude-101-course-notes]]):

| Surface | Notes |
|---|---|
| Terminal | gets new features first |
| VS Code / JetBrains | extension or plugin; roughly the same as the terminal |
| Desktop app, Code tab | diffs, terminal, git; local folder or cloud; good for background work |
| Web (claude.ai/code) | **GitHub repos only**; remote work |
| Slack (Claude Tag) | can start a session from a bug thread |

## Workflow & commands

- **Workflow:** [[explore-plan-code-commit]]. Plan first in Plan mode, code against success
  criteria and tests, then review with a subagent and commit.
- **Customization:** [[claude-md]] (memory), [[claude-skills]], [[subagents]],
  [[model-context-protocol|MCP]] and [[claude-code-hooks|hooks]]. For which to use when, see
  [[claude-code-extension-points]].
- **Git & PRs:** `/commit-push-pr` commits, pushes and opens a PR in one step. A PR opened via
  `gh pr create` is linked to the session; resume it with `claude --from-pr <n>`
  ([[claude-code-101-course-notes]]).
- **Cheatsheet:** `claude` · Shift+Tab · `/compact` · `/clear` · `/context` · `/init` ·
  `/agents` · `/mcp` · `/hooks` · `/commit-push-pr` · `claude mcp add` ·
  `claude --from-pr <n>` ([[claude-code-101-course-notes]]).

## Relationships

- The "build software" shape of work in [[choosing-a-claude-surface]]. [[claude-cowork]] is
  the non-code counterpart for handing off whole tasks.
- Can use [[claude-in-chrome]] to test UIs it builds ([[explore-plan-code-commit]]).
- The agent behind this KB's [[llm-wiki-pattern]] workflow; `CLAUDE.md` is the KB's
  [[claude-md]].

## Contradictions & open questions

- The Claude 101 notes suggested non-developers skip Claude Code ([[claude-101-course-notes]]),
  yet this KB uses it for non-code knowledge work. Assessment: the course's advice reflects its
  audience, not a limit of the tool.
- Install details, which surface gets features first, and thresholds such as the 10% MCP
  tool-search switch are time-sensitive.

## Sources

- [[claude-code-101-course-notes]]
- [[claude-101-course-notes]]
