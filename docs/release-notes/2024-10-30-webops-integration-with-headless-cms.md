---
title: "FastStore WebOps: Fixed the app integration with the Headless CMS"
slug: "2024-10-30-webops-integration-with-headless-cms"
type: "fixed"
excerpt: "FastStore WebOps now fully syncs with the Headless CMS, automatically deploying updates to your store."
createdAt: "2024-10-30T16:00:00.667Z"
---

Changes made in the Headless CMS on VTEX Admin, including creating new pages, adding sections, and updating fields, now automatically trigger pull requests to the store's GitHub repository and are reflected in its version history.

## What has changed?

Previously, FastStore WebOps could not sync changes from the Headless CMS. These updates weren’t reflected on the storefront and were inaccessible to store customers.

> ℹ️ For more information about this issue, refer to the [WebOps app not being fully integrated with Headless CMS](https://help.vtex.com/known-issues/webops-app-is-not-fully-integrated-with-headless-cms--577fIocKB9BYYCOkN9dZfW) known issue article.

FastStore WebOps now fully integrates with Headless CMS, automatically syncing changes and reflecting them on your storefront.

## What needs to be done?

Make sure your account is configured with the Headless CMS. For instructions, refer to the [Configuring your VTEX account with the Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-1-configuring-the-vtex-account#instructions) guide.

After configuring the Headless CMS for your store account, no further action is needed. This update is automatically applied to all VTEX stores using FastStore WebOps, so you can continue using both the app and the Headless CMS without synchronization issues.
