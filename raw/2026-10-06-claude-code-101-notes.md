---
title: "Claude Code 101 — my notes"
author: the user (personal course notes)
url: n/a ("Claude Code 101" course; platform not stated in the notes — likely Anthropic Academy, inferred from cross-references to "Intro to subagents" / "Intro to agent skills")
saved: 2026-10-06
source_type: note
note: "Dropped into raw/ as claude-code-101-notes.md; renamed to the raw naming convention and this frontmatter added. Content below is verbatim."
---

# Claude Code 101 notes (my notes, kinda messy)

Heads up: "Your first prompt" and "Skills" are video only, no text I could pull, so those two are thin.

## 1. what is CC

- agentic coding tool. reads codebase, edits files, runs cmds, hooks into ur dev tools
- where: terminal, VS Code, JetBrains, Desktop app, web
- vs claude.ai: has direct access to files/terminal/codebase, no copy paste back n forth. it just does the work
- agent = LLM running in a loop, can use tools / external services / other agents to hit a goal
- can: explain code, trace bugs, refactor across files, run builds/tests/installs, web search for docs
- 3 things to remember:
  - context window = working memory, finite. CC searches smartly instead of loading whole repo
  - asks permission by default
  - CAN mess up (misread intent, bugs, overengineer). stay in the loop

## 2. how it works

- agentic loop: prompt -> gather context -> take action (edit/run) -> verify -> done, or loop again
- u can interrupt / steer / add context anytime
- context fills up -> auto compaction (summarizes, drops junk)
- tools = backbone. lets it actually do stuff, not just text in text out
- permission modes:
  - default: asks before edits + shell cmds
  - auto accept: edits w/o asking, cmds still need ok
  - plan mode: read only, builds a plan first
- all configurable in settings file. careful w skipping perms!!

## 3. install

- mac/linux/WSL: curl one liner. brew works but NO auto update
- windows: PowerShell Invoke-RestMethod, or curl in CMD, or winget (no auto update)
- run `claude` in project dir. if not found, restart terminal
- sign in w Pro/Max/Enterprise or API key (pick Enterprise if org has it)
- **it gets access to that dir + all subfolders**
- VS Code: extension by Anthropic (blue check). Cmd/Ctrl+Shift+P -> "Claude Code Open in New Tab"
- JetBrains: plugin from marketplace, restart IDE
- Desktop: "Code" toggle at top, pick folder, can run in cloud
- web: claude.ai/code, GitHub repos only
- which one? terminal gets features first. IDE ~same. desktop good for background stuff. web for remote GitHub work

## 4. explore -> plan -> code -> commit (THE main takeaway)

- most ppl jump straight to "write code" = lots of fixing later
- explore + plan: Plan Mode (Shift+Tab till u see it). can't edit, only reads
  - eg prompt: "add WebP conversion to image upload pipeline, figure out where, deps, approach"
  - review plan, ask it to revise bits. **cheapest place to course correct**, before any code exists
  - explore subagent works w/o plan mode too if u just want a codebase summary
- code: approve plan, choose auto accept or ask each time
  - define success criteria (what does "correct" look like)
  - give it tools, eg Claude in Chrome ext so it can test UI itself
  - give it a test suite to validate against (make sure tests are actually reliable, else false positives)
  - keeps hitting same issue? ask it to save fix to CLAUDE.md
- commit: test urself first, then run a subagent code reviewer (fresh eyes, no bias from main session), then have it write commit msg in ur style. repeat

## 5. context mgmt

- everything eats context: prompts, file reads, tool calls, results
- near limit -> auto compact. can lose details!
- `/compact` = summarize so far, keep going (same feature, running out of room)
- `/clear` = wipe everything (new feature, avoid old bias)
- `/context` = see what's eating space + breakdown graphic
- stuff to remember across sessions -> CLAUDE.md
- tips:
  - be specific. vague prompt looks small but costs MORE (it explores + reasons more)
  - turn off unused MCP servers, they load all tools into context even if unused
  - skills = only load when needed
  - subagents for "just need the answer" tasks (eg "where r the auth endpoints"), returns summary only

