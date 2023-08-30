---
title: "Limitations of the PII data architecture during closed beta"
slug: "limitations-of-the-pii-data-architecture-during-closed-beta"
hidden: true
createdAt: "2022-02-22T22:29:28.541Z"
updatedAt: "2023-05-16T09:38:36.446Z"
---
>❗ This feature is in closed beta phase, meaning we are evolving it to support all scenarios. Do not share this documentation with people outside of your company.

Some commerce features of the VTEX platform are not available for accounts using the current [PII data architecture](https://developers.vtex.com/docs/guides/pii-data-architecture) closed beta version, as we are working to evolve it and ensure data privacy best practices across the platform.

In this guide, you can learn about the current limitations you must be aware of when managing your customers' information with the [Profile System](https://developers.vtex.com/docs/guides/profile-system).

### Master Data

Note that **Master Data** features may be impacted in the following three aspects.

#### Triggers

At the moment, triggers are not supported by the PII platform version Profile System.

#### Orders Index 

This is a legacy integration that was deprecated. VTEX will disable it.

#### CL

Currently, Master Data custom CL fields are not supported.

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

## Learn more

- [PII Data Architecture specifications](https://developers.vtex.com/docs/guides/pii-data-architecture-specifications)
- [Data residency](https://developers.vtex.com/docs/guides/data-residency)
- [Data subject rights](https://help.vtex.com/tutorial/data-subject-rights--6imchxTx09icupKMbzHVIM)
- [Profile System integration guide](https://developers.vtex.com/docs/guides/profile-system)
- [Changes in VTEX features behavior to handle PII data](https://developers.vtex.com/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data)