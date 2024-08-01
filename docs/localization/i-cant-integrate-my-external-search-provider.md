---
title: "I can’t integrate my external Search Provider"
slug: "i-cant-integrate-my-external-search-provider"
hidden: false
createdAt: "2024-08-01T15:08:23.602Z"
updatedAt: ""
excerpt: 'Learn how to fix "Unknown errors" when integrating an external search provider with VTEX.'
tags:
  - integration
  - vtex-protocol
  - search-protocol

---

**Keywords:** Integration | VTEX Protocol | Search Protocol | Search Resolver | External Search Provider

When attempting to integrate an external search provider with the VTEX Platform according to the [Implementing a Custom Search Resolver App](https://developers.vtex.com/docs/guides/external-search-provider-recipe) guide, you may encounter “Unknown errors” that prevent successful integration.

These errors may occur due to outdated dependencies in your app.

## Solution

To resolve any “Unknown errors” during search integration, follow these steps:

### Step 1 - Updating the `vtex.search-graphql` dependency version

Ensure that the `vtex.search-graphql` dependency in your `node/package.json` file is up-to-date with the latest version of the `vtex.search-graphql` app.

1. Open your app directory and go to the `node/package. json` file.
2. Locate the `vtex.search-graphql` dependency.
3. Compare the version listed in your `node/package.json` with the [latest version available for the `vtex.search-graphql` app](https://github.com/vtex-apps/search-graphql/blob/master/manifest.json#L4).
4. If your `vtex.search-graphql` dependency is outdated, update it to the latest version.

    a. Edit the `node/package. json` file, updating the version number for `vtex.search-graphql`.
  
    b. Save the changes to the `node/package. json` file.

### Step 2 - Install Updated Dependencies

After updating the `vtex.search-graphql` version, install the update dependencies:

1. Open a terminal and navigate to your app’s `node` folder.
2. Run the following command to install the updated dependencies:

   ```sh
   yarn
   ```

### Step 3 - Re-link the app

After installing the updated dependencies, re-link the app to apply the changes by running the following command:

```sh
vtex link
```

If the issue persists, open a ticket to [VTEX Support](https://help.vtex.com/support).
