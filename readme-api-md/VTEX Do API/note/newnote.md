---
title: "Create Note"
slug: "newnote"
excerpt: "Creates new note in VTEX Do. Beware of these limitations:\n\r> Maximum number of notes for any single order: 30\n\r> Maximum number of characters in a note's description: 2000"
hidden: false
createdAt: "2019-12-30T19:34:01.284Z"
updatedAt: "2022-01-11T20:54:53.504Z"
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