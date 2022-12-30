---
title: "Set single custom field value"
slug: "setsinglecustomfieldvalue"
excerpt: "Your account may create `apps`, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.\n\r\n\rTo do that, you need to inform in the URL the ID of the app you created with the configuration API (`appId`).\n\r\n\rIn the body of the request, you will inform the new value (`appFieldValue`, passed through the body) of the specific field created in this app (identified by the `appFieldName` parameter, passed through the URL).\r\n\r\nThe [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart."
hidden: false
createdAt: "2022-03-23T14:22:14.658Z"
updatedAt: "2022-03-23T14:22:14.658Z"
---
