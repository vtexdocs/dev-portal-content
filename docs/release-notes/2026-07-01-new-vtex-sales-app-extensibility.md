---
title: "New VTEX Sales App Extensibility"
slug: "2026-07-01-new-vtex-sales-app-extensibility"
type: "added"
createdAt: "2026-07-01T00:00:00.000Z"
updatedAt: "2026-07-01T00:00:00.000Z"
hidden: false
excerpt: "Customize the assisted-sales journey in Sales App through predefined extension points."
---

[VTEX Sales App Extensibility](https://developers.vtex.com/docs/guides/vtex-sales-app-extensibility) allows merchants to customize the default assisted-sales journey by rendering components and adding capabilities at predefined slots in the Sales App interface. The feature is available in open beta for all stores that use [Sales App](https://help.vtex.com/docs/tracks/what-is-vtex-sales-app).

To support the development and implementation of extensions, merchants and partners can use the [VTEX Sales App Extensions Skill](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-skill), an AI-powered skill that comes with built-in knowledge of the Sales App and the FastStore monorepo.

## What changed?

**VTEX Sales App Extensibility** introduces eight predefined extension points across key contexts of the sales journey:

- **Cart and checkout**: `cart.cart-item.after`, `cart.cart-list.after`, `cart.order-summary.after`
- **Product Detail Page (PDP)**: `pdp.sidebar.before`, `pdp.sidebar.after`, `pdp.content.after`
- **Menu and drawer**: `menu.item`, `menu.drawer-content`

Extensions can integrate with external APIs and safely interact with data from other applications. The solution is built around three core principles:

- **Security:** Safer code implementation for developers.
- **Stability:** Application stability is preserved even when customizations fail.
- **Compatibility:** Extensions remain compatible with existing customizations.

Common use cases include loyalty program integrations, additional services (such as warranties or insurance), integrations with VTEX solutions outside the default Sales App flow, and consolidation of sales representatives' tasks on a single platform.

## What needs to be done?

Implementation of **VTEX Sales App Extensibility** is handled by merchants and partners. Follow the [Sales App extensions implementation](https://developers.vtex.com/docs/guides/sales-app-extensions-implementation) guide to get started.

> ℹ️ Use the [VTEX Sales App Extensions Skill](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-skill) as an AI assistant throughout the definition and implementation of extensions.
