---
title: "Integrating inStore to a new payment acquirer"
slug: "integrating-instore-to-a-new-payment-acquirer"
hidden: true
createdAt: "2021-08-17T20:00:23.079Z"
updatedAt: "2021-08-17T20:24:18.657Z"
---

This article aims to explain how the inStore app configures AppLinking for `payment` and `payment-reversal` actions with the acquirers' apps.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/integrating-instore-to-a-new-payment-acquirer-0.png)

## Setting fields

All acquirers must have:
```json
{
  "data": {
    "h-0": "Field name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`acquirerProtocol`",
    "0-1": "string",
    "0-2": "The AppLinking protocol, that is, the payment app scheme. Ex: `stone`, `cielo-lio`, `cappta`.",
    "1-0": "`scheme`",
    "2-0": "`autoConfirm`",
    "3-0": "`acquirerId`",
    "1-1": "string",
    "1-2": "The scheme to which the payment app's' Intent will respond. The default value is `instore`.",
    "2-1": "boolean",
    "3-1": "string",
    "2-2": "The default value is `True`. Tells the app that it doesn't need to ask the user for any further permission to complete the action.",
    "3-2": "Affiliation ID of the acquirer which is registered in [VTEX Payments module](https://help.vtex.com/en/tutorial/setting-up-app-linking-for-payments-app-in-instore#setting-up-instore-connector-in-vtex-pci-gateway). Ex: `<stone_code>`, `<sitef_storeId>`."
  },
  "cols": 3,
  "rows": 4
}
```

If necessary, inStore can send additional information. Example with the sub-acquirer **Cappta**:
```json
{
  "data": {
    "0-0": "`authKey`",
    "0-1": "string",
    "1-1": "string",
    "2-1": "string",
    "3-1": "string",
    "h-0": "Field name",
    "h-1": "Type",
    "h-2": "Description",
    "0-2": "For example, `<cappta_authKey>`.",
    "1-2": "For example, `<cappta_authPassword>`.",
    "2-2": "Default password. For example, `cappta`.",
    "1-0": "`authPassword`",
    "2-0": "`administrativePassword`",
    "3-0": "`cnpj`",
    "3-2": "Company ID number."
  },
  "cols": 3,
  "rows": 4
}
```

```json
{
  "type": "info",
  "body": "To create any extra configuration, you need to send an email to the inStore team (instoredevs@vtex.com.br) informing the additional information the app needs to complete the transaction. With that, we will create a form on the **Payments** module so that customers can configure their acquirer."
}
```

## Sending URI and response URI for each action

Action: `payment` or `payment-reversal` (refund a previous payment).

- URI pattern that is sent by AppLinking:

```
<acquirerProtocol>://<action>?<params>
```

- Default URI received by AppLinking:

```
instore://<action>?<response_params>
```

## Sample sending URI for each action

### Example for the `payment` action

Payment context that is used to mount the URI (to make it easier to read):

```json
{
  acquirerProtocol: "super-acquirer",
  action: "payment",
  acquirerId: "954090369",
  installmentType: 2, // 1: the interest for each installment is applied by the bank or by the credit card; 2: the store is responsible for interest on installments
  installments: 3,
  paymentId: "1093019888",
  paymentType: "debit",  // may also be "credit"
  amount: 10, // payment apps usually expect the amount in cents (10 cents, in this example)
  installmentsInterestRate: "1%" // if the payment has no interest rate, it should not be on mobileLinkingUrl
  transactionId: "1093019039",
  scheme: "instore",
  urlCallback: "instore://payment",
  autoConfirm: "True",
  paymentSystem: 44,
  paymentSystemName: "Venda Direta Debito",
  paymentGroupName: "debitDirectSalePaymentGroup",
  sellerName: "instoreqa",
  payerEmail: 'customeremail@gmail.com', // Customer's e-mail
  payerIdentification: '12345678909', // Customer's document
  mobileLinkingUrl: "super-acquirer://payment?acquirerId=954090369&paymentId=1093019888&paymentType=debit&amount=10&installments=3&transactionId=1093019039&autoConfirm=True&scheme=instore&urlCallback=instore://payment"
}
```

