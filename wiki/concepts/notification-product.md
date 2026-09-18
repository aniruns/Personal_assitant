---
title: Notification Product
type: concept
tags: [zeta, notifications, luminos]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]"]
related: ["[[luminos]]", "[[receiver-preference-order]]", "[[tachyon]]", "[[luminos-notification-center]]", "[[luminos-notification-system]]"]
confidence: medium
status: seed
---

# Notification Product

The top-level configuration unit in [[luminos]]: a named scope inside which receivers, their
communication vectors, the default [[receiver-preference-order]], message definitions
(templates) and languages are defined. Created "by providing Product name and description
along with the receiver preferences at the product level along with the mapping to a tachyon
product (if applicable)" ([[luminos-notification-pcmm]]).

## Explanation

What a product carries, per the PCMM feature list:

- **Identity** — name and description (`LNS_NPM_001` / `LNC_NPM_001`, P1).
- **Product-level receiver preferences** — the default vector order for the product; see
  [[receiver-preference-order]].
- **Receivers and their vectors** — Receiver Management is scoped "within a product"
  (`LNS_RCM_001`), so the same person may be a different receiver in two products.
- **Mapping to a [[tachyon]] product** (optional) and, in LNC, to a Tachyon *product bundle*
  (`LNC_NPM_002`, P2). Assessment: this ties notification configuration to the banking
  product (e.g. a card programme) it serves.
- **Languages** (`LNC_NPM_003`, P2).
- **Message definitions / templates**, each with its own channel configuration and test setup
  (`LNC_CTD_001–003`) and optional preference override (`LNC_RCM_002`).

Assessment: for a tenant like [[cardworks]] a notification product probably corresponds to a
card programme, so that the fraud-check messages of [[two-way-notification]] are one template
within it — inferred, not stated.

## How it connects

- [[receiver-preference-order]] — product level is the widest of the three preference levels.
- [[tachyon]] — the product catalogue a notification product maps onto.
- [[luminos-notification-center]] — where most product-management features live.

## Contradictions & open questions

- Product vs tenant: is a product tenant-scoped (one CardWorks = many products) or can one
  product span tenants? Not stated.

## Sources

- [[luminos-notification-pcmm]]
