---
title: "Using CSS Handles for store customization"
slug: "vtex-io-documentation-using-css-handles-for-store-customization"
hidden: false
createdAt: "2020-06-03T16:02:45.024Z"
updatedAt: "2022-12-13T20:17:44.398Z"
---


This guide will walk you through how to use CSS Handles to customize your storefront. CSS Handles are unique identifiers assigned to HTML elements. They can be used in the store theme to customize frontend components via CSS classes.


## Step by step

1. Open your workspace on your browser, add `?__inspect` at the end of the page URL, and press enter. For example, `https://{workspace}--{account}.myvtex.com?__inspect`. Please note that it must be a development workspace rather than a production one, and it must be under the domain `myvtex.com`.

2. Hover over the element you want to customize. It should display its available CSS Handles in a box (the big names beginning with `.`), along with their respective CSS file names and other information.

![css-handles-inspect](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-0.png)

> ⚠️ Before proceeding to step 3, check the CSS Handles table in the documentation of the app/block responsible for rendering the HTML element. It will then be possible to confirm whether the inspected Handle is valid, mainly if the customization requires another add-on, such as the attribute of the HTML element.

> ⚠️ If, when checking the CSS Handles table, you notice that the desired Handle needs to use the attribute of the HTML element that will be customized, inspect the page again. Try using your browser and not the `?__inspect` feature. Upon inspecting the page, look for the desired HTML element and copy the attribute linked to it that will be used in the upcoming customization.

3. Open the Store Theme code using the code editor of your preference. Then, create a file in the CSS folder named after the text displayed below the desired handle. Following the example above, it would be `vtex.menu.css`.

4. Use one of the CSS Handles listed in the new file and customize its properties. For example:

```css
.menuItem {  
    background: rgba(0, 0, 0, 0.2);
    margin: 5px;
    border-radius: 5px;
}
```

> ℹ️ Remember: If the Handle requests an add-on, such as the HTML element attribute or a Handle modifier, add it next to the Handle name, following this format: `{cssHandleName}--{addon)`.

Once your app is linked and the changes are properly saved, your workspace should reflect the new customization immediately.

![css handles customization applied to the menuItem](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-1.png)

As you have seen, CSS Handles are used to overwrite a store default style and thus customize a type of block independently of the rest of the theme. Please note that the change above was applied to all `menu-item` blocks.

To customize a single `menu-item` block independently, you must use the  `blockClass` prop.

`blockClass` is a property whose value you may define freely. When passed onto a block, it serves as its single **identifier** for customization.

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

After saving and updating your workspace, when inspecting the element, an additional CSS Handle should be displayed along with its default one, as:

![css handles with block class](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-2.png)

Then, you can use the class `.menuItem--header` to target specifically the elements that have this `blockClass`.

![specific menu items with css handles applied using blockClass](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-css-handles-for-store-customization-3.png)


## Best practices

To standardize CSS customization and avoid potential breakdowns in layout, we recommend store customization to be performed exclusively using CSS Handles.

However, it is common to come across store scenarios whose customization uses CSS Selectors. As the name implies, they are used for selecting elements for CSS customization following the page's HTML hierarchy.

This customization practice is mostly deprecated. It means that only the CSS Selectors listed below will continue to be allowed for store customization:

- Class selectors (e.g. `.foo`)
- Pseudo-selectors `:hover`, `:visited`, `:active`, `:disabled`, `:focus`, `:local`, `:empty`, and `:target`
- `:not()`
- `:first-child` and `:last-child`
- `:nth-child(even)`, `:nth-child(odd)`, and `:nth-child(2n)` (or any other step like `4n`, `5n`, etc)
- All pseudo-elements, such as  `::before`, `::after` and `::placeholder`
- Space combinator (e.g. `.foo .bar`)
- `[data-...]`
- `:global(vtex-{AppName}-{AppVersion}-{ComponentName})` for selection of elements that come from different apps

CSS Selectors that are not on this list, such as `:nth-child(2)`, `foo > bar` and `[alt="bar"]`, are not accepted by VTEX IO CLI when [linking](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) the store theme to its local files.

> ⚠️ Please bear in mind that any customization that uses CSS Selectors depends on an HTML structure that, when changed, can break the merchant's desired customization. Always prefer to use CSS Handles.
