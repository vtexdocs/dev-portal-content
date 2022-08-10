---
title: "Create a Category"
slug: "createcategory"
excerpt: "The endpoint creates a new category."
hidden: true
createdAt: "2021-07-05T14:05:36.183Z"
updatedAt: "2021-07-05T15:20:29.327Z"
---
## Request body has the following properties:

| Attribute      | Type   | Description                               |
| -------------- | ------ | ----------------------------------------- |
| parentId | string | Parent category unique identifier number. |
| Name           | string | Category name.                            |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"parentId\": null,\n    \"Name\": \"sandboxintegracao\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute      | Type             | Description                                                                                        |
| -------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| value          | object           | Object with values of a category.                                                                  |
| ↳id            | string           | Category unique identifier number.                                                                 |
| ↳name          | string           | Category Name.                                                                                     |
| ↳isActive      | boolean          | The condition defines if the category is active or inactive.                                       |
| ↳displayOnMenu | boolean          | The condition will display the category on the store menu.                                         |
| ↳score         | integer          | Category’s score. The score of the category is used to set the priority on the search result page. |
| ↳filterByBrand | boolean          | The condition defines if the category can be filtered by brand.                                    |
| ↳isClickable   | boolean          | The condition defines if the category is clickable or not in the store.                            |
| children       | array of objects | List of all children categories of the parent category.                                            |

## ## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"value\": {\n        \"id\": \"1\",\n        \"name\": \"sandboxintegracao\",\n        \"isActive\": false,\n        \"displayOnMenu\": false,\n        \"score\": 0,\n        \"filterByBrand\": false,\n        \"isClickable\": false\n    },\n    \"children\": []\n}",
      "language": "json"
    }
  ]
}
[/block]