---
title: "Simulate a shopping cart"
slug: "simulate-a-shopping-cart"
hidden: false
createdAt: "2022-09-28T13:11:27.754Z"
updatedAt: "2022-11-17T12:25:40.541Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe the process of simulating a shopping cart at Checkout.

## Simulating a shopping cart

The first step is to send the parameters you want to be in the cart. This can be done via the [Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation) endpoint's request body.

See a request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"items\": [\n          {\n               \"id\": \"1\",\n               \"quantity\": 1,\n               \"seller\": \"1\"\n          }\n     ],\n     \"country\": \"BRA\"\n}",
      "language": "json"
    }
  ]
}
[/block]

>ℹ️ The fields `id`, `quantity`, `seller`, and `country` are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview to check the available fields.

After sending the request, the endpoint will return the response body containing the shopping cart information, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "\"items\": [\n        {\n            \"id\": \"1\",\n            \"requestIndex\": 0,\n            \"quantity\": 1,\n            \"seller\": \"1\",\n            \"sellerChain\": [\n                \"1\"\n            ],\n            \"tax\": 0,\n            \"priceValidUntil\": \"2023-09-28T11:53:03Z\",\n            \"price\": 9999,\n            \"listPrice\": 13499,\n            \"rewardValue\": 0,\n            \"sellingPrice\": 2999700,\n            \"offerings\": [],\n            \"priceTags\": [],\n            \"measurementUnit\": \"un\",\n            \"unitMultiplier\": 300.0000,\n            \"parentItemIndex\": null,\n            \"parentAssemblyBinding\": null,\n            \"availability\": \"available\",\n            \"catalogProvider\": \"vrn:vtex.catalog-api-proxy:-:lojadobreno:master:/proxy/authenticated/catalog/pvt/sku/stockkeepingunitbyid/1\",\n            \"priceDefinition\": {\n                \"calculatedSellingPrice\": 2999700,\n                \"total\": 2999700,\n                \"sellingPrices\": [\n                    {\n                        \"value\": 2999700,\n                        \"quantity\": 1\n                    }\n                ]\n            }\n        }\n    ],\n  ...",
      "language": "json"
    }
  ]
}
[/block]
## Error codes

The following errors may appear as a message in the response body.

### 200 - OK

Despite the code `200` (which indicates the success of the request), if the item `id` sent is incorrect or unavailable, the following message will appear.

- **Message error example (code ORD027)**: `"Item 5550 não encontrado ou indisponível"` (*item 5550 not found or unavailable*).
[block:code]
{
  "codes": [
    {
      "code": "\"messages\": [\n        {\n            \"code\": \"ORD027\",\n            \"text\": \"Item 5550 não encontrado ou indisponível\",\n            \"status\": \"error\",\n            \"fields\": {\n                \"id\": \"5550\"\n            }\n        }\n    ]",
      "language": "json"
    }
  ]
}
[/block]
### 400 - Bad Request

The Bad Request error appears for several reasons, such as when a mandatory field was not filled in correctly (eg seller) or the item quantity was not specified. In addition to the 400 error code, an additional code will be shown to indicate the type of error. 

- **Message error example (code ORD005)**: `"O campo Id do item é obrigatório"` (*item ID field is required*).
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD005\",\n        \"message\": \"O campo Id do item é obrigatório\",\n        \"exception\": null\n    },\n    \"operationId\": \"5ac2e42e-0967-43b3-b0b4-dcbc6da118b1\"\n}",
      "language": "json"
    }
  ]
}
[/block]
- **Message error example (code CHK0024)**: `"Id de vendedor de item inválido"` (*invalid item seller id*).
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK0024\",\n        \"message\": \"Id de vendedor de item inválido\",\n        \"exception\": null\n    },\n    \"operationId\": \"7adbc4af-32c8-4365-9f7e-c40ffc9ccf5a\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`. Check that the URL data is correct.
[block:code]
{
  "codes": [
    {
      "code": "<body>\n\t<h1>404 Not Found</h1>\n\t<p>The requested URL was not found on this server.</p>\n</body>",
      "language": "json"
    }
  ]
}
[/block]