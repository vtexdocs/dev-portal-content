---
title: "Data layer and data fetching in VTEX Sales App Extensibility"
slug: "data-layer-and-data-fetching-in-vtex-sales-app-extensibility"
hidden: false
excerpt: "Learn how to use the data layer and data fetching for Sales App extensions."
createdAt: "2026-05-27T00:00:00.000Z"
updatedAt: "2026-06-02T00:00:00.000Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact [Support](https://help.vtex.com/en/support).

When [creating a Sales App extension](https://developers.vtex.com/docs/guides/creating-sales-app-extensions), you may need to present data to the user, whether it's from the Sales App flow, VTEX APIs, or third-party APIs.

There are two ways of enabling your extensions to interact with data:

- Data layer resources, such as the `useCart` hook or `useCartItem`.
- Data fetching from VTEX APIs or external APIs.

## Data layer in extensions

All interactions with the Sales App data layer happen through functions and hooks provided by the `@vtex/sales-app` package.

> ℹ️ Whenever possible, use the Sales App data layer because this data is already cached in the core data layer. This approach prevents additional requests, optimizing application performance, which benefits your extensions.

For example, if you need to access cart item data while using the `cart.cart-item.after` extension point, you can use the `useCartItem` hook:

```tsx
import { useCartItem } from '@vtex/sales-app'

const MyComponent = () => {
  const { item } = useCartItem()

  return <p>Quantity: {item.quantity}</p>
}
```

> ℹ️ For detailed information about hooks and types for extensions, see the guide [Sales App extensions hooks and types](https://developers.vtex.com/docs/guides/sales-app-extension-hooks-and-types).

## Data fetching in extensions

When you need to fetch data from VTEX APIs (for example, Intelligent Search) or external APIs, you can use the browser's Fetch API to make requests, as shown in the example below:

> ⚠️ Extensions run in the browser, so authentication tokens and API keys included in requests can be exposed to users. The example below uses a public endpoint that doesn't require credentials. If your API requires authentication, create a [VTEX IO app](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-creating-the-new-app) to proxy the request and handle authentication on the server.

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

> ⚠️ When fetching data, handle loading states to ensure a better user experience. Additionally, allocate space in advance to avoid layout shifts. Learn more in the guide [Exploring Sales App extensions](https://developers.vtex.com/docs/guides/exploring-sales-app-extensions).
