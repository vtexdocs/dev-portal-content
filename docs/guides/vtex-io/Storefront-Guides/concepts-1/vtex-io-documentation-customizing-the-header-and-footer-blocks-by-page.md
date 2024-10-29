---
title: "Customizing the Header and Footer blocks by page"
slug: "vtex-io-documentation-customizing-the-header-and-footer-blocks-by-page"
excerpt: Learn how to customize the header and footer blocks for specific pages within your store.
hidden: false
createdAt: "2020-06-03T16:02:44.275Z"
updatedAt: "2022-12-13T20:17:44.048Z"
---

The Header and Footer blocks are essential for enhancing navigation and ensuring consistency across your online store, including the homepage, product listings, and checkout. These blocks are typically defined once in the `blocks.jsonc` file and serve as default elements for all other templates in the Store Framework.

However, you may want to customize these blocks for specific pages. For instance, you might wish to display a unique Header on your homepage while retaining the default Header for the Order Placed page, or even remove the Footer from product pages entirely to declutter the user interface.

This guide outlines how to customize these blocks for specific pages within your store.

## Instructions

1. Open your Store Theme project in your preferred code editor.
2. Find the template you want to customize within the `blocks.jsonc` file. 
3. [Replace](#replacing-the-header-and-footer-blocks) or [remove](#removing-the-header-and-footer-blocks) the Header and Footer blocks according to your needs.
4. Save your changes and [link your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to see the new configurations reflected on the desired page.

### Replacing the header and footer blocks

To customize the Header and Footer for a particular template, locate the desired template in the `blocks.jsonc` file and add the following code to override the default blocks:

    ```json blocks.jsonc
    {
      "store.{templateName}": {
        "parent": { 
          "header": "{headerBlock}", 
          "footer": "{footerBlock}"
        }
      }
    }
    ```
    
    > ℹ Replace `{headerBlock}` and `{footerBlock}` with the actual block names you want to use. Also, replace `{templateName}` with a valid theme template, such as `product`, `search#category`, and `custom`.

If you wish to override only one block, keep the parent structure and specify the block you want to change. For instance, to customize just the Header, use the following code:

```json blocks.jsonc
{
  "store.{templateName}": {
    "parent": { 
      "header": "{headerBlock}"
    }
  }
}
```

You can then configure the Header and Footer blocks based on your specific requirements for the selected template. 

Here’s an example configuration that customizes the Header for a product page:

```json blocks.jsonc
{
  "store.product": {
    "parent": { 
      "header": "header#product"
    }
  },
  "header#product": {
    "blocks": [
      "header-layout.desktop",
      "header-layout.mobile"
    ]
  },
  "header-layout.desktop": {
    "children": [
      "header-row#1-desktop"
    ]
  },
  "header-row#1-desktop": {
    "children": ["telemarketing"],
    "props": {
      "fullWidth": true
    }
  }
}
```

> For further customization, refer to the [Header](https://developers.vtex.com/docs/apps/vtex.store-header/) and [Footer](https://developers.vtex.com/docs/apps/vtex.store-footer/) documentation. 

### Removing the header and footer blocks

If you prefer to remove the Header and Footer blocks from a specific template, you can declare the blocks with empty `children` arrays:

```json blocks.jsonc
{
  "store.custom#noheaderfooter": {
    "parent": {
      "header": "header#empty",
      "footer": "footer#empty"
    },
  },
  "header#empty": {
    "blocks": [
      "header-layout.desktop#empty",
      "header-layout.mobile#empty"
    ]
  },
  "header-layout.desktop#empty": {
    "children": []
  },
  "header-layout.mobile#empty": {
    "children": []
  },
  "footer#empty": {
    "blocks": [
      "footer-layout.desktop#empty",
      "footer-layout.mobile#empty"
    ]
  },
  "footer-layout.desktop#empty": {
    "children": []
  },
  "footer-layout.mobile#empty": {
    "children": []
  }
}
```
