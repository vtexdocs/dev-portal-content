---
title: "Payments"
slug: "payments-overview"
hidden: false
createdAt: "2022-04-28t21:34:56.911Z"
updatedAt: "2024-06-28T00:00:00.444Z"
---

> **Help us improve our documentation!** Tell us about your experience with this article by completing [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

## Understanding VTEX Payments architecture

VTEX's payment systems offer extensive resources to support various payment methods, conditions, and integrations. See below some articles that show a little more about the concepts and our payments architecture:

- [Payments introduction](https://developers.vtex.com/docs/guides/payments-integration-guide)
- [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol)
- [Payment Methods](https://developers.vtex.com/docs/guides/payments-integration-payment-methods)
- [Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows)


## Developing a payment integration at VTEX

Once you understand how payments are processed on VTEX, you can join our platform by developing integrations as a:

- [Payment provider](#payment-provider-integration)
- [Anti-fraud provider](#anti-fraud-provider-integration)
- [External gift card provider](#gift-card-integration)

### Payment provider integration

Payment providers can implement their integrations using our [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol). This protocol enables providers to create a payment connector that interacts with our [Gateway](https://help.vtex.com/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk) and contains the endpoints described in our [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#overview). Besides developing the connector, providers must also test them and ensure they follow the required security standards before they can be available to the stores. 

To learn all the steps necessary to develop and customize your payment integration on our platform, access the following articles:
- [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex)
- [Payments configuration guides](https://developers.vtex.com/docs/guides/payments-configuration-guides)

### Anti-fraud provider integration

Anti-fraud solutions are essential to ensure secure payment transactions by carrying out risk analyses. VTEX offers integration capabilities for anti-fraud systems through the [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud- companies -works). This protocol is an agreement between VTEX and providers, defining a set of rules that must be implemented during the development of integrations. Each integration must include a set of endpoints defined in our [Anti-fraud Provider Protocol API](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#overview).


### External gift card provider integration

On VTEX, gift cards are treated as a payment method, and their transactions are processed at Checkout. In addition to [our native solution](https://developers.vtex.com/docs/api-reference/giftcard-api), VTEX allows external gift card providers to implement integrations using our Giftcard Provider Protocol. Through this protocol, providers can develop a middleware containing the endpoints described in our [Giftcard Provider Protocol API]([https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#overview](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol)) and connect with our [Giftcard Hub](https://developers.vtex.com/docs/api-reference/giftcard-hub-api#overview). You can check more details about gift cards in the articles below:

- [Gift card introduction](https://developers.vtex.com/docs/guides/gift-card-integration-guide)
- [Gift card system architecture](https://developers.vtex.com/docs/guides/gift-card-integration-guide-system-architecture)
- [Managing VTEX gift cards](https://developers.vtex.com/docs/guides/managing-vtex-gift-cards)
