---
title: "ProductSku type"
slug: "productsku-type"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `ProductSku` type represents the structure of a product SKU, including details such as quantity and pricing. Its signature and the types used follow this contract:

```typescript
type ProductSku = {
  id: string;
  name: string;
  quantity: number;
  price: number;
  listPrice: number;
  sellingPrice?: number;
};
```