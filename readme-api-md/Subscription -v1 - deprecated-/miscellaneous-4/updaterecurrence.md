---
title: "Update Subscription"
slug: "updaterecurrence"
excerpt: "Updates details of a given Subscription (formerly recurrence)."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T14:18:36.008Z"
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
      "code": "curl --location --request PUT 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n    \"email\": \"user@vtex.com.br\",\n    \"deliveryDay\": 26,\n    \"deliveryWeekday\": \"Friday\",\n    \"items\": [\n        {\n            \"sku\": \"18\",\n            \"seller\": \"1\",\n            \"quantity\": 2,\n            \"frequency\": {\n                \"periodicity\": \"weekly\",\n                \"interval\": 1\n            },\n            \"shippingAddressId\": \"-1461618656161\"\n        }\n    ],\n    \"paymentAccountId\": \"87FE21B06C0D42908D31A5B11E6FC043\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]