---
title: "Ri Happy - Video Component"
slug: "rihappyio-rihappy-store-components-readme"
excerpt: "rihappyio.rihappy-store-components@0.9.1"
hidden: true
createdAt: "2022-07-19T16:58:24.799Z"
updatedAt: "2022-07-28T19:08:41.074Z"
---
The purpose of this app is to work in a video scenario that the native vtex app could not handle.

When we tried to use the VTEX video app, it didn't work on the iPhone, so we had to create a video component for this scenario.

## Integrating with your store

On your store-theme, add this app as a dependency in the manifest.json file: "rihappyio.rihappy-store-components": "0.x".

This app has one block: video-component.

So you can use this app in your page, preferably, because it is easy to access for the user.

### `video-component` props

| Prop name     | Type      | Description                               | Default value                                                 |
| ------------- | --------- | ----------------------------------------- | ------------------------------------------------------------- |
| `isVisible`   | `boolean` | Define if element is visible or invisible | `true`                                                        |
| `controls`    | `boolean` | Set if video controls are active          | `false`                                                       |
| `autoPlay`    | `boolean` | Set if autoplay is active                 | `false`                                                       |
| `muted`       | `boolean` | Set if muted is active                    | `false`                                                       |
| `loop`        | `boolean` | Set if loop is active                     | `false`                                                       |
| `playsInline` | `boolean` | Set if playsinline is active              | `false`                                                       |
| `src`         | `string`  | Video URL.                                | `https://rihappynovo.vteximg.com.br/arquivos/frame-04.mp4.js` |
| `videoType`   | `string`  | Video type.                               | `video/mp4`                                                   |


## Customization

| CSS Handles               |
| ------------------------- |
| `videoComponentContainer` |
| `videoComponentContent`   |