---
title: "Implementing marketplaces"
slug: "implementing-marketplaces"
hidden: false
excerpt: "Learn about VTEX marketplace models to sell on other marketplaces or host multiple sellers."
createdAt: ""
---

A marketplace is an ecommerce platform where multiple sellers offer their products, while the marketplace operator manages the platform and the overall customer experience. With VTEX, you can operate as a marketplace, hosting products from various sellers, and sell your products on other marketplaces.

> ℹ️ Marketplace capabilities are available for all VTEX storefront technologies.

## Marketplace models

VTEX supports multiple marketplace models. Choose the one that best fits your operation:

### Acting as marketplace

When your VTEX store receives products from sellers, you're **acting as a marketplace**. You can integrate with the following types of sellers:

- **VTEX sellers:** Sellers that already have VTEX stores. Connect them to your marketplace natively with no additional development.
- **External sellers:** Sellers that don't use the VTEX platform but want to sell their products in your VTEX marketplace. This integration may require building a custom connector.

> ℹ️ Learn more in the guide [Acting as marketplace](https://developers.vtex.com/docs/guides/implementing-marketplaces-acting-as-marketplace).

### Acting as seller

When your VTEX store sells its products on other marketplaces, you're **acting as a seller**. You can integrate with the following types of marketplace connectors:

- **Native marketplace connectors:** Pre-built integrations maintained by VTEX that allow you to sell in external marketplaces without developing your own connector. These connectors are optimized for specific marketplaces and are fully integrated with VTEX Admin for catalog, inventory, and order flows.
- **External marketplace connectors:** Non‑native integrations, not built or maintained by VTEX, used to connect your VTEX store to marketplaces that don't have a VTEX native connector or when you need custom behavior that native connectors don't cover.

> ℹ️ Learn more in the guide [Acting as seller](https://developers.vtex.com/docs/guides/implementing-marketplaces-acting-as-seller)

## Next steps

To start implementing your operation, follow the instructions for the marketplace type that aligns with your business needs.

<WhatsNextCard
title="Acting as marketplace"
description="Learn how to implement a marketplace that receives products from sellers."
linkTo="/docs/guides/implementing-marketplaces-acting-as-marketplace"
linkTitle="See more"
/>

<WhatsNextCard
title="Acting as seller"
description="Learn how to sell your products in other marketplaces."
linkTo="/docs/guides/implementing-marketplaces-acting-as-marketplace"
linkTitle="See more"
/>
