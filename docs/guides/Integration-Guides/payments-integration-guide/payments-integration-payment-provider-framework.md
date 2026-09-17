---
title: "Payment Provider Framework"
slug: "payments-integration-payment-provider-framework"
hidden: false
createdAt: "2022-05-19T16:21:58.633Z"
updatedAt: "2026-08-24T00:00:00.000Z"
excerpt: "Learn how the Payment Provider Framework (PPF) allows you to develop payment connectors on VTEX IO using a boilerplate app that handles API routes, request/response types, Secure Proxy, and hosting."
---
Payment Provider Framework (PPF) is an alternative way to develop payment connectors through VTEX IO. Because development starts from a VTEX IO app boilerplate, the framework already provides the [API routes](https://developers.vtex.com/docs/api-reference/payment-provider-protocol), the types used in the request and response bodies, and the [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy). PPF connectors run on the VTEX IO infrastructure, so you don't need to host the connector yourself.

> ⚠️ Before developing a payment connector, you must meet the prerequisites defined by VTEX. For more information, see [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) and [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex).

## Getting started

### Cloning the base repository

If you're starting a new project, clone the [example repository](https://github.com/vtex-apps/payment-provider-example), which already includes the basic configuration.

### Updating your project

After you have the repository code in your workspace, check that all the necessary dependencies are installed and up to date:

1. Run the following command on your node folder:

    ```sh
      yarn add @vtex/payment-provider
    ```

2. In your `package.json`, confirm that the package was added as a dependency with the correct version:

    ```json
      "@vtex/payment-provider": "1.x"
    ```

3. Check in the `package.json` the version of `@vtex/api`, which should be listed in the devDependencies as follows:

    ```json
      "@vtex/api": "6.x"
    ```

4. When linking your app, this version might be updated to a version later than 6.x, which is fine. In case it's not listed as a `devDependency`, run the following command on your node folder:

    ```sh
      yarn add -D @vtex/api
    ```

    > ℹ️ If you get any type errors or conflicts in your project related to `@vtex/api`, follow these steps: 1. Delete the `node_modules` folder and the `yarn.lock` file from both your project root and your project's node folder. 2. Run the command `yarn install -f` in both folders.

5. In your `manifest.json`, check the builders section and include `paymentProvider` in its current version. This adds policies to call back the Payment Gateway APIs and exposes the Payment Provider Protocol routes.

    ```json
    "builders": {
      "node": "7.x",
      "paymentProvider": "1.x"
    }
    ```

## Next steps

To create your service, implement your [payment provider connector](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#payment-provider) and the [service](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#payment-provider-service) itself, as described in the sections below.

## Payment Provider

This is an abstract class with the signatures of the route functions required by your connector, based on the [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol).

Create a new class that extends Payment Provider and implements a function for each route. Each function receives the request body (when there is one) as a parameter and must return the response as an object, as in the following example:

```ts
import {
 PaymentProvider,
 // ...
} from '@vtex/payment-provider'

class YourPaymentConnector extends PaymentProvider {

 // ... implementation of the other route functions
}
```

> ℹ️ TypeScript automatically checks for typing errors. You can also review the request and response signatures of the Payment Flow endpoints in the [Payment Provider Protocol API reference](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest).

### Payment Provider builder

To specify which payment methods the connector processes, follow these steps:

1. Create a folder named `paymentProvider` using the following folder structure.

    ```
    📂 node
    📂 paymentProvider
    📄 manifest.json
    ```

2. Create a file named `configuration.json` inside the `paymentProvider` folder.

    ```
    📂 node
    📂 paymentProvider
    ┗ 📄configuration.json
    📄 manifest.json
    ```

3. Declare the payment methods accepted by your payment provider. This allows them to be automatically implemented by the builder, without the need to declare them in the `/manifest` route.

    > ⚠️ Before adding values to `paymentMethods` in your connector manifest, check the names already documented in the [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol?endpoint=get-/manifest) endpoint. If a payment method already exists, use the same name (same spelling and capitalization). Create a new name only when the payment method is new.

    ```json
    {
      "name": "MyConnector",
      "paymentMethods": [
        {
          "name": "Visa",
          "allowsSplit": "onCapture"
        },
        {
          "name": "American Express",
          "allowsSplit": "onCapture"
        },
        {
          "name": "Diners",
          "allowsSplit": "onCapture"
        },
        {
          "name": "Elo",
          "allowsSplit": "onCapture"
        },
        {
          "name": "Hipercard",
          "allowsSplit": "onCapture"
        },
        {
          "name": "Mastercard",
          "allowsSplit": "onCapture"
        },
        {
          "name": "BankInvoice",
          "allowsSplit": "onAuthorize"
        }
      ]
    }
    ```

    > ⚠️ Replace the `name` field value with the name of your provider. Don't keep the `"MyConnector"` placeholder.

> ℹ️ To check which payment methods are currently available in the VTEX Admin, go to **Store Settings > Payment > Settings**, or type **Settings** in the search bar at the top of the page, then click the green `+` button. To support a payment method that isn't available, [open a ticket with VTEX Support](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) describing the new payment method.

You can also declare the `customFields` array to allow your payment provider to send specific information. The `type` field can be configured as follows: `text` for non-confidential data; `password` for sensitive and security information (except `appKey` and `appToken`, which must not be sent in this field); and `select` to group a set of custom information.

```json
{
  "name": "MyConnector",
  "paymentMethods": [
    ...
  ],
  "customFields": [
    {
      "name": "Company account",
      "type": "text"
    },
    {
      "name": "POS URL",
      "type": "text"
    },
    {
      "name": "Client key",
      "type": "password"
    },
    {
      "name": "Auto Capture Settings",
      "type": "select",
      "options": [
        {
          "text": "Automatic Capture Immediately After Payment Authorization",
          "value": "Immediately"
        },
        {
          "text": "Auto Settle Delay: 7 Days",
          "value": "Deactivated"
        }
      ]
    }
  ]
}
```

### Overriding the manifest route

To override the default `/manifest` route because of a specific feature of your provider, [open a ticket with VTEX Support](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) describing your use case, and add the parameters shown below.

```json
{
  "memory": 256,
  "ttl": 10,
  "timeout": 10,
  "minReplicas": 2,
  "maxReplicas": 3,
  "routes": {
    "manifest": {
      "path": "/_v/api/my-connector/manifest",
      "handler": "vtex.payment-gateway@1.x/providerManifest",
      "headers": {
        "x-provider-app": "$appVendor.$appName@$appVersion"
      },
      "public": true
    }
  }
}
```

> ⚠️ Update the `x-provider-app` parameter whenever there is a significant change, for example, `vtex.payment-provider-example@1.2.3`. You can omit the `handler` and `headers` parameters, but then you must implement them yourself.

The `memory`, `ttl`, `timeout`, `minReplicas`, and `maxReplicas` fields are VTEX IO runtime parameters, not payment-specific settings. Two of them affect how quickly your connector answers the Payment Gateway:

- `ttl`: How long, in minutes, the platform keeps an instance running without receiving new requests. The default is 10 minutes, and the maximum is 60. After this period, the platform shuts down the instance, and the next request starts a new one.
- `timeout`: How many seconds the platform waits before aborting an incoming request. The default is 10 seconds. This value applies only to requests the platform sends to your connector, not to the calls your connector makes to the provider.

For the full list of parameters and their limits, see [service.json](https://developers.vtex.com/docs/guides/vtex-io-documentation-service).

### Available configurable options

In addition to the manifest fields (`paymentMethods` and `customFields`), the following configuration options are available:

| Parameter name | Required | Default | Description |
| - | - | - | - |
| `name` | Yes | | Payment provider connector name. |
| `serviceUrl` | Yes | Auto-generated for IO connectors. | A valid URL (can include relative paths). |
| `implementsOAuth` | No | `false` | Defines whether the provider implements the configuration flow with OAuth authentication support. |
| `implementsSplit` | No | `false` | Defines whether the provider implements the payment split flow. |
| `usesProviderHeadersName` | No | `true` | Defines whether the provider receives the appKey and appToken headers as `"x-provider-api-appKey"` and `"x-provider-api-appToken"` respectively. |
| `useAntifraud` | No | `false` | Defines whether anti-fraud providers can be used in the payment provider's transactions. |
| `usesBankInvoiceEnglishName` | No | `false` | Defines whether the Bank Invoice payment method uses the English name (`true`) or the Brazilian name, Boleto Bancário (`false`). |
| `usesSecureProxy` | No | `true` | If `true`, the provider can process payments without being [PCI-certified](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance). The connector receives a `secureProxyUrl` in the `createPayment` flow, along with the encrypted card data. If `false`, the provider must be PCI-certified, and you must send the AOC containing the provided `serviceUrl`. |
| `requiresDocument` | No | `false` | If `true`, the customer must include the cardholder document on Checkout. A new field appears on the Checkout form. If `false`, the customer doesn't need to include a cardholder document. |
| `acceptSplitPartialRefund` | No | `false` | If `true`, VTEX sends a partial refund when a payment split occurs. If `false`, the connector can't process a partial refund when a payment split occurs. |
| `usesAutoSettleOptions` | No | `false` | If `true`, the merchant can configure the auto-settlement behavior in the provider settings in the VTEX Admin. The available options are as follows: "Use behavior recommended by the payment processor", "Automatic capture immediately after payment authorization", "Automatic capture immediately after anti-fraud analysis", "Scheduled: schedules the automatic capture" and "Deactivated: not automatically captured". If `false`, the connector doesn't display this dropdown for auto settlement. For more information, see [Custom Auto Capture Feature](https://developers.vtex.com/docs/guides/custom-auto-capture-feature). |

### Request a retry from Payment Gateway

Your connector must support retries, as defined by the [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol). To request a retry, invoke the following function:

```ts
this.retry(request)
```

> ℹ️ For more information about the retry flow, see [Authorization](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#authorization) in the Purchase Flows guide.

### Payment Provider Service

This is a class that extends the Service from `@vtex/api`. Invoke it by passing the developed connector as a property of the first parameter. It automatically sets up the required routes.

The following code shows how to do this and find it in the `node/index.ts` file.

```ts
import {
 PaymentProviderService,
} from '@vtex/payment-provider'

new PaymentProviderService({
 connector: YourPaymentConnector,
})
```

By default, the Payment Provider Service declares the following routes:

- `/manifest`
- `/payments`
- `/settlements`
- `/refunds`
- `/cancellations`
- `/inbound`

If your service requires any extra routes, you must declare them separately and use them as parameters:

```ts
new PaymentProviderService({
 routes: newRoutes,
 connector: YourPaymentConnector,
})
```

If your connector requires any extra clients, you must also pass them in the parameters along with the connector:

```ts
new PaymentProviderService({
 clients: NewClients,
 connector: YourPaymentConnector,
})
```

### Using Secure Proxy

To process credit, debit, or co-branded card transactions, integrations must comply with [PCI DSS security standards](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance). Integrations hosted on VTEX IO that support these payment methods must use Secure Proxy to call a PCI-certified endpoint. You can check more details in the [Secure Proxy article](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy).

> ⚠️ VTEX Secure Proxy must allow the endpoint. To request this, [open a ticket with VTEX Support](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) and attach the AOC with the endpoint. Secure Proxy supports only two content types: `application/json` and `application/x-www-form-urlencoded`.

To make calls over Secure Proxy, follow these steps:

1. Extend the `SecureExternalClient` abstract class. The constructor declares the PCI-certified destination, for example, `'http://my-pci-certified-domain.com'`. VTEX adds this destination to the trusted list after receiving its AOC.
2. Set the Secure Proxy URL on the request you want to proxy. The connector receives `secureProxyUrl` in the `createPayment` flow.

> ℹ️ Declare the destination with the `http://` scheme, as shown in the example below. VTEX IO routes outbound requests over HTTP internally and applies TLS when the request leaves the VTEX infrastructure, so Secure Proxy calls still reach the provider over HTTPS. For outbound calls that do not go through Secure Proxy, such as the cancellation, settlement, and refund operations, keep the `http://` scheme and set the `x-vtex-use-https` header to `true`. For more information, see [How to create and use Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients).

```ts
import { SecureExternalClient, CardAuthorization } from '@vtex/payment-provider'
import type {
  InstanceOptions,
  IOContext,
  RequestConfig,
} from '@vtex/api'

export class MyPCICertifiedClient extends SecureExternalClient {
  constructor(protected context: IOContext, options?: InstanceOptions) {
    super('http://my-pci-certified-domain.com', context, options)
  }

  public myPCIEndpoint = (cardRequest: CardAuthorization) => {
    return this.http.post(
      'my-pci-endpoint',
      {
        holder: cardRequest.holderToken,
        number: cardRequest.numberToken,
        expiration: cardRequest.expiration,
        csc: cardRequest.cscToken,
      },
      {
        headers: {
          Authorization: 'my-pci-endpoint-authorization',
        },
        secureProxy: cardRequest.secureProxyUrl,
      } as RequestConfig
    )
  }
}
```

## Placing an order with your new connector

After your connector is ready, you can test it in the production flow using your store's Checkout.

> ℹ️ Beta versions always use a `ttl` of 10 minutes, regardless of the value declared in `service.json`. Only the most recent stable version of the app honors a custom `ttl`. While testing, expect the first request after an idle period to take longer because the platform must start a new instance.

Before starting, confirm that your store has products available for sale. To place an order with your new connector, follow these steps:

1. Launch a beta version of your connector, for example, `vtex.payment-provider-test@0.1.0-beta`. For more information, see the [Making your app publicly available article](https://developers.vtex.com/docs/guides/vtex-io-documentation-10-making-your-app-publicly-available#launching-a-new-version) to learn how to create a beta version of your app.
2. Install the beta version on the `master` workspace and wait about one hour.
3. Go to `https://{account}.myvtex.com/admin/affiliations/connector/Vtex.PaymentGateway.Connectors.PaymentProvider.PaymentProviderConnector_{connector-name}/`. Replace `{account}` with the name of the account you want to test on, and `{connector-name}` with the name of your connector. The format of the name is `${vendor}-${appName}-${appMajor}`, for example, `vtex-payment-provider-example-v1`.

   ![Payment affiliation configuration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration-Guides/payments-integration-guide/payments-integration-payment-provider-framework-0_370.png)

4. In **Payment Control**, activate the test environment by clicking **Enable test mode**. A new **Workspace** field appears.
5. Set the **Workspace** field. You can leave it as `master` if that is the workspace you want to test on.

   ![Payment affiliation configuration test](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration-Guides/payments-integration-guide/payments-integration-payment-provider-framework-1_375.png)

6. Configure a [payment condition](https://help.vtex.com/en/docs/tutorials/how-to-configure-payment-conditions) with your new connector, then wait 10 minutes for it to appear on Checkout.
7. Make a purchase with the payment condition you configured with your connector.
8. After completing all transaction testing in the beta version of the connector, [release and deploy](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available#step-6---deploying-the-app-stable-version) a stable version of your connector, for example, `vtex.payment-provider-test@0.1.0`. Submit this stable version to the [homologation process](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#7-homologation-and-go-live).

## Making your connector available to process sales

> ⚠️ To process sales with your connector on all VTEX accounts, send the `billingOptions` field as `free` in the manifest. If you want to restrict the use of the connector to only a few specific accounts, send the `billingOptions` field as `free` as well, and [open a support ticket](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) asking the payments team to enable the connector only for those accounts. For more information about this field, see [Billing Options](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options).

Publication happens through the [VTEX App Store](https://apps.vtex.com/). For more information, see [Submitting your app to the VTEX App Store](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store).

After that, [open a ticket with VTEX Support](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) stating that the integration is complete. Include the following information, which is specific to PPF connectors:

- **Connector app name**: The name of the PPF connector app, in the `vendor.appname` format, for example, `partnername.connector-partnername`. You can find it in the `manifest.json` file.
- **Allowed accounts**: Which VTEX accounts can use this connector, either all accounts or specific accounts.
- **New payment method**: Specify whether the connector supports a payment method that is not yet available in the VTEX Admin. If it does, specify whether the method works with Redirect or the Payment App. For more information, see [Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows).

For the complete list of information required in the ticket, see [Payment Provider Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation).

The payment team completes the homologation within 30 days.

After homologation, install the app in the account that will use it. A new affiliation then becomes available for configuration.

## Updating and testing new configurations for an already published connector

To change and test new settings in a published connector, follow these steps:

1. Apply the new settings to the last created beta version of your connector.
2. Follow the same procedures described in the [Placing an order with your new connector](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#placing-an-order-with-your-new-connector) section to verify that the beta version of your connector is working correctly after applying the new settings.
3. Create and submit a new stable version of your connector (containing the same modifications as the beta version) to the homologation process, for example, `vtex.payment-provider-test@0.1.1`.
4. Publish it as indicated in the [Making your connector available to process sales](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#making-your-connector-available-to-process-sales) section.
