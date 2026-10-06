---
title: Claude
type: entity
tags: [ai-tools, claude, anthropic]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[claude-code]]", "[[claude-cowork]]", "[[claude-in-chrome]]", "[[claude-projects]]", "[[claude-skills]]", "[[claude-connectors]]", "[[claude-artifacts]]", "[[choosing-a-claude-surface]]"]
confidence: medium
status: seed
---

# Claude

Anthropic's AI assistant and model family. In this KB it is both a subject (how to use it
well) and the tool that maintains the KB itself: the wiki is compiled by [[claude-code]]
following the [[llm-wiki-pattern]].

## What we know

- **Positioning.** Sold as a "thinking partner" rather than "just a chatbot". It is trained
  with **Constitutional AI**, a set of principles meant to keep it safe and aligned, and it is
  "steerable": it follows instructions on tone, personality and behaviour
  ([[claude-101-course-notes]]).
- **Strengths claimed:** writing, research and analysis, coding (called out as a major
  strength), reasoning/maths, and learning. **Thinking** makes it reason step by step before
  answering. **Learning mode** guides you to an answer instead of handing it over
  ([[claude-101-course-notes]]).
- **Context window:** 200K+ tokens (~500 pages), or 1M on paid plans with supported models,
  as of the course date ([[claude-101-course-notes]]).
- **Access:** web, desktop and mobile on all plans. Chats, projects and memory sync across
  devices. **Settings → "instructions for Claude"** applies to every chat. **Memory** keeps
  role, preferences and decisions, and can be edited in settings ([[claude-101-course-notes]]).
- **Uploads:** pdf, docx, csv, txt, png/jpg. It reads charts and images inside PDFs too
  ([[claude-101-course-notes]]).

## Surfaces and features

| Surface / feature | Page | One-liner |
|---|---|---|
| Chat (claude.ai, desktop, mobile) | [[choosing-a-claude-surface]] | turn-by-turn work |
| Cowork | [[claude-cowork]] | hand off multi-step tasks; scheduled, plugins |
| Claude Code | [[claude-code]] | agentic coding: terminal, IDE, desktop Code tab, Slack |
| Claude in Chrome | [[claude-in-chrome]] | browser sidebar that can see the page and act |
| Claude Tag | — | Claude in Slack threads; can start a Claude Code session from a bug thread |
| Claude for M365 | — | sidebars in Excel, PowerPoint, Word, Outlook (beta) |
| Claude Design / Slides / Docs | [[claude-artifacts]] | beta artifact types for prototypes, decks and living docs |
| Projects | [[claude-projects]] | knowledge + instructions workspace |
| Skills | [[claude-skills]] | reusable process packages |
| Connectors | [[claude-connectors]] | MCP access to your tools |
| Research / Ask {Org} | [[choosing-a-claude-surface]] | multi-step investigation / internal enterprise search |

## Relationships

- Prompted well via [[prompting-fundamentals]]; used responsibly via [[ai-fluency]].
- Runs this KB through [[claude-code]] (see [[llm-wiki-pattern]]).

## Contradictions & open questions

- Plan gating, beta labels and limits change often. Re-verify before relying on them.

## Sources

- [[claude-101-course-notes]]
