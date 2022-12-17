---
title: "How to keep stock updated"
slug: "external-marketplace-integration-stock-update"
hidden: false
createdAt: "2021-06-28T21:53:49.780Z"
updatedAt: "2022-02-03T19:23:27.419Z"
---

Learn how to keep integrated products updated with price and inventory level information. Before you start, check out what’s included in the product update flow:

| Included                                     | Not Included                                                          |
|----------------------------------------------|-----------------------------------------------------------------------|
| Prices defined in the VTEX main account      | Prices defined in third party sellers or franchise accounts           |
|                                              | Prices updated directly to the marketplace integration                |
| Inventory levels defined in the main account | Inventory levels defined in third party sellers or franchise accounts |
|                                              | Inventory levels updated directly to the marketplace integration      |

## How to configure the affiliate endpoint

To use this flow, the connector should provide an endpoint according to the standard:

`https://{endpointDoAfiliado}/api/notification/`

This endpoint should be configured in the VTEX affiliate registration page. Check out our [Configuring an Affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) article.

## VTEX Notification

Whenever the seller updates a  product or SKU in VTEX, a notification will be sent through the url configured in the section above. The table below presents the fields sent in this notification’s payload. The connector should use this data to implement the new product registration flow, described in the scenarios that will follow.

### Fields sent in the notification

| Name                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| idSKU                                   | SKU  ID in VTEX                                                                                                                                                                                                                                                                                                                                                                                                      |
| productId                               | Product ID in VTEX                                                                                                                                                                                                                                                                                                                                                                                                   |
| an                                      | Seller’s account name in VTEX, shown in the store’s VTEX Admin url.                                                                                                                                                                                                                                                                                                                                                  |
| idAffiliate                             | Affiliate ID generated automatically in the configuration.                                                                                                                                                                                                                                                                                                                                                           |
| DateModified                            | Date when the item was updated                                                                                                                                                                                                                                                                                                                                                                                       |
| isActive                                | Identifies whether the product is active or not. In case it is “false”, it means the product was deactivated in VTEX and should be blocked in the marketplace. We recommend that the inventory level is zeroed in the marketplace, and the product is blocked. In case the marketplace doesn’t allow it to be deactivated, the product should be excluded, along with any existing correspondences in the connector. |
| StockModified                           | Identifies that the inventory level has been altered. Connectors should send an Fulfillment Simulation  request to collect updated information.                                                                                                                                                                                                                                                                      |
| PriceModified                           | Identifies that the price  has been altered. Connectors should send an Fulfillment Simulation  request to collect updated information.                                                                                                                                                                                                                                                                               |
| HasStockKeepingUnitModified             | Identifies that the product/SKU registration data has changed, like name, description, weight, etc                                                                                                                                                                                                                                                                                                                   |
| HasStockKeepingUnitRemovedFromAffiliate | Identifies that the product is no longer associated with the trade policy. In case the marketplace doesn’t allow it to be deactivated, the product should be excluded, along with any existing correspondences in the connector.                                                                                                                                                                                     |

The inventory update flow begins when the connector receives a VTEX Catalog notification, indicating that changes have been made to the SKU or product. Besides this notification mechanism, we recommend using an independant  inventory update mechanism, so stocks are always updated. The diagram below illustrates the information flow used to keep prices of seller’s SKUs updated in the marketplace integration.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/external-marketplace-integration-guide/746746d-MarketplaceConnections_Docs_-_Integration_through_notification-1_47.jpg)
Follow the steps below to maintain inventory levels updated in the marketplace integration:

