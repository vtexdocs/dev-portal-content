---
title: "Creating an interface for your app settings"
slug: "creating-an-interface-for-your-app-settings"
hidden: false
createdAt: "2024-06-18T14:06:36.006Z"
updatedAt: "2024-06-18T14:06:36.006Z"
excerpt: "Learn how to create a user interface for your app and fetch data from it."
---

When developing a [VTEX IO app](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app), you can create an interface for accepting custom user settings. The app settings interface allows you to retrieve data provided by the user and enable or modify an app behavior based on it. The configuration possibilities depend on the type of data collected by the interface and the intended use.

This guide outlines the process of creating such an interface and using the data input by users within your app.

## Usage example

The app settings interface displays configuration forms for installed apps in the [App Store](https://help.vtex.com/en/tracks/extensions-hub--AW7klkYMh557y5IUOgzco/2LDRvGujYsumxi7IlE7CEJ). This interface is defined via the `settingsSchema` field on [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest), where an app may declare the schema of its configuration.

See the Google Tag Manager app interface in the example below, with the appropriate configuration of the `settingsSchema` field in the `manifest.json` file.

![GTM_image](https://github.com/vtexdocs/dev-portal-content/assets/112641072/d916b8da-0039-4364-b21e-a8cf8ba629dd) | ![carbon (6)](https://github.com/vtexdocs/dev-portal-content/assets/112641072/db87ac7e-7e36-4656-8ddb-b7735b5b92f4)
:--- | ---:

After building the settings interface for your app, you need to consume the data provided by the app’s user. Consider the Google Tag Manager example above retrieving the GTM ID.

Based on the given example, below is a step-by-step guide for creating an interface for your app and retrieving the data to use within the app.

## Instructions

### Step 1 - Creating the settings interface

Open your app project in any code editor of your choice and open the `manifest.json` file.

Define the `settingsSchema` object, declaring a JSON Schema containing the fields that meet your business needs. See the [JSON Schema documentation](http://json-schema.org/understanding-json-schema/) to build the `settingsSchema` field correctly.

> ℹ️ The JSON Schema offers a predefined model that outlines how the settings should be formatted in your app. Note that, according to the JSON Schema specification, the types accepted within a property include: `string`, `number`, `integer`, `boolean`, `object`, `array`, or `null`. It is also possible to use arrays of types (e.g., `[string, number]`) to indicate that the property accepts multiple types.

Considering the example of the Google Tag Manager interface previously presented, the `settingsSchema` object was configured as follows:

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
  },
```

This code defines a schema for the settings UI that interacts with the Google Tag Manager app. The configured fields are described below:

- `title`: App name shown in the app settings interface. It is recommended to use the same app name configured in the [`title` field of the manifest.json file](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest#title).
- `type`: JSON Schema type (this must always be set as `object`).
- `description` (optional): Description of the `settingsSchema` field.
- `properties`: Key-value pairs that define the fields that will be displayed to the app users, with their own definition within this object. Each defined key accepts the following `properties`: `title`, `description`, and `type`.
- `gtmId`: String-type property that represents the Google Tag Manager ID. In the settings UI, this property is shown as a text box.
- `allowCustomHtmlTags`: Boolean-type property that determines whether custom HTML tags are allowed. In the settings UI, this property is shown as a checkbox.
- `sendGA4Events`: Boolean-type property that indicates whether to send Google Analytics 4 events. In the settings UI, this property is shown as a checkbox.

### Step 2 - Retrieving and consuming the app settings data

On your app’s code, you can retrieve the app settings in two ways:

- [Frontend apps](#frontend-apps): Fetch the data using a GraphQL query.
- [Backend apps](#backend-apps): Use the `getAppSettings` method from the `ctx.clients.apps` client.

Below is an example of each case.

#### Frontend apps

1. In the `manifest.json` file, add the `vtex.apps-graphql` 3.x within the `dependencies` field.
2. In the `react` directory, create a new folder named `queries`.
3. Create a new `graphql` file (e.g., `AppSettings.graphql`) and query the settings options as in the following example.

```gql
query getSettings {
  appSettings(app: "{vendor}.{app.name}", version: "0.x")
    @context(provider: "vtex.apps-graphql") {
    message
  }
}
```

>⚠ Replace `vendor`, `app.name`, and `0.x` with values based on your scenario.

The example above is a GraphQL query that fetches the data of a specific app declared in the arguments of `publicSettingsForApp` field: the app and its version. The configured fields are described below:

- `@context(provider: “vtex.apps-graphql”)`: The context for the query. In this case, it must be configured as “vtex.apps-graphql”.
- `message`: The message field to be included in the query result, which is a field within the `publicSettingsForApp` object. Note that the message may vary depending on the app's settingsSchema.

This query will return an object like the one below:

```json
{
  "data": {
    "publicSettingsForApp": {
      "message": "{\"maxNumberOfItemsToCompare\":2}"
    }
  }
}
```

>⚠ Please be aware that only settings labeled with `public` `access` in the `settingsSchema` will be returned.

4. Open the `tsx` file of the React component that will consume this information (e.g., `ProductComparisonContext.tsx`) and import the GraphQL query:

```tsx
import AppSettings from './queries/AppSettings.graphql'
```

5. Parse and use the defined query (e.g., `AppSettings`) value based on your needs. Check the example below:

```tsx
const { data: appSettingsData } = useQuery(AppSettings, {
    variables: {
      // eslint-disable-next-line no-undef
      version: process.env.VTEX_APP_VERSION,
    },
    ssr: false,
  })

  useEffect(() => {
    const appSettings = JSON.parse(
      pathOr(`{}`, ['publicSettingsForApp', 'message'], appSettingsData)
    )

    dispatch({
      type: 'SET_MAX_LIMIT',
      args: {
        maxLimit: pathOr(
          MAX_ITEMS_TO_COMPARE,
          ['maxNumberOfItemsToCompare'],
          appSettings
        ),
      },
    })
  }, [appSettingsData])
```

The code above interacts with an API through a GraphQL query, which is managed by the `useQuery` hook, to fetch the app settings. It then parses and updates the app’s state with these settings using a `useEffect` hook whenever the settings data changes.

#### Backend apps

1. Open your `node` app in any code editor of your choice.
2. Declare a new function (e.g., `getConfig`) and use the `getAppSettings` method to retrieve and return the app settings data. Consider the example below:

```ts
export async function getConfig: async (_: any, __: any, ctx: Context) => {
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
 },
```

The `getConfig` function returns a promise as it fetches the app settings and handles errors. It retrieves an app ID from environment variables, uses it to request settings, and logs any errors that occur.

3. Import the defined function and consume it based on your needs.
