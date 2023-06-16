---
title: "Migrating Google Tag Manager app from major 2.x to major 3.x"
slug: "vtex-io-documentation-migrating-google-tag-manager-app"
hidden: false
createdAt: "2021-10-27T17:53:23.675Z"
updatedAt: "2023-05-17T09:17:44.057Z"
category: "Storefront Development"
seeAlso:
 - "/docs/guides/vtex-google-tag-manager"
 - "/docs/guides/vtex-io-documentation-setting-up-google-tag-manager"
---

Version 3.x of VTEX’s Google Tag Manager (GTM) app enables comprehensive tracking of the user's journey within the store, from product views to purchases, using events triggered by the `ecommerceV2` variable. Additionally, it allows stores to send events in both the Google Analytics 4 (GA4) format and the Universal Analytics (UA) format, facilitating a seamless transition to GA4.

## New properties and product schema

To ensure consistency in product information across all areas of the store and effectively track the user's journey, Google Tag Manager 3.x introduces Enhanced Ecommerce properties to the product data schema as events. By adding these properties, stores can include additional information such as product printing, promotion, and sales data, thereby enhancing the overall tracking capabilities and maintaining a unified view of the user's journey throughout the store.

| GTM 3.x property | Type               | Description                                                                 |
| ---------------- | ------------------ | --------------------------------------------------------------------------- |
| `id`             | Renewed property   | Product ID - Previously SKU ID.                                             |
| `variant`        | Renewed property   | SKU ID - Previously SKU Name. The variant of the product, e.g., Rebel pink. |
| `name`           | Renewed property   | Product Name - Previously Product Name or SKU Name.                         |
| `quantity`       | Unchanged property | Product quantity                                                            |
| `price`          | Unchanged property | Product price.                                                              |
| `category`       | Unchanged property | Product category, e.g., Apparel.                                            |
| `brand`          | Unchanged property | Product brand.                                                              |
| `dimension1`     | New property       | Product Reference ID.                                                       |
| `dimension2`     | New property       | SKU Reference ID.                                                           |
| `dimension3`     | New property       | SKU Name (does not include the Product Name).                               |



The `dimension1`, `dimension2`, `dimension3` properties are custom dimensions that you can use to collect and analyze data that Google Analytics does not automatically create.

For more information about custom dimensions and Enhanced Ecommerce, refer to [Custom dimensions and metrics](https://support.google.com/analytics/answer/2709828?hl=en&ref_topic=2709827#configuration&zippy=%2Cin-this-article) and [Google Enhanced ecommerce official guide](https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce#ecommerce-data) respectively.

## Migrating to GTM 3.x

 To migrate to the app's 3.x version, please follow these guides:

1. [Create a Google Analytics 4 property](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-google-tag-manager#create-a-google-analytics-4-property): Refer to the section Create a Google Analytics and follow the instructions provided.
2. Once you have completed the setup, proceed to the  [Setting up Google Tag Manager documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-up-google-tag-manager) documentation for instructions on configuring events, tags, and triggers specifically for GA4.

By following these steps, you'll be able to smoothly migrate to the latest version of the app and set up events, tags, and triggers for both GA4 and UA formats.
