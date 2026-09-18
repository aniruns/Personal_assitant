---
title: CLM (Aries)
aliases: [Aries]
type: entity
tags: [zeta, clm, consent]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[communication-preferences]]", "[[point-of-presence]]", "[[luminos]]", "[[tachyon]]", "[[cardworks]]"]
confidence: medium
status: seed
---

# CLM (Aries)

Zeta's customer/account-holder lifecycle system — "CLM" — documented in the **Aries**
Confluence space and served from an `aries.internal.…zetaapps.in` host. In this KB it matters
as the **system of record for customer consent**: it holds each account holder's
[[communication-preferences]] and pushes them to [[luminos]]
([[communication-preferences-in-clm-aries]]). The expansion of "CLM" is not given by the
source (assessment: Customer Lifecycle Management).

## What we know

- Models an account holder as a set of [[point-of-presence|points of presence]] (labelled
  Billing / Communication / Home …), each with typed addresses (Postal, Email, Phone).
- Stores communication preferences as `COMMUNICATION_PREFERENCE` tags on each address, with
  a parent `isCommunicationAllowed` flag per address.
- Exposes `POST /mars/tachyon/v4/ifi/{ifiID}/accountholders/{accountHolderId}/communicationPreferences/update`
  (pre-prod host `aries.internal.mum1-pp.zetaapps.in`, auth via `X-Zeta-AuthToken`) to change
  preferences after onboarding. The path's `mars/tachyon/v4` segment suggests CLM sits on the
  [[tachyon]] API surface.
- Publishes an event when preferences change; the Notifications Centre (Luminos) consumes it
  and CLM's version overrides Luminos's copy.
- `ifi` = the issuer identifier used as tenant scope; the sample uses `600309`
  ([[cardworks]] uses the same number as a tenant id in the Orcus contract).

## Relationships

- Upstream of [[luminos]] for consent.
- Same tenant scope (`ifiID`) as [[orcus]] / [[cardworks]] integrations.

## Contradictions & open questions

- Is "Aries" the CLM product's name, the team's, or the space's? Unclear.
- Event contract between CLM and Luminos is not documented anywhere ingested so far.

## Sources

- [[communication-preferences-in-clm-aries]]
