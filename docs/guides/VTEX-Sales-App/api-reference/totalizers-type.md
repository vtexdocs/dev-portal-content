---
title: "Totalizers type"
slug: "totalizers-type"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `Totalizers` type represents the structure of the summary totals returned in an orderForm or cart, such as shipping, taxes, or discounts. Its signature and the types used follow this contract:

```typescript
type Totalizers = {
  id: string
  name: string
  value: number
};