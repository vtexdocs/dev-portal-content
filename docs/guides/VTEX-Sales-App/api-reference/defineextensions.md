---
title: "defineExtensions function"
slug: "defineextensions"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `defineExtensions` function registers one or more React components by associating them with the [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points).

Use this function in your extension entry point file, such as `src/index.tsx`.

## Usage

In the following example, `Recomendations` is rendered in the `cart.cart-list.after` extension point, which is located below the cart items list.

```typescript src/index.tsx
import { defineExtensions } from '@vtex/sales-app';
import { Recommendations } from './Recommendations';

export default defineExtensions({
  'cart.cart-list.after': Recommendations
});
```

## Parameters

The `defineExtensions` function accepts a single parameter, `Record<ExtensionPoints, () => ReactNode>`.

The `ExtensionPoints` type represents the list of valid extension points available in VTEX Sales App.
