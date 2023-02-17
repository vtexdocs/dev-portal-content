---
title: "Specifications"
slug: "specifications"
hidden: false
createdAt: "2021-12-14T13:38:45.386Z"
updatedAt: "2022-02-03T20:15:19.310Z"
---

Specifications are additional properties that can be added to your store's products or SKUs. A specification is used to create site browsing filters and to differentiate SKUs and products within the product page.

This guide will describe all the steps to create a specification for a product or an SKU:

1. Create a specification group (mandatory)
2. Create a specification (mandatory)
3. Create a specification value
4. Associate a specification to a product or to an SKU (mandatory)

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-create-a-specification-0.png)

## Specification Groups

To create specifications, the first step is to create specification groups. They are specification aggregators, for example, we can create a group named Technical Specifications, and in it we can insert specifications referring to the product's technical data, such as material, voltage, dimensions, etc.

>⚠️ The groups and fields created will be valid for its registration category and for all child categories. For example, if a field is created in the root category, it will be available in all store categories.

Usually just one group is created at root level and all the specification fields are associated with this group.

### Create a Specification Group

To create a specification group, use the [Create Specification Group](https://developers.vtex.com/vtex-rest-api/reference/specificationgroupinsert2) endpoint. The request body for this endpoint must include the `CategoryId` of the category that you are creating the specification group and the `Name` for the specification group. See the request body example below:

```json
{
    "CategoryId": 11,
    "Name": "Features"
}
```

You can also configure the `CategoryId`  attribute as `null`. This will set the specification group to global, valid to all Categories in your Catalog. See the request body example below:

```json
{
    "CategoryId": null,
    "Name": "Features"
}
```

>⚠️ You need to create the specification group in the category associated with the desired product or SKU. If you create a specification group on a different category and associate it to the product or SKU by API the response will return `200 OK`, but it won't be visible at the Admin or your store, only by API.

## Specifications

After creating a Specification Group, you must create the specification field itself, which can be a [SKU specification](#sku-specifications) or a [product specification](#product-specifications).

### Product Specifications

A product specification is generally used to create site browsing filters or to display additional product information.

For example, in a fashion store you would be able to create a product specification to let your client know which type of fabric is sold in your store.

This information could be displayed as a filter in the search navigation menu or as an informative text inside the product page.

Product specifications can receive data such as strings and numbers, which VTEX APIs then consume and use for front-end customizations or to send information to external integrations.

### SKU Specifications

SKU specifications are used to create site browsing filters and to differentiate SKUs within the product page.

For example, a store that sells shirts, you would be able to create a SKU specification to tell your products apart by size.

Your SKU specifications would have values such as XS, S, M, L and XL. These would be used as a browsing filter on your site. In addition, these specifications would work as SKU selectors on the product page.

>⚠️ In VTEX, SKU specifications are mandatory fields required to add SKUs, meaning that if a specification were to be created in a category, all SKUs within that category would need to carry this new specification. All these SKUs are therefore disabled until this new specification is added to the SKUs of the category in question.

For more details about each field, you can access the  [Adding product specifications or fields](https://help.vtex.com/en/tutorial/adding-specifications-or-product-fields--tutorials_106#product-field-types) or the [Adding SKU specifications or fields](https://help.vtex.com/en/tutorial/adding-sku-specifications-or-fields--tutorials_119#sku-field-types) documentation.

### Create a specification

To create a specification, use the [Create specification API endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specification).

Consider the following aspects in the request body:

- If you are creating an [SKU specification](#sku-specifications), you need to set `IsStockKeepingUnit` as `true`. If it is a [product specification](#product-specifications), set `IsStockKeepingUnit` as `false`.
- You will need the `FieldGroupId`, which is the ID of the specification group previously created. You can use the [List Specifications Group by Category](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-group-categoryid) endpoint to get all groups IDs from a category. 
- The request body for this endpoint also includes the `FieldTypeId` that refers to the type you defined as this specification's type. The available types are:

| Specification Type | ID | Description |
|-|-|-|
|Text|1| This specification is a small text, one-line restricted. The content is free text, but not suitable for large HTML structures. |
|Multi-line Text|2| this specification is a larger text, containing a multi-line text. The content is free text, suitable for large HTML structures.|
|Number|4| this specification is an integer number.|
|Combo|5|this specification is a dropdown component with all the values you configure to it. This specification can be selected by the buyer. |
|Radio|6|this specification is a radio button with all the values you configure to it. This specification can be selected by the buyer.|
|Checkbox|7|this specification is a list of values with selectable checkboxes. This specification can be selected by the buyer.|
|Indexed Text|8|this specification is a small text, one-line restricted. The content is free text, but not suitable for large HTML structures. The value will be directed to the Catalog indexer, so it will influence the search results of customers in the store.|
|Indexed Multi-Line Text|9|this specification is a larger text, containing a multi-line text. The content is free text, suitable for large HTML structures. The value will be directed to the Catalog indexer, so it will influence the search results of customers in the store.|

>⚠️ When creating an SKU Specification, the request only allows two possible types: **Combo** or **Radio**. If you set up other types and `IsStockKeepingUnit` as `true`, the request will return `400 Bad Request` with the error message `Sku Field can be only of the Radio or Combo type`.

**Request body example:**

```json
{
    "FieldTypeId": 1,
    "CategoryId": 11,
    "FieldGroupId": 1,
    "Name": "Fabric",
    "Description": "Fabric of the dress",
    "Position": 1,
    "IsFilter": true,
    "IsRequired": true,
    "IsOnProductDetails": true,
    "IsStockKeepingUnit": false,
    "IsActive": true,
    "IsTopMenuLinkActive": false,
    "IsSideMenuLinkActive": true,
    "DefaultValue": "Cotton"
}
```

>⚠️ If the `CategoryId` field is null, the field will be created in the root category.

**Response body example:**

```json
{
    "Id": 193,
    "FieldTypeId": 1,
    "CategoryId": 11,
    "FieldGroupId": 1,
    "Name": "Fabric",
    "Description": "Fabric of the dress",
    "Position": 1,
    "IsFilter": true,
    "IsRequired": true,
    "IsOnProductDetails": true,
    "IsStockKeepingUnit": false,
    "IsActive": true,
    "IsTopMenuLinkActive": false,
    "IsSideMenuLinkActive": true,
    "DefaultValue": "Cotton"
}
```

## Specification values

After creating the specification fields, if the `FieldTypeId` is `5` or `6` or `7` (Combo, Radio or Checkbox), it is necessary to register the respective possible values.

You can add multiple values to the specification, therefore creating the selective options displayed to the buyer. These values will be shown on the product form, as illustrated below:

![Product register page example with specification](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/specifications-0.png)

### Create specification values

Use the [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) endpoint to create the specification value.

You need to add the `FieldId` in the request body. To get the ID of the specification you created, use the [Get Specifications By Category ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-category) endpoint.


>⚠️ Use this request for one value of one specification at a time. To register multiple values to one specification, you will need to create a request for each of the values.

See the example request below.

**Request body example:**

```json
{
    "FieldId": 193,
    "Name": "Metal",
    "IsActive": true,
    "Position": 1
}
```

**Response body example:**

```json
{
    "FieldValueId": 360,
    "FieldId": 193,
    "Name": "Metal",
    "Text": null,
    "IsActive": true,
    "Position": 1
}
```

>❗ You should activate specification fields, otherwise they will not work.

## Associating a Specification 

Once you have created a specification, and if needed added a value to it, you will associate the specification with a product or an SKU.

### To a Product

To associate a specification with a product, use the [Associate Product Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-create-product-specification) endpoint. There are two different request bodies possible. This depends on the type of the created specification. Check the request body examples below to know which use when associating your specification with a product.

For Combo and Radio types:

To get the `FieldValueId` from the previously created specification value, use the [Get Specifications Values By Field ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-field-value-fieldid) endpoint.

```json
{
    "FieldId": 1,
    "FieldValueId": 13
}
```

For the other specification types:

```json
{
    "FieldId": 1,
    "Text": "Cotton"
}
```

### To an SKU

To associate a specification with an SKU, use the [Associate SKU Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-specification) endpoint. As informed before, the SKU specification can only be the Combo and Radio types.

Check the request body example below to see all requirements and read their descriptions on the [endpoint documentation](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-specification).

To get the `FieldValueId` from the previously created specification value, use the [Get Specifications Values By Field ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-field-value-fieldid) endpoint.

```json
{
    "FieldId": 1,
    "FieldValueId": 13
}
```
