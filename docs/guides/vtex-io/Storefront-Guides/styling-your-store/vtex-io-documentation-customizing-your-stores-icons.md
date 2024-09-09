---
title: "Customizing your store's icons"
slug: "vtex-io-documentation-customizing-your-stores-icons"
hidden: false
createdAt: "2020-06-03T16:02:44.699Z"
updatedAt: "2022-12-13T20:17:44.425Z"
---

The [VTEX Styleguide](https://styleguide.vtex.com) provides a [default iconography](https://styleguide.vtex.com/#/Icons) used across all Store Framework components, which is implemented via the [Store Icons](https://github.com/vtex-apps/store-icons) app.

While these icons are suitable for most stores, you can customize them to better align with your store's branding. Follow the steps below to override the default icons.

## Before you begin

Ensure that your Store Theme is using the [`styles` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-styles-builder) at version 1.8.1 or higher.

## Instructions

### Step 1 - Create an Icon Pack

1. In your Store Theme, create a new folder named `iconpacks` within the `styles` folder.
2. Inside the `iconpacks` folder, create a file named `iconpack.svg`.
3. Copy the content of the [iconpack.svg](https://github.com/vtex-apps/store-icons/blob/master/styles/iconpacks/iconpack.svg?short_path=62ebf4b) file and paste it into your `iconpack.svg` file.

### Step 2 - Customize Icons

The `iconpack.svg` file contains all the store's icons, with each icon having a unique `id` and grouped inside a `<g>` tag. These `id`s allow you to reference and modify individual icons.

Each icon is identified by an `id` within its `<g>` tag (e.g., `hpa-cart` for the cart icon). You can reference and modify a specific icon in the store’s code using its fragment identifierl, like `#hpa-cart`.

To customize an icon, find its corresponding `<g>` tag by `id` in the `iconpack.svg` file and adjust its content (shapes, paths, etc.). You don't need to recreate the entire icon — just modify the parts you want to change.

For example, to customize the cart icon (`hpa-cart`), you only need to modify the elements within its `<g>` tag:

```svg styles/iconpacks/iconpack.svg
<g id="hpa-cart">
    <path d="M15.0503 3.0002H4.92647C4.81221 3.00072 4.7012 2.96234 4.6118 2.89142C4.52239 2.8205 4.45996 2.72129 4.43483 2.6102L4.01342 0.800203C3.96651 0.570928 3.84041 0.365306 3.65708 0.219131C3.47375 0.0729566 3.24479 -0.00451449 3.01006 0.000203439H0.501677C0.368624 0.000203439 0.241021 0.0528819 0.146938 0.14665C0.0528551 0.240418 0 0.367595 0 0.500203L0 1.5002C0 1.63281 0.0528551 1.75999 0.146938 1.85376C0.241021 1.94753 0.368624 2.0002 0.501677 2.0002H1.80604C1.92077 1.9978 2.03274 2.03548 2.12253 2.10671C2.21232 2.17794 2.27429 2.27823 2.29768 2.3902L4.01342 10.2002C4.06032 10.4295 4.18642 10.6351 4.36975 10.7813C4.55308 10.9274 4.78204 11.0049 5.01677 11.0002H13.0436C13.2478 10.9891 13.4436 10.9161 13.605 10.791C13.7664 10.6659 13.8856 10.4947 13.9466 10.3002L15.9533 4.3002C15.9995 4.15468 16.0116 4.00057 15.9888 3.84965C15.9659 3.69874 15.9088 3.55504 15.8216 3.42956C15.7344 3.30408 15.6196 3.20015 15.4859 3.12573C15.3522 3.0513 15.2032 3.00837 15.0503 3.0002Z" fill="currentColor"/>
    <path d="M5.02682 16.0002C6.13509 16.0002 7.03353 15.1048 7.03353 14.0002C7.03353 12.8956 6.13509 12.0002 5.02682 12.0002C3.91855 12.0002 3.02011 12.8956 3.02011 14.0002C3.02011 15.1048 3.91855 16.0002 5.02682 16.0002Z" fill="currentColor"/>
    <path d="M13.0737 16.0002C14.182 16.0002 15.0804 15.1048 15.0804 14.0002C15.0804 12.8956 14.182 12.0002 13.0737 12.0002C11.9655 12.0002 11.067 12.8956 11.067 14.0002C11.067 15.1048 11.9655 16.0002 13.0737 16.0002Z" fill="currentColor"/>
</g>
```

> To find each icon’s unique `id`, refer to the [Icon Pack list](https://github.com/vtex-apps/store-icons/blob/cbbb1b82bfca247a811d146b1e2cafb642db1928/docs/ICONPACK.md) This allows you to customize individual icons without affecting the entire icon set.

### Step 3 - Applying your changes

Once you've made the desired changes, [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) your app to see the updated icons reflected in the store.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-customizing-your-stores-icons-2.png)

> ⚠️ If the changes don't appear after linking, ensure the `styles` builder version is 1.8.1 or higher.

## Best practices

- Icons should not exceed `20x20` pixels.
- Each [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) can only have one app installed that includes `iconpack` customizations.
