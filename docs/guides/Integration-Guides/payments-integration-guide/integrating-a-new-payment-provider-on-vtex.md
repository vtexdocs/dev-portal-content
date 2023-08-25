---
title: "Integrating a new payment provider on VTEX"
slug: "integrating-a-new-payment-provider-on-vtex"
hidden: false
createdAt: "2023-08-25T00:00:15.623Z"
updatedAt: ""
---
This article is divided into steps that explain the integration flow for a new payment provider on VTEX. Before completing each stage and moving on, make sure to check and understand the information in the related links, as well as any prerequisites and settings that need to be in place in the current stage.

The integration flow of a new payment provider on VTEX has the following stages:

1. [Payment Provider Protocol - Overview](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#1-payment-provider-protocol---overview)
2. [Defining the operation environment](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#2-defining-the-operation-environment)
3. [Selecting the infrastructure type](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#3-selecting-the-infrastructure-type)
4. [Defining the purchase flow](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#4-defining-the-purchase-flow)
5. [Additional requirements and settings](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#5-additional-requirements-and-settings)
6. [Connector tests](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#6-connector-tests)
7. [Homologation and Go-live](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#7-homologation-and-go-live)

The following flowchart shows the possible journeys within the integration process.

<p align="center">
<img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/new-payment-provider-flow.gif"></img>
</p>

## 1. Payment Provider Protocol - Overview

Payment service providers (PSP), or simply payment providers, are companies that support electronic transactions with different payment methods, such as credit cards or digital wallets.

To operate in the VTEX environment, payment providers need to be integrated through the Payment Provider Protocol (PPP). This protocol defines the necessary prerequisites and settings that the payment methods available in your connector need to have in order to work in VTEX stores.

To understand how the Payment Provider Protocol works and the routes used in the payment and authentication flows, see:

- [Payment Provider Protocol - Overview](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m)
- [Payment Provider Protocol - API References](https://developers.vtex.com/docs/api-reference/payment-provider-protocol)

After making sure you meet the PPP implementation [prerequisites](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#implementation-prerequisites), the next step is defining how your connector will work in the VTEX environment.

## 2. Defining the operation environment

On VTEX, a payment connector can operate in three different environments: ecommerce websites, physical stores, or both. Select the option that matches the operating characteristics of your connector.

### Operating payments on the ecommerce website only

A payment connector can handle purchases for all virtual stores within the VTEX ecosystem, whether they be national or international.

> ℹ️ To process sales in countries other than your home country, check if your payment system meets the financial regulations of every country where you wish to operate. In addition, you need to sign a local or global partnership agreement with VTEX. Learn more in [Become a VTEX partner](https://vtex.com/us-en/partner/).

### Operating payments in the physical stores only

For payment operations in physical stores, VTEX offers the VTEX Sales App solution. This app enables sales associates to offer a complete and customized in-person experience for each customer, tracking the purchase process from selecting the product to delivering the order.

> ℹ️ Connectors developed for VTEX Sales App also use the Payment Provider Protocol (PPP).

To learn more about VTEX Sales App, see:

- [VTEX Sales App - Getting started and setting up](https://help.vtex.com/en/tracks/instore-primeiros-passos-e-configuracoes--zav76TFEZlAjnyBVL5tRc)
- [VTEX Sales App - Using the app](https://help.vtex.com/en/tracks/instore-usando-o-app--4BYzQIwyOHvnmnCYQgLzdr/6cq4E1JCmA6vCvBCCtAgIM)
- [VTEX Sales App - Payments](https://help.vtex.com/en/tracks/instore-pagamentos--43B4Nr7uZva5UdwWEt3PEy)
- [Payment Provider Protocol applied to payments with POS](https://developers.vtex.com/docs/guides/payments-integration-ppp-applied-to-pos)

### Operating payments in both physical stores and ecommerce website

If you want to offer a payment experience in physical stores and on the ecommerce website, you will need to configure settings for both cases.

To learn more about this type of operation, in addition to the documentation references linked in previous sections, see [Unified Commerce Strategies](https://help.vtex.com/en/tracks/estrategias-de-comercio-unificado--3WGDRRhc3vf1MJb9zGncnv/2LGAiUnHES1enjHsfi8fI3).

> ℹ️ You can develop a single connector configured to work in both environments (physical stores and ecommerce websites). You do not have to create a connector for each type of operation.

## 3. Selecting the infrastructure type

When implementing the payment connector on VTEX, you can use the internal infrastructure of your company or our low-code development platform, [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io).

### Developing with internal infrastructure

You can develop a connector using your internal infrastructure. In this case, you need to make sure that the architecture allows secure communication between you (payment provider) and the VTEX gateway.

To protect sensitive information, like credit card numbers, during transactions, you need to have the [PCI - DSS Compliance](https://www.pcisecuritystandards.org/document_library/?document=pci_dss) security certification or use Secure Proxy, the VTEX solution that replaces confidential information with encrypted tokens.

To learn more about how to develop the integration (middleware) and transfer sensitive payment information, see:

- [Implementing a Payment Provider - Middleware](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider)
- [PCI - DSS Compliance - Developer Portal](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance)
- [Secure proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy)

### Developing with VTEX infrastructure (VTEX IO)

If you want to develop your connector using VTEX infrastructure, you can use our [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io), our proprietary development platform. VTEX IO offers the following advantages:

- Greater integration agility by reusing VTEX templates and clients.
- [Serverless](https://www.redhat.com/en/topics/cloud-native-apps/what-is-serverless) environment with no need to invest additional financial resources related to infrastructure, reliability, and security management.
- Simplified authentication, authorization, and configuration resources that are integrated with all other VTEX systems.

If you use our infrastructure, you can also use our VTEX IO boilerplate, __Payment Provider Framework (PPF)__, which makes creating the connector faster in comparison to using your own infrastructure. With PPF, you don't have to manually configure the API routes, response and request body default formats, and sensitive information transfer (such as credit card information).

To learn more about development using VTEX IO and how the Payment Provider Framework works, see:

- [What is VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io)
- [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference)
- [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework)

## 4. Defining the purchase flow

A purchase flow represents the steps or actions that a customer takes to complete the payment of a purchase. On VTEX, the [available purchase flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows) are: transparent or custom (Payment App or Redirect). Select the option that matches the operating characteristics of your connector.

### Transparent

In the transparent purchase flow, the customer enters the payment information and places the order directly in the checkout of the VTEX store. This is the most widely used flow type because it allows completing all payment steps in the same environment, which improves the customer purchase experience.

To learn more about the transparent purchase flow, see [What is transparent checkout?](https://help.vtex.com/en/tutorial/what-is-transparent-checkout--2Y4ECegUmcYUggmck2GOwe).

### Custom

If you don't want to use the native VTEX purchase flow (transparent), you have two options to create custom payment experiences for your customer: Payment App and Redirect.

#### Payment App

Payment App is an app created in [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io), which enables a payment provider to create a custom payment experience without having to redirect the customer to an external page, unlike the redirect purchase flow.

If your connector is being developed using [VTEX infrastructure](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#developing-with-vtex-infrastructure-vtex-io), you can implement Payment App in two different ways:

1. [Create a specific app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-an-app) for Payment App.
2. Use the connector's app. In this case, you have to create a specific React folder for Payment App within the connector app.

> ⚠️ Connectors that only [operate payments in physical stores](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#operating-payments-in-the-physical-stores-only) are required to use Payment App as the default purchase flow.

To learn more, see [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app).

#### Redirect

In this flow, the customer selects the payment option in the VTEX store and is redirected to an external page to complete their payment information. After completing the fields and confirming the payment, the customer is redirected back to the order confirmation screen in the VTEX store.

> ℹ️ The redirect flow involves the most friction and the lowest purchase conversion rate, making it the least recommended flow.

To learn more about the redirect purchase flow, see [Purchase Flows - Redirect](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#redirect).

#### Layout modification (optional)

When you implement Payment App or Redirect in your connector, you can also create a non-interactive custom layout (using HTML and CSS) that will be displayed on VTEX Checkout.

To learn how to create a custom payment layout, see [Layout Development Guide for payment methods in Smart Checkout VTEX](https://developers.vtex.com/docs/guides/layout-development-guide-for-payment-methods-in-smart-checkout-vtex).

### Payment provider and VTEX interactions in the purchase flow

In addition to defining the best purchase flow, you need to know the operation and communication patterns between your connector and the VTEX payment gateway. To learn more, see:

- [Payment flow - Operations](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#operations-in-the-payment-flow)
- [Payment flow - Communication](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#communication-in-the-payment-flow)

### Configuration flow information

The [configuration flow](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider#configuration-flow) has three endpoints ([Create Authorization Token](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/authorization/token), [Provider Authentication](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/authorization/redirect), and [Get Credentials](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/authorization/credentials)), designed to improve merchant experience when enabling your connector on the VTEX Admin.

This flow enables the merchant to authenticate in your connector through the VTEX Admin using the `appKey`, `appToken`, and `applicationId` as credentials. Also, you can use this resource to provide other authentication methods for the merchant, such as login on your platform or even an initial registration.

> ℹ️ Implementing a configuration flow is optional. It can be done during middleware creation when you develop the connector using [your own infrastructure](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider#developing-with-internal-infrastructure) or with the [VTEX IO](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider#developing-with-vtex-infrastructure-vtex-io).

## 5. Additional requirements and settings

Depending on the payment method or features that your connector offers, you might need to meet specific requirements or configure additional settings.

- __Payment methods (ecommerce website)__

  - __Debit, credit, or co-branded cards__: Make sure that your connector has the [PCI - DSS Compliance](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance) certification. If you don't have or don't want to use that certification in your connector, you can implement [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy).
- __Payment methods (physical store)__

  - __Direct credit sale and direct debit sale__: Make sure that both these payment methods were configured as described in [Payment Provider Protocol applied to payments with POS](https://developers.vtex.com/docs/guides/payments-integration-ppp-applied-to-pos#payment-connector-pre-requisites).
- __Features__

  - __Split Payout__: This solution enables marketplaces to manage order amounts, and it divides your commission and the amount due to the seller. Learn more in:
    - [Split Payouts on Payment Provider Protocol](https://developers.vtex.com/docs/guides/split-payouts-on-payment-provider-protocol)
    - [Split Payment](https://help.vtex.com/en/tutorial/split-payment--6k5JidhYRUxileNolY2VLx)
  - __Custom Auto Capture__: This solution enables the merchant to set a window for automatic capture after the payment is completed. Learn more in Custom Auto Capture Feature.
  - __Inbound Request__: URL directly connected between the VTEX gateway and the payment provider. Learn more in 6. POST Inbound Request (BETA) in [Payment Flow](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider#payment-flow).

## 6. Connector Tests

After connector development is complete, you can use [Test Suite App](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation#install-the-test-suite-app) to test the following routes:

- [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments)
- [Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations)
- [Settle Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements)
- [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds)

Learn more about Test Suite App tests in [Testing details](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#4-testing).

You can also access your test store to [simulate payment of an order](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#placing-an-order-with-your-new-connector) before starting the connector homologation process on VTEX.

## 7. Homologation and Go-live

After completing all the above stages, ensuring that all the necessary requirements and settings are in place, and getting positive test results, you need to request connector homologation by opening a [ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM?locale=en) with VTEX support.

> ⚠️ The required SLA for homologation is 30 days, which may vary depending on any inconsistencies found in the connector development.

After the homologation process is completed, you will receive a confirmation message and your connector will be available for configuration to VTEX Admin merchants.

> ℹ️ If you want to increase the visibility of your connector in another channel, you can also publish your connector on the [VTEX App Store](https://apps.vtex.com/). Learn more in [Making your connector available to everyone](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#making-your-connector-available-to-everyone) and [Submitting your app to the VTEX App Store](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store).
