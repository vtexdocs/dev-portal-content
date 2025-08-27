---
title: "Using CSS handles for store customizations"
excerpt: "Learn how to customize your storefront using CSS handles."
slug: "vtex-io-documentation-using-css-handles-for-store-customization"
hidden: false
createdAt: "2020-06-03T16:02:45.024Z"
updatedAt: "2025-07-15T16:34:53.615Z"
---

In this guide, you’ll learn how to customize your storefront using CSS handles. These unique identifiers assigned to HTML elements allow you to target and add CSS classes to a component within your [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme).

CSS handles can overwrite a storefront's default styles, allowing for independent customization of specific blocks within a Store Theme. For example, consider you want to customize the `menu-item` blocks of the [Menu](https://developers.vtex.com/docs/apps/vtex.menu) component. You can apply a [general customization](#applying-a-general-customization) or [customize a single block](#customizing-a-single-block).

## Instructions

### Identifying CSS handles

1. Open your browser and go to your store’s development workspace using this URL: `https://{workspace}--{account}.myvtex.com?__inspect`. Replace the values inside curly braces with your specific workspace and account names.

>⚠️ Always use a development workspace and make sure your store domain is under `myvtex.com`.

2. Hover your mouse over the page element you want to customize. A box will appear displaying its available CSS handles (names starting with `.`), CSS file names, and related information.

![css-handles-inspect](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-0.png)

3. Check the CSS handles table in the documentation of the app or block that renders the HTML element. This allows you to confirm whether the inspected handle is valid and if the customization requires another add-on, such as the HTML element attribute.

>⚠️ If a handle requires an HTML element attribute for customization, inspect the page again using your browser’s developer tools instead of the `?__inspect` option. Look for the desired HTML element and copy its associated attribute for the upcoming customization.

### Applying a general customization

Follow the steps below to apply a style that affects every block instance:

1. Open your Store Theme code using the code editor of your choice and navigate to the `css` folder.
2. In the `css` folder, create a new CSS file named after the component you’re targeting. For example, `vtex.menu.css`.
3. In the new file, use one of the listed CSS handles and customize its properties. For example:

```css
.menuItem {  
    background: rgba(0, 0, 0, 0.2);
    margin: 5px;
    border-radius: 5px;
}
```

>⚠️ If the handle requires an add-on, such as the HTML element attribute or a handle modifier, add it next to the handle name, following this format: `{cssHandleName}--{addon)`.

4. [Link your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to see the changes. Once linked, the new style applies to all `menu-item` blocks in the workspace you’re working on.

![css handles customization applied to the menuItem](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-1.png)

### Customizing a single block

To customize a single, specific block without affecting others of the same type, use the  `blockClass` property, which serves as the block’s unique identifier for customization:

1. In the `json` file where your target block is declared, add the prop `blockClass` to the element you want to customize. Assign any unique name as its value. For example:

```json mark=4
"menu-item#your-item": {
  "props": {
    ...,
    "blockClass": "header"
  },
  ...
}
```

2. Save the file to update the workspace you’re working on.
3. Inspect the element by following the instructions on [Identifying CSS handles](#identifying-css-handles). You’ll see a new, more specific CSS handle composed of the original handle and the `blockClass` value you provided.

![css handles with block class](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-2.png)

4. In your CSS file, you can now use this new class (for example: `.menu-Item--header`) to target only the block with that specific `blockClass`.

![specific menu items with css handles applied using blockClass](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-3.png)

## Best practices

CSS selectors are commonly used for customization, but this depends on the HTML structure. If you change the HTML, it can affect your customizations. To standardize CSS customization and avoid any potential breakdown in layout, we recommend only using CSS handles for store customizations.

Customization using CSS selectors is mostly deprecated. The following selectors are the only ones allowed for store customization:

- Class selectors (example: `.foo`)
- Pseudo-selectors `:hover`, `:visited`, `:active`, `:disabled`, `:focus`, `:local`, `:empty`, and `:target`
- `:not()`
- `:first-child` and `:last-child`
- `:nth-child(even)`, `:nth-child(odd)`, and `:nth-child(2n)` (or any other step like `4n`, `5n`, and so on.)
- All pseudo-elements, such as  `::before`, `::after`, and `::placeholder`
- Space combinator (example: `.foo .bar`)
- `[data-...]`
- `:global(vtex-{AppName}-{AppVersion}-{ComponentName})` for selecting elements that come from different apps
- Media queries, such as `@media (max-width: 768px)` (responsive override for screens up to 768px wide) and `@media (prefers-reduced-motion: reduce)` (remove transitions if user prefers reduced motion).

>⚠️ CSS selectors that are not included in this list, such as `:nth-child(2)`, `foo > bar`, and `[alt="bar"]`, aren’t supported. Using them can cause issues like app linking failure.
