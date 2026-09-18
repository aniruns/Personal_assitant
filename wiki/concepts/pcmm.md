---
title: PCMM (Product Capability Maturity Matrix)
type: concept
tags: [zeta, product-management]
created: 2026-09-18
updated: 2026-09-18
sources: ["[[2026-09-18-luminos-notification-pcmm]]"]
related: ["[[luminos-notification-pcmm]]", "[[luminos]]"]
confidence: low
status: seed
---

# PCMM (Product Capability Maturity Matrix)

The tabular format Zeta product teams use to describe a product as
**Module → Capability → Feature**, each with a maturity level and a priority. The user calls
it a "PCMM"; the expansion is my guess (assessment: *Product Capability Maturity
Model/Matrix*) — the source does not spell it out. The first instance in this KB is the
[[luminos-notification-pcmm]].

## Explanation

Columns, as seen in the Luminos instance:

| Column | Values seen |
|---|---|
| `Module_Name`, `Module_Code` | e.g. Luminos Notification System / `LNS` |
| `Module_maturity_level` | `Beta` |
| `Capability_name`, `Capability_code` | e.g. Receiver Management / `LNS_RCM` |
| `Capability_maturity_level` | `Beta` |
| `Capability_description` | one sentence, repeated on every feature row |
| `Priority` | `P1` – `P3` |
| `Feature_code` | `<module>_<capability>_<nnn>`; reused across vendor variants of one feature |
| `Feature_Guidance` | empty |
| `Feature_Description` | one line |

Conventions worth knowing when reading one: capability codes are shared across modules
(`NPM`, `RCM`, `CPM`, `CTD` appear in both LNS and LNC), so the module prefix is what
distinguishes them; and the same feature code can appear several times when a feature has
per-vendor variants with different priorities.

## How it connects

- [[luminos-notification-pcmm]] — the only instance so far; more modules' PCMMs would make
  this page useful as a comparison key.

## Contradictions & open questions

- What the maturity levels are (Alpha / Beta / GA?) and what P1–P3 mean in planning terms —
  unknown.

## Sources

- [[luminos-notification-pcmm]]
