---
title: "Building a carousel using Slider Layout"
slug: "vtex-io-documentation-building-a-carousel-using-slider-layout"
hidden: false
createdAt: "2020-06-03T16:02:44.233Z"
updatedAt: "2022-12-13T20:17:43.910Z"
---

Some block types in Store Framework carry and provide data to their child blocks instead of rendering storefront components.

These blocks are instances of a `list-context` interface called `lists`. They are exported by the `vtex.list-context` app.

A carousel is essentially a slider that showcases a collection of images. Hence, to create a carousel for your store, you can use one of the available `list-context` instances together with a `slider-layout`, a versatile layout block that allows you to create a Slider component from a set of other blocks.

Check the instructions below for more information.

## Instructions

1. Make sure your store is running `vtex.store@2.70.0` or higher.

2. Add the following **dependencies** to the theme `manifest.json` file:

```json
"vtex.store-image": "0.x",
"vtex.slider-layout": "0.x"
```

3. Declare the `list-context.image-list` block and use the `slider-layout` as its only child. Each desired image should be forwarded to the `list-context.image-list` as an object with the following properties:

| Property      | Type                                                                                                                                | Description                                                 | Default value |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------- |
| `image`       | `string`                                                                                                                            | Link to the image.                                          | N/A           |
| `mobileImage` | `string`                                                                                                                            | Link to the mobile image.                                   | N/A           |
| `description` | `string`                                                                                                                            | The image description.                                      | N/A           |
| `link`        | [`link`](https://github.com/vtex-apps/native-types/blob/f63aeeb8f6e62f4a9aaec052a8be34973be7389b/pages/contentSchemas.json#L52-L74) | Specifies the link the image will redirect to when clicked. | N/A           |

*Example:*

```json
"list-context.image-list#demo": {
    "children": ["slider-layout#demo-images"],
    "props": {
      "height": 650,
      "images": [
        {
          "image": "https://storecomponents.vteximg.com.br/files/banner-infocard2.png",
          "description": "something something"
        },
        {
          "image": "https://storecomponents.vteximg.com.br/assets/vtex.file-manager-graphql/images/Group%207%20(1)%20(1)%20(1)%20(1)%20(1)___c6b3ed853fb16a08b265753b50e0c57a.png",
          "description": "something something"
        }
      ]
    }
  },
```

> ⚠️ Note that list blocks do not render anything in your store. Instead, they hold content that can be edited using Site Editor and pass it down to their child blocks.

4. Now that you have specified which information, an image in this case, will be displayed in your slider using a `list` block, you need to configure the [slider properties](https://developers.vtex.com/docs/guides/vtex-slider-layout) themselves, meaning the properties of `slider-layout`.

*Example:*

```json
  "list-context.image-list#demo": {
    "children": ["slider-layout#demo-images"],
    "props": {
      "height": 650,
      "images": [
        {
          "image": "https://storecomponents.vteximg.com.br/files/banner-infocard2.png",
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
  }
```

Now you have a fully functioning carousel for your store.

![gif-caroulsel-slider-layout](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-carousel-using-slider-layout-0.gif) 

*When inspecting the page, you will notice that the `carousel` block was not used to build the component.*

Note that you can also edit the information contained in `list-context.image-list` through Site Editor section in the Admin:

![carousel-slider-site-editor](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-carousel-using-slider-layout-1.png)
