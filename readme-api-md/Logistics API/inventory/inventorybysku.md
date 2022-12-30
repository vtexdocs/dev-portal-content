---
title: "List inventory by SKU"
slug: "inventorybysku"
excerpt: "Lists your store's inventory by SKU ID"
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.230Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/skus/skuId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
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
      "code": "{\n  \"skuId\": \"2390059\",\n  \"balance\": [\n    {\n      \"warehouseId\": \"1937054\",\n      \"warehouseName\": \"Estoque A\",\n      \"totalQuantity\": 101,\n      \"reservedQuantity\": 9,\n      \"hasUnlimitedQuantity\": false\n    },\n    {\n      \"warehouseId\": \"avl\",\n      \"warehouseName\": \"Estoque InStore\",\n      \"totalQuantity\": 100,\n      \"reservedQuantity\": 0,\n      \"hasUnlimitedQuantity\": false\n    },\n    {\n      \"warehouseId\": \"1448dc2\",\n      \"warehouseName\": \"Estoque C\",\n      \"totalQuantity\": 100,\n      \"reservedQuantity\": 0,\n      \"hasUnlimitedQuantity\": false\n    },\n    {\n      \"warehouseId\": \"140ac66\",\n      \"warehouseName\": \"Estoque B\",\n      \"totalQuantity\": 100,\n      \"reservedQuantity\": 0,\n      \"hasUnlimitedQuantity\": false\n    },\n    {\n      \"warehouseId\": \"pickuppoint\",\n      \"warehouseName\": \"PickupPoint\",\n      \"totalQuantity\": 100,\n      \"reservedQuantity\": 0,\n      \"hasUnlimitedQuantity\": false\n    },\n    {\n      \"warehouseId\": \"pickuppoint_2\",\n      \"warehouseName\": \"PickupPoint 2\",\n      \"totalQuantity\": 200,\n      \"reservedQuantity\": 0,\n      \"hasUnlimitedQuantity\": false\n    },\n    {\n      \"warehouseId\": \"15bfc76\",\n      \"warehouseName\": \"Estoque Principal\",\n      \"totalQuantity\": 1011,\n      \"reservedQuantity\": 0,\n      \"hasUnlimitedQuantity\": false\n    }\n  ]\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]