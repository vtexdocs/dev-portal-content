---
title: "Ignore profile data"
slug: "ignoreprofiledata"
excerpt: "When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.\r\n\r\nThe [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.\r\n\r\nNote that this request will only work if you have not sent the `clientProfileData` to the cart yet. Sending it to a cart that already has a `clientProfileData` should return a status `403 Forbidden` error, with an `Access denied` message."
hidden: false
createdAt: "2022-03-23T14:22:14.651Z"
updatedAt: "2022-03-23T14:22:14.651Z"
---
