---
title: "List warehouse by ID"
slug: "warehousebyid"
excerpt: "Lists the information of a given warehouse, searching by warehouse ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.134Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/warehouses/warehouseId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Response body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\": \"15bfc76\",\n  \"name\": \"Estoque Principal\",\n  \"warehouseDocks\": [\n    {\n      \"dockId\": \"1a8bce3\",\n      \"time\": \"3.00:00:00\",\n      \"cost\": 5\n    }\n  ]\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]