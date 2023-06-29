---
title: "Payments"
slug: "payments-overview"
hidden: false
createdAt: "2022-04-28t21:34:56.911Z"
updatedAt: "2022-09-29T21:05:13.444Z"
---

> **Help us improve our documentation!** Tell us about your experience with this article by completing [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

## Developing an antifraud integration

Antifraud solutions play a crucial role in ensuring secure payment transactions by performing risk analysis. VTEX offers integration capabilities for antifraud systems through the [Antifraud Provider Protocol](https://help.vtex.com/en/tutorial/antifraud-provider--4aZtmdpgFikcsQomWyqAOq). This protocol is an agreement between VTEX and providers, defining a set of rules that have to be implemented by the providers in their integrations. The integrations must include a set of endpoints defined in our [Antifraud Provider Protocol API](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#overview).

## Developing a gift card integration

On VTEX, gift cards are treated as a payment option, and their transactions are processed at Checkout. Besides our native solution, VTEX allows external gift card providers to implement integrations using our Gift Card Provider Protocol. Through this protocol, providers can develop a middleware containing the endpoints described in our [Gift Card Provider Protocol API](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#overview) and connects with our [Gift Card Hub](https://developers.vtex.com/docs/api-reference/giftcard-hub-api#overview). You can check more details about gift cards in the articles below:

- [Gift Card introduction](https://developers.vtex.com/docs/guides/gift-card-integration-guide)
- [Gift Card system architecture](https://developers.vtex.com/vtex-rest-api/docs/gift-card-integration-guide-system-architecture)
- [Gift Card Provider Protocol API](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#overview)

## Understanding VTEX Payments architecture

VTEX's payment systems offer extensive resources to support various payment methods, conditions, and integrations. This versatility also comes with complexity. If you are developing an integration or dealing with a more complex payment configuration, a better understanding of VTEX Payments architecture might help you. See more details in these articles:

- [Payments introduction](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-guide)
- [Payment Methods](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-methods)
- [Purchase Flows](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-purchase-flows)

## Configuring specific payment methods or affiliations

The most common process for enabling payments in your store is by configuring an [affiliation](https://help.vtex.com/tutorial/registering-gateway-affiliations--tutorials_444) related to the provider you have a contract with and a [payment method](https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions) in the Admin. Instructions for this process can be found primarily in our [Help Center](https://help.vtex.com/subcategory/payment-settings--3tDGibM2tqMyqIyukqmmMw). However, some configurations are more advanced and are described in the articles below:

- [Setting up Merchant ID in Apple Pay](https://developers.vtex.com/vtex-rest-api/docs/setting-up-merchant-id-in-apple-pay)
- [Installing Affirm Payment App](https://developers.vtex.com/vtex-rest-api/docs/installing-affirm-payment-app-1)

## Configuring payments for specific use cases

When adding or editing a payment configuration in your store, you might need specific use cases, such as defining a type of interest rate or processing payments through an external seller. Read the articles below for more information:

- [Setting up the type of interest rate](https://developers.vtex.com/vtex-rest-api/docs/setting-up-the-type-of-interest-rate)
- [External seller processing payments](https://developers.vtex.com/vtex-rest-api/docs/external-seller-processing-payments)

## Developing a payment integration

Payment providers can implement their integrations using our [Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol). This protocol enables providers to create a payment connector that interacts with our [Gateway](https://help.vtex.com/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk) and contains the endpoints described in our [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#overview). Besides developing the connector, providers must also test them and ensure they follow the required security standards before they can be available to the stores. Learn more in the articles below:

- [Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol)
- [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#overview)
- [Implementing a Payment Provider](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-implementing-a-payment-provider)
- [Payment Provider Homologation](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-homologation)
- [PCI - DSS Compliance](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance)
- [Secure Proxy](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy)
- [Payment Provider Framework](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-framework)
- [Payment Provider Protocol applied to payments with POS](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-ppp-applied-to-pos)

Here are the steps you usually need to follow to implement an integration:

1. If your integration supports credit, debit, or co-branded cards, it's essential to ensure that your payment connector meets one of the following conditions:
   - The connector is hosted in a secure environment that adheres to the [PCI - DSS security standards](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance). In this case, an Attestation of Compliance (AOC) is required.
   - The connector is developed using [Secure Proxy](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy), where it receives tokens instead of sensitive data related to the card transaction. The Gateway acts as a proxy to communicate with the acquirer.
2. Implement your payment connector based on our [Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol), which includes all the required [endpoints](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#overview). Make sure to list all the payment methods supported by your integration in the response of the [List Payment Provider Manifest](https://developers.vtex.com/vtex-developer-docs/reference/manifest-1) endpoint. Additionally, for each payment method, you need to implement specific behavior for the [Create Payment](https://developers.vtex.com/vtex-developer-docs/reference/createpayment) endpoint.
3. Install your connector in a store and proceed with the [homologation step](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-homologation). During this phase, you will test each endpoint of your connector using the [Payment Provider Test Suite app](https://apps.vtex.com/vtex-payment-provider-test-suite/p).
4. Once your connector successfully passes all the tests, [open a ticket](https://help.vtex.com/en/support), so our team can carry out the homologation process.

## Customizing your payment integration

When developing a payment integration, you might need to add specific features. You can enable specific payment methods that require additional work (i.e., Pix, an offline payment method in Brazil), create a custom flow or add a validation step in the Checkout (Payment App), among other options. See our available options in the articles below:

- [Payment app](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-app)
- [Pix: Instant Payments in Brazil](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pix-instant-payments-in-brazil)
- [Split Payouts on Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/split-payouts-on-payment-provider-protocol)
- [Custom Auto Capture Feature](https://developers.vtex.com/vtex-rest-api/docs/custom-auto-capture-feature)
- [Cardholder document configuration](https://developers.vtex.com/vtex-rest-api/docs/cardholder-document-configuration)
- [Layout Development Guide for payment methods in Smart Checkout VTEX](https://developers.vtex.com/vtex-rest-api/docs/layout-development-guide-for-payment-methods-in-smart-checkout-vtex)

![Payment layout customization example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-overview-0.gif)

![Payment app example](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/payments-overview-1.gif)
