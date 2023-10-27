---
title: "Gift Card"
slug: "gift-card-integration-guide"
hidden: false
createdAt: "2020-07-01T02:17:41.385Z"
updatedAt: "2022-02-10T13:15:10.405Z"
---
In VTEX, gift cards are a payment option that allows brands to manage loyalty programs, create refund vouchers and accept physical gift cards in their online storefronts.

There are two ways a VTEX store can offer gift cards to their customers:

- Using our native gift card provider
- Integrating an external gift card provider

To use our native gift card solution, simply set it up as a payment method and your customers will be able to use their gift cards on your store's checkout. These gift cards are created and managed in your store's admin panel.

To integrate with an external gift card provider, however, you must develop a middleware according to our [Gift Card Provider Protocol](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#overview). This tutorial will present the main concepts and guide you through the steps required to complete this integration.

>ℹ️ Stores may activate multiple gift card providers. For example, you may use our native gift card provider and two external providers.


## Structure of this guide

| Article | Description |
| - | - |
| [Gift Card system architecture](https://developers.vtex.com/docs/guides/gift-card-integration-guide-system-architecture) | How to identify the payment methods' ID and set up the interest rate type using the Payments Gateway API. |
| [Managing VTEX gift cards](https://developers.vtex.com/docs/guides/managing-vtex-gift-cards) | How to manage VTEX native gift cards from the VTEX gift card provider through the GiftCard API. |


> ⚠️ This guide is currently being written and published as content become available.