---
title: "Routing"
slug: "routing"
hidden: false
createdAt: "2024-08-27T12:32:13.057Z"
updatedAt: ""
excerpt: "Learn how routing is managed in VTEX IO Store Framework."
---

A route maps a URL pattern and an HTTP request method to an action. It defines how the application responds to client requests for specific endpoints.

When using [VTEX IO Store Framework](https://developers.vtex.com/docs/guides/store-framework), you do not need to manage routing and HTTP methods directly. Instead, routing and HTTP request methods are managed by either the [Rewriter](https://developers.vtex.com/docs/apps/vtex.rewriter) app or the [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder), depending on the route type. This allows you to focus on creating and managing route paths and page templates.

VTEX IO routes are classified into four different categories:

- **Product routes:** Related to product pages.
- **Search routes:** Related to search pages.
- **Navigation routes:** Client-side defined routes related to VTEX IO custom paths and predefined templates, such as [department](https://github.com/vtex-apps/store/blob/master/store/routes.json#L27), [brand](https://github.com/vtex-apps/store/blob/master/store/routes.json#L21), and [category](https://github.com/vtex-apps/store/blob/master/store/routes.json#L33) routes.
- **Custom routes:** Created by the user to handle custom landing pages.

The Rewriter app manages the first three route types. It interprets the requested path, identifies the route type, and then forwards the route path to the rendering pipeline. Learn more in [Rewriter GraphQL API](https://developers.vtex.com/docs/apps/vtex.rewriter@1.63.0/rewriter-graphql-api).

The store builder manages custom routes. Therefore, custom routes are not stored in the Rewriter app, meaning their paths are directly forwarded to the render server. To learn how to create a custom page, see the [Creating a new custom page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) guide.

## Before you begin

<Steps>

### Develop your Store Theme

Ensure your store has a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) developed with [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) and [Store Framework](https://developers.vtex.com/docs/guides/store-framework), following the [Storefront](https://developers.vtex.com/docs/guides/getting-started-3) guide.

### Check the builders

Check if the builders are properly installed in your Store Theme. To use builders, your account must have at least version `vtex.builder-hub@0.293.4` installed. Also, you need to specify them in the app's `manifest.json` file. Learn more in [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders).

### Check Rewriter installation

To check if the [Rewriter app](https://developers.vtex.com/docs/apps/vtex.rewriter) is installed in your store, follow the guide [Listing an account's apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-listing-an-accounts-apps) and search for `vtex.rewriter` in the **Installed apps** list. If it is not, install the app by following the guide [Installing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app).

</Steps>

## Guides in this section

In this section, you will find the following guides.

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
