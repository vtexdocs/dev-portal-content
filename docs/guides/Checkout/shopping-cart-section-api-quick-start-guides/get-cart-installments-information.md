---
title: "Get cart installments information"
slug: "get-cart-installments-information"
hidden: false
createdAt: "2022-10-28T18:00:21.483Z"
updatedAt: "2022-11-17T12:47:05.110Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to obtain information about the number of installments and their respective amounts from an existing payment method in the shopping cart.
[block:callout]
{
  "type": "warning",
  "body": "Before starting the search for information about installments, make sure that there is already payment information (`paymentData`) assigned to the chosen cart (`orderFormId`)."
}
[/block]
## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart information that you want to obtain information about the amount of installments. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.


## Accessing cart installments information

With the `orderFormId` information available, you must use the [Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments) endpoint to send the following information through the URL:

- **Path Param**: `orderFormId` value.
- **Query Param**: `paymentSystem`. Payment method Id in which the installments information will be consulted.

See an URL example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/9420cbb7ebc34ca68a86621428816c5a?paymentSystem=2`

After sending the request, the endpoint will return the response body containing the installments information, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n{\n      \"paymentSystem\": \"2\",\n      \"bin\": null,\n      \"paymentName\": null,\n      \"paymentGroupName\": null,\n      \"value\": 6940,\n      \"installments\": [\n          {\n             \"count\": 1,\n             \"hasInterestRate\": false,\n             \"interestRate\": 0,\n             \"value\": 6940,\n             \"total\": 6940,\n             \"sellerMerchantInstallments\": [\n                  {\n                     \"id\": \"COSMETICS2\",\n                     \"count\": 1,\n                     \"hasInterestRate\": false,\n                     \"interestRate\": 0,\n                     \"value\": 6940,\n                     \"total\": 6940\n                   }\n              ]\n          }\n      ]\n}\n...\n",
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
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Invalid order form\",\n        \"exception\": null\n    },\n    \"operationId\": \"d6a5b535-68b4-49f7-a783-93762974554b\"\n}",
      "language": "json"
    }
  ]
}
[/block]
- **Message error example (code CHK0152)**: `"Orderform does not have installment options"`. This shopping cart does not have any payment information (`paymentData`).
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK0152\",\n        \"message\": \"Orderform does not have installment options\",\n        \"exception\": null\n    },\n    \"operationId\": \"6d8408b4-3adf-4fc7-b708-8d322b3e021f\"\n}\n",
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