---
title: "Retrieve payment transaction"
slug: "getpaymenttransaction"
excerpt: "Retrieves transaction details by order ID. All events in the transaction will be registered in this call's response body. \n\nIn scenarios of [order changes](https://developers.vtex.com/vtex-rest-api/reference/registerchange), it is possible to insert a [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe). The total value of the order will be updated after the insertion of the invoice, even when there is a [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenario. The updated value is settled by VTEX's Payment Gateway. The reimbursement for the shopper is automatic."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-06-27T20:21:48.356Z"
---
> Learn more about [Transaction Details in VTEX Help](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details)


## Request object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `orderId` | string | Order Id |



## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------|
| `status` | string | Transaction Status |
| `isActive` | boolean | If is a active transaction |
| `transactionId` | string | Transaction Id |
| `merchantName` | string | Transaction Merchant Name |
| `payments` | object | Payments details object |
| `id` | string | Payment ID |
| `paymentSystem` | string | Payment System Id |
| `paymentSystemName` | string | Payment Sytem Name |
| `value` | integer | Payment Value |
| `installments` | integer | Payment Installments Quantity |
| `referenceValue` | integer | Payment Reference Value |
| `cardHolder` | string | Payment Card Holder |
| `cardNumber` | string | Payment Card Number |
| `firstDigits` | string | Payment Card First Digits |
| `lastDigits` | string | Payment Card Last Digits |
| `cvv2` | string | ??? |
| `expireMonth` | string | Payment Card expire Month |
| `expireYear` | string | Payment Card expire Year |
| `url` | string | Payment URL |
| `giftCardId` | string | Gift Card Id |
| `giftCardName` | string | Gift Card Name |
| `giftCardCaption` | string | Gift Card Caption |
| `authId` | string | Connector Authorization Id |
| `group` | string | Payment Group. It represents the payment method. For each method, it can have the following values: <ul><li>Credit card: `creditCard`</li><li>Debid card: `debitCard`</li><li>Bank invoice: `bankInvoice`</li><li>Promissory: `promissory`</li><li>Gift card: `giftCard`</li><li>Pix: `instantPayment`</li></ul> |
| `tid` | string | Payment Transaction Id |
| `dueDate` | string | Payment Due Date |
| `connectorResponses` | string | Order Id |
| `Tid` | string | Connector Transaction Id |
| `ReturnCode` | string | Connector Return Code |
| `Message` | string | Order Id |
| `authId` | string | Connector Authorization Id |

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/payment-transaction' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Response body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"status\": \"Finished\",\n  \"isActive\": true,\n  \"transactionId\": \"CB452D77E7D04099A4DB0479087B1D2C\",\n  \"merchantName\": \"LUXSTORE\",\n  \"payments\": [\n    {\n      \"id\": \"721CBE1090324D12ABE301FE33DE775A\",\n      \"paymentSystem\": \"4\",\n      \"paymentSystemName\": \"Mastercard\",\n      \"value\": 10150,\n      \"installments\": 1,\n      \"referenceValue\": 10150,\n      \"cardHolder\": null,\n      \"cardNumber\": null,\n      \"firstDigits\": \"412341\",\n      \"lastDigits\": \"4123\",\n      \"cvv2\": null,\n      \"expireMonth\": null,\n      \"expireYear\": null,\n      \"url\": null,\n      \"giftCardId\": null,\n      \"giftCardName\": null,\n      \"giftCardCaption\": null,\n      \"redemptionCode\": null,\n      \"group\": \"creditCard\",\n      \"tid\": \"101770752\",\n      \"dueDate\": null,\n      \"connectorResponses\": {\n        \"Tid\": \"101770752\",\n        \"ReturnCode\": null,\n        \"Message\": null,\n        \"authId\": \"170852\"\n      }\n    }\n  ]\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]