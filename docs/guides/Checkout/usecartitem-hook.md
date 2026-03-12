---
title: "useCartItem hook"
slug: "usecartitem-hook"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
---

The `useCartItem` hook allows you to access detailed information about an individual cart item. This is particularly useful when you need to retrieve or display specific data related to a single item in the cart.

> ℹ️ This hook is only available in some extension points.

## Usage

```js
import { useCartItem } from '@vtex/checkout';

const CartItemDetails = () => {
  const cartItem = useCartItem();

  return (
    <div>
      <p>Product: {cartItem.id}</p>
      <p>Quantity: {cartItem.quantity}</p>
      <p>Price: {cartItem.price}</p>
      <img src={cartItem.imageUrl} alt="Product image" />
    </div>
  );
};
```

## Parameters

The `useCartItem` hook does not accept any parameters.

## Returns

The `useCartItem` returns a `CartItem` object for the current cart item context.

## Extension Points

This hook is available in the following extension points:

- `cart.cart-item.after`
- `punchout.cart-item.after`
- `delivery.cart-item.after`
- `review.cart-item.after`
- `payment.cart-item.after`
- `order-placed.cart-item.after`
