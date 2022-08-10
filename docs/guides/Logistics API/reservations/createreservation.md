---
title: "Create reservation"
slug: "createreservation"
excerpt: "Creates reservation"
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.552Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/reservation' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '{\n  \"salesChannel\": \"2\",\n  \"lockId\": null,\n  \"autorizationExpirationTTL\": \"00:10:00\",\n  \"deliveryItemOptions\": [{\n    \"item\": {\n        \"id\": \"2390059\",\n        \"groupItemId\": null,\n        \"kitItem\": [],\n        \"quantity\": 1,\n        \"price\": 0,\n        \"additionalHandlingTime\": \"00:00:00\",\n        \"dimension\": {\n          \"weight\": 800,\n          \"height\": 10,\n          \"width\": 12,\n          \"length\": 35\n        }\n      },\n    \"slaType\": \"Normal\",\n    \"slaTypeName\": \"Normal\",\n    \"listPrice\": 10.5,\n    \"promotionalPrice\": 10.5,\n    \"transitTime\": \"2.00:00:00\",\n      \"dockTime\": \"00:00:00\",\n      \"timeToDockPlusDockTime\": \"1.00:00:00\",\n      \"aditionalTimeBlockedDays\": \"00:00:00\",\n      \"totalTime\": \"3.00:00:00\",\n    \"deliveryWindows\": [],\n    \"wareHouseId\": null,\n    \"dockId\": null,\n    \"location\": {\n      \"zipCode\": \"22220070\",\n      \"country\": \"BRA\",\n      \"inStore\": {\n          \"IsCheckedIn\": false,\n          \"StoreId\": \"180082\"\n        }\n    }\n  }]\n}'",
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
      "code": "{\n  \"LastUpdateDateUtc\": \"2016-04-15T19:59:20.0397988+00:00\",\n  \"SalesChannel\": \"2\",\n  \"LockId\": \"3bfe679d-c0a8-475a-b315-706f84a9deb4\",\n  \"ReservationDateUtc\": \"2016-04-15T19:59:20.0397988+00:00\",\n  \"MaximumConfirmationDateUtc\": \"2016-04-15T20:09:20.0397988+00:00\",\n  \"Status\": 1,\n  \"SlaRequest\": [\n    {\n      \"item\": {\n        \"id\": \"2390059\",\n        \"groupItemId\": null,\n        \"quantity\": 1,\n        \"price\": 0,\n        \"modal\": null,\n        \"additionalHandlingTime\": \"00:00:00\",\n        \"dimension\": {\n          \"weight\": 800,\n          \"height\": 10,\n          \"width\": 12,\n          \"length\": 35,\n          \"maxSumDimension\": 0\n        },\n        \"kitItem\": [],\n        \"unlimitedQuantity\": false\n      },\n      \"slaType\": \"Normal\",\n      \"slaTypeName\": \"Normal\",\n      \"freightTableName\": \"Correios PAC\",\n      \"freightTableId\": \"11cc4b6\",\n      \"listPrice\": 10.5,\n      \"promotionalPrice\": 10.5,\n      \"transitTime\": \"2.00:00:00\",\n      \"dockTime\": \"00:00:00\",\n      \"timeToDockPlusDockTime\": \"1.00:00:00\",\n      \"totalTime\": \"3.00:00:00\",\n      \"deliveryWindows\": null,\n      \"wareHouseId\": \"1937054\",\n      \"dockId\": \"1_1_1\",\n      \"wmsEndPoint\": \"\",\n      \"location\": {\n        \"zipCode\": \"22220070\",\n        \"country\": \"BRA\",\n        \"deliveryPointId\": null,\n        \"point\": null,\n        \"inStore\": {\n          \"IsCheckedIn\": false,\n          \"StoreId\": \"180082\"\n        }\n      },\n      \"pickupStoreInfo\": null\n    }\n  ],\n  \"PickupPointItemOptions\": null,\n  \"CanceledDateUtc\": \"0001-01-01T00:00:00+00:00\",\n  \"AuthorizedDateUtc\": \"2016-04-15T19:59:20.0397988+00:00\",\n  \"ConfirmedDateUtc\": \"0001-01-01T00:00:00+00:00\",\n  \"Errors\": [],\n  \"IsSucess\": true\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]