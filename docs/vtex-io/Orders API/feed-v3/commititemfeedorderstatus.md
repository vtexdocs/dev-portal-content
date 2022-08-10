---
title: "Commit item feed order status"
slug: "commititemfeedorderstatus"
excerpt: "Acknowledges an item's feed order status."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-04-17T04:43:28.241Z"
---
Learn know more about Feed v3 in [VTEX Help.](https://help.vtex.com/tutorial/feed-v3-de-gerenciamento-de-pedidos--5qDml3cQypWDRTgw69s4C1?locale=pt)
[block:api-header]
{
  "title": "Request object has the following properties"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "handles",
    "0-1": "string",
    "0-2": "List of status order event handles (as seen in [Retrieve feed order status](https://developers.vtex.com/reference/feed-v3#getfeedorderstatus1))"
  },
  "cols": 3,
  "rows": 1
}
[/block]

[block:api-header]
{
  "title": "Response codes"
}
[/block]
200 - Success

429 - Too many requests

403 - The credentials are not enabled to access the service

404 - Value not found
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{accountName}}.vtexcommercestable.com/api/orders/feed' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n    \"handles\":[\n        \"AQEBSM/bSqonHYtx+UrHdbuJ0i7M9yMbI2jtYwMIPdEc4BenuneaCTC9VEJ3dgAy1XtfQvHBvgwZTO8LvGObIKNqiKXDZiMKY25vK+pblZEqf1pWdLMugu5XoHA5ZAd4IcBcXrBcrlr1GU8uvPEBoVLOsVBP9IAxIZkkeEedIDg3K6GPyEXVuPlTEYb/0OCunEGxWF+AZ1frFdXh7ulORTcuqO5oDlBGbpD+QYzCmF4mUZtQ0VVWh9icM1QBVh6PlJ0D/lfwnJKWpBn3jf8c+DTm7sD7wb1Lcz9uWMLhDtPwvH9vue4MvKU9sCahEQe7K5jWuwwb54szGbFKdfcACsTSQ9WlyBfMdbV83c27k68G3cnaBFExkC1MLHHE9UzpQ6l4s43BT4k95ocgMXffnj/HMUYXn+OCvlvjytY59x1OCRE=\"\n    ]\n}'",
      "language": "text",
      "name": "Example request"
    }
  ]
}
[/block]