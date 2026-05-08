---
title: "FastStore WebOps: Password protection for preview and production environments"
slug: "2026-05-11-faststore-webops-password-protection-for-preview-and-production-environments"
hidden: false
type: "added"
createdAt: "2026-05-11T15:00:00.000Z"
excerpt: "WebOps now allows you to restrict access to preview environments and production domains with username and password authentication."
tags:
  - FastStore
  - WebOps
---

> ℹ️ Password protection is in closed beta, which means that only selected customers can access it. If you're interested in implementing it in the future, please contact our [Support](https://support.vtex.com/hc/en-us) team.

[FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/webops-dashboard) now includes password protection, allowing you to restrict access to your preview environments and the production domain using basic authentication. This feature enables merchants to protect internal testing environments, staging builds, and production domains from unauthorized access during development or initial launch phases.

## What has changed?

Previously, preview deployments and production domains were publicly accessible once deployed. Now, you can enable password protection in the **Settings** tab to require username and password authentication before accessing these environments.

## Why did we make this change?

This feature enhances security by allowing you to:

* Protect preview environments during development and testing phases.
* Control access to production domains before official launch.
* Prevent unauthorized or accidental access to staging and QA environments.
* Ensure internal testing environments remain private.

## What needs to be done?

To enable password protection:

1. Go to your [FastStore WebOps dashboard](https://developers.vtex.com/docs/guides/faststore/webops-dashboard) and navigate to the **Settings** tab.
2. Locate the **Password protection** section.
3. Enable password protection for preview environments or your production domain by toggling the corresponding switch.
4. Enter a **Password** that users will need to authenticate with.
5. Save your settings.

When password protection is enabled, users will see a basic authentication dialog when accessing the protected environment's URL. They must enter the configured password to proceed.

For detailed instructions, see the [Password protection](https://developers.vtex.com/docs/guides/faststore/webops-dashboard#password-protection) section in the FastStore WebOps - Dashboard guide.

> ⚠️ Remember to share the password with authorized users through a secure channel.
