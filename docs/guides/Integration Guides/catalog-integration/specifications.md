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

<table>
    <tr>
        <td><strong>Field</strong></td>
        <td><strong>Description</strong></td>
        <td><strong>Required</strong></td>
        <td><strong>Format</strong></td>
        <td><strong>Default</strong></td>
    </tr>
    <tr>
        <td>Name</td>
        <td>Group's Name</td>
        <td>Yes</td>
        <td>String (150)</td>
        <td>-</td>
    </tr>
    <tr>
        <td>CategoryId</td>
        <td>Category where this group is associated</td>
        <td>No</td>
        <td>Integer</td>
        <td>null</td>
    </tr>
    <tr>
        <td>Position</td>
        <td>Store Framework - Deprecated. Classic CMS -</td>
        <td>No</td>
        <td>Integer</td>
        <td>null</td>
    </tr>
</table>

### API integration

The [Create specification group API request](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-group) may be used to create your groups.

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

<table>
    <tr>
        <td>Type</td>
        <td>ID</td>
    </tr>
    <tr>
        <td>Text</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Long Text (Textarea)</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Number</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Dropdown</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Radio</td>
        <td>6</td>
    </tr>
    <tr>
        <td>CheckBox</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Indexed Text</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Long Indexed Text</td>
        <td>9</td>
    </tr>
</table>

[block:callout]
{
  "type": "warning",
  "body": "For SKU fields (IsStockKeepingUnit = true) the only types of fields available are Dropdown and Radio, IDs 5 and 6 respectively."
}
[/block]
For more details about each field, you can access the  [Setting up the specification type](https://help.vtex.com/tutorial/configurando-tipo-de-campo-de-categoria?locale=en) documentation.

### Specification data model

<table>
    <tr>
        <td><strong>Field</strong></td>
        <td><strong>Description</strong></td>
        <td><strong>Required</strong></td>
        <td><strong>Format</strong></td>
        <td><strong>Default</strong></td>
    </tr>
    <tr>
        <td>FieldTypeId</td>
        <td>Specification Field Type Id (FieldType Table)</td>
        <td>Yes</td>
        <td>Integer</td>
        <td>-</td>
    </tr>
    <tr>
        <td>CategoryId</td>
        <td>CategoryId associated with this field</td>
        <td>No</td>
        <td>Integer</td>
        <td>null</td>
    </tr>
    <tr>
        <td>FieldGroupId</td>
        <td>GroupId associated with this field</td>
        <td>Yes</td>
        <td>Integer</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Name</td>
        <td>Field name</td>
        <td>Yes</td>
        <td>String (150)</td>
        <td>null</td>
    </tr>
    <tr>
        <td>Description</td>
        <td>Deprecated</td>
        <td>No</td>
        <td>String</td>
        <td>null</td>
    </tr>
    <tr>
        <td>Position</td>
        <td>Store Framework - Deprecated. Classic CMS - This position number is used in ordering the fields both in the
                navigation menu and in the field listing on the product page</td>
        <td>No</td>
        <td>Integer</td>
        <td>0</td>
    </tr>
    <tr>
        <td>IsFilter</td>
        <td>Store Framework - Deprecated. Classic CMS - To allow the specification field to be used as a facet (filter)
                on the search navigation bar.</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>IsRequired</td>
        <td>To make the specification field required</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>IsOnProductDetails</td>
        <td>Store Framework - Deprecated. Classic CMS -If field is visible on the Product page</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>IsStockKeepingUnit</td>
        <td>If true, it will be added as a SKU specification field. If false, it will be added as a product
            specification field.</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>IsWizard</td>
        <td>Deprecated</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>IsActive</td>
        <td>Enable/Disable field</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>IsTopMenuLinkActive</td>
        <td>Store Framework - Deprecated. Classic CMS - To make the specification field visible in the store's upper
                menu</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>IsSideMenuLinkActive</td>
        <td>Store Framework - Deprecated. Classic CMS - To make the specification field clickable in the search
                navigation bar</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>DefaultValue</td>
        <td></td>
        <td>No</td>
        <td>String</td>
        <td>null</td>
    </tr>
</table>

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

![Product register page example with specification](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/catalog-integration/a9bde79-catalog_technical_specifications_353.png)

### Specification values data model

<table>
    <tr>
        <td><strong>Field</strong></td>
        <td><strong>Description</strong></td>
        <td><strong>Required</strong></td>
        <td><strong>Format</strong></td>
        <td><strong>Default</strong></td>
    </tr>
    <tr>
        <td>FieldId</td>
        <td>FieldId associated with this fieldvalue</td>
        <td>Yes</td>
        <td>Integer</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Name</td>
        <td>Name of field value</td>
        <td>Yes</td>
        <td>String (150)</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Text</td>
        <td>Deprecated</td>
        <td>No</td>
        <td>String</td>
        <td>null</td>
    </tr>
    <tr>
        <td>IsActive</td>
        <td>Enable/Disable field value</td>
        <td>No</td>
        <td>Boolean (true/false)</td>
        <td>false</td>
    </tr>
    <tr>
        <td>Position</td>
        <td>The position of the value to be shown on product registration page (/admin/Site/Produto.aspx)</td>
        <td>No</td>
        <td>Integer</td>
        <td>0</td>
    </tr>
</table>

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