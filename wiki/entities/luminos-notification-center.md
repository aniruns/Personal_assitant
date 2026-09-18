---
title: Luminos Notification Center (LNC)
aliases: [Notifications Centre, Notification Centre]
type: entity
tags: [zeta, notifications, luminos]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]", "[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[luminos]]", "[[luminos-notification-system]]", "[[notification-product]]", "[[receiver-preference-order]]", "[[notification-channels-and-routes]]", "[[tachyon]]"]
confidence: medium
status: seed
---

# Luminos Notification Center (LNC)

The second module of [[luminos]] in the [[luminos-notification-pcmm]] (module code `LNC`,
maturity Beta). Every LNC feature is a *management* task — products, templates, route plans,
preference overrides — so it reads as the admin/configuration console over the
[[luminos-notification-system|LNS]] engine. Probably the same thing older documents call the
"Notification(s) Centre" ([[communication-preferences-in-clm-aries]],
[[two-way-notification-frm-cardworks-contract]] diagram). Assessment: both identifications
are inferred.

## What we know

All capabilities are Beta. Features and priorities ([[luminos-notification-pcmm]]):

| Capability | Code | Feature | Priority |
|---|---|---|---|
| Notification Product Management | `LNC_NPM_001` | [[notification-product]] lifecycle management | P1 |
| Notification Product Management | `LNC_NPM_002` | Notification product → [[tachyon]] product *bundle* mapping | P2 |
| Notification Product Management | `LNC_NPM_003` | Managing the languages for a notification product | P2 |
| Receiver Management | `LNC_RCM_001` | [[receiver-preference-order|Receiver preference]] management at product and message-definition (template) level | P1 |
| Receiver Management | `LNC_RCM_002` | Override receiver preference order for a given message definition (template) | P2 |
| Channel & Provider Mgmt | `LNC_CPM_001` | Channel lifecycle management | P1 |
| Channel & Provider Mgmt | `LNC_CPM_002` | Route-plan management for a channel; provider route configuration | P1 |
| Channel & Provider Mgmt | `LNC_CPM_003` | Route priority management for a given communication | P2 |
| Trigger & Delivery | `LNC_CTD_001` | Communication-channel management for a message definition (template) | P1 |
| Trigger & Delivery | `LNC_CTD_002` | Test setup of a message definition via a channel + vendor combination | P2 |
| Trigger & Delivery | `LNC_CTD_003` | Message-definition lifecycle management | P2 |

Notable: **message definitions (templates)** only appear on the LNC side, and the LNC
preference features are phrased at "template" level where LNS says "event" level.

## Relationships

- Configures what [[luminos-notification-system]] executes.
- Where the Aries page says the "Notifications centre updates communication preferences based
  on the event published by CLM", this is the module it presumably means — see
  [[communication-preferences]].

## Contradictions & open questions

- "Event" (LNS) vs "message definition / template" (LNC) as the middle preference level:
  synonyms, or is an event a trigger that selects a template? Not resolved by either source.

## Sources

- [[luminos-notification-pcmm]]
- [[communication-preferences-in-clm-aries]]
