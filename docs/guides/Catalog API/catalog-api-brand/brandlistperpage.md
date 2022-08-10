---
title: "Get Brand List Per Page"
slug: "brandlistperpage"
excerpt: "Retrieves all Brands registered in the store's Catalog by page number."
hidden: false
createdAt: "2021-09-20T17:13:52.612Z"
updatedAt: "2021-09-29T18:07:34.783Z"
---
## Response body has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `items` | array of objects | Array of objects with information of the store's brands. |
| `id` | integer | Brand unique number identifier. |
| `name` | string      |  Brand name.  |
| `imageUrl`  | string | Brand image URL. |
| `isActive` | boolean    | Condition if the brand is active or not.  |
| `title` | string | Title shown in the browser bar, which corresponds to the title of your page. |
| `metaTagDescription` | string | A brief description of the brand, displayed by search engines. Since search engines can only display less than 150 characters, we recommend not exceeding this character limit when creating the description. |
| `paging` | object | Object with information about the paging. |
| `page` | integer | Page number of the brand list. |
| `perPage` | integer | Quantity of brands per page. |
| `total` | integer | Total of brands in the store. |
| `pages` | integer | Total number of pages. |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"items\": [\n    {\n      \"id\": 2000000,\n      \"name\": \"Farm\",\n      \"isActive\": true,\n      \"title\": \"Farm\",\n      \"metaTagDescription\": \"Farm\",\n      \"imageUrl\": null\n    },\n    {\n      \"id\": 2000001,\n      \"name\": \"Adidas\",\n      \"isActive\": true,\n      \"title\": \"\",\n      \"metaTagDescription\": \"\",\n      \"imageUrl\": null\n    },\n    {\n      \"id\": 2000002,\n      \"name\": \"Brastemp\",\n      \"isActive\": true,\n      \"title\": \"Brastemp\",\n      \"metaTagDescription\": \"Brastemp\",\n      \"imageUrl\": null\n    }\n  ],\n    \"paging\": {\n      \"page\": 1,\n        \"perPage\": 3,\n          \"total\": 6,\n            \"pages\": 2\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]