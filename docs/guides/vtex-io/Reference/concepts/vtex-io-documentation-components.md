---
title: "Components"
slug: "vtex-io-documentation-components"
hidden: false
createdAt: "2024-06-14T16:48:46.518Z"
updatedAt: "2024-06-14T16:48:46.518Z"
seeAlso: 
  - "/docs/guides/store-framework-apps"
  - "/docs/guides/layout-apps"
---

Components are building blocks used to create storefronts and admin apps, as they are built on the [VTEX IO development platform](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) and [React](https://react.dev/) technology.

These components are modular, reusable pieces of code that encapsulate specific functionality and can be combined to create complex user interfaces. They range from basic elements, such as buttons and forms, to more complex ones, such as product carousels and navigation bars. Conceptually, components resemble JavaScript functions. They take arbitrary inputs, referred to as `props`, and return React elements that articulate what should be displayed on the screen.

## React components and VTEX IO apps

These React components are encapsulated and delivered as VTEX IO apps through the [react builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder). They are also mapped to corresponding [interfaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-interface) via the [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder). This architecture defines how the component should behave and interact within the broader Store Framework environment.

You can use our [native components](#native-components), customize them as needed, or even [create your own components](#custom-components) to meet the specific needs of your projects on the VTEX IO platform.

## Native components

Within the VTEX IO ecosystem, different types of components cater to different aspects of store development. Below are the main types of components:

- [**Basic components**](https://developers.vtex.com/docs/guides/basic-components): Reusable UI elements such as buttons, forms, input fields, and other fundamental interface elements. These components provide the building blocks for constructing more complex UI elements and features.

The [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary) exemplifies a basic storefront component, summarizing essential product information like name, price, and image, which can be seamlessly integrated into other store blocks, such as the [Shelf](https://developers.vtex.com/docs/apps/vtex.shelf).

- [**Store Components**](https://developers.vtex.com/docs/guides/store-components): Collection of components that can be used to create or extend other VTEX apps to improve the functionality and appearance of the storefront. They cover a range of elements, including product displays, navigation bars, checkout processes, and category pages. In this collection, some components offer advanced features, such as product recommendations, search filters, and personalized content delivery.

Learn more about each component of this collection in the [VTEX Store Components](https://developers.vtex.com/docs/apps/vtex.store-components) guide.

## Custom components

When building a [store theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-6-buildingyourownstoretheme), you can leverage existing VTEX IO apps or create custom apps to add new components and extend the platform’s features.

See our guide about how to [develop an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-an-app) or our [Learning Certer](https://learn.vtex.com/docs/course-store-block-lang-en) to learn more about this process.