Final URI that the payment app will receive to perform the payment action with the context of the above example:

```
super-acquirer://payment?acquirerProtocol=super-acquirer&action=payment&acquirerId=954090369&installmentType=2&installments=3&paymentId=1093019888&paymentType=debit&amount=10&installmentsInterestRate=1%&transactionId=1093019039&paymentSystem=44&paymentSystemName=Venda%20Direta%20Debito&paymentGroupName=debitDirectSalePaymentGroup&sellerName=instoreqa&payerIdentification=12345678909&payerEmail=customeremail%40gmail.com&scheme=instore&urlCallback=instore://payment&autoConfirm=True
```

With the values present in this URI, it will be possible to reimburse this payment.

### Example for the `payment-reversal` action (refund)

Refund context used to assemble the URI (in order to make it easier to read):

```json
{
  acquirerProtocol: "super-acquirer",
  action: "payment-reversal",
  acquirerAuthorizationCode: "86273634-3a05-4f0a-a430-f55ed3f21eab", // identifies the payment transaction
  acquirerId: "954090369",
  transactionId: "1093019039",
  paymentId: "1093019888",
  acquirerTid: "1093019888",
  administrativeCode: "11010103033", // This ammount must be received from the payment and is saved in VTEX PCI Gateway.
  autoConfirm: "True",
  sellerName: "instoreqa",
  scheme: "instore",
  urlCallback: "instore://payment-reversal",
  mobileLinkingUrl: "super-acquirer://payment-reversal?acquirerAuthorizationCode=86273634-3a05-4f0a-a430-f55ed3f21eab&acquirerId=954090369&paymentId=1093019888&transactionId=1093019039&autoConfirm=True&scheme=instore&urlCallback=instore://payment-reversal"
}
```

Final URI that the payment app will receive to perform the refund action with the context of the above example:

```
super-acquirer://payment-reversal?acquirerAuthorizationCode=86273634-3a05-4f0a-a430-f55ed3f21eab&acquirerId=954090369&transactionId=1093019039&paymentId=1093019888&acquirerTid=1093019888&administrativeCode=11010103033&sellerName=instoreqa&autoConfirm=True&scheme=instore&urlCallback=instore://payment-reversal
```

>⚠️ Not all parameters will be used by all payment acquirers/apps. Example: <code>transactionId</code>. This parameter is the ID of a transaction in VTEX that identifies all payments of a complete order on VTEX PCI Gateway. A transaction can contain multiple payments, such as when an order is paid with multiple credit or debit cards.

## Examples of response URIs for each action

### Example for the `payment` action

URI:

```
Success: instore://payment?responsecode=0&<response_params>
Failed:  instore://payment?responsecode=110&reason=card+refused+by+acquirer&paymentId=<value_of_the_sender_URI>
```

