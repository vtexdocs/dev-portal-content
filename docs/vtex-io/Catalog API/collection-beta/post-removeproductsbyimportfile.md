---
title: "Remove products from Collection by imported file"
slug: "post-removeproductsbyimportfile"
excerpt: "Removes products from a collection from the request body file. The file must be an imported template"
hidden: false
createdAt: "2020-12-21T16:28:05.320Z"
updatedAt: "2021-03-01T21:19:32.142Z"
---
To add the file to the request body, you must use a `form-data` body. Once you select this form, the request body expects two variables: a key and a value.
[block:parameters]
{
  "data": {
    "h-0": "Key",
    "h-1": "Value",
    "0-0": "This needs to be a type `file` key.",
    "0-1": "Here you will select the Products file on your computer. The file must be an imported template from [Import Collection file example](ref:get-importfileexample) endpoint."
  },
  "cols": 2,
  "rows": 1
}
[/block]
Once you selected the file, you can send the request.
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