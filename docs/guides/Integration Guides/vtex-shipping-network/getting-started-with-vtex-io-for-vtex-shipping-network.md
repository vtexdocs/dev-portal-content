---
title: "Getting started with VTEX IO for VTEX Shipping Network"
slug: "getting-started-with-vtex-io-for-vtex-shipping-network"
hidden: false
createdAt: "2021-04-29T19:53:39.297Z"
updatedAt: "2022-04-08T20:16:01.460Z"
---

[VTEX IO](https://developers.vtex.com/vtex-developer-docs/docs/what-is-vtex-io) is a cloud-native platform that allows VTEX’s clients and partners to develop apps that integrate seamlessly with our ecosystem. This means that once a carrier creates an app on VTEX IO, the app can be made available to any given VTEX store. The store then can simply install it in order to integrate with that carrier’s service.

## VTEX IO CLI and the development environment

VTEX has its own CLI (command line interface), which enables you to perform different tasks required throughout the development process on VTEX IO. For example, it allows you to log in to your VTEX account, link your local files to the platform, or even publish and deprecate apps.

To install VTEX's CLI, you must first have [Node.js](https://nodejs.org/en/) and [Yarn](https://yarnpkg.com/) installed. See the [VTEX IO CLI documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) to learn more about how to install it.

## Developing

When developing carrier apps in VTEX IO, you can start by cloning one of the boilerplate repositories provided below (notification or tracking) to your machine.

[block:callout]
{
  "type": "info",
  "body": "To develop on VTEX IO, a user must have Admin or VTEX IO Developer permission. See this article for more information on accounts and permissions."
}
[/block]
We recommend that you create a new workspace for development. Each workspace works as a separate version of the account in which you can develop your app and test it. To learn more, access our [workspace documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-workspace).

### Manifest

The `manifest.json` file contained in the boilerplate repository holds important app metadata, such as its name, version, and dependencies, among other things. It is the app’s first point of communication with VTEX IO.

After you clone the repository, you should update your app’s `manifest.json` file with its basic information.

You should be mindful of the `billingOptions` field. This field is used to define an app’s distribution on the platform and structure its pricing data, allowing the application usage to be public and, in some scenarios, even monetized. To know more about this field’s structure and how to fill it, see the [Billing Options documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-billing-options).

To learn more about what information other fields must contain, see the [Manifest documentation](https://developers.vtex.com/vtex-developer-docs/docs/manifest).

Below is an example of how some important fields could be filled in the `manifest.json` of a tracking app for an account named `Example Carrier`:

```json
{
    “name”: “example-carrier-notification”,
    “vendor”: “Example Carrier”,
    “title”: “Example Carrier notification”,
    “description”: “This app allows stores to track packages shipped with Example Carrier.”,
    “billingOptions”: {
        “type”: “free”,
        “support”: {
            “email”: “[support@examplecarrier.com](mailto:support@examplecarrier.com)”,
            “url”: “examplecarrier.com/support”
        },
        “availableCountries”: [
            “BRA”,
            “USA”
        ]
    },
    ...
}
```

### Integration hubs

You should also install the VTEX integration hub apps on your account. There are two hubs, and you can install them by running:

- `vtex install vtex.carrier-notifier`
- `vtex install vtex.carrier-tracking`

### Link

Now you can run the command `vtex link`. With this, your local files will be linked to the platform, and you will be able to see the changes you make in the app working in real-time.
[block:callout]
{
  "type": "warning",
  "body": "When you link an app for the first time, it is possible you get an error message like this:\n`Account {{accountName}} is not allowed for developing app \"{{appName}}\" in major \"{{majorVersion}}\"`.\nThis is because developing Node apps is still in closed beta, and your account needs to be approved in the beta program. To do that, just fill the VTEX IO Closed Beta form according to these guidelines for filling the application form. In the \"What are the builders that your app needs?\" field, you should check the builders listed in the `manifest.json` file of the provided boilerplate"
}
[/block]
With this, you should be able to start developing your application.
[block:callout]
{
  "type": "warning",
  "body": "Carrier integration apps should be developed in Node.js."
}
[/block]

### Authentication

After you have released your app, stores will be able to install it in order to integrate with the carrier. Therefore, it is important to put in place an authentication setting to ensure that only the carrier’s clients can use the app.
[block:callout]
{
  "type": "warning",
  "body": "We recommend that you provide different credentials to each store that uses your app."
}
[/block]
You can implement the authentication process by configuring app settings in order to ask the user to input login information. To do this, create a `settingsSchema` field in your `manifest.json` file, like the example below.

```json
“settingsSchema”: {
    “title”: “Carrier Authentication”,
    “type”: “object”,
    “properties”: {
        “user”: {
            “title”: “User”,
            “type”: “string”
        },
        “token”: {
            “title”: “Token”,
            “type”: “string”
        }
    }
}
```

With these settings, whenever a store installs the app, they will be redirected to the Admin and required to provide a user and token. This does not authenticate the user, but asks for the necessary information. It is up to the carrier to implement the internal authentication logic.

Below is an example of how to access these settings in your app.

```js
const appSettings = await ctx.clients.apps.getAppSettings(
    ‘’ + process.env.VTEX_APP_ID
)
```

In case you want to test your authentication setting before the app is published, you can do so whenever it is linked. In this case, go to the Admin page of your VTEX account, then go to **Apps**, **My Apps** and open the **settings** of the linked app.

![Carrier notifier app example on the app store](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/getting-started-with-vtex-io-for-vtex-shipping-network-0.png)

![User and Token settings displayed on admin](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/getting-started-with-vtex-io-for-vtex-shipping-network-1.png)

[block:callout]
{
  "type": "warning",
  "body": "Remember to access the admin in the same workspace the app has been linked to. The URL should be similar to this: `https://{workspace}--{account}.{environment}.com/admin`."
}
[/block]

### App endpoints

Carrier notification and tracking apps are meant to receive data from VTEX’s integration hubs. That is done through API calls made to your apps’ endpoints. These endpoints are described in the `service.json` file, that is in the folder named `node` of the boilerplate repositories.
[block:callout]
{
  "type": "warning",
  "body": "Note that the `service.json` file specifies the external behavior of your app's endpoints, not the internal logic applied to the received data. That logic must be implemented by the developer."
}
[/block]
During development, you may need to test these endpoints, but keep in mind that they are private, meaning that only users with permission can send requests to them. Calls made to these endpoints must include an authorization header with an access token. You can run the command `vtex local token` command to get your token. Since this token contains the email registered to your VTEX account, you will need to set permission to that email  in the `[service.json](https://github.com/vtex-apps/carrier-hubs-examples/blob/main/carrier-notifier-example/node/service.json#L19)` file, by changing `@vtex.com.br` to your own domain.

### Publish

When you are done developing your app and have promoted it to the master workspace, it is ready to be published.

To do so, you may follow the steps described in this tutorial on [how to make your new app version publicly available](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-making-your-new-app-version-publicly-available).
[block:callout]
{
  "type": "info",
  "body": "You may note that steps number 3, 4, and 5 of the tutorial mentioned above are meant for stores creating apps for their own use. So when creating carrier apps, they are not strictly necessary for the app to be made public since carrier apps are meant to be used by other accounts. In that case, steps 1, 2, and 6 should be sufficient, but we do recommend that you follow all steps in order to thoroughly validate it."
}
[/block]

## What is next

See the [integration flow](https://developers.vtex.com/vtex-rest-api/docs/integration-flow) for carriers and learn more about [notification](https://developers.vtex.com/vtex-rest-api/docs/notification-1) and [tracking](https://developers.vtex.com/vtex-rest-api/docs/tracking-1).
