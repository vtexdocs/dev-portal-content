---
title: "Store Media"
slug: "vtex-store-media"
excerpt: "vtex.store-media@0.3.0"
hidden: false
createdAt: "2021-01-22T13:03:07.471Z"
updatedAt: "2021-03-31T17:25:38.265Z"
---
📢 Use this project, [contribute](https://github.com/vtex-apps/store-media) to it or open issues to help evolve it using [Store Discussion](https://github.com/vtex-apps/store-discussion).

# Store Media

<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/advanced-components/#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Media app allows you to display image and video assets using a single block.

![media-list-example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-media-0.gif)
## Configuration

1. Add the `store-media` app to your theme's dependencies in the `manifest.json` file:

```diff
 "dependencies ": {
+  "vtex.store-media": "0.x"
 }
```

Now, you are able to use all blocks exported by the `store-media` app. Check out the full list below:

| Block name                | Description                                                                                                                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `media`                   | This block is capable of displaying a single image or video.                                                                                                                                                                                                 |
| `list-context.media-list` | This block allows you to display a list of images and videos in your store with a higher degree of composability. You can use it along with other `list-context` or `slider-layout` blocks to create different sliders and layouts. |

### `media` block

The `media` block inherits all props from `image` and `video` blocks. It's highly recommended you check out the docs for [Image](https://github.com/vtex-apps/store-image) and [Video](https://github.com/vtex-apps/store-video) blocks before using this block.

You can use props from both blocks, but `media` will only consider the props from the block (`image` or `video`) that matches the current `mediaType`, or, in the case of `mediaType` being `imageOrVideo`, that matches the type of the `src`.

| Prop name   | Type | Description                                                                                                                                                                                                                                                                                                                         | Default value  |
| ----------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `mediaType` | enum | Type of the media to be displayed. Possible values are: `image` (behaves as an image block no matter the `src`), `video` (behaves as an video block no matter the `src`), and `imageOrVideo`. Choosing `imageOrVideo` will make `media` automatically identify the type of the `src` based on its extension and behave accordingly. | `imageOrVideo` |

Use the **admin's Site Editor** to manage some props declared in the `media` block. Using the Site Editor to provide the image or video `src` will force you to choose between `image` and `video`.

**Usage Example**:

```json
"media#mobile-phone": {
  "props": {
    "src": "https://storecomponents.vteximg.com.br/arquivos/mobile-phone.png",
    "blockClass": "storePrint"
  }
}
```

### `list-context.media-list` block

The `list-context.media-list` block acts just like the `list-context.image-list` block and inherits a lot from `image` and `video` blocks, with a few key differences. It's highly recommended you check out the docs for [Image](https://github.com/vtex-apps/store-image) and [Video](https://github.com/vtex-apps/store-video) blocks before using this block.

`list-context.media-list` accepts both images and videos, so you can mix them inside a single carousel, for example. Images can receive `image` blocks' props and videos can receive `video` blocks' props. If you pass props that don't match the media type, they will be ignored.

| Prop name   | Type | Description                                                                                                                                                                                                                                                                                                                         | Default value  |
| ----------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `height` | `string  | number` | This value is used for the `max-height` CSS property and **is applied to images only**. | `420` |
| `mediaList` | [MediaListElement] | List of `MediaListElement` that represents the media to be added to the list context. | `[]` |

- `MediaListElement` object

A `MediaListElement` object has a very similar shape to the props accepted by the `media` component, that is, you can specify the `mediaType` of the asset you want to display and pass the props for `image` and `video` blocks. Read the docs for the `media` block to better understand how that works.

Differently from the `media` component, it does **not** use the `src` prop to receive the assets. For images, it uses the `image` and `mobileImage` props, and, for video, it uses the `video` and `mobileVideo` props.

| Prop name   | Type | Description                                                                                                                                                                                                                                                                                                                         | Default value  |
| ----------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `image` | `string` | URL to the image to be displayed. | undefined |
| `mobileImage` | `string` | URL to the image to be displayed when the user is using a mobile device. If it's undefined, `image` will be used instead. | undefined |
| `video` | `string` | URL to the video to be displayed. | undefined |
| `mobileVideo` | `string` | URL to the video to be displayed when the user is using a mobile device. If it's undefined, `video` will be used instead. | undefined |


**Usage Example**:

```json
"list-context.media-list#demo": {
  "children": ["slider-layout#demo-media"],
  "props": {
    "height": 720,
    "mediaList": [
      {
        "image": "https://storecomponents.vteximg.com.br/arquivos/banner-principal.png",
        "mobileImage": "https://storecomponents.vteximg.com.br/arquivos/banner-principal-mobile.jpg"
      },
      {
        "video": "https://www.youtube.com/embed/JgkrlaF52WQ"
      },
      {
        "image": "https://storecomponents.vteximg.com.br/arquivos/banner.jpg",
        "mobileImage": "https://storecomponents.vteximg.com.br/arquivos/banner-principal-mobile.jpg"
      }
    ]
  }
},
"slider-layout#demo-media": {
  "props": {
    "itemsPerPage": 1,
    "infinite": true,
    "showNavigationArrows": "desktopOnly",
    "blockClass": "carousel"
  }
}
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Just like they do with props, all blocks from this app inherits all of `image` and `video` blocks' CSS Handles. You can find them in their respective docs.

Keep in mind that, for instance, applying CSS customizations to CSS Handles that came from `image` won't have any effect if the `mediaType` is set to `video` or if the `mediaType` is set to `imageOrVideo` and the `src` was identified as a video.

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->