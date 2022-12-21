---
title: "Payment Provider Framework: Develop payment connectors with VTEX IO"
slug: "payment-provider-framework-develop-payment-connectors-with-vtex-io"
type: "added"
createdAt: "2022-07-18T13:14:43.462Z"
hidden: false
---

![Payments](https://img.shields.io/badge/-Payments-blueviolet)

We have just made publicly available the Payment Provider Framework (PPF), which is an alternative way to develop payment connectors through VTEX IO. This feature is in the beta stage.

## What changed?

Before PPF, the only way partners could develop connectors for payment integrations was by implementing our [Payment Provider Protocol (PPP)](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol) in their infrastructure. Partners would have to implement their solution with all the required endpoints and deal with hosting the connector.

With PPF, since the development is based on an IO app boilerplate, a lot of the work is already done to accelerate the implementation of your integration. Also, developers do not need to worry about hosting the connector since it is hosted on the IO infrastructure.

## What needs to be done?

To start developing your connector with PPF, you can clone the [example repository](https://github.com/vtex-apps/payment-provider-example) and work with it to make your solution. You can check all the details in our [Payment Provider Framework](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-framework) article.
