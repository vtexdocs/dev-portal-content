---
title: "Get Brand by ID"
slug: "getbrand"
excerpt: "The endpoint retrieves general information about a brand by its ID."
hidden: true
createdAt: "2021-07-05T14:05:36.178Z"
updatedAt: "2021-07-05T15:04:47.175Z"
---
## Response body has the following properties:

| Attribute     | Type    | Description                                                                                  |
| ------------- | ------- | -------------------------------------------------------------------------------------------- |
| id            | string  | Brand unique identifier number.                                                              |
| name          | string  | Brand Name.                                                                                  |
| isActive      | boolean | The condition defines if the brand is active or inactive.                                    |
| score         | integer | Brand’s score. The score of the brand is used to set the priority on the search result page. |
| createdAt     | string  | Date when the brand was created.                                                             |
| updatedAt     | string  | Last date when the brand was updated.                                                        |
| displayOnMenu | boolean | The condition will display the brand on the store menu.                                      |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"1\",\n    \"name\": \"Givenchy\",\n    \"isActive\": false,\n    \"score\": 0,\n    \"createdAt\": \"2021-01-18T14:32:15.682643+00:00\",\n    \"updatedAt\": \"2021-01-18T14:32:15.682643+00:00\",\n    \"displayOnMenu\": false\n}",
      "language": "json"
    }
  ]
}
[/block]