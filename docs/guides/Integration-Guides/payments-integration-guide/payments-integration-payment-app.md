---
title: "Payment App"
slug: "payments-integration-payment-app"
hidden: false
createdAt: "2021-08-05T18:04:05.139Z"
updatedAt: "2022-03-09T16:31:39.613Z"
---

> ℹ️ You can check the demo videos of Payment App on our Office Hours through these links in [English](https://youtu.be/nrZOZ7LMtLE?t=3119) and [Portuguese](https://youtu.be/YJ0qSgYiN8c?t=1064).

A Payment App is a special type of app built-in [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) which allows developers to create custom payment experiences on the checkout page, without redirecting customers to an external website.

In terms of programming, a Payment App is defined as a class in TypeScript that extends from [React’s Component](https://reactjs.org/docs/react-component.html). You can configure a payment method to use a specific Payment App, and this app is instantiated by the Checkout UI when the payment method is selected in the purchase.

The main reasons why someone would choose to build a Payment App over a standard [Payments Integration](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-guide) are that it allows you to:

- Implement a payment method through [Payment Provider Protocol](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-protocol) without a redirect flow (without redirecting users to an external website).
- Add a security layer to your store’s online payments using the [3D Secure 2 (3DS2)](https://help.vtex.com/en/announcements/3ds2-authentication-flow-accept-online-payments-more-securely--6UdTjjVU1AcEQ2aE3Ftxsl) standard.
- Measure conversions by analytics tools for customized flows.

As you can see below, the Payment App is displayed as a modal window when the customer clicks on the **Buy now** button:
![Affirm Payment App](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-app-0.gif)
This tutorial will guide you through the steps required to develop, test, and set up a Payment App in your store. The sections of this tutorial are:

- [Understanding the Payment App flow](#understanding-the-payment-app-flow): An explanation of what a Payment App is, its behavior, and usage.
- [Implementing a Payment App](#implementing-a-payment-app): A step-by-step guide with the basic information needed to develop a Payment App.
- [Operational Mode](#operational-mode): After having deployed the Payment App, check more information about the checkout response. Also, learn how to handle an order payload and how to inject external scripts.

## Understanding the Payment App flow

Our Payment App model applies to a large variety of payment methods thanks to its interaction with the Checkout API, as shown in the following sequence diagram:
![Payment App flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-app-1.png)
Below is described the flow in the same order of the sequence diagram (steps from 1 to 4 are the same for every payment flow; steps unique to the Payment App flow are from 5 onwards):

1. Checkout UI sends a Start Transaction request to the Checkout API.
2. Checkout API sends a [Start Transaction request](https://developers.vtex.com/vtex-rest-api/reference/1createanewtransaction) to the Gateway API.
   - VTEX Payment Gateway creates the new transaction and generates a unique `transactionId`, which is returned to the Checkout, and then to the Checkout UI.
3. Checkout UI sends a [Send Payments request](https://developers.vtex.com/vtex-rest-api/reference/2sendpaymentspublic) directly to the Gateway API.
   - The Gateway will create, for each payment, a payment entity inside the transaction entity that was created in the previous request. Note that, for multiple payments, they are all sent in this same request. That is, one transaction can have multiple payments. For each payment entity, a `paymentId` is generated and all of them are returned to the Checkout UI. This step sends the actual payment information (i.e.: credit card data).
4. Checkout UI sends an Authorization request to the Checkout API.
5. Checkout API encapsulates two requests to the Gateway API.
   - The first is the [Send Additional Data request](https://developers.vtex.com/vtex-rest-api/reference/3sendadditionaldata) that sends to the Gateway API information about the order, such as the client profile data, the shipping address, and the cart information (cart items). Such information is securely stored in the Gateway database, and this information is used by anti-fraud providers, and also used by a few payment providers to Authorize the transaction.
   - The second is the actual [Authorization request](https://developers.vtex.com/vtex-rest-api/reference/4doauthorization) that the Checkout API performs to the Gateway API. This request will trigger the Payment Authorization workflow inside the Gateway API.
     1. The Gateway API calls the [Create Payment request](https://developers.vtex.com/vtex-developer-docs/reference/createpayment) for the correct connector depending on the Payment Conditions that was set up by the store administrator.
     2. At this point, the connector handles the request and performs its logic depending on the Payment method. Using Pix as an example, the connector will request the Payment Provider to create a payment in their API and will receive the necessary information to build the Pix QR Code.
     3. The connector responds the Create Payment request to the Gateway. The body of the response has a `paymentAppData` field, which contains two properties. The first is `appName`, which describes the name of the VTEX account responsible for developing, maintaining and distributing the app, and the name of the Payment App that will be used in the transaction (e.g., `"{vendor}.{appName}"` ). The second is `payload` containing the payload to complete the transaction (i.e.: the information to build the Pix QR code). Then, the Gateway responds to the Checkout API and it responds back to the Checkout UI which instantiates the Payment App with the corresponding payload that was generated in the connector.
6. The Checkout UI instantiates the Payment App defined by the `paymentAppData.appName` and adds to the app object the `appPayload` property and fills this property with the content of `paymentAppData.payload`. Then the Payment App can perform its logic here. For instance, it could be an Authorization App (3DS v2) or a QR Code (Pix), or it could simulate a redirection inside the Payment App frame. At this point, the transaction is in Authorizing state (more information about transaction status can be found in the [Transaction flow in Payments](https://help.vtex.com/en/tutorial/transaction-flow-in-payments--Er2oWmqPIWWyeIy4IoEoQ) article).
7. When the user finishes the interaction, the Payment App closes and it will trigger the transaction Validation in the Checkout UI, which starts the validation where the Checkout UI gets the transaction status from the Checkout API (which will [request the transaction status](https://developers.vtex.com/vtex-rest-api/reference/transactiondetails) from the Gateway API). If the transaction status is **Authorized** or **Undefined** then the Checkout UI displays the Order Placed screen. Else, the Checkout UI shows a warning and returns to the state where the user can choose the payment method.

## Implementing a Payment App

The following tutorial will guide you through the steps required to implement a Payment App, including:

- Information on how to set up a development environment.
- Steps to clone the repository that contains a Payment App boilerplate code for you to edit.
- How to run and test your Payment App.
- Information about the deployment process.

To proceed with the following steps, you will be using the [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) development platform.
> ⚠️ If you are implementing a new payment method in your Payment App, please contact the [VTEX Support Team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support) to add it to the VTEX backend.

### Step 1: Setting up the development environment

1. Using your computer system terminal, [install the VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) (Command Line Interface).
2. After installing VTEX IO CLI, check the documentation [Creating a Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) to create a workspace and start developing the Payment App.
3. When you finish creating the workspace, jump to the next section.

### Step 2: Developing your Payment App

These are the minimum things you need to change in the boilerplate and make your own app.

In addition to these modifications, you need to add the business logic of your payment system.
> ⚠️ Before you start editing the Payment App, it is necessary to have Git installed on your computer. Click [here](https://git-scm.com/downloads) to learn more.

1. Using your terminal, clone the repository that contains a Payment App model to your local files by running:

```shell
git clone https://github.com/vtex-apps/example-payment-authorization-app.git
```

2. After cloning the repository, use a code editor of your choice to open the project locally.

3. Open the `manifest.json` file and update its content according to your scenario. If you need more information about the required fields, access our [Manifest documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest). The value set in the `name` field will be the unique identifier for this app and must be the exact name that corresponds to the response of your connector (`appname` property of `paymentAppData` field in the response body of the Create Payment endpoint). The `billingOptions` field is also required and set with the property `type` as `free`. More information about the `billingOptions` field can be found in the [Billing Options article](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options).

4. After finishing the update, open the `pages/pages.json` file and replace `example-payment-auth-app` with the app `name` set in `manifest.json`. The `pages.json` file is responsible for creating the routes for your application. So it is necessary to make this configuration for the VTEX system to find and display the app at checkout. Also, the `"component"` field having the `"index"` value indicates that the `index.js` file in the `react` folder is the file with the component that will be instantiated at checkout.

> ⚠️ Replace only the last part of the path in the `pages.json` file for the name of your app. In this case, the `example-payment-auth-app` part.  Do not change the beginning of the path `checkout/transactions/`, since the checkout uses it to identify a payment application.\n\nAlso, if you are using the **Test Connector** to make internal tests with your app, you have to keep the original name of the app that came from the repository in the `pages.json` file, since it will be the reference for this connector to open the Payment App in the checkout.

5. Using your terminal, go to the app directory and run the following command:

```shell
vtex link
```

Once you [link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app), your local computer files will sync to our cloud development environment. It means that any change done locally in the code you are working on will be sent to the cloud and reflected in the workspace.

### Step 3: Testing a Payment App flow

A Payment App will appear on the checkout screen by following the steps below, allowing you to test the Payment App general flow.

> ℹ️ Proceed with the following steps only when you want to test a Payment App flow; otherwise, skip to [Step 4: Deploying the Payment app](#step-4-deploying-your-payment-app).

1. Make sure you have your connector installed in your account configured with the Payment App and the payment method you want to test in your Payment App. The connector must contain the field `paymentAppData` in the response body of the [Create Payment endpoint](https://developers.vtex.com/vtex-developer-docs/reference/createpayment) with the right properties (`"appName": "{vendor}.{appName}"` and `"payload": "{payload information}"`). If you do not have the connector installed yet, contact the [VTEX Support Team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support) to help you with the installation process. More information about how the endpoints should be implemented can be found in the article [Implementing a Payment Provider](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-implementing-a-payment-provider).
2. Select the payment condition associated with your connector in the checkout and finish the purchase to test the flow.

### Step 4: Deploying your Payment App

Once you finish the changes, follow our documentation on [Making your new app version publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) to run your app on the **Master** workspace.

## Operational Mode

If you followed all the previous steps, it means that you successfully created a Payment App and are ready to take advantage of the benefits of having an additional verification step to the checkout of your store.

This section discusses the following topics to help you make the best use of the Payment App:

- Handling the order payload.
- Understanding the response to the Checkout UI.
- Injecting external scripts.

### Handling the order payload

The `appPayload` is what the Payment App receives as props, and it consists of a serialized JSON of the order payload. This variable is not declared in the Payment App class, but it is added to its `props` after the Payment App is instantiated in the Checkout UI. You can access this information with the following code:

```js
const { appPayload } = this.props // This appPayload is a serialized JSON (as string).
```

The expected content is a JSON object consisting of the Payment App’s data needed for the Payment App to allow or deny an order placement. Thus, the `appPayload` fields will be defined by the developer of the associated connector.

To exemplify how the payload can be used, take the following example:

```json
{
    "timeToCancel": 300,
    "transactionApproveLink": "https://..."
}
```

In this example, there are two fields for illustration. The first field (`"timeToCancel"`) can mean the amount of time after the payment app stays open before automatically canceling the transaction. The second field (`"transactionApproveLink"`) can have a link to request for the approval of the transaction if all the conditions in the Payment App are fulfilled.

### Understanding the response to the Checkout UI

When the Payment App finishes its operation, it has to inform the Checkout UI that it should be closed and then check if the transaction is approved or not. If the transaction is `approved` or `undefined`, the Checkout UI will redirect the user to the Order Placed page; otherwise, it will show a warning pop-up and then take the user back to the payment options.

To perform these steps, the Checkout UI listens to the `transactionValidation.vtex` event that is triggered by the Payment App using the [browser’s native event handling engine](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events) during the validation step. When this event is triggered, the Checkout UI will close the Payment App and check the transaction status from the Gateway. The following [example method](https://github.com/vtex-apps/example-payment-authorization-app/blob/master/react/index.tsx#L45) can be used by the Payment App to trigger the event:

```js
respondTransaction = () => {
    $(window).trigger('transactionValidation.vtex')
}
```

> ⚠️ If the `transactionValidation.vtex` event is not triggered, the order confirmation email will not be sent to the user. We recommend that you create a retry flow to act in cases where this event is not triggered or the order confirmation email is not sent.

### Injecting external scripts

An external script injection allows your Payment App to have additional content and behavior. To run external scripts on your Payment app, you need to inject the following script on the `head` of the checkout `html`. To do so, you have to do a DOM injection as follows:

```js
const head = document.getElementsByTagName('head')[0]

const js = document.createElement('script')
js.id = {{script-id}}
js.src = {{script-src}}
js.async = true;
js.defer = true;
js.onload = {{callback-onload}}


head.appendChild(js)
```

There is an example of script injection [here](https://github.com/vtex-apps/example-payment-authorization-app/blob/master/react/index.tsx#L89) that inserts Google Recaptcha to a Payment App.
> ℹ️ Keep in mind that if the external `js` script handles DOM manipulation, you should use [React's Ref](https://reactjs.org/docs/refs-and-the-dom.html) to create a `div` container and hand it over to the library. You can find an [example here](https://github.com/vtex-apps/example-payment-authorization-app/blob/master/react/index.tsx#L106).

## Payment App Scenarios

In the following sections, you will find some scenarios in which you can use a Payment App.

### Scenario 1: An integration via Payment Provider Protocol that requires a new payment method

The best way to create a new payment method is by developing a Payment App, once it allows customers to complete the payment transaction without leaving the checkout page. It also allows you to add a security layer to your store’s online payments by using the [3D Secure 2](#scenario-2-payment-app-and-3d-secure-2) standards.

### Scenario 2: Payment App and 3D Secure 2

The [3D Secure 2](https://3dsecure2.com/) is a protocol that allows a website’s checkout process to comply with the [Strong Customer Authentication (SCA)](https://3dsecure2.com/glossary/#what-is-strong-customer-authentication-sca) requirements by performing risk-based authentication to approve an online card transaction. It was created to attend to the [Revised Payment Service Directive 2 (PSD2)](https://3dsecure2.com/glossary/#what-is-payment-service-directive-2) regulations in Europe.

The 3D Secure 2 (3DS2) is an evolution of the 3D Secure 1 (3DS1). It introduces the [frictionless authentication flow](https://3dsecure2.com/glossary/#what-is-frictionless-flow) and improves the purchase experience compared to 3DS1. More details about the differences between 3DS1 and 3DS2 can be found in the [3D Secure 2 FAQ](https://3dsecure2.com/frequently-asked-questions/#what-are-the-main-changes-in-3d-secure-2).

> ⚠️ On VTEX, [3D Secure 2](https://3dsecure2.com/) can only be implemented through the Payment App, as the platform doesn't support alternative methods such as redirect URLs for this protocol.

#### 3DS2 flow

To apply the 3DS2 to the checkout, the acquirer that processes the website payments needs to create a Payment App that will handle challenges for each [issuing Bank](https://help.vtex.com/en/tutorial/what-is-the-issuing-bank--7aVIVGwgtU4SWuqowSQksg) that will use the Strong Authentication through the 3DS2.

When the customer adds the credit card information and clicks on the Checkout button, the acquirer will call the issuing bank through the 3DS2 flow.

The card issuer will, in turn, analyze the fraud context of that purchase (the score, probability), also called [Risk-based Authentication](https://3dsecure2.com/frictionless-flow/#what-is-risk-based-authentication). The score will be a result of a series of risk-based elements which can include the value of the purchase, transactional history, device information, among others. If this analysis returns as a score for high fraud risk, the provider can choose to call the 3DS2 challenge asking the customer to proceed with the Strong Authentication method (i.e.: approve the payment in the bank app). If it falls in a score for low fraud risk, the provider will not call the challenge.

If the acquirer decides that it must perform the Strong Authentication for any payment, it must return to VTEX, in the response body of the [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) route, his `status` as `undefined` and his Payment App information in the `paymentAppData` field.

The `status` returned as `undefined` indicates to our Gateway that the payment has not yet been authorized or denied. There may be several reasons for this, with Strong Authentication being one of them. What will make the Payment App, which runs 3DS2, be called is the `paymentAppData` field in the response.

The Gateway will save this app data on the payment and tell the Checkout that payment has not yet been authorized or denied. It will make the Checkout UI run the Payment App specified in the `paymentAppData` field.

Once the Payment App opens, the Strong Authentication warning will be displayed to the customer within the Payment App on the checkout screen. It will require the customer to approve the transaction from his account on the issuing Bank (i.e.: in the bank app).

After finishing the interaction with the Payment App, the app closes and redirects the customer depending on the `status` of the transaction. If it is `approved` or still is `undefined`, it will go to the order placed screen. If it is `denied` or `canceled`, the Checkout UI shows a warning and returns to the state where the user can choose the payment method.

The following image shows how the 3DS2 is displayed to customers:

![Payment App 3DS2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-payment-app-2.png)
