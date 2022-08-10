---
title: "Tracking Events with App"
slug: "vtex-log-tracking-events-with-app"
excerpt: "This endpoint is called by the hub to  obtain the tracking events of a series of tracking numbers. This call's request updates the events of a list of tracking codes, for packages that are still pending delivery. The expected response is an object contaning the tracking information and the package's notification ID for every `packageID`."
hidden: false
createdAt: "2021-01-19T15:21:59.966Z"
updatedAt: "2021-01-19T16:42:47.881Z"
---
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"trackingNumber\": \"BR000000000\"\n  }\n]",
      "language": "text",
      "name": "Request example "
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  <trackingNumber>: {\n    \"deliveredDate\": Date,\n    \"events\": [\n      {\n        \"city\": string,\n        \"date\": Date,\n        \"description\": string,\n        \"state\": string\n      }\n    ],\n    \"hasReturnedToSender\": bool,\n    \"isDelivered\": bool\n  }\n}",
      "language": "text",
      "name": "Response Example"
    }
  ]
}
[/block]