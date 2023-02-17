---
title: "Create a product"
slug: "create-a-product"
hidden: false
createdAt: "2021-12-14T13:52:49.437Z"
updatedAt: "2022-02-03T20:10:26.202Z"
---
A product is a generic definition of an item that is part of your store's Catalog, for instance, a shirt.

Products may vary by model, color, size, among other characteristics. Therefore, it would be possible to have the same product (shirt) in different models, like short or long sleeves, gray or pink color, sizes S, M or L. 

Each variation, such as a _long sleeve gray size S shirt_, will correspond to a [Stock Keeping Unit (SKU)](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA), which is the actual item in the inventory that customers can purchase. Before creating SKUs, you must create a product.

To insert a new product, use the [Create product API endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product).

When creating or updating products, note that any product must be associated with their corresponding [category](https://developers.vtex.com/docs/guides/categories) in the more specific category level.

>⚠️ We recommend leaving VTEX to automatically generate an ID, by not including a custom product ID in the `Id` field of the request body. The generated ID can be retrieved in the request's response and must be stored in the system for future updates of this product.

**Request body example**

```json
{
  "Id": null,
  "Name": "Zoom Stefan Janoski Canvas RM SB Varsity Red",
  "DepartmentId": 2000089,
  "CategoryId": 2000090,
  "BrandId": 12121219,
  "LinkId": "stefan-janoski-canvas-varsity-red",
  "RefId": "sr_1_90",
  "IsVisible": true,
  "Description": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
  "DescriptionShort": "The Nike Zoom Stefan Janoski is made with a premium leather.",
  "ReleaseDate": "2023-01-01T00:00:00",
  "KeyWords": "Zoom,Stefan,Janoski",
  "Title": "Zoom Stefan Janoski Canvas RM SB Varsity Red",
  "IsActive": true,
  "MetaTagDescription": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
  "ShowWithoutStock": true,
}
```

**Response body example**

```json
{
  "Id": 42,
  "Name": "Zoom Stefan Janoski Canvas RM SB Varsity Red",
  "DepartmentId": 2000089,
  "CategoryId": 2000090,
  "BrandId": 12121219,
  "LinkId": "stefan-janoski-canvas-varsity-red",
  "RefId": "sr_1_90",
  "IsVisible": true,
  "Description": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
  "DescriptionShort": "The Nike Zoom Stefan Janoski is made with a premium leather.",
  "ReleaseDate": "2023-01-01T00:00:00",
  "KeyWords": "Zoom,Stefan,Janoski",
  "Title": "Zoom Stefan Janoski Canvas RM SB Varsity Re",
  "IsActive": true,
  "TaxCode": "",
  "MetaTagDescription": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
  "SupplierId": 1,
  "ShowWithoutStock": true,
  "AdWordsRemarketingCode": null,
  "LomadeeCampaignCode": null,
  "Score": 1
}
```

## Update a product

In case you have already created a product and want to change it, use the [Update product API request](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/product/-productId-), sending in the `Id` of the product already created.

>❗ If you need to change any product field, it is necessary to send all the other fields in the request. Otherwise, all previously configured information from blank fields will be deleted. Therefore, before making a change, you should [get the product data](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-) for the same `Id` and use the response as a template to make the change.

**Request body example**

```json
{
    "Id": 42,
    "Name": "Zoom Stefan Janoski Canvas RM SB Varsity Red",
    "DepartmentId": 2000089,
    "CategoryId": 2000090,
    "BrandId": 12121219,
    "LinkId": "stefan-janoski-canvas-varsity-red",
    "RefId": "sr_1_90",
    "IsVisible": true,
    "Description": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
    "DescriptionShort": "The Nike Zoom Stefan Janoski is made with a premium leather.",
    "ReleaseDate": "2023-01-01T00:00:00",
    "KeyWords": "Zoom,Stefan,Janoski",
    "Title": "Zoom Stefan Janoski Canvas RM SB Varsity Re",
    "IsActive": true,
    "TaxCode": "",
    "MetaTagDescription": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
    "SupplierId": 1,
    "ShowWithoutStock": true,
    "AdWordsRemarketingCode": null,
    "LomadeeCampaignCode": null,
    "Score": 1
}
```

**Response body example**

```json
{
    "Id": 42,
    "Name": "Zoom Stefan Janoski Canvas RM SB Varsity Red",
    "DepartmentId": 2000089,
    "CategoryId": 2000090,
    "BrandId": 12121219,
    "LinkId": "stefan-janoski-canvas-varsity-red",
    "RefId": "sr_1_90",
    "IsVisible": true,
    "Description": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
    "DescriptionShort": "The Nike Zoom Stefan Janoski is made with a premium leather.",
    "ReleaseDate": "2023-01-01T00:00:00",
    "KeyWords": "Zoom,Stefan,Janoski",
    "Title": "Zoom Stefan Janoski Canvas RM SB Varsity Red",
    "IsActive": true,
    "TaxCode": "",
    "MetaTagDescription": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
    "SupplierId": 1,
    "ShowWithoutStock": true,
    "AdWordsRemarketingCode": null,
    "LomadeeCampaignCode": null,
    "Score": 1
}
```
