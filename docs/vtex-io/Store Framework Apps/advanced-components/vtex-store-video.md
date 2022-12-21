---
title: "Video"
slug: "vtex-store-video"
excerpt: "vtex.store-video@1.4.3"
hidden: false
createdAt: "2020-10-05T19:26:27.897Z"
updatedAt: "2021-12-08T18:22:55.061Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Video app allows you to display video assets on your store pages.

![Media Placeholder](https://storecomponents.vtexassets.com/arquivos/ids/155640)

## Configuration

1. Add the `store-video` app to your theme's dependencies in the `manifest.json` file:

```diff
 "dependencies ": {
+  "vtex.store-video": "1.x"
 }
```

2. In any desired theme template, add the `video` block with the desirable props. For example:

```json
  "video#background": {
    "props": {
      "width": "100%",
      "height": "600px",
      "loop": false,
      "autoPlay": true,
      "muted": false,
      "src": "https://www.youtube.com/watch?v=wygFqZXMIco",
      "blockClass": "videoEl"
    }
  }
```

### `video` props

| Prop name        | Type                 | Description                                                                                                                                                                                            | Default value     |
| ---------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| `name`           | `string`             | Video name for SEO and accessibility.                                                                                                                                                                  | `undefined`       |
| `description`    | `string`             | Video description for SEO and accessibility.                                                                                                                                                           | `undefined`       |
| `src`            | `string`             | Video URL. It can be a `youtube` URL, `vimeo` URL or a self-hosted video URL.                                                                                                                          | `undefined`       |
| `type`           | `string`             | Video type.                                                                                                                                                                                            | `undefined`       |
| `poster`         | `string`             | Cover image URL to be displayed before the video playback.                                                                                                                                             | `undefined`       |
| `controlsType`   | `enum`               | The type of controls. It can be `custom-vtex`( only works if the video URL represents a HTML5 player ), `native` or `none`.                                                                            | `undefined`       |
| `autoPlay`       | `boolean`            | Whether the video will start automatically after loaded(`true`) or not(`false`). Note that if the value is `true`, the muted property will automatically be setted to `true`.                          | `false`           |
| `muted`          | `boolean`            | Whether the video will start with the audio on(`false`) or not(`true`).                                                                                                                                | `false`           |
| `loop`           | `boolean`            | Whether the video will run in a loop(`true`) or not(`false`).                                                                                                                                          | `false`           |
| `playsInline`           | `boolean`            | Whether the video will play inline(`true`) or not(`false`).                                                                                                                                          | `false`           |
| `width`          | `number` or `string` | The width of the video exhibition area. It could be as %(`string`) or pixels(`number`).                                                                                                                | `undefined`       |
| `height`         | `number` or `string` | The height of the video exhibition area. It could be as %(`string`) or pixels(`number`).                                                                                                               | `undefined`       |
| `PlayIcon`       | `string`             | Video play icon for `custom-vtex` controls.                                                                                                                                                            | `icon-play`       |
| `PauseIcon`      | `string`             | Video pause icon for `custom-vtex` controls.                                                                                                                                                           | `icon-pause`      |
| `VolumeOnIcon`   | `string`             | Video volume on icon for `custom-vtex` controls.                                                                                                                                                       | `icon-volume-on`  |
| `VolumeOffIcon`  | `string`             | Video volume off icon for `custom-vtex` controls.                                                                                                                                                      | `icon-volume-off` |
| `FullscreenIcon` | `string`             | Video fullscreen icon for `custom-vtex` controls.                                                                                                                                                      | `icon-extend`     |
| `classes`        | `CustomCSSClasses`   | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it here. Note that this is only useful if you're importing this block as a React component. | `undefined`       |

Use the **admin's Site Editor** to manage some props declared in the `video` block.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles         |
| ------------------- |
| `controlsContainer` |
| `fallbackContainer` |
| `fallbackImage`     |
| `fullscreenButton`  |
| `playButton`        |
| `trackBar`          |
| `trackContainer`    |
| `trackTimer`        |
| `videoContainer`    |
| `videoElement`      |
| `volumeContainer`   |
| `volumeButton`      |
| `volumeSlider`      |

> ⚠️ It's required that `controlsType` prop is set as `custom-vtex` in order to have the following CSS Handles properly working: `controlsContainer`, `fullscreenButton`, `playButton`, `trackContainer`, `trackTimer`, `trackBar`, `volumeContainer`, `volumeSlider`, and `volumeButton`.

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