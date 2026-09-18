---
title: Luminos
aliases: [Luminous, Notifications Centre, Notification Centre, LN]
type: entity
tags: [zeta, notifications, luminos]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-two-way-notification-frm-cardworks]]", "[[2026-09-18-luminos-notification-pcmm]]", "[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[luminos-notification-system]]", "[[luminos-notification-center]]", "[[notification-product]]", "[[receiver-preference-order]]", "[[communication-preferences]]", "[[notification-channels-and-routes]]", "[[two-way-notification]]", "[[orcus]]", "[[clm]]"]
confidence: medium
status: growing
---

# Luminos

Zeta's notification platform (also written "Luminous", and referred to as the
**Notifications Centre** / "Notification Centre" in older documents; the user's shorthand is
"LN"). It owns the modelling of *who* gets told *what* over *which channel* — products,
receivers, preferences, channels, routes, templates — and the actual triggering and delivery
of messages. In this KB it appears both as the customer-facing half of
[[two-way-notification]] and as the consumer of the consent that [[clm]] captures.

## What we know

**Structure.** The [[luminos-notification-pcmm]] splits Luminos into two Beta modules with the
same four capability areas:

| Capability | [[luminos-notification-system|LNS]] (system) | [[luminos-notification-center|LNC]] (center) |
|---|---|---|
| Notification Product Management (`NPM`) | product lifecycle | product lifecycle, Tachyon bundle mapping, languages |
| Receiver Management (`RCM`) | receiver lifecycle, preference order per product/event/receiver | preference at product & template level, per-template override |
| Channel & Provider Management (`CPM`) | channel lifecycle, per-vendor channel features, new-provider onboarding | channel lifecycle, route plans, route priority |
| Communication Trigger & Delivery (`CTD`) | send via configured routes, delivery callbacks, call-to-action | per-template channel config, test sends, template lifecycle |

Assessment: LNS reads as the runtime engine and LNC as the configuration console — inferred
from which features sit where; the source doesn't say.

**Domain model.** A [[notification-product]] groups receivers, their communication vectors
(points of contact), a [[receiver-preference-order]] over those vectors at product / event
(template) / individual-receiver level, and message definitions (templates). Delivery goes
over channels and routes ([[notification-channels-and-routes]]); vendors in use include
[[twilio]], SendGrid, Plivo, Sinch/ACL, GupShup, Karix, FCM and APNs
([[communication-preferences-in-clm-aries]]).

**Consent.** Luminos does not own customer consent. [[clm]] stores
[[communication-preferences]] per address of a [[point-of-presence]] and publishes an event on
change; Luminos updates its copy and CLM's version wins
([[communication-preferences-in-clm-aries]]). Luminos classifies every message into one of
eight [[notification-message-types]], which is the axis consent is expressed on.

**Workflow API (as seen from Orcus).** `POST /1.0/tenants/{tenantID}/workflows/{workflowType}/initiate`
with an `eventData` body returns a `workflowID`; the CardWorks-on-FRM workflow type is
`CWFRMWorkflow`. Expected `eventData` fields: `accountHolderId`, `transactionId`, `cguid`,
`maskedPAN`, `merchantName`, `transactionAmount{value,currency,baseValue,baseCurrency}`,
`timestamp`, `tenantId`, `action` (e.g. `TWO_WAY_NOTIFICATION`), `triggeredRule`,
`valueTime`, `rrn`, `resourceID`. The customer's answer is published to the [[atropos]] topic
`notificationWorkflowResponse`. Used for both `2WAYNOTI` and `AutomatedSoftBlock`
([[two-way-notification-frm-cardworks-contract]]).

- A separate Confluence page, "Notification Workflow Contracts with Orcus/FRM"
  (`https://zeta-tm.atlassian.net/wiki/x/E4ITzQ`), holds the sandbox details and fuller
  workflow contract — not yet ingested.

## Relationships

- Initiated by [[orcus]] for fraud-control notifications; responds via [[atropos]].
- Receives consent from [[clm]]; maps notification products to [[tachyon]] products.
- Tenants seen using it: [[cardworks]] (Inbox channel, printed letters), HDFC and Pixel
  (SMS), Pluxee (Spotlight) ([[communication-preferences-in-clm-aries]]).

## Contradictions & open questions

- **Name.** "Luminous" ([[two-way-notification-frm-cardworks-contract]]) vs "Luminos"
  ([[luminos-notification-pcmm]], and the user's usage). Assessment: same system; Luminos is
  the product's name, Luminous a common misspelling. The Orcus diagram's "Notification Centre"
  and the Aries page's "Notifications Centre" are also taken to be Luminos (or its LNC
  module) — medium confidence, no source states the equivalence outright.
- Is LNS/LNC a *deployment* split (two services) or a *product-management* split (two feature
  lists over one system)? Not stated.
- Shape of the response event on `notificationWorkflowResponse` is not in any source.
- How does Luminos combine CLM consent with its own preference order? See
  [[communication-preferences]].

## Sources

- [[two-way-notification-frm-cardworks-contract]]
- [[luminos-notification-pcmm]]
- [[communication-preferences-in-clm-aries]]
