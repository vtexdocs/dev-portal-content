---
title: "Set multiple custom field values"
slug: "setmultiplecustomfieldvalues"
excerpt: "Your account may create `apps`, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.\n\r\n\rTo do that, you need to inform the ID of the app you created with the configuration API (`appId`).\n\r\n\rIn the body of the request, for each field created in this app (`appFieldName`) you will inform a value (`appFieldValue`)."
hidden: false
createdAt: "2020-02-05T23:27:53.590Z"
updatedAt: "2020-05-19T14:56:35.205Z"
---
**Example of request body:**
[block:code]
{
  "codes": [
    {
      "code": "{\n\t\"name\": \"John\",\n\t\"age\": 42\n}",
      "language": "json"
    }
  ]
}
[/block]