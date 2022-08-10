---
title: "Slider Categories"
slug: "pasteurio-slider-categories-slidercategories"
excerpt: "pasteurio.slider-categories@0.0.3"
hidden: true
createdAt: "2022-07-27T22:41:30.228Z"
updatedAt: "2022-07-27T22:41:30.228Z"
---
The `slider-categories` is the block is responsible show the selider of categories a page of the departament

![image](https://user-images.githubusercontent.com/17678382/151086921-ca4ecacd-146a-44db-a256-2c0fa1aff041.png)

## Configuration

1. Import the `blacksipqa.slider-categories` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "blacksipqa.slider-categories": "0.x"
    }
}
```

2. Add the `slider-categories` block in the page of departament `store.search#departament`. For example:

```json
{
    "store.search#departament": {
        "blocks": ["slider-categories"]
    }
}
```

3. Use handles for each item of slider and add images and efects from css

# props `slider-categories`

| Prop name              | Type       | Description                                                                                                                                                                         | Default value                         |
| ---------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `departamentId`        | `string`   | department id use only when the component is rendered outside of a search context.                                                                                                  | `undefined`                           |
| `showNavigationArrows` | `enum`     | When navigation arrows should be rendered. Possible values are: `mobileOnly`, `desktopOnly`, `always`, or `never`.                                                                  | `always`                              |
| `showPaginationDots`   | `enum`     | When pagination dots should be rendered. Possible values are: `mobileOnly`, `desktopOnly`, `always`, or `never`.                                                                    | `always`                              |
| `infinite`             | `boolean`  | Whether the slider should be infinite (`true`) or not (`false`). When this prop is set as `false`, the slider will have an explicit end for users.                                  | `false`                               |
| `usePagination`        | `boolean`  | Whether the slider should use slide pages (`true`) or not (`false`). When this prop is set as `false`, the slider will use smooth scrolling for slide navigation instead of arrows. | `true`                                |
| `itemsPerPage`         | `object`   | Number of slider items to be shown on each type of device. For more on this, check out the `itemsPerPage` object section below.                                                     | `{ desktop: 5, tablet: 3, phone: 1 }` |
| `fullWidth`            | `boolean`  | Whether the slides should occupy the full page width, making the arrows appear on top of them (`true`) or not (`false`).                                                            | `true`                                |
| `tagert`               | `string`   | The target attribute specifies where to open the linked document                                                                                                                    | `_self`                               |
| `Title`                | `Componet` | Component to display as title for example a rich-text                                                                                                                               | `undefined`                           |

-   **`itemsPerPage` object**

| Prop name | Type     | Description                                      | Default value |
| --------- | -------- | ------------------------------------------------ | ------------- |
| `desktop` | `number` | Number of slides to be shown on desktop devices. | `5`           |
| `tablet`  | `number` | Number of slides to be shown on tablet devices.  | `3`           |
| `phone`   | `number` | Number of slides to be shown on phone devices.   | `1`           |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles    |
| -------------- |
| `container`    |
| `slide`        |
| `slideContent` |
| `slideName`    |
| `departament`  |
| `categorie`    |