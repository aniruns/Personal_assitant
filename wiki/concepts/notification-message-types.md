---
title: Notification Message Types
type: concept
tags: [zeta, notifications, consent]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[communication-preferences]]", "[[luminos]]", "[[clm]]"]
confidence: high
status: seed
---

# Notification Message Types

The eight categories the Notifications Centre ([[luminos]]) sorts every message into. They
are the axis along which customers give or withhold consent in [[communication-preferences]]
([[communication-preferences-in-clm-aries]]).

## Explanation

| Type | Tag value | What it covers (per the source) |
|---|---|---|
| Critical | `CRITICAL` | Urgent/sensitive, must be prioritised: fraud alerts, outages, regulatory notices, security breaches, transaction failures, legal matters, credit-risk and delinquency messages |
| Directed | `DIRECTED` | Targeted at one individual for timely action: customer alerts, action requests, individual compliance items such as a KYC action |
| OTP | `OTP` | One-time passwords. **Always allowed**, even when an address has `isCommunicationAllowed: false` |
| Authentication | `AUTHENTICATION` | When a customer needs to be approved or authorised |
| Promotional | `PROMOTIONAL` | Marketing of products, services, offers |
| Announcement | `ANNOUNCEMENT` | Updates about the bank's operations, policies, services, events |
| Transactional | `TRANSACTIONAL` | Triggered by a specific customer action or transaction |
| Default | `DEFAULT` | Standardised, pre-set, generic messages fired on conditions or events |

Assessment: a [[two-way-notification]] fraud check straddles Critical (it is a fraud alert)
and Authentication (the customer approves a transaction); which one Luminos uses is not
stated.

## How it connects

- [[communication-preferences]] — each type gets its own `disallowedChannels` per address.
- [[receiver-preference-order]] — the "event"/template level of preference presumably maps
  onto these types or onto finer-grained templates; not confirmed.

## Contradictions & open questions

- Is the type attached to a template in Luminos, or chosen per send by the calling system?

## Sources

- [[communication-preferences-in-clm-aries]]
