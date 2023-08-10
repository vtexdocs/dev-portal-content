---
title: "Specification"
slug: "external-search-provider-specification"
hidden: false
createdAt: "2020-09-11T16:49:44.772Z"
updatedAt: "2020-10-30T20:45:02.331Z"
---

## GraphQL Queries to Implement

To implement the protocol you need to implement resolvers for every GraphQL query on the `vtex.search-graphql` [schema](https://github.com/vtex-apps/search-graphql). As explained in the Limitations section below, only a part of these queries are actually interesting for an external search provider to implement:

- `productSearch`: the actual search engine query
- `facets`: facets to be used as filters
- `banners`: banners to retrieve and show in specific sections of the web page
- `correction`: Corrections for possible typos that a user makes when searching for a product
- `searchSuggestions`: Suggestions of terms based on the search term that the user has made.
- `topSearches`: top searches that is shown when a user puts the cursor over the search bar
- `autocompleteSearchSuggestions`: suggestions of products and terms to be shown in the search bar.
- `productSuggestions`: suggestions of products to be shown in the search result page
- `searchMetadata`: metadata for the specific search result page

## GraphQL Queries Not needed to be Reimplemented

The following queries are not needed to reimplement using the external search provider, as they don't add anything potentially beneficial to the UX if you use an external search provider. On the other hand, these queries are still needed for the store to work properly, so make sure to leverage the VTEX Catalog API's to implement them.

- `product`
- `products`
- `productsByIdentifier`
- `searchURLsCount`

## Limitations

- It is only possible to have one search-resolver service per workspace. If more than one is installed, the workspace will break. This is a known issue that we plan to solve in the near future. To start the development of a new search provider, create a workspace, uninstall the old one (e.g. `vtex.search-resolver`), and then you can start developing your new `search-resolver`.
- The 4 queries listed above that are not needed to be reimplemented are still indeed needed to be implemented. So the best path at this moment is to copy the code for these 4 queries from the reference implementations section.

## Indexing

- You can also use the same VTEX IO app responsible for being a search provider to also set up a webhook and receive notifications whenever a change in the catalog occurs. This VTEX IO app can, then, send the catalog changes to the search provider.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration-Guides/search-integration-guide/cc299d1-catalog_40.png)

To receive catalog changes, refer to this [Receiving Catalog Changes on VTEX IO](https://developers.vtex.com/docs/guides/how-to-receive-catalog-changes-on-vtex-io).

## Onboarding

- When a user installs your search-resolver app, you probably will need an admin panel to set up the app. You can find a working example on `https://github.com/vtex-apps/admin-example`. This admin app can show the indexing progress and also notify the search provider service that a new customer needs to be onboarded.
- The onboarding flow usually is: VTEX client installs app in a different workspace than master → Enters the admin panel to set up the app → app notifies indexing system that a new account is to be indexed → index is 100% completed → VTEX client can promote/install the search provider in master.
