---
title: "Using advanced layouts"
slug: "store-framework-using-advanced-layouts"
hidden: false
createdAt: "2025-01-21T16:36:39.917Z"
updatedAt: ""
excerpt: "Discover how to create advanced layouts in your Store Framework store." 
---

In this section, you'll learn how to use advanced layout components in your Store Framework store to improve your storefront design and functionality.

Advanced layout components, as well as other components, are built on the [VTEX IO development platform](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) using [React](https://react.dev/) technology. To learn more about the use of components, see the section [Using components](https://developers.vtex.com/docs/guides/store-framework-using-components).

See below the available [Layout apps](https://developers.vtex.com/docs/guides/layout-apps):

- [Condition Layout](https://developers.vtex.com/docs/apps/vtex.condition-layout): Renders a component in your store when predefined conditions are met.
- [Disclosure Layout](https://developers.vtex.com/docs/apps/vtex.disclosure-layout): Creates a layout structure based on disclosure indicators.
- [Flex Layout](https://developers.vtex.com/docs/apps/vtex.flex-layout): Allows building complex custom layouts using the concept of rows and columns.
- [Modal Layout](https://developers.vtex.com/docs/apps/vtex.modal-layout): Provides blocks to help you create modals in your store.
- [Overlay Layout](https://developers.vtex.com/docs/apps/vtex.overlay-layout): Provides blocks to create a Dropdown, Select, or Tooltip component.
- [Responsive Layout](https://developers.vtex.com/docs/apps/vtex.responsive-layout): Allows you to declare layout structures that will only be rendered in a specific screen-size breakpoint.
- [Slider Layout](https://developers.vtex.com/docs/apps/vtex.slider-layout): Allows building block sliders, such as carousels.
- [Stack Layout](https://developers.vtex.com/docs/apps/vtex.stack-layout): Shows blocks on top of other blocks.
- [Sticky Layout](https://developers.vtex.com/docs/apps/vtex.sticky-layout): Provides layout structures to build elements that remain fixed relative to the viewport in certain contexts.
- [Tab Layout](https://developers.vtex.com/docs/apps/vtex.tab-layout): Creates different layouts within the store's main one using *tabs*.

## Before you begin

<Steps>

### Have a Store Framework store

Make sure your store has a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) developed following the [Getting Started](https://developers.vtex.com/docs/guides/getting-started-3) tutorial.

### Check the builders

Check if the builders are properly installed in your Store Theme. To use builders, your account must have at least version `vtex.builder-hub@0.293.4` installed. Also, you need to specify them in the app's manifest.json file. Learn more in [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders).

You must have at least the following builders configured:

- [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder): Enables the development of Store Framework storefronts.
- [react builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder): Used to develop apps with React when your project requires customized frontend solutions.

### Learn about VTEX IO apps

Familiarize yourself with [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps).
 
</Steps>

## Guides in this section

<Flex>

<WhatsNextCard
title="Building a carousel using Slider Layout"
description="Learn how to integrate and customize carousels for your storefront using Slider Layout."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout"
linkTitle="See more"
/>

<WhatsNextCard
title="Creating modals using icons"
description="Explore how to create modals using icons to enhance user experience."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-modals-using-icons"
linkTitle="See more"
/>

<WhatsNextCard
title="Configuring a quickview using Modal Layout"
description="Learn how to create a quickview feature using the Modal Layout app."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-using-flex-layout"
linkTitle="See more"
/>

<WhatsNextCard
title="Rendering a badge on top of a product"
description="Discover how to render badges on top of products to highlight special offers, discounts, or new arrivals."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-rendering-a-badge"
linkTitle="See more"
/>

<WhatsNextCard
title="Using Flex Layout"
description="Understand the Flex Layout component to create responsive layouts for your store."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-using-flex-layout"
linkTitle="See more"
/>

</Flex>
