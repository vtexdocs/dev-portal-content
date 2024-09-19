---
title: "Using CSS handles for store customizations"
excerpt: "Learn how to customize your storefront using CSS handles."
slug: "vtex-io-documentation-using-css-handles-for-store-customization"
hidden: false
createdAt: "2020-06-03T16:02:45.024Z"
updatedAt: "2022-12-13T20:17:44.398Z"
---

This guide will teach you how to customize your storefront using CSS handles. CSS handles are unique identifiers assigned to HTML elements. They can be used in your Store Theme to target and add CSS classes to a component, allowing you to personalize your storefront according to your preferences.

## Instructions

1. Access the following URL: `https://{workspace}--{account}.myvtex.com?__inspect`, replacing the values between curly braces according to your scenario. Please note that you must use a development workspace rather than a production one, and the store domain must be under `myvtex.com`.

2. Hover over the element you want to customize. It should display its available CSS handles in a box (the big names beginning with `.`), along with their respective CSS file names and other information.

![css-handles-inspect](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-0.png)

3. Check the CSS handles table in the documentation of the app/block that renders the HTML element. This will allow you to confirm whether the inspected handle is valid and also if the customization requires another add-on, such as the HTML element attribute.

> ⚠️ If after checking the CSS handles table, you notice that the desired handle needs to use the attribute of the HTML element that will be customized, inspect the page again, this time using your browser and not the `?__inspect` option. After inspecting the page, look for the desired HTML element and copy the attribute linked to it that will be used in the upcoming customization.

4. Open the Store Theme code using the code editor of your choice. Then, create a file inside the `css` folder named after the text displayed below the desired handle. Following the example above, we would have `vtex.menu.css`.

5. In the new file, use one of the CSS handles listed and customize its properties. For example:

```css
.menuItem {  
    background: rgba(0, 0, 0, 0.2);
    margin: 5px;
    border-radius: 5px;
}
```

> ⚠️ If the handle requires an add-on, such as the HTML element attribute or a handle modifier, add it next to the handle name, following this format: `{cssHandleName}--{addon)`.

Once your app is linked and the changes are saved, the new customization should immediately be reflected in your workspace.

![css handles customization applied to the menuItem](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-1.png)

As demonstrated, CSS handles can be used to overwrite the default styles of a storefront, allowing for independent customization of specific blocks within a Store Theme. Note that the change above was applied universally to all `menu-item` blocks.

### Customizing a single block

To independently customize a single block (e.g., `menu-item`), you should use the  `blockClass` property. When passed in a block, the `blockClass` value serves as the block's unique identifier for customization.

1. In the `json` file where your block is declared, add the prop `blockClass` to the element you want to customize, with any name as a value.

For example:

```json
"menu-item#your-item": {
  "props": {
    ...,
    "blockClass": "header"
  },
  ...
}
```

Once you have saved and updated your workspace, inspecting the element should display an additional CSS handle in addition to the default one. The element will be displayed as follows, showcasing both the default CSS handle and the newly added one:

![css handles with block class](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-2.png)

After that, you can use the class `.menuItem--header` to specifically target the elements that have this `blockClass`.

![specific menu items with css handles applied using blockClass](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-3.png)

## Best practices

While it is common to encounter scenarios where CSS selectors are utilized for customization, it is important to note that such customization relies on the HTML hierarchy. Consequently, any changes to the HTML structure may disrupt the desired customization. Therefore, to standardize CSS customization and avoid any potential breakdown in layout, we recommend making store customizations exclusively using CSS handles.

Customization using CSS selectors is mostly deprecated. Only the following CSS selectors are still allowed for store customization:

- Class selectors (e.g. `.foo`)
- Pseudo-selectors `:hover`, `:visited`, `:active`, `:disabled`, `:focus`, `:local`, `:empty`, and `:target`
- `:not()`
- `:first-child` and `:last-child`
- `:nth-child(even)`, `:nth-child(odd)`, and `:nth-child(2n)` (or any other step like `4n`, `5n`, and so on.)
- All pseudo-elements, such as  `::before`, `::after`, and `::placeholder`
- Space combinator (e.g. `.foo .bar`)
- `[data-...]`
- `:global(vtex-{AppName}-{AppVersion}-{ComponentName})` for selection of elements that come from different apps

> ⚠️ CSS selectors that are not included in this list, such as `:nth-child(2)`, `foo > bar`, and `[alt="bar"]`, are not supported by the platform. Therefore, processes like [linking an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) will fail if unlisted selectors are used.
