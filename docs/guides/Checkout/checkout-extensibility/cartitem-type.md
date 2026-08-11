---
title: "CartItem type"
slug: "cartitem-type"
hidden: false
createdAt: "2026-06-16T00:00:00.000Z"
updatedAt: "2026-06-16T00:00:00.000Z"
excerpt: "Reference for the CartItem type, which represents the possible item types within a cart in Checkout extensions."
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

The `CartItem` type represents the possible item types within a cart. In summary, its signature and the types used follow this contract:

```ts
type CartItem = CartAvailableItem | CartUnavailableItem;
```

Here are the respective types for `CartAvailableItem` and `CartUnavailableItem`:

```ts
type CartAvailableItem = BaseCartItem & {
  status: 'available';
  price: number;
};

type CartUnavailableItem = BaseCartItem & {
  status: 'unavailable';
  price?: number;
};
```

## BaseCartItem

Both `CartAvailableItem` and `CartUnavailableItem` extend `BaseCartItem`, which has the following structure:

```ts
type BaseCartItem = {
  id: string;
  originalIndex: number;
  quantity: number;
  imageUrl: string;
  productUrl: string;
  offerings: Array<Offering>;
};
```

The `originalIndex` property represents the unique position of the item in the cart and is used for operations like removing items via the `removeItem` function available in the [`useCart`](https://developers.vtex.com/docs/guides/usecart-hook) and [`useCartPunchout`](https://developers.vtex.com/docs/guides/usecartpunchout-hook) hooks.

## Offering

The `Offering` type is defined as:

```ts
type Offering = {
  type: string;
  name: string;
  id: string;
};
```
