---
title: "Remove products from Collection by imported file"
slug: "post-removeproductsbyimportfile"
excerpt: "Removes products from a collection from the request body file. The file must be an imported template."
hidden: false
createdAt: "2020-12-21T16:28:05.320Z"
updatedAt: "2022-05-20T22:23:44.385Z"
---
>❗ Due to an issue in our documentation platform, the file upload will not work in the `Try it` button. But you can still use the `cURL` code generated to test it.

[block:callout]
{
  "type": "warning",
  "body": "The file must be an XLS file."
}
[/block]
## Response body has the following properties:

| Attribute     | Type    | Description                                    |
| ------------- | ------- | ---------------------------------------------- |
| `TotalItemProcessed` | integer | Total of items removed from the Collection |
| `TotalErrorsProcessed` | integer | Total of items with error in the Collection |
| `TotalProductsProcessed` | integer | Total of products removed from the Collection |
| `Errors` | array | Errors during the request|


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"TotalItemProcessed\": 4,\n    \"TotalErrorsProcessed\": 0,\n    \"TotalProductsProcessed\": 0,\n    \"Errors\": []\n}",
      "language": "json"
    }
  ]
}
[/block]