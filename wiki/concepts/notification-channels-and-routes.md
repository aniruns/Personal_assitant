---
title: Notification Channels, Providers and Routes
aliases: [channels, routes, providers]
type: concept
tags: [zeta, notifications, luminos]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]", "[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[luminos]]", "[[luminos-notification-system]]", "[[luminos-notification-center]]", "[[twilio]]", "[[receiver-preference-order]]", "[[communication-preferences]]", "[[cardworks]]"]
confidence: high
status: growing
---

# Notification Channels, Providers and Routes

How [[luminos]] models the delivery side of a message. "Channels are the modes of
communication and Routes define the path of delivery" ([[luminos-notification-pcmm]]); a
**provider** (vendor) is the third party or internal component that a route goes through.
Which channel is used for a given customer is decided upstream by the
[[receiver-preference-order]] and constrained by [[communication-preferences]].

## Explanation

**Channels and providers in use** ([[communication-preferences-in-clm-aries]], with PCMM
priorities from [[luminos-notification-pcmm]]):

| Channel | Providers today | Used for / where | PCMM priority |
|---|---|---|---|
| SMS | Sinch (ACL), GupShup, [[twilio]], TLRX (common prod) | HDFC, Pixel | Twilio P1; ACL, Plivo P3 |
| Email | Karix, SendGrid | — | SendGrid P1; SMTP, Gmail, HTTP P3 |
| Flow | Twilio, Plivo | IVR calls | 2-way via Twilio Flow P1 |
| WhatsApp | (Twilio, planned) | — | P1 |
| Push | Firebase Cloud Messaging (Android), APNs (iOS) | — | P1 |
| Inbox | "Collection" | In-app notification; specifically [[cardworks]] | (onboarding P1) |
| Printed Letters | "IO" drops PDFs into an SFTP owned by Sparrow or CardWorks | US only | (onboarding P1) |
| Spotlight | "Collection" | Pop-up inside the Pluxee app; Pluxee only | (onboarding P1) |

The PCMM's list of channels a new provider can be onboarded for — SMS, PUSH, INBOX, EMAIL,
PRINTED LETTERS, SPOTLIGHT (`LNS_CPM_007`) — matches the Aries table exactly except for Flow
and WhatsApp, which the PCMM tracks as their own features. Two independent sources agreeing
on the channel set is why this page is `confidence: high`.

**Routes.** LNC manages a *route plan* per channel ("provider route configuration",
`LNC_CPM_002`, P1) and *route priority for a given communication* (`LNC_CPM_003`, P2)
([[luminos-notification-pcmm]]). Assessment: a route plan is an ordered list of providers for
a channel (e.g. SMS → Twilio, fall back to GupShup), and route priority lets a specific
communication pick a different order. LNS's `LNS_CTD_001` then "sends through all configured
channels through the routes configured".

**Two-way as a channel.** `LNS_CPM_006` treats "2 Way Communication" as a channel in its own
right, implemented over Twilio Flow. This is the first hint of *how* a
[[two-way-notification]] reaches the customer — see that page's open questions.

**Delivery tracking.** Status tracking via provider callbacks is `LNS_CTD_002`, P2; "Call to
Action registration" is `LNS_CTD_003`, P3.

## How it connects

- [[luminos-notification-system]] holds the per-vendor channel features; [[luminos-notification-center]] holds route plans and priorities.
- [[communication-preferences]] names channels in `disallowedChannels` (`SMS`, `CALL`, …).
- [[cardworks]] is the tenant that uses the Inbox channel and (with Sparrow) the printed-letter SFTP.

## Contradictions & open questions

- `disallowedChannels` uses `CALL`; the channel table has no "Call", only "Flow (IVR calls)".
  Assessment: the same channel under two names.
- "Collection" and "IO" as providers for Inbox/Spotlight/Printed Letters look like internal
  component names, not vendors; unexplained.
- Is a route chosen per message, per receiver, or per product? Not stated.

## Sources

- [[luminos-notification-pcmm]]
- [[communication-preferences-in-clm-aries]]
