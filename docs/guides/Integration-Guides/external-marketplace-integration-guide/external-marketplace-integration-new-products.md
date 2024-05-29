---
title: "How to get a new product to offer in the marketplace"
slug: "external-marketplace-integration-new-products"
hidden: false
createdAt: "2021-06-25T21:03:55.330Z"
updatedAt: "2022-02-03T20:26:40.959Z"
---

This part of the guide explains how the connector should act when receiving the VTEX notification of a new product or SKU registered. The information flows according to the diagram below:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-new-products-0.jpg)

## How to configure the affiliate endpoint

To use this flow, the connector should provide an endpoint according to the standard:

`https://{endpointDoAfiliado}`

This endpoint should be configured in the VTEX affiliate registration page. Check out our [Configuring an Affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) article.

## VTEX Notification

When creating a new product or SKU in VTEX a notification will be sent through the url configured in the section above. The table below presents the fields sent in this notification’s payload. The connector should use this data to implement the new product registration flow, described in the scenarios that will follow.

Fields sent in the notification:

| Name                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| idSKU                                   | SKU  ID in VTEX                                                                                                                                                                                                                                                                                                                                                                                                      |
| productId                               | Product ID in VTEX                                                                                                                                                                                                                                                                                                                                                                                                   |
| an                                      | Seller’s account name in VTEX, shown in the store’s VTEX Admin url.                                                                                                                                                                                                                                                                                                                                                  |
| idAffiliate                             | Affiliate ID generated automatically in the configuration.                                                                                                                                                                                                                                                                                                                                                           |
| DateModified                            | Date when the item was updated                                                                                                                                                                                                                                                                                                                                                                                       |
| isActive                                | Identifies whether the product is active or not. In case it is “false”, it means the product was deactivated in VTEX and should be blocked in the marketplace. We recommend that the inventory level is zeroed in the marketplace, and the product is blocked. In case the marketplace doesn’t allow it to be deactivated, the product should be excluded, along with any existing correspondences in the connector. |
| StockModified                           | Identifies that the inventory level has been altered. Connectors should send an [Fulfillment Simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) request to collect updated information.                                                                                                                                                                                         |
| PriceModified                           | Identifies that the price  has been altered. Connectors should send an [Fulfillment Simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) request to collect updated information.                                                                                                                                                                                                  |
| HasStockKeepingUnitModified             | Identifies that the product/SKU registration data has changed, like name, description, weight, etc                                                                                                                                                                                                                                                                                                                   |
| HasStockKeepingUnitRemovedFromAffiliate | Identifies that the product is no longer associated with the trade policy. In case the marketplace doesn’t allow it to be deactivated, the product should be excluded, along with any existing correspondences in the connector.                                                                                                                                                                                     |

## Integration flow after notification

Follow the steps below, to send the initial load of products in the integration’s flow:

