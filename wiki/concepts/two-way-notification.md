---
title: Two-Way Notification (2WAYNOTI)
type: concept
tags: [zeta, payments, fraud-risk]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[post-approval-risk-assessment]]", "[[orcus]]", "[[luminous]]", "[[featurespace]]", "[[atropos]]", "[[cardworks]]"]
confidence: high
status: seed
---

# Two-Way Notification (2WAYNOTI)

A fraud-control action in which the issuer asks the cardholder, via a push notification, to
confirm whether a transaction was legitimate, then acts on the answer. In this KB it is the
`2WAYNOTI` / `TWO_WAY_NOTIFICATION` queue-tag action that [[featurespace]] can return during
[[post-approval-risk-assessment]], fulfilled by [[orcus]] through [[luminous]]
([[two-way-notification-frm-cardworks-contract]]).

## Explanation

**Trigger.** After a [[cardworks]] transaction is authorised and completed, Orcus sends it to
Featurespace via CardNRT. If the response's queue tag is `2WAYNOTI`, Orcus initiates a Luminous
workflow ([[two-way-notification-frm-cardworks-contract]]).

**Outbound (Orcus → Luminous).**
`POST /1.0/tenants/{tenantID}/workflows/CWFRMWorkflow/initiate` with an `eventData` object
carrying the account holder, transaction id, `cguid`, masked PAN, merchant name, amount
(value + base value/currency), timestamp, tenant id, `action: TWO_WAY_NOTIFICATION`, the
triggered rule(s), `valueTime`, `rrn`, and `resourceID`. Luminous responds with a `workflowID`.
Unlike `AutomatedSoftBlock`, no block is placed on the account before asking the customer
(queue-tag handler diagram).

**Inbound (customer → Luminous → Atropos → Orcus).** The customer's approve/deny answer is
published by Luminous to the [[atropos]] topic `notificationWorkflowResponse`. Orcus's
subscription (Sub2) reads it and invokes an `evaluateQuestion` API with
`domainEvent = notification-response` (response-processor diagram).

**Outcome.**

| Customer says | Account action | Feedback to Featurespace (`transactionReturn`) |
|---|---|---|
| Legitimate | No blocking needed | `confirmedFraud: FALSE`, `msgStatus: Legitimate`, `returnType: ALL` |
| Illegitimate | `TEMP_BLOCK` applied via Ruby & AccountClassification | `confirmedFraud: TRUE`, `msgStatus: Fraud`, `returnType: FRAC` |

In both cases `returnReasonCode` is the triggered rule name and an audit event is published to
the `orcus-transactions` topic ([[two-way-notification-frm-cardworks-contract]]).

![[notification-response-processor.png]]

## How it connects

- [[post-approval-risk-assessment]] — the flow that produces the queue tag; 2WAYNOTI is one of
  five possible actions (alongside ManualReview, AutomatedHardBlock, AutomatedSoftBlock, none).
- [[luminous]] — runs the customer-facing notification workflow (`CWFRMWorkflow`).
- [[atropos]] — carries both the inbound transaction events and the customer-response events.
- [[orcus]] — owns both the outbound call and the response processor.

## Contradictions & open questions

- What happens on **no response** (timeout)? Not covered by the source.
- How is the Luminous response **correlated** to the original transaction — `workflowID`,
  `transactionId`, or `resourceID`? Not stated.
- The source's prose says the possible actions are "Account Block / no action"; the diagram
  shows `TEMP_BLOCK` specifically. Assessment: TEMP_BLOCK is the concrete mechanism.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