1. Connector validates the VTEX <> Marketplace authentication. In case it has expired, perform the update routine defined in the marketplace’s documentation. Otherwise, connectors should log the error AND put the VTEX notification in a contingency queue.
2. After receiving the VTEX notification, connectors should:
a. Check which store the product belongs to, through the “an” parameter.
b. If the `HasStockKeepingUnitModified` is defined as true, the product should be registered or updated in the marketplace.
c. Collect details from every SKU using the [Get details of an SKU](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku) endpoint.
d. Validate if the product is active through the [Get Product by ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-product) endpoint, through the `isActive` property.
e. Validate if the product is associated with the trade policy used in the marketplace integration through the `salesChannel` property.
f. Identify whether the SKU conforms to the marketplace’s product registration rules.
g. Validate if the product’s category is mapped in the marketplace.  
In case it is not mapped, the marketplace should put the SKU in the approvement’s queue, until the [mapping](https://developers.vtex.com/vtex-rest-api/reference/send-category-mapping-to-vtex-mapper) is complete.
h. Use [Fulfillment Simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) (without postalCode) to check if price is configured in the selected trade policy.
    - To collect the product’s price, use the `price` attribute.
    - To collect the sales price configured for that trade policy, use the attribute `salesprice`.
3. Register operation’s [Logs](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs). Check out [Content of the messages](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs#content-of-the-messages) for this step.

If all validations pass, the product or SKU is sent to the marketplace and the operation is logged according to information described in the [Logs made available for users](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs) section.

If the IDs between VTEX and the marketplace differ, the connector should store both values.

## Recommendations

To avoid processing gaps due to the big volume of information of the initial load of products, we recommend:

- Using an async messaging architecture, using individual queues by context and store.  
- Creating mechanisms that respect the marketplace API limit rates. We suggest the standard use of the _Circuit Breaker_ integration.  
- In case any of the steps listed above presents failures in communication, we suggest using the contingency mechanism of _deadLetters_.
- Being TotalReader: whenever possible, in the data transformation process, using standard values accepted by the marketplace, in case the information is not filled or sent by VTEX.  
- In case the marketplace’s processing is in lots - meaning that the connector assembles a group of SKUs, guaranteeing the the limit of records per lot is respected, according to marketplace riles, and sending them to the marketplace at once - it is fundamental to control the lot’s processing, to avoid sending SKU updates without making sure that the product exists in the marketplace.
- Keeping a states table to know which SKUs have not been integrated with success, attempt date and the response received. This allows the system to use the contingency flow effectively, avoiding infinite loops, and avoiding reaching the request limit.
[block:callout]
{
  "type": "warning",
  "body": "Make sure to check out our Recommendations for performing the steps above successfully.\nBe mindful to make all validations at once, and before the SKU’s publication in the marketplace’s catalog. In case there’s an error detected, the connector presents the seller a list of actions to correct. This way we can avoid the correct - publish - correct cycle. \n\nIf products do not apply to steps a, b and c, an error log must be filed, and the connector should collect the next items on the list obtained by step 2."
}
[/block]

## API Reference

Use the endpoints described below to get SKU, price and inventory details. It is important to note that when consuming this API, the connector must have a valid VTEX App Key and App Token. You can also [download our Postman collection](https://www.getpostman.com/collections/95a809929905a50e2b7b) to access the API. The diagram illustrates the endpoints used in the integration:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/external-marketplace-integration-guide/3067366-Marketplace_Docs_-_API_Ref_90.jpg)

[block:callout]
{
  "type": "info",
  "body": "All parameters in the endpoints below must be declared in the request. In case one of the parameters does not have a value, you must still send it as `null`.",
  "title": "Request bodies for POST calls"
}
[/block]
[Get list of SKUs associated with a sales channel](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-system-pvt-sku-stockkeepingunitidsbysaleschannel)

[Get details of an SKU associated with a sales channel](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku)

[Check if product is active](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-products-skus#productandtradepolicy)

[Simulate price and inventory levels](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation)

## Scenario 1: Update Inventory level

1. Validate if the `isActive` property is “true”. If otherwise, skip to Scenario 3.
2. Check if the VTEX `idSKU` and `idSkuMarketplace` are mapped, and if the SKU is already published on the marketplace.
3. Evaluate if the notification message has the `HasStockKeepingUnitModified` property set as “true”. If otherwise, validate the other JSON properties and execute the following scenarios, if needed.
4. Use [Fulfillment Simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) (without postalCode) to check if price and inventory are configured in the selected trade policy.
5. Offer a contingency mechanism that allows steps to be repeated in case they fail.
6. Make the necessary data transformations and [Log](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs) errors if needed.
7. Send data to the marketplace.
8. Register operation’s logs. Check out [Content of the messages](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs#content-of-the-messages) for this step.
9. Offer contingency mechanism that verify frequently if inventory levels match in both marketplace and VTEX. We recommend focusing on SKUs with high order rates, regardless of VTEX’s notification.
[block:callout]
{
  "type": "info",
  "body": "Tables should follow the format below. They will be implemented in the integration according to the connector’s documentation."
}
[/block]

### Template table for field mapping

| VTEX field | How to fill it in VTEX | VTEX API                          | Marketplace field | Transformation                             | Mandatory | BuyBox |
|------------|------------------------|-----------------------------------|-------------------|--------------------------------------------|-----------|--------|
| Name       | Catalog page           | /api/catalog/pvt/stockkeepingunit | ShortName         | Sent to the marketplace only 50 characters | Yes       | Yes    |
