---
slug: "new-referencevalue-parameter-create-payment-endpoint"
title: "New referenceValue parameter in the Create Payment endpoint request body"
createdAt: 2023-10-24T00:00:00.000Z
hidden: false
type: "added"
excerpt: "New parameter available in the Create Payment endpoint request body."
---
The `referenceValue` parameter was added to the [Create Payment endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) request body. This new field is mandatory and must be sent on the endpoint to represent the payment amount without interest applied.

The values ​​of the `value` and `referenceValue` fields will be equal whenever the value of the `installmentsInterestRate` field is equal to zero.

See the examples below:

Example 1: Order value is 15.00 (interest free).

```json
...
"value": "15.00",
"referenceValue": "15.00",
"installments": 1,
"installmentsInterestRate": "0.00"
...
```

Example 2: Order value is 15.00 (with interest of 1.00 per month, 3 installments).

```json
...
"value": "15.00",
"referenceValue": "12.00",
"installments": 3,
"installmentsInterestRate": "1.00"
...
```
