---
title: "Delete Hook Configuration"
slug: "deletehookconfiguration"
excerpt: "Deletes Hook configuration."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-02-28T14:18:16.979Z"
---
Learn more about Hook at [VTEX Help.](https://help.vtex.com/tutorial/feed-v3-de-gerenciamento-de-pedidos--5qDml3cQypWDRTgw69s4C1?locale=pt)
[block:api-header]
{
  "title": "Response Codes"
}
[/block]
200 - Success

429 - Too many requests

403 - The credentials is not enabled to access the service

404 - Value not found 

The status event will be removed if it can't deliver a message more than 100 times, 4 days progressively.
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request DELETE 'https://{{accountName}}.vtexcommercestable.com/api/orders/hook/config' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw ''",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]