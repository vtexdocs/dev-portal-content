---
title: "How to configure extra fields in inStore cart"
slug: "how-to-configure-extra-fields-in-instore-cart"
hidden: false
createdAt: "2022-09-14T14:46:51.281Z"
updatedAt: "2022-09-14T14:49:35.965Z"
---
The configuration of extra fields in the inStore cart allows product specifications to be used in the order invoice issuance process.

To create the extra fields, follow the steps below:

1. Check current store configuration via [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration). 
2. Save the JSON information returned from the request.
[block:code]
{
  "codes": [
    {
      "code": "{ \n\t\"paymentConfiguration\": {\n    \t\"requiresAuthenticationForPreAuthorizedPaymentOption\": false,\n  }\n  \"minimumQuantityAccumulatedForItems\": 1,\n  \"decimalDigitsPrecision\": 2,\n  \"minimumValueAccumulated\": 0,\n  \"apps\": []\n}",
      "language": "json"
    }
  ]
}
[/block]

3. Make a request using the endpoint [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration) with the same saved JSON data, and add the extra fields (`fields`) with the information inside the `apps` property.
[block:code]
{
  "codes": [
    {
      "code": "{ \n\t\"paymentConfiguration\": {\n    \t\"requiresAuthenticationForPreAuthorizedPaymentOption\": false,\n  }\n  \"minimumQuantityAccumulatedForItems\": 1,\n  \"decimalDigitsPrecision\": 2,\n  \"minimumValueAccumulated\": 0,\n  \"apps\": [\n    {\n      \"fields\": [\n        \"cart-extra-context\",\n        \"cart-type\"\n      ],\n      \"id\": \"cart-extra-context\",\n      \"major\": 1\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]