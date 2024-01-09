---
title: "Regionalization setup (Beta)"
slug: "regionalization-beta"
hidden: true
createdAt: "2021-10-19T17:54:09.606Z"
updatedAt: "2021-10-25T20:15:31.016Z"
---

> ℹ️ This feature is in closed beta, which means that only specific customers can access it now. If you want to implement it in the future, please contact [our Support](https://help.vtex.com/support).

Regionalization is a feature of [VTEX Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG#) that allows store administrators to optimize search results according to the availability of sellers in a customer's region. For information on installing and configuring VTEX Intelligent Search in your store, refer to the [Search app](https://developers.vtex.com/docs/apps/vtex.search) article.

Regionalization leverages a native functionality from the VTEX Intelligent Search known as [Availability](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/7LMQbWK5nElIkXo0NK8Kux). This feature searches for products currently in stock within a specified region. In addition, it checks the inventories of registered sellers in the store, ensuring a comprehensive assessment of available stock within the designated area.

Stores that have more than one registered white label seller usually have specific inventories for each region. This is the case for supermarkets, for example. With the Regionalization feature enabled, if a customer enters their ZIP code while browsing the store (before checkout), the search results will only display the products available in the corresponding region.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/regionalization-beta-0.gif)

## Before you begin

Make sure you have finished these actions before setting up the Regionalization feature in your store:

- Install and configure VTEX Intelligent Search in your store, according to instructions in the [Search](https://developers.vtex.com/docs/guides/vtex-search) developer guide and information available in the [VTEX Intelligent Search track](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb).
- Follow the steps described in [Regionalization (Beta)](https://help.vtex.com/tutorial/regionalization-beta--72fwxdSLvjKC7ZAT58vlqf), including seller configuration and a request to our support to activate the Regionalization feature.

## Configuration

In the following sections, learn how to set up Regionalization in your store.

### Setting up the `search-result` app

To use the Regionalization feature, you must have the [Search Result](https://developers.vtex.com/docs/guides/vtex-search-result) app installed. After this configuration, you must set the `simulationBehavior` prop as `default` on the `search.jsonc` file to the correct use of the Regionalization, as shown below.

```json
{
  "store.search": {
    "blocks": ["search-result-layout"],
    "props": {
      "context": {
        "skusFilter": "FIRST_AVAILABLE",
        "simulationBehavior": "default"
      }
    }
  }
}
```

### Showing out-of-stock products on the search results page

You can show customers out-of-stock products from your sellers using the Regionalization feature.

> ℹ The products shown will depend on the [Availability](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/7LMQbWK5nElIkXo0NK8Kux) context.

For this, you must make the following configurations on your store's Catalog and on VTEX IO.

#### Catalog

To display products, even when they are out of stock, the **Show out of stock** option must be enabled. Take the following steps:

1. On VTEX Admin, click on the **Catalog** module.
2. Click on **Products and SKUs**.
3. Click on the `Add Product` button for a new product, or on the `Update` button for a product update.
4. Check the box of the **Show out of stock** option from the product.
5. Click on `Save`.

You can also set the `ShowWithoutStock` attribute in the [Create Product](https://developers.vtex.com/docs/api-reference/catalog-api/#post-/api/catalog/pvt/product) endpoint or in the [Update Product](https://developers.vtex.com/docs/api-reference/catalog-api/#put-/api/catalog/pvt/product/-productId-) endpoint.

#### VTEX IO

Set the `hideUnavailableItems` prop to `true` on the `autocomplete-result-list.v2` block. Check our [Search documentation](https://developers.vtex.com/docs/guides/vtex-search#autocomplete-result-listv2-props).

```json
{
  "search-bar": {
    "blocks": ["autocomplete-result-list.v2"],
    "props": {
      "hideUnavailableItems": true
    }
  }
}
```

## Indexing

After finishing the configuration, stores using VTEX Intelligent Search for the first time need to initiate the indexing of the store's Catalog with the Intelligent Search. If applicable, follow the steps below:

1. On VTEX Admin, go to **Store Settings > Intelligent Search > Integrations**.
2. Click `Start`.

Stores that have already set up this integration do not need to redo this action. For more information about this page, check the [Integration Settings](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V) guide.
