---
title: "Products"
slug: "products"
hidden: false
createdAt: "2021-12-14T13:52:49.437Z"
updatedAt: "2022-02-03T20:10:26.202Z"
---
Learn more about [products in VTEX catalog](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru#).

## Data Model 

<table>
  <tr>
   <td><strong>Field</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Required</strong>
   </td>
   <td><strong>Format</strong>
   </td>
   <td><strong>Default</strong>
   </td>
  </tr>
  <tr>
   <td>Id
   </td>
   <td>Product ID. If not provided, it will be generated automatically (sequence)
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>AutoIncrement
   </td>
  </tr>
  <tr>
   <td>Name
   </td>
   <td>Product name
   </td>
   <td>Yes
   </td>
   <td>String (150)
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>DepartmentId
   </td>
   <td>Department ID according to the product's category. This field should not be provided during product creation.
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>CategoryId
   </td>
   <td>Category ID associated with this product.
   </td>
   <td>Yes
   </td>
   <td>Integer
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>BrandId
   </td>
   <td>Brand ID associated with this product
   </td>
   <td>Yes
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>LinkId
   </td>
   <td>String to be used to build the product URL. If it not informed, it will be generated automatically according to product's name replacing spaces and special characters with hyphens (`-`)
   </td>
   <td>No
   </td>
   <td>String(255)
   </td>
   <td>Product Name
   </td>
  </tr>
  <tr>
   <td>RefId
   </td>
   <td>Product reference code
   </td>
   <td>No
   </td>
   <td>String(200)
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>IsVisible
   </td>
   <td>Show/Hide product in search result and product page but can be added into shopping cart. Usually applicable for gifts.
   </td>
   <td>No
   </td>
   <td>Boolean (true/false)
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>Description
   </td>
   <td>Product description
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>DescriptionShort
   </td>
   <td>Product short description. This information is presented by:
<ul>

<li>Store Framework:  <strong>$product.DescriptionShort</strong> control

<li>Classic CMS:

<p>
And can be displayed on both the product page and the shelf.
</li>
</ul>
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>ReleaseDate
   </td>
   <td>Used to assist in the ordering of the search result of the site. Using the O=OrderByReleaseDateDESC query string, you can pull this value and show the display order by release date. This attribute is also used as a condition for dynamic collections.
   </td>
   <td>No
   </td>
   <td>DateTime
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>KeyWords
   </td>
   <td>Store Framework: Deprecated
<p>
Classic CMS: Synonyms of terms related to product. "Television", for example, can have a substitute word like "TV". This field is important to make your searches more comprehensive.
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Title
   </td>
   <td>Product title tag. It is displayed in the browser tab and corresponds to the title of the product page. This field is important for SEO.
   </td>
   <td>No
   </td>
   <td>String (150)
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>IsActive
   </td>
   <td>Activate/Inactivate  product
   </td>
   <td>No
   </td>
   <td>Boolean (true/false)
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>TaxCode
   </td>
   <td>Product fiscal number. Usually used for tax calculation.
   </td>
   <td>No
   </td>
   <td>String (50)
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>MetaTagDescription
   </td>
   <td>Brief description of the product for SEO. It's recommended that you don't exceed 150 characters.
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>SupplierId
   </td>
   <td>Deprecated
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>ShowWithoutStock
   </td>
   <td>If true, activates "Notify Me" form when the product is out of stock.
   </td>
   <td>No
   </td>
   <td>Boolean (true/false)
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>AdWordsRemarketingCode
   </td>
   <td>Deprecated
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>LomadeeCampaignCode
   </td>
   <td>Deprecated
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Score
   </td>
   <td>Value used to set the priority on the search result page.
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
</table>


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