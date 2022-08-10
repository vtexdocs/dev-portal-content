---
title: "Get List of Brands"
slug: "listbrand"
excerpt: "The endpoint retrieves general information about all brands of the store."
hidden: true
createdAt: "2021-07-05T14:05:36.174Z"
updatedAt: "2021-07-05T15:02:27.560Z"
---
## Query params

| Param   | Type    | Description                                                                                                                                                                              |
| ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from    | integer | The first page of the interval of the brand list.                                                                                                                                        |
| to      | integer | The last page of the interval of the brand list.                                                                                                                                         |
| orderBy | string  | The order that the list is displayed. You can select `name`, or `updated_at` to select the order criteria. Then you can add `,` , `asc` or `desc` to define the brands order. |
| q       | string  | Search word.                                                                                                                                                                             |

## Response body has the following properties:

| Attribute       | Type             | Description                                                                                                                                                                              |
| --------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data            | array of objects | List with information about the store’s brands.                                                                                                                                          |
| ↳id             | string           | Brand unique identifier number.                                                                                                                                                          |
| ↳name           | string           | Brand Name.                                                                                                                                                                              |
| ↳isActive       | boolean          | The condition defines if the brand is active or inactive.                                                                                                                                |
| ↳score          | integer          | Brand’s score. The score of the brand is used to set the priority on the search result page.                                                                                             |
| ↳ createdAt     | string           | Date when the brand was created.                                                                                                                                                         |
| ↳ updatedAt     | string           | Last date when the brand was updated.                                                                                                                                                    |
| ↳ displayOnMenu | boolean          | The condition will display the brand on the store menu.                                                                                                                                  |
| \_metadata      | object           | Information about the organization and exhibition of the brand list.                                                                                                                     |
| ↳ total         | integer          | Total of brands on the list.                                                                                                                                                             |
| ↳ from          | integer          | The first page of the interval of the brand list.                                                                                                                                        |
| ↳ to            | integer          | The last page of the interval of the brand list.                                                                                                                                         |
| ↳ orderBy       | string           | The order that the list is displayed. You can select `name`, or `updated_at` to select the order criteria. Then you can add `,` , `asc` or `desc` to define the brands order. |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"data\": [\n        {\n            \"id\": \"863\",\n            \"name\": \"Zwilling\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:41:45.696488+00:00\",\n            \"updatedAt\": \"2021-01-18T14:41:45.696488+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"1298\",\n            \"name\": \"Zooz Pets\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:45:32.900176+00:00\",\n            \"updatedAt\": \"2021-01-18T14:45:32.900176+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"110\",\n            \"name\": \"Zootekna\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:32:34.900283+00:00\",\n            \"updatedAt\": \"2021-01-18T14:32:34.900283+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"494\",\n            \"name\": \"Zoo Med\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:34:20.219922+00:00\",\n            \"updatedAt\": \"2021-01-18T14:34:20.219922+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"429\",\n            \"name\": \"Zoomed\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:33:52.056893+00:00\",\n            \"updatedAt\": \"2021-01-18T14:33:52.056893+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"360\",\n            \"name\": \"ZooFood\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:33:23.404791+00:00\",\n            \"updatedAt\": \"2021-01-18T14:33:23.404791+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"1046\",\n            \"name\": \"Zona Criativa\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:43:12.201395+00:00\",\n            \"updatedAt\": \"2021-01-18T14:43:12.201395+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"274\",\n            \"name\": \"Zoetis\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:32:57.161795+00:00\",\n            \"updatedAt\": \"2021-01-18T14:32:57.161795+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"989\",\n            \"name\": \"Zoe Pet\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:42:36.241914+00:00\",\n            \"updatedAt\": \"2021-01-18T14:42:36.241914+00:00\",\n            \"displayOnMenu\": false\n        },\n        {\n            \"id\": \"113\",\n            \"name\": \"Zip Clean\",\n            \"isActive\": false,\n            \"score\": 0,\n            \"createdAt\": \"2021-01-18T14:32:35.598339+00:00\",\n            \"updatedAt\": \"2021-01-18T14:32:35.598339+00:00\",\n            \"displayOnMenu\": false\n        }\n    ],\n    \"_metadata\": {\n        \"total\": 1399,\n        \"from\": 1,\n        \"to\": 10,\n        \"orderBy\": \"name,desc\"\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]