---
title: Twilio
type: entity
tags: [vendor, notifications]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]", "[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[notification-channels-and-routes]]", "[[luminos-notification-system]]", "[[two-way-notification]]"]
confidence: high
status: seed
---

# Twilio

Communications-API vendor (SMS, voice, WhatsApp, "Studio Flow" call flows). For Zeta's
[[luminos]] it is the **P1 provider for three channels** — SMS, WhatsApp, and two-way
communication via Flow — which makes it the most load-bearing vendor in the notification
stack ([[luminos-notification-pcmm]]).

## What we know

- P1 features in the PCMM: `LNS_CPM_003` SMS (Twilio), `LNS_CPM_005` WhatsApp (Twilio),
  `LNS_CPM_006` "2 Way Communication as a Channel (Flow integration Twilio)"
  ([[luminos-notification-pcmm]]).
- Already in use today for SMS (alongside Sinch/ACL, GupShup, TLRX) and for **Flow**, i.e.
  IVR calls (alongside Plivo) ([[communication-preferences-in-clm-aries]]).

## Relationships

- Provider on several channels in [[notification-channels-and-routes]].
- Likely carrier of [[two-way-notification]] if 2WAYNOTI uses the Flow channel — unconfirmed.

## Contradictions & open questions

- (none yet)

## Sources

- [[luminos-notification-pcmm]]
- [[communication-preferences-in-clm-aries]]
