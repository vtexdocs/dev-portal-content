---
title: "5. Defining styles"
slug: "vtex-io-documentation-5-definingstyles"
hidden: false
createdAt: "2020-08-11T07:03:18.383Z"
updatedAt: "2022-12-13T20:17:44.175Z"
category: "Storefront Development"
excerpt: "Learn how to set specific styles for your store components to enhance your store's user experience."
seeAlso:
 - "/docs/guides/vtex-io-documentation-6-buildingyourownstoretheme"
---

Your website’s visual style is fundamental to building your store’s identity.

Once you understand what blocks and templates are and how they render interface components, it's time to learn how to customize them.

The Store Theme will allow you to:

- Set a default style for all your store components.
- Set a specific style for a store component type or for a single component from all available in your store.

## Setting a default style for all store components

To set the default visual style for your entire store, you can utilize the `style.json` file located in the `style` folder of the Store Theme app. This single file allows you to customize the appearance of your store by modifying the default definitions declared within it. With this approach, you can avoid the need to customize individual components on each page.

For example, we can set the default theme background color to blue by changing the `semanticColors` block’s `base` property:

```json
"semanticColors": {
  "background": {
    "base": "#00BFFF",
    "base--inverted": "#03044e",
    "action-primary": "#0F3E99",
    "action-secondary": "#eef3f7",
    "emphasis": "#f71963",
    "disabled": "#f2f4f5",
    "success": "#8bc34a",
    "success--faded": "#eafce3",
    "danger": "#ff4c4c",
    "danger--faded": "#ffe6e6",
    "warning": "#ffb100",
    "warning--faded": "#fff6e0",
    "muted-1": "#727273",
    "muted-2": "#979899",
    "muted-3": "#cacbcc",
    "muted-4": "#e3e4e6",
    "muted-5": "#f2f4f5"
  },
}
```

For detailed instructions on customizing your theme, refer to the [VTEX Styleguide](https://styleguide.vtex.com/#/Styles), a comprehensive CSS framework that provides guidelines for defining component styles. It includes a detailed explanation of the `styles.json` file structure to assist you in your customization efforts.

## Setting a specific style for a component type or a single component

The `style.json` file allows for more generic customization of your store's visual style and can be useful in most scenarios.

However, if you desire a more distinctive store identity, where certain components have unique styles different from the default theme, consider the following scenario: suppose your store primarily uses blue as its main color, but you want the text components (rendered by `rich-text` blocks) to appear in red. Now, let's say you only want one specific text component to be red while the rest remain in the default blue color. To achieve such advanced customization, you can override the default style defined in `styles.json` with CSS handles and use the `blockClass` prop for the last given example.

If you are interested in applying advanced customization in your store style, access the [**Using CSS Handles for store customization**](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization/) guide for more instructions.
