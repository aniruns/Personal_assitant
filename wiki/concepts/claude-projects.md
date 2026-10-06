---
title: Claude Projects
type: concept
tags: [ai-tools, claude, knowledge-management]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[claude-skills]]", "[[retrieval-augmented-generation]]", "[[llm-wiki-pattern]]", "[[claude]]"]
confidence: medium
status: seed
---

# Claude Projects

A self-contained workspace in [[claude]] with its own chats, knowledge base, instructions and
memory. In the course's phrase, it is where the **knowledge** lives (the "what"), while
[[claude-skills]] hold the **process**.

## Explanation

**Use it when** you keep re-uploading the same reference docs, apply the same rules every
time, or a team needs shared context ([[claude-101-course-notes]]).

**Setup** ([[claude-101-course-notes]]):
1. claude.ai/projects → New Project → name and description. Claude **does not see** the
   description; it is for humans. Choose private or shared with the org.
2. **Instructions:** context, process ("first outline, then draft"), tone, must-haves. They
   can automate behaviour: "when I upload a transcript → summarise with this template".
3. **Knowledge:** pdf/docx/csv/txt/html, or Google Drive. **Name files properly**
   ("Q4-2024-Brand-Guidelines.pdf", not "document1.pdf"), because Claude uses file names to
   find things.

**Scaling:** near the context limit a project switches to **RAG** automatically, searching and
pulling only the relevant parts. This gives roughly **10x** capacity, with an on-screen
indicator ([[claude-101-course-notes]], [[retrieval-augmented-generation]]).

**Sharing (Team/Enterprise):** can view / can edit / owner, with specific people or everyone
at the org ([[claude-101-course-notes]]).

**Tips:** start narrow, keep docs current, write clear instructions, and mention docs by name
in questions. Ideas from the course: product-launch hub, research support, client-account hub,
event planning, JD generator ([[claude-101-course-notes]]).

## How it connects

- [[claude-skills]]: process to the project's knowledge. The two stack.
- [[retrieval-augmented-generation]]: the automatic fallback at scale.
- [[llm-wiki-pattern]]: Assessment: a project is "upload raw docs plus instructions". It does
  not compile a maintained wiki, so it sits closer to the RAG side of the contrast the wiki
  pattern draws. The "name files properly" tip echoes this KB's slug conventions.
- "Ask {Org}" enterprise search is described as a pre-built project wired to company
  knowledge ([[choosing-a-claude-surface]]).

## Contradictions & open questions

- How is the RAG switch triggered exactly, and does it hurt answers that need synthesis
  across many documents? That is the [[llm-wiki-pattern]]'s core critique of RAG.

## Sources

- [[claude-101-course-notes]]
