---
title: "Components"
slug: "vtex-io-documentation-components"
hidden: false
createdAt: "2024-02-06T12:06:55.338Z"
updatedAt: "2024-02-06T12:06:55.338Z"
excerpt: 
---

In the Store Framework context, **components** refer to the building blocks used to create storefronts, admin interfaces, and other parts of the VTEX platform; that is, they are [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps).

These components are modular, reusable pieces of code that encapsulate specific functionality and can be combined to create complex user interfaces.

In addition to providing storefront components for rendering UI elements and admin components for managing store settings and configurations, the VTEX IO apps, or simply components, provide blocks for defining layout structures and extensions for integrating with third-party services or adding new features.

>ℹ️ Refer to the following documentation to know more about the [basic components](https://developers.vtex.com/docs/guides/basic-components), the [store components](https://developers.vtex.com/docs/guides/store-components), and the [advanced components](https://developers.vtex.com/docs/guides/advanced-components).

## Types of components

Components play a crucial role in developing VTEX stores and applications, enabling developers to create rich, interactive user experiences and empowering merchants to manage their businesses effectively.

Within the VTEX IO ecosystem, various types of components cater to different aspects of store development:

- **Storefront Components**: These are components used to build the frontend of online stores. They include UI components for displaying products, navigation menus, search bars, cart summaries, and more. Storefront components are typically built using React and can be customized and extended to fit specific design requirements.

For instance, the [Product Summary app](https://developers.vtex.com/docs/apps/vtex.product-summary) exemplifies a storefront component, summarizing essential product information like name, price, and image, which can be seamlessly integrated into other store blocks, such as the [Shelf](https://developers.vtex.com/docs/apps/vtex.shelf).

- **Admin Components**: These components are used to build the administrative interfaces of VTEX stores, where merchants manage their products, orders, customers, promotions, and other aspects of their business. Admin components provide tools and forms for performing administrative tasks efficiently.

As an example, consider the [Reviews & Ratings app](https://developers.vtex.com/docs/apps/vtex.reviews-and-ratings), which facilitates customer interaction by enabling them to submit product reviews and ratings for products and see them while navigating the store.

Once installed, it is available in the VTEX Admin:

![vtex-reviews-and-ratings-2](https://github.com/vtex-apps/search-result/assets/112641072/d7cba1bb-c05e-4f9f-98f3-4dceb680a488)

- **Blocks**: predefined combinations of components and functionality that serve as building blocks for creating store layouts and pages. Blocks can include storefront components, admin components, and developed custom components. Blocks help streamline the process of building and customizing store layouts by providing ready-to-use sections of functionality.

Considering the Reviews & Ratings example given above, go to the `interfaces.json` file within the app code. There you can see the blocks that compose it:

   ```json
   // reviews-and-ratings/store/interfaces.json
   {
     "product-reviews.vtex": {
       "component": "Reviews"
     },
     "product-rating-summary.vtex": {
       "component": "RatingSummary"
     },
     "product-rating-inline.vtex": {
       "component": "RatingInline"
     }
   }
   ```

Refer to our documentation to know more about [blocks](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition#blocks) and their relation with [interfaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-interface).
 
- **Extensions**: specialized components or modules that extend the functionality of the VTEX platform. They can add new features, integrate third-party services, enhance performance, or provide other valuable capabilities. Extensions are often developed by third-party developers or partner solution providers and can be installed and configured to meet specific business needs.

The extensions include VTEX IO apps, payment connectors, and marketplace integrations. These solutions are available in the [VTEX App Store](https://apps.vtex.com/).
 
## Custom components

When building a store, you can leverage existing VTEX IO apps or create custom apps to add new components and extend the platform’s capabilities.

Check out our guide about how to [develop an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-an-app) or our [Learning Certer](https://learn.vtex.com/docs/course-store-block-lang-en) to know more about this process.