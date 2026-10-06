---
title: Explore → plan → code → commit
type: concept
tags: [ai-tools, claude, coding, workflow]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]"]
related: ["[[claude-code]]", "[[subagents]]", "[[claude-md]]", "[[claude-in-chrome]]", "[[prompting-fundamentals]]", "[[agentic-loop]]"]
confidence: medium
status: seed
---

# Explore → plan → code → commit

The core workflow the Claude Code 101 course teaches, and the user's "main takeaway" from it:
don't jump straight to "write code"; explore and plan first ([[claude-code-101-course-notes]]).
Most people skip the first two steps and spend the time saved on fixes later.

## Explanation

1. **Explore + plan.** Switch to **Plan mode** (Shift+Tab until it shows). In this mode Claude
   can only read. Describe the goal and ask it to work out where the change goes, what it
   depends on and how to approach it. The course's example: "add WebP conversion to image
   upload pipeline". Review the plan and ask for revisions. This is the **cheapest place to
   course correct** because no code exists yet. If you only need a summary of the codebase,
   the explore subagent works without Plan mode ([[claude-code-101-course-notes]]).
2. **Code.** Approve the plan, then choose auto accept or approve each edit.
   - Define **success criteria**: what does "correct" look like?
   - Give Claude **tools to verify itself**, e.g. [[claude-in-chrome]] so it can test the UI.
   - Give it a **test suite** to validate against, and make sure the tests are reliable, or
     you will get false positives.
   - If it keeps hitting the same problem, have it save the fix to [[claude-md]]
   ([[claude-code-101-course-notes]]).
3. **Commit.** Test it yourself first. Then run a **code-reviewer subagent**, which has fresh
   eyes and none of the main session's bias ([[subagents]]). Finally, have Claude write the
   commit message in your style. Repeat for the next change ([[claude-code-101-course-notes]]).

**Git extras:** a `/commit-push-pr` skill commits, pushes and opens a PR in one step. With a
Slack MCP server and channels listed in CLAUDE.md, it also posts the PR link. A PR created
with `gh pr create` is linked to the session; `claude --from-pr <n>` resumes it later
([[claude-code-101-course-notes]]).

## How it connects

- The coding version of [[prompting-fundamentals]]' "set the stage → define the task →
  specify rules". Plan mode is where you set the stage.
- Each phase is the [[agentic-loop]] with a different permission mode.
- Assessment: this KB's ingest follows the same shape. Read and orient (explore), discuss
  takeaways (plan), write pages (code), then log and offer a commit (commit)
  ([[llm-wiki-pattern]]).

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-code-101-course-notes]]
