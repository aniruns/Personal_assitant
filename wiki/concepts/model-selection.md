---
title: Model selection
type: concept
tags: [ai-tools, claude, api, evaluation]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude]]", "[[claude-platform]]", "[[lightweight-evals]]", "[[extended-thinking]]"]
confidence: medium
status: seed
---

# Model selection

How to choose which Claude model handles a task. The course's rule: **the right model is the
cheapest one whose output you'd actually ship** ([[claude-platform-101-course-notes]]).

## Explanation

**The tiers** (as of the course date) ([[claude-platform-101-course-notes]]):

| Model | Use for | Trade-off |
|---|---|---|
| **Fable** | the hardest problems; a new tier above Opus | much more expensive than Opus |
| **Opus** | deep reasoning, complex analysis, multi-step coding, nuanced writing | slowest and most expensive of the core three |
| **Sonnet** | most production work | balanced |
| **Haiku** | high-volume simple work: classification, extraction, routing | fastest, cheapest |

**The method** ([[claude-platform-101-course-notes]]):
1. Build a small eval: **20–30 real examples** from your workload, plus a definition of "good".
2. Run it on **Haiku first**. If good enough, stop.
3. Otherwise try Sonnet; use Opus only if you need it.

**Route per task:** in a real app each task gets its own model, e.g. classify with Haiku, draft
with Sonnet, write RFP responses with Opus. `response.usage` shows the input and output tokens
you are billed for ([[claude-platform-101-course-notes]]).

## How it connects

- The eval step is [[lightweight-evals]] with a bigger sample and a cost question attached.
- [[extended-thinking]] is the other dial for hard tasks.
- Assessment: this KB runs on a frontier model for ingest (judgement-heavy writing), which fits
  the table; mechanical checks are already offloaded to `scripts/lint.py`.

## Contradictions & open questions

- **Sample size:** 20–30 examples here vs. 5–10 in [[lightweight-evals]]
  ([[claude-101-course-notes]]). Assessment: not a real conflict. 5–10 checks whether *any*
  prompt works for a task you do by hand; 20–30 compares models for production, where small
  quality differences matter.
- Model names and the Fable tier are time-sensitive.

## Sources

- [[claude-platform-101-course-notes]]
