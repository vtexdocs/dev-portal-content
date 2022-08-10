---
title: "Associate attachments to SKU"
slug: "catalog-api-post-associate-attachment-sku"
excerpt: "Amplifies a cart data by associating attachments to SKUs.\n\rThis request removes existing SKU attachment associations and recreates the associations with the attachments being sent."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:47:18.057Z"
---
Amplify your Cart data by associate attachments to SKUs 

This request remove existing sku attachments associations and recreates the associations with those being posted.



> know more about [Attachments in VTEX Help](https://help.vtex.com/en/search/Attachments)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `SkuId` | object | Array with SKU reference ID that you need identify the SKU IDs |
| `AttachmentNames` | object | Array with all attachments name that you need to associate SKU |




For example, in case you need to associate attachments to SKU ID `799`
You will have to replace de variable `SkuId` for `799` and the variable `AttachmentNames` with attachment array :

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/sku/associateattachments
```

```

    {
       "SkuId":"{{skuId}}",
       "AttachmentNames":["{{attachmentName1}}","{{attachmentName2}}"]
    }
```







## Response object has the following properties:
Response

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `StatusCode` | integer | HTTP Status Code |
| `StatusDescription` | integer | HTTP Status Description|





## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)