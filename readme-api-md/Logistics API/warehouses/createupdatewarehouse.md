---
title: "Create/update warehouse"
slug: "createupdatewarehouse"
excerpt: "Creates or updates your store's warehouses"
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.082Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/warehouses' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '{\n  \"id\": \"15bfc76\",\n  \"name\": \"Estoque Principal\",\n  \"warehouseDocks\": [\n    {\n      \"dockId\": \"1a8bce3\",\n      \"name\": \"Centro de Distribuição Principal\",\n      \"time\": \"3.00:00:00\",\n      \"cost\": \"5.00\",\n      \"translateDays\": \"dias\",\n      \"costToDisplay\": \"5,00\"\n    }\n  ]\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]