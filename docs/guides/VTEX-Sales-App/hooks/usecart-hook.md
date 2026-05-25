---
title: "useCart hook"
slug: "usecart-hook"
hidden: false
createdAt: "2026-05-25T19:03:19.410Z"
---

The `useCart` hook allows you to access cart data and perform mutations that will reflect on other entities within the Sales App data layer.

This hook is available in the following extension points:

- `cart.cart-list.after`
- `cart.cart-item.after`
- `cart.order-summary.after`
- `pdp.sidebar.before`
- `pdp.sidebar.after`
- `pdp.content.after`

See all available extension points in the guide [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points).

## Usage

```tsx src/index.tsx
import { useCart } from '@vtex/sales-app'

const TotalItems = () => {
const cart = useCart()

  return <div>Items: {cart.items.length}</div>

}
```

You can also use `useCart` to interact with the Sales App data layer by mutating the cart items list:

```tsx src/index.tsx
import { useCart } from '@vtex/sales-app'

const TotalItems = () => {
const cart = useCart()

  const addItem = () => cart.addItem({
    quantity: 1,
    seller: '1',
    id: '8392'
  })

  return <button onClick={addItem}>Add to cart</button>

}
```

## Parameters

The `useCart` hook doesn't accept any parameters.

## Returns

The `useCart` hook returns an object with the following properties:

### `orderFormId`

- type `orderFormId: string | undefined`

### `value`

- type `value: number`

### `items`

- type: [`CartItem[]`](https://developers.vtex.com/docs/guides/cartitem-type)

### `totalizers`

- type [`Totalizers[]`](https://developers.vtex.com/docs/guides/totalizers-type)

### `clientProfileData`

- type: [`ClientProfileData`](https://developers.vtex.com/docs/guides/clientprofiledata-type)

### `giftCards`

- type: `GiftCard[]`

Gift cards currently attached to the cart.

### `addItem`

- type: `addItem: (data: UseCartAddItemData) => Promise<void>`

The `UseCartAddItemData` type is an object with the following structure:

```typescript
type UseCartAddItemData = {
  id: string;
  quantity: number;
  seller: string;
  attachments?: Attachment[];
};
```

### `removeItem`

- type `removeItem: (id: string, index: number) => Promise<void>`

### `addCoupon`

- type `addCoupon: (coupon: string) => Promise<void>`

### `addGiftCard`

- type: `addGiftCard: (redemptionCodeOrGiftCard: string | GiftCard, provider?: string) => Promise<void>`

Adds a gift card to the cart payment data. You can pass either:

- a **redemption code** (`string`) and optionally a `provider`, or
- a **GiftCard object** (when you already have the gift card data).

The `GiftCard` type follows this structure:

```typescript
export type GiftCard = {
  id: string
  redemptionCode?: string | null
  name: string
  caption: string
  value: number
  balance: number
  provider: string
  groupName?: string | null
  inUse: boolean
  isSpecialCard: boolean
}
```

Example using a redemption code:

```typescript src/index.tsx
import { useCart } from '@vtex/sales-app'

const AddGiftCard = () => {
const cart = useCart()

const add = async () => {
  await cart.addGiftCard('ABC-123', 'my-giftcard-provider')
  await cart.sync()
}

return <button onClick={add}>Add gift card</button>
}
```

### `sync`

Syncs the cart with the latest data from the Order Form. This is useful to ensure that the cart reflects any changes made outside Sales App.

- type `sync: () => Promise<void>`
