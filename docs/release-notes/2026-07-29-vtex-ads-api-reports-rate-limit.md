---
title: "VTEX Ads API: Rate limit on Reports endpoints"
slug: "2026-07-29-vtex-ads-api-reports-rate-limit"
hidden: false
type: "info"
createdAt: "2026-08-04T12:00:00.000Z"
excerpt: "Reports endpoints in the VTEX Ads API are now limited to 100 requests per minute per account. Exceeding the limit returns HTTP 429. Large-scale export integrations should throttle requests."
---

The [Reports endpoints](https://developers.vtex.com/docs/guides/exporting-ads-reports) in the **[VTEX Ads API](https://developers.vtex.com/docs/api-reference/vtex-ads-api)** now enforce a rate limit of 100 requests per minute per account. The limit applies only to API Key-authenticated calls.

## What has changed?

- Reports endpoints are limited to 100 requests per minute per account.
- Requests that exceed the limit receive `429 Too Many Requests` with the error message `Rate limit exceeded for this account`.
- Only API Key-authenticated calls to Reports endpoints are affected.

## What needs to be done?

If your integration runs large-scale data exports, such as historical loads or full daily syncs, spread requests over time and wait for the next window before retrying after a `429` response.

Contact [our support](https://help.vtex.com/en/tutorial/how-does-vtex-support-work--2eAT5EyOvaLoHdIWDVaxC3) if your integration needs a higher volume.

## Learn more

- [Exporting ads reports](https://developers.vtex.com/docs/guides/exporting-ads-reports) guide.
- [VTEX Ads API](https://developers.vtex.com/docs/api-reference/vtex-ads-api) reference.
