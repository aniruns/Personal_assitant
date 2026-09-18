---
title: CardWorks (CW)
type: entity
tags: [zeta, payments, tenant]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]", "[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[orcus]]", "[[featurespace]]", "[[post-approval-risk-assessment]]", "[[two-way-notification]]", "[[luminos]]", "[[notification-channels-and-routes]]", "[[clm]]"]
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
- The [[luminos]] workflow type for CardWorks on FRM is `CWFRMWorkflow`.
- Tenant identifiers seen: `600309` (in [[atropos]] subscription names, and as the `ifiID` in
  the [[clm]] preferences sample — [[communication-preferences-in-clm-aries]]) and `600335`
  (in the sample Luminos payload's `tenantId`).
- Notification channels specific to CardWorks: the **Inbox** (in-app) channel is "specifically
  for Cardworks", and **Printed Letters** are delivered as PDFs into an SFTP owned by Sparrow
  or CardWorks, US only ([[notification-channels-and-routes]],
  [[communication-preferences-in-clm-aries]]).

## Relationships

- Served by [[orcus]]; risk-scored by [[featurespace]]; notified through [[luminos]];
  customer consent held in [[clm]].

## Contradictions & open questions

- **Conflict:** subscription names use tenant `600309`, the sample payload uses `600335`
  ([[two-way-notification-frm-cardworks-contract]]). Assessment: likely different environments
  (e.g. sandbox vs. prod) or a stale example — unresolved. `600309` recurring as an `ifiID`
  in a second source ([[communication-preferences-in-clm-aries]]) makes it the more likely
  canonical id; "ifi" (issuing financial institution) and "tenant" appear to be the same key.
- What CardWorks is as a business (issuer program? processor client?) is not stated. The
  US-only printed-letter channel and the Sparrow SFTP suggest a US card programme.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
- [[communication-preferences-in-clm-aries]]
