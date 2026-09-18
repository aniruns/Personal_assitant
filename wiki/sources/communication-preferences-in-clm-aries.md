---
title: "Communication Preferences in CLM (Aries)"
type: source
tags: [zeta, notifications, clm, consent]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[communication-preferences]]", "[[clm]]", "[[point-of-presence]]", "[[notification-message-types]]", "[[notification-channels-and-routes]]", "[[luminos]]", "[[cardworks]]"]
confidence: high
status: seed
author: unknown (Zeta ARIES Confluence space; page author not captured by the clipper)
published: unknown (sample data is dated 2024-05 to 2025-01, so 2025 or later)
url: https://zeta-tm.atlassian.net/wiki/spaces/ARIES/pages/3558114469/Communication+Preferences+in+CLM
source_type: article
---

# Communication Preferences in CLM (Aries)

An internal Zeta Confluence page (ARIES space) explaining how [[clm]] captures a customer's
consent for different kinds of messages and how that consent reaches the Notifications Centre
([[luminos]]). It lists the eight [[notification-message-types]] the Notifications Centre
supports, tabulates the delivery channels and providers in use
([[notification-channels-and-routes]]), shows the account-holder data model in which
preferences live — tags on each address of a [[point-of-presence]] — and gives the update
API. Clipped with Obsidian Web Clipper on 2026-09-18. The clipping's sample
`X-Zeta-AuthToken` was redacted before commit; the sample customer data is faker-style.

## Key claims

- The Notifications Centre supports **eight message types**: Critical, Directed, OTP,
  Authentication, Promotional, Announcement, Transactional, Default (definitions on
  [[notification-message-types]]).
- **Channels and providers in use today:** SMS — Sinch (ACL), GupShup, [[twilio]], TLRX
  (common prod), used in HDFC and Pixel; Email — Karix, SendGrid; Flow — Twilio, Plivo, used
  for IVR calls; Inbox — "Collection" provider, in-app notification, specifically for
  [[cardworks]]; Printed Letters — "IO" places PDFs in an SFTP owned by Sparrow or CardWorks,
  US only; Push — Firebase Cloud Messaging (Android), APNs (iOS); Spotlight — "Collection",
  pop-up inside the Pluxee app, Pluxee only.
- Consent is modelled **per address, per message type**: each account holder has
  `pointsOfPresence` (labelled Billing / Communication / Home …), each with `addresses` of
  type Postal / Email / Phone. An address carries `isCommunicationAllowed` plus tags of
  `type: COMMUNICATION_PREFERENCE`, `value: <message type>`,
  `attributes.disallowedChannels: "SMS,CALL"` (or `""` = allowed on all channels).
- `isCommunicationAllowed: false` on an address blocks **every message type except OTP** on
  that address. When `true`, per-type preferences apply.
- CLM **publishes an event** on preference change; the Notifications Centre updates its copy,
  and CLM's version **overrides** whatever the Notifications Centre held for that account
  holder.
- Update API: `POST …/mars/tachyon/v4/ifi/{ifiID}/accountholders/{accountHolderId}/communicationPreferences/update`
  on the Aries host (`aries.internal.mum1-pp.zetaapps.in`), body = array of
  `{addressType, popLabels[], preferenceTags[]}`. Used to change preferences after onboarding.
- Sample data uses `ifiID: 600309` — the same number the Orcus contract used as a tenant id
  for [[cardworks]].

## Notable quotes

> CLM gives the flexibility to the issuer to define and set their communication preferences at
> a particular email or phone level.

> if `isCommunicationAllowed` is false then **except OTP** no other messages will be allowed on
> that address

## Assessment

Clear and concrete on the data model and the consent semantics; the JSON sample is worth more
than the prose. Gaps: it never says which message type a given template maps to, how the
Notifications Centre resolves a conflict between the CLM consent and its own
[[receiver-preference-order]] (assessment: consent should act as a filter *before* preference
ordering, but the page doesn't say), what `CALL` in `disallowedChannels` corresponds to (Flow /
IVR, presumably), or what the CLM event looks like. The "Used For" column of the channel table
is mostly empty. Two channel tables appear because the clipper duplicated the header row.

Terminology: this page says "Notifications Centre"; the [[luminos-notification-pcmm]] says
"Luminos Notification Center (LNC)" and the Orcus diagram says "Notification Centre". Treated
as the same system — see [[luminos]].

## Wiki changes

- Created: [[communication-preferences]], [[clm]], [[point-of-presence]],
  [[notification-message-types]]
- Updated: [[notification-channels-and-routes]] (providers-in-use table),
  [[luminos]] (Notifications Centre identity; consent sync), [[cardworks]] (Inbox channel,
  printed letters, `ifiID` 600309), [[tachyon]] (API namespace), [[twilio]], [[overview]],
  [[index]]

## Raw

[[2026-09-18-communication-preferences-in-clm-aries]]
