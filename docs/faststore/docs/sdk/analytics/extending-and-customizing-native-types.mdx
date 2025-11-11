---
title: "Extending and customizing native types"
---

The [Analytics](https://developers.vtex.com/docs/guides/faststore/analytics-overview) module offers built-in [ecommerce events](https://support.google.com/analytics/answer/14434488?hl=en) based on the [Google Analytics 4 (GA4) data model](https://developers.google.com/analytics/devguides/collection/ga4/reference/events).

While these parameters are often the most used in online stores, you may need to track additional properties to monitor specific behaviors that are only valuable to particular business models. For example, a subscription box service would want to track details like `subscription_frequency` or `is_renewal` beyond standard purchase data to understand customer lifetime value and churn better.

FastStore natively supports extending and customizing Analytics native types. The Analytics module can accept new types and also export its native types. You don't need to rewrite an event interface's code to make minor additions. Also, since the Analytics module is built with [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html), you can rewrite only part of a type, like the `Item` structure,  if necessary.

In this guide, you'll learn how to extend and customize native types from the Analytics module.

## Before you begin

- Review the list of [Available types](https://developers.vtex.com/docs/guides/faststore/analytics-overview#list-of-native-event-types) that you can extend.

- Familiarize yourself with [Type Aliases or Extended Interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces) in TypeScript, which are the techniques you'll use to extend the desired type.

## Extending event interfaces

To add new properties to an existing event interface, you must create a new TypeScript interface that extends the native FastStore Analytics event type. This step allows you to add custom event-level details that aren't part of the standard GA4 data model but are important for your business. For example, knowing whether the cart contains a product bundle can be key to a specific promotion or product strategy.

1. Create a new interface that extends the native FastStore Analytics event type. For example, to add an `isProductBundle` property to `AddToCartEvent`:

    ```ts
    import type { AddToCartEvent } from '@faststore/sdk'

    interface AddToCartExtended extends AddToCartEvent {
        isProductBundle: boolean
    }
    ```

   - The `isProductBundle` property is a flag that indicates whether the added item is part of a product bundle.
   - The `AddToCartExtended` interface now includes all properties from `AddToCartEvent` (`name` and `params`) and the new `isProductBundle` property.

2. To use this extended type when sending an event, ensure your event object conforms to the `AddToCartExtended` new interface structure inside the component you send analytics events. See the following example:

    ```ts
    import { analytics } from 'src/sdk/analytics'

    const extendedAddToCartEvent: AddToCartExtended = {
    name: 'add_to_cart',
    params: {
        currency: 'USD',
        value: 12.99,
        items: [
        {
            item_id: 'SKU123',
            item_name: 'Product A',
            price: 12.99,
            quantity: 1,
        },
        ],
    },
    isProductBundle: true, // The new custom property
    };

    // Call your analytics send method with the extended event object:
    analytics.sendEvent(extendedAddToCartEvent);
    ```

## Overriding `Item` properties using generics

To add custom dimensions or metrics to individual items within an event without changing the overall event structure, use [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) to override the `Item` property. This allows you to attach unique custom attributes to individual products or services in your catalog.

1. Create an interface for your custom `Item` properties. For example, to add `dimension10` to an item:

    ```ts
    import type { AddToCartEvent, Item } from '@faststore/sdk'

    interface ItemExtension {
    dimension10: string
    }
    ```

    - `dimension10` serves as a customizable placeholder for item-specific dimensions in analytics, such as "product color family" and "licensing type". This placeholder allows for the representation of custom data.

2. Create a new type that combines the native `Item` type with your `ItemExtension` using a TypeScript intersection (`&`):

    ```ts mark=7,8,9
    import type { AddToCartEvent, Item } from '@faststore/sdk'

    interface ItemExtension {
    dimension10: string
    }

    type ItemExtended = Item & ItemExtension

    type AddToCartWithExtendedItems = AddToCartEvent<ItemExtended>
    ```

    - `AddToCartExtended` has the same properties as `AddToCartEvent` (`name` and `params`), but the items inside the `params` property will now have the `ItemExtended type`.

Below, see an example of how you can use this type when sending an event in a component:

```ts
import { analytics } from 'src/sdk/analytics'

const addToCartWithExtendedItemsEvent: AddToCartWithExtendedItems = {
  name: 'add_to_cart',
  params: {
    currency: 'USD',
    value: 25.00,
    items: [
      {
        item_id: 'SKU456',
        item_name: 'Product B',
        price: 25.00,
        quantity: 1,
        dimension10: 'Custom Value Here', // The new custom property for the item
      },
    ],
  },
};

analytics.sendEvent(addToCartWithExtendedItemsEvent);
```

- `const addToCartWithExtendedItemsEvent: AddToCartWithExtendedItems`: Declares a constant variable named `addToCartWithExtendedItemsEvent` and explicitly tells that it must conform to the `AddToCartWithExtendedItems` type.
- `name: 'add_to_cart'`: Default event name recognized by GA4.
- `params: { ... }`: Holds the default GA4 parameters for an `add_to_cart` event (`currency`, `value`, `items`).
- dimension10: `ItemExtended` now includes the `dimension10` custom dimension.

## Best practices for validating extended types at runtime

Since TypeScript types are erased during compilation, validate your extended event data at runtime to ensure analytics tools like [Google Analytics 4](https://support.google.com/analytics/topic/14089939?hl=en&ref_topic=14090456&sjid=1384409646416570899-SA) receive correctly formatted events. Consider the following methods:

> ⚠️ These methods can help catch runtime errors. Choose what fits your workflow.

| **Method** | **Purpose** |
| --------- | ------------ |
| Installing a validation library | Use a validation library to catch typos and validate backend data. |
| Intercepting events | Verify events before they reach analytics tools by wrapping `analytics.sendEvent(safeEvent)` with validation logic to filter invalid events in your code. |
| Debugging with [GA4 DebugView](https://support.google.com/analytics/answer/7201382?hl=en#zippy=) | Enable debug mode and monitor real-time events in GA4's DebugView interface. For more information, see the [GA4 DebugView](https://support.google.com/analytics/answer/7201382?hl=en#zippy=) guide. |
| Adding unit tests | Write tests that verify your event objects catches schema violations during development. |
