---
title: "Overriding native app blocks"
slug: "vtex-io-documentation-overriding-native-app-blocks"
hidden: false
createdAt: "2025-05-06T15:06:15.403Z"
updatedAt: "2025-05-29T14:27:44.625Z"
excerpt: "Discover how to override the blocks of your custom VTEX IO app."
---

In this guide, you will learn how to override the blocks provided by a native VTEX IO app with a custom app by configuring the `store/plugins.json` file. This approach allows custom apps to modify existing Store Framework blocks without changing the original app's code.

This is especially useful when you need to customize a page or component while maintaining compatibility with future updates of the original app. Follow the steps below to ensure your custom app works properly with existing dependencies and block schemas.

## Before you begin

<Steps>

### Develop your VTEX IO custom app

Start the development of a new VTEX IO app by running the `vtex init` command and choosing the appropriate template. Learn more in the tutorial [Storefront apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io).

>⚠️ Use a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) to develop you custom app.

### Check the builders

Configure the following builders in the app's `manifest.json` file:

- [`store builder`](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder): Enables the development of Store Framework storefronts.
- [`react builder`](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder): Used to develop apps with [React](https://react.dev/) when your project requires customized frontend solutions.

</Steps>

## Instructions

### Step 1 - Managing dependencies

Add the corresponding native VTEX IO app as a dependency in the custom app's `manifest.json` file.

```json manifest.json/dependencies
  "dependencies": {
    "vtex.original-app": "1.x"
  }
```

### Step 2 - Defining the app's schema

1. In your app's root directory, create the `store` folder.
2. In the `store` folder, create the `interfaces.json` file and define the app's schema by following the original native app. For example, if the native app block has `example-child` as `required`, the new block must also declare it:

  ```json
  "new-block": {
   "component": "NewBlock"
   "required": ['example-child']
  }
  ```

### Step 3 - Configuring plugins

In the `store` folder, create the `plugins.json` file within the key-value pairs of the blocks you want to override.

  ```json store/plugins.json
  {
    "original-block": "new-block"
  }
  ```

### Step 4 - Customizing your app code

Declare the React component for your new block. In the example below, we added the greeting **HELLO WORLD**.

```js NewBlock.js
import React from 'react'

const NewBlock: React.FC = () => {
  return <h1>HELLO WORLD</h1>
}

export default NewBlock
```

### Step 5 - Testing your custom app

[Link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) in the development workspace you're working in to see the changes.

Based on the given example, you'll see the following page when placing an order:

![overriding-block](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-11304-Overriding-blocks/docs/guides/vtex-io/Storefront-Guides/images/overriding-blocks.png)

### Step 6 - Making your app publicly available

Once you finish developing and testing your custom app, deploy it to make it available in the live store. Learn how in the guide [Deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available).
