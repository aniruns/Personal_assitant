# Overview

The living map of this knowledge base: what it covers, what it currently believes, and what it
doesn't know yet. Rewritten by the agent whenever a source shifts the big picture.
See [[index]] for the full catalog and [[log]] for the timeline.

## What this KB is

A personal second brain maintained by an LLM agent following the [[llm-wiki-pattern]]. Raw
sources go in `raw/`, the agent compiles them into the pages under `wiki/`, and `CLAUDE.md` is
the schema. Started 2026-09-17.

## Domains so far

| Domain | Pages | State |
|---|---|---|
| Knowledge management & LLM agents (meta — how this KB works) | [[llm-wiki-pattern]], [[retrieval-augmented-generation]], [[memex]], [[obsidian]], [[qmd]], [[vannevar-bush]] | 1 source; seed |
| Zeta card payments & fraud risk (work) | [[post-approval-risk-assessment]], [[two-way-notification]], [[orcus]], [[featurespace]], [[atropos]], [[cardworks]], [[tachyon]] | 1 source; seed |
| Zeta notifications & customer consent (work) | [[luminos]], [[luminos-notification-system]], [[luminos-notification-center]], [[notification-product]], [[receiver-preference-order]], [[communication-preferences]], [[notification-message-types]], [[notification-channels-and-routes]], [[point-of-presence]], [[clm]], [[twilio]], [[pcmm]] | 2 sources; growing |
| Using AI tools well — Claude (personal learning) | [[claude]], [[prompting-fundamentals]], [[ai-fluency]], [[lightweight-evals]], [[claude-projects]], [[claude-skills]], [[claude-connectors]], [[claude-artifacts]], [[claude-code]], [[claude-cowork]], [[claude-in-chrome]], [[model-context-protocol]], [[choosing-a-claude-surface]] | 1 source (course notes); seed |

## Current theses

1. Compiling knowledge once and maintaining it beats re-deriving it per query
   ([[llm-wiki-pattern]] vs. [[retrieval-augmented-generation]]). *Held on one source; the
   founding assumption of this KB — to be tested by use.*
2. In Zeta's card stack, fraud control is a two-pass loop: [[featurespace]] scores pre- and
   post-approval, [[orcus]] executes the returned queue-tag action, and confirmed outcomes are
   fed back to the engine ([[post-approval-risk-assessment]]). *Held on one design contract.*
3. Notification preferences at Zeta are two separate layers that must be combined at send
   time: **consent** (what the customer allows, per address and message type — owned by
   [[clm]] as [[communication-preferences]]) and **delivery preference** (which contact vector
   to try first, at product / event / receiver level — owned by [[luminos]] as the
   [[receiver-preference-order]]). *Each layer held on one source; the combination rule is
   nowhere documented — the biggest open question in this domain.*
4. Getting value from an AI assistant is less about clever prompts than about **picking the
   right surface for the shape of the work and iterating** — stage/task/rules, then specific
   feedback, then verification ([[prompting-fundamentals]], [[ai-fluency]],
   [[choosing-a-claude-surface]]). *Held on one vendor course; the user's own reflection is that
   they still hand over whole tasks one question at a time.*

## Open questions

- Does index-first retrieval still work at ~30+ sources, or is [[qmd]] needed sooner?
- What domains will this KB actually accumulate? (Next ingests will tell.)
- Primary sources to add: Bush's "As We May Think" for [[memex]].
- Payments domain gaps: [[two-way-notification]] timeout/correlation behaviour and its
  delivery channel; the linked "Notification Workflow Contracts with Orcus/FRM" and
  "Solutioning" docs; what [[tachyon]] really is (three roles seen, no definition) and what
  "Ruby & AccountClassification" is; the [[cardworks]] tenant-id discrepancy.
- Notifications domain gaps: how [[luminos]] combines CLM consent with its own preference
  order; the CLM → Luminos event contract; whether "event" (LNS) = "message definition /
  template" (LNC); the still-unread SharePoint design doc "LN Including product and event
  level preferences" (its clipping came back empty — needs a docx export or paste).

- AI-tools domain gaps: the original AI Fluency material ([[ai-fluency]]); an MCP primary
  source ([[model-context-protocol]]); how [[claude-projects]]' RAG fallback affects
  cross-document synthesis; which surfaces the user actually adopts at work.

## Stats

- Sources: 5 · Entities: 18 · Concepts: 19 · Syntheses: 1 · Last ingest: 2026-10-06
