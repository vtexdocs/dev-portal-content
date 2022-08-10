---
title: "Payment Provider Framework (IO)"
slug: "qabriggsandstrattonstandby-delego-card-processor"
excerpt: "qabriggsandstrattonstandby.delego-card-processor@0.2.0"
hidden: true
createdAt: "2022-08-08T18:21:41.200Z"
updatedAt: "2022-08-08T18:21:41.200Z"
---
## Disclaimer

This is a feature in BETA stage, which means it's on a testing phase. In case there is a new scenario that PPF is not ready, our team will take some time to perform an investigation. If it's a case that need the development of anything new, this will enter the process of prioritization of the product team. This can take some time, so we don't recommend the use of this Beta version of PPF for connectors related to stores with rollout date close (less than 3 months).

## Getting Started: Cloning base repository

If you're starting a brand new project, we recommend you clone [the example repository](https://github.com/vtex-apps/payment-provider-example), as it already has all the basic configuration setup.

<br />

## Getting Started: Updating project

Your first step should be to run the following command on your node folder:

```
yarn add @vtex/payment-provider
```

Afterwards, go to your ***package.json*** and make sure it has been added as a dependency with the correct version:

```
"@vtex/payment-provider": "1.x",
```

Also check in the ***package.json*** is the version of vtex/api, which should be listed in the *devDependencies* as follows:

```
"@vtex/api": "6.x",
```

(When linking your app, this version might get updated to a later 6.x version, which is fine.)

In case it's not listed as a devDependency, run the following command on your node folder:

```
yarn add -D @vtex/api
```

  Note: If you get any type errors or conflicts in your project related to @vtex/api, follow these steps to resolve the problem: delete the **node_modules** folder and the **yarn.lock** file from both your project root and your project's **node** folder, then run the command **yarn install -f** in both folders.  

Lastly, in your ***manifest.json,*** you should check the ***builders*** section, in which you must include the ***paymentProvider*** in it's current version:

```tsx
"builders": {
    "node": "6.x",
    "paymentProvider": "1.x"
  },
```

Note: This will add policies to callback the Payment Gateway APIs and also expose Payment Provider protocol routes.


<br />

## Next steps

Now, in order to create your service, you must implement your payment provider connector and the service itself. To help you with them, we created the following:

<br />

## Payment Provider

