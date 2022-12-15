---
title: "Add payment data attachment to the cart"
slug: "add-payment-data-to-the-cart"
hidden: true
createdAt: "2022-11-28T18:26:30.450Z"
updatedAt: "2022-11-28T18:32:23.152Z"
---
The shopping cart is where the information of the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add payment information in the shopping cart by the API. 
[block:callout]
{
  "type": "warning",
  "body": "The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows the platform to update any relevant information that may be impacted by the payment method."
}
[/block]
## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart you want to add the merchant context data to. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding payment data to the shopping cart

To add payment data to the shopping cart, you need to use the [Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown by the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/paymentData`

Additionally, you need to send the request body containing the following payment data information:

- `paymentSysytem`: payment system ID.
- `paymentSystemName`: payment system name.
- `group`: payment system group.
- `installments`: number of installments.
- `installmentsInterestRate`: installments interest rate.
- `installmentsValue`: value of each installment.
- `value`: total value assigned to this payment.
- `referenceValue`: reference value used to calculate total order value with interest.
- `hasDefaultBillingAddress`: indicates whether billing address for this payment is the default address.

See a request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"payments\": [\n          {\n               \"paymentSysytem\": 1,\n               \"paymentSystemName\": \"Boleto Bancário\",\n               \"group\": \"bankInvoicePaymentGroup\",\n               \"installments\": 3,\n               \"installmentsInterestRate\": 0,\n               \"installmentsValue\": 100,\n               \"value\": 300,\n               \"referenceValue\": 300,\n               \"hasDefaultBillingAddress\": false\n          }\n     ]\n}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body containing the payment data information in the shopping cart, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n\"paymentData\": {\n        \"updateStatus\": \"updated\",\n        \"installmentOptions\": [\n            {\n                \"paymentSystem\": \"1\",\n                \"bin\": null,\n                \"paymentName\":  \"Boleto Bancário\",\n                \"paymentGroupName\": \"bankInvoicePaymentGroup\",\n                \"value\": 300,\n                \"installments\": [\n                    {\n                        \"count\": 3,\n                        \"hasInterestRate\": false,\n                        \"interestRate\": 0,\n                        \"value\": 300,\n                        \"total\": 300,\n                        \"sellerMerchantInstallments\": [\n                            {\n                                \"id\": \"COSMETICS2\",\n                                \"count\": 3,\n                                \"hasInterestRate\": false,\n                                \"interestRate\": 0,\n                                \"value\": 300,\n                                \"total\": 300\n                            }\n                        ]\n                    }\n                ]\n            }\n...",
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
- **Message error example (code ORD020)**: `"Invalid payment"`. The `referenceValue` information has not been sent.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD020\",\n        \"message\": \"Invalid payment\",\n        \"exception\": null\n    },\n    \"operationId\": \"9d14e7af-a63d-4c26-8974-bad734b758da\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check that the URL data is correct.
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