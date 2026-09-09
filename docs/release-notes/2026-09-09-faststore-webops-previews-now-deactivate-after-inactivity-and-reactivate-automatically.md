---
title: "FastStore WebOps: Previews now deactivate after inactivity and reactivate automatically"
slug: "2026-09-09-faststore-webops-previews-now-deactivate-after-inactivity-and-reactivate-automatically"
type: "improved"
createdAt: "2026-09-09T00:00:00.000Z"
updatedAt: "2026-09-09T00:00:00.000Z"
excerpt: "FastStore preview URLs no longer require a redeploy to stay usable. Idle previews are automatically deactivated and reactivate on the next access."
tags:
    - FastStore
    - WebOps
---

FastStore preview deploys now use an inactivity-based lifecycle instead of a fixed expiration window. Preview URLs stay usable for longer, and no longer require a redeploy just to bring them back.

## What has changed?

Previously, preview URLs were discarded a few days after creation, regardless of usage, and had to be redeployed to work again.

Now, a preview URL is automatically deactivated only after **12 hours of inactivity**. Accessing the URL again automatically reactivates it:

* The first request to a deactivated preview shows a loading screen while the preview wakes up. The page refreshes on its own, and the storefront loads normally after a few seconds.
* If a preview can no longer be reactivated, an expired page is shown instead, and the branch needs to be redeployed to generate a new preview.

For more information, see [Preview availability](https://developers.vtex.com/docs/guides/faststore/webops-dashboard#preview-availability) in the FastStore WebOps - Dashboard guide.

## Why did we make this change?

This change lets you keep using a preview URL for as long as you need it, simply by accessing it, instead of losing it after a fixed number of days and having to trigger a new deploy.

## What needs to be done?

This behavior is automatic and requires no configuration. However, if you run automated tests against preview URLs, add a retry to your test setup: a request made right after a period of inactivity may not immediately return the storefront (status `200`), since the preview could still be waking up.
