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

To integrate with an external gift card provider, however, you must develop a middleware according to our [Gift Card Provider Protocol](https://developers.vtex.com/vtex-rest-api/reference/giftcard-provider-protocol-overview). This tutorial will present the main concepts and guide you through the steps required to complete this integration.
[block:callout]
{
  "type": "info",
  "title": "Stores may activate multiple gift card providers",
  "body": "For example, you may use our native gift card provider and two external providers."
}
[/block]
## Structure of this guide
[block:parameters]
{
  "data": {
    "h-0": "Article",
    "h-1": "Description",
    "0-0": "Gift Card system architecture",
    "0-1": "An overview of our system, so you understand its building blocks and how they interact with each other.",
    "1-0": "How do gift cards work?",
    "1-1": "An explanation of our abstract model of a gift card, specifying the most important state variables and behaviors, so you can map these to the proper entities for your use case.",
    "2-0": "Integrating a new gift card provider",
    "3-0": "Managing gift cards",
    "2-1": "Walkthrough of the API endpoints that your middleware must implement to adhere to our Gift Card Provider Protocol, along with activation instructions.",
    "3-1": "A final (optional) step covering how Gift Card Hub can be used to manage gift cards from multiple providers."
  },
  "cols": 2,
  "rows": 4
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "This guide is currently being written and published as content become available.",
  "title": "Work in progress"
}
[/block]