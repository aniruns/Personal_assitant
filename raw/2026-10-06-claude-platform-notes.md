---
title: "Claude Platform 101 — my notes"
author: the user (personal course notes)
url: n/a ("Claude Platform 101" course, Anthropic Academy (Skilljar), per the notes' own header)
saved: 2026-10-06
source_type: note
note: "Copied from ~/Downloads/Claude-platform-notes.md; renamed to the raw naming convention and this frontmatter added. Content below is verbatim."
---

# Claude Platform 101: Course Notes

*Anthropic Academy (Skilljar), 13 lessons + quiz. Model names and beta version strings below are copied from the course and change over time, so check the docs before you use them.*

---

## The big picture in one paragraph

The Claude Platform lets you use Claude **from code** instead of a chat window. You start with a single API call (`messages.create`). Then you give Claude **tools** so it can act, put it in a **loop** so it can keep working, and add **thinking**, **built-in tools**, **skills** and **MCP** to make it more capable. You manage **context** so it stays affordable. When the loop gets long or heavy, you hand the whole thing to Anthropic with **managed agents**. Claude Code can write most of this code for you.

> **Shorthand from the course:** *build with primitives, scale on infrastructure, run with control.*

---

## 1. What is the Claude Platform?

It's Anthropic's infrastructure for building with Claude programmatically. You get:

- A **REST API**, usable from any language
- **SDKs** for several languages
- **CLIs**
- A **Console** (platform.claude.com) for API keys, usage, managed agents and testing prompts

**Three layers:**

| Layer | What it is | Examples |
|---|---|---|
| **Primitives** | The building blocks you call from code | Messages API, tool use, files, web search, code execution, MCP, skills |
| **Infrastructure** | What you need to scale past a prototype | Managed agents, retries, queues, observability |
| **Controls** | What you use to run it in production | Dashboards, evals |

**Key idea:** you aren't building a chatbot. You're wiring Claude into a product you already have, for example a "Draft reply" button in a help desk app.

---

## 2. Your first API call

**Setup**

1. Get an API key from platform.claude.com. You need to buy credits first.
2. Put the key in `.env.local`, never in source code, so it doesn't leak to GitHub.
3. Install the SDK: `npm install @anthropic-ai/sdk` (or `pip install anthropic`)

**Every call has three essentials:**

- `model`: which Claude handles it
- `max_tokens`: cap on the response length
- `messages`: a list of `user` / `assistant` turns

Plus an optional `system` prompt to set the persona and rules.

```python
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    system="You are a terse senior code reviewer.",
    messages=[{"role": "user", "content": "Review this code: ..."}],
)
```

**Watch out:** `response.content` is a **list of blocks**, not a string. Blocks can be text, tool calls or thinking, so always loop over them and check `block.type`.

---

## 3. Choosing the right model

| Model | Use it for | Trade-off |
|---|---|---|
| **Fable** | The hardest problems (a new tier above Opus) | Much more expensive than Opus |
| **Opus** | Deep reasoning, complex analysis, multi-step coding, nuanced writing | Slowest, most expensive of the core three |
| **Sonnet** | Most production work | Balanced |
| **Haiku** | High-volume, simple work: classification, extraction, routing | Fastest and cheapest |

**How to pick (the course's method):**

1. Build a small eval: **20–30 real examples** from your workload, plus a definition of "good".
2. Run them on **Haiku first**. If the output is good enough, stop there.
3. Otherwise move up to Sonnet, and use Opus only if you need it.

> **Rule:** the right model is the **cheapest one whose output you'd actually ship.**

- `response.usage` shows input and output tokens. Your bill is based on these.
- In a real app, **route each task to its own model**, e.g. classify with Haiku, draft with Sonnet, write RFP responses with Opus.

---

## 4. The agent loop

An **agent** is Claude in a loop: **observe → decide → act → repeat**, with no human in the middle.

**The loop:**

1. Send messages and the available tools to Claude.
2. Claude replies with either a final answer or a request to use a tool.
3. **Your code** runs the tool.
4. Send the result back as a `tool_result`.
5. Repeat until `stop_reason == "end_turn"`.

| `stop_reason` | Meaning | What you do |
|---|---|---|
| `tool_use` | Claude wants a tool | Run it, append the result, loop again |
| `end_turn` | Claude is done | Print the answer, exit |

> **You own the loop and the tools. Claude owns the reasoning.**

The same loop works for a toy weather demo and for a production compliance agent. Only the tools and plumbing change.

---

## 5. Tool use

A **tool** is a function you define and expose to Claude. **Claude decides when to call it; your code actually runs it.**

A tool definition has three parts:

- `name`
- `description`: Claude reads this to decide whether to use the tool
- `input_schema`: a JSON schema for the inputs

> **#1 reason agents misfire: vague tool descriptions.** Be specific.

**With several tools**, Claude reads the descriptions and picks the right one, sometimes calling more than one in a single turn. Your code dispatches on the tool name. To add a tool, add it to the array and add a `case`.

**The tool runner (SDK shortcut, TypeScript/Python/Ruby):**

- Pass in your **real functions**. It builds the schemas from your types and docs.
- It runs the whole tool loop for you. `runner.untilDone()` returns the final answer.
- No `while` loop, no `stop_reason` switch, and no schemas written twice.

**The spectrum:** run the loop yourself → let the tool runner do it → let **managed agents** run the whole agent.

---

## 6. Extended thinking

Claude reasons step by step **before** answering. The reasoning is **visible** in the response as thinking blocks.

**Turn it on (Opus 4.7, adaptive thinking):**

```python
thinking={"type": "adaptive"},
output_config={"effort": "high"},   # low | medium | high (default) | xhigh | max
```

- With adaptive thinking there's **no token budget**. Claude decides when to think and how much.
- **Gotcha:** `effort` goes inside `output_config`, not next to `thinking`.

| Use thinking for | Skip it for |
|---|---|
| Math, multi-step logic | Simple classification |
| Debugging code | Extraction |
| Regulatory analysis | Boilerplate |
| Trade-offs and comparing options | (it only adds latency and cost here) |

---

## 7. Built-in tools

Some tools are **pre-built by Anthropic**, so you just declare them.

**Server tools: declared by you, run by Anthropic**

- **Web search**: searches the web and returns citations
- **Web fetch**: pulls the full content of a URL
- **Code execution**: Claude writes and runs Python in a sandbox

**No agent loop needed.** The result comes back in the same response. Look for `server_tool_use` blocks and tool-result blocks next to the usual text blocks.

**Client tools: run where your code runs, but the SDK ships the schema and a runner**

- **Memory**: read and write memory across sessions
- **Bash**: a persistent shell

**Caveat:** finding something on the internet doesn't make it true. Double-check Claude's work.

---

## 8. Skills

A **Skill** is a folder (centred on a `SKILL.md`, plus any scripts and resources) that teaches Claude **how you do something**: your report format, review checklist or release-notes style.

| Tools | Skills |
|---|---|
| **What** Claude can do | **How** you want it done |
| Connect to data and actions | A playbook Claude reads and follows |

- **Progressive loading:** only the name and description load at first. The full skill loads when Claude decides it's relevant, which keeps context lean.
- **Upload once** (`client.beta.skills.create`), then reference it by ID.
- **Attach** through `container.skills` on a `client.beta.messages.create` call. It's a list, so you can layer several skills.
- They often **pair with code execution** so the skill can run its scripts.
- Skills are **beta** (they need a beta header).

**Why it matters:** every PM gets the same report structure without copy-pasting templates into prompts.

---

## 9. MCP (Model Context Protocol)

**The problem:** if you write your own Asana, Slack and Google integrations, **you maintain them** every time their APIs change.

**MCP's fix:** the **service provider** publishes and maintains an MCP server with tools, schemas and auth. When their API changes, they update the server and you change nothing.

> **Tools = your stuff · Skills = your processes · MCP = everyone else's stuff**

**How to connect** (beta, needs a beta header):

- `mcp_servers`: declares the connection (type, URL, name, optional auth token)
- An `mcp_toolset` entry in `tools`: says which of the server's tools Claude may use (all of them by default)
- Claude **discovers the tools by itself**, so you write no schemas.

**Scoping down (e.g. read-only Slack):** set `default_config: {"enabled": False}`, then enable only the specific tools, like `search_messages` and `list_channels`. This also saves context.

More servers: modelcontextprotocol.io

---

## 10. Context management

**Context** = everything Claude sees on a turn: the system prompt, message history, tool definitions and results, files, skills and thinking blocks.

- You pay for it **every call**.
- When the window is full, **the request fails**.
- The goal isn't to fit everything in. **It's to fit the right things in.**

**Four patterns:**

| # | Pattern | What it does | Fixes |
|---|---|---|---|
| 1 | **Just-in-time context** *(a design choice)* | Load only what's needed now and let tools fetch the rest | Window size |
| 2 | **Server-side compaction** | Add `context_management={"edits":[{"type":"compact"}]}` and old turns are auto-summarised past a threshold | Long conversations |
| 3 | **Prompt caching** | Cache stable parts (system prompt, tools, long docs) and reuse them cheaply | Cost |
| 4 | **Memory tool** | Claude reads and writes a memory directory; **you** own the storage backend | Statelessness across sessions |

In production you usually **layer all four**. Managed agents turn caching and compaction on by default.

---

## 11. What are managed agents?

**Claude Managed Agents** = APIs for building and deploying agents at scale. **Anthropic hosts the agent loop**, and each run happens in an isolated container with file system access, bash and web search.

**Examples from the course:**

- **Kanban board:** dragging a ticket to "In progress" starts a session. Claude optimises site performance against a **rubric** (e.g. Lighthouse > 90). A **separate grader** checks the work and Claude iterates (it reached 96). Several tickets run **in parallel**.
- **Weekly SaaS pricing tracker:** web search, Python cost analysis, an Excel skill, then posts to Slack and Asana via MCP. **Memory** lets it report what changed since last week.
- **Incident response:** a **coordinator** agent delegates to three **specialists**. A **permissions policy** holds the Slack message until a human approves it. Memory spots repeat incidents.

**Building blocks:** Agents · Sessions · Environments · Tools · MCP · Memory · Outcomes (rubrics and graders) · Multi-agent coordination

> **You define what "done" looks like. Claude works until it gets there.**

---

## 12. Building your first managed agent

**Why use one:** the loop would run for minutes or hours, touch many tools and files, or need to survive a network hiccup.

**Four primitives, in order:**

1. **Agent**: the persona (model, system prompt, toolset). **Reusable.**
2. **Environment**: where it runs (cloud or local, networking).
3. **Session**: a single run, **the unit of work**.
4. **Events**: everything flowing in and out.

**The flow:** create the agent → create the environment → create a session → **open the event stream** → send the kickoff message → read the events.

> **Gotcha:** open the stream **before** you send the kickoff. It only delivers events that happen after it opens.

**Events to watch:**

| Event | Meaning |
|---|---|
| `agent.message` | Claude's text |
| `agent.tool_use` | Which tool it picked |
| `session.status_idle` | The agent is done |

- The `agent_toolset_...` tool gives you Anthropic's bundled file, bash and web tools, so you don't define any yourself.
- Managed agents are **on by default** for every API account.
- **The trade:** you give up the loop, the sandbox and resumability, and just consume events. Use a **manual loop** when you want full control.

---

## 13. Building with Claude Code

Have **Claude Code** write the API code for you.

- Its built-in **Claude API skill** (`/claude-api`) loads automatically when it sees the SDK. If it's missing, run `/plugin marketplace add AnthropicsSkills` (note the **s** at the end).
- **A good prompt names three things:** the **file**, the **pattern** (e.g. the tool runner) and the **end state**.
- Claude Code writes the code, runs it, and fixes errors in place.

**The pattern behind almost everything:** define a tool → hand it to a runner → return the result.

> **Stub the file, delegate it, review the diff.**

---

## Quick-revision cheat sheet

- **One call:** `messages.create(model, max_tokens, messages, system?)`. Response = list of blocks.
- **Model choice:** start with Haiku, move up only when needed, and test on 20–30 real examples.
- **Agent loop:** keep going while `stop_reason == "tool_use"` and stop at `end_turn`.
- **Tools:** Claude chooses, your code runs. Descriptions matter most.
- **Tool runner:** pass real functions, skip schemas and loop code.
- **Thinking:** `{"type":"adaptive"}` + `output_config.effort`. Only for hard problems.
- **Server tools** (web search, fetch, code exec): Anthropic runs them, no loop needed.
- **Skills** = how · **Tools** = what · **MCP** = third-party, maintained by the provider.
- **Context:** just-in-time loading, compaction, caching, memory.
- **Managed agents:** Agent → Environment → Session → Events. Open the stream first.
- **Claude Code:** name the file, the pattern and the end state, then review the diff.
