---
title: "FastStore: new experimental SEO flags for search engines"
slug: "2025-05-30-faststore-new-seo-flags"
type: added
excerpt: "Control search engine behavior with three new experimental flags: `noRobots`, `noindex`, and `nofollow`."
createdAt: "2025-05-30T00:00:00.000Z"
updatedAt: ""
hidden: false
---

FastStore projects can now use new experimental flags to manage how search engines interact with and categorize store content:

| Flag | Type | Description |
| ------ | ------- | -------------- |
| `noRobots` | boolean | Disables the default `robots` meta tag on all pages, removing the default crawler instructions. <ul><li>Set to `true`: Prevents including any robots meta tags on the page.</li><li>Set to `false`: Includes crawler instructions as the FastStore default behavior, allowing search engines to understand how to index and follow the site.</li></ul> |
| `noindex` | boolean | Instructs web crawlers not to index the store page, which keeps the page out of search results. <ul><li>Set to `true`: Indicates the page should not be indexed by search engines.</li><li>Set to `false`: Allows search engines to include the page in their search results.</li></ul> |
| `nofollow` | Boolean | Prevents search engines from following links on the page to ensure that sensitive or irrelevant content is not included in search results. <ul><li>Set to `true`: Stops the page from passing SEO values to linked pages.</li><li>Set to `false`: Allows search engines to crawl and potentially pass SEO values to linked pages.</li></ul> |

> ⚠️ These flags are experimental and may have limitations. Before using them in a production environment, run tests to make sure they are compatible with your store.
## What needs to be done?

To use these flags, update your FastStore project and add them to the [`discovery.config.js`](https://developers.vtex.com/docs/guides/faststore/project-structure-config-options) file:

1. Open your store project in the code editor of your choice.
2. Open the terminal and run the following command to update the FastStore packages to the latest version:

    ```bash
    yarn upgrade -L --scope @faststore
    ```

3. Open the `discovery.config.js` file and, under the `experimental` field, add the `noRobots` and `noindex`, or `nofollow` flags. The experimental field will look like this:

    ```js discovery.config.js
    experimental: {
        …
        noRobots: false, // Disables default robots meta tag if true
        noindex: true, // Prevents indexing if true
    },
    ```
4. Run `yarn dev` in the terminal.
5. Open the available localhost URL and check if the flags are applied by inspecting the `<head>` element of the page or using SEO tools:
![seo-experimental-flags-example](https://vtexhelp.vtexassets.com/assets/docs/src/seo-flags___8e77083576529c49e160590a9229ed02.png)
