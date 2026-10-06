---
title: CLAUDE.md (project memory)
type: concept
tags: [ai-tools, claude, coding, configuration]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]"]
related: ["[[claude-code]]", "[[context-management]]", "[[claude-code-hooks]]", "[[claude-code-extension-points]]", "[[llm-wiki-pattern]]", "[[claude-projects]]"]
confidence: medium
status: seed
---

# CLAUDE.md (project memory)

A markdown file that [[claude-code]] reads automatically at the start of every session and
appends to its prompt. It acts as persistent project memory, an "onboarding script for your
codebase" ([[claude-code-101-course-notes]]). Without one, Claude starts fresh each time,
re-explores the project and makes assumptions. This KB's own schema is a CLAUDE.md.

## Explanation

- **Typical contents:** the stack (e.g. Next.js 15, Tailwind, Drizzle), commands (dev, test,
  lint) and code style (2-space indent, named exports, where API routes go)
  ([[claude-code-101-course-notes]]).
- **Hierarchy** ([[claude-code-101-course-notes]]):
  - *Project level:* in the repo root, committed to git, shared with the team.
  - *User level:* in the user's config folder, private, applies to all projects. Personal
    preferences go here.
- **References:** pull in other docs with `@`, e.g. `@README.md`
  ([[claude-code-101-course-notes]]).
- **Growing it:** **start without one**. Notice where you keep correcting Claude, then run
  `/init` to generate the file; this keeps it lean. When you correct the same thing twice, tell
  Claude to save the rule. Repeated fixes during coding belong here too
  ([[claude-code-101-course-notes]], [[explore-plan-code-commit]]).

## How it connects

- **"Usually" vs "always":** an instruction in CLAUDE.md is advisory. If something must happen
  every time, use a hook ([[claude-code-hooks]]). Full comparison in
  [[claude-code-extension-points]].
- Plays the same role as a [[claude-projects]] project's instructions: standing context, but
  version-controlled with the code.
- Assessment: in this KB, `CLAUDE.md` is the **schema layer** of the [[llm-wiki-pattern]]. It
  defines page types, operations and conventions rather than a code stack, and `AGENTS.md`
  points to it so that other agents follow the same rules.

## Contradictions & open questions

- Size guidance: the course says to keep it lean but gives no limit. This KB's CLAUDE.md is
  fairly long; is that costing context on every session?

## Sources

- [[claude-code-101-course-notes]]
