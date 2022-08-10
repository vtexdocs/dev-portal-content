---
title: "Create Note"
slug: "newnote"
excerpt: "Creates new note in VTEX Do."
hidden: false
createdAt: "2019-12-30T19:34:01.284Z"
updatedAt: "2020-03-02T15:02:24.174Z"
---
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/do/notes' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"target\": \n    {\n      \"id\": \"v964735bdev-01\",\n      \"type\": \"order\",\n      \"url\": \"https://basedevmkp.vtexcommercebeta.com.br/admin/checkout/#/orders/v964741bdev-01\"\n    },\n  \"domain\": \"oms\",\n  \"description\": \"Id do pedido no marketplace é 786-09\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]