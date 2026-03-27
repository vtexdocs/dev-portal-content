---
title: "FastStore WebOps: Password protection for preview and production environments"
slug: "2026-03-27-faststore-webops-password-protection-for-environments"
hidden: false
type: "added"
createdAt: "2026-03-27T15:00:00.000Z"
excerpt: "WebOps now allows you to restrict access to preview environments and production domains with username and password authentication."
tags:
  - FastStore
  - WebOps
---

FastStore WebOps now includes password protection capabilities, allowing you to restrict access to your preview environments and production domain using basic authentication. This feature enables merchants to protect internal testing environments, staging builds, and production domains from unauthorized access during development or initial launch phases.

## What has changed?

Previously, preview deployments and production domains were publicly accessible once deployed. Now, you can enable password protection in the **Settings** tab to require username and password authentication before accessing these environments.

## Why did we make this change?

This feature enhances security by allowing you to:
* Protect preview environments during development and testing phases
* Control access to production domains before official launch
* Prevent unauthorized or accidental access to staging and QA environments
* Ensure internal testing environments remain private

## What needs to be done?

To enable password protection:

1. Go to your [FastStore WebOps dashboard](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard) and navigate to the **Settings** tab.
2. Locate the **Password protection** section.
3. Enable password protection for preview deployments or your production domain by toggling the corresponding switch.
4. Enter a **Username** that users will need to authenticate with.
5. Enter a **Password** that users will need to authenticate with.
6. Save your settings.

When password protection is enabled, users will see a basic authentication dialog when accessing the protected environment's URL. They must enter the configured username and password to proceed.

For detailed instructions, see the [Password protection](https://developers.vtex.com/docs/guides/faststore/webops-dashboard#password-protection) section in the WebOps Dashboard guide.

> ⚠️ Remember to share the username and password with authorized users through a secure channel.
