---
title: "Set single custom field value"
slug: "setsinglecustomfieldvalue"
excerpt: "Your account may create `apps`, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.\n\r\n\rTo do that, you need to inform in the URL the ID of the app you created with the configuration API (`appId`).\n\r\n\rIn the body of the request, you will inform the new value (`appFieldValue`, passed through the body) of the specific field created in this app (identified by the `appFieldName` parameter, passed through the URL)."
hidden: false
createdAt: "2020-02-05T23:27:53.590Z"
updatedAt: "2020-02-28T14:07:22.415Z"
---
**Example of request body:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n\t\"value\": \"Hello World\"\n}",
      "language": "json"
    }
  ]
}
[/block]