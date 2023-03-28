---
title: "How to get product updates"
slug: "external-marketplace-integration-product-updates"
hidden: false
createdAt: "2021-06-25T21:24:13.724Z"
updatedAt: "2022-02-03T20:38:11.391Z"
---

This section of the integration guide goes over the process of updating SKUs that are already integrated in the marketplace. The information flows according to the diagram below:

![](https://user-images.githubusercontent.com/77292838/211638002-1f4e9025-30d5-406c-bfaa-b3e30f0ed1c1.png)

To begin the integration of this process, it is necessary to have a search Endpoint configured, in order to receive notifications.

## How to configure the affiliate endpoint

To use this flow, the connector should provide an endpoint according to the standard:

`https://{endpointDoAfiliado}/api/notification/`

This endpoint should be configured in the VTEX affiliate registration page. Check out our [Configuring an Affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) article.

## VTEX Notification

When creating a new product or SKU in VTEX a notification will be sent through the url configured in the section above. The table below presents the fields sent in this notification’s payload. The connector should use this data to implement the new product registration flow, described in the scenarios that will follow.

Fields sent in the notification:

| Name | Description |
|-|-|
| idSKU | SKU ID in VTEX |
| productId | Product ID in VTEX |
| an | Seller’s account name in VTEX, shown in the store’s VTEX Admin url. |
| idAffiliate | Affiliate ID generated automatically in the configuration. |
| DateModified | Date when the item was updated |
| isActive | Identifies whether the product is active or not. In case it is “false”, it means the product was deactivated in VTEX and should be blocked in the marketplace. We recommend that the inventory level is zeroed in the marketplace, and the product is blocked. In case the marketplace doesn’t allow it to be deactivated, the product should be excluded, along with any existing correspondences in the connector. |
| StockModified | Identifies that the inventory level has been altered. Connectors should send an [Fulfillment Simulation](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/-fulfillmentEndpoint-/pvt/orderForms/simulation) request to collect updated information. |
| PriceModified | Identifies that the price has been altered. Connectors should send an [Fulfillment Simulation](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/-fulfillmentEndpoint-/pvt/orderForms/simulation) request to collect updated information. |
| HasStockKeepingUnitModified | Identifies that the product/SKU registration data has changed, like name, description, weight, etc |
| HasStockKeepingUnitRemovedFromAffiliate | Identifies that the product is no longer associated with the trade policy. In case the marketplace doesn’t allow it to be deactivated, the product should be excluded, along with any existing correspondences in the connector. |

![](https://user-images.githubusercontent.com/77292838/211638123-d396bfe9-cf54-45eb-a366-ba5c8f547203.png)

## Integration flow

1. Connector validates the VTEX <> Marketplace authentication. In case it has expired, perform the update routine defined in the marketplace’s documentation. Otherwise, connectors should log the error AND put the VTEX notification in a contingency queue.
2. After receiving the VTEX notification, connectors should:
   a. Check which store the product belongs to, through the “an” parameter.
   b. If the HasStockKeepingUnitModified is defined as true, the product should be registered or updated in the marketplace.
   c. Collect details from every SKU using the [Get details of an SKU associated with a sales channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-) endpoint.
   d. Validate if the product is active through the [Get Product by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-) endpoint, through the `isActive` property.
   e. Validate if the product is associated with the trade policy used in the marketplace integration through the `salesChannel` property.
   f. Identify whether the SKU conforms to the marketplace’s product registration rules.
   g. Validate if the product’s category is mapped in the marketplace.\
   In case it is not mapped, the marketplace should put the SKU in the approvement’s queue, until the [mapping](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-mapper#post-/api/mkp-category-mapper/categories/marketplace/-id-) is complete.
   h. Use [Fulfillment Simulation](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/-fulfillmentEndpoint-/pvt/orderForms/simulation) (without postalCode) to check if price and inventory are configured in the selected trade policy.

If all validations pass, the product or SKU is sent to the marketplace and the operation is logged according to information described in the [Logs made available for users](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs) section.

If the IDs between VTEX and the marketplace differ, the connector should store both values. This information will be used for SKU update operations.

### Recommendations

To avoid processing gaps due to the big volume of information of the initial load of products, we recommend:

- Using an async messaging architecture, using individual queues by context and store.
- Creating mechanisms that respect the marketplace API limit rates. We suggest the standard use of the *Circuit Breaker* integration.
- In case any of the steps listed above presents failures in communication, we suggest using the contingency mechanism of *deadLetters*.
- Being TotalReader: whenever possible, in the data transformation process, using standard values accepted by the marketplace, in case the information is not filled or sent by VTEX.
- In case the marketplace’s processing is in lots - meaning that the connector assembles a group of SKUs, guaranteeing the the limit of records per lot is respected, according to marketplace riles, and sending them to the marketplace at once - it is fundamental to control the lot’s processing, to avoid sending SKU updates without making sure that the product exists in the marketplace.
- Keeping a states table to know which SKUs have not been integrated with success, attempt date and the response received. This allows the system to use the contingency flow effectively, avoiding infinite loops, and avoiding reaching the request limit.

>⚠️ Make sure to check out our Recommendations for performing the steps above successfully.\nBe mindful to make all validations at once, and before the SKU’s publication in the marketplace’s catalog. In case there’s an error detected, the connector presents the seller a list of actions to correct. This way we can avoid the correct - publish - correct cycle. \n\nIf products do not apply to steps a, b and c, an error log must be filed, and the connector should collect the next items on the list obtained by step 2.

## API Reference

Use the endpoints described below to get SKU, price and inventory details. It is important to note that when consuming this API, the connector must have a valid VTEX App Key and App Token. You can also [download our Postman collection](https://www.getpostman.com/collections/95a809929905a50e2b7b) to access the API. The diagram illustrates the endpoints used in the integration:

![](https://user-images.githubusercontent.com/77292838/211638221-d444704e-bb9d-4c31-b2e0-8b62af4dcf08.png)

>ℹ️ All parameters in the endpoints below must be declared in the request. In case one of the parameters does not have a value, you must still send it as `null`.",

[Get list of SKUs associated with a sales channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel)

[Get details of an SKU associated with a sales channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-)

[Check if product is active](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-)

[Simulate price and inventory levels](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/-fulfillmentEndpoint-/pvt/orderForms/simulation)

## Scenario 1: Update information of an SKU already published

After receiving the VTEX Catalog notification of product or SKU updates, connectors should update the published item’s information on the marketplace:

1. Validate if the `isActive` property is `true`. If otherwise, skip to Scenario 3.
2. Check if the VTEX `idSKU` and `idSkuMarketplace` are mapped, and if the SKU is already published on the marketplace.
3. Evaluate if the notification message has the `HasStockKeepingUnitModified` property set as `true`. If otherwise, validate the other JSON properties and execute the following scenarios, if needed.
4. Use [Get product details](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/productget/-productId-) API.
5. Use [Get details of an SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyid/-skuId-)API.  
6. Use [Fulfillment Simulation](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/-fulfillmentEndpoint-/pvt/orderForms/simulation) (without postalCode) to check if price and inventory are configured in the selected trade policy.
7. Perform category mapping routines through VTEX Mapper. In case the mapping does not exist, log an error, and direct the message to the contingency queue, while logging and alerting the user about the error.
8. Make the necessary data transformations and [Log](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#log-messages) errors if needed.
9. Send data to the marketplace.
10. Register operation’s logs. Check out [Content of the messages](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#content-of-the-messages) for this step.  

In case steps 4, 5 or 6 present errors, connectors should create contingency mechanisms to repeat them.

## Scenario 2: Deactivate SKU from VTEX

1. Validate if the `isActive` property is “false”.
2. [Get SKU information](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-).
3. Check if the VTEX `idSKU` and `idSkuMarketplace` are mapped, and if the SKU is already published on the marketplace.  Otherwise,  [Log](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#log-messages) errors and skip to Scenario 1.
4. Send an SKU block or deactivation request to the marketplace. If the marketplace does not allow this operation, skip to Scenario 4.
5. Register operation’s logs. Check out [Content of the messages](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#content-of-the-messages) for this step.

In case step 2 presents errors, connectors should create contingency mechanisms to repeat them.

## Scenario 3: Activate SKU from VTEX

1. Validate if the `isActive` property is “true”.
2. [Get SKU information](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-).
3. Check if the VTEX `idSKU` and `idSkuMarketplace` are mapped, and if the SKU is already published on the marketplace.  Otherwise,  [Log](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#log-messages) errors and skip to Scenario 1.
4. Send SKU activation to the marketplace. The endpoint used for this step varies according to the marketplace, but it should be the marketplace’s activate/deactivate published SKU.
5. Register operation’s logs. Check out [Content of the messages](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#content-of-the-messages) for this step.

In case step 2 presents errors, connectors should create contingency mechanisms to repeat them. We recommend using a queue to control exceptions.

## Scenario 4: Delete SKU from VTEX

Note that this scenario should only be executed if the marketplace does not offer the product block or deactivation options.

1. Validate if the `isActive` property is “false”.
2. [Get SKU information](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-).
3. Check if the VTEX `idSKU` and `idSkuMarketplace` are mapped, and if the SKU is already published on the marketplace.  Otherwise,  [Log](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#log-messages) errors and skip to Scenario 1.
4. Send “Delete SKU request” to the marketplace. The endpoint used for this step varies according to the marketplace.
5. Once the Delete SKU operation is confirmed, clean the SKU mapping. This step is performed within the connector’s mapping database.
6. Register operation’s logs. Check out [Content of the messages](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#content-of-the-messages) for this step.

In case step 2 presents errors, connectors should create contingency mechanisms to repeat them.We recommend using a queue to control exceptions.

>⚠️ Make sure that all steps are logged as either success or failure, to offer the operation’s full traceability. Check out the [Logs made available for users](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs) page to learn more."

## What VTEX needs to validate the integration flow

To consider the integration validated by VTEX, the connector should:

1. Follow the step by step of the catalog integration flow.
2. Check if flows comply with the scenarios described.
3. Validate log messages contained in the table of Log’s [Content of the messages](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs#content-of-the-messages).
4. Perform the performance test to validate response time, and SKU processing time from a set of 5000 SKUs.
5. Create tutorials for the final user (including text, videos and diagrams), including a step by step guide explaining how the connector created works. The documentation should be published in the production environment with easy access and navigation.
6. Create a table that explicits which data is mandatory and which is recommended when registering products or SKUs, and to improve the offer’s positioning in the marketplace’s storefront.
7. Create a table with known error logs and actions that the user can do to solve the problem.

>ℹ️ Tables should follow the format below. They will be implemented in the integration according to the connector’s documentation.


### Template table for field mapping

| VTEX field | How to fill it in VTEX | VTEX API | Marketplace field |
|------------|------------------------|-----------------------------------|-------------------|
| Name | Catalog page | /api/catalog/pvt/stockkeepingunit | ShortName |
| Image | Catalog page (SKU) | | Images |
