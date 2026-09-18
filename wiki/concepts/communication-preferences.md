---
title: Communication Preferences (customer consent in CLM)
type: concept
tags: [zeta, clm, consent, notifications]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[clm]]", "[[point-of-presence]]", "[[notification-message-types]]", "[[receiver-preference-order]]", "[[luminos]]", "[[notification-channels-and-routes]]"]
confidence: high
status: seed
---

# Communication Preferences (customer consent in CLM)

The per-customer record of which kinds of messages may be sent to which of their addresses
over which channels. [[clm]] stores it as tags on each address of a [[point-of-presence]] and
pushes it to [[luminos]], which must respect it when delivering. It is the *consent* half of
notification preferences; the *delivery* half — which contact to try first — is the
[[receiver-preference-order]] in Luminos ([[communication-preferences-in-clm-aries]]).

## Explanation

**Data model.** An account holder has several points of presence (labelled e.g. `Billing`,
`Communication`, `Home`), each holding `addresses` of type `Postal`, `Email` or `Phone`. On
each address ([[communication-preferences-in-clm-aries]]):

- `isCommunicationAllowed: true|false` — the parent consent for that address.
- `tags[]` with `type: COMMUNICATION_PREFERENCE`, `value: <message type>` — one of the eight
  [[notification-message-types]] (`CRITICAL`, `DIRECTED`, `OTP`, `AUTHENTICATION`,
  `PROMOTIONAL`, `ANNOUNCEMENT`, `TRANSACTIONAL`, `DEFAULT`) — and
  `attributes.disallowedChannels: "SMS,CALL"` (comma-separated) or `""`.
- `attributes.communicationPreferences: "true"` marks addresses that carry preferences.

**Semantics.**

- `isCommunicationAllowed = false` → nothing except **OTP** goes to that address.
- `isCommunicationAllowed = true` → each message type is allowed unless its tag lists the
  channel in `disallowedChannels`. Empty string = allowed on all channels.
- Preferences are per *address*, so an issuer can allow promotions on one email and block
  them on another.

**Sync to Luminos.** CLM publishes an event when preferences change; the Notifications Centre
updates its copy, and CLM's version **overrides** whatever Luminos held for that account
holder. CLM is therefore the source of truth.

**Update API.** `POST /mars/tachyon/v4/ifi/{ifiID}/accountholders/{accountHolderId}/communicationPreferences/update`
with a body of `[{addressType, popLabels[], preferenceTags[]}]` — i.e. preferences are
addressed by (address type, POP label), not by address id. Intended for changes after
onboarding.

## How it connects

- [[point-of-presence]] — the structure the tags hang off.
- [[notification-message-types]] — the vocabulary of `value`.
- [[receiver-preference-order]] — Luminos's ordering, which consent should filter.
- [[notification-channels-and-routes]] — the channel names used in `disallowedChannels`.
- [[two-way-notification]] — as a fraud alert it is presumably `CRITICAL` or `AUTHENTICATION`
  (assessment), which would make it hard for a customer to opt out of.

## Contradictions & open questions

- Which channel name does `CALL` in `disallowedChannels` map to — the "Flow" (IVR) channel?
- How Luminos combines consent with its own preference order, and what it does when every
  vector is disallowed, is undocumented.
- The CLM → Luminos event contract is not in any ingested source.

## Sources

- [[communication-preferences-in-clm-aries]]
