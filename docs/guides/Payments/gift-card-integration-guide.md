---
title: "Gift Cards"
slug: "gift-card-integration-guide"
hidden: false
createdAt: "2020-07-01T02:17:41.385Z"
updatedAt: "2026-05-13T00:00:00.00Z"
excerpt: "Manage loyalty programs, create refund vouchers, and accept physical gift cards in online storefronts."
---
On VTEX, gift cards are a payment method processed at checkout. Stores can offer gift cards to customers in two ways:

- **Native gift card provider:** Set up VTEX gift cards as a payment method. Gift cards are created and managed in the VTEX Admin.
- **External gift card provider:** Develop a middleware that implements the [Giftcard Provider Protocol](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol) and connects to the [Giftcard Hub](https://developers.vtex.com/docs/api-reference/giftcard-hub-api).

> ℹ️ Stores can activate multiple gift card providers simultaneously. For example, they may have the native provider and two external providers.

## In this section

| Article | Description |
| --- | --- |
| [Gift Card system architecture](https://developers.vtex.com/docs/guides/gift-card-integration-guide-system-architecture) | Overview of the gift card system architecture and how providers connect to VTEX. |
| [Managing VTEX gift cards](https://developers.vtex.com/docs/guides/managing-vtex-gift-cards) | How to manage native VTEX gift cards through the GiftCard API. |
