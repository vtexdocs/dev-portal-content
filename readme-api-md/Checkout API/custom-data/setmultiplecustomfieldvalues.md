---
title: "Set multiple custom field values"
slug: "setmultiplecustomfieldvalues"
excerpt: "Your account may create `apps`, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.\n\r\n\rTo do that, you need to inform the ID of the app you created with the configuration API (`appId`).\n\r\n\rIn the body of the request, for each field created in this app (`appFieldName`) you will inform a value (`appFieldValue`).\r\n\r\nThe [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart."
hidden: false
createdAt: "2022-03-23T14:22:14.657Z"
updatedAt: "2022-03-23T14:22:14.657Z"
---
