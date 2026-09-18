---
title: Luminos Notification System (LNS)
type: entity
tags: [zeta, notifications, luminos]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]"]
related: ["[[luminos]]", "[[luminos-notification-center]]", "[[receiver-preference-order]]", "[[notification-channels-and-routes]]", "[[twilio]]", "[[two-way-notification]]"]
confidence: medium
status: seed
---

# Luminos Notification System (LNS)

One of the two modules of [[luminos]] in the [[luminos-notification-pcmm]] (module code `LNS`,
maturity Beta). Its feature list mixes configuration with runtime delivery, so it is best read
as the notification *engine* — the part that holds products, receivers, channels and routes
and actually sends and tracks messages. Assessment: the engine/console reading is inferred;
the source only lists features.

## What we know

All capabilities are Beta. Features and priorities ([[luminos-notification-pcmm]]):

| Capability | Code | Feature | Priority |
|---|---|---|---|
| Notification Product Management | `LNS_NPM_001` | [[notification-product]] lifecycle management | P1 |
| Receiver Management | `LNS_RCM_001` | Receiver lifecycle management (communication vectors / points of contact per receiver within a product) | P1 |
| Receiver Management | `LNS_RCM_002` | [[receiver-preference-order|Receiver preference management]] — vector preference order for a product, an event, and an individual receiver | P1 |
| Channel & Provider Mgmt | `LNS_CPM_001` | Channel lifecycle management | P1 |
| Channel & Provider Mgmt | `LNS_CPM_002` | Email channel — SendGrid (P1); SMTP, Gmail, HTTP (P3) | P1/P3 |
| Channel & Provider Mgmt | `LNS_CPM_003` | SMS channel — [[twilio]] (P1); ACL, Plivo (P3) | P1/P3 |
| Channel & Provider Mgmt | `LNS_CPM_004` | Push notification management | P1 |
| Channel & Provider Mgmt | `LNS_CPM_005` | WhatsApp channel (Twilio) | P1 |
| Channel & Provider Mgmt | `LNS_CPM_006` | **2-way communication as a channel** (Twilio Flow integration) | P1 |
| Channel & Provider Mgmt | `LNS_CPM_007` | Onboard a new provider for any channel: SMS, PUSH, INBOX, EMAIL, PRINTED LETTERS, SPOTLIGHT | P1 |
| Trigger & Delivery | `LNS_CTD_001` | Send through all configured channels via configured routes | P1 |
| Trigger & Delivery | `LNS_CTD_002` | Delivery-status tracking via callback | P2 |
| Trigger & Delivery | `LNS_CTD_003` | Call-to-action registration | P3 |

Reading the priorities: the P1 set is a single vendor per channel (SendGrid, Twilio ×3, push)
plus generic provider onboarding; alternative vendors are P3. Delivery tracking is only P2,
so "sent" may be the only reliable state in the Beta.

## Relationships

- Sibling module: [[luminos-notification-center]] (same capability codes, config-only features).
- `LNS_CPM_006` is the likely mechanism behind [[two-way-notification]] — see the open
  question there about which channel 2WAYNOTI actually uses.

## Contradictions & open questions

- Is `LNS_CPM_002`/`003` reuse of one feature code for several vendors deliberate (one feature,
  vendor variants) or a data-entry shortcut? Source is ambiguous.

## Sources

- [[luminos-notification-pcmm]]
