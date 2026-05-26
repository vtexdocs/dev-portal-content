---
title: "CartItem type"
slug: "cartitem-type"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `CartItem` type represents the possible item types within a cart. Its signature and the types used follow this contract:

```typescript
 type CartItem = {
  id: string
  name: string
  quantity: number
  seller: string
  sellingPrice: number
  listPrice: number
  manualPrice?: number
  price: number
  imageUrl: string
  productRefId?: string
  attachments?: Attachment[]
};
```

### Attachment

The `Attachment` type is defined as:

```typescript
type Attachment = {
   name: string;
   content: Record<string, string>;
};
```