---
title: "Products"
slug: "products"
hidden: false
createdAt: "2021-12-14T13:52:49.437Z"
updatedAt: "2022-02-03T20:10:26.202Z"
---
Learn more about [products in VTEX catalog](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru#).

## Data Model

| **Field**   | **Description**    | **Required**    | **Format**    | **Default** |
|---|---|---|---|---|
| Id    | Product ID. If not provided, it will be generated automatically (sequence)    | No    | Integer    | AutoIncrement    |
| Name    | Product name    | Yes    | String (150)    | -    |
| DepartmentId    | Department ID according to the product's category. This field should not be provided during product creation.    | No    | String    | -    |
| CategoryId    | Category ID associated with this product.    | Yes    | Integer    | -    |
| BrandId    | Brand ID associated with this product    | Yes    | Integer    | null    |
| LinkId    | String to be used to build the product URL. If it not informed, it will be generated automatically according to product's name replacing spaces and special characters with hyphens (`-`)    | No    | String(255)    | Product Name    |
| RefId    | Product reference code    | No    | String(200)    | null    |
| IsVisible    | Show/Hide product in search result and product page but can be added into shopping cart. Usually applicable for gifts.    | No    | Boolean (true/false)    | false    |
| Description    | Product description    | No    | String    | null    |
| DescriptionShort    | Product short description. This information is presented by the `$product.DescriptionShort` control and can be displayed on both the product page and the shelf.    | No    | String    | null    |
| ReleaseDate    | Used to assist in the ordering of the search result of the site. Using the O=OrderByReleaseDateDESC query string, you can pull this value and show the display order by release date. This attribute is also used as a condition for dynamic collections.    | No    | DateTime    | null    |
| KeyWords    | Store Framework: Deprecated. Legacy CMS Portal: Synonyms of terms related to product. "Television", for example, can have a substitute word like "TV". This field is important to make your searches more comprehensive.    | No    | String    | null    |
| Title    | Product title tag. It is displayed in the browser tab and corresponds to the title of the product page. This field is important for SEO.    | No    | String (150)    | null    |
| IsActive    | Activate/Inactivate  product    | No    | Boolean (true/false)    | false    |
| TaxCode    | Product fiscal number. Usually used for tax calculation.    | No    | String (50)    | null    |
| MetaTagDescription    | Brief description of the product for SEO. It's recommended that you don't exceed 150 characters.    | No    | String    | null    |
| SupplierId    | Deprecated    | No    | Integer    | null    |
| ShowWithoutStock    | If true, activates "Notify Me" form when the product is out of stock.    | No    | oolean (true/false)    | false    |
| AdWordsRemarketingCode    | Deprecated    | No    | String    | null    |
| LomadeeCampaignCode    | Deprecated    | No    | String    | null    |
| Score    | Value used to set the priority on the search result page.    | No    | Integer    | null    |

## API integration

### Create a product

Use the [Create product API endpoint](https://developers.vtex.com/vtex-rest-api/reference/post-product) to insert a new product.

#### Example request

Body:

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
  "ReleaseDate": "2020-01-01T00:00:00",
  "KeyWords": "Zoom,Stefan,Janoski",
  "Title": "Zoom Stefan Janoski Canvas RM SB Varsity Red",
  "IsActive": true,
  "MetaTagDescription": "The Nike Zoom Stefan Janoski Men's Shoe is made with a premium leather upper for superior durability and a flexible midsole for all-day comfort. A tacky gum rubber outsole delivers outstanding traction.",
  "ShowWithoutStock": true,
}
```

Response:

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
  "ReleaseDate": "2020-01-01T00:00:00",
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

[block:callout]
{
  "type": "warning",
  "body": "We recommend not sending the product ID (`Id` field), leaving VTEX to manage the creation of IDs. The ID that is generated can be retrieved in the request's response and must be stored in the system for future updates of this product."
}
[/block]

### Update a product

If you have already created a Product and want to change it, use the [Update product API request](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-product), sending in the `Id` of the product already created.

#### Example request

Body:

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
    "ReleaseDate": "2020-01-01T00:00:00",
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

Response:

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
    "ReleaseDate": "2020-01-01T00:00:00",
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

[block:callout]
{
  "type": "danger",
  "title": "Keep in mind",
  "body": "- If you need to change any product field, it is necessary to send the other fields, otherwise, the fields not entered will be deleted. Therefore, we suggest that before making a change, you should [get the product data](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-product#catalog-api-get-product) for the same `Id` and use the response as a template to make the change.\n- When creating or updating products note that any product must be associated with the lowest level of category tree."
}
[/block]
