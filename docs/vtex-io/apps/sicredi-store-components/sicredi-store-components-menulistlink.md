---
title: "MenuLinkList"
slug: "sicredi-store-components-menulistlink"
excerpt: "sicredi.store-components@0.1.0"
hidden: true
createdAt: "2022-08-08T17:35:54.078Z"
updatedAt: "2022-08-08T17:35:54.078Z"
---
## Description

This component will show a dropdown menu in the mobile device and a column menu on the desktop that can be use to navigate to pages in the site.

## Configuration

1. Add the `sicredi.store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.store-components": "0.x"
}
```

2. The component can be called inside another component as `<MenuLinkList {...props}/>`


```jsx
  <MenuListLink menuItems={
    [
      { link: '/', title: 'title' }
    ]
  }>
```

## Props of the `MenuListLink`

| Prop name         | Type      | Description                              | Default value |
| ----------------- | --------- | ---------------------------------------- | ------------- |
| `menuItems`         | `array`  | Array of menu items                     |              |

## Props of the `MenuItem`

| Prop name         | Type      | Description                              | Default value |
| ----------------- | --------- | ---------------------------------------- | ------------- |
| `link`            | `string`  | URL of the menu item                     |               |
| `title`           | `string`  | title of the menu item                   |               |

## Customization

Below are the classes available for customization. For more information access: [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                   |
| ----------------------------- |
|  `menu-list`                  |
|  `menu-list__item`            |
|  `dropdown`                   |
|  `dropdown__selected`         |
|  `dropdown__items-container`  |
|  `dropdown__item`             |
|  `dropdown__icon`             |