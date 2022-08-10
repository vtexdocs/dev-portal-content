---
title: "List reservation by ID"
slug: "reservationbyid"
excerpt: "Lists reservation's information by ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.577Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/reservations/reservationId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
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
      "code": "{\n  \"LastUpdateDateUtc\": \"2016-04-15T19:59:40.9832533+00:00\",\n  \"SalesChannel\": \"2\",\n  \"LockId\": \"621a9121-06c9-4731-96d1-edf8c5c23877\",\n  \"ReservationDateUtc\": \"2016-04-15T19:59:40.9832533+00:00\",\n  \"MaximumConfirmationDateUtc\": \"2016-04-15T20:09:40.9832533+00:00\",\n  \"Status\": 1,\n  \"SlaRequest\": [\n    {\n      \"item\": {\n        \"id\": \"2390059\",\n        \"groupItemId\": null,\n        \"quantity\": 1,\n        \"price\": 0,\n        \"modal\": null,\n        \"additionalHandlingTime\": \"00:00:00\",\n        \"dimension\": {\n          \"weight\": 800,\n          \"height\": 10,\n          \"width\": 12,\n          \"length\": 35,\n          \"maxSumDimension\": 0\n        },\n        \"kitItem\": [],\n        \"unlimitedQuantity\": false\n      },\n      \"slaType\": \"Normal\",\n      \"slaTypeName\": \"Normal\",\n      \"freightTableName\": \"Correios PAC\",\n      \"freightTableId\": \"11cc4b6\",\n      \"listPrice\": 10.5,\n      \"promotionalPrice\": 10.5,\n      \"transitTime\": \"2.00:00:00\",\n      \"dockTime\": \"00:00:00\",\n      \"timeToDockPlusDockTime\": \"1.00:00:00\",\n      \"totalTime\": \"3.00:00:00\",\n      \"deliveryWindows\": null,\n      \"wareHouseId\": \"1937054\",\n      \"dockId\": \"1_1_1\",\n      \"wmsEndPoint\": \"\",\n      \"location\": {\n        \"zipCode\": \"22220070\",\n        \"country\": \"BRA\",\n        \"deliveryPointId\": null,\n        \"point\": null,\n        \"inStore\": {\n          \"IsCheckedIn\": false,\n          \"StoreId\": \"180082\"\n        }\n      },\n      \"pickupStoreInfo\": null\n    }\n  ],\n  \"PickupPointItemOptions\": null,\n  \"CanceledDateUtc\": \"0001-01-01T00:00:00+00:00\",\n  \"AuthorizedDateUtc\": \"2016-04-15T19:59:40.9832533+00:00\",\n  \"ConfirmedDateUtc\": \"0001-01-01T00:00:00+00:00\",\n  \"Errors\": [],\n  \"IsSucess\": true\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]