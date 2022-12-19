---
title: "Share"
slug: "vtex-store-components-share"
excerpt: "vtex.store-components@3.163.4"
hidden: false
createdAt: "2020-06-03T16:04:30.418Z"
updatedAt: "2022-11-22T18:39:23.096Z"
---
The `Share` component allows shoppers to share a product URL via social media. This component can be imported and used by any VTEX app.

![share-component](https://user-images.githubusercontent.com/67270558/134995068-62543fb4-f2fe-4f06-b220-658f4b4c7eb1.png)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json` file as in the following example:

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
``` 

2. Add the `share` block as a child of the `store.product` template (Product Details Page template). For example:

```json
  "store.product": {
    "children": [
      "share"
    ]
  }
```

3. Then, declare the `share` block using the props stated in the [Props](#props) table. For example:

```json
  "share": {
    "component": "Share"
  }
```

### Props

| Prop name | Type | Description | Default value |
| --------- | ---- | ----------- | ------------- |
| `buttonsContainerClass` | `String` | Button container classes. | `true` |
| `className` | `String` | Main container classes. | `null` |
| `imageUrl` | `String` | Image url to share in social medias. ||
| `options` | `Options` | Share button options, such as `size`. | `{}` |
| `shareLabelClass` | `String` | Share label classes. | `true` |
| `social` | `Social` | Possible social media icons to be displayed. | `{Facebook: true, Twitter: true, WhatsApp: true, Pinterest: true}` |

#### `options` props:

| Prop name | Type | Description |
| --------- | ---- | ----------- | 
| `size` | `Number` | The size of the share button in pixels. |

#### `social` props:

| Prop name | Type | Description |
| --------- | ---- | ----------- |
| `Facebook` | `Boolean` | If Facebook social media will be shown. |
| `Twitter` | `Boolean` | If Twitter social media will be shown. |
| `WhatsApp` | `Boolean` | If WhatsApp social media will be shown. |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| ---------- |
| `shareButtons` |
| `shareContainer` | 
| `shareLabel` | 
| `shareLoader` | 
| `shareSocialButton` | 
| `shareSocialIcon` |