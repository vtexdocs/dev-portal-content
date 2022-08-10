---
title: "List inventory with dispatched reservations"
slug: "getinventorywithdispatchedreservations"
excerpt: "Lists inventory with dispatched reservations. When the number of active reservations is more than 2000 the return is an error with status code 400 (BadRequest) and the message: Too many active reservations."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T21:20:02.145Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/items/itemId/warehouses/warehouseId/dispatched' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request body example"
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
      "code": "{\n  \"skuId\": \"19\",\n  \"warehouseId\": \"1_1\",\n  \"quantity\": 2147483647,\n  \"isUnlimitedQuantity\": true,\n  \"totalReservedQuantity\": 13,\n  \"dispatchedReservationsQuantity\": 0,\n  \"availableQuantity\": 2147483634\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]