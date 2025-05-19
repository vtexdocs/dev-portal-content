---
title: "Creating an interface for your app settings"
slug: "creating-an-interface-for-your-app-settings"
hidden: false
createdAt: "2024-06-18T14:06:36.006Z"
updatedAt: "2025-05-19T15:14:31.250Z"
excerpt: "Learn how to create a user interface for your app and fetch data from it."
---

When developing a [VTEX IO app](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app), you can create an interface for accepting custom user settings. The app settings interface allows you to retrieve data provided by the user and enable or modify an app's behavior based on it. The configuration possibilities depend on the type of data collected by the interface and the intended use.

This guide outlines the process of creating such an interface and using the data input by users within your app.

## Usage example

The app settings interface displays configuration forms for installed apps in the [App Store](https://help.vtex.com/en/tracks/extensions-hub--AW7klkYMh557y5IUOgzco/2LDRvGujYsumxi7IlE7CEJ). This interface is defined via the `settingsSchema` field on [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest), where you declare the schema of your app’s configuration.

Below is an example of the Google Tag Manager app interface and its corresponding `settingsSchema`configuration:

<Tabs items={[Interface, settingsSchema]} defaultIndex="0">
  <Tab>
  <img src="https://github.com/vtexdocs/dev-portal-content/assets/112641072/d916b8da-0039-4364-b21e-a8cf8ba629dd" alt="GTM_image" />
  </Tab>
  
  <Tab>
```json manifest.json
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
  </Tab>
</Tabs>


After building your app's settings interface, you need to consume the data provided by the app’s user. Consider the Google Tag Manager example above, retrieving the GTM ID.

Based on the given example, below is a step-by-step guide for creating an interface for your app and retrieving the data to use within the app.
## Instructions
### Step 1 - Creating the settings interface

To create the app settings interface, define the `settingsSchema` object in its `manifest.json` file.

This object declares a JSON Schema containing the fields that meet your business needs. See the [JSON Schema documentation](http://json-schema.org/understanding-json-schema/) to build the `settingsSchema` field correctly.

> ℹ️ The JSON Schema offers a predefined model that outlines how the settings should be formatted in your app. Note that, according to the JSON Schema specification, the types accepted within a property include: `string`, `number`, `integer`, `boolean`, `object`, `array`, or `null`. It is also possible to use arrays of types (for example, `[string, number]`) to indicate that the property accepts multiple types.

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

In your app’s code, you can retrieve the app settings in two ways:

- [Frontend apps](#frontend-apps): Use a GraphQL query to fetch app settings.
- [Backend apps](#backend-apps): Use the `getAppSettings` method from the `ctx.clients.apps` client.

Below is an example of each case.

>⚠ Make sure your app has the necessary permissions to communicate with the frontend or backend app. 
Without proper permissions, your store won’t be able to share data with the solution. Learn more in [Policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies).

#### Frontend apps

1. In the `manifest.json` file, add the `vtex.apps-graphql@3.x` within the `dependencies` field.
2. In the `react` directory, create a new folder named `queries`.
3. Create a new `graphql` file (for example, `AppSettings.graphql`) and query the settings options as in the following example.

```gql
query getSettings {
  publicSettingsForApp(app: "{vendor}.{app.name}", version: "0.x")
    @context(provider: "vtex.apps-graphql") {
    message
  }
}
```

>⚠ Replace `vendor`, `app.name`, and `0.x` with values based on your scenario. In the case of Google Tag Manager app, the `app` value is `vtex.google-tag-manager`, and the `version` value is `1.x`.

The example above is a GraphQL query that fetches the data of a specific app declared in the arguments of `publicSettingsForApp` field: the app and its version. The configured fields are described below:

- `@context(provider: "vtex.apps-graphql")`: The context for the query. In this case, it must be configured as "vtex.apps-graphql".
- `message`: The message field to be included in the query result, which is a field within the `publicSettingsForApp` object. The message may vary depending on the app's settingsSchema.

This query will return an object like the one below:

```json
{
  "data": {
    "publicSettingsForApp": {
      "message": "{\"gtmId\": \"GTM-1234\"}"
    }
  }
}
```

4. Open the `tsx` file of the React component that will consume this information and import the GraphQL query:

```tsx
import AppSettings from './queries/AppSettings.graphql'
```

5. Parse and use the defined query value (for example, `AppSettings`) based on your needs. Check the example below:

```tsx
  const { data: appSettingsData } = useQuery(AppSettings, {
    variables: { version: process.env.VTEX_APP_VERSION },
    ssr: false,
  });

  useEffect(() => {
    if (appSettingsData) {
      const { gtmId } = JSON.parse(appSettingsData.publicSettingsForApp?.message || '{}');
      if (gtmId) {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
        const script = document.createElement('script');
        script.src = `https://www.googletagmanager.com/gtm.js?id=${gtmId}`;
        document.head.appendChild(script);
      }
    }
  }, [appSettingsData]);
```

The code above interacts with an API through a GraphQL query, which is managed by the `useQuery` hook, to fetch the app settings. When the data is retrieved, a `useEffect` hook parses the settings, extracts the `gtmId`, and dynamically initializes GTM by injecting its script into the document if the `gtmId` is available.

#### Backend apps

1. Open your `node` app in any code editor of your choice.
2. Declare a new function (for example, `getConfig`) and use the `getAppSettings` method from the `apps` client to retrieve and return the app settings data. Consider the example below:

```ts
export const getConfig = async (_: any, __: any, ctx: Context) => {
  const {
    clients: { apps },
    vtex: { logger },
  } = ctx;

  const appId = process.env.VTEX_APP_ID;

  try {
    const settings = await apps.getAppSettings(appId);
    return settings;
  } catch (error) {
    logger.error({
      message: 'getConfig-getAppSettings-error',
      error,
    });
  }
};
```

The `getConfig` function returns a promise as it fetches the app settings and handles errors. It retrieves an app ID from environment variables, uses it to request settings, and logs any errors that occur.

3. Import the defined function and consume it based on your needs. For example, you can use it in a resolver, middleware, or any other part of your backend app.
