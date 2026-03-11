---
title: "useCartPunchout hook"
slug: "usecartpunchout-hook"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
---

The `useCartPunchout` hook allows you to access cart data and perform mutations that are reflected across the Checkout data layer.

> ℹ️ This hook is only available in some extension points.

## Usage

```js
import { useCartPunchout } from '@vtex/checkout'

const TotalItems = () => {
  const cart = useCartPunchout()

  return <div>Items: {cart.items.length}</div>
}
```

You can also use `useCartPunchout` to update the cart by mutating the items list:

```js //src/index.tsx
import { useCartPunchout } from '@vtex/checkout'

const AddItemExample = () => {
  const cart = useCartPunchout()
  const addItem = () => cart.addItem({
    quantity: 1,
    seller: '1',
    id: '8392'
  })

  return <button onClick={addItem}>Add to cart</button>
}
```

You can also remove items from the cart:

```js //src/index.tsx
import { useCartPunchout, useCartItem } from '@vtex/checkout'

const RemoveItemExample = () => {
  const cart = useCartPunchout()
  const cartItem = useCartItem()

  const removeItem = () => cart.removeItem({
    originalIndex: cartItem.originalIndex
  })

  return <button onClick={removeItem}>Remove from cart</button>
}
```

`useCartPunchout` does not expose every operation supported by the [Checkout API](https://developers.vtex.com/docs/guides/checkout-api-overview). If you update Checkout data through the Checkout API directly, call `sync()` afterward to refresh the UI and ensure it reflects the latest cart state.

This is useful for actions not covered by the hook, such as updating shipping information through [`POST` Add shipping address and select delivery option](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/shippingData) endpoint.

```js //src/index.tsx
import { useCartPunchout } from '@vtex/checkout'

const MyComponent = () => {
  const cart = useCartPunchout()

  const handleClick = async() => {
    // Performs some interaction with some VTEX API
    await cart.sync();
  }

  return <button onClick={handleClick}>Add to cart</button>
}
```

## Parameters

The `useCartPunchout` hook does not accept any parameters.

## Returns

The `useCartPunchout` hook returns an object with the following property:

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

### sync

type: `sync: () => Promise<void>`

## Extension Points

This hook is available in the following extension points:

- `punchout.cart-item.after`
- `punchout.order-summary.cta`
