---
title: "Add cart items"
slug: "add-cart-items"
hidden: false
createdAt: "2022-11-08T18:49:48.631Z"
updatedAt: "2022-11-17T12:52:06.253Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add new items to a shopping cart by the API.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart to which you want to add items. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding items to the shopping cart

To add items to the shopping cart, you need to use the [Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items) endpoint. In this request, you must send the following information through the URL:

- **Path param**: `orderFormId` value.
- **Query param**: `allowedOutdatedData`. You can set up this query as `false` or `true` to define whether some cart information can be updated through the minicart.

See a URL example below:

`https://accountname.environment.com.br/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/items?allowedOutdatedData=paymentData`

Additionally, you must send the request body containing the following information about the new item to be added to the cart:

- `quantity`
- `seller`
- `id`
- `index`
- `price`

>ℹ️ `price` should be sent only in case you want to make a bulk price change.

See a request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"orderItems\": [\n          {\n               \"quantity\": 3,\n               \"seller\": \"cosmetics1\",\n               \"id\": \"2005\",\n               \"index\": 0\n          }\n     ]\n}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body containing the shopping cart information including the new item added, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n\"items\": [\n        {\n            \"uniqueId\": \"D1E0949706A3441DA0386929FAB6E7E8\",\n            \"id\": \"2005\",\n            \"productId\": \"3\",\n            \"productRefId\": \"\",\n            \"refId\": null,\n            \"ean\": \"978020137962\",\n            \"name\": \"Weightless Waves Mild Lather Cleanser 50 ml\",\n            \"skuName\": \"50 ml\",\n            \"modalType\": null,\n            \"parentItemIndex\": null,\n            \"parentAssemblyBinding\": null,\n            \"assemblies\": [],\n            \"priceValidUntil\": \"2023-11-07T22:14:44Z\",\n            \"tax\": 0,\n            \"price\": 3190,\n            \"listPrice\": 3190,\n            \"manualPrice\": null,\n            \"manualPriceAppliedBy\": null,\n            \"sellingPrice\": 3107,\n            \"rewardValue\": 0,\n            \"isGift\": false,\n            \"additionalInfo\": {\n                \"dimension\": null,\n                \"brandName\": \"VALDIE&CO\",\n                \"brandId\": \"2000000\",\n                \"offeringInfo\": null,\n                \"offeringType\": null,\n                \"offeringTypeId\": null\n            },\n            \"preSaleDate\": null,\n            \"productCategoryIds\": \"/2/\",\n            \"productCategories\": {\n                \"2\": \"Computers\"\n            },\n            \"quantity\": 3,\n            \"seller\": \"cosmetics1\",\n            \"sellerChain\": [\n                \"cosmetics1\"\n            ],\n            \"imageUrl\": \"http://cosmetics2.vteximg.com.br/arquivos/ids/155401-55-55/ID-001-MAIN.jpg?v=637109313796670000\",\n            \"detailUrl\": \"/weightless-waves-mild-lather-cleanser/p\",\n            \"components\": [],\n            \"bundleItems\": [],\n            \"attachments\": [],\n            \"attachmentOfferings\": [],\n            \"offerings\": [],\n            \"priceTags\": [\n                {\n                    \"name\": \"discount@price-0e45a4e3-6084-4bf9-bff7-0fe8403699fc#ac2d3d37-5845-45a6-9254-191449d6f100\",\n                    \"value\": -416,\n                    \"rawValue\": -4.160,\n                    \"isPercentual\": false,\n                    \"identifier\": \"0e45a4e3-6084-4bf9-bff7-0fe8403699fc\",\n                    \"owner\": \"cosmetics2\"\n                }\n            ],\n            \"availability\": \"available\",\n            \"measurementUnit\": \"un\",\n            \"unitMultiplier\": 1.0000,\n            \"manufacturerCode\": null,\n            \"priceDefinition\": {\n                \"calculatedSellingPrice\": 3107,\n                \"total\": 15534,\n                \"sellingPrices\": [\n                    {\n                        \"value\": 3107,\n                        \"quantity\": 4\n                    },\n                    {\n                        \"value\": 3106,\n                        \"quantity\": 1\n                    }\n                ]\n            }\n        },\n... \n  ",
      "language": "json"
    }
  ]
}
[/block]

>ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview.

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
- **Message error example (code CHK0024)**: `"Invalid seller for item"`. This message indicates that the `seller` used in the request does not exist, is incorrect or has not been informed.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK0024\",\n        \"message\": \"Invalid seller for item\",\n        \"exception\": null\n    },\n    \"operationId\": \"abe5d1b9-a85f-4f10-a3e8-f783082c5c3d\"\n}",
      "language": "json"
    }
  ]
}
[/block]

### 403 - Forbidden

- **Message error example (code CHK003)**: `"Access denied"`. This message indicates that it is not possible to make a bulk price change on this item.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK003\",\n        \"message\": \"Access denied\",\n        \"exception\": null\n    },\n    \"operationId\": \"a6ea8b84-68d9-43a7-902e-846e8c5c05b6\"\n}",
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
