---
title: "Creating a Quickview using Modal Layout"
slug: "vtex-io-documentation-creating-a-quickview-using-modal-layout"
hidden: false
createdAt: "2024-11-25T14:01:22.113Z"
updatedAt: ""
excerpt: "Learn how to create a Quickview feature using the Modal Layout app."
---

In this guide, you will learn how to configure a Quickview feature in your store using the [Modal Layout](https://developers.vtex.com/docs/guides/vtex-modal-layout) app. The quickview allows users to view product details directly from the homepage or category pages without navigating to the product's detailed page.

![quickview](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-modal-layout-0.png)

>⚠ This guide is based on the [Store Theme template](https://github.com/vtex-apps/store-theme), a boilerplate with pre-set configurations for creating a store using [Store Framework](LINK). Learn more in [Available templates](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme#available-themes).

## Instructions

### Step 1 - Adding the Modal Layout app to the theme's dependencies

1. Using a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace), open your [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) app using the code editor of your choice.

2. Open the `manifest.json` file and add the Modal layout app to your theme's dependencies.

```js manifest.json
 "dependencies": {
    "vtex.modal-layout": "0.x",
  }
```

### Step 2 - Configuring the quickview trigger

To enable the Quickview feature, you need to define the trigger for the modal. The `modal-trigger#quickview` block activates the modal when the user interacts with the associated element (for example, a button). This block links the modal trigger to the `modal-layout#quickview`, which contains the layout of the modal.

1. Open the `quickview.jsonc` file located in the `store/blocks/product-summary` folder.
2. Add the `modal-trigger#quickview` block to trigger the Quickview modal. In this example, we're using `icon-expand` to represent the trigger.

```js store/blocks/product-summary/quickview.json mark=3
 "modal-trigger#quickview": {
    "children": [
      "icon-expand",
      "modal-layout#quickview"
    ],
    "props": {
      "blockClass": "quickview"
    }
  },
```

3. Add the `modal-layout#quickview` as a child of the `modal-trigger#quickview` block. This defines the layout of the modal.

```js store/blocks/product-summary/quickview.json mark=4
  "modal-trigger#quickview": {
    "children": [
      "icon-expand",
      "modal-layout#quickview"
    ],
    "props": {
      "blockClass": "quickview"
    }
  },
```

Note that the children property specifies the elements inside the trigger block. In this case, it includes `icon-expand`, which represents the visual element that users interact with to open the modal, and `modal-layout#quickview`, which defines the modal layout that will be displayed when the trigger is activated. The props section includes `blockClass`, a custom CSS class (Quickview) that allows you to style both the modal trigger and the modal itself.

### Step 3 - Customizing the Quickview modal

To customize the Quickview, you can combine Modal Layout's native blocks, such as `modal-header`, `modal-content`, and `modal-actions`, with other native components to structure and display the modal's content. The inner content may include elements such as the product's images, name, price, SKU selector, and actions like adding the product to the cart or viewing more details.

For example, you can use [Flex Layout](https://developers.vtex.com/docs/apps/vtex.flex-layout) to define the rows and columns within your modal and leverage [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary) blocks to render product information. Learn more in the guides available under [Using components](https://developers.vtex.com/docs/guides/store-framework-using-components).

> ℹ Refer to quickview.json for a complete example and consult the [Modal Layout](https://developers.vtex.com/docs/apps/vtex.modal-layout) documentation for further information on configuring and customizing your modal.

### Step 4 - Making your changes publicly available

After testing your component, deploy the new version of your Store Theme app to make it publicly available. Follow the instructions of the guide [Deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available).
