---
title: "Master Data: Temporary restriction on public fields"
slug: "2026-10-23-master-data-temporary-restriction-on-public-fields"
hidden: false
type: "info"
createdAt: "2026-10-22T19:00:00.000Z"
updatedAt: "2026-10-22T19:00:00.000Z"
excerpt: "Starting October 26, 2026, Master Data v1 and v2 will temporarily restrict public fields. You won't be able to create new public fields or change existing private fields to public."
tags:
  - Master Data
seeAlso:
  - "/docs/guides/api-authentication-using-api-keys"
---

Starting October 26, 2026, [Master Data](https://developers.vtex.com/docs/guides/master-data) will temporarily block the creation of public fields and the conversion of existing private fields to public. This change applies to both native and custom fields in Master Data v1 and v2.

> Master Data public fields can be accessed through unauthenticated API requests, while private fields require authenticated API requests.

## What is changing?

- New fields can only be created as private.
- Existing private fields can no longer be changed to public.
- Attempts to create public fields or change private fields to public will return an error, and the changes won't be applied.

## Why did we make this change?

This restriction strengthens data security in Master Data by preventing new fields from being exposed through unauthenticated requests. It helps reduce the risk of unintended data exposure and encourages authenticated access to store and customer information.

## What needs to be done?

If your store or integration uses public fields, update your implementation to use private fields and retrieve their data through [authenticated API requests](https://developers.vtex.com/docs/guides/api-authentication-using-api-keys).

If you have a legitimate use case that requires public fields, [open a support ticket](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) explaining why unauthenticated access is necessary. The VTEX product team will review each request on a case-by-case basis.