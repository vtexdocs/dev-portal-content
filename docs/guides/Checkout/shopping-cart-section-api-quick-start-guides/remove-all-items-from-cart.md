---
title: "Remove all items from cart"
slug: "remove-all-items-from-cart"
hidden: false
createdAt: "2022-10-11T17:57:42.451Z"
updatedAt: "2022-11-17T12:28:19.722Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to remove all items from a shopping cart by the API.

## Getting and accessing shopping cart information

The first step is to get the `orderFormId` and access the shopping cart information that you want to remove the items from. To do so, access the [Get cart information by ID](https://developers.vtex.com/docs/guides/get-cart-information-by-id) guide.

See below an example of item details contained in a shopping cart:
[block:code]
{
  "codes": [
    {
      "code": "...\n\"items\": [\n        {\n            \"uniqueId\": \"C6D260865A4B4609B494973D96790104\",\n            \"id\": \"5\",\n            \"productId\": \"7\",\n            \"productRefId\": \"\",\n            \"refId\": null,\n            \"ean\": \"978020137962\",\n            \"name\": \"Ultra Moisturizing Milk Conditioner 100 ml\",\n            \"skuName\": \"100 ml\",\n            \"modalType\": null,\n            \"parentItemIndex\": null,\n            \"parentAssemblyBinding\": null,\n            \"assemblies\": [],\n            \"priceValidUntil\": \"2023-10-11T16:31:28Z\",\n            \"tax\": 0,\n            \"taxCode\": \"54WC8ZN6K8\" ,\n            \"price\": 4490,\n            \"listPrice\": 4490,\n            \"manualPrice\": null,\n            \"manualPriceAppliedBy\": null,\n            \"sellingPrice\": 448509,\n            \"rewardValue\": 0,\n            \"isGift\": false,\n            \"additionalInfo\": {\n                \"dimension\": null,\n                \"brandName\": \"VALDIE&CO\",\n                \"brandId\": \"2000000\",\n                \"offeringInfo\": null,\n                \"offeringType\": null,\n                \"offeringTypeId\": null\n            },\n            \"preSaleDate\": null,\n            \"productCategoryIds\": \"/4/1/\",\n            \"productCategories\": {\n                \"1\": \"Treatments\",\n                \"4\": \"Stylers\"\n            },\n            \"quantity\": 1,\n            \"seller\": \"cosmetics1\",\n            \"sellerChain\": [\n                \"cosmetics1\"\n            ],\n            \"imageUrl\": \"http://cosmetics2.vteximg.com.br/arquivos/ids/155403-55-55/Ultra-Moisturizing-Milk-Conditioner.jpg?v=637109315995300000\",\n            \"detailUrl\": \"/ultra-moisturizing-milk-conditioner/p\",\n            \"components\": [],\n            \"bundleItems\": [],\n            \"attachments\": [],\n            \"attachmentOfferings\": [],\n            \"offerings\": [],\n            \"priceTags\": [\n                {\n                    \"name\": \"discount@price-0e45a4e3-6084-4bf9-bff7-0fe8403699fc#5aeb71dd-f6dd-4a2d-a624-d635f20e7cd0\",\n                    \"value\": -491,\n                    \"rawValue\": -4.91,\n                    \"isPercentual\": false,\n                    \"identifier\": \"0e45a4e3-6084-4bf9-bff7-0fe8403699fc\",\n                    \"owner\": \"cosmetics2\"\n                }\n            ],\n            \"availability\": \"available\",\n            \"measurementUnit\": \"mg\",\n            \"unitMultiplier\": 100.0000,\n            \"manufacturerCode\": null,\n            \"priceDefinition\": {\n                \"calculatedSellingPrice\": 448509,\n                \"total\": 448509,\n                \"sellingPrices\": [\n                    {\n                        \"value\": 448509,\n                        \"quantity\": 1\n                    }\n                ]\n            }\n        },\n  ...",
      "language": "json"
    }
  ]
}
[/block]

> ℹ️️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Removing all items from the shopping cart 

To remove all items from the shopping cart, you need to use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint. In this request, the `ordeFormId` of the shopping cart must be sent through the URL request, as shown by the example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/{orderFormId}/items/removeAll`

Additionally, you need to send the request body containing only two curly brackets, as shown below:
[block:code]
{
  "codes": [
    {
      "code": "{}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body with all item information removed from the shopping cart (`"items"` field empty).
[block:code]
{
  "codes": [
    {
      "code": "...\n\"items\": [],\n...  ",
      "language": "json"
    }
  ]
}
[/block]
## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD002)**: `"Carrinho inválido"` (*Invalid Cart*): this message indicates that the `orderFormId` used in the request does not exist or is incorrect.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Carrinho inválido\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d37a185-bfe6-4686-9d92-aac9482cc63d\"\n}",
      "language": "json"
    }
  ]
}
[/block]
- **Message error example (code 001)**: `"Bad Request"`: this message indicates that information other than `{}` was sent in the request body.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"001\",\n        \"message\": \"Bad request\",\n        \"exception\": null\n    },\n    \"operationId\": \"91b68251-1a60-4716-b846-c7c9c31fa565\"\n}",
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