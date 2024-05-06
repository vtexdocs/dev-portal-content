---
title: "Store builder"
slug: "vtex-io-documentation-store-builder"
excerpt: "Learn how to use the VTEX IO Store builder."
hidden: false
createdAt: "2024-05-02T09:33:00.000Z"
updatedAt: "2024-05-06T17:15:00.000Z"
category: "App Development"
---

The `store` builder enables the development of [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io) storefronts, empowering the development of both [storefront components](https://developers.vtex.com/docs/guides/getting-started-3) and unique store themes. The main use cases of the `store` builder include:

- **Frontend apps**: When used alongside the [`react` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder), the `store` builder allows integrating a [frontend component](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io) with Site Editor. It enables mapping a React component to a block, grouping store blocks, and defining route handling within a component.
- **Store Theme apps**: Defines block usage and store routes.

>ℹ️ Note that if your store uses a different [storefront solution](https://developers.vtex.com/docs/storefront-development), the `store` builder is not necessary, as this builder is specifically designed for developing apps for Store Framework.

This builder interprets and validates the [blocks](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition#blocks), [interfaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-interface), and [routes](https://developers.vtex.com/docs/guides/vtex-io-documentation-routes) within the `/store` folder.

With the `store` builder, you can use VTEX IO capabilities to quickly build store components and themes that can be reused across ecommerce stores and interact seamlessly with VTEX APIs and existing components.

## Folder structure

An app that uses the `store` builder has a folder named `/store` in its root directory. The directory structure may vary depending on the specific project settings.

The basic structure of a `/store` folder is composed of the following files, as you can see in the [store repository](https://github.com/vtex-apps/store/tree/master/store):

```txt
store
 ┣ 📄 blocks.json
 ┣ 📄 contentSchemas.json
 ┣ 📄 interfaces.json
 ┗ 📄 routes.json
```

- `blocks.json`: Declares all blocks that exist in your project. Note that blocks can be defined both in the `store/blocks.json` file or in any number of `.json` files organized within the `store/blocks` directory, using an arbitrary directory structure.
- `contentSchemas.json`: Follows the [JSON Schema](https://json-schema.org/) format.
- `interfaces.json`: Establishes a relationship between blocks and React components. Learn more in [Interfaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-interface).
- `routes.json`: Creates custom routes in your app, mapping page templates to the path they will respond to. When developing store themes, see [Creating a custom page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) for more information.

## Usage

To use the `store` builder in your app, follow these steps:

Add the `store` builder to your app’s builder list in the `manifest.json` file, as follows:

```json
  "builders": {
      "store": "3.x"
  }
```

In the root directory of your app, create a `/store` folder.

>ℹ️ If you are developing a store theme with Store Framework from the [Store Theme boilerplate](https://github.com/vtex-apps/store-theme), the `store` builder is natively installed, along with the `/store` folder.

## Use case examples

Every store theme developed using Store Framework requires the `store` builder. Moreover, the `store` builder is also used in the development of any [Store Framework component](https://developers.vtex.com/docs/vtex-io-apps).

Below, you can check both scenarios.

### Store theme

When [creating a Store Framework storefront project](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-settingyourstoretheme), the first step is installing the [Store Theme boilerplate](https://github.com/vtex-apps/store-theme). This process automatically installs the `store` builder in the `manifest.json` file.

Next, you can check the file structure of the Store Theme app:

```txt
store
 ┣ 📂 blocks
      ┗ 📂 footer
      ┗ 📂 header
      ┗ 📂 home
      ┗ 📂 pdp
      ┗ 📂 product-summary
      ┗ 📄about-us.json
      ┗ 📄contact.jsonc
      ┗ 📄faq.jsonc
      ┗ 📄minicart.jsonc
      ┗ 📄orderplaced.jsonc
      ┗ 📄product-price.jsonc
      ┗ 📄search.jsonc
 ┣ 📄blocks.json
 ┣ 📄routes.json
```

- The `blocks` folder contains the [Store Components](https://developers.vtex.com/docs/guides/store-components) installed by default, such as `footer`, `header`, `home`, `minicart`, `search`, among others.
- The `blocks.json` file defines the organization and structure of different blocks that compose the storefront project.
- The `routes.json` file defines custom routes for different sections of the storefront project, such as `store.custom#about-us`, `store.custom#faq`, and `store.custom#contact-us`, providing the path where the content related to that route can be accessed.

For more information on building a store theme with Store Framework, check the [Storefront](https://developers.vtex.com/docs/guides/getting-started-3) documentation.

### Frontend components

The `store` builder is also necessary when developing a frontend app for use within a Store Theme app. Typically, such an app also leverages the [`react` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder). For example, consider the [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary) app.

The Product Summary app summarizes product information, including its name, price, and image.

Next, you can check the structure of the `store` folder for the Product Summary app:

```txt
store
 ┣ 📄 blocks.json
 ┣ 📄 contentSchemas.json
 ┣ 📄 interfaces.json
```

Within each of these files, there is a JSON structure, as follows:

- `blocks.json`: Outlines the composition of a product summary component, specifying how different elements, such as image, name, attachments, price, and buy button should be arranged within various layouts (shelf and flex).
- `contentSchemas.json`: Defines the properties and settings for two types of components related to product summaries, “ProductSummary” and “ProductSummaryList”. This includes specifying text labels, badge information, and positional details for integration with Site Editor.
- `inferfaces.json`: Maps a React component from the [`react` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder) to a block definition.
