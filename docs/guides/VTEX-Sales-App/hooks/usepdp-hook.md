---
title: "usePDP hook"
slug: "usepdp-hook"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `usePDP` hook allows you to access Product Detail Page (PDP) data and perform mutations that will reflect on other entities within the Sales App data layer.

This hook is available in the following extension points:

* `pdp.sidebar.before`
* `pdp.sidebar.after`
* `pdp.content.after`

See all available extension points in the guide [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points).

## Usage

```typescript src/index.tsx
import { usePDP } from '@vtex/sales-app'

const Product= () => {
  const { productSku } = usePDP()

  return <div>Product name: {productSku?.name}</div>
}
```

## Parameters

The `usePDP` hook doesn't accept any parameters.

## Returns

The `usePDP` hook returns an object with the following property:

### `productSku`

* **type:** [`ProductSku`](https://developers.vtex.com/docs/guides/productsku-type)
