---
title: "Using CSS handles for store customizations"
slug: "vtex-io-documentation-using-css-handles-for-store-customization"
hidden: false
createdAt: "2020-06-03T16:02:45.024Z"
updatedAt: "2022-12-13T20:17:44.398Z"
---


This guide will teach you how to customize your storefront using CSS handles. CSS handles are unique identifiers assigned to HTML elements. They can be used in your store theme to target and add CSS classes to a component, allowing you to personalize your storefront according to your preferences.


## Step by step

1. While viewing your workspace on your browser, add `?__inspect` at the end of the page URL and press enter. For example, `https://yourworkspace--youraccount.myvtex.com?__inspect`. Note that the workspace must be a development workspace rather than a production one, and it must be under the domain `myvtex.com`.

2. Hover over the element you want to customize. It should display its available CSS handles in a box (the big names beginning with `.`), along with their respective CSS file names and other information.

![css-handles-inspect](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-0.png)

> ⚠️ Before proceeding to the third step, check the CSS handles table in the documentation of the app/block that renders the HTML element. This will allow you to confirm whether the inspected handle is valid and also if the customization requires another add-on, such as the HTML element attribute.

> ⚠️ If after checking the CSS handles table, you notice that the desired handle needs to use the attribute of the HTML element that will be customized, inspect the page again, this time using your browser and not the `?__inspect` option. After inspecting the page, look for the desired HTML element and copy the attribute linked to it that will be used in the upcoming customization.

3. Open the Store Theme code using the code editor of your choice. Then, create a file inside the css folder named after the text displayed below the desired handle. Following the example above, we would have `vtex.menu.css`.

4. In the new file, use one of the CSS handles listed and customize its properties. For example:

```css
.menuItem {  
    background: rgba(0, 0, 0, 0.2);
    margin: 5px;
    border-radius: 5px;
}
```

> ℹ️ Remember: If the handle requires an add-on, such as the HTML element attribute or a handle modifier, add it next to the handle name, following this format: `{cssHandleName}--{addon)`.

Once your app is linked and the changes are saved, the new customization should immediately be reflected in your workspace.

![css handles customization applied to the menuItem](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-1.png)

As you have seen, CSS handles are used to overwrite a store's default style and, thus, independently customize a type of block separate from the rest of the theme. Note that the change above was applied to all `menu-item` blocks.

To independently customize a single `menu-item` block, you should use the  `blockClass` prop.

`blockClass` is a property that you can freely define. When passed in a block, it serves as its single **identifier** for customization.

### Using the blockClass property

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

After saving and updating your workspace, when you inspect the element, it should display an additional CSS handle along with the default one, like this:

![css handles with block class](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-2.png)

After that, you can use the class `.menuItem--header` to specifically target the elements that have this `blockClass`.

![specific menu items with css handles applied using blockClass](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-3.png)

> ℹ️ Our team is constantly working on developing CSS handles for every possible store component. However, if you are unable to find a CSS handle for a component you want to customize, share this use case with us at [Store Discussion](https://github.com/vtex-apps/store-discussion).

## Best practices

To standardize CSS customization and avoid any potential breakdown in layout, **we recommend making store customizations exclusively using CSS handles**.

However, it is common to come across store scenarios where CSS selectors are used for the customization. As the name implies, they select elements for CSS customization based on the HTML hierarchy of the page.

Customization using HTML hierarchy was mostly deprecated. This means that **only** the CSS selectors listed below will continue to be allowed for store customization:

- Class selectors (e.g. `.foo`)
- Pseudo-selectors `:hover`, `:visited`, `:active`, `:disabled`, `:focus`, `:local`, `:empty`, and `:target`
- `:not()`
- `:first-child` and `:last-child`
- `:nth-child(even)`, `:nth-child(odd)`, and `:nth-child(2n)` (or any other step like `4n`, `5n`, and so on.)
- All pseudo-elements, such as  `::before`, `::after`, and `::placeholder`
- Space combinator (e.g. `.foo .bar`)
- `[data-...]`
- `:global(vtex-{AppName}-{AppVersion}-{ComponentName})` for selection of elements that come from different apps

**Any CSS selectors that are not on this list, such as** `:nth-child(2)`**,** `foo > bar` **, and** `[alt="bar"]`**, is not accepted by the VTEX IO CLI during the [linking](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) of the store's theme to the local files.**

> ⚠️ Note that any customization that uses CSS selectors depends on an HTML structure that, when changed, can break the merchant's desired customization. **Always use CSS handles as your first choice**.
