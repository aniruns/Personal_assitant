---
title: "Luminos Notification (LNS / LNC) — PCMM capability matrix"
type: source
tags: [zeta, notifications, luminos, product-management]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]"]
related: ["[[luminos]]", "[[luminos-notification-system]]", "[[luminos-notification-center]]", "[[receiver-preference-order]]", "[[notification-product]]", "[[notification-channels-and-routes]]", "[[pcmm]]"]
confidence: high
status: seed
author: unknown (Zeta internal; pasted into chat by the user)
published: unknown
url: n/a
source_type: dataset
---

# Luminos Notification (LNS / LNC) — PCMM capability matrix

A 29-row tab-separated capability matrix — a [[pcmm]] — for Zeta's [[luminos]] notification
platform, pasted by the user on 2026-09-18. It decomposes Luminos into two **modules**,
[[luminos-notification-system|Luminos Notification System (LNS)]] and
[[luminos-notification-center|Luminos Notification Center (LNC)]], each with four
**capabilities** (Notification Product Management, Receiver Management, Channel & Provider
Management, Communication Trigger & Delivery) broken into **features** with a priority
(P1–P3). Every module and capability is at maturity level **Beta**. The `Feature_Guidance`
column is empty throughout. It is the KB's first product-level description of Luminos
(the earlier [[two-way-notification-frm-cardworks-contract]] only saw it as an API).

## Key claims

- Luminos is split into two modules, both Beta: **LNS** (system) and **LNC** (center). Both
  share the same four capability codes (`NPM`, `RCM`, `CPM`, `CTD`) but list different
  features under them.
- A **[[notification-product]]** is created with a name, description, receiver preferences at
  the product level, and an optional mapping to a [[tachyon]] product (`LNS_NPM_001`,
  `LNC_NPM_001`, both P1). LNC adds product-to-Tachyon *product bundle* mapping (`LNC_NPM_002`,
  P2) and per-product language management (`LNC_NPM_003`, P2).
- **Receiver Management** defines a receiver's *communication vectors* ("points of contact")
  within a product (`LNS_RCM_001`, P1) and the **[[receiver-preference-order]]** — "the
  communication vector preference order for a product, event and an individual receiver"
  (`LNS_RCM_002`, P1). LNC states the same at "product and message definition (Template)
  level" (`LNC_RCM_001`, P1) and allows overriding the order for a given template
  (`LNC_RCM_002`, P2).
- **Channels vs routes:** "Channels are the modes of communication and Routes define the
  path of delivery" ([[notification-channels-and-routes]]). LNC manages route plans per
  channel / provider route configuration (`LNC_CPM_002`, P1) and route priority per
  communication (`LNC_CPM_003`, P2).
- Channel/provider features and priorities (LNS_CPM): Email — SendGrid P1, SMTP/Gmail/HTTP
  P3; SMS — [[twilio]] P1, ACL/Plivo P3; Push P1; WhatsApp (Twilio) P1; **"2 Way
  Communication as a Channel (Flow integration Twilio)"** P1 (`LNS_CPM_006`); onboarding a new
  provider for any channel — SMS, PUSH, INBOX, EMAIL, PRINTED LETTERS, SPOTLIGHT — P1
  (`LNS_CPM_007`).
- **Trigger & delivery (LNS_CTD):** send through all configured channels via the configured
  routes (P1); delivery-status tracking via callback (P2); "Call to Action registration" (P3).
  LNC's CTD features are all about *message definitions (templates)*: channel management per
  template (P1), test-sending a template via a channel+vendor combination (P2), template
  lifecycle management (P2).

## Notable quotes

> Ability to provide the Communication vector preference order for a product, event and an
> individual receiver

> Channels are the modes of communication and Routes define the path of delivery

## Assessment

Reliable as a statement of *scope and priority* (it is the kind of artifact a product team
maintains), but it is a list, not a design: it never defines "communication vector", "event",
"message definition", or how the three preference levels combine. LNS vs LNC is not explained
either — the feature mix (LNS holds runtime send/track features, LNC holds only configuration
features) suggests LNS is the engine and LNC the admin console, but that is my inference.
"Event" (LNS) and "message definition (Template)" (LNC) appear to name the same preference
level; treated as synonyms with medium confidence. The user's original request referred to an
"LN Including product and event level preferences" SharePoint doc, which is presumably the
design behind `LNS_RCM_002` — still to be ingested.

Confirms, from a second source, the channel list in [[communication-preferences-in-clm-aries]]
(SMS, Email, Inbox, Printed Letters, Push, Spotlight) and the Twilio/Plivo/ACL/SendGrid vendor
set. Also establishes the spelling **Luminos** (the Orcus contract wrote "Luminous").

## Wiki changes

- Created: [[luminos-notification-system]], [[luminos-notification-center]],
  [[notification-product]], [[receiver-preference-order]],
  [[notification-channels-and-routes]], [[pcmm]], [[tachyon]], [[twilio]]
- Updated: [[luminos]] (renamed from `luminous`; rewritten around the module/capability
  model), [[two-way-notification]] (2-way as a Luminos channel; delivery-channel question),
  [[overview]], [[index]]

## Raw

[[2026-09-18-luminos-notification-pcmm]]
