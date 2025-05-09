---
title: "FastStore WebOps: Self-service domain setup now available"
slug: "2025-04-08-faststore-webops-self-service-domain-setup-now-available"
type: improved
excerpt: "FastStore WebOps now allows users to configure their store’s production domains."
createdAt: "2025-04-03T17:15:14.007Z"
updatedAt: ""
hidden: false
---


Developers and merchants can now configure their store’s production domains by accessing the new **Settings** tab in the [FastStore WebOps Dashboard](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard).

![settings-webops](https://vtexhelp.vtexassets.com/assets/docs/src/settings-webops___e1ce8e4cc9ced1c62e74d7d81e88ca65.png)

## What has changed?

This feature allows developers and merchants to manage their production storefront domains. This self-service approach gives teams more flexibility and autonomy when configuring their storefronts.

Users can:

- **Add** a new production domain
- **Remove** a domain that is no longer needed.

After adding a domain to FastStore WebOps, a new deployment will be triggered automatically, and the deployment’s progress can be tracked in the WebOps Dashboard. If something is wrong with the domain setting, the deployment will receive the status `Failed`. Learn more about deployment statuses in [Production deploys](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#production-deploys).

## Why did we make this change?

The self-service domain configuration has been released to:

- Simplify the domain migration process.
- Centralize the domain management.
- Offer real-time deployment monitoring.

## What needs to be done?

During the go-live process, after completing the DNS configuration, configure the production domain directly in WebOps. Learn more about the complete go-live process in [Configuring external DNS](https://developers.vtex.com/docs/guides/faststore/go-live-1-configuring-external-dns).

To learn more about domain management, see the section [Settings](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#settings) in the FastStore WebOps Dashboard guide.