---
title: "Update inventory by SKU and warehouse"
slug: "updateinventorybyskuandwarehouse"
excerpt: "Updates inventory for a given SKU and warehouse."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2022-11-29T23:35:47.167Z"
---
[block:api-header]
{
  "title": "Request body example"
}
[/block]
The parameter `dateUtcOnBalanceSystem` refers to date and time. It defines the corresponding moment to the informed warehouse. It is useful due to the liberation of handling order's reservations. When requested as `null`, this value will be the date/time of the request. Its format is `DateTimeOffset`, like yyyy-mm-dd-Thh:mm:ss. For example: `2022-03-15T00:52:16`.


[block:code]
{
  "codes": [
    {
      "code": "curl --location --request PUT 'https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/skus/skuId/warehouses/warehouseId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '{\n    \"unlimitedQuantity\": false,\n    \"dateUtcOnBalanceSystem\": \"2022-03-15T00:52:16\",\n    \"quantity\": 101\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]