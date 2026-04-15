---
title: "FastStore WebOps: Choose your storefront build Node.js version"
slug: "2026-04-14-faststore-webops-choose-your-storefront-build-nodejs-version"
type: "added"
createdAt: "2026-04-14T12:00:00.000Z"
excerpt: "FastStore WebOps now lets you choose the Node.js version used for storefront builds."
tags:
  - FastStore
  - WebOps
---

[FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard) now includes the **Node.js version** section, so you can control which Node.js runtime is used in your FastStore project builds and ensure compatibility with **FastStore v4**, as this version is based on Next.js v16 and requires a more recent Node.js runtime.

![node-webops](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-17950/images/node-webops.png)

## What has changed?

Previously, WebOps used a predefined Node.js version managed by the platform, and you couldn't explicitly choose which Node.js version your FastStore project should use.

Now, WebOps provides a Node.js version setting at the project level. In this setting:

* New FastStore projects created in WebOps are configured to use Node.js v24 by default.
* Existing projects continue to use their current Node.js version (v22 or v20), and you can update them when you're ready.
* When you update a storefront to FastStore (Next.js 16), you can switch the WebOps project to Node.js v24 directly in the WebOps project settings, avoiding build and runtime incompatibility issues.

For more details about this feature, see the Settings section in the guide [FastStore WebOps - Dashboard](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard).

## Why did we make this change?

By adding a Node.js version selector in WebOps, we give you more control over your build environment and make the [**FastStore v4** migration](https://developers.vtex.com/docs/guides/faststore/getting-started-upgrading-faststore-to-v4) path clearer and safer.

## What needs to be done?

**Check the Node.js version of existing projects**

1. In the VTEX Admin, go to **Storefront > FastStore WebOps** and navigate to the **Settings** tab.
2. In the **Node.js version** section, confirm which version your project is using (`v20` or `v22`).

> ℹ️ Existing projects continue using their current Node.js version until you update it.

**Update the Node.js version when upgrading to FastStore v4**

FastStore v4 requires Node.js v24 in WebOps. If you're upgrading from an earlier FastStore major, follow the instructions in the guide [Upgrading FastStore to v4](https://developers.vtex.com/docs/guides/faststore/getting-started-upgrading-faststore-to-v4), including the WebOps steps after you update your repository and configuration.

**Review new projects**

New FastStore projects created in WebOps already use Node.js `v24` by default. Only change this value if you have a specific reason to keep an older Node.js version.
