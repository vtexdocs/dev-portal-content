---
title: "Retrieve Feed Configuration"
slug: "getfeedconfiguration"
excerpt: "Lists a given Feed's configuration details."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-02-28T14:18:16.687Z"
---
[block:api-header]
{
  "title": "Request has the following properties:"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "accountName",
    "0-1": "string",
    "0-2": "Account Name"
  },
  "cols": 3,
  "rows": 1
}
[/block]

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.vtexcommercestable.com/api/orders/feed/config' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text"
    }
  ]
}
[/block]