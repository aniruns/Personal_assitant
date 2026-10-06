---
title: Claude Connectors
type: concept
tags: [ai-tools, claude, integration]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]", "[[2026-10-06-claude-code-101-notes]]"]
related: ["[[model-context-protocol]]", "[[claude-skills]]", "[[claude-projects]]", "[[choosing-a-claude-surface]]", "[[claude]]"]
confidence: medium
status: seed
---

# Claude Connectors

Access from [[claude]] to your actual tools, letting it read **and act** (search, create,
update). Connectors are built on [[model-context-protocol]].

## Explanation

- **Two types** ([[claude-101-course-notes]]):
  - *Web connectors:* Google Drive, Notion, Slack, Asana, Gmail, Linear, Stripe…
  - *Desktop extensions:* local files, browser control, native apps (e.g. Figma). Desktop
    app only, under Settings → Extensions.
- **Finding them:** claude.ai/directory, or + → Connectors in a chat. The directory lists
  connectors, not apps: Jira and Confluence are under **Atlassian Rovo**. If nothing fits, use
  a custom connector ([[claude-101-course-notes]]).
- **Setup:** connect → log in → approve permissions → test with "can you access my X?"
  ([[claude-101-course-notes]]).
- **Example asks:** top-priority tasks this week (Asana/Jira); find the vendor-contract
  thread (Gmail); what the style guide says about contractions (Notion); last quarter's
  revenue trend (Stripe) ([[claude-101-course-notes]]).
- **Security:** permissions are scoped and can be toggled individually. **Claude sees only
  what you can see**: connecting your email does not expose the CEO's inbox. You can revoke
  access at any time. Use custom connectors only from trusted sources
  ([[claude-101-course-notes]]).

## How it connects

- The course's one-line model: projects = knowledge, [[claude-skills]] = process,
  connectors = **access** ([[claude-101-course-notes]]).
- Enterprise search and Research both build on connectors
  ([[choosing-a-claude-surface]]).
- In [[claude-code]], the same protocol is configured directly as MCP servers (`claude mcp
  add`, local / user / project scope). The course there stresses the **context cost** of tool
  definitions, which the claude.ai connector lessons didn't mention
  ([[model-context-protocol]], [[claude-code-101-course-notes]]).

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-101-course-notes]]
- [[claude-code-101-course-notes]]
