---
title: Featurespace (FS / ARIC)
type: entity
tags: [zeta, payments, fraud-risk, vendor]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[post-approval-risk-assessment]]", "[[two-way-notification]]", "[[orcus]]", "[[cardworks]]"]
confidence: medium
status: seed
---

# Featurespace (FS / ARIC)

The fraud risk management (FRM) engine that [[orcus]] integrates with; referred to as "FS" and
"ARIC (FS)" in the source. It scores card transactions before and after approval and returns
tags telling the issuer what to do ([[two-way-notification-frm-cardworks-contract]]).

## What we know

- Exposes two calls used by Orcus: **CardRT** (real-time, pre-approval, "Rules Set 1") and
  **CardNRT** (near-real-time, post-approval, "Rules Set 2") — see
  [[post-approval-risk-assessment]].
- CardRT responses can carry a **FOLLOW UP** tag; CardNRT responses carry a **Queue Tag**
  (`ManualReview`, `AutomatedHardBlock`, `AutomatedSoftBlock`, `2WAYNOTI`, or none).
- Has an **ARIC portal** where `ManualReview` cases are worked and incidents marked
  Risk / No-Risk (diagram).
- Receives outcome feedback from Orcus as `transactionReturn` events
  (`confirmedFraud`, `msgStatus`, `returnType: ALL | FRAC`, `returnReasonCode` = triggered rule)
  after a [[two-way-notification]] resolves.
- "ARIC" is Featurespace's product name for its risk engine. Assessment: the source uses the
  labels together ("ARIC (FS)"); the expansion is from general knowledge, not the source.

## Relationships

- Called by [[orcus]]; decisions apply per tenant, here [[cardworks]].

## Contradictions & open questions

- Which rules trigger FOLLOW UP vs. each queue tag is not documented here.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
