---
title: "`useAnalyticsEvent`"
createdAt: "2024-11-08T14:10:15.623Z"
updatedAt: ""
---

The `useAnalyticsEvent` hook intercepts both native and custom events triggered by the [`sendAnalyticsEvent`](/LINK) function. The hook automatically detects the events sent by [`sendAnalyticsEvent`](/LINK) and provides a response to them.

## Import

```tsx
import type { AnalyticsEvent } from '@faststore/sdk'
import { useAnalyticsEvent } from '@faststore/sdk'
```

## Usage

The `useAnalyticsEvent` hook accepts a callback function that runs whenever the `sendAnalyticsEvent` is triggered. The callback function receives the event that triggered its execution as an argument.

Ideally, you should use the `useAnalyticsEvent` hook to transmit events to the analytics provider of your choice (e.g., Google Analytics).

```tsx
import type { AnalyticsEvent } from '@faststore/sdk'
import { useAnalyticsEvent } from '@faststore/sdk'

export const AnalyticsHandler = () => {
  useAnalyticsEvent((event: AnalyticsEvent) => {
    /**
     * This is where you can send events to your analytics provider
     *
     * Example:
     * window.dataLayer.push({ event: event.name, ecommerce: event.params })
     */
  })

  /* ... */
}
```

## Events from external libraries

External libraries can also send events via the Analytics module, which means you might come across unexpected events being intercepted by `useAnalyticsEvent`. This is usually not an issue, as most common analytics providers don't break if you send them meaningless data. However, if that's the case, filter events by name to ensure only the desired events are sent to the provider.
