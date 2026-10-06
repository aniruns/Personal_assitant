---
title: Choosing a Claude surface — which tool for which job
type: synthesis
tags: [ai-tools, claude, decision-guide]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[claude]]", "[[claude-cowork]]", "[[claude-code]]", "[[claude-in-chrome]]", "[[claude-projects]]", "[[claude-skills]]", "[[claude-connectors]]", "[[claude-artifacts]]"]
confidence: medium
status: seed
---

# Choosing a Claude surface — which tool for which job

A decision guide that combines the Claude 101 course's three separate "which one?" lessons
(shapes of work, research vs. search, the surface cheat sheet) into one place. The course's
principle: **work out what kind of work it is first; then the right tab is obvious**
([[claude-101-course-notes]]).

## 1. By shape of work

| Shape | Use | Signals |
|---|---|---|
| Turn-by-turn | **Chat** | The answer changes what you ask next; you want to stay in the loop; it's quick. Desktop extras: double-tap Option for a floating quick-entry window, screenshots and window sharing, dictation |
| Hand it off | **[[claude-cowork]]** | Multi-step; many tools; finished files saved to a folder; scheduled or background |
| Build software | **[[claude-code]]** (Code tab) | Diffs, terminal, git; local or cloud |

## 2. By kind of question

| Need | Use | Why |
|---|---|---|
| Big report, comparison, competitor/vendor scan, hours of manual work | **Research** | Agentic: plans with Thinking, runs many searches that build on each other (100s of sources), synthesises web + Gmail/Calendar/Drive, cites everything; takes minutes |
| A quick fact from 1–2 sources, where speed matters | **Web search** | Fast and shallow |
| Pure reasoning: maths, debugging, logic | **Thinking** | No outside information needed |
| Internal company knowledge | **Enterprise search ("Ask {Org}")** | Team/Enterprise only: a pre-built project over SharePoint/Slack/Gmail/Drive; one cited answer; shows only what you can already access |

Research prompts: be specific about the goal, specify the sections you want, add constraints
(budget, time, location), and ask Claude to help write the research prompt itself. Enable it
via + → Research, with web search on. Enterprise-search setup needs an admin to connect a docs
source (Drive/SharePoint) and a chat source (Slack/Teams); email is optional
([[claude-101-course-notes]]).

## 3. By where you are working

| Where | Surface |
|---|---|
| General use | claude.ai (with [[claude-projects]], [[claude-artifacts]]) |
| Development | [[claude-code]] |
| Multi-step hand-offs | [[claude-cowork]] |
| Slack / team threads | Claude Tag |
| UI prototypes | Claude Design |
| Inside Excel / PowerPoint / Word / Outlook | Claude for M365 |
| Web pages, browser automation | [[claude-in-chrome]] |

Source: [[claude-101-course-notes]].

## Building blocks underneath

**Projects = knowledge, skills = process, connectors = access** ([[claude-projects]],
[[claude-skills]], [[claude-connectors]]). Every surface above draws on some mix of the three.

## The user's tl;dr

From the user's own summary in the notes ([[2026-10-06-claude-101-notes]]):
quick question → chat; whole task → Cowork; deep dive → Research; internal question → Ask
{Org}; ask for the deliverable (an artifact), not just a chat answer; verify anything that
matters.

## Open questions

- Plan and beta gating changes often. Re-verify the "who gets what" details before relying
  on them.
- Which of these does the user actually reach for at work (Zeta)? Their notes flag status
  reports and decoding an inherited spreadsheet as the most useful use cases.
