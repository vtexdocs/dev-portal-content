---
title: "Import Status"
slug: "importstatus"
excerpt: "This endpoint will indicate the current status of the [Import request](https://developers.vtex.com/vtex-rest-api/reference/import?showHidden=a2b51#importxlsx)."
hidden: true
createdAt: "2021-06-24T00:05:45.690Z"
updatedAt: "2021-06-24T00:09:19.120Z"
---
## Request has the following properties:

| Attribute              | Type             | Description                                                                                                                                                                                                  |
| ---------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| status | string           | Import status.                                                                                                                                            |
| percentage | integer           | Percentage of the current status of the [Import request](https://developers.vtex.com/vtex-rest-api/reference/import?showHidden=a2b51#importxlsx).   

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"status\": \"Completed\",\n    \"percentage\": 100\n}",
      "language": "json"
    }
  ]
}
[/block]