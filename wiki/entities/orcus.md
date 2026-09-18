---
title: Orcus
type: entity
tags: [zeta, payments, orcus]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[featurespace]]", "[[luminos]]", "[[atropos]]", "[[cardworks]]", "[[post-approval-risk-assessment]]", "[[two-way-notification]]"]
confidence: medium
status: seed
---

# Orcus

A Zeta card-transaction processing system that sits between the authorisation switch and the
fraud-risk engine; the "Orcus Interceptor" component makes the risk calls to [[featurespace]]
and executes the resulting actions. Orcus has its own Confluence space (ORCUS), from which
[[two-way-notification-frm-cardworks-contract]] was clipped.

## What we know

- The **Orcus Interceptor** receives authorisation requests from the [[tachyon]] switch, calls
  Featurespace CardRT (pre-approval) and CardNRT (post-approval), and calls back the switch
  with FS advice ([[post-approval-risk-assessment]]).
- It publishes transaction events with the FS response to the [[atropos]] topic
  `orcus-transactions` and consumes them again via subscriptions whose names encode the
  component and tenant, e.g.
  `_orcus_code_interceptor_featurespace_switch-authorization_600309_RESOURCE` (Sub1) and
  `_orcus_code_interceptor_featurespace_queueTag-processor_600309_orcus-transactions` (Sub2)
  ([[two-way-notification-frm-cardworks-contract]]).
- It hosts the **queue-tag action handlers**: applying `TEMP_BLOCK` through "Ruby &
  AccountClassification", and initiating [[luminos]] workflows for
  [[two-way-notification]] / soft-block notifications.
- It hosts the **notification-response processor**, reached through an `evaluateQuestion` API
  with `domainEvent = notification-response`, and sends `transactionReturn` feedback to FS.
- Naming in the source suggests Orcus is organised as code "interceptors" per integration
  (`orcus_code_interceptor_featurespace`). Assessment: inferred from subscription names only.

## Relationships

- Calls [[featurespace]] (risk decisions) and [[luminos]] (customer notification workflows).
- Publishes to / subscribes on [[atropos]].
- Serves the [[cardworks]] tenant (among others, presumably — not stated).

## Contradictions & open questions

- What is Orcus's full scope beyond FRM integration? The source only shows the risk path.
- Relationship to "Ruby & AccountClassification" (account blocking) — named only in a
  diagram; no page yet. ([[tachyon]] now has a seed page.)

## Sources

- [[two-way-notification-frm-cardworks-contract]]
