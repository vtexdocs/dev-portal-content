---
title: "Catalog Integration"
slug: "external-marketplace-integration-catalog"
hidden: false
createdAt: "2021-06-25T20:36:32.888Z"
updatedAt: "2022-02-03T20:17:05.264Z"
---
Learn how to integrate the VTEX Catalog with external marketplaces or connectors that work as hubs. Before you start, check out what’s included in the Catalog flow:

## How to offer VTEX Products in other channels

| Included                                                                                                               | Not Included                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Products and SKUs in the VTEX main account                                                                             | Products and SKUs in third party sellers or franchise accounts                                                                |
| Inventory level and prices defined only in the main account                                                            | Inventory level and prices defined in third party sellers or franchise accounts                                               |
| Products and SKUs that belong both to the [sales channel](https://help.vtex.com/tutorial/configurando-a-politica-comercial-para-marketplace--tutorials_404) and [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) previously set up in the marketplace integration | Products and SKUs that are not configured in the  [sales channel](https://help.vtex.com/tutorial/configurando-a-politica-comercial-para-marketplace--tutorials_404) and [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) previously set up in the marketplace integration |
|                                                                                                                        | Products and SKUs added directly to the marketplace integration                                                               |
|                                                                                                                        | Products with specifications and attributes                                                                                   |



## Glossary

- **Seller**: Owns the product, responsible for the fulfillment, or SKU delivery. 

- **Marketplace/affiliate:** Owns the storefront, responsible for selling the SKU

- **SKU**: item to be exchanged and sold between seller and marketplace

- **Sales channel/Trade policy**: product assortment, prices, and logistics configurations attached to a sales channel. Know more about [how to configure a marketplace trade policy](https://help.vtex.com/tutorial/configurando-a-politica-comercial-para-marketplace--tutorials_404).

- **Connector**: party responsible for the integration, being either the marketplace itself, or an integration hub.

## Index

The Catalog Integration for external marketplaces includes the following steps:
- [Logs made available for users](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs)
- [Get product list for an initial load of products](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-product-load)
- [How to get a new product to offer in the marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-new-products)
- [How to get product updates](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-product-updates)
- [Product and category mappings](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-catalog-mapping)
- [How to keep prices updated](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-price-update) 
- [How to keep stock updated](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-stock-update)
