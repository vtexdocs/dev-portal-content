---
title: "`sendAnalyticsEvent`"
createdAt: "2024-11-08T14:34:00.623Z"
updatedAt: ""
---

The `sendAnalyticsEvent` function is responsible for firing events in the browser, adhering to the [Google Analytics 4 (GA4) data model](https://developers.google.com/analytics/devguides/collection/ga4/reference/events). This function is primarily related to ecommerce-tracking but also supports[custom events](/LINK), serving as a centralized point for managing events.

> ⚠️ `sendAnalyticsEvent` does not send events to any analytics provider. To intercept events fired by this function, use the [`useAnalyticsEvent`](/LINK) hook.

## Import

```tsx
import { sendAnalyticsEvent } from '@faststore/sdk'
```

## Usage

In the component related to the event, declare a callback function. In this function, define an event object with the desired event type (e.g., `add_to_cart`) and call the `sendAnalyticsEvent`. Then, pass the related event as an argument. Finally, call the callback function in the event trigger (e.g., `onClick`).

Take the following example of an `add_to_cart` event triggered by the `button` component:

```tsx
import { useCallback } from 'react'
import { sendAnalyticsEvent } from '@faststore/sdk'

const MyComponent = () => {
  const addToCartCallback = useCallback(() => {
    /* ... */

    const addToCartEvent = {
      type: 'add_to_cart',
      data: {
        items: [
          /* ... */
        ],
      },
    }

    sendAnalyticsEvent(addToCartEvent)
  }, [])

  return <button onClick={addToCartCallback}>Add to cart</button>
}
```

Check the list of [Available types](/LINK).

## Exporting custom event types with generics

The `sendAnalyticsEvent` function supports generics, enabling you to extend default types or modify existing ones. This approach provides type-checking and code suggestions for your custom event properties.

Take the following example of providing a custom type reference for `sendAnalyticsEvent`:

```tsx
import { sendAnalyticsEvent } from '@faststore/sdk'

interface CustomEvent {
  name: 'custom_event'
  params: {
    customProperty?: string
  }
}

/**
 * By passing CustomEvent as a generic type to sendAnalyticsEvent, you'll receive code hints for all properties of this type, including params subfields.
 */
sendAnalyticsEvent<CustomEvent>(/* ... */)
```
