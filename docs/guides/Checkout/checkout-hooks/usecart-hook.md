---
title: "useCart hook"
slug: "usecart-hook"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
excerpt: "Learn how to use the useCart hook to access and modify cart data in Checkout extensions, including adding and removing cart items."
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

The `useCart` hook allows you to access cart data and perform mutations that are reflected across other entities within the Checkout data layer.

> ℹ️ This hook is only available in some extension points.

## Usage

```js
import { useCart } from '@vtex/checkout';

const TotalItems = () => {
  const cart = useCart();

  return <div>Items: {cart.items.length}</div>;
};
```

You can also use `useCart` to interact with the Checkout data layer by mutating the cart items list:

```js
import { useCart } from '@vtex/checkout';

const AddItemExample = () => {
  const cart = useCart();
  const addItem = () => cart.addItem({
    quantity: 1,
    seller: '1',
    id: '8392'
  });

  return <button onClick={addItem}>Add to cart</button>;
};
```

You can also remove items from the cart:

```js
import { useCart, useCartItem } from '@vtex/checkout';

const RemoveItemExample = () => {
  const cart = useCart();
  const cartItem = useCartItem();

  const removeItem = () => cart.removeItem({
    originalIndex: cartItem.originalIndex
  });

  return <button onClick={removeItem}>Remove from cart</button>;
};
```

## Parameters

The `useCart` hook does not accept any parameters.

## Returns

The `useCart` hook returns an object with the following properties:

### items

- `items: CartItem[]`

The current list of items in the cart.

### addItem

- `addItem: (data: AddItemData) => Promise<void>`

The `AddItemData` type is an object with the following structure:

```js
type AddItemData = {
   quantity: number;
   id: string;
   seller: string;
};
```

### removeItem

- `removeItem: (data: RemoveItemData) => Promise<void>`

The `RemoveItemData` type is an object with the following structure:

```js
type RemoveItemData = {
   originalIndex: number;
};
```

## Extension Points

This hook is available in the following [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points):

- `cart.cart-list.before`
- `cart.cart-list.after`
- `cart.cart-item.after`
- `cart.assembly-options.button.after`
