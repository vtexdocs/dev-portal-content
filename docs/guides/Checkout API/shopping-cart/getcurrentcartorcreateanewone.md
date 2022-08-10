---
title: "Get current cart or create a new one"
slug: "getcurrentcartorcreateanewone"
excerpt: "This request allows you to obtain information of an existing shopping cart or to create a new empty one. VTEX checkout provides browsers with a cookie containing an `orderFormId`. Sending this request with such a cookie retrieves information of the cart corresponding to that ID. Without the cookie, this request creates and retrieves a new shopping cart.\r\n\r\nThe [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` obtained in response is the identification code of the newly created cart.\n\r\n\r> This request has a time out of 45 seconds."
hidden: false
createdAt: "2022-03-23T14:22:14.646Z"
updatedAt: "2022-03-23T14:22:14.646Z"
---
