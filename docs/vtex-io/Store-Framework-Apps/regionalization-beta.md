---
title: "Regionalization (Beta)"
slug: "regionalization-beta"
hidden: true
createdAt: "2021-10-19T17:54:09.606Z"
updatedAt: "2021-10-25T20:15:31.016Z"
---

> ℹ️ This feature is in beta, which means that we are working to improve it. If you have any questions, please contact [our Support](https://support.vtex.com/hc/en-us).

Regionalization is a feature of [VTEX Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG#) that allows store administrators to optimize search results according to the availability of sellers in a customer's region. To learn how to install and configure VTEX Intelligent Search in your store, read our [Search app article](https://developers.vtex.com/docs/guides/vtex-search).

For the Regionalization to work, it uses a native behavior from the VTEX Intelligent Search called [Availability](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/7LMQbWK5nElIkXo0NK8Kux). The platform searches for available products according to the stock in a given region. In a Availability paradigm, the platform also checks the sellers registered in the store for their stocks.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/regionalization-beta-0.gif)

## Configuration

### Setting up sellers

To know the possible seller options and how to configure them, check [this article](https://help.vtex.com/en/tutorial/regionalization-beta--72fwxdSLvjKC7ZAT58vlqf).

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

## Show out of stock products on the search result page

In Regionalization, you can show to your customer the out of stock products from your sellers.

> ℹ The products shown will depend on the Availability context.

### On Catalog

#### By the Admin

1. On Admin, click on the **Catalog** module.
2. Click on **Products and SKUs**.
3. Click on the `Add Product` button for a new product, or on the `Update` button for a product update.
4. Check the box of the **Show out of stock** option from the product.
5. Click on `Save`.

#### By API

You can also set the `ShowWithoutStock` attribute in the [Create Product](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-product#post-product) endpoint or in the [Update Product](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-product#catalog-api-put-product) endpoint.

### On VTEX IO

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

After finishing the configuration, you need to initiate the indexing of the store's Catalog with the Intelligent Search. For this, use the [Integration Settings](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V) functionality.