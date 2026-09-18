---
title: Tachyon
type: entity
tags: [zeta, payments, platform]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]", "[[2026-09-18-luminos-notification-pcmm]]", "[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[orcus]]", "[[notification-product]]", "[[clm]]", "[[luminos-notification-center]]"]
confidence: low
status: seed
---

# Tachyon

A Zeta platform name that recurs across three sources in three roles: the **Tachyon switch**
that receives card-network authorisation requests ahead of [[orcus]], the **Tachyon product /
product bundle** that a [[notification-product]] can be mapped to, and the `mars/tachyon/v4`
**API namespace** under which [[clm]] exposes account-holder endpoints. Assessment: Tachyon is
probably Zeta's core banking/issuing platform, of which the switch, the product catalogue and
the API surface are all parts — but no source defines it, hence `confidence: low`.

## What we know

- Card Network → Tachyon Switch (auth checks) → Orcus Interceptor, in the CardWorks
  risk-evaluation diagram ([[two-way-notification-frm-cardworks-contract]]).
- A notification product is created "along with the mapping to a tachyon product (if
  applicable)" (`LNS_NPM_001` / `LNC_NPM_001`); LNC adds product-*bundle* mapping
  (`LNC_NPM_002`, P2) ([[luminos-notification-pcmm]]).
- CLM's preference-update endpoint lives at `…/mars/tachyon/v4/ifi/{ifiID}/accountholders/…`
  ([[communication-preferences-in-clm-aries]]).

## Relationships

- Fronts [[orcus]] in authorisation; underlies [[clm]]'s API; referenced by [[luminos]]
  product configuration.

## Contradictions & open questions

- What exactly is a "Tachyon product" vs a "product bundle"? No source says.

## Sources

- [[two-way-notification-frm-cardworks-contract]]
- [[luminos-notification-pcmm]]
- [[communication-preferences-in-clm-aries]]
