---
slug: "replace-capture-term-for-settlement-in-the-payment-provider-protocol"
title: "Replace \"Capture\" term for \"Settlement\" in the Payment Provider Protocol documentation"
createdAt: 2022-03-30T20:57:28.149Z
hidden: false
type: "improved"
---

![Payments](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/replace-capture-term-for-settlement-in-the-payment-provider-protocol-0.png)

The "Capture" term was replaced by "Settlement" in our Payment Provider Protocol (PPP), including similar forms (e.g.: "to capture" was replaced by "to settle"). This change in nomenclature is applied throughout our documentation, including in our API reference. The **Capture Payment** endpoint is now called **Settle Payment**. You can check the changes in our [API Reference](https://developers.vtex.com/vtex-rest-api/reference/payment-provider-protocol-api-overview) and in the [Payment Provider Protocol article](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m).

No changes were made to how the API works, including its parameters. The [Settle Payment endpoint](https://developers.vtex.com/vtex-rest-api/reference/settlepayment) still uses the same path `/settlements`.

There were also some improvements in the PPP API documentation:

- Improved examples of successful responses for Settle Payment and Refund Payment endpoints.
- Changed the default value of some parameters (`value`, `verificationOnly` and `installments` in the request body of Create Payment).
- Changed the type of `document` parameter in `recipients` of the request body of Settle Payment and Refund Payment endpoints from `number` to `string`. The `number` type was incorrectly documented.
- Improved schema of the response body in the List Payment Provider Manifest endpoint.
