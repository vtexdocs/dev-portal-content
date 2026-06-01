---
title: "Payment App"
slug: "payments-integration-payment-app"
hidden: false
createdAt: "2021-08-05T18:04:05.139Z"
updatedAt: "2026-05-26T00:00:00.000Z"
excerpt: "Learn how to build a Payment App on VTEX IO to create custom payment experiences at checkout without redirecting customers."
---

> ℹ️ Watch the Payment App demo on VTEX Office Hours: [English](https://youtu.be/nrZOZ7LMtLE?t=3119) | [Portuguese](https://youtu.be/YJ0qSgYiN8c?t=1064).

A Payment App is a special type of app built in [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) that allows developers to create custom payment experiences on the checkout page without redirecting customers to an external website.

Technically, a Payment App is a TypeScript class that extends [React's Component](https://react.dev/reference/react/Component). You configure a payment method to use a specific Payment App, and the Checkout UI instantiates the app when the customer selects that payment method.

Build a Payment App instead of a standard [Payments Integration](https://developers.vtex.com/docs/guides/payments-integration-guide) to:

- Implement a payment method through [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) without a redirect flow (without redirecting users to an external website).
- Add a security layer to your store’s online payments using the [3D Secure 2 (3DS2)](https://3dsecure2.com/) standard.
- Measure conversions by analytics tools for customized flows.

The Payment App is displayed as a modal window when the customer clicks the **Buy now** button:
![Affirm Payment App](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-app-0.gif)
This guide covers how to develop, test, and deploy a Payment App:

- [Understanding the Payment App flow](#understanding-the-payment-app-flow): How the Payment App interacts with the Checkout API and Gateway.
- [Implementing a Payment App](#implementing-a-payment-app): Step-by-step development guide.
- [Operational Mode](#operational-mode): Handling the order payload, responding to the Checkout UI, and injecting external scripts.

> ⚠️ IO apps do not work in headless environments. If you want to process payments in this type of scenario, you must use a checkout [webview](https://developer.chrome.com/docs/webview) or implement a fully headless integration directly between your system and the acquirer/connector, sending the information via custom payments or promissory notes.

## Understanding the Payment App flow

The Payment App model supports a wide variety of payment methods through its interaction with the Checkout API. The following sequence diagram illustrates the complete flow:

![Payment App flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-app-1.png)

The numbered steps below correspond to the diagram. Steps 1–4 are common to every payment flow. Steps 5–7 are specific to the Payment App flow.

1. Checkout UI sends a [Start Transaction request](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions) to the Checkout API.
2. Checkout API sends a [Start Transaction request](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions) to the Gateway API. The Gateway creates a new transaction, generates a unique **`transactionId`**, and returns it to the Checkout UI.
3. Checkout UI sends a [Send Payments request](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments) directly to the Gateway API. The Gateway creates a payment entity for each payment inside the transaction. A single transaction can contain multiple payments (all sent in this request). Each payment entity receives a unique **`paymentId`**. This step transmits the actual payment information (for example, credit card data).
4. Checkout UI sends an [Authorization request](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/authorization-request) to the Checkout API.
5. Checkout API sends two requests to the Gateway API:
   - [Send Additional Data](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/additional-data): Sends order information (client profile, shipping address, cart items) to the Gateway. This data is stored securely in the Gateway database, and used by anti-fraud providers or some payment providers during authorization.
   - [Authorization request](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/authorization-request): Triggers the Payment Authorization workflow inside the Gateway. The workflow proceeds as follows:
     1. The Gateway calls [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) on the connector configured in the store's payment conditions.
     2. The connector executes its payment-method logic. For example, a Pix connector requests the payment provider to generate a QR code.
     3. The connector responds with a **`paymentAppData`** field containing:
        - **`appName`**: The Payment App identifier in the format `"{vendor}.{appName}"`.
        - **`payload`**: The data required to complete the transaction (for example, the Pix QR code content).
        The Gateway forwards this response through the Checkout API back to the Checkout UI.
6. The Checkout UI instantiates the Payment App identified by `paymentAppData.appName` and injects `paymentAppData.payload` into the app's `appPayload` property. The app then executes its logic, for example, rendering a 3DS2 authentication challenge, displaying a Pix QR code, or simulating a redirect within the Payment App frame. At this point, the transaction enters the **Authorizing** state. Learn more in [Transaction flow in Payments](https://help.vtex.com/en/tutorial/transaction-flow-in-payments--Er2oWmqPIWWyeIy4IoEoQ).
7. When the user completes the interaction, the Payment App closes and triggers transaction validation. The Checkout UI [queries the transaction status](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/pvt/transactions/-transactionId-) from the Gateway API through the Checkout API:
   - **Authorized** or **Undefined**: The Checkout UI displays the Order Placed screen.
   - **Any other status**: The Checkout UI displays a warning and returns the user to the payment method selection.

## Implementing a Payment App

This section walks through setting up the development environment, cloning the boilerplate, testing, and deploying. All steps use the [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) development platform.
> ⚠️ If you are implementing a new payment method in your Payment App, contact the [VTEX Support Team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support) to add it to the VTEX backend.

### Step 1: Setting up the development environment

1. [Install the VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) in your terminal.
2. [Create a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace).

### Step 2: Developing your Payment App

Make the following changes to the boilerplate to create your own app. You also need to add the business logic of your payment system.

> ⚠️ Before you start editing the Payment App, you must have [Git](https://git-scm.com/downloads) installed on your computer.

1. Using your terminal, clone the repository that contains a Payment App model to your local files by running:

```shell
git clone https://github.com/vtex-apps/example-payment-authorization-app.git
```

2. Open the cloned project in a code editor.
3. Open `manifest.json` and update the fields for your scenario. Key requirements:
   - **`name`**: Must match the `appName` property of `paymentAppData` in the connector's [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) response body.
   - **`billingOptions`**: Set `type` to `free`. See [Billing Options](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options).

   For details on all required fields, see the [Manifest documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

4. Open `pages/pages.json` and replace `example-payment-auth-app` with the `name` value from `manifest.json`. This file creates the routes that allow VTEX to find and display the app at checkout. The `"component": "index"` entry indicates that `react/index.js` contains the component instantiated at checkout.

> ⚠️ Replace only the last part of the path in `pages.json` with your app name (the `example-payment-auth-app` part). Do not change the `checkout/transactions/` prefix, which the checkout uses to identify payment applications.
>
> If you are using the **Test Connector** for internal tests, keep the original app name from the repository in `pages.json`. The Test Connector uses this name to open the Payment App in checkout.

5. Using your terminal, go to the app directory and run the following command:

```shell
vtex link
```

Once you [link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app), local file changes sync automatically to the VTEX cloud development environment and are reflected in your workspace.

### Step 3: Testing a Payment App flow

Follow the steps below to display the Payment App on the checkout screen and test the general flow.

> ℹ️ Proceed with the following steps only when you want to test a Payment App flow; otherwise, skip to [Step 4: Deploying the Payment app](#step-4-deploying-your-payment-app).

1. Verify that your connector is installed and configured with the Payment App and payment method you want to test. The connector must return the `paymentAppData` field in the [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) response body with the following properties:
   - `"appName": "{vendor}.{appName}"`
   - `"payload": "{payload information}"`
   If the connector is not installed yet, contact the [VTEX Support Team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support) for help with installation. See [Implementing a Payment Provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider) for endpoint implementation details.
2. Select the payment condition associated with your connector in the checkout and finish the purchase to test the flow.

### Step 4: Deploying your Payment App

Once you finish the changes, follow the documentation on [Making your new app version publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) to run your app on the **Master** workspace.

## Operational Mode

After deploying the Payment App, use the following features to customize its behavior:

### Handling the order payload

The Payment App receives `appPayload` as a prop, a serialized JSON string containing the order payload. This prop is not declared in the Payment App class; the Checkout UI injects it after instantiation. Access it with the following code:

```js
const { appPayload } = this.props // This appPayload is a serialized JSON (as string).
```

The JSON object contains the data the Payment App needs to approve or deny the transaction. The connector developer defines which fields appear in `appPayload`.

Example payload:

```json
{
    "timeToCancel": 300,
    "transactionApproveLink": "https://..."
}
```

In this example:

- `"timeToCancel"`: Time in seconds before the Payment App automatically cancels the transaction.
- `"transactionApproveLink"`: URL to request transaction approval when the Payment App conditions are met.

### Understanding the response to the Checkout UI

When the Payment App finishes its operation, it must notify the Checkout UI so the UI can close the app and verify the transaction status. If the status is `approved` or `undefined`, the Checkout UI redirects the customer to the Order Placed page. Otherwise, it displays a warning and returns the customer to payment method selection.

The Payment App notifies the Checkout UI by dispatching the `transactionValidation.vtex` event using the [browser’s native event handling engine](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events). The Checkout UI listens for this event, closes the Payment App, and queries the transaction status from the Gateway. Use the following [method](https://github.com/vtex-apps/example-payment-authorization-app/blob/master/react/index.tsx#L45) to trigger the event:

```js
respondTransaction = () => {
    $(window).trigger('transactionValidation.vtex')
}
```

> ℹ️ The `$(window).trigger()` syntax above uses jQuery, which is available in the VTEX Checkout environment. Alternatively, you can use the native browser API: `window.dispatchEvent(new Event('transactionValidation.vtex'))`.

> ⚠️ If the `transactionValidation.vtex` event is not triggered, the order confirmation email will not be sent to the user. Create a retry flow to act in cases where this event is not triggered or the order confirmation email is not sent.

### Injecting external scripts

External script injection adds custom content and behavior to your Payment App. Inject the script into the checkout `<head>` element using DOM manipulation:

```js
const head = document.getElementsByTagName('head')[0]

const js = document.createElement('script')
js.id = '{{script-id}}'       // Replace with your script's unique identifier
js.src = '{{script-src}}'     // Replace with the external script URL
js.async = true
js.defer = true
js.onload = {{callback-onload}} // Replace with a callback function to run after the script loads

head.appendChild(js)
```

See the [script injection example](https://github.com/vtex-apps/example-payment-authorization-app/blob/master/react/index.tsx#L89) that adds Google reCAPTCHA to a Payment App.
> ℹ️ If the external script handles DOM manipulation, use [React's Ref](https://react.dev/learn/referencing-values-with-refs) to create a `div` container and pass it to the library. See the [example](https://github.com/vtex-apps/example-payment-authorization-app/blob/master/react/index.tsx#L106).

## Payment App Scenarios

The following scenarios illustrate common Payment App use cases.

### Scenario 1: An integration via Payment Provider Protocol that requires a new payment method

A Payment App is the recommended approach for new payment methods because customers complete the transaction without leaving the checkout page. It also enables adding a security layer to online payments using the [3D Secure 2](#scenario-2-payment-app-and-3d-secure-2) standard.

### Scenario 2: Payment App and 3D Secure 2

[3D Secure 2](https://3dsecure2.com/) (3DS2) is a protocol that enables checkout processes to comply with [Strong Customer Authentication (SCA)](https://3dsecure2.com/glossary/#what-is-strong-customer-authentication-sca) requirements through risk-based authentication for online card transactions. It was created to meet the [Revised Payment Service Directive 2 (PSD2)](https://3dsecure2.com/glossary/#what-is-payment-service-directive-2) regulations in Europe.

3DS2 is an evolution of 3D Secure 1 (3DS1), introducing the [frictionless authentication flow](https://3dsecure2.com/glossary/#what-is-frictionless-flow) and improving the purchase experience. See the [3D Secure 2 FAQ](https://3dsecure2.com/frequently-asked-questions/#what-are-the-main-changes-in-3d-secure-2) for a comparison.

> ⚠️ On VTEX, [3D Secure 2](https://3dsecure2.com/) can only be implemented through the Payment App, as the platform doesn't support alternative methods such as redirect URLs for this protocol.

#### 3DS2 flow

To apply 3DS2 at checkout, the acquirer must create a Payment App that handles authentication challenges for each [issuing bank](https://help.vtex.com/en/tutorial/what-is-the-issuing-bank--7aVIVGwgtU4SWuqowSQksg) that requires Strong Authentication.

When the customer enters card information and clicks the Checkout button, the acquirer calls the issuing bank through the 3DS2 flow.

The card issuer performs [Risk-based Authentication](https://3dsecure2.com/frictionless-flow/#what-is-risk-based-authentication), analyzing the fraud context of the purchase. The risk score is based on elements such as transaction value, purchase history, and device information.

- **High fraud risk**: The issuer triggers the 3DS2 challenge, requiring the customer to complete Strong Authentication (for example, approving the payment in the bank app).
- **Low fraud risk**: The issuer does not trigger the challenge (frictionless flow).

If the acquirer requires Strong Authentication for a payment, it must return `status` as `undefined` and include the Payment App information in the `paymentAppData` field of the [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) response body.

A `status` of `undefined` indicates to the VTEX Gateway that the payment is not yet authorized or denied, Strong Authentication is one possible reason. The `paymentAppData` field in the response determines which Payment App the Checkout UI instantiates.

The Gateway stores the app data on the payment and notifies the Checkout that the payment is not yet authorized or denied. The Checkout UI then instantiates the Payment App specified in the `paymentAppData` field.

The Payment App displays the Strong Authentication challenge on the checkout screen, requiring the customer to approve the transaction through the issuing bank (for example, via the bank app).

After the customer completes the challenge, the Payment App closes and the Checkout UI checks the transaction status:

- **`approved` or `undefined`** — The Checkout UI displays the Order Placed screen.
- **`denied` or `canceled`** — The Checkout UI displays a warning and returns the customer to payment method selection.

The following image shows how the 3DS2 is displayed to customers:

![Payment App 3DS2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-app-2.png)
