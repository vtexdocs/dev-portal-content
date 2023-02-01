---
title: "Specifications"
slug: "specifications"
hidden: false
createdAt: "2021-12-14T13:38:45.386Z"
updatedAt: "2022-02-03T20:15:19.310Z"
---

Specifications are additional properties that can be added to your store's products or SKUs. A specification is used to create site browsing filters and to differentiate SKUs and products within the product page.

Here we take a look at some of the integration aspects of specifications, but we recommend you also check this detailed step by step guide on [How to create a specification](https://developers.vtex.com/vtex-rest-api/docs/how-to-create-a-specification).

## Groups

To create specifications, it is necessary to register the groups. Groups are specification groupers, for example, we can create a group named Technical Specifications, and in it we can insert specifications referring to the product's technical data, such as material, voltage, dimensions, etc.

[block:callout]
{
  "type": "warning",
  "body": "The groups and fields created will be valid for its registration category and for all child categories. For example, if a field is created in the root category, it will be available in all store categories."
}
[/block]

Usually just one group is created at root level and all the specification fields are associated with this group.

### Groups data model

| Field | Description | Required | Format | Default |
|---|---|---|---|---|
| Name | Group's Name | Yes | String (150) | - |
| CategoryId | Category where this group is associated | No | Integer | null |
| Position | Store Framework - Deprecated. Classic CMS - | No | Integer | null |

### API integration

The [Create specification group API request](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specificationgroup) may be used to create your groups.

[block:callout]
{
  "type": "warning",
  "body": "If the CategoryId field is null, the group will be created in the root category."
}
[/block]

#### Example request

Body:

```json
{
    "CategoryId": null,
    "Name": "Technical Specifications",
    "Position": 1
}
```

Response:

```json
{
    "Id": 34,
    "CategoryId": null,
    "Name": "Technical Specifications",
    "Position": 1
}
```

## Specification fields

Specifications are additional properties that can be added to your store's products or SKUs. In VTEX, these specifications are associated with specific categories.

### Product Specification

A product specification is generally used to create site browsing filters or to display additional product information.

For example, in a fashion store you would be able to create a product specification to let your client know which type of fabric is sold in your store.

This information could be displayed as a filter in the search navigation menu or as an informative text inside the product page.

Product specifications can receive data such as strings and numbers, which VTEX APIs then consume and use for front-end customizations or to send information to external integrations.

### SKU Specifications

SKU specifications are used to create site browsing filters and to differentiate SKUs within the product page.

For example, a store that sells shirts, you would be able to create a SKU specification to tell your products apart by size.

Your SKU specifications would have values such as XS, S, M, L and XL. These would be used as a browsing filter on your site. In addition, these specifications would work as SKU selectors on the product page.

[block:callout]
{
  "type": "warning",
  "body": "In VTEX, SKU specifications are mandatory fields required to add SKUs, meaning that if a specification were to be created in a category, all SKUs within that category would need to carry this new specification. All these SKUs are therefore disabled until this new specification is added to the SKUs of the category in question."
}
[/block]

### FieldType

When registering fields, it is necessary to specify the type of values accepted by that field. Available options are listed below with their respective IDs.

Fields as **dropdown**, **radio** or **checkbox** can be used as filters on the search navigation menu.

| Type | ID |
|---|---|
| Text | 1 |
| Long Text (Textarea) | 2 |
| Number | 4 |
| Dropdown | 5 |
| Radio | 6 |
| CheckBox | 7 |
| Indexed Text | 8 |
| Long Indexed Text | 9 |

[block:callout]
{
  "type": "warning",
  "body": "For SKU fields (IsStockKeepingUnit = true) the only types of fields available are Dropdown and Radio, IDs 5 and 6 respectively."
}
[/block]

For more details about each field, you can access the  [Adding product specifications or fields](https://help.vtex.com/en/tutorial/adding-specifications-or-product-fields--tutorials_106#product-field-types) or the [Adding SKU specifications or fields](https://help.vtex.com/en/tutorial/adding-sku-specifications-or-fields--tutorials_119#sku-field-types) documentation.

### Specification data model

| Field | Description | Required | Format | Default |
|---|---|---|---|---|
| FieldTypeId | Specification Field Type Id (FieldType Table). | Yes | Integer | - |
| CategoryId | CategoryId associated with this field. | No | Integer | null |
| FieldGroupId | GroupId associated with this field. | Yes | Integer | - |
| Name | Field name. | Yes | String (150) | null |
| Description | Deprecated. | No | String | null |
| Position | Store Framework - Deprecated. Classic CMS - This position number is used in ordering the fields both in the navigation menu and in the field listing on the product page. | No | Integer | 0 |
| IsFilter | Store Framework - Deprecated. Classic CMS - To allow the specification field to be used as a facet (filter) on the search navigation bar. | No | Boolean (true/false) | false |
| IsRequired | To make the specification field required. | No | Boolean (true/false) | false |
| IsOnProductDetails | Store Framework - Deprecated. Classic CMS -If field is visible on the Product page. | No | Boolean (true/false) | false |
| IsStockKeepingUnit | If true, it will be added as a SKU specification field. If false, it will be added as a product             specification field. | No | Boolean (true/false) | false |
| IsWizard | Deprecated. | No | Boolean (true/false) | false |
| IsActive | Enable/Disable field. | No | Boolean (true/false) | false |
| IsTopMenuLinkActive | Store Framework - Deprecated. Classic CMS - To make the specification field visible in the store's upper menu. | No | Boolean (true/false) | false |
| IsSideMenuLinkActive | Store Framework - Deprecated. Classic CMS - To make the specification field clickable in the search navigation bar | No | Boolean (true/false) | false |
| DefaultValue | Specification default value. | No | String | null |

### API integration

To create a specification, use the [Create specification API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification). See the example request below.

Body:

```json
{
    "FieldTypeId": 6,
    "CategoryId": 2000089,
    "FieldGroupId": 34,
    "Name": "Material",
    "Position": 1,
    "IsFilter": false,
    "IsRequired": true,
    "IsOnProductDetails": false,
    "IsStockKeepingUnit": false,
    "IsActive": true,
    "IsTopMenuLinkActive": false,
    "IsSideMenuLinkActive": true,
    "DefaultValue": ""
}
```

[block:callout]
{
  "type": "warning",
  "body": "If the `CategoryId` field is null, the field will be created in the root category."
}
[/block]

Response:

```json
{
    "Id": 193,
    "FieldTypeId": 6,
    "CategoryId": 2000089,
    "FieldGroupId": 34,
    "Name": "Material",
    "Description": null,
    "Position": 1,
    "IsFilter": true,
    "IsRequired": true,
    "IsOnProductDetails": false,
    "IsStockKeepingUnit": false,
    "IsWizard": false,
    "IsActive": true,
    "IsTopMenuLinkActive": false,
    "IsSideMenuLinkActive": false,
    "DefaultValue": null
}
```

## Specification values

After creating the specification fields, if the `FieldTypeId` is `5`, `6` or `7` (Combo, Radio or Checkbox), it is necessary to register the respective possible values.

Those values will be shown on product register page like this one:

![Product register page example with specification](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/specifications-0.png)

### Specification values data model

| Field | Description | Required | Format | Default |
|---|---|---|---|---|
| FieldId | FieldId associated with this fieldvalue | Yes | Integer | - |
| Name | Name of field value | Yes | String (150) | - |
| Text | Deprecated | No | String | null |
| IsActive | Enable/Disable field value | No | Boolean (true/false) | false |
| Position | The position of the value to be shown on product registration page (/admin/Site/Produto.aspx) | No | Integer | 0 |

### API integration

To register a new value for a specification use the [Create specifications value API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value).

[block:callout]
{
  "type": "warning",
  "body": "Use this request for one value of one specification at a time. To register multiple values to one specification, you will need to create a request for each of the values."
}
[/block]
See the example request below.

Body:

```json
{
    "FieldId": 193,
    "Name": "Metal",
    "IsActive": true,
    "Position": 1
}
```

Response:

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
