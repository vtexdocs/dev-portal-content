---
title: "Buyer Portal Checkout Extensibility"
slug: "buyer-portal-checkout-extensibility"
excerpt: "Learn about Checkout extensions, how to set them up and build them, and where you can place them across the Checkout journey."
hidden: false
createdAt: "2026-06-09T00:00:00.000Z"
updatedAt: "2026-06-09T00:00:00.000Z"
---

> ⚠️ This feature is only available for stores using B2B Buyer Portal, which is currently available to selected accounts.

Buyer Portal Checkout Extensibility lets you extend the default checkout journey with capabilities aligned to your business model, such as external integrations and custom UI. Using extension points across all Checkout stages (Cart, Delivery, Review, Payment, and Order Placed), you can render your own components without changing checkout's core behavior.

The technical aspects of Checkout extensions are covered in the following articles:

- [Setting up Buyer Portal Checkout](https://developers.vtex.com/docs/guides/setting-up-buyer-portal-checkout) — Install the Buyer Portal Checkout modules in your FastStore monorepo, create a Checkout project, and preview your extensions in development.
- [Getting started with Checkout extensions](https://developers.vtex.com/docs/guides/getting-started-with-checkout-extensions) — Understand the structure of a Buyer Portal Checkout extensions project and build your first extension.
- [Deploying Checkout extensions](https://developers.vtex.com/docs/guides/deploying-checkout-extensions) — Deploy your extensions to production, generate preview deploys, and troubleshoot build failures.
- [Using CSS in Checkout extensions](https://developers.vtex.com/docs/guides/css-styling-in-checkout-extensibility) — Style your extensions using CSS Modules, global imports, and CSS variables.
- [Data-layer and data-fetching in Checkout extensions](https://developers.vtex.com/docs/guides/data-layer-and-data-fetching-in-checkout-extensibility) — Access the Checkout data layer with hooks and fetch data from VTEX or external APIs.
- [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points) — Explore the available extension points across all Checkout stages, learn how to deal with layout shift, and display extension points in dev mode.
- Checkout hooks — Consult the hooks available to access the data layer and perform actions from your extensions:
  - [`useCart` hook](https://developers.vtex.com/docs/guides/usecart-hook): Access cart data and perform mutations that are reflected across the checkout data layer.
  - [`useCartItem` hook](https://developers.vtex.com/docs/guides/usecartitem-hook): Access detailed information about the current cart item.
  - [`useCartPunchout` hook](https://developers.vtex.com/docs/guides/usecartpunchout-hook): Access cart data and perform mutations on the Punchout cart screen.
  - [`useRedirect` hook](https://developers.vtex.com/docs/guides/useredirect-hook): Redirect the user to another page.
  - [`useSettings` hook](https://developers.vtex.com/docs/guides/usesettings-hook): Access checkout settings, such as branding data like logos and colors.
  - [`useExtension` hook](https://developers.vtex.com/docs/guides/useextension-hook): Access information about the current account and the extension point where your extension is running.
- [Punchout cart integration](https://developers.vtex.com/docs/guides/punchout-cart-integration) — Customize the Punchout cart screen using Checkout extension points, allowing buyers to transfer their cart back to the eprocurement system.
