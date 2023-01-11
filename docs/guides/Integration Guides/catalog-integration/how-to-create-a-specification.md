---
title: "How to create a specification"
slug: "how-to-create-a-specification"
hidden: false
createdAt: "2021-03-25T20:16:13.760Z"
updatedAt: "2022-05-12T15:03:54.944Z"
---

Specifications are additional properties that can be added to your store's products or SKUs. A specification is used to create site browsing filters and to differentiate SKUs and products within the product page.

This guide will describe all the steps to create a specification for a product or an SKU. They are (steps with * are mandatory):

1. Create a specification group*
2. Create a specification*
3. Create a specification value
4. Associating a specification to a product or to an SKU*

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration%20Guides/catalog-integration/how-to-create-a-specification-0_18.png)

## Creating a Specification Group

The first step is to create a Specification Group. A Specification Group is a grouping of specifications related to a product or SKUs. The specification group is associated with a category and all products or SKUs.

To create a specification group, use the [Create Specification Group](https://developers.vtex.com/vtex-rest-api/reference/specificationgroupinsert2) endpoint. The request body for this endpoint must include the `CategoryId` of the category that you are creating the specification group and the `Name` for the specification group. See the request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CategoryId\": 11,\n    \"Name\": \"Features\"\n}",
      "language": "json"
    }
  ]
}
[/block]
You can also configure the `CategoryId`  attribute as `null`. This will set the specification group to global, valid to all Categories in your Catalog. See the request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CategoryId\": null,\n    \"Name\": \"Features\"\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "You need to create the specification group in the category associated with the desired product or SKU. If you create a specification group on a different category and associate it to the product or SKU by API the response will return `200 OK`, but it won’t be visible at the Admin or your store, only by API."
}
[/block]
## Creating a Specification

After creating a Specification Group, use the [Create Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification) endpoint to create the specification. To create the specification as an SKU specification, you need to set `IsStockKeepingUnit` as `true`. To create a product specification, set `IsStockKeepingUnit` as `false`.

You will need the `FieldGroupId`. To know the ID of the specification group previously created, you can use the [List Specifications Group by Category](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-group-categoryid) endpoint to get all groups from a category. 

The request body for this endpoint also includes the `FieldTypeId` that refers to the type you defined as this specification’s type. 

To create a specification you will firstly need to define its type. Available types are:

- **Text**: this specification is a small text, one-line restricted. The content is free text, but not suitable for large HTML structures.
- **Multi-Line Text**: this specification is a larger text, containing a multi-line text. The content is free text, suitable for large HTML structures.
- **Number**: this specification is an integer number.
- **Combo**: this specification is a dropdown component with all the values you configure to it. This specification can be selected by the buyer. 
- **Radio**: this specification is a radio button with all the values you configure to it. This specification can be selected by the buyer.
- **Checkbox**: this specification is a list of values with selectable checkboxes. This specification can be selected by the buyer.
- **Indexed Text**: this specification is a small text, one-line restricted. The content is free text, but not suitable for large HTML structures. The value will be directed to the Catalog indexer, so it will influence the search results of customers in the store.
- **Indexed Multi-Line Text**: this specification is a larger text, containing a multi-line text. The content is free text, suitable for large HTML structures. The value will be directed to the Catalog indexer, so it will influence the search results of customers in the store.

Below you will find a table with IDs by specification type. 
[block:parameters]
{
  "data": {
    "h-0": "Specification type",
    "h-1": "ID",
    "0-0": "Text",
    "0-1": "1",
    "1-0": "Multi-Line Text",
    "1-1": "2",
    "2-0": "Number",
    "2-1": "4",
    "3-0": "Combo",
    "3-1": "5",
    "4-0": "Radio",
    "4-1": "6",
    "5-0": "Checkbox",
    "5-1": "7",
    "6-0": "Indexed Text",
    "6-1": "8",
    "7-1": "9",
    "7-0": "Indexed Multi-Line Text"
  },
  "cols": 2,
  "rows": 8
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "When creating an SKU Specification, the request only allows two possible types: Radio or Combo. If you set up other types and `IsStockKeepingUnit` as `true`, the request will return `400 Bad Request` with the error message `Sku Field can be only of the Radio or Combo type`."
}
[/block]
Check the request body example below to see all requirements. You can read their descriptions on the [endpoint documentation](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification).
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldTypeId\": 1,\n    \"CategoryId\": 11,\n    \"FieldGroupId\": 1,\n    \"Name\": \"Fabric\",\n    \"Description\": \"Fabric of the dress\",\n    \"Position\": 1,\n    \"IsFilter\": true,\n    \"IsRequired\": true,\n    \"IsOnProductDetails\": true,\n    \"IsStockKeepingUnit\": false,\n    \"IsActive\": true,\n    \"IsTopMenuLinkActive\": false,\n    \"IsSideMenuLinkActive\": true,\n    \"DefaultValue\": \"Cotton\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Creating a Specification Value

After creating the specification, you need to add value - or values - to it. You can add multiple values to the specification, therefore creating the selective options displayed to the buyer. 

[block:callout]
{
  "type": "warning",
  "body": "You can only create specification values for the Combo and Radio specification types. To add value to the other specification types, check the section of [Associating a Specification to a Product](https://developers.vtex.com/vtex-developer-docs/docs/how-to-create-a-specification#to-a-product) of this guide."
}
[/block]
Use the [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) endpoint to create the specification value. You need to add the `FieldId` in the request body. To get the ID of the specification you created, use the [Get Specifications By Category ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-category) endpoint.

Check the request body example below to see all requirements and read their descriptions on the [endpoint documentation](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value).
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 1,\n    \"Name\": \"Cotton\",\n    \"Text\": \"The dress is made of cotton\",\n    \"IsActive\": true,\n    \"Position\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]

> ℹ️️ This request is only valid to one specification at a time. To register multiple values to one specification, you will need to create a request for each one of the values.

## Associating a Specification 

Once you have created a specification, and if needed added a value to it, you will associate the specification with a product or an SKU. 

### To a Product

To associate a specification with a product, use the [Associate Product Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-create-product-specification) endpoint. There are two different request bodies possible. This depends on the type of the created specification. Check the request body examples below to know which use when associating your specification with a product.

For Combo and Radio types:

To get the `FieldValueId` from the previously created specification value, use the [Get Specifications Values By Field ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-field-value-fieldid) endpoint.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 1,\n    \"FieldValueId\": 13\n}",
      "language": "json"
    }
  ]
}
[/block]
For the other specification types:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 1,\n    \"Text\": \"Cotton\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### To an SKU
To associate a specification with an SKU, use the [Associate SKU Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-specification) endpoint. As informed before, the SKU specification can only be the Combo and Radio types. 

Check the request body example below to see all requirements and read their descriptions on the [endpoint documentation](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-specification).

To get the `FieldValueId` from the previously created specification value, use the [Get Specifications Values By Field ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-field-value-fieldid) endpoint.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 1,\n    \"FieldValueId\": 13\n}",
      "language": "json"
    }
  ]
}
[/block]
