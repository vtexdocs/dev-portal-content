---
title: "Setting up brand search queries as full text"
slug: "setting-up-brand-search-queries-as-full-text"
excerpt: "Learn how to resolve brand search queries in Intelligent Search as full text."
hidden: true
createdAt: "2024-12-12T14:45:40.782Z"
updatedAt: "2024-12-12T14:49:33.433Z"
---

By default, when searching for a brand using the search bar with Intelligent Search, the results only display products that are registered in the catalog under that specific brand. A brand filter is applied to the search, meaning if the brand does not exist in the store’s catalog, the search does not return any results.

However, you can modify this behavior to treat brand searches as full text. This means you can show products that contain the brand name in the product title, description or any product field.

This guide explains how to change the default behavior to resolve brand search queries in Intelligent Search, enabling them to be resolved as full text.

## Before you begin

Make sure that [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) is installed and set up in your store.

## Instructions

### Step 1 - Setting up the Store Indexer app

Follow the instructions below to enable brand search as full text when receiving catalog notifications using the [Store Indexer](https://developers.vtex.com/docs/apps/vtex.store-indexer) app:

1. On VTEX Admin, go to **Apps > Extensions Hub > App Management**, or access `https://{accountName}.myvtex.com/admin/apps` directly.  
2. In the **My Apps** page, search for the `store indexer` as shown below. If it doesn’t appear at first, run `vtex install vtex.store-indexer` using VTEX IO CLI and refresh the page.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@maindocs/guides/Search/setting-up-brand-search-queries-as-full-text-1.png)
3. In the Store Indexer card, click **Settings**.  
4. In the **Brand Queries Map** field, select **Full Text**.  
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@maindocs/guides/Search/setting-up-brand-search-queries-as-full-text-2.png)
5. Click `Save`.

If you need to revert back to the default behavior, repeat the instructions above, changing step 4 back to **Brand**.

### Step 2 - Changing the existing routes in Rewriter

To configure the [Rewriter](https://developers.vtex.com/docs/guides/rewriter) app to resolve brand routes using the full text method, follow these instructions:

1. Go to https://`{accountName}.myvtex.com/admin/graphql-ide`.  
2. Search for `routes-bootstrap`. This app gets data from the catalog and creates, translates and saves brand, department, category and subcategory routes to Rewriter.  
3. Run the following GraphQL query:

    ```graphql
    {
      bootstrap{
        brands(resolveMapQueryAs: FT)
      }
    }
    ```

### Step 3 - Testing a brand search

After configuring the full text search for brands, follow these steps to verify that it works correctly:

1. Go to your store's website.  
2. Search for a brand using the search bar.  
3. Open a new tab and go to **Storefront > Intelligent Search > Explained Search** on VTEX Admin or visit `https://{accountName}.myvtex.com/admin/search/explained-search`.  
4. Compare the search results displayed on your storefront with the **Explained Search** results on VTEX Admin.
