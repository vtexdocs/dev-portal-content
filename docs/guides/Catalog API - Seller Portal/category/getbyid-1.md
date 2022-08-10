---
title: "Get Category by ID"
slug: "getbyid-1"
excerpt: "The endpoint retrieves general information about a category by its ID."
hidden: true
createdAt: "2021-07-05T14:05:36.182Z"
updatedAt: "2021-07-05T15:17:53.355Z"
---
## Response body has the following properties:

| Attribute       | Type             | Description                                                                                                          |
| --------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| value           | object           | Object with values of a category.                                                                                    |
| ↳id             | string           | Category unique identifier number.                                                                                   |
| ↳name           | string           | Category Name.                                                                                                       |
| ↳isActive       | boolean          | The condition defines if the category is active or inactive.                                                         |
| ↳displayOnMenu  | boolean          | The condition will display the category on the store menu.                                                           |
| ↳score          | integer          | Category’s score. The score of the category is used to set the priority on the search result page.                   |
| ↳filterByBrand  | boolean          | The condition defines if the category can be filtered by brand.                                                      |
| ↳isClickable    | boolean          | The condition defines if the category is clickable or not in the store.                                              |
| children        | array of objects | List of all children categories of the parent category.                                                              |
| ↳value          | object           | Object with values of a children category.                                                                           |
| ↳↳id            | string           | Children category unique identifier number.                                                                          |
| ↳↳name          | string           | Children category Name.                                                                                              |
| ↳↳isActive      | boolean          | The condition defines if the children category is active or inactive.                                                |
| ↳↳displayOnMenu | boolean          | The condition will display the children category on the store menu.                                                  |
| ↳↳score         | integer          | Children category’s score. The score of the children category is used to set the priority on the search result page. |
| ↳↳filterByBrand | boolean          | The condition defines if the children category can be filtered by brand.                                             |
| ↳↳isClickable   | boolean          | The condition defines if the category is clickable or not in the store.                                              |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n\n    \"value\": {\n        \"id\": \"1\",\n        \"name\": \"sandboxintegracao\",\n        \"isActive\": false,\n        \"displayOnMenu\": false,\n        \"score\": 0,\n        \"filterByBrand\": false,\n        \"isClickable\": false\n    },\n    \"children\": [\n        {\n            \"value\": {\n                \"id\": \"2\",\n                \"name\": \"Perfumes\",\n                \"isActive\": false,\n                \"displayOnMenu\": false,\n                \"score\": 0,\n                \"filterByBrand\": false,\n                \"isClickable\": false\n            }\n        }\n    ]\n}",
      "language": "json"
    }
  ]
}
[/block]