---
title: Receiver Preference Order (product / event / receiver level)
aliases: [Receiver Preference Management, product and event level preferences]
type: concept
tags: [zeta, notifications, luminos]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]"]
related: ["[[communication-preferences]]", "[[notification-product]]", "[[luminos]]", "[[luminos-notification-system]]", "[[luminos-notification-center]]", "[[notification-channels-and-routes]]"]
confidence: medium
status: seed
---

# Receiver Preference Order (product / event / receiver level)

In [[luminos]], the ordered list of a receiver's **communication vectors** (points of contact
— e.g. a phone number, an email, a device for push) that says which one to try first when a
message goes out. The order can be set at three levels — for a whole
[[notification-product]], for an **event** (a message definition / template), and for an
**individual receiver** — with the narrower level overriding the wider one. This is the
"product and event level preference" feature (`LNS_RCM_002`, `LNC_RCM_001/002`)
([[luminos-notification-pcmm]]).

## Explanation

**The three levels.** The PCMM phrases the feature as "the Communication vector preference
order for a product, event and an individual receiver" (LNS, P1) and, on the LNC side, as
preference management "at product and message definition (Template) level" (P1) plus "override
receiver preference order for a given Message definition (Template)" (P2)
([[luminos-notification-pcmm]]). Read together:

| Level | Set where | Meaning (assessment) |
|---|---|---|
| Product | product creation (`*_NPM_001`: "receiver preferences at the product level") | default vector order for every message in the product |
| Event / template | `LNC_RCM_001`, override `LNC_RCM_002` | a specific message type (e.g. an OTP, a fraud check) prefers a different vector |
| Individual receiver | `LNS_RCM_002` | one customer's own ordering, e.g. "email before SMS" |

The precedence (receiver > event > product) is my inference from the word "override"; the
source does not state a resolution rule.

**What a vector is.** Receiver Management defines "Communication vectors (point of contacts)
definitions for a receiver within a product" (`LNS_RCM_001`). So a vector is a concrete
contact endpoint, scoped to a product — the Luminos-side counterpart of a [[clm]] address on a
[[point-of-presence]]. Whether vectors are typed by channel (one vector = one channel) or one
address can serve several channels (a phone number for SMS *and* WhatsApp *and* IVR) is not
stated.

**Relation to consent.** The preference order says what Luminos *wants* to try; the customer's
[[communication-preferences]] in CLM say what they *allow* (per message type, per address,
with disallowed channels). Assessment: consent must filter the ordered list before the first
allowed vector is used; no source describes the combination.

**Relation to routes.** Once a vector and hence a channel is chosen, route plans and route
priority ([[notification-channels-and-routes]]) pick the provider path. Preference order is
about the *receiver's endpoint*; routing is about the *vendor*.

## How it connects

- [[notification-product]] — the container in which vectors and the product-level default
  are defined.
- [[communication-preferences]] — the consent layer that constrains the order.
- [[luminos-notification-system]] / [[luminos-notification-center]] — where the feature codes
  live (`LNS_RCM_002`, `LNC_RCM_001`, `LNC_RCM_002`).
- [[two-way-notification]] — a concrete event whose preferred vector presumably differs from
  the product default (a question needs an interactive channel).

## Contradictions & open questions

- **"Event" vs "message definition (Template)":** LNS names the middle level "event", LNC
  names it "message definition (Template)". Assessment: the same level; an event triggers a
  template. Medium confidence.
- Resolution rule when levels conflict, and what happens when every vector is disallowed by
  consent — not in any source.
- The design doc behind this feature ("LN Including product and event level preferences",
  SharePoint) has not been ingested; its clipping was empty.

## Sources

- [[luminos-notification-pcmm]]
