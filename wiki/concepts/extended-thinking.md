---
title: Extended thinking
type: concept
tags: [ai-tools, claude, api, reasoning]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-platform-notes]]", "[[2026-10-06-claude-101-notes]]"]
related: ["[[claude]]", "[[claude-platform]]", "[[model-selection]]", "[[choosing-a-claude-surface]]"]
confidence: medium
status: seed
---

# Extended thinking

Claude reasons step by step **before** answering, and the reasoning is visible in the response
as thinking blocks ([[claude-platform-101-course-notes]]). In the chat app it is the
"Thinking" toggle ([[claude-101-course-notes]]); on the [[claude-platform]] it is a request
parameter.

## Explanation

**Turning it on** (Opus 4.7, adaptive thinking, as of the course date)
([[claude-platform-101-course-notes]]):

```python
thinking={"type": "adaptive"},
output_config={"effort": "high"},   # low | medium | high (default) | xhigh | max
```

- **No token budget** with adaptive thinking: Claude decides when to think and how much.
- *Gotcha:* `effort` goes **inside `output_config`**, not next to `thinking`.

| Use thinking for | Skip it for |
|---|---|
| Maths, multi-step logic | Simple classification |
| Debugging code | Extraction |
| Regulatory analysis | Boilerplate |
| Trade-offs, comparing options | (adds only latency and cost here) |

Source: [[claude-platform-101-course-notes]].

## How it connects

- Same rule in the chat app: Thinking is the right tool for "pure reasoning: maths, debugging,
  logic" ([[choosing-a-claude-surface]], [[claude-101-course-notes]]).
- It's a cost lever alongside [[model-selection]]: turn up thinking or move up a model tier.
  Assessment: the course doesn't say which to try first.
- Thinking blocks are one of the block types in a response, and they count toward context
  ([[context-management]]).

## Contradictions & open questions

- Which models support adaptive thinking, and how effort maps to cost, isn't in the notes.

## Sources

- [[claude-platform-101-course-notes]]
- [[claude-101-course-notes]]
