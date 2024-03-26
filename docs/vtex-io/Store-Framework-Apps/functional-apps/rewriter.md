---
title: "Rewriter"
slug: "rewriter"
hidden: false
createdAt: "2020-08-31T17:21:31.944Z"
updatedAt: "2021-08-31T23:51:49.853Z"
---
Rewriter is the VTEX IO app responsible for managing VTEX IO [routes](https://developers.vtex.com/docs/guides/vtex-io-documentation-routes) related to the storefront. Through the use of the [app’s GraphQL API](https://developers.vtex.com/docs/guides/rewriter-graphql), it is possible to read, create and delete routes in a store.

The Rewriter app has many functionalities that can be configured in its Admin settings page, which are described in the next section. Some of these functionalities are:

- Redirect routes with specific configurations (ending with `/`, use of uppercase, etc.).
- Configure behavior when using `hreflang` tags, which can be useful for multilanguage stores.
- Override client-side cache duration for PDPs and PLPs.

## Settings

Follow the steps below to access the Rewriter settings page in your store:

1. Open your store’s Admin.
2. Go to **Apps** > **Extensions Hub** > **App Management**.
3. Search for **Rewriter**.
4. In the Rewriter app’s box, click on <i class="fa fa-gear"></i> **Settings**.

![Rewriter settings](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/rewriter-settings.jpg)

The table below describes the available settings of the Rewriter app:

|Name|Type|Description|
|-|-|-|
|Enable 404 for paths with one segment|`boolean`|This will enable 404 for paths with one segment. Make sure your search bar adds `map=ft` to your URL. For more details, see [Enabling 404 pages](https://developers.vtex.com/docs/guides/vtex-io-documentation-enabling-404-pages).|
|Routes version|`number`|The version routes will be saved in. If this is changed, all routes saved in VBase will be invalidated.|
|Blocks default routes in other bindings|`boolean`|Blocks the default binding's routes in other bindings.|
|Enforce URLs in lowercase|`boolean`|This enforces that all URLs that end with a slash will do a 301 redirection to the corresponding page without the ending slash.|
|Remove repeated `hreflang` tags|`boolean`|This removes the repeated `hreflang` tags, prioritizing showing `hreflang` tags with the current host.|
|Enable full locale in the `hreflang`|`boolean`|This will include the full locale in the `hreflang`.|
|Remove locales with `myvtex`|`boolean`|This will remove all `hreflang` tags on URLs that include `myvtex`.|
|Custom `hreflang`|`array`|Associate your custom `hreflang` tags with the canonical address desired.|
|↳ Canonical address|`string`|The canonical address of the `hreflang` tag to be modified.|
|Canonical address of the `hreflang` tag to be modified|`string`|The custom locale that will be used in the `hreflang` tag for the selected canonical address.|
|Overwrite cache control settings|`boolean`|This will allow overwriting the `max-age` and `stale-while-revalidate` values on the cache-control header. The default value is `false`.|
|Max-Age overwrite|`number`|This setting allows you to override the `max-age` value in the cache-control header for Product Detail Pages (PDP) and Product Listing Pages (PLP). The valid range for this setting is between 300 to 3600 seconds. The default value is 300 seconds. For more details, see [Cache-control settings](https://developers.vtex.com/docs/guides/cache-control-settings).|
|Stale Revalidate overwrite|`number`|This setting enables the override of the `stale-while-revalidate` value in the cache-control header for Product Detail Pages (PDP) and Product Listing Pages (PLP). The valid range for this setting is between 600 and 86400 seconds. The default value is 600 seconds. For more details, see [Cache-control settings](https://developers.vtex.com/docs/guides/cache-control-settings).|
