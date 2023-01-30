---
title: "Building a Carousel using Slider Layout"
slug: "vtex-io-documentation-building-a-carousel-using-slider-layout"
hidden: false
createdAt: "2020-06-03T16:02:44.233Z"
updatedAt: "2022-12-13T20:17:43.910Z"
---

## Introduction

There are block types in VTEX IO's Store Framework that instead of being responsible for rendering store components, such as the `shelf`, they **carry and provide data to their subsequent child blocks**.

These blocks are instances of a `list-context` interface called `lists`. They are exported by the `vtex.list-context` app.

Since **a Carousel is a slider with images displayed on it**, you can create one for your store using one of the available `list-context` instances together with a `slider-layout`, a generic layout block that enables you to create a Slider component out of a set of other blocks.

See the instructions below for how it can be easily done!

## Step by step

1. Make sure your store is running `vtex.store@2.70.0` or higher.

2. Add the following **dependencies** to your theme's `manifest.json` file:

```json
"vtex.store-image": "0.x",
"vtex.slider-layout": "0.x"
```

3. Declare the `list-context.image-list` block and use the `slider-layout` as its only child. Each desired image should be forwarded to the `list-context.image-list` as an object with the following properties:

| Property      | Type                                                                                                                                | Description                                                   | Default value |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------- |
| `image`       | `String`                                                                                                                            | Link for the image                                            | N/A           |
| `mobileImage` | `String`                                                                                                                            | Link for the mobile image                                     | N/A           |
| `description` | `String`                                                                                                                            | The image's description                                       | N/A           |
| `link`        | [`Link`](https://github.com/vtex-apps/native-types/blob/f63aeeb8f6e62f4a9aaec052a8be34973be7389b/pages/contentSchemas.json#L52-L74) | Specifies the link the image will redirect to when clicked on | N/A           |

*For example:*

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

> ⚠️ Bear in mind that **list blocks do not render anything in your store**, they simply hold content that can be edited using the Site Editor and pass it down to their child blocks.

4. Now that you've specified which data (in this case, which images) will be displayed in your slider using a `list` block, you need to configure the [slider properties](https://developers.vtex.com/vtex-developer-docs/docs/vtex-slider-layout) themselves, meaning those of the `slider-layout`.

*For example:*

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

And there you go! You now have a fully functioning Carousel for your store.

![gif-caroulsel-slider-layout](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-carousel-using-slider-layout-0.gif)
*When inspecting the page you’ll notice that the `carousel` block was not used to build the component.*

Bear in mind that you are also able to edit data contained in `list-context.image-list` using the admin's Site Editor section:

![carousel-slider-site-editor](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-carousel-using-slider-layout-1.png)
