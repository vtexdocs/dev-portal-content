---
title: "Pricing Hub is no longer supported"
slug: "2026-09-22-pricing-hub-end-of-support"
hidden: false
type: "deprecated"
createdAt: "2026-09-22T00:00:00.000Z"
updatedAt: "2026-09-22T00:00:00.000Z"
excerpt: "VTEX no longer supports Pricing Hub. A replacement is in development. Until it is available, use the Audience API to send prices outside VTEX."
tags:
    - Pricing
---

VTEX no longer supports [Pricing Hub](https://developers.vtex.com/docs/guides/pricing-hub-overview). We are working on a replacement solution, which will be announced in future documentation.

## What has changed?

Pricing Hub was an intermediary between VTEX and external pricing systems, used mainly in B2B scenarios to fetch personalized prices from an external source at checkout.

This feature is no longer supported. Do not start new implementations that rely on Pricing Hub, including the [Pricing Hub API](https://developers.vtex.com/docs/api-reference/pricing-hub) and the related middleware templates.

## What needs to be done?

Until the replacement is available, if you need to send prices outside VTEX, use the [Audience API](https://developers.vtex.com/docs/api-reference/audience-api).

The Audience API, together with Price Table Mapper, lets you associate price tables with customer audiences and apply contextual prices. See [Contextual price per shopper](https://developers.vtex.com/docs/guides/contextual-price-per-shopper) for the recommended flow.

If your store currently uses Pricing Hub, contact [VTEX Support](https://help.vtex.com/support) to discuss migration options.
