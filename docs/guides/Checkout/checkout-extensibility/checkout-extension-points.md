---
title: "Checkout extension points"
slug: "checkout-extension-points"
hidden: false
createdAt: "2026-06-09T00:00:00.000Z"
updatedAt: "2026-06-09T00:00:00.000Z"
excerpt: "Explore the available Checkout extension points to extend the UI of Checkout across all of its stages."
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

Checkout offers a variety of extension points across all of its stages, including cart, delivery, cart review, and order placed. These extension points allow you to extend the UX/UI of Checkout to meet your store's specific needs.

Before implementing extensions, make sure you have [set up Buyer Portal Checkout](https://developers.vtex.com/docs/guides/setting-up-buyer-portal-checkout).

## Available extension points

The following table lists all available extension points, the Checkout stage where they render, and whether they may cause layout shift.

| Extension point | Stage | Description | Layout shift |
| --------------- | ----- | ----------- | ------------ |
| [`layout.footer`](#layoutfooter) | Global | Render content in the Checkout footer, available across all Checkout pages. | No |
| [`cart.cart-list.before`](#cartcart-listbefore) | Cart | Render content before the cart item list. | Yes ⚠️ |
| [`cart.cart-list.after`](#cartcart-listafter) | Cart | Render content after the cart item list. | No |
| [`cart.cart-item.after`](#cartcart-itemafter) | Cart | Render content below each cart item row. | Yes ⚠️ |
| [`cart.assembly-options.button.after`](#cartassembly-optionsbuttonafter) | Cart | Render content after the assembly options button of a cart item. | Yes ⚠️ |
| [`cart.order-summary.after`](#cartorder-summaryafter) | Cart | Render content below the order summary on the cart page. | Yes ⚠️ |
| [`cart.order-button.after`](#cartorder-buttonafter) | Cart | Render content after the main order button on the cart page. | Yes ⚠️ |
| [`punchout.cart-item.after`](#punchoutcart-itemafter) | Cart Punchout | Render content below each cart item row on the Punchout cart screen. | Yes ⚠️ |
| [`punchout.order-summary.cta`](#punchoutorder-summarycta) | Cart Punchout | Render a primary action (call to action) in the Punchout order summary. | No |
| [`delivery.cart-item.after`](#deliverycart-itemafter) | Delivery | Render content below each cart item row on the delivery stage. | Yes ⚠️ |
| [`delivery.information-form.after`](#deliveryinformation-formafter) | Delivery | Render content after the delivery information form. | Yes ⚠️ |
| [`delivery.order-button.after`](#deliveryorder-buttonafter) | Delivery | Render content after the order button on the delivery stage. | Yes ⚠️ |
| [`review.cart-item.after`](#reviewcart-itemafter) | Review | Render content below each cart item row on the review stage. | Yes ⚠️ |
| [`payment.cart-item.after`](#paymentcart-itemafter) | Payment | Render content below each cart item row on the payment stage. | Yes ⚠️ |
| [`payment.order-button.after`](#paymentorder-buttonafter) | Payment | Render content after the order button on the payment stage. | Yes ⚠️ |
| [`order-placed.cart-item.after`](#order-placedcart-itemafter) | Order Placed | Render content below each cart item row on the order placed stage. | Yes ⚠️ |

> ⚠️ Some extension points may cause layout shifts and are marked with `Yes ⚠️` in the table above. If your extension relies on data fetching (for example, Fetch API calls), reserve space to handle dynamic content smoothly by using loading states and skeletons.
> Fully static extensions and extensions that rely solely on data-layer hooks (such as `useCart`) shouldn't cause layout shifts, because Checkout always renders extensions seamlessly within the existing layout. Even so, implementing skeletons or loading states is recommended to improve the overall UX/UI.

## Global extension points

These extension points are global and available across all Checkout pages, from the cart to the order placed stage.

### `layout.footer`

Use this extension point to render content in the Checkout footer. Since it's global, the content is displayed consistently across all Checkout pages.

![Footer](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/layout.footer.webp)

## Cart extension points

Use the following extension points to customize different areas of the cart experience.

### `cart.cart-list.before`

Render content before the cart item list, ideal for cart-level messaging that should appear above the items. Use the [`useCart` hook](https://developers.vtex.com/docs/guides/usecart-hook) to access and mutate cart data.

![cart-list.before](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/cart.cart-list.before.webp)

### `cart.cart-list.after`

Render content after the cart item list and before the bottom of the cart page. Use the [`useCart` hook](https://developers.vtex.com/docs/guides/usecart-hook) to access and mutate cart data.

![Shopping cart page with one item and order summary, highlighting the full cart list area below the main cart content.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/cart.cart-list.after.webp)

### `cart.cart-item.after`

Render content immediately below each cart item row, allowing you to attach item-specific content such as warranties, services, or custom details for that product. Use the [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook) to access data for the current item and the [`useCart` hook](https://developers.vtex.com/docs/guides/usecart-hook) to access and mutate cart data.

![Shopping cart page showing one MacBook Pro item with delivery details, quantity selector, remove button, and a highlighted placeholder area for the cart item component below the product row.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/cart.cart-item.after.webp)

### `cart.assembly-options.button.after`

Render content after the assembly options button of a cart item. Use the [`useCart` hook](https://developers.vtex.com/docs/guides/usecart-hook) to access and mutate cart data.

![cart.assembly-options.button.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/cart.assembly-options.button.after.webp)

### `cart.order-summary.after`

Append components under the order summary on the cart page, such as financing simulators, loyalty messages, or upsell suggestions.

![Shopping cart page with subtotal, discount, total, and Continue button, highlighting the order summary component in the right sidebar.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/cart.order-summary.after.webp)

### `cart.order-button.after`

Render content after the main order button on the cart page.

![cart.order-button.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/cart.order-button.after.webp)

## Cart Punchout extension points

Use the following extension points to customize the [Punchout cart screen](https://developers.vtex.com/docs/guides/punchout-cart-integration).

### `punchout.cart-item.after`

Render content below each cart item row on the Punchout cart screen, for example to add per-item options or attachments. Use the [`useCartPunchout`](https://developers.vtex.com/docs/guides/usecartpunchout-hook) and [`useCartItem`](https://developers.vtex.com/docs/guides/usecartitem-hook) hooks to read and update the cart.

![punchout.cart-item.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/punchout.cart-item.after.webp)

### `punchout.order-summary.cta`

Render a primary action button in the Punchout order summary sidebar, typically used to transfer the cart back to the eprocurement system. Use the [`useRedirect` hook](https://developers.vtex.com/docs/guides/useredirect-hook) to redirect the user to a target URL.

![punchout.order-summary.cta](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/punchout.order-summary.cta.webp)

## Delivery extension points

Use the following extension points to customize the delivery stage.

### `delivery.cart-item.after`

Render content below each cart item row on the delivery stage. Use the [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook) to access data for the current item.

![delivery.cart-item.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/delivery.cart-item.after.webp)

### `delivery.information-form.after`

Render content after the delivery information form.

![delivery.information-form.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/delivery.information-form.after.webp)

### `delivery.order-button.after`

Render content after the order button on the delivery stage.

![delivery.order-button.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/delivery.order-button.after.webp)

## Review extension points

Use the following extension point to customize the review stage.

### `review.cart-item.after`

Render content below each cart item row on the review stage. Use the [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook) to access data for the current item.

![review.cart-item.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/review.cart-item.after.webp)

## Payment extension points

Use the following extension points to customize the payment stage.

### `payment.cart-item.after`

Render content below each cart item row on the payment stage. Use the [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook) to access data for the current item.

![payment.cart-item.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/checkout-extensibility/payment.cart-item.after.webp)

### `payment.order-button.after`

Render content after the order button on the payment stage.

![payment.order-button.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/payment.order-button.after.webp)

## Order Placed extension points

Use the following extension point to customize the order placed stage.

### `order-placed.cart-item.after`

Render content below each cart item row on the order placed stage. Use the [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook) to access data for the current item.

![order-placed.cart-item.after](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Checkout/order-placed.cart-item.after.webp)

## Displaying extension points in dev mode

You can view all available extension points directly in the Checkout UI. To do this, run Checkout using the Checkout CLI with the `--show-placeholders` flag (see the [Checkout CLI documentation](https://developers.vtex.com/docs/guides/checkout-cli) for more information):

```bash
yarn checkout dev <account> <project-path> <port> --show-placeholders
```

The `--show-placeholders` flag tells Checkout to display placeholders where extension points are located.
