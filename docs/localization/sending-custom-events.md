---
title: "Sending custom events"
---

Even though the [Analytics](https://developers.vtex.com/docs/guides/faststore/analytics-overview) module supports [Google Analytics ecommerce events](https://support.google.com/analytics/answer/14434488?hl=en) by default, a store may need to monitor customer activity not covered by the Analytics module. In these cases, it is still possible to use the [`sendAnalyticsEvent`](https://developers.vtex.com/docs/guides/faststore/analytics-send-analytics-event) and [`useAnalyticsEvent`](https://developers.vtex.com/docs/guides/faststore/analytics-use-analytics-event) functions to fire and intercept custom events. In this guide, learn how to define and send custom events.

{/* > ℹ For a use case scenario of this implementation, see the [Use case: Implementing custom newsletter analytics events](https://docs.google.com/document/d/11ziaTwu4I-n_YcbDQi8Gavt5ss7hGqMXM393I7JsjCk/edit?tab=t.0) guide. */}

## Instructions

### Step 1 - Declaring an interface for your custom event

To fire a custom event, you first need to declare an interface that describes the structure of your event object, including all its properties and types. To do that, you can:

    - [Create a new event interface](#creating-a-new-event-interface)
    - [Extend existing types from the Analytics module](#extending-existing-types-from-the-analytics-module)
    - [Override multiple types](#overriding-multiple-types)

#### Creating a new event interface

You can use the `sendAnalyticsEvent` function to create a custom event interface. This function demands that the event contains two properties:

| Property name | Type | Description |
| ------------------- |-------- |---------------- |
| `name`            | `string` | The name of the event presented in Analytics reports. The `name` doesn't need to follow any event name conventions related to natively supported events. |
| `params` | `any` | Any type and value used by your custom event. |

Take the following example to track when a user adds a product to their wishlist by defining the `WishlistEvent`:

    ```ts
    import { sendAnalyticsEvent } from '@faststore/sdk'

    interface WishlistEvent {
        name: 'wishlist-event',
        params: {
        productId: string
        productName: string
        }
        userId: string
        isLoggedIn: boolean
    }

    sendAnalyticsEvent<WishlistEvent>({ name, params, userId, isLoggedIn })
    ```

This custom event interface allows you to capture when a user adds a product to their wishlist. It logs details like the `productId`, `productName`, and whether the user is logged in (`isLoggedIn`). This data can then be sent to your analytics tool to better understand customer behavior, such as which products are popular on wishlists and how engagement varies between logged-in and anonymous users.

#### Extending existing types from the Analytics module

If your event is related to an existing one, you can extended existing types {/*ADD THE LINK FOR THE EXTENDING EXISTING EVENTS ONCE WE HAVE THE DOCUMENTATION*/} from the Analytics module by using the [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) available on the [`sendAnalyticsEvent`](https://developers.vtex.com/docs/guides/faststore/analytics-send-analytics-event) function.

Take the following example where the `AddToCartEvent` interface is extended to also accept the `couponCode` property, useful to track if a customer applied a coupon code when adding an item to the cart.:

    ```ts
    import type { AddToCartEvent } from '@faststore/sdk'
    import { sendAnalyticsEvent } from '@faststore/sdk'

    interface AddToCartExtended extends AddToCartEvent {
        couponCode: string
    }

    /* ... */

    sendAnalyticsEvent<AddToCartExtended>({ name, params, couponCode })
    ```

#### Overriding multiple types

If you have multiple custom events, like adding to the cart, removing from the cart, or viewing products, you can create a unified type to manage them all and easily fire extended events:

    ```ts
    /* types.ts */
    import { sendAnalyticsEvent } from '@faststore/sdk'

    type AddToCartExtended = /* ... */
    type RemoveFromCartExtended = /* ... */
    type ViewItemExtended = /* ... */
    type SelectItemExtended = /* ... */

    type ExtendedEvents =
    | AddToCartExtended
    | RemoveFromCartExtended
    | ViewItemExtended
    | SelectItemExtended

    type SendExtendedAnalyticsEvent = (event: ExtendedEvents) => void

    export const sendExtendedAnalyticsEvent: SendExtendedAnalyticsEvent = (event) =>
    sendAnalyticsEvent<ExtendedEvents>(event)
    ```

    ```ts
    /* MyComponent.tsx */
    import { sendExtendedAnalyticsEvent } from './types'

    /* ... */

    sendExtendedAnalyticsEvent({ /* Extended event object */})
    ```

The example above sets up a flexible way to fire various custom events. Instead of managing multiple event types separately, the purpose of the example is to handle them all through a single interface, making. You can use this setup to track diverse customer interactions, such as adding/removing products from the cart, viewing products, or saving items to the wishlist.

### Step 2 - Intercepting custom events

After creating or extending an event interface, you'll need to intercept these events using the `useAnalyticsEvent` hook. You can do that in the following:

    ```ts
    import { useAnalyticsEvent } from '@faststore/sdk'

    import type { ArbitraryEvent } from './types'

    export const AnalyticsHandler = () => {
    useAnalyticsEvent((event: ArbitraryEvent) => {
    })

    /* ... */

    return null
    }
    ```

Also, notice that to target extended properties of events, you'll also need to configure the types of your [`useAnalyticsEvent`](/reference/sdk/analytics/useAnalyticsEvent) callback function to expect an event of such type.

    ```ts
    import { useAnalyticsEvent } from '@faststore/sdk'

    import type { ExtendedEvents } from './types'

    export const AnalyticsHandler = () => {

    useAnalyticsEvent((event: ExtendedEvents) => {
        /* ... */
    })

    /* ... */

    return null
    }
    ```

    > ℹ  By typing the callback function with the extended types, you are able to reference properties that are not natively offered by the analytics module.

### Step 3 - Firing custom events

Now that you have declared your event interface and intercepted them with the `useAnalyticsEvent` hook, you can implement it in your components to fire the event when desired.

    ```ts
    import { useCallback } from 'react'
    import { sendAnalyticsEvent } from '@faststore/sdk'

    const MyComponent = () => {
    const arbitraryEvent = useCallback(() => {
        /* ... */

        const arbitraryEvent = {
        type: 'arbitrary-event',
        data: {
            items: [
            /* ... */
            ],
        },
        }

        sendAnalyticsEvent(arbitraryEvent)
    }, [])

    return <button onClick={arbitraryEvent}>Arbitrary button</button>
    }
    ```
