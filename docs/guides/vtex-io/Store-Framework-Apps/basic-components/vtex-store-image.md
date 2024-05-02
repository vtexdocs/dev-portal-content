---
title: "Store Image"
slug: "vtex-store-image"
hidden: false
createdAt: "2020-06-03T15:19:10.796Z"
updatedAt: "2022-09-08T19:10:41.275Z"
---

The Store Image app exports the `list-context.image-list` block, which is responsible for working with image content in the store's theme.

![store-image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-image-0.png)

## Configuration

1. Add the `store-image` app to your theme's dependencies in the `manifest.json`, for example:

```diff
 "dependencies ": {
+  "vtex.store-image": "0.x"
 }
```

You are now able to use the `list-context.image-list` block, exported by the Store Image app. The block allows you to display images in your store with a higher degree of composability, since you can use it along with other `list-context` blocks to create a more flexible and customizable image slider.

2. In any desired theme template, add the `list-context.image-list` block, declaring the `slider-layout` block as child. For example:

```json
  "list-context.image-list#demo": {
    "children": ["slider-layout#demo-images"],
    "props": {
      "preload": true,
      "height": 650,
      "images": [
        {
          "image": "https://storecomponents.vteximg.com.br/arquivos/banner-infocard2.png",
          "description": "something something"
        },
        {
          "image": "https://storecomponents.vteximg.com.br/assets/vtex.file-manager-graphql/images/Group%207%20(1)%20(1)%20(1)%20(1)%20(1)___c6b3ed853fb16a08b265753b50e0c57a.png",
          "description": "something something"
        }
      ]
    }
  },

  "slider-layout#demo-images": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true
    }
  },
```

Note that the `slider-layout` block, exported from the Slider Layout app, is given as a child of `list-context.image-list`. It is responsible for defining which images will be displayed, as well as their behavior once rendered.

### `list-context.image-list` props

| Prop name | Type      | Description                                                                                          | Default value |
| --------- | --------- | ---------------------------------------------------------------------------------------------------- | ------------- |
| `images`  | `array`   | Array of objects declaring all desired images to be rendered.                                        | `undefined`   |
| `height`  | `number`  | Image height for all images declared in the `image` object (in `px`).                                | `undefined`   |
| `preload` | `boolean` | Preloads the first image in a list, which helps prioritizing the display of images over other assets | `false`       |

### `image-list` props

| Prop name | Type     | Description                                                           | Default value |
| --------- | -------- | --------------------------------------------------------------------- | ------------- |
| `images`  | `array`  | Array of objects declaring all desired images to be rendered.         | `undefined`   |
| `height`  | `number` | Image height for all images declared in the `image` object (in `px`). | `undefined`   |

- **`images` array:**

| Prop name     | Type                | Description                               | Default value |
| ------------- | ------------------- | ----------------------------------------- | ------------- |
| `image`       | `string`            | Image URL.                                | `undefined`   |
| `mobileImage` | `string`            | Mobile image URL.                         | `undefined`   |
| `description` | `string`            | Image description.                        | `undefined`   |
| `link`        | `object`            | Links an URL to the image being rendered. | `undefined`   |
| `width`       | `string` / `number` | Image width (in `%` or `px`).             | `100%`        |

- **`link` object:**

| Prop name    | Type      | Description                                                                                                                                                                     | Default value |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `url`        | `string`  | URL users will be redirected to when clicking on the image.                                                                                                                     | `undefined`   |
| `noFollow`   | `boolean` | Whether the linked URL is endorsed by the owner of the page the user was navigating on i.e. if there is a commercial relationship between both pages (`true`) or not (`false`). | `false`       |
| `openNewTab` | `string`  | Whether a new tab on browser will be opened (`true`) or not (`false`) .                                                                                                         | `undefined`   |
| `title`      | `string`  | Text label used to identify the image in the admin's Site Editor.                                                                                                               | `undefined`   |

> ℹ️ Use the **admin's Site Editor** to manage all images declared in the `list-context.image-list` block.

## Customization

The block still doesn't have CSS Handles for its specific customization.

All CSS Handles available for the Image block are the ones available for the `slider-layout` block. Take a look at the Customization section in the [**Slider Layout documentation**](https://developers.vtex.com/docs/apps/vtex.slider-layout).
Note that the `image-slider` uses our `vtex.slider-layout` app, so all the CSS namespaces defined by it are also available for `image-slider`. Take a look at [Slider-Layout](https://developers.vtex.com/docs/apps/vtex.slider-layout).
