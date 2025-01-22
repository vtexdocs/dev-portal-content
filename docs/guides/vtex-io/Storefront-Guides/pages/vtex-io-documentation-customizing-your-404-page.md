---
title: "Customizing your 404 page"
slug: "vtex-io-documentation-customizing-your-404-page"
hidden: false
createdAt: "2025-01-22T14:11:43.125Z"
updatedAt: ""
excerpt: ""
seeAlso:
  - "/docs/guides/vtex-io-documentation-enabling-404-pages-for-invalid-single-segment-paths"
---

This guide provides instructions for customizing your store's 404 pages using the VTEX IO Store Framework. With flexible blocks and configurations, you can create a custom error page that aligns with your brand and helps users seamlessly navigate back to key areas of your site.

## Instructions

To customize 404 pages, follow the steps below:

1. Open the terminal and [switch to a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/).
2. Open your [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) using your preferred code editor.
3. In the product or search template (`store.product` or `store.search`), add and configure the `store.not-found#product` or `store.not-found#search` block, respectively. See below an example of a `store.not-found#product` configuration for a product template:
    
    ```json
    "store.not-found#product": {
      "blocks": ["rich-text#not-found"]
    },
    "rich-text#not-found": {
      "props": {
        "textAlignment": "CENTER",
        "textPosition": "CENTER",
        "text": "**PAGE NOT FOUND**",
        "font": "t-heading-1"
      }
    }
    ```
    
  > ℹ The `store.not-found` blocks will only be rendered when the server returns a 404 error. The child block will be displayed to users in such cases.

4. Save your changes and run `vtex link` in your terminal to preview the updated 404 page:

  ![not-found-block](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-enabling-404-pages-1.png)

5. Once you're satisfied with the changes, [publish your new theme version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public/).