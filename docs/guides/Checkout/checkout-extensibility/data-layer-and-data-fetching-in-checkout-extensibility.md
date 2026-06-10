---
title: "Data-layer and data-fetching in Checkout extensions"
slug: "data-layer-and-data-fetching-in-checkout-extensibility"
hidden: true
createdAt: "2026-06-10T00:00:00.000Z"
updatedAt: "2026-06-10T00:00:00.000Z"
excerpt: "Access the Checkout data layer with hooks and fetch data from VTEX or external APIs in your extensions."
---

> ⚠️ This feature is only available for stores using B2B Buyer Portal, which is currently available to selected accounts.

When extending the UX/UI of Checkout, you may need to present data to the user, whether it's data from the Checkout flow itself, additional information from VTEX APIs, or data from your own or third-party APIs.

In extension points, there are two main ways to interact with data:

- Data-layer resources, such as the [`useCart`](https://developers.vtex.com/docs/guides/usecart-hook) or [`useCartItem`](https://developers.vtex.com/docs/guides/usecartitem-hook) hooks.
- Fetching data from VTEX APIs or external APIs.

> ℹ️ In this release, the extensions data layer includes a limited set of hooks and utilities.

## Data-layer

Whenever possible, prefer using the data layer from Checkout itself. This is recommended because this data is already cached within the core Checkout's data layer, so accessing data (for example, through `useCartItem`) won't trigger additional requests, which is highly beneficial for both application performance and your extensions.

All interactions with the Checkout data layer happen through functions and hooks provided by the `@vtex/checkout` package. For example, if you need to access cart item data while using the `cart.cart-item.after` extension point, you can use the [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook):

```tsx
import { useCartItem } from '@vtex/checkout';

const MyComponent = () => {
  const item = useCartItem();

  return <p>Quantity: {item.quantity}</p>;
};
```

> ℹ️ For more information on Checkout data-layer hooks and utilities, see [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points) and the available [Checkout hooks](https://developers.vtex.com/docs/guides/usecart-hook).

## Data-fetching

The data in the Checkout layer might not always be sufficient for building your extension. Sometimes, you may need to communicate with a VTEX API (such as Intelligent Search) or with your own or third-party APIs.

In these cases, you can use the browser's Fetch API to make requests, just as you would in your everyday React applications:

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
        setResponse({ status: 'error' });
      }
    };

    fetchData();
  }, []);

  if (response.status === 'loading') return <MySkeleton />;
  if (response.status === 'error') return null;

  return <p>Data: {response.data.information}</p>;
}
```

> ⚠️ When performing data-fetching, handle loading states to ensure a good UX. Additionally, allocate space in advance to avoid layout shift. For more information, see how to deal with layout shift in [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points).
