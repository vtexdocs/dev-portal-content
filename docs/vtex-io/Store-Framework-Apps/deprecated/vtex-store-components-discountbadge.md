---
title: "Discount Badge"
slug: "vtex-store-components-discountbadge"
hidden: false
createdAt: "2020-06-03T16:04:30.348Z"
updatedAt: "2021-10-25T14:49:23.936Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-discountbadge-0.png)

>⚠️ **Warning**
>
> **The Discount Badge block has been deprecated in favor of the [Product Price app](https://developers.vtex.com/docs/guides/vtex-product-price).** Although support for this block is still granted, we strongly recommend you to update your store theme with the Product Price's blocks in order to keep up with the component's evolution.

`Discount Badge` is a VTEX component that shows a discount of a product. This component can be imported and used by any VTEX App.

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/store-components/blob/master/docs/README.md#usage).

To import it into your code:

```js
import { DiscountBadge } from 'vtex.store-components'
```

You can use it in your code like a React component with the jsx tag: `<DiscountBadge />`.

```jsx
<DiscountBadge listPrice={commertialOffer.ListPrice}
                sellingPrice={commertialOffer.Price}
                label={badgeText}>
  <img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/deprecated/" alt="">
</DiscountBadge>
```

## Configuration

| Prop name      | Type      | Description                          |
| -------------- | --------- | ------------------------------------ |
| `listPrice`    | `Number!` | Product's default price              |
| `sellingPrice` | `Number!` | Product's price with discount        |
| `label`        | `String`  | Label to track the discount percent  |
| `children`     | `Node!`   | Element where the badge is displayed |

## Styles API

This app provides some CSS classes as an API for style customization. You should follow the Styles API instruction in the main [README](https://github.com/vtex-apps/store-components/blob/master/docs/README.md#styles-api).

### CSS namespaces

Below, we describe the namespaces that are defined in the `DiscountBadge`.

| Class name                | Description                  | Component Source                                  |
| ------------------------- | ---------------------------- | ------------------------------------------------- |
| `discountContainer`       | The discount container       | [index](/react/components/DiscountBadge/index.js) |
| `discountInsideContainer` | The discount inner container | [index](/react/components/DiscountBadge/index.js) |