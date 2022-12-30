---
title: "Update rules for a price table"
slug: "put_pipeline-catalog-pricetableid"
excerpt: "This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request.\r\n\r\n## Request body example\r\n\r\n```json\r\n{\r\n    \"rules\": [\r\n          {\r\n               \"id\": 1,\r\n               \"context\": {\r\n                    \"categories\": {\r\n                         \"Category ID\": \"1\",\r\n                         \"Category Name\": \"Alimentação\"\r\n                    },\r\n                    \"brands\": {\r\n                         \"Brand ID\": \"2000002\",\r\n                         \"Brand Name\": \"Whiskas\"\r\n                    },\r\n                    \"markupRange\": {\r\n                         \"from\": 0,\r\n                         \"to\": 200\r\n                    },\r\n                    \"dateRange\": {\r\n                         \"from\": \"2022-01-23T19:00:00.000Z\",\r\n                         \"to\": \"2023-10-26T00:00:00.000Z\"\r\n                    }\r\n               },\r\n               \"percentualModifier\": 0\r\n          }\r\n    ]\r\n}\r\n```"
hidden: false
createdAt: "2020-03-02T07:47:33.056Z"
updatedAt: "2022-06-14T19:50:14.919Z"
---
