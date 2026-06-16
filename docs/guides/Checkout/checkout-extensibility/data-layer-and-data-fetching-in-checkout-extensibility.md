---
title: "Data layer and data fetching in Checkout extensions"
slug: "data-layer-and-data-fetching-in-checkout-extensibility"
hidden: true
createdAt: "2026-06-10T00:00:00.000Z"
updatedAt: "2026-06-10T00:00:00.000Z"
excerpt: "Access the Checkout data layer with hooks and fetch data from VTEX or external APIs in your extensions."
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

When [creating a Checkout extension](https://developers.vtex.com/docs/guides/getting-started-with-checkout-extensions), you may need to present data to the user, whether it is data from the Checkout flow, VTEX APIs, or third-party APIs.

There are two ways to enable your extensions to interact with data:

- Data layer resources, such as the [`useCart`](https://developers.vtex.com/docs/guides/usecart-hook) or [`useCartItem`](https://developers.vtex.com/docs/guides/usecartitem-hook) hooks.
- Data fetching from VTEX APIs or external APIs.

> ℹ️ In this release, the extensions data layer includes a limited set of hooks and utilities.

## Data layer in extensions

All interactions with the Checkout data layer happen through functions and hooks provided by the `@vtex/checkout` package.

> ℹ️ Whenever possible, use the Checkout data layer, because this data is already cached in the core data layer. This approach prevents additional requests, enhancing application performance and benefiting your extensions.

For example, if you need to access cart item data while using the `cart.cart-item.after` extension point, you can use the [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook):

```tsx
import { useCartItem } from '@vtex/checkout';

const MyComponent = () => {
  const item = useCartItem();

  return <p>Quantity: {item.quantity}</p>;
};
```

> ℹ️ For detailed information about the available hooks and the extension points where they can be used, see [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points) and the [Checkout hooks](https://developers.vtex.com/docs/guides/usecart-hook).

## Data fetching in extensions

When you need to fetch data from VTEX APIs (for example, Intelligent Search) or external APIs, you can use the browser's Fetch API to make requests, as shown in the example below:

> ⚠️ Extensions run in the browser, so authentication tokens and API keys included in requests can be exposed to users. The example below uses a public endpoint that does not require credentials. If your API requires authentication, create a [VTEX IO app](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-creating-the-new-app) to proxy the request and handle authentication on the server.

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

> ⚠️ When fetching data, handle loading states to ensure a better user experience. Additionally, allocate space in advance to avoid layout shift. For more information, see how to deal with layout shift in [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points).
