---
title: "Product and Category Mappings"
slug: "external-marketplace-integration-catalog-mapping"
hidden: false
createdAt: "2021-06-28T21:31:02.506Z"
updatedAt: "2022-02-03T18:04:42.939Z"
---

This section of the integration guide goes over which mappings are necessary to maintain the connection between the VTEX platform and the marketplace. It includes mappings for Catalog and mappings for Orders.

## Product Mapping

Usually marketplaces offer a unique ID that identifies an SKU within its storefront. This ID enables SKU consultation, updates, blocking and exclusion operations.

When this ID differs from the code that identifies the SKU within VTEX, the connector must offer a mechanism/repository that allows the mapping of these IDs.

It is important to implement a routine that allows the cleaning of this mapping in case the SKU is blocked or excluded in VTEX.

In case the marketplace’s ID is the same used in VTEX, this action is not necessary.

## Category Mapping

Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree.

To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace.

## VTEX Mapper

To use the category mapping service, follow the steps below, that will be further explored in the items that follow:

1. [Register the connector in VTEX Mapper](#register-the-connector-in-vtex-mapper)
2. [Send category tree to VTEX Mapper](#send-category-tree-to-vtex-mapper)
3. [Receive the category mapping in VTEX Mapper](#receive-the-category-mapping-in-vtex-mapper)
4. [Use the category mapping in the product registration flow](#use-the-category-mapping-in-the-product-registration-flow)

## API Reference

- [VTEX Mapper Registration](https://developers.vtex.com/vtex-rest-api/reference/vtex-mapper-registration)
- [Send Category Mapping to VTEX Mapper](https://developers.vtex.com/vtex-rest-api/reference/send-category-mapping-to-vtex-mapper)

### Register the connector in VTEX Mapper

After obtaining the [access keys](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication) to operate a VTEX account, the diagram below illustrates the necessary steps to register the connector in VTEX Mapper.
![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-integration-catalog-mapping-0.jpg)

1. Use the [Mapper Registration endpoint](https://developers.vtex.com/vtex-rest-api/reference/vtex-mapper-registration).
2. In case the registration is successful, VTEX Mapper returns a unique ID and endpoint to the connector. 
3. Store the ID returned, to be later used in the category tree update action, in VTEX Matcher.
[block:callout]
{
  "type": "info",
  "body": "In case VTEX Mapper detects an error and the call fails, the connector should check if mandatory information was sent correctly. Ex. are URLs correctly registered in the properties categoryTreeEndPoint and mappingEndPoint?",
  "title": "Errors"
}
[/block]

### Send category tree to VTEX Mapper

To send the marketplace’s category tree to VTEX Mapper, follow the steps illustrated in this diagram:
![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-integration-catalog-mapping-1.jpg)

1. Collect marketplace category tree.
2. Check if the category tree doesn’t already exist in its repository. 
a. If it is **not** mapped, store the category tree and the last update’s date. 
b. If it **is **mapped, check if the category tree has updates. If there are updates, send the full tree to the mapper (step 3). If there are no updates, update the tree’s date, and log informing the tree is updated. 
3. Assemble the full category tree schema, following the JSON example below. 
4. Send the category tree through the [Send Category Mapping to VTEX Mapper](https://developers.vtex.com/vtex-rest-api/reference/send-category-mapping-to-vtex-mapper) endpoint. Connectors should send the payload compacted in .gzip format.
5. If VTEX Mapper receives the category tree successfully, the call’s response will be a 204. Connectors should log the response offered by the Mapper.
[block:callout]
{
  "type": "info",
  "body": "Category tree processing is asynchronous. Once processing is complete, the Mapper will send the connector the confirmation of creation through the endpoint defined in the property connectorEndpoint during the integration’s registration in VTEX Mapper.",
  "title": "Processing"
}
[/block]
### Receive the category mapping in VTEX Mapper

VTEX Mapper will send the updated category mapping  through the endpoint defined in the property `mappingEndpoint` during the Mapper app’s registration.

Once receiving the category tree, the connector should store it. This data will be used during the catalog integration flow. Once receiving a notification from VTEX to integrate a product, connectors verify if the VTEX category ID sent from the catalog exists in the mapping sent by the mapper. 


### Use the category mapping in the product registration flow 

When receiving a VTEX notification to register an SKU in the marketplace, connectors should:

1. [Get SKU information](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-context) through the `{stockKeepUnit/skuId}` property. 
2. Collect value of `categoryId` property, from the call’s response.
3. Verify if the ID exists in the mapping previously sent by VTEX Mapper.  \
a) If the ID **exists**, collect the corresponding value in the marketplace.  \
b) If the ID **does not** exist, generate a log informing the seller that they should perform the category mapping in VTEX. 
4. With the corresponding ID, register the SKU in the marketplace, following the steps described in the [How to get a new product to offer in the marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-new-products) section.
