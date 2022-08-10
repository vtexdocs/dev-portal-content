---
title: "Breadcrumb"
slug: "tuttoperlacasa-breadcrumb"
excerpt: "tuttoperlacasa.breadcrumb@1.11.0"
hidden: true
createdAt: "2022-07-28T13:05:55.807Z"
updatedAt: "2022-07-28T13:05:55.807Z"
---
The VTEX BreadCrumb is a navigation scheme that shows a user's browsing history up to their current location in your store.

![img2-breadcrumb](https://user-images.githubusercontent.com/52087100/69836587-a4237380-1228-11ea-89c8-0f34cea3a96f.png)

## Configuration

1. Import the breadcrumb's app to your theme's dependencies in the `manifest.json`, for example:

```json
  dependencies: {
    "vtex.breadcrumb": "1.x"
  }
```

2. Add the `breadcrumb` block to the Product template. For example:

```
 "breadcrumb": {
    "props": {
      "showOnMobile": true
    }
  },
```

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `showOnMobile`        | `Boolean`       | It determines whether Breadcrumb should also be displayed on mobile          | `false`              |
| `homeIconSize`  | `Number`        | Controls the `size` property of [`IconHome`](https://github.com/vtex-apps/store-icons#icons)                                                                                                      | `26` |
| `caretIconSize` | `Number`        | Controls the `size` property of [`IconCaret`](https://github.com/vtex-apps/store-icons#icons)                                                                                                     | `8` |
| `homeType` | `"text" | "icon"`        | Controls if the home link will show as an icon or a text | `"icon"` |
| `homeLinkText` | `String`        | The text shown when `homeType` is set to `"text"` | `"home"` |

:warning: The product's categories should appear as an array in one of this two formats:

```javascript
categories = ['/Eletronics/', '/Eletronics/Computers']
```

```javascript
categories = ['eletronics', 'eletronics-computers']
```

3. Add the `breadcrumb.search` block to the Search template. For example:

```
 "breadcrumb.search": {
    "props": {
      "showOnMobile": true
    }
  },
```

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `showOnMobile`        | `Boolean`       | It determines whether Breadcrumb should also be displayed on mobile          | `false`              |
| `homeIconSize`  | `Number`        | Controls the `size` property of [`IconHome`](https://github.com/vtex-apps/store-icons#icons)                                                                                                      | `26` |
| `caretIconSize` | `Number`        | Controls the `size` property of [`IconCaret`](https://github.com/vtex-apps/store-icons#icons)                                                                                                     | `8` |
> ℹ️ *The `breadcrumb.search` block is specific for the Breadcrumb inside the search result page.* 

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization). 

| CSS Handles |
| ----------- | 
| `container` | 
| `link`      | 
| `arrow`     | 
| `homeLink`  | 
| `termArrow` |


## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!