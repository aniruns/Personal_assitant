---
title: CardWorks (CW)
type: entity
tags: [zeta, payments, tenant]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]"]
related: ["[[orcus]]", "[[featurespace]]", "[[post-approval-risk-assessment]]", "[[two-way-notification]]", "[[luminous]]"]
confidence: medium
status: seed
---

# CardWorks (CW)

A tenant on Zeta's card platform for which the [[featurespace]] FRM integration — including
[[two-way-notification]] — was specified. The source is a per-tenant contract: its rules
(e.g. "every completed txn goes to CardNRT") are scoped to CardWorks
([[two-way-notification-frm-cardworks-contract]]).

## What we know

- Every successfully authorised and completed CardWorks transaction is sent to Featurespace via
  CardNRT ([[post-approval-risk-assessment]]).
- The [[luminous]] workflow type for CardWorks on FRM is `CWFRMWorkflow`.
- Tenant identifiers seen in the source: `600309` (in [[atropos]] subscription names) and
  `600335` (in the sample Luminous payload's `tenantId`).

## Relationships

- Served by [[orcus]]; risk-scored by [[featurespace]]; notified through [[luminous]].

## Contradictions & open questions

- **Conflict:** subscription names use tenant `600309`, the sample payload uses `600335`
  ([[two-way-notification-frm-cardworks-contract]]). Assessment: likely different environments
  (e.g. sandbox vs. prod) or a stale example — unresolved.
- What CardWorks is as a business (issuer program? processor client?) is not stated.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