This is an abstract class with the signatures of the routes functions required in your connector, according to the [protocol](https://help.vtex.com/en/tutorial/payment-provider-protocol).

You must create a new class extending the PaymentProvider, which must implement a function for each route. The functions will receive the request body (when there is one) as a parameter and the response must be returned as an object, such as the example shown below:

```tsx
import {
	PaymentProvider,
	// ...
} from '@vtex/payment-provider'

class YourPaymentConnector extends PaymentProvider {

	// ... implementation of the other routes functions
}
```

Typescript should automatically check for typing errors, but if you need, you can check the requests and responses signatures [here](https://developers.vtex.com/vtex-developer-docs/reference/payment-flow).


<br />

### Payment Provider Builder

In order to specify which payment methods the connector will accept to process, you need to create a folder named *paymentProvider* using the following folder structure

```markdown
node
paymentProvider
manifest.json
```

Then, inside paymentProvider folder you must create a file named *configuration.json*

```markdown
node
paymentProvider
   |--configuration.json
manifest.json
```

Next, declare the accepted payment methods, for instance:

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

By doing this you don't need to declare /manifest or /payment-methods route, it will be implemented automatically by the builder.

<br />

### Overriding Default Routes

You can also override the default generated routes by redeclaring it on *service.json*

```json
{
  "memory": 256,
  "ttl": 10,
  "timeout": 10,
  "minReplicas": 2,
  "maxReplicas": 3,
  "routes": {
    "authorize": {
      "path": "/_v/api/my-connector/payments",
      "public": true
    },
    "cancel": {
      "path": "/_v/api/my-connector/payments/:paymentId/cancellations",
      "public": true
    },
    "settle": {
      "path": "/_v/api/my-connector/payments/:paymentId/settlements",
      "public": true
    },
    "refund": {
      "path": "/_v/api/my-connector/payments/:paymentId/refunds",
      "public": true
    },
    "inbound": {
      "path": "/_v/api/my-connector/payments/:paymentId/inbound/hooks",
      "public": true
    },
  }
}
```

Then you must specify which is the new serviceUrl on paymentProvider/configuration.json

```json
{
  "name": "MyConnector",
  "serviceUrl": "/_v/api/my-connector",
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

> !! Prefer using default generated routes !!

<br />

### Overriding the Manifest Route

The manifest route is special, it is automatically generated by the builder, our payment gateway exposes it as a proxy of your app.

Generally speaking, the manifest route makes no difference at runtime, and if you have a use case to override the default route tell us.

But, if you want to override it anyway you have to add special parameters on it,

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

Pay attention on `x-provider-app` it should be updated every time that your major changes,

Example

- `vtex.payment-provider-example@1.2.3` should be `vtex.payment-provider-example@1.2.3`

The same applies to payment-methods route

You can also omit the `handler` and `headers` parameters, by doing it you will need to implement it by your own

<br />

### Available Configurable Options

Along with manifest fields (paymentMethods and customFields) there are another configurable options,

- ***serviceUrl*** (required, default: auto-generated for IO Connectors)
    - A valid url (can include relative paths)
- ***implementsOAuth** (default: **false**)*
    - ***true*** - The provider implements the configuration flow supporting OAuth.
    - ***false*** - The provider dosnt implements the configuration flow
- ***implementsSplit** (default: **false**)*
    - ***true*** - The provider implements can receive recipients on payment flow (capture or authorization)
    - ***false*** - The provider doesn't implements the split flow
- ***usesProviderHeadersName*** (default: ***true***, for IOConnectors it should be true)
    - ***true*** - The provider will reiceve appKey and appToken headers as ```"x-provider-api-appKey"``` & `"x-provider-api-appToken"`
    - ***false*** - The provider will reiceve appKey and appToken headers as `"x-vtex-api-appKey"` & `"x-vtex-api-appToken"`
- ***usesAntifraud** (default: **false**)*
    - ***true*** - The provider can be used along antifrauds.
    - ***false*** - The provider can't be used along antifrauds
- ***usesBankInvoiceEnglishName (**default**: false)***
- ***name*** (required)
    - The connector name
- ***usesSecureProxy (**default**: true)***
    - ***true*** - The provider can process payment without being PCI-Certified, the connector will receive a secureProxyUrl on createPayment flow, and the card encrypted data.
    - ***false*** - The provider MUST be a PCI-Certified entity, and we should receive the AoC containing the provided serviceUrl.
- ***requiresDocument (**default**: false)***
    - ***true*** - The customer must include the card holder document on checkout. A new field will appear on checkout form.
    - ***false*** - The customer doesn't need to include card holder document.
- ***acceptSplitPartialRefund (**default**: false)***
    - ***true*** - Partial refund will be sent when payment split occurs.
    - ***false*** - The connector couldn't process partial refund when payment split occurs.
- ***usesAutoSettleOptions (**default**: false)***
    - ***true*** - The client will be able to choose the behaviour of the auto settlement in the VTEX admin configurations of the provider. The options available are the following: Use behavior recommended by the payment processor, Automatic capture immediately after payment authorization, Automatic capture immediately after anti-fraud analysis, Deactivated: Not automatically captured.
    - ***false*** - The connector won't have this dropdown configuration field for auto settlement.
   



<br />

### Request a retry from Payment Gateway

A retry is required in order to develop your connector according to the [protocol](https://help.vtex.com/en/tutorial/payment-provider-protocol), so we built a function, which can be invoked like shown below:

```tsx
this.retry(request)
```

> Callback flow is replaced by retry flow. Payment Providers implemented using VTEX IO are not able to callback the Payment Gateway with the Payment status updated. Instead, the retry flow allow the connector to ask the Payment Gateway to call create payment route again.
> The connector should be able to respond approved/denied consistently.
![image](https://user-images.githubusercontent.com/5839364/138521406-fe3875c1-92ae-4064-aafe-c4c5de56427e.png)

<br />

### Payment Provider Service

This is a class that extends the Service from @vtex/api. You must invoke it passing the developed connector as a property of the first parameter and it will automatically setup the required routes for you.

```tsx
import {
	PaymentProviderService,
} from '@vtex/payment-provider'

new PaymentProviderService({
	connector: YourPaymentConnector,
})
```

By default, the Payment Provider Service declares the following routes:

- /payment-methods
- /manifest
- /payments
- /settlements
- /refunds
- /cancellations
- /inbounds

If your service requires any extra routes, you must declare them separately and use them as parameters:

```tsx
new PaymentProviderService({
	routes: newRoutes,
	connector: YourPaymentConnector,
})
```

If your connector requires any extra clients, you must also pass them in the parameters along with the connector:

```tsx
new PaymentProviderService({
	clients: NewClients,
	connector: YourPaymentConnector,
})
```


<br />

### Using Secure Proxy

Those who aren't PCI-certified, could use Secure Proxy to make calls to a PCI-Certified endpoint.

 ***Important: The endpoint must be allowed by VTEX Secure Proxy by sending the AOC with the wanted endpoint.*** 

 ***Important 2: Currently we only accept two Content-Types: You can use "application/json" or "application/x-www-form-urlencoded", any other Content-Type will not be supported by the Secure Proxy.***

In order to make calls over our Secure Proxy, you must:

1. Extend SecureExternalClient abstract class

```tsx
import { SecureExternalClient } from '@vtex/payment-provider'
import type {
  InstanceOptions,
  IOContext
} from '@vtex/api'
export class MyPCICertifiedClient extends SecureExternalClient {
  constructor(protected context: IOContext, options?: InstanceOptions) {
    super('http://my-pci-certified-domain.com', context, options)
  }
 ...
}
```

> This means that VTEX allows 'http://my-pci-certified-domain.com' as one of the trusted destinations by receiving its AOC.

2.   Set secure proxy URL on the request that you want to be proxied

```tsx
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

> Note: SecureProxyURL is received on createPayment flow

<br />

## Placing an Order with your new Connector!

Now that we have a new connector ready to be use, we can test it entirely in the production flow using your store's checkout.


> <span style="color:red"> ***!! The account MUST be ALLOWED to use IO Connectors !!***</span>

> <span style="color:red"> ***!! For processing NEW payment methods, their creation must be requested !!***</span>

Ask for this in the `#beta-payment-provider-framework-questions` slack channel

A prerequisite for this step is to have products for sale at your store for testing

1. Launch a beta version of your connector, e.g. `vtex.payment-provider-test@0.1.0-beta`
2. Install the beta version on `master` workspace (wait ~1 hour)
3. Go to https://${account}.myvtex.com/admin/pci-gateway/#/affiliations/vtex-payment-provider-test-v0/

The format is: `${vendor}-${appName}-${appMajor}`

![new-configuration-production](https://user-images.githubusercontent.com/27698855/116406925-91d7ab80-a807-11eb-9a26-44e2f418df9d.png)

4. Change the toggle configuration to `Test`

5. Click save and refresh page

6. Enter again in the saved configuration and you will notice that a new field appears, called `workspace`

7. Set the `workspace` as you wish (you can leave it as `master`)

![new-configuration-test](https://user-images.githubusercontent.com/27698855/116406935-94d29c00-a807-11eb-80c6-190e8fd6d373.png)

8. Configure a payment condition with your newly created connector and wait 10 minutes to appear on checkout!

<br />

## Making your connector available to everyone

â ï¸ Important: If you want to make your connector available to all accounts, make sure to have the billing options field in your manifest

The publication process is made via app store, more info on how to do that here: 

[Submitting your app in the VTEX app store](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store)

After the homolog step is complete, your app needs to be installed in the account that wants to use it, and after that, a new affiliation will be available to configure it.

The app should be available at `apps.vtex.com`.


**Upcoming documentation:**

 - [Add vbase client to persist responses](https://github.com/vtex-apps/payment-provider-example/pull/30)