---
title: "Payment app"
slug: "murilofaria-payment-auth-app-mnf"
excerpt: "murilofaria.payment-auth-app-mnf@1.0.2"
hidden: true
createdAt: "2022-07-19T19:51:32.052Z"
updatedAt: "2022-07-21T19:58:20.860Z"
---
The *Payment* app adds a verification step to the checkout process, responsible for allowing or forbidding an order placement.

To implement this feature in your store, you'll need to develop your own *Payment app*, but don't worry! This repository provides the necessary structure for that, and the following step by step will guide you.

## Step by step

> ℹ️ Please, keep in mind that in this step by step you'll be using the [VTEX IO](https://developers.vtex.com/vtex-developer-docs/docs/what-is-vtex-io) development platform.

### Step 1: Setting up the basic development environment

1. Using the terminal, [install the VTEX IO CLI](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/) (Command Line Interface) known as **Toolbelt** .
2. Using the terminal and the Toolbelt, log in to your VTEX account by running the following command:

```shell
vtex login {account}
```

> ⚠️ Remember to replace the values between the curly brackets according to your scenario

Once you run this command, a window will open in your browser asking for your credentials.

3. Once you provide your credentials, run the following command in the terminal to create a [Development workspace](https://vtex.io/docs/recipes/development/creating-a-development-workspace/) and to start developing your *Payment* app.

```shell
vtex use {examplename}
```

> ⚠️ Replace `{examplename}` with a name of your choosing. This name will be given to the workspace in which you will develop.

> ℹ️ If you're used to working with GitHub, think of workspaces as branches.

### Step 2: Editing the Payment app

1. Using your terminal, clone the *Payment* app boilerplate repository to your local files by running:

```shell
git clone https://github.com/vtex-apps/example-payment-authorization-app
```

2. Then, using any code editor of your choice, open the boilerplate repository's directory.
3. Open the `manifest.json` file and update its metadata, according to your scenario. It's essential that you update the following fields:

- `vendor` - The app owner. That is, the VTEX account responsible for the app development, maintenance, and distribution.
- `name` - The app name. It should concisely express the app's purpose. They must be comprised of lowercase letters separated by hyphens. Special characters, such as `*` and `@`, and numbers at the beginning of the name are not recommended.

4. Open the `pages/pages.json` file and replace `{example-payment-auth-app}` with the app `name` set in step 3.
5. Using your terminal, go to the app's directory and run the following command:

```shell
vtex link
```

> ℹ️ Once you [link the app](https://vtex.io/docs/recipes/development/linking-an-app/), your computer's local files will sync to our cloud development environment. This means that any change done locally in the code you are working on will be sent to the cloud and then reflected in the workspace in which you are working.

### Step 3: Running the *Payment* app

1. Using your browser, go to `http://{workspace}--{account}.myvtex.com/checkout?workspace={workspace}`.

> ⚠️ Remember to replace the values between the curly brackets according to your scenario

2. Open the *browser Developer tools* and run the following command:

```javascript
window.transactionAppName = '{app-name}'
```

Now, if you go through the *checkout process*, you'll notice an additional verification step (set in our *Payment* app) after the *Order confirmation*.


### Step 4: Deploying the *Payment* app

> ℹ️ Before deploying your app, we recommend that you perform tests and check if everything is as expected. For that, go to `http://{workspace}--{store}.myvtex.com`. Add products to your store's cart and go to the shopping cart page. Open your browser DevTools and run the following command to get the `orderFormId` value: `vtexjs.checkout.orderFormId`. Now, inject the `orderFormId` value in `vtexcommercestable`, using:
`http://{workspace}--{account}.myvtex.com/checkout?workspace={workspace}&orderFormId={orderFormId}`.

Once you're happy with the changes, follow our documentation on [making your new app version publicly available](https://vtex.io/docs/recipes/development/making-your-new-app-version-publicly-available/) to run your app on master.

## Modus Operandi

After developing and implementing the *Payment* app, your store will profit from having an additional verification step in its checkout process.

To make the best use of the *Payment* app, this section discusses the following topics:

- Understanding the checkout response.
- Handling the order payload.
- Injecting external scripts.

### Understanding the checkout response

After the order placement, there's a validation step to check whether the transaction is approved or not.

If the transaction is approved, the checkout UI redirects to the *Order Placed* page. Otherwise, it shows a warning pop-up.

In our *Payment* app, this validation is performed through the `transactionValidation.vtex` event, which, when triggered, sends the payment status to the checkout UI according to the following [method](https://github.com/vtex-apps/payment-authorization-app-example/blob/3e5742c87a2771998009cff4fecacb092bb3362b/react/index.js#L22):

```javascript
respondTransaction = (status) => {
    $(window).trigger('transactionValidation.vtex', [status])
}
```

Notice that the `respondTransaction` function receives the `status` boolean value, which resolves (`status == true`) or rejects (`status == false`) an order placement.

Hence, whenever the `transactionValidation.vtex` event occurs, the Checkout UI checks the payment status and is redirected according to the `status` value provided to the `respondTransaction` function

### Handling the order payload

The `appPayload` is what the *Payment* app receives as `props` and it consists of a serialized JSON of the order payload.

Thus, to access this information, just run the following command:

```javascript
const { appPayload } = this.props // This appPayload is a serialized JSON (as string).
```

The expected response is a JSON object consisting of the data needed for the Payment app to allow or deny an order placement. Thus, depending on the payment processes implemented in your store, the `appPayload` fields may vary.

Take the following example:

```json
{
    "timeToCancel": 300,
    "transactionApproveLink": "https://..."
}
```

### Injecting external scripts

To run external scripts on your *Payment* app, you need to inject the following script on the head of the checkout `html`. 

To do so, you have to do a DOM injection. For that, you should do:

```javascript
const head = document.getElementsByTagName('head')[0]

const js = document.createElement('script')
js.id = {{script-id}}
js.src = {{script-src}}
js.async = true;
js.defer = true;
js.onload = {{callback-onload}}

head.appendChild(js)
```

There is an example for the script injection [here](https://github.com/vtex-apps/payment-authorization-app-example/blob/3e5742c87a2771998009cff4fecacb092bb3362b/react/index.js#L41)

> ℹ️ Keep in mind that if the external `js` script handles DOM manipulation, then you should use React's [`ref`](https://reactjs.org/docs/refs-and-the-dom.html) to create a `div` container and hand it over to the library. There's also an [example](https://github.com/vtex-apps/payment-authorization-app-example/blob/3e5742c87a2771998009cff4fecacb092bb3362b/react/index.js#L11) for doing so in this repo.