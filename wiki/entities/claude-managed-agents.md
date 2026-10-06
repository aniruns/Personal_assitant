---
title: Claude Managed Agents
type: entity
tags: [ai-tools, claude, api, llm-agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude-platform]]", "[[agentic-loop]]", "[[who-runs-the-agent-loop]]", "[[tool-use]]", "[[context-management]]", "[[subagents]]"]
confidence: medium
status: seed
---

# Claude Managed Agents

APIs on the [[claude-platform]] for building and deploying agents at scale, where **Anthropic
hosts the [[agentic-loop]]**. Each run happens in an isolated container with file system
access, bash and web search ([[claude-platform-101-course-notes]]). It is the far end of
[[who-runs-the-agent-loop]].

## What we know

**When to use one:** the loop would run for minutes or hours, touch many tools and files, or
need to survive a network hiccup ([[claude-platform-101-course-notes]]).

**Four primitives, in order** ([[claude-platform-101-course-notes]]):

1. **Agent** — the persona: model, system prompt, toolset. Reusable.
2. **Environment** — where it runs: cloud or local, networking.
3. **Session** — a single run; the unit of work.
4. **Events** — everything flowing in and out.

**Flow:** create agent → create environment → create session → **open the event stream** →
send the kickoff message → read events. *Gotcha:* the stream only delivers events that happen
after it opens, so open it first.

| Event | Meaning |
|---|---|
| `agent.message` | Claude's text |
| `agent.tool_use` | which tool it picked |
| `session.status_idle` | the agent is done |

- The bundled `agent_toolset_...` gives Anthropic's file, bash and web tools, so you define none
  yourself ([[claude-platform-101-course-notes]]).
- **Caching and compaction are on by default** ([[context-management]]).
- **Wider building blocks:** Agents · Sessions · Environments · Tools · MCP · Memory ·
  **Outcomes** (rubrics and graders) · multi-agent coordination
  ([[claude-platform-101-course-notes]]).
- **The trade:** you give up control of the loop, the sandbox and resumability, and just
  consume events. Use a manual loop when you want full control
  ([[claude-platform-101-course-notes]]).
- On by default for every API account, as of the course date
  ([[claude-platform-101-course-notes]]).

## Course examples

- **Kanban board:** moving a ticket to "In progress" starts a session. Claude optimises site
  performance against a **rubric** (Lighthouse > 90); a **separate grader** checks the work and
  Claude iterates (it reached 96). Tickets run in parallel.
- **Weekly SaaS pricing tracker:** web search → Python cost analysis → an Excel skill → posts to
  Slack and Asana via MCP. **Memory** lets it report what changed since last week.
- **Incident response:** a **coordinator** delegates to three **specialists**. A **permissions
  policy** holds the Slack message until a human approves it; memory spots repeat incidents.

> You define what "done" looks like. Claude works until it gets there.

## Relationships

- The coordinator/specialist pattern is the hosted version of [[subagents]] in [[claude-code]].
- A permissions policy plays the role that [[claude-code-hooks]] and permission modes play
  locally: a deterministic gate around the model's actions. (Assessment.)
- Rubric + grader is an automated form of [[lightweight-evals]]. (Assessment.)

## Contradictions & open questions

- How resumability works, and what "local" environments mean in practice, isn't in the notes.
- Pricing isn't covered.

## Sources

- [[claude-platform-101-course-notes]]
