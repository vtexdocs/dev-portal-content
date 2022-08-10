---
title: "Delete Feed Configuration"
slug: "feedconfigurationdelete"
excerpt: "Deletes the configuration set up in Feed v3."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-02-28T14:18:16.781Z"
---
Learn  more about Feed v3 in [VTEX Help.](https://help.vtex.com/tutorial/feed-v3-de-gerenciamento-de-pedidos--5qDml3cQypWDRTgw69s4C1?locale=pt)
[block:api-header]
{
  "title": "Response codes"
}
[/block]
200 - Success

403 - The credentials are not enabled to access the service

400 - Bad Request - "Unable to check address" / "Only https scheme is accepted"

404 - Value not found

429 - Too many requests
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request DELETE 'https://{{accountName}}.vtexcommercestable.com/api/orders/feed/config' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw ''",
      "language": "text"
    }
  ]
}
[/block]