Response Parameters:
```json
{
  "data": {
    "h-0": "Field name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`scheme`",
    "0-2": "`instore`",
    "0-1": "string",
    "1-0": "`action`",
    "1-1": "string",
    "1-2": "`payment",
    "2-0": "`paymentId`",
    "2-1": "string",
    "2-2": "Payment identification in VTEX",
    "3-0": "`cardBrandName`",
    "3-1": "string",
    "3-2": "Brand name, such as`mastercard`,`visa`, etc.",
    "4-0": "`firstDigits`",
    "4-1": "string",
    "5-1": "string",
    "6-1": "string",
    "4-2": "Card BIN / IIN (first six digits)",
    "5-2": "Card last four digits",
    "5-0": "`lastDigits`",
    "6-0": "`acquirerName`",
    "6-2": "Name of the acquirer (optional)",
    "7-0": "`tid`",
    "7-1": "string",
    "7-2": "Transaction identification code required to perform a refund action",
    "8-0": "`acquirerAuthorizationCode`",
    "8-1": "string",
    "8-2": "Transaction authorization code generated by the acquirer",
    "9-0": "`nsu`",
    "9-1": "string",
    "9-2": "Unique sequential number that identifies the operation",
    "10-0": "`merchantReceipt`",
    "10-1": "string",
    "11-1": "string",
    "11-0": "`customerReceipt`",
    "12-0": "`responsecode`",
    "12-1": "integer",
    "12-2": "`0`means success; values greater than`0` mean acquirer error codes, in which case the `reason` parameter will be an error message",
    "13-2": "On success, the value is empty; in case of error, it contains the error message",
    "13-1": "string",
    "14-1": "boolean",
    "13-0": "`reason`",
    "14-0": "`success`",
    "14-2": "Generated by the app given the value of`responsecode`",
    "10-2": "Text of the receipt for the establishment. Must be in the URI",
    "11-2": "Text of the receipt for the client. Must be in the URI"
  },
  "cols": 3,
  "rows": 15
}
```

### Example for the `payment-reversal` action (refund)

URI:

```
Success: instore://payment-reversal?responsecode=0&<response_params>
Failed:  instore://payment-reversal?responsecode=110&reason=card+refused+by+acquirer&paymentId=<id_sent_previously>
```

Response parameters:
```json
{
  "data": {
    "h-0": "Field name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`scheme`",
    "0-1": "string",
    "0-2": "`instore`",
    "1-1": "string",
    "1-2": "`payment-reversal`",
    "1-0": "`action`",
    "2-0": "`paymentId`",
    "2-1": "string",
    "2-2": "Ex: `1093019888` - to identify which payment was refunded",
    "3-0": "`paymentAcquirerAuthorizationCode`",
    "3-1": "string",
    "4-1": "string",
    "3-2": "Authorization code that was used for the refund action (`tid`)",
    "4-0": "`acquirerAuthorizationCode`",
    "4-2": "Transaction authorization code generated by the acquirer",
    "5-0": "`merchantReceipt`",
    "5-1": "string",
    "5-2": "Text of the receipt for the merchant. Must be in the URI",
    "6-2": "Text of the receipt for the client. Must be in the URI",
    "6-0": "`customerReceipt`",
    "6-1": "string",
    "7-0": "`responsecode`",
    "8-0": "`reason`",
    "9-0": "`success`",
    "9-1": "boolean",
    "8-1": "string",
    "7-1": "integer",
    "7-2": "`0` means \"success\"; values greater than `0` mean acquirer error codes, in which case the `reason` parameter will be an error message",
    "8-2": "On success, the value is empty; in case of error, it contains the error message",
    "9-2": "Generated by the app given the value of `responsecode`"
  },
  "cols": 3,
  "rows": 10
}
```

## Setting up inStore connector in VTEX Payments module

For the integration to work, the customer must set up the inStore connector on the **Payments** module (our payment backend). In this connector, the customer must choose in the field **Acquirer** which acquirer or app will receive the payment. This registration must contain all the information necessary for the acquirer to carry out the transaction. Example: Acquirer Id, Token, etc.).

AppLinking integration doesn't include other dependencies, since communication between the inStore application and the payment application happens with specific URIs containing all the configuration and payment parameters required for the action.

>⚠️ On Android, all communication must happen with a new <code>Intent</code>. This means that you should not send the response as a callback from the initial <code>Intent</code> call. Instead, send a new <code>Intent</code> to the inStore application with the previous response.

To configure the inStore connector, follow the steps below:

1. Access the **Payments** module.
2. Access **Settings**.
3. On the **Gateway Affiliations** tab, click the `+` button.
4. Click the **InStore** connector.
5. In the **Acquirer** field, select the acquirer which will receive the payment.
6. Fill in the other setting fields of the connector according to the information passed by the acquirer (Type of installment, Acquirer Id, Extra Configurations, etc).

## Learn more

- [App to simulate App Linking](https://github.com/vtex/vtex-payment-test/)
- [Sample App to Make a payment](https://github.com/vtex/payment-example-app)
