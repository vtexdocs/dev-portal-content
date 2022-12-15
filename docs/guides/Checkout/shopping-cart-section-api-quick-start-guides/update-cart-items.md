---
title: "Update cart items"
slug: "update-cart-items"
hidden: false
createdAt: "2022-11-08T19:57:15.132Z"
updatedAt: "2022-11-17T12:54:09.270Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to modify the quantity of an item in the cart or remove it by the API.
[block:callout]
{
  "type": "info",
  "body": "To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint."
}
[/block]
## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart that you want to update cart items information. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Updating shopping cart items quantity

To update items in the shopping cart, you need to use the [Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate) endpoint. In this request, you must send the following information through the URL:
- **Path param**: `orderFormId` value.
- **Query param**: `allowedOutdatedData`. You can set up this query as `false` or `true` to define whether some cart information can be updated through the minicart.

See a URL example below:

`https://accountname.environment.com.br/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/items?allowedOutdatedData=paymentData`

Additionally, you need to send the request body containing the `index` (item's position in the array or cart) and the new `quantity` value. See a request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"orderItems\": [\n          {\n               \"quantity\": 3,\n               \"index\": \"1\"\n          }\n     ]\n}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body with the shopping cart information containing the new item quantity information.
[block:code]
{
  "codes": [
    {
      "code": "...\n\"items\": [\n        {\n            \"uniqueId\": \"BAE0177A615A4EB1B261DDF3274076F8\",\n            \"id\": \"5\",\n            \"productId\": \"7\",\n            \"productRefId\": \"\",\n            \"refId\": null,\n            \"ean\": \"978020137962\",\n            \"name\": \"Ultra Moisturizing Milk Conditioner 100 ml\",\n            \"skuName\": \"100 ml\",\n            \"modalType\": null,\n            \"parentItemIndex\": null,\n            \"parentAssemblyBinding\": null,\n            \"assemblies\": [],\n            \"priceValidUntil\": \"2023-11-08T18:01:42Z\",\n            \"tax\": 0,\n            \"price\": 4490,\n            \"listPrice\": 4490,\n            \"manualPrice\": null,\n            \"manualPriceAppliedBy\": null,\n            \"sellingPrice\": 448840,\n            \"rewardValue\": 0,\n            \"isGift\": false,\n            \"additionalInfo\": {\n                \"dimension\": null,\n                \"brandName\": \"VALDIE&CO\",\n                \"brandId\": \"2000000\",\n                \"offeringInfo\": null,\n                \"offeringType\": null,\n                \"offeringTypeId\": null\n            },\n            \"preSaleDate\": null,\n            \"productCategoryIds\": \"/4/1/\",\n            \"productCategories\": {\n                \"1\": \"Treatments\",\n                \"4\": \"Stylers\"\n            },\n            \"quantity\": 3,\n            \"seller\": \"cosmetics1\",\n            \"sellerChain\": [\n                \"cosmetics1\"\n            ],\n            \"imageUrl\": \"http://cosmetics2.vteximg.com.br/arquivos/ids/155403-55-55/Ultra-Moisturizing-Milk-Conditioner.jpg?v=637109315995300000\",\n            \"detailUrl\": \"/ultra-moisturizing-milk-conditioner/p\",\n            \"components\": [],\n            \"bundleItems\": [],\n            \"attachments\": [],\n            \"attachmentOfferings\": [],\n            \"offerings\": [],\n            \"priceTags\": [\n                {\n                    \"name\": \"discount@price-0e45a4e3-6084-4bf9-bff7-0fe8403699fc#e5b461db-58da-46a0-87b9-fbab27c5caad\",\n                    \"value\": -480,\n                    \"rawValue\": -4.8,\n                    \"isPercentual\": false,\n                    \"identifier\": \"0e45a4e3-6084-4bf9-bff7-0fe8403699fc\",\n                    \"owner\": \"cosmetics2\"\n                }\n            ],\n            \"availability\": \"cannotBeDelivered\",\n            \"measurementUnit\": \"mg\",\n            \"unitMultiplier\": 100.0000,\n            \"manufacturerCode\": null,\n            \"priceDefinition\": {\n                \"calculatedSellingPrice\": 448840,\n                \"total\": 1346520,\n                \"sellingPrices\": [\n                    {\n                        \"value\": 448840,\n                        \"quantity\": 3\n                    }\n                ]\n            }\n        },\n...",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview."
}
[/block]
## Removing shopping cart items

To remove an item from the cart you must use the same endpoint and parameters as in the previous section ([Updating shopping cart items quantity](doc:update-cart-items#updating-shopping-cart-items-quantity)). However, the `quantity` value to be sent in the request body must be `0`. See a request body example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n{\n     \"orderItems\": [\n          {\n               \"quantity\": 0,\n               \"index\": 1\n          }\n     ]\n}\n...",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body with the shopping cart information without the removed item.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD002)**: `"Invalid order form"`. The `orderFormId` information is not valid.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Invalid order form\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d9f54e6-7db4-46d6-bca9-deeb278b8b98\"\n}",
      "language": "json"
    }
  ]
}
[/block]
- **Message error example (code CHK0023)**: `"Invalid quantity for the item"`. This message indicates that the `quantity` value (mandatory) has not been sent in the request body.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK0023\",\n        \"message\": \"Invalid quantity for item\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d9f54e6-7db4-46d6-bca9-deeb278b8b98\"\n}",
      "language": "json"
    }
  ]
}
[/block]
- **Message error example (code CHK0041)**: `"Invalid item index"`. This message indicates that the `index` used in the request does not exist or is incorrect.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK0041\",\n        \"message\": \"Invalid item index\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d9f54e6-7db4-46d6-bca9-deeb278b8b98\"\n}",
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