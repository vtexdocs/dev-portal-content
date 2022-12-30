---
title: "List all warehouses"
slug: "allwarehouses"
excerpt: "Lists information about all warehouses set up in your store."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.111Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/warehouses' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
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
      "code": "[\n  {\n    \"id\": \"1937054\",\n    \"name\": \"Estoque A\",\n    \"warehouseDocks\": [\n      {\n        \"dockId\": \"1_1_1\",\n        \"time\": \"1.00:00:00\",\n        \"cost\": 0\n      }\n    ]\n  },\n  {\n    \"id\": \"140ac66\",\n    \"name\": \"Estoque B\",\n    \"warehouseDocks\": [\n      {\n        \"dockId\": \"139270d\",\n        \"time\": \"00:00:00\",\n        \"cost\": 0\n      }\n    ]\n  },\n  {\n    \"id\": \"1448dc2\",\n    \"name\": \"Estoque C\",\n    \"warehouseDocks\": [\n      {\n        \"dockId\": \"avl\",\n        \"time\": \"1.00:00:00\",\n        \"cost\": 0\n      }\n    ]\n  },\n  {\n    \"id\": \"avl\",\n    \"name\": \"Estoque InStore\",\n    \"warehouseDocks\": [\n      {\n        \"dockId\": \"avl\",\n        \"time\": \"1.00:00:00\",\n        \"cost\": 0\n      }\n    ]\n  },\n  {\n    \"id\": \"15bfc76\",\n    \"name\": \"Estoque Principal\",\n    \"warehouseDocks\": [\n      {\n        \"dockId\": \"1a8bce3\",\n        \"time\": \"3.00:00:00\",\n        \"cost\": 5\n      }\n    ]\n  },\n  {\n    \"id\": \"pickuppoint\",\n    \"name\": \"PickupPoint\",\n    \"warehouseDocks\": [\n      {\n        \"dockId\": \"pickup_1\",\n        \"time\": \"1.00:00:00\",\n        \"cost\": 1\n      },\n      {\n        \"dockId\": \"pickup_2\",\n        \"time\": \"1.00:00:00\",\n        \"cost\": 1\n      },\n      {\n        \"dockId\": \"pickup_3\",\n        \"time\": \"1.00:00:00\",\n        \"cost\": 1\n      }\n    ]\n  },\n  {\n    \"id\": \"pickuppoint_2\",\n    \"name\": \"PickupPoint 2\",\n    \"warehouseDocks\": [\n      {\n        \"dockId\": \"pickup_2\",\n        \"time\": \"5.00:00:00\",\n        \"cost\": 5\n      }\n    ]\n  }\n]",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]