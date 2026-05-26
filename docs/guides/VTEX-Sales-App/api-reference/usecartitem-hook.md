---
title: "useCartItem hook"
slug: "usecartitem-hook"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `useCartItem` hook allows you to access detailed information about an individual cart item. This is particularly useful when you need to retrieve or display specific data related to a single item in the cart.

## Extension Points

This hook is available in the following extension point:

* `cart.cart-item.after`

See all available extension points in the guide [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points).

## Usage

```typescript
import { useCartItem } from '@vtex/sales-app';

const CartItemDetails = () => {
  const { item } = useCartItem();

  return (
    <div>
      <p>Product: {item.id}</p>
      <p>Quantity: {item.quantity}</p>
      <img src={item.imageUrl} alt="Product image" />
    </div>
  );
};
```

## Parameters

The `useCartItem` hook doesn't accept any parameters.

## Returns

The `useCartItem` hook returns an object with the following properties:

### `item`

* **type:** [`CartItem[]`](https://developers.vtex.com/docs/guides/cartitem-type)| undefined`.

### `itemIndex`

* **type:** `number | undefined`

### `changeItem`

* **type:** `(data: UseCartItemChangeItemData) => Promise<void>`

The `UseCartItemChangeItemData` type is an object with the following structure:

```typescript
type UseCartItemChangeItemData = {
  quantity?: number
  attachments?: Attachment[]
};
```

### `changePrice`

To use this function, the feature of `manual price` must be active. To check if it's active, use the [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) endpoint, making the `allowManualPrice` field true.

* **type:** `changePrice: (price: number) => Promise<void>`
