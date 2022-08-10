---
title: "Retrieve SkuId list by RefId list"
slug: "catalog-api-get-sku-list-productid"
excerpt: "Receives a list of Reference IDs and returns the same list with the corresponding SKU IDs."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-04-22T15:07:05.062Z"
---
Identify the SKU ID by a list of SKU Reference ID

Send a list of Reference Codes, and returns the same list with the correspondent Sku Id.  

If the Reference Code is not found, a `null` will return associated to it.



> know more about [SKU in VTEX Help](https://help.vtex.com/en/search/SKU)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `body` | object | Array with SKU reference ID that you need identify the SKU IDs |



For example, in case you need get the SKU ID for the SKU reference ID `799`

You will have to replace de variable `refId` for `799`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/799
```






## Response body has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `body` | object | Object compose by list of SKU IDs related to Reference ID list searched |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"D25133K-B2\": null,\n    \"14-556\": null,\n    \"123\": null,\n    \"DCF880L2-BR\": null\n}",
      "language": "json"
    }
  ]
}
[/block]
## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)