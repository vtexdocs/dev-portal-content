---
title: "Payments"
slug: "payments-overview"
hidden: false
createdAt: "2022-04-28T21:34:56.911Z"
updatedAt: "2022-09-29T21:05:13.444Z"
---
[block:html]
{
  "html": "<style>\n    .markdown-body .callout[theme=\"📣\"] {\n    --icon: \"\\f0a1\";\n    --icon-color: #142032;\n    --border: #142032;\n    --background: #f8f7fc;\n    --text: #4a596b;\n    }\n  </style>\n  <blockquote class=\"callout callout_loudspeaker\" theme=\"📣\">\n    <h3 class=\"callout-heading\"><span class=\"callout-icon\">📣</span>Help us improve our documentation! </h3>\n      <p>\n      Tell us about your experience with this article by filling out <button style=\"background-color:transparent;color:#f71963;text-decoration:underline;border:none;padding:0;cursor:pointer;font-size: var(--markdown-font-size,14px);\" onclick=\"closeModal()\">this form.</button>\n      </p>\n  </blockquote>"
}
[/block]

## Developing an antifraud integration

Antifraud solutions are used along with payment transactions to make them more secure by performing a risk analysis. VTEX allows antifraud systems to be integrated by providers through a protocol. The [Antifraud Provider Protocol](https://help.vtex.com/en/tutorial/antifraud-provider--4aZtmdpgFikcsQomWyqAOq) is a contract between VTEX and providers where VTEX defines a set of rules that have to be implemented by the providers in their integrations. The integrations have to include a set of endpoints defined in our [Antifraud Provider Protocol API](https://developers.vtex.com/vtex-rest-api/reference/antifraud-provider-protocol-overview).

## Developing a gift card integration

At VTEX, gift cards are treated as a payment option and their transactions are processed in the Checkout. Besides our native solution, VTEX allows external gift card providers to implement their integrations using our Gift Card Provider Protocol. Through this protocol, providers can develop a middleware containing the endpoints described in our [Gift Card Provider Protocol API](https://developers.vtex.com/vtex-rest-api/reference/giftcard-provider-protocol-overview) and connects with our [Gift Card Hub](https://developers.vtex.com/vtex-rest-api/reference/giftcard-hub-api-overview). You can check more details about Gift Cards in the articles below:

- [Gift Card introduction](https://developers.vtex.com/vtex-rest-api/docs/gift-card-integration-guide-system-architecture)
- [Gift Card system architecture](https://developers.vtex.com/vtex-rest-api/docs/gift-card-integration-guide-system-architecture)
- [Gift Card Provider Protocol API](https://developers.vtex.com/vtex-rest-api/reference/giftcard-provider-protocol-overview)

## Understanding VTEX’s Payments architecture

VTEX’s payment systems provide many resources to support all kinds of payment methods, conditions and integrations. This versatility also comes with complexity. If you are developing an integration or dealing with a more complex payment configuration, having a better understanding of our Payments architecture might help you. You can check details about it in these articles:

- [Payments introduction](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-guide)
- [Payment Methods](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-methods)
- [Purchase Flows](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-purchase-flows)

## Configuring specific payment methods or affiliations

The most common process to make payments available in your store is by configuring an [affiliation](https://help.vtex.com/tutorial/registering-gateway-affiliations--tutorials_444) (related to the provider you have a contract with) and a [method](https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions) in the Admin. Instructions for this process are found mostly in our [Help Center](https://help.vtex.com/subcategory/payment-settings--3tDGibM2tqMyqIyukqmmMw), but some configurations are more advanced and described in the articles below:

- [Setting up Merchant ID in Apple Pay](https://developers.vtex.com/vtex-rest-api/docs/setting-up-merchant-id-in-apple-pay)
- [Installing Affirm Payment App](https://developers.vtex.com/vtex-rest-api/docs/installing-affirm-payment-app-1)

## Configuring payments for specific use cases

When adding or editing a payment configuration in your store, you might need specific use cases such as defining a type of interest rate or processing payments through an external seller. Check the articles below for more information:

- [Setting up the type of interest rate](https://developers.vtex.com/vtex-rest-api/docs/setting-up-the-type-of-interest-rate)
- [External seller processing payments](https://developers.vtex.com/vtex-rest-api/docs/external-seller-processing-payments)

## Developing a payment integration

Payment providers can implement their integrations using our [Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol). This protocol enables providers to create a payment connector that interacts with our [Gateway](https://help.vtex.com/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk) and contains the endpoints described in our [Payment Provider Protocol API](https://developers.vtex.com/vtex-rest-api/reference/payment-provider-protocol-api-overview). Besides developing the connector, providers also need to test them and make sure they follow the required security standards before they can be available to the stores. You can check the details for those steps in the articles below:

- [Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol)
- [Payment Provider Protocol API](https://developers.vtex.com/vtex-rest-api/reference/payment-provider-protocol-api-overview)
- [Implementing a Payment Provider](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-implementing-a-payment-provider)
- [Payment Provider Homologation](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-homologation)
- [PCI - DSS Compliance](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance)
- [Secure Proxy](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy)
- [Payment Provider Framework](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-framework)
- [Payment Provider Protocol applied to payments with POS](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-ppp-applied-to-pos)

Below there are the steps you usually need to follow to implement an integration:

1. If your integration supports credit, debit or co-branded cards, before start developing, you have to assure that your payment connector follows one of these conditions:
    - The connector is hosted in a secure environment that follows the [PCI - DSS security standards](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance). An Attestation of Compliance (AOC) is required in this case.
    - The connector is developed by using [Secure Proxy](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy), where it receives tokens instead of sensitive data related to the card transaction, and the Gateway acts as a proxy to communicate with the acquirer.
2. Implement your payment connector according to our [Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol). This includes all the required [endpoints](https://developers.vtex.com/vtex-rest-api/reference/payment-provider-protocol-api-overview). All the payment methods supported by your integration will have to be listed in the response of the [List Payment Provider Manifest](https://developers.vtex.com/vtex-developer-docs/reference/manifest-1) endpoint. Also, for each payment method, you will have to implement a specific behavior for the [Create Payment](https://developers.vtex.com/vtex-developer-docs/reference/createpayment) endpoint.
3. Install your connector in a store and perform the [homologation step](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-homologation). Here you will test each endpoint of your connector using the [Payment Provider Test Suite app](https://apps.vtex.com/vtex-payment-provider-test-suite/p).
4. After your connector passes all the tests, [open a ticket](https://help.vtex.com/en/support) so our team can carry out the homologation process.

## Customizing your payment integration

When developing a payment integration, you might need to add specific features. You can enable specific payment methods that require additional work (i.e.: Pix), create a custom flow or add a validation step in the Checkout (Payment App), among other options. You can check our available options in the articles below:

- [Payment App](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-app)
- [Pix: Instant Payments in Brazil](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pix-instant-payments-in-brazil)
- [Split Payouts on Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/split-payouts-on-payment-provider-protocol)
- [Custom Auto Capture Feature](https://developers.vtex.com/vtex-rest-api/docs/custom-auto-capture-feature)
- [Cardholder document configuration](https://developers.vtex.com/vtex-rest-api/docs/cardholder-document-configuration)
- [Layout Development Guide for payment methods in Smart Checkout VTEX](https://developers.vtex.com/vtex-rest-api/docs/layout-development-guide-for-payment-methods-in-smart-checkout-vtex)

![Payment layout customization example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Getting%20Started/98a1ba7-2b693ad-layout_gif_85.gif)

![Payment App example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Getting%20Started/d9a2e11-c95f758-kX6y8QN55B_87.gif)
