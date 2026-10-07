---
title: "B2B Buyer Portal Release Notes — Version 2.0.33"
slug: "2026-10-06-buyer-portal-release-notes-2-0-33"
type: improved
excerpt: "Organization Account identifies the plugin version on Buyer Portal backend requests so accounts can enable the backend client check after upgrading"
createdAt: "2026-10-06T00:00:00.000Z"
updatedAt: "2026-10-06T00:00:00.000Z"
hidden: true
tags:
  - Buyer Portal
---

**B2B Buyer Portal** plugin `v2.0.33` (2026-10-06) covers Organization Account. This version prepares Organization Account to keep loading when an account turns on the Buyer Portal backend's client identification check.

## Upgrade notes

- Before the Buyer Portal backend client identification check is turned on for an account, upgrade the store to this plugin version (or later).

---

## Organization Account

### Added

- Organization Account requests to the Buyer Portal backend now identify the plugin and its version (from the browser and when pages load on the server), so the account can keep loading once the backend's client identification check is on. Requests to other services (saved cards, tokenization, postal code, localization) do not send this identification.
