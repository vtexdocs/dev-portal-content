---
slug: "new-parameters-for-installments-in-payment-provider-protocol"
title: "New parameters for installments in Payment Provider Protocol"
createdAt: 2020-10-13T19:38:21.814Z
hidden: false
type: "added"
---

![Commerce APIs](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/new-parameters-for-installments-in-payment-provider-protocol-0.png)

Our [Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#overview) was extended to make it easier to include payments in installments in your provider implementation.

The POST [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint now has two new parameters:

- `installmentsValue`
- `installmentsInterestRate`

These parameters allow the provider to establish a value for each installment and an interest rate for it, respectively, when creating a new payment method.
