---
title: "Creating an interface for your app settings"
slug: "vtex-io-documentation-creating-an-interface"
hidden: false
createdAt: "2024-02-20T15:29:55.338Z"
updatedAt: "2024-02-20T15:29:55.338Z"
excerpt: "Learn how to create an interface for your app settings and retrieve its data"
---

When developing a [VTEX IO app](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app), you can create an interface for accepting custom user settings.  This app interface displays configuration forms for each app installed on the account, and it uses the `settingsSchema` field on `manifest.json` that an app may declare the schema of its configuration.

See the Google Tag Manager app interface in the example below, with the appropriate configuration of the `settingsSchema` field in the `manifest.json` file:

![GTM_PixelApp](https://github.com/vtexdocs/dev-portal-content/assets/112641072/fe615b04-add7-47fe-aa86-9aa2c24f62c9)

In addition to building an interface for your app, you can also consume the data provided by the app’s user. Considering the Google Tag Manager example, retrieving the GTM ID, for instance. In a more general sense, it is possible to retrieve some data imputed in the app interface and, based on that, allow or disallow a user action within the app.

The configuration possibilities depend on the type of data collected by the interface and what one intends to do with that information.

Based on the Google Tag Manager example above, below is a step-by-step guide on how to create an interface for your app, and how to retrieve this data for use within the app.

## Step by step

### Creating an interface

Open the `manifest.json` file.
Ensure that the appropriate [builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) are properly declared within it, as shown in the following example:

```json
 "builders": {
    "react": "3.x",
    "store": "0.x",
    "pixel": "0.x",
    "docs": "0.x"
```

Within the `settingsSchema` object, declare a JSON Schema containing the fields that meet your business needs.

Refer to the [JSON Schema documentation](http://json-schema.org/understanding-json-schema/) to build the `settingsSchema` field correctly. The JSON Schema offers a predefined model that outlines how the settings should be formatted in your app. Using it, it is possible to accept multiple field with multiple data types.

Considering the example of the Google Tag Manager interface shown previously, the `settingsSchema` object was configured as follows:

```json
  "settingsSchema": {
    "title": "Google Tag Manager",
    "type": "object",
    "bindingBounded": true,
    "properties": {
      "gtmId": {
        "title": "Google Tag Manager",
        "description": "Enter the ID (GTM-XXXX) from your Google Tag Manager",
        "type": "string"
      },
      "allowCustomHtmlTags": {
        "title": "Allow Custom HTML tags",
        "description": "Beware that using Custom HTML tags can drastically impact the store's performance",
        "type": "boolean"
      },
      "sendGA4Events": {
        "title": "Send Google Analytics 4 Events",
        "description": "When this setting is active, also send the GA4 version of the events",
        "type": "boolean"
      }
    }
  }
```

This code defines a schema for settings UI that interacts with Google Tag Manager app. Below, you can better understand the configured fields:

- `title` - App name.
- `type` - Json Schema type (this must always be completed as `object`).
- `description` (optional) - Description of the `settingsSchema` field.
- `properties` - Key-values pairs that define what will be displayed to the app users, with their own definition within this object. Possible keys for `properties` are: `title`, `description`, and `type`.

According to the JSON Schema specification, the types accepted within a property include: `”string”`, `“number”`, `“integer”`, `“boolean”`, `“object”`, `“array”` or `“null”`. It is also possible to use arrays of types (e.g. `[“string”, “number”]`) to indicate that the property accepts multiple types.

In the case of the Google Tag Manager app, the following `properties` were configured:

- `gtmId` - A string-type property that represents the Google Tag Manager ID. In the settings UI, this property is shown as a text box.
- `allowCustomHtmlTags` - A boolean-type property that determines whether custom HTML tags are allowed. In the settings UI, this property is shown as a checkbox.
- `sendGA4Events` - A boolean-type property that indicates whether to send Google Analytics 4 events. In the settings UI, this property is shown as a checkbox.

### Fetching the app settings data

On your app’s code, it is possible to retrieve the app settings in two ways:

- With a GraphQL query from the frontend to the `vtex.apps-graphql`
- On the backend, using the `getAppSettings` method from `ctx.clients.apps` client

Below is an example of each case.

#### Storefront apps

The [storefront apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io) are composed by React components that provide frontend solutions.

Below is an example of how to retrieve into your React app the app settings configured within the `settingsSchema` field.

```gql
query getSettings {
  publicSettingsForApp(app: "{vendor}.{app.name}", version: "0.x")
    @context(provider: "vtex.apps-graphql") {
    message
  }
}
```

The example above is a GraphQL query that fetches the data of a specific app, declared in the arguments of `publicSettingsForApp` field: the app and its version. Below, you can better understand the other configured fields:

- `@context(provider: “vtex.apps-graphql”)` - The context for the query. In this case, it specifies the provider as “vtex.apps-graphql”.
- `message` - The field message to be included in the query result, which is a field within the `publicSettingsForApp` object with specific filtering criteria for the app and version arguments, and it includes context information specifying the provider.

#### Backend apps

The [backend apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-service) are Node or .NET Core services that speed up connections with Storefront or Admin apps.

Below is an example of how to retrieve the app settings from a Node app:

```sh
getConfig: async (_: any, __: any, ctx: Context) => {
   const {
     clients: { apps },
     vtex: { logger },
   } = ctx

   const appId = process.env.VTEX_APP_ID

   return apps.getAppSettings(appId).catch((error) => {
     logger.error({
       message: 'getConfig-getAppSettings-error',
       error,
     })
   })
 }
```

This code is part of a GraphQL server within a VTEX IO context, where interaction with apps occurs through specific clients, such as the `apps` client used in this example. When the `getConfig` query is employed, it retrieves the app settings defined in the `manifest.json` file for that specific app.