1. Connector validates the VTEX <> Marketplace authentication. In case it has expired, perform the update routine defined in the marketplace’s documentation. Otherwise, connectors should log the error AND put the VTEX notification in a contingency queue.
2. After receiving the VTEX notification, connectors should:
   a. Check which store the product belongs to, through the `an` parameter.
   b. If the `HasStockKeepingUnitModified` is defined as true, the product should be registered or updated in the marketplace.
   c. Collect details from every SKU using the [Get details of an SKU associated with a sales channel. ](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku)
   d. Validate if the product is active through the [Get Product by ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-product) endpoint, through the `isActive` property.
   e. Validate if the product is associated with the trade policy used in the marketplace integration through the `salesChannel` property.
   f. Identify whether the SKU conforms to the marketplace’s product registration rules.
   g. Validate if the product’s category is mapped in the marketplace.
   In case it is not mapped, the marketplace should put the SKU in the approvement’s queue, until the [mapping](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-mapper#post-/api/mkp-category-mapper/categories/marketplace/-id-) is complete.
   h. Use [Fulfillment Simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) (without postalCode) to check if price and inventory are configured in the selected trade policy.

If all validations pass, the product or SKU is sent to the marketplace and the operation is logged according to information described in the [Logs made available for users](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs#log-messages) section.

If the IDs between VTEX and the marketplace differ, the connector should store both values. This information will be used for SKU [update](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-product-updates) operations.

### Recommendations

To avoid processing gaps due to the big volume of information of the initial load of products, we recommend:

- Using an async messaging architecture, using individual queues by context and store.
- Creating mechanisms that respect the marketplace API limit rates. We suggest the standard use of the *Circuit Breaker* integration.
- In case any of the steps listed above presents failures in communication, we suggest using the contingency mechanism of *deadLetters*.
- Being TotalReader: whenever possible, in the data transformation process, using standard values accepted by the marketplace, in case the information is not filled or sent by VTEX.
- In case the marketplace’s processing is in lots - meaning that the connector assembles a group of SKUs, guaranteeing the the limit of records per lot is respected, according to marketplace riles, and sending them to the marketplace at once - it is fundamental to control the lot’s processing, to avoid sending SKU updates without making sure that the product exists in the marketplace.
- Keeping a states table to know which SKUs have not been integrated with success, attempt date and the response received. This allows the system to use the contingency flow effectively, avoiding infinite loops, and avoiding reaching the request limit.
[block:callout]
{
  "type": "warning",
  "body": "Make sure to check out our Recommendations for performing the steps above successfully.\nBe mindful to make all validations at once, and before the SKU’s publication in the marketplace’s catalog. In case there’s an error detected, the connector presents the seller a list of actions to correct. This way we can avoid the correct - publish - correct cycle. \n\nIf products do not apply to steps a, b and c, an error log must be filed, and the connector should collect the next items on the list obtained by step 2.",
  "title": "Validations"
}
[/block]

## API Reference

Use the endpoints described below to get SKU, price and inventory details. It is important to note that when consuming this API, the connector must have a valid VTEX App Key and App Token. You can also [download our Postman collection](https://www.getpostman.com/collections/95a809929905a50e2b7b) to access the API. The diagram illustrates the endpoints used in the integration:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-new-products-1.jpg)

[block:callout]
{
  "type": "info",
  "body": "All parameters in the endpoints below must be declared in the request. In case one of the parameters does not have a value, you must still send it as `null`.",
  "title": "Request bodies for POST calls"
}
[/block]
[Get list of SKUs associated with a sales channel](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-system-pvt-sku-stockkeepingunitidsbysaleschannel)

[Get details of an SKU associated with a sales channel ](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku)

[Check if product is active](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-product)

[Simulate price and inventory levels](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation)

## Scenario 1: Register new product or SKU after notification

After receiving the VTEX notification of new product or SKU added `(HasStockKeepingUnitModified = true)`, connectors should:

1. Verify if the idSKU and idSkuMarketplace are mapped in the integration.
2. Verify if the SKU is already published in the marketplace.
3. If the conditions above are not met: register the new product in the marketplace.
4. Collect information about the SKU (weight, dimensions, etc).
5. Use the Orderform simulation to get price and inventory level, if needed.
6. Make the necessary data transformations.
7. Perform category mapping routines through VTEX Mapper. In case the mapping does not exist, log an error, and direct the message to the contingency queue, while logging and alerting the user about the error.
8. Make the necessary data transformations.
9. Send data to the marketplace. In case there’s a communication error, direct the message to the contingency queue.
10. If the call returns a success, they should create a correspondence table between the VTEX SkuId and Marketplace SkuId, to guarantee SKU [update](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-product-updates) operations.
[block:callout]
{
  "type": "warning",
  "body": "Make sure that all steps are logged as either success or failure, to offer the operation’s full traceability. Check out the [Logs made available for users](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs) page to learn more.",
  "title": "Logs"
}
[/block]

## What VTEX needs to validate the integration flow

To consider the integration validated by VTEX, the connector should:

1. Follow the step by step of the catalog integration flow.
2. Check if flows comply with the scenarios described.
3. Validate log messages contained in the table of Log’s [Content of the messages](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs#content-of-the-messages).
4. Perform the performance test to validate response time, and SKU processing time from a set of 5000 SKUs.
5. Create tutorials for the final user (including text, videos and diagrams), including a step by step guide explaining how the connector created works. The documentation should be published in the production environment with easy access and navigation.
6. Create a table that explicits which data is mandatory and which is recommended when registering products or SKUs, and to improve the offer’s positioning in the marketplace’s storefront.
7. Create a table with known error logs and actions that the user can do to solve the problem.
[block:callout]
{
  "type": "info",
  "body": "Tables should follow the format below. They will be implemented in the integration according to the connector’s documentation.",
  "title": "Table format"
}
[/block]

### Template table for field mapping {#template-table-for-field-mapping}

| VTEX field | How to fill it in VTEX | VTEX API                          | Marketplace field |
| ---------- | ---------------------- | --------------------------------- | ----------------- |
| Name       | Catalog page           | /api/catalog/pvt/stockkeepingunit | ShortName         |
