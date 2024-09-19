---
title: "Routing"
slug: "routing"
hidden: false
createdAt: "2024-09-19T13:32:26.286Z"
updatedAt: ""
excerpt: "Learn how routing is managed in VTEX IO Store Framework."
---

A route maps a URL pattern and an HTTP request method to an action. It defines how the application responds to client requests for specific endpoints.

When using [VTEX IO Store Framework](https://developers.vtex.com/docs/guides/store-framework), you do not need to manage routing and HTTP methods directly. Instead, routing and HTTP request methods are managed by either the [Rewriter](https://developers.vtex.com/docs/apps/vtex.rewriter) app or the [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder), depending on the route type. This allows you to focus on creating and managing route paths and page templates.

In Store Framework, different apps and builder manage various types of routes. The table below outlines the primary managers for each route type:

| Route type      | Responsibility             | Description                                                                                   |
|---------------------|------------------------------------|---------------------------------------------------------------------------------------------------|
| **Product routes**    |  Rewriter app                   | Routes related to product pages, forwarded by the Rewriter app to the rendering pipeline. |
| **Search routes**     | Rewriter app                     | Routes related to search result pages, processed and forwarded by the Rewriter app. |
| **Catalog routes**     | Rewriter app                  | Custom routes for predefined templates (e.g., [department](https://github.com/vtex-apps/store/blob/master/store/routes.json#L27), [brand](https://github.com/vtex-apps/store/blob/master/store/routes.json#L21), and [category](https://github.com/vtex-apps/store/blob/master/store/routes.json#L33) handled by the Rewriter app and mapped to the appropriate page.|
| **Custom routes**    |  Store builder              | User-defined routes for custom landing pages or other routes that fall outside of predefined product or category routes, directly managed by the store builder and forwarded to the render server. |

The [Rewriter app](https://developers.vtex.com/docs/apps/vtex.rewriter) interprets the requested path, identifies the route type, and then forwards the route path to the rendering pipeline. Learn more in [Rewriter GraphQL API](https://developers.vtex.com/docs/apps/vtex.rewriter@1.63.0/rewriter-graphql-api).

The [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder) forwards custom route paths directly to the render server. To learn how to create a custom page, see the [Creating a new custom page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) guide.

In this section, you will learn how to manage routes in your Store Framework store.

## Before you begin

<Steps>

### Develop your Store Theme

Make sure your store has a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) developed following the [Getting Started](https://developers.vtex.com/docs/guides/getting-started-3) tutorial.

### Check the builders

Check if the builders are properly installed in your Store Theme. To use builders, your account must have at least version `vtex.builder-hub@0.293.4` installed. Also, you need to specify them in the app's `manifest.json` file. Learn more in [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders).

Make sure the [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder) is configured, as it enables the development of Store Framework storefronts.

### Check Rewriter installation

To check if the [Rewriter app](https://developers.vtex.com/docs/apps/vtex.rewriter) is installed in your store, follow the guide [Listing an account's apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-listing-an-accounts-apps) and search for `vtex.rewriter` in the **Installed apps** list. If it is not, install the app by following the guide [Installing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app).

</Steps>

## Guides in this section

<Flex>

<WhatsNextCard
title="Best practices for associating a custom page with a content type"
description="Learn how to effectively associate custom pages with content types in VTEX IO."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-associating-a-custom-page-with-a-content-type"
linkTitle="See more"
/>

<WhatsNextCard
title="Enabling 404 pages"
description="Learn how to enable and configure 404 error pages for better user experience."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-enabling-404-pages"
linkTitle="See more"
/>

<WhatsNextCard
title="Managing URL redirects"
description="Discover how to manage URL redirects to ensure seamless navigation."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-managing-url-redirects"
linkTitle="See more"
/>

<WhatsNextCard
title="Using several service workers in your store"
description="Explore how to use multiple service workers to enhance your store’s performance and offline capabilities."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-using-several-service-workers-in-your-store"
linkTitle="See more"
/>

</Flex>
