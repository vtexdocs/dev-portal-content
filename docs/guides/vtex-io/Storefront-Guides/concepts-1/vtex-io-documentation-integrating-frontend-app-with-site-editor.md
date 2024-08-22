---
title: "Integrating a frontend app with Site Editor"
slug: "vtex-io-documentation-integrating-frontend-app-with-site-editor"
hidden: false
createdAt: "2024-08-07T15:11:18.590Z"
updatedAt: ""
excerpt: "Learn how to integrate a frontend app with Site Editor."
seeAlso:
  - "/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io"
  - "/docs/guides/vtex-io-documentation-developing-custom-storefront-components"
  - "docs/guides/vtex-io-documentation-making-a-custom-component-available-in-site-editor"
---

Once you have developed a [frontend app](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io) using [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io), the next step is to declare this app in the [dependencies](https://developers.vtex.com/docs/guides/vtex-io-documentation-dependencies) of the Store Theme app. This step is essential to make your custom frontend app available in [Site Editor](https://developers.vtex.com/docs/guides/vtex-io-documentation-site-editor).

In this guide, you will learn how to integrate your custom frontend app with Site Editor.

## Before you begin

- Create your frontend app following the guide [Creating the new app](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-creating-the-new-app).
- Develop a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) for your store, following the [Storefront](https://developers.vtex.com/docs/guides/getting-started-3) guide.
- Check if your Store Theme has the [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) properly installed. You must have at least the following builders configured:
  - [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder): Enables the development of Store Framework storefronts.
  - [react builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder): Used to develop apps with [React](https://react.dev/) when your project requires customized frontend solutions.

## Instructions

### Step 1 - Declaring your app in Store Theme dependencies

Follow the steps below to update your Store Theme dependencies with the name and version of your frontend app.

1. Open the Store Theme app folder in your local files using the code editor of your choice, such as Visual Studio Code.
2. In the Store Theme `manifest.json` file, add your app to `dependencies`, following this pattern: `"{accountName}.{appName}": "{appVersion}"`. See the example below:

   ```js
   "dependencies": {
     "{accountName}.{appName}": "{appVersion}",
     "vtex.store": "2.x",
     "vtex.store-header": "2.x",
     "vtex.product-summary": "2.x",
     "vtex.store-footer": "2.x",
     "vtex.store-components": "3.x",
     "vtex.styleguide": "9.x",
     "vtex.slider": "0.x",
     "vtex.carousel": "2.x",
   ...
   }
   ```

### Step 2 - Using a component of your frontend app within a store page

Consider your frontend app has a component named `CustomComponent`, which is declared in a block [interface](https://developers.vtex.com/docs/guides/vtex-io-documentation-interface) as `custom-component`:

```js frontend-app/store/interfaces.json
{
  "custom-component": {
    "component": "CustomComponent"
  }
}
```

To use this component on the store’s main page, for example, declare the `custom-component` block within the `home` block:

```js store-theme/store/blocks/home/home.jsonc
{
  "store.home": {
    "blocks": ["custom-component"]
  }
}
```

### Step 3 - Making your component available in Site Editor

By [linking](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) the Store Theme app, your component will be available to visualize and test in Site Editor within the corresponding [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace).

> ℹ️ Learn how to create a custom component within your Store Theme app and make it editable directly in Site Editor by following the guide [Making a custom component available in Site Editor](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-a-custom-component-available-in-site-editor).
