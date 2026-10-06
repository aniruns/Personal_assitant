---
title: Claude
type: entity
tags: [ai-tools, claude, anthropic]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]", "[[2026-10-06-claude-code-101-notes]]", "[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]", "[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude-code]]", "[[claude-cowork]]", "[[claude-in-chrome]]", "[[claude-projects]]", "[[claude-skills]]", "[[claude-connectors]]", "[[claude-artifacts]]", "[[choosing-a-claude-surface]]", "[[claude-platform]]", "[[model-selection]]"]
confidence: medium
status: growing
---

# Claude

Anthropic's AI assistant, and the name of its family of large language models
([[ai-fluency-vocabulary-cheat-sheet]]). In this KB it is both a subject (how to use it
well) and the tool that maintains the KB itself: the wiki is compiled by [[claude-code]]
following the [[llm-wiki-pattern]].

## What we know

- **Positioning.** Sold as a "thinking partner" rather than "just a chatbot". It is trained
  with **Constitutional AI**, a set of principles meant to keep it safe and aligned, and it is
  "steerable": it follows instructions on tone, personality and behaviour
  ([[claude-101-course-notes]]).
- **Strengths claimed:** writing, research and analysis, coding (called out as a major
  strength), reasoning/maths, and learning. **Thinking** makes it reason step by step before
  answering, making it a "reasoning model" in [[ai-fluency-glossary]] terms. **Learning mode** guides you to an answer instead of handing it over
  ([[claude-101-course-notes]]).
- **Model tiers** (as of the course date): **Haiku** (fast, cheap, high-volume), **Sonnet**
  (most production work), **Opus** (deep reasoning, complex coding) and **Fable**, a newer tier
  above Opus for the hardest problems. Pick the cheapest one whose output you'd ship
  ([[model-selection]], [[claude-platform-101-course-notes]]).
- **Context window:** 200K+ tokens (~500 pages), or 1M on paid plans with supported models,
  as of the course date ([[claude-101-course-notes]]). The window works as the model's
  finite **working memory** ([[context-management]], [[claude-code-101-course-notes]]).
- **Knowledge cutoff:** like any LLM, it has no built-in knowledge after its training cutoff,
  so recent facts need web search ([[ai-fluency-vocabulary-cheat-sheet]]).
- **As an agent:** in [[claude-code]] and [[claude-cowork]], Claude runs in an
  [[agentic-loop]], an LLM in a loop with tools ([[claude-code-101-course-notes]]).
- **From code:** the [[claude-platform]] (API, SDKs, Console) for building Claude into your own
  product ([[claude-platform-101-course-notes]]).
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
| Claude Code | [[claude-code]] | agentic coding: terminal, IDE, desktop Code tab, web (GitHub), Slack |
| Claude in Chrome | [[claude-in-chrome]] | browser sidebar that can see the page and act |
| Claude Tag | — | Claude in Slack threads; can start a Claude Code session from a bug thread |
| Claude for M365 | — | sidebars in Excel, PowerPoint, Word, Outlook (beta) |
| Claude Design / Slides / Docs | [[claude-artifacts]] | beta artifact types for prototypes, decks and living docs |
| Projects | [[claude-projects]] | knowledge + instructions workspace |
| Skills | [[claude-skills]] | reusable process packages |
| Connectors | [[claude-connectors]] | MCP access to your tools |
| Claude Platform (API) | [[claude-platform]] | build Claude into your own app; [[claude-managed-agents]] for hosted agents |
| Research / Ask {Org} | [[choosing-a-claude-surface]] | multi-step investigation / internal enterprise search |

## Relationships

- Prompted well via [[prompting-fundamentals]]; used responsibly via [[ai-fluency]]; can
  [[hallucination|hallucinate]]. Vocabulary in [[ai-fluency-glossary]].
- Runs this KB through [[claude-code]] (see [[llm-wiki-pattern]]).

## Contradictions & open questions

- Plan gating, beta labels and limits change often. Re-verify before relying on them.

## Sources

- [[claude-101-course-notes]]
- [[claude-code-101-course-notes]]
- [[ai-fluency-vocabulary-cheat-sheet]]
- [[claude-platform-101-course-notes]]
