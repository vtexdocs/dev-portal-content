---
title: "Collection Badges"
slug: "vtex-store-components-collectionbadges"
excerpt: "vtex.store-components@3.132.2"
hidden: false
createdAt: "2020-06-03T16:04:30.346Z"
updatedAt: "2021-10-25T14:50:59.973Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red)

>⚠️ **Warning**
>
> **The Collection Badges block has been deprecated**. Despite this, support for it is still granted.

`Collection Badges` is a VTEX component that will render an image with the list of collection badges located at the bottom.
This component can be imported and used by any VTEX app.

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/store-components/blob/master/README.md#usage).

To import it into your code:

```tsx
import { CollectionBadges } from 'vtex.store-components'
```

You can use it in your code like a React component with the `JSX` tag: `<CollectionBadges>`.

```tsx
<CollectionBadges collectionBadgesText={[ 'foo', 'bar' ]}>
  <img src="..." alt="...">
</CollectionBadges>
```

### Configuration

| Prop name              | Type       | Description                                                                  | Default Values |
| ---------------------- | ---------- | ---------------------------------------------------------------------------- | -------------- |
| `collectionBadgesText` | `string[]` | An array of collection badges text                                           | `[]`           |
| `children`             | `Node`     | Children components that should be rendered inside the collection badge item | `undefined`    |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles           |
| --------------------- |
| `collectionContainer` |
| `item`                |