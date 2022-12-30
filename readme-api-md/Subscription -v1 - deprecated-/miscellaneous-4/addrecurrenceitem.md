---
title: "Add Subscription item"
slug: "addrecurrenceitem"
excerpt: "Adds an item to a Subscription (formerly Recurrence)."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T14:18:36.112Z"
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
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions/{{recurrenceId}}/items' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '[\n    {\n        \"sku\": \"20\",\n        \"seller\": \"1\",\n        \"quantity\": 2,\n        \"frequency\": {\n            \"periodicity\": \"monthly\",\n            \"interval\": 1\n        },\n        \"shippingAddressId\": \"-1461618656161\"\n    }\n]'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"sku\": {{ID sku }} ,\n    \"seller\": {{SellerId}},\n    \"quantity\": {{Quantidade}},\n    \"frequency\": {\n      \"periodicity\": {{frequency}}\",\n      \"interval\": {{interval}}\n    },\n    \"shippingAddressId\": {{AddressId}}\n }",
      "language": "json"
    }
  ]
}
[/block]