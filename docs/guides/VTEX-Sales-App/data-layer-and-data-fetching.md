---
title: "Data layer and data fetching"
slug: "data-layer-and-data-fetching"
hidden: false
excerpt: "Learn how to use the data layer and data fetching in VTEX Sales App Extensibility."
createdAt: "2026-05-27T00:00:00.000Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

When using [VTEX Sales App Extensibility](link-placeholder), you may need to present data to the user, whether it’s data from the Sales App flow itself, VTEX APIs, or third-party APIs.

In extension points, there are two ways to interact with data:

- Data-layer resources, such as the `useCart` hook or `useCartItem`.
- Fetching data from VTEX APIs or external APIs

## Extensions data-layer

All interactions with the Sales App data-layer happen through functions and hooks provided by the `@vtex/sales-app` package.

> ℹ️ Whenever possible, we recommend using the data-layer from the Sales App itself, because these data are already cached within the core Sales App’s data-layer, so accessing data (e.g., `useCartItem`) won’t trigger additional requests, which is highly beneficial for both applications performance and your extensions.

For example, if you need to access cart item data while using the `cart.cart-item.after` extension point, you can use the `useCartItem` hook:

```typescript
import { useCartItem } from '@vtex/sales-app'

const MyComponent = () => {
  const { item } = useCartItem()

  return <p>Quantity: {item.quantity}</p>
}
```

> ℹ️ For detailes information about hooks and utilities for extensions, see our [API Reference](link-placeholder).

## Extensions data-fetching

When you need to fetch data from VTEX APIs (e.g., Intelligent Search) or external APIs, you can use the browser's Fetch API to make requests, as shown in the example below:

```tsx
import React, { useState, useEffect } from 'react';

function MyCustomData() {
  const [response, setResponse] = useState({ status: 'loading' });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://my-custom-data-api.com/custom-data');
        const data = await response.json();
        setResponse({ status: 'data', data });
      } catch (error) {
        setResponse({ status: 'error' })
      }
    };
    fetchData();
  }, []);

  if(response.status === 'loading') return <MySkeleton />
  if(response.status === 'error') return null

  return <p>Data: {data.information}</p>
}
```

> ⚠️ When performing data-fetching, it’s important to handle loading states to ensure a good UX. Additionally, allocate space in advance to avoid layout shift. Read more about ["Dealing with Layout Shift"](/sales-app/reference/extension-points#dealing-with-layout-shift).
