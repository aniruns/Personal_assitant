---
title: Claude Skills
type: concept
tags: [ai-tools, claude, automation]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[claude-projects]]", "[[claude-connectors]]", "[[claude-cowork]]", "[[claude]]"]
confidence: medium
status: seed
---

# Claude Skills

Folders of instructions, scripts and resources that [[claude]] loads when they are relevant,
described as "expertise packages". They encode **process** (the "how"), as opposed to the
knowledge held in [[claude-projects]].

## Explanation

- **Kinds:** *Anthropic skills* (Excel, Word, PowerPoint and PDF creation; used
  automatically) and *custom skills* (yours or your org's, e.g. brand guidelines, a
  meeting-note format, variance analysis) ([[claude-101-course-notes]]).
- **Enable:** Settings → Capabilities → "code execution & file creation" ON → toggle skills.
  On by default for Team; an Enterprise owner must enable them first
  ([[claude-101-course-notes]]).
- **Use:** you don't invoke them; Claude picks them, and the choice shows in its reasoning.
  Output arrives as a file download or in Google Drive. If you upload a file, Claude makes a
  **new version** and leaves your original untouched. Some skills may need "allow limited
  network access" ([[claude-101-course-notes]]).
- **Making one:** tell Claude "I want a skill for X". It interviews you, you upload templates
  and examples, and you save. Skills are managed under **Customize** in the sidebar and
  improved by asking Claude to edit them ([[claude-101-course-notes]]).
- **Security:** skills run code, so install only from trusted sources and read external
  skills before using them. Custom skills are private to your account
  ([[claude-101-course-notes]]).
- **Plugins** in [[claude-cowork]] bundle skills with [[claude-connectors]] and agents per role
  ([[claude-101-course-notes]]).

## How it connects

- **Skills vs projects:** a "call prep" skill can pull from customer profiles stored in a
  project ([[claude-101-course-notes]]).
- Assessment: the knowledge/process split matches this KB's layers. `wiki/` is knowledge;
  `CLAUDE.md` and `templates/` are process ([[llm-wiki-pattern]]). The KB's operations (ingest,
  query, lint) could be packaged as skills.

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-101-course-notes]]
