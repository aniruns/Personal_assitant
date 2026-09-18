---
title: "Two way notification Integration with FRM for CardWorks: Contract (Orcus)"
type: source
tags: [zeta, payments, fraud-risk, orcus]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[two-way-notification]]", "[[post-approval-risk-assessment]]", "[[orcus]]", "[[featurespace]]", "[[luminous]]", "[[atropos]]", "[[cardworks]]"]
confidence: high
status: seed
author: unknown (Zeta ORCUS Confluence space; page author not captured by the clipper)
published: unknown (embedded screenshots are dated 2024-10-21/22, so likely Oct 2024)
url: https://zeta-tm.atlassian.net/wiki/spaces/ORCUS/pages/3456008473/Two+way+notification+Integration+with+FRM+for+CardWorks+Contract
source_type: article
---

# Two way notification Integration with FRM for CardWorks: Contract (Orcus)

An internal Zeta Confluence design contract (ORCUS space) describing how [[orcus]] integrates
with the [[featurespace]] fraud-risk engine for the [[cardworks]] tenant, and in particular how
the **2WAYNOTI** queue-tag action is fulfilled by asking the customer to approve or decline a
suspicious transaction through [[luminous]]. It covers the [[post-approval-risk-assessment]]
flow (CardRT → CardNRT → queue tag), the payload Orcus sends to Luminous, and how the customer's
response is processed back into account blocks and fraud feedback to Featurespace. Clipped with
Obsidian Web Clipper on 2026-09-18; three architecture/sequence diagrams were saved alongside
it in `raw/assets/two-way-notification-frm-cardworks/`.

## Key claims

- For CardWorks, every **successfully authorised and completed** transaction is sent to
  Featurespace a second time via the **CardNRT** API (the post-approval "near-real-time" call),
  in addition to the pre-approval **CardRT** call made during authorisation.
- The CardRT response may carry a **"FOLLOW UP"** tag; for those transactions Orcus adds
  `msgStatusReason: FOLLOWUP` to the CardNRT event it sends to Featurespace.
- The CardNRT response carries a **Queue Tag** naming the action to take against the user.
  The diagram lists five outcomes: `ManualReview`, `AutomatedHardBlock`, `AutomatedSoftBlock`,
  `2Way Notification`, and no tag (no action).
- For `2WAYNOTI`, Orcus calls Luminous `POST /1.0/tenants/{tenantID}/workflows/{workflowType}/initiate`
  with workflowType `CWFRMWorkflow`; Luminous runs a workflow that notifies the customer and
  returns a `workflowID`.
- The Luminous payload (`eventData`) carries: `accountHolderId`, `transactionId`, `cguid`,
  `maskedPAN`, `merchantName`, `transactionAmount` (value/currency/baseValue/baseCurrency),
  `timestamp`, `tenantId`, `action: TWO_WAY_NOTIFICATION`, `triggeredRule`, `valueTime`,
  `rrn`, `resourceID`.
- Once the customer responds, Luminous publishes to the [[atropos]] topic
  `notificationWorkflowResponse`; Orcus subscribes (Sub2) and takes action — account block or
  no action — based on the response.
- Two Atropos subscriptions are named: Sub1
  `_orcus_code_interceptor_featurespace_switch-authorization_600309_RESOURCE` and Sub2
  `_orcus_code_interceptor_featurespace_queueTag-processor_600309_orcus-transactions`.
- (Diagram) Queue-tag handlers: `AutomatedHardBlock` and `AutomatedSoftBlock` both apply a
  `TEMP_BLOCK` at account level via "Ruby & AccountClassification" with the tag name as remark;
  SoftBlock additionally pushes a Luminous notification; 2WAYNOTI only pushes the notification.
- (Diagram) Response processing: for a **legitimate** answer, a prior soft block is deleted (or
  nothing is done for 2WAYNOTI) and a `transactionReturn` event is sent to FS with
  `confirmedFraud: FALSE, msgStatus: Legitimate, returnType: ALL`; for an **illegitimate**
  answer, a `TEMP_BLOCK` is applied (or kept) and `transactionReturn` carries
  `confirmedFraud: TRUE, msgStatus: Fraud, returnType: FRAC`. `returnReasonCode` is the
  triggered rule name. An audit event is also published to `orcus-transactions`.
- (Diagram) Orcus reaches the response handler through an `evaluateQuestion` API with
  `domainEvent = notification-response`.
- (Diagram) The surrounding authorisation path: Card Network → Tachyon Switch (auth checks) →
  Orcus Interceptor → CardRT to FS "ARIC" (Rules Set 1, pre-approval) → callback with FS
  advice → posting/accounting checks → NRT txns via Atropos → CardNRT to FS (Rules Set 2,
  post-approval) → communication with customer via Notification Centre.

## Notable quotes

> For Cardworks, each **successfully authorised** and **completed** transaction **will be sent
> to FS again in the CardNRT API** request.

> For the `2WAYNOTI` action tag, make a call to **Luminous**, which will initiate a workflow to
> send the notification to the user.

## Assessment

Strong on the *contract* (payload shape, endpoint, topic names, subscription names) and on the
end-to-end flow thanks to the three diagrams. Weak on rationale: no discussion of timeouts
(what if the customer never answers?), idempotency, retries, or how Luminous's response is
correlated back to the transaction (presumably `workflowID` / `transactionId`, but not stated).
Several linked documents (sequence diagram in Google Docs, "Notification Workflow Contracts
with Orcus/FRM", a "Solutioning" .docx) were not captured — they'd be natural follow-up ingests.

Inconsistency to note: the Atropos subscription names embed tenant `600309`, while the sample
Luminous payload uses `tenantId: 600335`. Could be two environments/tenants or a stale example.
Filed under [[cardworks]] as an open question.

The page's text says "Based on the Queue Tag take actions" but only documents 2WAYNOTI in
prose; the other handlers exist only in the diagram. Treated as medium-confidence claims.

## Wiki changes

- Created: [[two-way-notification]], [[post-approval-risk-assessment]], [[orcus]],
  [[featurespace]], [[luminous]], [[atropos]], [[cardworks]]
- Updated: [[overview]] (new domain: Zeta card payments & fraud risk), [[index]]

## Raw

[[2026-09-18-two-way-notification-frm-cardworks]] — diagrams:
`raw/assets/two-way-notification-frm-cardworks/{risk-evaluation-flow-cw,queue-tag-processing-flow,notification-response-processor}.png`
