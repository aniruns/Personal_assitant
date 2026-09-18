---
title: Atropos
type: entity
tags: [zeta, infrastructure, messaging]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[orcus]]", "[[luminous]]", "[[post-approval-risk-assessment]]", "[[two-way-notification]]"]
confidence: medium
status: seed
---

# Atropos

Zeta's pub/sub event system (topics + subscriptions) as seen in the [[orcus]]–[[featurespace]]
integration. It decouples "payment effected" from the post-approval risk call, and
[[luminous]]'s customer responses from Orcus's handling of them
([[two-way-notification-frm-cardworks-contract]]).

## What we know

- **Topics named in the source:** `orcus-transactions` (transaction events with the FS
  response, plus audit events) and `notificationWorkflowResponse` (customer answers from
  Luminous).
- **Subscriptions** carry tenant-level filters and invoke a webhook on the consumer. Named
  examples: Sub1 `_orcus_code_interceptor_featurespace_switch-authorization_600309_RESOURCE`,
  Sub2 `_orcus_code_interceptor_featurespace_queueTag-processor_600309_orcus-transactions`.
- Naming convention (inferred): `_<service>_<component>_<integration>_<handler>_<tenant>_<topic>`.
  Assessment: pattern from two examples; unverified.
- In the risk-evaluation diagram Atropos delivers "NRT Txns" to the Orcus Interceptor after
  payment is effected ([[post-approval-risk-assessment]]).

## Relationships

- Producers/consumers seen so far: [[orcus]], [[luminous]].

## Contradictions & open questions

- Underlying technology (Kafka? custom?) and delivery guarantees are not described.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
