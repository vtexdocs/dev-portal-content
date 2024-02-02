# Creating an interface for your app settings

When developing a [Pixel App](https://developers.vtex.com/docs/guides/vtex-io-documentation-pixel-app), you can need to create an interface to it and integrate its data with the store. This article guides you through these processes.

Considering your [Pixel App](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developnativeintegrationswithpixelapps) is already developed, follow the steps below.


## Step by step

### Creating an interface

1. Open the `manifest.json` file. 
2. Ensure that the `pixel` [builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) is properly declared within it, as shown in the following example:

   ```json
    "builders": {
       "react": "3.x",
       "store": "0.x",
       "pixel": "0.x",
       "docs": "0.x"
   ```

3. Within the `settingsSchema` object, declare a JSON Schema containing the fields that meet your business needs. Below is an example from the Google Tag Manager Pixel App:

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

   >ℹ️ Refer to the [JSON Schema documentation](http://json-schema.org/understanding-json-schema/) to correctly build the `settingsSchema` field.

In the App Management module accessible via VTEX Admin, you can view its interface:

   ![GTM_PixelApp](https://github.com/vtexdocs/dev-portal-content/assets/112641072/1a6f8f2b-8184-423d-9e8f-346aebd5bbd8)

### Fetching the app settings data

If you need to retrieve the app settings data configurated in your app’s `manifest.json` file, you can achieve this by creating a GraphQL query and incorporating it into the React component of your Pixel app.

Below is an example of how to retrieve the app settings from your app:

   ```json
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
    },
   ```

This code is part of a GraphQL server within a VTEX IO context, where interaction with apps occurs through specific clients, such as the `apps` client used in this example. When the `getConfig` query is employed, it retrieves the app settings defined in the `manifest.json` file for that specific app. 