---
title: "Get product list for an initial load"
slug: "external-marketplace-integration-product-load"
hidden: false
createdAt: "2021-06-25T20:54:16.459Z"
updatedAt: "2022-04-06T21:10:32.305Z"
---

The initial load of products only occurs after the user installs and configures the connector to use the VTEX Catalog and communicate with the marketplace. All products active on the main account and associated to a sales channel must be sent to the marketplace.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/external-marketplace-integration-guide/ceb5fb3-MarketplaceConnections_Docs_-_Initial_load_of_products-1_12.jpg)

## Send initial load of products

Follow the steps below, to send the initial load of products in the integration’s flow:

1. Connector validates the VTEX <> Marketplace authentication. In case it has expired, perform the update routine defined in the marketplace’s documentation. Otherwise, connectors should log the error AND put the VTEX notification in a contingency queue.
2. VTEX Seller informs connector the sales channel’s ID for the integration.
3. Connector collects the list of SKUs through the Get SKU by sales channel `(api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel)` endpoint.
4. For each SKU retrieved, the connector must:
a. Collect details of each SKU through the [Get SKU and Context](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-context) endpoint.
b. Validate if the SKU is active through the `isActive` property.
c. Validate if the SKU is associated to the sales channel used in the intgration through the `salesChannel` property.
d. Validate if the product is active through the [Get Product by ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-product) endpoint, through the `isActive` property.
*This step is optional, since the [Get SKU and Context](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-context) endpoint already delivers the attribute `IsProductActive` for this purpose*.
e. Identify whether the SKU conforms to the marketplace’s product registration rules.
f. Validate if the product’s category is mapped in the marketplace.  In case it is not mapped, the marketplace should put the SKU in the approval queue, until the [mapping](https://developers.vtex.com/vtex-rest-api/reference/send-category-mapping-to-vtex-mapper) is complete.
g. For SKUs sent with price and inventory levels set up, the connector should validate whether the SKU has price and inventory levels with the sales channel configured for the integration. This should be done through the [Fulfillment Simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) endpoint, without the Postal Code.
h.  Collect:
        - Inventory level on all available warehouses, through the  `logisticsStockBalance` field.
        - Sales price value with applied promotions and discounts, through the `price` field. It is also possible to retrieve the original price through the `listPrice` field.

If all validations pass, the product or SKU is sent to the marketplace and the operation is logged according to information described in the [Logs made available for users](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs#log-messages).

If the IDs between VTEX and the marketplace differ, the connector should store both values. This information will be used for SKU [update](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-product-updates) operations.

[block:callout]
{
  "type": "warning",
  "body": "Be mindful to make all validations at once, and before the SKU’s publication in the marketplace’s catalog. In case there’s an error detected, the connector presents the seller a list of actions to correct. This way we can avoid the correct - publish - correct cycle. \n\nIf products do not apply to steps a, b and c, an error log must be filed, and the connector should collect the next items on the list obtained by step 2.",
  "title": "Validations"
}
[/block]

### Recommendations

To avoid processing gaps due to the big volume of information of the initial load of products, we recommend:

- Using an async messaging architecture, using individual queues by context and store.  
- Creating mechanisms that respect the marketplace API limit rates. We suggest the standard use of the *Circuit Breaker* integration.  
- In case any of the steps listed above presents failures in communication, we suggest using the contingency mechanism of *deadLetters*.
- Being TotalReader: whenever possible, in the data transformation process, using standard values accepted by the marketplace, in case the information is not filled or sent by VTEX.  
- In case the marketplace’s processing is in lots - meaning that the connector assembles a group of SKUs, guaranteeing the the limit of records per lot is respected, according to marketplace riles, and sending them to the marketplace at once - it is fundamental to control the lot’s processing, to avoid sending SKU updates without making sure that the product exists in the marketplace.
- Keeping a states table to know which SKUs have not been integrated with success, attempt date and the response received. This allows the system to use the contingency flow effectively, avoiding infinite loops, and avoiding reaching the request limit.

## API Reference

Use the endpoints described below to get SKU, price and inventory details. It is important to note that when consuming this API, the connector must have a valid VTEX App Key and App Token. You can also [download our Postman collection](https://www.getpostman.com/collections/95a809929905a50e2b7b) to access the API. The diagram illustrates the endpoints used in the integration:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/external-marketplace-integration-guide/8f8b5c9-Marketplace_Docs_-_API_Ref_62.jpg)
[Get list of SKUs associated with a sales channel](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-system-pvt-sku-stockkeepingunitidsbysaleschannel)

[Get details of an SKU associated with a sales channel](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku)

[Check if product is active](https://developers.vtex.com/vtex-rest-api/reference/productandtradepolicy)

[Simulate price and inventory levels](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation)

## Scenario 1: First load of products after integration’s activation

After configuring the communication with the marketplace, connectors must send the first load of products. For every product retrieved from the SKU list associated with the sales channel, the connector must:

1. Validate category mapping.
2. Collect skuId ‘s available in the sales channel associated with the marketplace.
3. [Get SKU information](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku), like weight and dimensions.
4. Use the [Orderform simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) to get price and inventory level, if needed.

In case there’s any failures in an item, connectors should log the error, and move on to the next item on the list, until all SKUs are processed.

## Scenario 2: Deactivate products if the integration is deactivated

If the integration’s deactivation is confirmed with the marketplace, connectors must deactivate products published in the marketplace.

1. [Get SKU information](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku).
2. Send SKU block or deactivation request.
3. Exclude SKUs and clean state control of the integration’s SKUs.


[block:callout]
{
  "type": "warning",
  "title": "Logs",
  "body": "Make sure that all steps are logged as either success or failure, to offer the operation’s full traceability. Check out the [Logs made available for users](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs) page to learn more."
}
[/block]

## What VTEX needs to validate the integration flow

To consider the integration validated by VTEX, the connector should:

1. Follow the step by step of the catalog integration flow.
2. Create a table with VTEX and marketplace field mapping. It should include limitations, transformations, and required fields.
3. Create a table that explicits which data is mandatory and which is recommended when registering products or SKUs and to improve the offer’s positioning in the marketplace’s storefront.
4. Create a table with known error logs and actions that the user can do to solve the problem.

### Template table for field mapping

| VTEX field | How to fill it in VTEX | VTEX API                          | Marketplace field |
| ---------- | ---------------------- | --------------------------------- | ----------------- |
| Name       | Catalog page           | /api/catalog/pvt/stockkeepingunit | ShortName         |
| Image      | Catalog page (SKU)     |                                   | Images            |
