---
title: "New VTEX Sales App Extensibility"
slug: "2026-07-01-new-vtex-sales-app-extensibility"
type: "added"
createdAt: "2026-07-01T00:00:00.000Z"
updatedAt: "2026-07-01T00:00:00.000Z"
hidden: false
excerpt: "Customize the assisted-sales journey in Sales App through predefined extension points."
---

[VTEX Sales App Extensibility](https://developers.vtex.com/docs/guides/vtex-sales-app-extensibility) lets merchants customize the default assisted-sales journey by rendering components and adding capabilities at predefined slots in the Sales App interface. The feature is available in open beta for all VTEX stores.

## What changed?

**VTEX Sales App Extensibility** introduces eight predefined extension points across key contexts of the sales journey:

- **Cart and checkout**: `cart.cart-item.after`, `cart.cart-list.after`, `cart.order-summary.after`
- **Product Detail Page (PDP)**: `pdp.sidebar.before`, `pdp.sidebar.after`, `pdp.content.after`
- **Menu and drawer**: `menu.item`, `menu.drawer-content`

Extensions can integrate with external APIs and interact with data from other applications safely. The solution is built around three core principles:

- **Security:** safer code implementation for developers.
- **Stability:** application stability is preserved even when customizations fail.
- **Compatibility:** extensions remain compatible with existing customizations.

Common use cases include loyalty program integrations, additional services (such as warranties or insurance), integrations with VTEX solutions outside the standard Sales App flow, and consolidation of seller tasks in a single platform.

## What needs to be done?

The implementation of **VTEX Sales App Extensibility** is the responsibility of merchants and partners. Follow the [Sales App extensions implementation](https://developers.vtex.com/docs/guides/sales-app-extensions-implementation) guide to get started.

> ℹ️ Use the [VTEX Sales App Extensions Skill](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-skill) as an AI assistant throughout the definition and implementation process.
