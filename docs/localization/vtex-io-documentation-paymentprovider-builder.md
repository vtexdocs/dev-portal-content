---
title: PaymentProvider builder"
slug: "vtex-io-documentation-paymentprovider-builder"
hidden: false
createdAt: "2024-07-11T11:00:00.000Z"
updatedAt: ""
excerpt: "Learn how to use the VTEX IO PaymentProvider builder."
---

The `paymentProvider` builder configures the payment methods of a payment connector built using the Payment Provider Framework (PPF).

Payment connectors are developed at VTEX following the [Payment Provider Protocol (PPP)](https://help.vtex.com/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m), a set of rules and endpoints that define the connector behavior and publishing process. They connect the VTEX Payment Gateway with financial institutions (issuing banks, card networks, etc.) to process payment data. Payment connectors can be developed to support multiple payment methods (credit cards, digital wallets, promissory, etc.) and conditions (split payment, installments, etc.).

Developing a payment connector with PPF accelerates the process using an IO app boilerplate since all the payment routes and functions available in the PPP are declared in the code. See the [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework) article for more details about the connector implementation.

## Folder structure

The `paymentProvider` builder uses a folder named `paymentProvider` located in the app’s root folder. This folder contains a single file: `configuration.json`.

```txt
paymentProvider
 ┗ 📄 configuration.json
```

- `configuration.json`: Defines the payment methods of the connector and the response of the /manifest route of the connector, so it is unnecessary to include the response body of this route in the code.

## Usage

To develop an app using the `paymentProvider` builder, refer to the following steps:

1. **Start with a template**: Download the [`payment-provider-example` template](https://github.com/vtex-apps/payment-provider-example) or create a new project using the [`vtex init` CLI command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#starting-a-new-project) and choose the `payment-provider-example` option. This template provides a payment connector being developed with the [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework).
2. **Configure the manifest**: Edit the `configuration.json` file to define the payment methods of the connector and the supported [split options](https://help.vtex.com/en/tutorial/split-payment--6k5JidhYRUxileNolY2VLx). This will define the response body of the `/manifest` route of the connector. There are also [configurable options](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#available-configurable-options) such as using antifraud and Secure Proxy.
3. **Implement the app's logic**: Edit the TypeScript files inside the `node` folder to define the behavior of each payment route of the connector. See the [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework) guide for more details.
4. **Testing**: [Link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to a development workspace for testing. To test the payment routes with the connector, install the [Payment Provider Test Suite app](https://apps.vtex.com/vtex-payment-provider-test-suite/p) in your workspace and follow the steps in the [Payment Provider Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) guide.
