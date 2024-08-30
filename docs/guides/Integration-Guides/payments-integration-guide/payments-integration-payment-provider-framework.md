---
title: "Payment Provider Framework"
slug: "payments-integration-payment-provider-framework"
hidden: false
createdAt: "2022-05-19T16:21:58.633Z"
updatedAt: "2022-05-19T17:46:05.176Z"
---
Payment Provider Framework (PPF) is an alternative way to develop payment connectors for your integration through VTEX IO. Since the development is based on a boilerplate of an IO app, a lot of the work is already done to implement the needed feature including the [API routes](https://developers.vtex.com/docs/guides/payment-provider-protocol-api-overview), the types used in the request and response bodies, and the [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy). With PPF, developers also do not need to worry about hosting the connector since it is hosted on the IO infrastructure.

> ⚠️ To develop a new payment connector, it is mandatory to follow the **prerequisites determined by VTEX**. You can learn about them in the [Implementation prerequisites section of our Payment Provider Protocol article](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#implementation-prerequisites). For more information on how payment providers can be integrated into VTEX, visit [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex).

## Getting started

### Cloning base repository

If you are starting a brand new project, we recommend you to clone the [example repository](https://github.com/vtex-apps/payment-provider-example), as it already has all the basic configuration setup.

### Updating your project

Once you have the repository code in your workspace, you have to make sure you have all the necessary dependencies and that they are updated. To do so, follow these steps:

1. Run the following command on your node folder:

```sh
  yarn add @vtex/payment-provider
```

2. Go to your `package.json` and make sure it has been added as a dependency with the correct version:

```sh
  "@vtex/payment-provider": "1.x"
```

3. Check in the `package.json` the version of `@vtex/api`, which should be listed in the devDependencies as follows:

```sh
  "@vtex/api": "6.x"
```

4. When linking your app, this version might get updated to a later than 6.x version, which is fine. In case it is not listed as a `devDependency`, run the following command on your node folder:

```shell
  yarn add -D @vtex/api
```

> ℹ️ If you get any type errors or conflicts in your project related to `@vtex/api`, follow these steps: 1. Delete the `node_modules` folder and the `yarn.lock` file from both your project root and your project's node folder. 2. Run the command `yarn install -f` in both folders.

5. In your `manifest.json`, you should check the builders section, in which you must include the `paymentProvider` in its current version. This will add policies to callback the Payment Gateway APIs and also expose Payment Provider protocol routes.

```json
"builders": {
  "node": "6.x",
  "paymentProvider": "1.x"
}
```

## Next steps

In order to create your service, you must implement your [payment provider connector](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#payment-provider) and the [service](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#payment-provider-service) itself, as described in the sections below.

## Payment Provider

This is an abstract class with the signatures of the route functions required in your connector, according to the [protocol](https://help.vtex.com/en/tutorial/payment-provider-protocol).

You must create a new class extending the Payment Provider, which must implement a function for each route. The functions will receive the request body (when there is one) as a parameter and the response must be returned as an object, such as the example shown below:

```js
import {
 PaymentProvider,
 // ...
} from '@vtex/payment-provider'

class YourPaymentConnector extends PaymentProvider {

 // ... implementation of the other routes functions
}
```

> ℹ️ Typescript should automatically check for typing errors, but if you need, you can check the requests and responses signatures from the [Payment Flow endpoints in our API Reference](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest).

### Payment Provider builder

To specify which payment methods the connector will accept to process, follow the steps below:

1. Create a folder named `paymentProvider` using the following folder structure.

```
node
paymentProvider
manifest.json
```

2. Create a file named `configuration.json` inside the `paymentProvider` folder.

```
node
paymentProvider
   |--configuration.json
manifest.json
```

3. Declare the payment methods accepted by your payment provider. This action allows them to be implemented automatically by the builder, without the need to declare them in the `/manifest` route.

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

> ⚠️ The `name` field indicating the name of the connector must be replaced with the name of your provider. This field cannot be filled with a value `"MyConnector"`.

> ℹ️ To check which payment methods are currently available in the VTEX Admin, go to Store **Settings > Payment > Settings**, or type **Settings** in the search bar at the top of the page and click the green `+` button. If you want to support a new payment method that is not available, you need to [open a ticket to the VTEX team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) informing them of this new payment method.

### Overriding the Manifest route

If you wish to override the default `/manifest` route due to some specific feature of your provider, please [open a ticket to the VTEX support team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) describing your use case and add special parameters as specified below.

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
          "x-provider-app": "$appVendor.$appName@$appVersion",
        },
        "public": true
      }
  }
}
```

> ⚠️ The `x-provider-app` parameter must be updated whenever there is an important change (e.g. vtex.payment-provider-example@1.2.3). You can also omit the `handler` and `headers` parameters, however, when performing this procedure you will need to implement them yourself.

### Available Configurable Options

In addition to the manifest fields (`paymentMethods` and `customFields`), the following configuration options are available:

| Parameter name | Required | Default | Description |
| - | - | - | - |
| `name` | Yes | | Payment provider connector name. |
| `serviceUrl` | Yes | Auto-generated for IO connectors. | A valid URL (can include relative paths). |
| `implementsOAuth` | No | `false` | Defines whether the provider implements the configuration flow with OAuth authentication support. |
| `implementsSplit` | No | `false` | Defines whether the provider implements the payment split flow. |
| `usesProviderHeadersName` | No | `true` | Defines whether the provider will receive appKey and appToken headers as `"x-provider-api-appKey"` and `"x-provider-api-appToken"` respectively. |
| `useAntifraud` | No | `false` | Defines whether anti-fraud providers can be used in the payment provider's transactions. |
| `usesBankInvoiceEnglishName` | No | `false` | Defines if the Bank Invoice payment method will use the English name (`true`), or the Brazilian name (Boleto Bancário)(`false`). |
| `usesSecureProxy` | No | `true` | If `true`, the provider can process payment without being [PCI-Certified](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance). The connector will receive a `secureProxyUrl` on `createPayment flow`, and the card encrypted data. If `false`, the provider must be a PCI-Certified entity, and you should send the AOC containing the provided `serviceUrl`. |
| `requiresDocument` | No | `false` | If `true`, the customer must include the cardholder document on Checkout. A new field will appear on the Checkout form. If `false`, the customer does not need to include a cardholder document. |
| `acceptSplitPartialRefund` | No | `false` | If `true`, a partial refund will be sent when a payment split occurs. If `false`, the connector couldn't process a partial refund when a payment split occurs. |
| `usesAutoSettleOptions` | No | `false` | If `true`, the client will be able to choose the behavior of the auto settlement in the VTEX admin configurations of the provider. The available options are as follows: "Use behavior recommended by the payment processor", "Automatic capture immediately after payment authorization", "Automatic capture immediately after anti-fraud analysis", "Scheduled: schedules the automatic capture" and "Deactivated: not automatically captured". If `false`, the connector will not have this dropdown configuration field for auto settlement. More information can be found in the [Custom Auto Capture Feature article](https://developers.vtex.com/docs/guides/custom-auto-capture-feature). |

### Request a retry from Payment Gateway

A retry is required to develop your connector according to the [protocol](https://help.vtex.com/en/tutorial/payment-provider-protocol), and for this action, the function below must be invoked:

```js
this.retry(request)
```

> ℹ️ More information about the retry flow can be found in the [Payment Authorization section of the Payment Provider Protocol article](https://help.vtex.com/en/tutorial/payment-provider-protocol#payment-authorization).

### Payment Provider Service

This is a class that extends the Service from `@vtex/api`. You must invoke it by passing the developed connector as a property of the first parameter and it will automatically set up the required routes for you.

The following code shows how to do this and find it in the `node/index.ts` file.

```
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

```js
new PaymentProviderService({
 routes: newRoutes,
 connector: YourPaymentConnector,
})
```

If your connector requires any extra clients, you must also pass them in the parameters along with the connector:

```js
new PaymentProviderService({
 clients: NewClients,
 connector: YourPaymentConnector,
})
```

### Using Secure Proxy

For processing credit, debit or co-branded card transactions, integrations must be compliant with [PCI-DSS security standards](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance). For integrations hosted in VTEX IO supporting one of those payment methods, it is mandatory to use Secure Proxy to make calls to a PCI-certified endpoint. You can check more details in the [Secure Proxy article](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy).

> ⚠️ The endpoint must be allowed by VTEX Secure Proxy. This must be [requested via ticket](https://help.vtex.com/support) sending the AOC with the wanted endpoint. Currently the Secure Proxy only accepts two Content-Types: You can use `\"application/json\"` or `\"application/x-www-form-urlencoded\"`. Any other Content-Type will not be supported.

To make calls over our Secure Proxy, you must:

1. Extend the `SecureExternalClient` abstract class. The constructor of the class is made in a way that VTEX allows `'http://my-pci-certified-domain.com'` as one of the trusted destinations by receiving its AOC.
2. Set the Secure Proxy URL on the request that you want to be proxied. `SecureProxyURL` is received on `createPayment` flow.

```js
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
     csc: cardRequest.cscToken
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

Now that you have a new connector ready to be used, you can test it entirely in the production flow using your store's Checkout.

> ⚠️ The account must be allowed to test IO Connectors. This must be [requested via ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) informing the name of the app and the account where the tests will be made.

A prerequisite for this procedure is to have products for sale at your store for testing. To place an order with your new connector:

1. Launch a beta version of your connector. E.g.: `vtex.payment-provider-test@0.1.0-beta`. If you need, check the [Making your app publicly available article](https://developers.vtex.com/docs/guides/vtex-io-documentation-10-making-your-app-publicly-available#launching-a-new-version) to learn how to create a beta version of your app.
2. Install the beta version on `master` workspace. Wait for around 1 hour.
3. Go to `https://{account}myvtex.com/admin/affiliations/connector/Vtex.PaymentGateway.Connectors.PaymentProvider.PaymentProviderConnector_{connector-name}/`. Replace `{account}` for the name of the account you want to test on and `{connector-name}` for the name of your connector. The format of the name is: `${vendor}-${appName}-${appMajor}` (e.g.: `vtex-payment-provider-example-v1`).
   ![Payment affiliation configuration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-provider-framework-0.png)
4. In **Payment Control**, activate the test environment by clicking **Enable test mode**. A new field called **Workspace** will appear.
5. Set the **Workspace** as you wish. You can leave it as `master` if it is the workspace you want to test on.
   ![Payment affiliation configuration test](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-provider-framework-1.png)
8. Configure a [payment condition](https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions--tutorials_455) with your newly created connector and wait 10 minutes to appear on Checkout.
9. Make a purchase with the payment condition you configured with your connector.
10. After completing all transaction testing in the beta version of the connector, [release and deploy](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available#step-6---deploying-the-app-stable-version) a stable version of your connector (e.g.: vtex.payment-provider-test@0.1.0). This stable version must be sent to the [homologation process](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex#7-homologation-and-go-live).

## Making your connector available to process sales

> ⚠️ To process sales with your connector on all VTEX accounts, make sure to send the `billingOptions` field indicated as `free` in the manifest. If you want to restrict the use of the connector to only a few specific accounts, the `billingOptions` field must also be sent as `free`, but the payments team must be notified via a [support ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) to enable the connector only for the desired accounts. More information about this field can be found in the [Billing Options article](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options).

The publication process is made via the [app store](https://apps.vtex.com/). More info on how to do that can be found in the [Submitting your app to the VTEX App Store article](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store).

After that, you need to [open a ticket to the VTEX support team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM?locale=en) informing them that the integration was completed. However, before opening the ticket, make sure you have the following information:

- **Connector App Name**: Name of the PPF connector app. Use the following format: `"vendor.appname"`. For example: `partnername.connector-partnername`. These can be found in the `manifest.json` file.
- **Partner contact**: partner email address in case we need to communicate changes and new features of our protocol.
- **Production Service Provider Endpoint**: the base path that will be used for API calls to the provider, e.g. `https://vtex.pagseguro.com`. It has to respond to the route `{{serviceUrl}}/manifest` . This endpoint must be publicly available.
- **Allowed Accounts**: describe which VTEX accounts from this provider will be available (all accounts or specific accounts).
- **New Payment methods**: inform if this connector supports a payment method that is not yet available in the VTEX Admin.
- **New Payment method purchase flow**: if a "New Payment method" is supported, inform whether it works with Redirect or Payment App. For more information, access the [Purchase Flows article](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows).

The SLA required for the payment team to carry out homologation is 30 days.

After the homologation step is complete, your app needs to be installed in the account that wants to use it. Then, a new affiliation will be available to configure it.

## Updating and testing new configurations for an already published connector

To change and test new settings in an already published connector, you must:

1. Apply the new settings to the last created beta version of your connector.
2. Follow the same procedures described in the [Placing an order with your new connector](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#placing-an-order-with-your-new-connector) section to verify that the beta version of your connector is working correctly after applying the new settings.
3. Create and submit a new stable version of your connector (containing the same modifications as the beta version) to the homologation process. E.g.: vtex.payment-provider-test@0.1.1.
4. Publish it as indicated in the [Making your connector available to process sales](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#making-your-connector-available-to-process-sales) section.
