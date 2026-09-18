---
title: Post-Approval Risk Assessment (CardRT / CardNRT / Queue Tags)
type: concept
tags: [zeta, payments, fraud-risk]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[two-way-notification]]", "[[featurespace]]", "[[orcus]]", "[[atropos]]", "[[cardworks]]", "[[luminos]]"]
confidence: medium
status: seed
---

# Post-Approval Risk Assessment (CardRT / CardNRT / Queue Tags)

The pattern of evaluating a card transaction for fraud *twice*: once synchronously during
authorisation (pre-approval, **CardRT**) and again after it has been approved and completed
(post-approval, **CardNRT** — "near real time"), with the second pass returning a **queue tag**
that tells the issuer what to do about the transaction. It is how [[orcus]] and [[featurespace]]
work together for [[cardworks]] ([[two-way-notification-frm-cardworks-contract]]).

## Explanation

**Two rule sets, two calls.** The risk-evaluation diagram shows Featurespace's ARIC engine with
*Rules Set 1* (pre-approval, answered on CardRT) and *Rules Set 2* (post-approval, answered on
CardNRT). Steps as drawn ([[two-way-notification-frm-cardworks-contract]]):

1. Card network sends an auth request to the [[tachyon]] switch, which passes it to the Orcus
   Interceptor.
2. Orcus sends **CardRT Req.** to FS; FS replies with advice and, optionally, a **"FOLLOW UP"**
   tag meaning "validate this one post-approval".
3. Orcus calls back the switch with FS advice; the switch does accounting/posting checks and
   answers the network.
4. If payment is effected, the NRT transaction is published through [[atropos]] and Orcus
   sends **CardNRT Req.** to FS. For CardWorks *every* successfully authorised and completed
   transaction goes through this step. Transactions that were tagged FOLLOW UP carry
   `msgStatusReason: FOLLOWUP`.
5. **CardNRT Resp.** carries a **Queue Tag** (labelled "A" in the diagram). Orcus publishes
   the event with the FS response to the `orcus-transactions` topic; an Atropos subscription
   applies a tenant-level filter and calls a webhook that runs the queue-tag handler.
6. Communication with the customer goes out through the Notification Centre, i.e. [[luminos]].

![[risk-evaluation-flow-cw.png]]

**Queue tag → action.** From the diagrams (prose in the source only documents 2WAYNOTI):

| Queue tag | Handler |
|---|---|
| `ManualReview` | Manual review in the FS ARIC portal; incident marked Risk / No-Risk |
| `AutomatedHardBlock` | `TEMP_BLOCK` at account level (remark `AutomatedHardBlock`); customer must contact the issuer to unblock / hotlist / replace |
| `AutomatedSoftBlock` | `TEMP_BLOCK` (remark `AutomatedSoftBlock`) **and** a Luminos notification; block is removed if the customer confirms the txn as legitimate |
| `2Way Notification` | Luminos notification only; block applied only if the customer says illegitimate — see [[two-way-notification]] |
| *(no tag)* | No action |

![[queue-tag-processing-flow.png]]

**Closing the loop.** After a customer response, Orcus sends a `transactionReturn` event back to
FS (`confirmedFraud`, `msgStatus`, `returnType: ALL | FRAC`, `returnReasonCode`), which feeds
confirmed outcomes back into the risk engine ([[two-way-notification]]).

## How it connects

- [[two-way-notification]] — the most fully specified of the queue-tag actions.
- [[featurespace]] — the engine returning FOLLOW UP tags and queue tags.
- [[orcus]] — the interceptor that makes both calls and runs the handlers.
- [[atropos]] — the pub/sub layer between "payment effected" and the CardNRT call, and between
  the FS response and the handler.

## Contradictions & open questions

- The handler table beyond 2WAYNOTI is read from diagrams only; treat as medium confidence
  until a source describes those handlers in prose.
- Is CardNRT sent for *all* tenants or only CardWorks? The source scopes the "every completed
  txn" rule to CardWorks.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
