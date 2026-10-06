---
title: Claude Code hooks
type: concept
tags: [ai-tools, claude, coding, automation]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]"]
related: ["[[claude-code]]", "[[claude-md]]", "[[claude-code-extension-points]]", "[[agentic-loop]]", "[[llm-wiki-pattern]]"]
confidence: medium
status: seed
---

# Claude Code hooks

Shell commands that [[claude-code]] runs at fixed points in its lifecycle. Unlike every other
customization, hooks are **deterministic and always run** ([[claude-code-101-course-notes]]).

> if it has to happen every time, don't put it in a prompt, put it in a hook

## Explanation

**"Usually" vs "every time."** "Run prettier after edits" in [[claude-md]] is followed
*usually*; a hook runs *every single time* ([[claude-code-101-course-notes]]).

**Uses:** auto-formatting, logging commands for compliance, blocking dangerous operations
(production files, `rm -rf`, commits to main), and notifying you when Claude is done
([[claude-code-101-course-notes]]).

**Configuration:** in `settings.json` or via `/hooks`. Pick an event, an optional matcher and
a command. `.claude/settings.json` is project level and committed to the repo. Use the
`CLAUDE_PROJECT_DIR` environment variable to point at scripts so that paths work from any
directory ([[claude-code-101-course-notes]]).

**Events** ([[claude-code-101-course-notes]]):

| Event | Fires |
|---|---|
| `PreToolUse` | before a tool call — **can block** |
| `PostToolUse` | after a tool call |
| `UserPromptSubmit` | when a prompt is submitted, before Claude sees it |
| `Stop` | when Claude finishes responding |
| `Notification` | when Claude sends a notification |

**Blocking (`PreToolUse`).** The hook receives the tool name and input as JSON on stdin
([[claude-code-101-course-notes]]):
- exit **0** → allow the call
- exit **2** → block; stderr goes **back to Claude as feedback** so it can adjust
- any other code → non-blocking error, shown only to the user

**Example: auto-format.** `PostToolUse`, matcher `Edit|MultiEdit|Write`. The command checks
the file extension and runs prettier, gofmt, etc. ([[claude-code-101-course-notes]]).

## How it connects

- The top, "guaranteed" rung of [[claude-code-extension-points]].
- Exit-2 feedback closes the [[agentic-loop]]: a blocked action becomes new context, and
  Claude tries again.
- Assessment: this KB could add a `Stop` or `PostToolUse` hook that runs `scripts/lint.py`, so
  that mechanical lint happens on every edit rather than when remembered. A Gitleaks hook
  already blocked a commit once (see the CLM ingest in [[log]]) ([[llm-wiki-pattern]]).

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-code-101-course-notes]]
