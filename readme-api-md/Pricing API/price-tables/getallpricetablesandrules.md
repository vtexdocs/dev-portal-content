---
title: "Get all price tables and their rules"
slug: "getallpricetablesandrules"
excerpt: "This method will retrieve all price tables and their rules.\r\n\r\n## Response body example\r\n\r\n```json\r\n[\r\n    {\r\n        \"tradePolicyId\": \"2\",\r\n        \"rules\": [\r\n            {\r\n                \"id\": 0,\r\n                \"context\": {\r\n                    \"categories\": {},\r\n                    \"brands\": {},\r\n                    \"stockStatuses\": null,\r\n                    \"internalCategories\": null,\r\n                    \"markupRange\": null,\r\n                    \"dateRange\": null\r\n                },\r\n                \"percentualModifier\": 20\r\n            }\r\n        ]\r\n    },\r\n    {\r\n        \"tradePolicyId\": \"b2c\",\r\n        \"rules\": [\r\n            {\r\n                \"id\": 0,\r\n                \"context\": {\r\n                    \"categories\": {},\r\n                    \"brands\": {\r\n                        \"2000009\": \"Whiskas\"\r\n                    },\r\n                    \"stockStatuses\": null,\r\n                    \"internalCategories\": null,\r\n                    \"markupRange\": null,\r\n                    \"dateRange\": null\r\n                },\r\n                \"percentualModifier\": 15\r\n            }\r\n        ]\r\n    }\r\n]\r\n```"
hidden: false
createdAt: "2022-06-14T19:00:49.582Z"
updatedAt: "2022-06-14T19:00:49.582Z"
---
