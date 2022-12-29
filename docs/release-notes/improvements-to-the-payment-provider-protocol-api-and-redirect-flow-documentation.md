---
title: "Improvements to the Payment Provider Protocol API and Redirect flow documentation"
slug: "improvements-to-the-payment-provider-protocol-api-and-redirect-flow-documentation"
type: "improved"
createdAt: "2022-06-02T20:57:52.908Z"
hidden: false
excerpt: "The [Payment Provider Protocol (PPP) API documentation](https://developers.vtex.com/vtex-rest-api/reference/payment-provider-protocol-api-overview) and the [Redirect section of the Purchase Flows article](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-purchase-flows#redirect) have just been updated."
---

![Payments](https://img.shields.io/badge/-Payments-blueviolet)

The [Payment Provider Protocol (PPP) API documentation](https://developers.vtex.com/vtex-rest-api/reference/payment-provider-protocol-api-overview) and the [Redirect section of the Purchase Flows article](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-purchase-flows#redirect) have just been updated. The changes in the PPP API documentation are:

- [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) endpoint.
  - Removed requirement of `installmentsInterestRate`, `installmentsValue` and `ipAddress` parameters in the request body.
  - Added description of `card` parameter in the request body.
  - `document` field is now properly located inside the `card` parameter in the request body. Before, it was incorrectly located inside `card.expiration`.
  - Added description of `isCorporate`, `corporateName`, `tradeName` and `corporateDocument` fields of the `miniCard.buyer` parameter in the request body.
  - Removed requirement of `complement` field of the `miniCart.shippingAddress` and `miniCart.billingAddress` parameters in the request body.
  - Removed requirement of `categoryId` and `sellerId` fields of the `miniCard.items` parameter in the request body.
  - Corrected type of `miniCart.merchantSettings` parameter in the request body from object to array of objects and added description.
  - Added response examples for Redirect and Callback cases.
  - Added examples for multiple request body fields.
- [GET List Payment Provider Manifest](https://developers.vtex.com/vtex-rest-api/reference/manifest-1) endpoint.
  - Improved description of `paymentMethods[].allowsSplit` field in the response body to include reference to the [Split Payouts on the Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/split-payouts-on-payment-provider-protocol) article.
  - Improved description of `autoSettleDelay` parameter in the response body to include reference to the [Custom Auto Capture Feature](https://developers.vtex.com/vtex-rest-api/docs/custom-auto-capture-feature) article and added requirement of `minimum` and `maximum` fields.
- [POST Settle Payment](https://developers.vtex.com/vtex-rest-api/reference/settlepayment), [POST Cancel Payment](https://developers.vtex.com/vtex-rest-api/reference/cancelpayment), [POST Refund Payment](https://developers.vtex.com/vtex-rest-api/reference/refundpayment) and [POST Inbound Request](https://developers.vtex.com/vtex-rest-api/reference/inboundrequestbeta) endpoints.
  - Added `merchantSettings` parameter in the request body with all the parameters.

Also, we improved the [Redirect section of the Purchase Flows article](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-purchase-flows#redirect) by adding an image with a sequence diagram and a detailed explanation of the steps that occur when the Redirect flow is used for payments.