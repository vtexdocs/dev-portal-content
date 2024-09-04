---
title: "Building pages"
slug: "building-pages"
hidden: false
createdAt: "2024-09-04T19:00:34.804Z"
updatedAt: ""
excerpt: "Discover how to leverage Store Framework to build various types of pages tailored to your business needs."
---

VTEX IO streamlines page creation by offering a set of pre-built components and [development tools](https://developers.vtex.com/docs/guides/developer-experience#developer-tools). These resources simplify the building and customization of different page types, such as product details pages, promotional layouts, and custom pages.

This section covers a range of page-building scenarios, and each guide focuses on practical implementation, ensuring you can effectively develop pages that meet your business needs.

## Before you begin

<Steps>

### Develop your Store Theme

Ensure your store has a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) developed according to the [Storefront](https://developers.vtex.com/docs/guides/getting-started-3) guide.

### Check the builders

Check if the builders are properly installed in your Store Theme. To use builders, you must have at least the `vtex.builder-hub@0.293.4` version installed in your account. Also, you need to specify them in the app’s `manifest.json` file. Learn more at [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders).

You must have at least the [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder) configured. This builder enables the development of Store Framework storefronts.

### Learn about VTEX IO apps

Become familiar with the [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps).

</Steps>

## Essential concepts

To better understand how to build your store’s pages, you should comprehend the concepts of  **components** and **templates**.

Components are building blocks built on the [VTEX IO development platform](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) and [React](https://react.dev/) technology, used to create storefronts and admin apps.

Learn more in the [Using components] section.

A template refers to the structural layout of your site’s pages. Templates define the components for various pages, such as the home, product, and search results pages, by declaring `json` blocks that render these components.

Learn more in the [Configuring templates](https://developers.vtex.com/docs/guides/vtex-io-documentation-4-configuringtemplates) guide.

## Guides in this section

<Flex>

<WhatsNextCard
title="Building a product details page"
description="Discover how to create a product page for your store."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-product-details-page"
linkTitle="See more"
/>

<WhatsNextCard
title="Building a search results page with multiple layouts"
description="Learn how to create search result pages leveraging our VTEX IO apps."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-search-results-page-with-multiple-layouts"
/>

<WhatsNextCard
title="Creating a Black Friday page from template"
description="Explore our templates to create promotional pages.”
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-black-friday-page-from-template"
linkTitle="See more"
/>

<WhatsNextCard
title="Creating a custom search results page"
description="Learn how to customize your search results page and enhance user interaction."
linkTo=”https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-custom-search-results-page”
linkTitle="See more"
/>

<WhatsNextCard
title="Creating a new custom page"
description="Understand the process of building a custom page that meets specific business needs."
linkTo=https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page"
linkTitle="See more"
/>

<WhatsNextCard
title="Customizing the Header and Footer blocks by page"
description="Discover how to optimize your site’s navigation by customizing header and footer blocks by page."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-customizing-the-header-and-footer-blocks-by-page"
linkTitle="See more"
/>

<WhatsNextCard
title="Creating an institutional page with Content types"
description="Learn how to create an institutional page using various content types."
linkTo="https://developers.vtex.com/docs/guides/creating-an-institutional-page-with-content-types-1"
linkTitle="See more"
/>

</Flex>
