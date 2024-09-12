---
title: "Styling"
slug: "styling"
hidden: false
createdAt: "2024-09-12T12:52:42.285Z"
updatedAt: ""
excerpt: "Discover how to customize your store layout with Store Framework."
---

Styling directly impacts user experience and brand perception. A well-styled store attracts visitors and keeps them engaged, encouraging navigation and interaction with your site.

In [Store Framework](https://developers.vtex.com/docs/guides/store-framework), styling is flexible and customizable, allowing you to create a visual identity that aligns with your brand. Whether you need to make minor adjustments or comprehensive changes, Store Framework’s tools enable you to tailor each visual element to meet specific business needs.

In this section, you will learn how to leverage our styling tools to customize your store.

## Before you begin

<Steps>

### Develop your Store Theme

Make sure your store has a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) developed following the [Getting Started](https://developers.vtex.com/docs/guides/getting-started-3) tutorial.

### Check the builders

Check if the builders are properly installed in your Store Theme. To use builders, your account must have at least version `vtex.builder-hub@0.293.4` installed. Also, you need to specify them in the app's `manifest.json` file. Learn more in [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders).

You must have at least the following builders configured:

- [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder): Enables the development of Store Framework storefronts.
- [styles builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-styles-builder): Exports CSS configurations for Store Framework blocks.

### Create store pages

Develop your store pages by following the [Building pages](https://developers.vtex.com/docs/guides/building-pages) guides.

</Steps>

## Essential concepts

To better understand the styling process in Store Framework, you should know the concept of CSS Handle, which is a CSS class that maps to an HTML element. It serves as a layout-building assistant for your store, allowing you to customize any block by applying CSS classes within the Store Theme’s code. Therefore, CSS Handles streamline the layout customization of your store by targeting specific elements in your custom CSS.

Each VTEX component is preconfigured with unique CSS Handles, allowing you to apply styles to specific parts of a component without changing its structure.

## Guides in this section

<Flex>

<WhatsNextCard
title="Contributing with new CSS Handles"
description="Enhance the styling options available for VTEX IO components."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-contributing-with-new-css-handles"
linkTitle="See more"
/>

<WhatsNextCard
title="Customizing your store's icons"
description="Replace or customize the icons used across your store."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-customizing-your-stores-icons"
linkTitle="See more"
/>

<WhatsNextCard
title="Customizing your store’s typography"
description="Adjust the typography in your store to create a cohesive design."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-customizing-your-stores-typography"
linkTitle="See more"
/>

<WhatsNextCard
title="Interactively inspecting storefront blocks"
description="Inspect and identify block elements in your store for targeted customization."
linkTo="https://developers.vtex.com/docs/guides/how-to-interactively-inspect-blocks-on-a-store-framework-store"
linkTitle="See more"
/>

<WhatsNextCard
title="Using CSS handles for store customizations"
description="Target and style specific elements within your store using CSS Handles."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization"
linkTitle="See more"
/>

<WhatsNextCard
title="Using the Markers prop to customize a block's message"
description="Customize the messaging and appearance of blocks in your store using the markers prop."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-markers-prop-to-customize-a-blocks-message"
linkTitle="See more"
/>

</Flex>
