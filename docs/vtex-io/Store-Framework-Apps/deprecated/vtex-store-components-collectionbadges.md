---
title: "Collection Badges"
slug: "vtex-store-components-collectionbadges"
hidden: false
createdAt: "2020-06-03T16:04:30.346Z"
updatedAt: "2021-10-25T14:50:59.973Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-collectionbadges-0.png)

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
  <img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/deprecated/..." alt="...">
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