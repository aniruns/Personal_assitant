---
title: Point of Presence (POP)
aliases: [POP, pointsOfPresence]
type: concept
tags: [zeta, clm]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-communication-preferences-in-clm-aries]]"]
related: ["[[clm]]", "[[communication-preferences]]", "[[receiver-preference-order]]"]
confidence: high
status: seed
---

# Point of Presence (POP)

In [[clm]], a labelled group of an account holder's contact addresses — e.g. a `Billing` POP
with a postal address, a `Communication` POP with an email, a `Home` POP with a phone number.
It is the structure that [[communication-preferences]] are attached to
([[communication-preferences-in-clm-aries]]).

## Explanation

Shape, from the sample in the source:

- POP: `id`, `ifiID`, `accountHolderId`, `label`, `addresses[]`, `isDefault`, `attributes`
  (e.g. `nearestLandmark`), audit fields (`createdAt/By`, `updatedAt/By`).
- Address: `id`, `type` (`Postal` | `Email` | `Phone`), `value` (a string for email/phone; an
  object with `line1..3`, `city`, `state`, `country`, `postCode` for postal),
  `isCommunicationAllowed`, `tags[]`, `attributes`, `headers`.
- Preferences are set **per address**, so two addresses in the same POP can differ. The update
  API addresses a target by `addressType` + `popLabels[]`, not by id.

Assessment: a POP address is the CLM-side counterpart of a Luminos "communication vector"
([[receiver-preference-order]]); no source says how the two are linked (by value? by id?).

## How it connects

- [[communication-preferences]] — the tags live on POP addresses.
- [[clm]] — owns the model.

## Contradictions & open questions

- The sample's `Billing` POP has `country: "US"` with an Indian address and post code —
  clearly test data; don't read anything into it.

## Sources

- [[communication-preferences-in-clm-aries]]
