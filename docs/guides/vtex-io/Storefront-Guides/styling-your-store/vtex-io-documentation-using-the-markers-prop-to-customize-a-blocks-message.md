---
title: "Using the Markers prop to customize a block's message"
slug: "vtex-io-documentation-using-the-markers-prop-to-customize-a-blocks-message"
hidden: false
createdAt: "2020-06-03T16:02:45.317Z"
updatedAt: "2022-12-13T20:17:44.379Z"
---

When styling storefront components, CSS Handles and Block Classes are helpful for general styles. However, to customize specific text messages within blocks, you can use the `markers` prop. This prop lets you add unique identifiers to parts of a block’s message, making it easier to apply targeted styles.

Follow the steps below to use the `markers` prop for customizing block messages.

## Before you begin

Check if the block you want to customize supports the `markers` prop. This information can usually be found in the block’s documentation.

## Instructions

1. Open the terminal and use the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference/) to log in to your VTEX account.
2. Change to a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/).
3. Open your Store Theme using your preferred code editor and locate the block where you want to use the `markers` prop.
4. In the block's configuration, add the `markers` prop with a unique value (e.g., `discount`). For example:
    
    ```json
    "product-price-savings#summary": {
      "props": {
        "markers": [
          "discount"
        ],
      }
    },
    ```

5. Save your changes and [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) the app to your workspace.
6. Open the Admin of your workspace at (`{workspaceName}--{accountName}.myvtex.com/admin`).
7. Go to the Site Editor and select the block to which you addeed the `markers` prop.
9. In the Site Editor, wrap the message variable you want to customize with the `markers` value. For example, to style the discount percentage in a product price block, you can wrap it with the markers tag like this: `<discount>-{savingsPercentage}</discount>`. This allows you to target and style just the portion of text inside the discount tag with CSS.

    ![markers-prop-site-editor](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-the-markers-prop-to-customize-a-blocks-message-0.gif)
    
    > ℹ️ To find out which message parts you can customize, refer to the block’s documentation. It lists all message variables, like `{savingsPercentage}` in this example. You can use these variables to identify and wrap the specific text you want to style.

10. Save the changes. This assigns a unique identifier to the wrapped text, allowing you to later customize its style with CSS.
11. Access your site in the development workspace at `{workspaceName}--{accountName}.myvtex.com` and inspect the HTML element associated with the edited block’s message.
    
    ![product-price-markers-inspect](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-the-markers-prop-to-customize-a-blocks-message-1.png)
    In this example, note the message's HTML element is wrapped in a new `span` with a unique selector: `<span class="vtex-product-price-1-x-savings-discount">`.
    
13. [Use CSS Handles](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization) to apply your styles to the new class.
14. Once you are satisfied with the changes to your Store Theme, [make your theme content publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public/).
