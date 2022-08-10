---
title: "Update a Brand"
slug: "putbrand"
excerpt: "The endpoint updates an existing brand."
hidden: true
createdAt: "2021-07-05T14:05:36.177Z"
updatedAt: "2022-07-20T20:09:02.058Z"
---
## Request body has the following properties:

| Attribute          | Type    | Description                                                                                  |
| ------------------ | ------- | -------------------------------------------------------------------------------------------- |
| id                 | string  | Brand unique identifier number.                                                              |
| name               | string  | Brand Name.                                                                                  |
| metaTagDescription | string  | Meta tag description of the brand. This information is used on SEO.                          |
| keywords           | array   | An array of strings with keywords of the Brand, that can be used on the search.              |
| siteTitle          | string  | Name that will be displayed in the site title.                                               |
| isActive           | boolean | The condition defines if the brand is active or inactive.                                    |
| slug               | string  | Reference of the product in the URL of the store.                                            |
| score              | integer | Brand’s score. The score of the brand is used to set the priority on the search result page. |
| createdAt          | string  | Date when the brand was created.                                                             |
| updatedAt          | string  | Last date when the brand was updated.                                                        |
| displayOnMenu      | boolean | The condition will display the brand on the store menu.                                      |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"1409\",\n    \"name\": \"Marca 27/04\",\n    \"metaTagDescription\": \"description\",\n    \"keywords\": [],\n    \"siteTitle\": \"description\",\n    \"isActive\": true,\n    \"slug\": \"slug/marca/marca27/04\",\n    \"score\": 123,\n    \"createdAt\": \"2021-05-17T15:20:36.077253+00:00\",\n    \"updatedAt\": \"2021-05-17T15:20:36.077253+00:00\",\n    \"displayOnMenu\": true\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute          | Type    | Description                                                                                  |
| ------------------ | ------- | -------------------------------------------------------------------------------------------- |
| id                 | string  | Brand unique identifier number.                                                              |
| name               | string  | Brand Name.                                                                                  |
| metaTagDescription | string  | Meta tag description of the brand. This information is used on SEO.                          |
| keywords           | array   | An array of strings with keywords of the Brand, that can be used on the search.              |
| siteTitle          | string  | Name that will be displayed in the site title.                                               |
| isActive           | boolean | The condition defines if the brand is active or inactive.                                    |
| slug               | string  | Reference of the product in the URL of the store.                                            |
| score              | integer | Brand’s score. The score of the brand is used to set the priority on the search result page. |
| createdAt          | string  | Date when the brand was created.                                                             |
| updatedAt          | string  | Last date when the brand was updated.                                                        |
| displayOnMenu      | boolean | The condition will display the brand on the store menu.                                      |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"1409\",\n    \"name\": \"Marca 27/04\",\n    \"metaTagDescription\": \"description\",\n    \"keywords\": [],\n    \"siteTitle\": \"description\",\n    \"isActive\": true,\n    \"slug\": \"slug/marca/marca27/04\",\n    \"score\": 123,\n    \"createdAt\": \"2021-05-17T15:20:36.077253+00:00\",\n    \"updatedAt\": \"2021-05-17T15:20:36.077253+00:00\",\n    \"displayOnMenu\": true\n}",
      "language": "json"
    }
  ]
}
[/block]