## 6. code review / git

- review w subagent before PR. own context, unbiased
- reviewer subagent = **read only tools**. flag not edit. check config into repo so team shares it
- `/commit-push-pr` skill: commit + push + PR in one go
  - Slack MCP + channels in CLAUDE.md -> auto posts PR link
- PR via gh pr create links the session. come back later w `claude --from-pr <PR_NUMBER>`

## 7. CLAUDE.md

- persistent memory for the project. w/o it CC starts fresh every time, re explores, assumes stuff
- md file in project root, auto read every session, appended to prompt. "onboarding script for ur codebase"
- typical contents: stack (eg Next.js 15, Tailwind, Drizzle), commands (dev/test/lint), code style (2 space indent, named exports, where API routes go etc)
- commit it to git, team benefits
- hierarchy:
  - project level: repo root, shared
  - user level: config folder, just me, all projects. personal prefs go here
- tips:
  - keep correcting it on same thing? tell it to save the rule to memory
  - ref docs w @, eg @README.md
  - **start WITHOUT one**, see where u keep correcting, then `/init` to generate. keeps it lean

## 8. subagents

- delegate tasks, run in parallel, each has own isolated context
- why: exploration/web search junk clutters main context. subagent does the digging, returns just a summary
- defined as md files w YAML frontmatter
- `/agents` -> "Create new agent" -> pick scope, purpose, tools, color. claude writes name/desc/prompt
- description also decides when claude auto calls it
- extras: persistent memory across convos; preload skills via skill key (NOTE: full skill gets loaded into context here, unlike main convo)
- separate course: Intro to subagents

## 9. skills

- video lesson, no text. from other lessons: only name + desc sit in context, full content loads only when claude decides it needs it. lighter than MCP
- separate course: Intro to agent skills

## 10. MCP

- open standard to connect CC to external tools/data (DBs, prod apps, repos)
- eg Linear MCP for ur issues, Context7 for up to date docs
- `claude mcp add`
  - HTTP = remote, hosted by provider
  - stdio = local process on ur machine
- `/mcp` to see connected, status, disable
- scopes:
  - local: this project, just u
  - user: all ur projects
  - project: `.mcp.json` checked into git, whole team gets same servers
- context cost!! tool defs sit in context even when unused
  - CLI equivalent exists (gh, aws)? use CLI, cheaper
  - or use a skill
  - MCP tools > 10% of context -> auto switches to tool search mode (finds tools on demand, less reliable)

## 11. hooks

- run cmds at specific lifecycle points. **deterministic, ALWAYS run** (key diff vs everything else)
- CLAUDE.md "run prettier after edits" = usually. hook = every single time
- uses: auto format, log cmds for compliance, block dangerous ops (prod files), notify when done
- config in settings.json or `/hooks`. pick event + optional matcher + command
- events:
  - PreToolUse: before tool call
  - PostToolUse: after tool call
  - UserPromptSubmit: on prompt submit, before claude sees it
  - Stop: claude done responding
  - Notification: claude sends a notification
- eg auto format: PostToolUse, matcher "Edit|MultiEdit|Write", cmd checks extension -> prettier / gofmt etc
- PreToolUse can BLOCK. gets tool name + input as JSON on stdin
  - exit 0 = go ahead
  - exit 2 = block, stderr goes back to claude as feedback so it adjusts
  - anything else = non blocking error, shown to u only
  - eg block writes to prod config, block rm -rf, block commits to main
- `.claude/settings.json` = project level, check into repo
- use `CLAUDE_PROJECT_DIR` env var to point at scripts so paths work from anywhere
- **"if it has to happen every time, don't put it in a prompt, put it in a hook"**

## quick cmd cheatsheet

`claude` · Shift+Tab (modes / plan) · `/compact` · `/clear` · `/context` · `/init` · `/agents` · `/mcp` · `/hooks` · `/commit-push-pr` · `claude mcp add` · `claude --from-pr <n>`
