---
title: "Limitations of the PII data architecture during closed beta"
slug: "limitations-of-the-pii-data-architecture-during-closed-beta"
hidden: false
createdAt: "2022-02-22T22:29:28.541Z"
updatedAt: "2023-05-16T09:38:36.446Z"
seeAlso:
 - "/docs/guides/data-protection-plus"
 - "/docs/guides/pii-data-architecture-specifications"
 - "/docs/guides/data-residency"
 - "/docs/guides/profile-system"
 - "/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data"
---

>⚠️ **Closed beta:** [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus) is in closed beta and is only available in select regions.

>❗ This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh), meaning *additional fees may apply.* 
> 
> If you are already a VTEX customer and want to adopt VTEX Shield for your business, please contact [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ).
>
> If you are not yet a customer but are interested in this solution, please complete our [contact form](https://vtex.com/us-en/contact/). 

Some commerce features of the VTEX platform are unavailable for accounts using the PII data architecture during the closed beta phase of [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus). We are actively enhancing this feature to ensure the best data privacy practices across the platform.

In this guide, you can learn about the current limitations you must be aware of when managing your customers' information with the [Profile System](https://developers.vtex.com/docs/guides/profile-system).

### Master Data

Accounts with the PII data architecture must use only the dedicated [Profile System](https://developers.vtex.com/docs/guides/profile-system) for managing customer profiles. [Master Data](https://developers.vtex.com/docs/guides/master-data-components), previously used for profile management, is not compatible with the PII data architecture. You cannot use it alongside or instead of the Profile System. Triggers are not supported in the current version of Profile System.

### Pricing - Price tables

The [Price tables](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S#) feature is not supported at this moment.

### Order Management

VTEX’s Order Management System is impacted on a few different aspects. See details below.

#### Call center

You must disable call center impersonation at the License Manager.

### Gift card

The [gift card](https://help.vtex.com/en/subcategory/gift-card--3qWeS7abxCyC0G0GMq42gA#) feature is not supported for PII platform version accounts yet.

### Customer Credit

Currently, the [Customer Credit](https://help.vtex.com/en/tutorial/customer-credit-overview--1uIqTjWxIIIEW0COMg4uE0) feature is not supported.
