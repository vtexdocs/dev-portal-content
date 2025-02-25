---
title: Cart
createdAt: "2025-01-16T14:47:00.000Z"
---

The Cart module offers features to manage the store shopping cart. It handles large orders and complex ecommerce operations, such as marketplace integration, coupons, gift options, and promotions.

## Cart data storage

Cart data is saved in the browser's [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API), ensuring that users' carts remain saved even when they close the browser. The data is structured as follows:

![Cart SDK Architecture](https://vtexhelp.vtexassets.com/assets/docs/src/Cart___74c390e654f666b3a2adb7b6a0b5ecf7.png)

## Cart modes

The Cart module provides two modes:

- [**Pure**](#pure-mode) (default): Operates on the client side, storing cart data locally and supporting offline use. It lacks server-side validation and may not handle complex cases like unavailable items. Ideal for basic cart functionality.

- [**Optimistic**](#optimistic-mode): Handles complex ecommerce operations like unavailable items. Validates the cart state on the server using debounced requests.

## Pure mode

The Pure mode stores cart data locally in the browser. This allows users to add or remove items and keep their carts even if they close the browser. However, it can't validate items on the server side.

The Pure cart also works offline but doesn't automatically correct errors. For example, if a customer adds an out-of-stock item, the cart won't prevent it. The item will appear in the cart even though it's unavailable.

### Implementing Pure mode

To implement the Pure cart mode, follow these steps:

1. Wrap your app with the `CartProvider` component.
2. Access the cart using the `useCart` hook:

    ```tsx
    import { CartProvider, useCart } from '@faststore/sdk'

    // In the App's root component:
    const App = ({ children }) => {
    return <CartProvider>{children}</CartProvider>
    }

    // In your component:
    const MyComponent = () => {
    const { items } = useCart()

    return <div>Number of items on cart: {items.length}</div>
    }
    ```

## Optimistic mode

Optimistic mode validates the cart state on the server and handles edge cases like unavailable items. For example, Optimistic mode checks with the store system if a customer tries to add an out-of-stock item. If the product is unavailable, it's removed from the cart, and the customer is notified.

This feature can be implemented in the `optimistic` mode using the `validateCart` callback function, which allows developers to make requests and cause side effects to the cart. If the function returns `null`, the cart behavior doesn't change. However, if you opt to change the cart state to handle a specific side effect, it must return the new cart state within the callback function.

### Implementing Optimistic mode

To implement the Optimistic cart mode, follow these steps:

1. Use the `CartProvider` component with the `optimistic` mode.
2. Implement the `validateCart` function to handle server-side validation:

    ```tsx
    import { CartProvider, useCart, Cart } from '@faststore/sdk'

    // In the App's root component:
    const validateCart = async (cart: Cart) => {
    const response = await fetch(...)

    if (response) {
        return response
    }

    return null
    }

    const App = ({children}) => {
    return <CartProvider mode="optimistic" onValidateCart={validateCart}>{children}</CartProvider>
    }

    // In your component:
    const MyComponent = () => {
    const { items, isValidating } = useCart()

    if (isValidating) {
        return <div>Cart is validating</div>
    }

    return <div>Number items in cart: {items.length}</div>
    }
    ```
