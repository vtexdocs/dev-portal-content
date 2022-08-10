---
title: "Create/Update Carrier"
slug: "createupdatecarrier"
excerpt: "This endpoint creates or updates carriers in your store. Fill in the params to check out an example of request."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-04-22T19:30:21.582Z"
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
      "code": "{\n    \"id\": \"13942e4\",\n    \"slaType\": \"Expressa\",\n    \"name\": \"Transportadora Expressa\",\n    \"scheduledDelivery\": false,\n    \"maxRangeDelivery\": 0,\n    \"dayOfWeekForDelivery\": null,\n    \"dayOfWeekBlockeds\": [],\n    \"freightValue\": [],\n    \"factorCubicWeight\": null,\n    \"freightTableProcessStatus\": 1,\n    \"freightTableValueError\": null,\n    \"modals\": [],\n    \"onlyItemsWithDefinedModal\": false,\n    \"deliveryOnWeekends\": false,\n    \"carrierSchedule\": [],\n    \"maxDimension\": {\n      \"weight\": 0,\n      \"height\": 0,\n      \"width\": 0,\n      \"length\": 0,\n      \"maxSumDimension\": 0\n    },\n    \"exclusiveToDeliveryPoints\": false,\n    \"minimunCubicWeight\": 0,\n    \"isPolygon\": false,\n    \"numberOfItemsPerShipment\": null\n  }",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]


[block:api-header]
{
  "title": "Create/Update Carrier by Delivery windows"
}
[/block]
If you wish to update or create a carrier while adding a **delivery window**, use the example of request below as a guide. For adding days of the week through the variable {{dayOfWeek}}, consider Sunday = 0, Monday = 1, Tuesday = 3, and so on, until Saturday = 6. 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\": \"11cc4b5\",\n  \"name\": \"Entrega Agendada\",\n  \"slaType\": \"Entrega Agendada\",\n  \"factorCubicWeight\": null,\n  \"minimunCubicWeight\": null,\n  \"numberOfItemsPerShipment\": null,\n  \"modals\": [],\n  \"onlyItemsWithDefinedModal\": false,\n  \"maxDimension\": {\n    \"maxSumDimension\": null,\n    \"height\": null,\n    \"length\": null\n  },\n  \"scheduledDelivery\": true,\n  \"maxRangeDelivery\": 7,\n  \"dayOfWeekForDelivery\": [\n    {\n      \"dayOfWeek\": 0,\n      \"deliveryRanges\": [\n        {\n          \"startTime\": \"08:00:00\",\n          \"endTime\": \"12:00:00\",\n          \"listPrice\": 10\n        },\n        {\n          \"startTime\": \"12:01:00\",\n          \"endTime\": \"18:00:00\",\n          \"listPrice\": 10\n        }\n      ]\n    },\n    {\n      \"dayOfWeek\": 1,\n      \"deliveryRanges\": [\n        {\n          \"startTime\": \"08:00:00\",\n          \"endTime\": \"12:00:00\",\n          \"listPrice\": 10\n        },\n        {\n          \"startTime\": \"12:01:00\",\n          \"endTime\": \"18:00:00\",\n          \"listPrice\": 10\n        }\n      ]\n    },\n    {\n      \"dayOfWeek\": 2,\n      \"deliveryRanges\": [\n        {\n          \"startTime\": \"08:00:00\",\n          \"endTime\": \"12:00:00\",\n          \"listPrice\": 10\n        },\n        {\n          \"startTime\": \"12:01:00\",\n          \"endTime\": \"18:00:00\",\n          \"listPrice\": 10\n        }\n      ]\n    },\n    {\n      \"dayOfWeek\": 3,\n      \"deliveryRanges\": [\n        {\n          \"startTime\": \"08:00:00\",\n          \"endTime\": \"12:00:00\",\n          \"listPrice\": 10\n        },\n        {\n          \"startTime\": \"12:01:00\",\n          \"endTime\": \"18:00:00\",\n          \"listPrice\": 10\n        }\n      ]\n    },\n    {\n      \"dayOfWeek\": 4,\n      \"deliveryRanges\": [\n        {\n          \"startTime\": \"08:00:00\",\n          \"endTime\": \"12:00:00\",\n          \"listPrice\": 10\n        },\n        {\n          \"startTime\": \"12:01:00\",\n          \"endTime\": \"18:00:00\",\n          \"listPrice\": 10\n        }\n      ]\n    },\n    {\n      \"dayOfWeek\": 5,\n      \"deliveryRanges\": [\n        {\n          \"startTime\": \"08:00:00\",\n          \"endTime\": \"12:00:00\",\n          \"listPrice\": 10\n        },\n        {\n          \"startTime\": \"12:01:00\",\n          \"endTime\": \"18:00:00\",\n          \"listPrice\": 10\n        }\n      ]\n    },\n    {\n      \"dayOfWeek\": 6,\n      \"deliveryRanges\": [\n        {\n          \"startTime\": \"08:00:00\",\n          \"endTime\": \"12:00:00\",\n          \"listPrice\": 10\n        },\n        {\n          \"startTime\": \"12:01:00\",\n          \"endTime\": \"18:00:00\",\n          \"listPrice\": 10\n        }\n      ]\n    }\n  ],\n  \"deliveryOnWeekends\": false,\n  \"carrierSchedule\": []\n}",
      "language": "text",
      "name": "Delivery Windows"
    }
  ]
}
[/block]