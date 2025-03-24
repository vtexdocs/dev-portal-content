---
title: "Discontinuation of the Pricing V1 module compatibility routes"
slug: "2025-03-24-discontinuation-of-the-pricing-v1-module-compatiblity-routes"
hidden: false
type: "deprecated"
createdAt: "2025-03-24T00:00:00.219Z"
updatedAt: ""
excerpt: "After July 1, 2025, any store using the compatibility routes of the Pricing V1 module will get the following error message: This resource is not available for this account, with status HTTP 410 Gone"
---

After July 1, 2025, any store using the compatibility routes of the Pricing V1 module will get the following error message:

>❗ This resource is not available for this account, with status HTTP 410 Gone

## What has changed?

We've disabled the compatibility routes of the Pricing V1 module to simplify maintenance and focus on evolving the platform. This change requires all clients to adopt the routes of the Pricing V2 module, which ensures access to updates and new features.

This action is part of the deprecation process of the previous version of the module, announced in [Pricing V1 module will be discontinued](https://help.vtex.com/en/announcements/deprecacao-pricing-v1--46YxKNOCLH2Ykw6a9uyxXB).

## What needs to be done?

Check which of the following Pricing V1 scenarios applies to your store:

**Store using Pricing V1 to set pricing per UTM:** Contact your **Account Manager**, **Customer Success Manager**, or [VTEX Support](https://help.vtex.com/en/support) to migrate the [Pricing](https://help.vtex.com/en/tracks/precos-101--6f8pwCns3PJHqMvQSugNfP) module.

**Store using Pricing V1 for price management only (not using UTM):** No action is required. VTEX will automatically migrate all stores to Pricing V2. In this case, all the information contained in Pricing V1 will be updated in the Pricing module securely and gradually without any data loss.
