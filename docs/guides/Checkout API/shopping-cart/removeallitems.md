---
title: "Remove all items"
slug: "removeallitems"
excerpt: "This request removes all items from a given cart, leaving it empty.\r\n\r\nYou must send an empty JSON in the body of the request.\r\n\r\nThe [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart."
hidden: false
createdAt: "2022-03-23T14:22:14.648Z"
updatedAt: "2022-03-25T19:36:48.860Z"
---
[block:callout]
{
  "type": "warning",
  "body": "__Request Body__ must always be sent with empty value \"{ }\" in this endpoint."
}
[/block]