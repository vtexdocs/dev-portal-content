---
title: "Change price"
slug: "pricechange"
excerpt: "This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)\r\n\r\nThe [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.\n\r\n\rYou need to inform which cart you are referring to, by sending its `orderFormId`; and what is the item whose price you want to change, by sending its `itemIndex`.\n\r\n\rYou also need to pass the new price value in the body.\n\r\n\rRemember that, to use this endpoint, the feature of *manual price* must be active. To check if it's active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the `allowManualPrice` field `true`.\n\r\n\r> Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the `items` array due to customizations or attachments, for example."
hidden: false
createdAt: "2022-03-23T14:22:14.650Z"
updatedAt: "2022-03-23T14:22:14.650Z"
---
