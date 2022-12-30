---
title: "Remove all personal data"
slug: "removeallpersonaldata"
excerpt: "This call removes all user information, making a cart anonymous, while leaving the items.\r\n\r\nThe [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.\r\n\r\nThis call works by creating a new orderForm, setting a new cookie and returning a redirect 302 to the cart URL (`/checkout/#/orderform`)."
hidden: false
createdAt: "2022-03-23T14:22:14.648Z"
updatedAt: "2022-03-23T14:22:14.648Z"
---
