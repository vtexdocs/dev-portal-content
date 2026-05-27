---
title: "Data-layer and data-fetching in extensions"
slug: "data-layer-and-data-fetching-in-extensions"
hidden: false
excerpt: "Learn how to use the data-layer and data-fetching in VTEX Sales App Extensibility."
createdAt: "2026-05-27T00:00:00.000Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

When using [VTEX Sales App Extensibility](link-placeholder), you may need to present data to the user, whether it’s data from the Sales App flow itself, VTEX APIs, or third-party APIs.

In extension points, there are two ways to interact with data:

- Data-layer resources, such as the `useCart` hook or `useCartItem`.
- Data-fetching from VTEX APIs or external APIs.

## Data-layer in extensions

All interactions with the Sales App data-layer happen through functions and hooks provided by the `@vtex/sales-app` package.

> ℹ️ Whenever possible, we recommend using the Sales App data-layer, because this data is already cached in the core data-layer. Accessing it (e.g., via `useCartItem`) won’t trigger additional requests, which improves application performance and benefits your extensions.

For example, if you need to access cart item data while using the `cart.cart-item.after` extension point, you can use the `useCartItem` hook:

```typescript
import { useCartItem } from '@vtex/sales-app'

const MyComponent = () => {
  const { item } = useCartItem()

  return <p>Quantity: {item.quantity}</p>
}
```

> ℹ️ For detailed information about hooks and utilities for extensions, see the [API Reference](link-placeholder).

## Data-fetching in extensions

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

  if (response.status === 'loading') return <MySkeleton />
  if (response.status === 'error') return null

  return <p>Data: {data.information}</p>
}
```

> ⚠️ When performing data-fetching, it’s important to handle loading states to ensure a good user experience. Additionally, allocate space in advance to avoid layout shift. Read more about [Dealing with Layout Shift](link-placeholder).
