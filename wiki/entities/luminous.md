---
title: Luminous
type: entity
tags: [zeta, payments, notifications]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[two-way-notification]]", "[[orcus]]", "[[atropos]]", "[[cardworks]]"]
confidence: medium
status: seed
---

# Luminous

A Zeta workflow/notification service that, when initiated by [[orcus]], pushes a notification to
the customer and collects their approve/deny answer for a suspicious transaction — the
customer-facing half of [[two-way-notification]]
([[two-way-notification-frm-cardworks-contract]]).

## What we know

- API: `POST /1.0/tenants/{tenantID}/workflows/{workflowType}/initiate` with an `eventData`
  body; returns a `workflowID`. Workflow type for CardWorks-on-FRM is **`CWFRMWorkflow`**.
- Expected `eventData` fields: `accountHolderId`, `transactionId`, `cguid`, `maskedPAN`,
  `merchantName`, `transactionAmount{value,currency,baseValue,baseCurrency}`, `timestamp`,
  `tenantId`, `action` (e.g. `TWO_WAY_NOTIFICATION`), `triggeredRule` (comma-separated),
  `valueTime`, `rrn`, `resourceID`.
- After the customer responds, Luminous publishes the response to the [[atropos]] topic
  **`notificationWorkflowResponse`**, which Orcus subscribes to.
- Used for both `2WAYNOTI` and `AutomatedSoftBlock` notifications (queue-tag handler diagram).
- A separate Confluence page, "Notification Workflow Contracts with Orcus/FRM"
  (`https://zeta-tm.atlassian.net/wiki/x/E4ITzQ`), holds the sandbox details and fuller
  contract — not yet ingested.

## Relationships

- Initiated by [[orcus]]; responds via [[atropos]].
- The diagram's "Notification Centre" box is presumably Luminous or its parent system.
  Assessment: inferred, not stated.

## Contradictions & open questions

- Shape of the response event on `notificationWorkflowResponse` is not in this source.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
