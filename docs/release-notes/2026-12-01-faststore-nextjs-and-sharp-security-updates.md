---
title: "FastStore: Next.js and sharp security updates"
slug: "2026-12-01-faststore-nextjs-and-sharp-security-updates"
type: fixed
excerpt: "Update your FastStore v2, v3, or v4 project to the latest patch release, which includes Next.js and sharp security updates."
createdAt: "2026-12-01T00:00:00.000Z"
updatedAt: "2026-12-01T00:00:00.000Z"
---

To keep your store secure and avoid vulnerability flags in scanners and audits, update your FastStore project to the latest patch release of your version (v2, v3, or v4). These releases include updated Next.js and `sharp` dependencies with the latest security fixes.

## What has changed?

FastStore v2, v3, and v4 now update the Next.js and `sharp` dependencies to versions with the latest security fixes. The changes vary depending on your FastStore version:

- **FastStore v4:** `@faststore/core` 4.x now depends on `next@^16.4.3`, which includes `sharp` 0.35.5.
- **FastStore v2 and v3:** patches of `@faststore/core` 2.x and 3.x update `sharp` to `^0.35.5` and require Node `>= 20.9.0`.

## Why did we make this change?

Updating these dependencies keeps your store aligned with the latest security recommendations and prevents scanners and audits from flagging it.

## What needs to be done?

Follow the guide [Next.js and sharp security updates for FastStore stores](https://developers.vtex.com/docs/guides/faststore/security-nextjs-and-sharp-vulnerabilities) to learn more and update your store.
