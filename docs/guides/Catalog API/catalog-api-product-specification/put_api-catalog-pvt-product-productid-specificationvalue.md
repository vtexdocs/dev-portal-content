---
title: "Associate product specification using specification name and group name"
slug: "put_api-catalog-pvt-product-productid-specificationvalue"
excerpt: "Associates a specification to a product using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.\r\n\r\n ## Request body example\r\n\r\n```json\r\n{\r\n    \"FieldName\": \"Material\",\r\n    \"GroupName\": \"Additional Information\",\r\n    \"RootLevelSpecification\": false,\r\n    \"FieldValues\": [\r\n        \"Cotton\",\r\n       \"Polyester\"\r\n        ]\r\n}\r\n```\r\n \r\n \r\n## Response body example\r\n\r\n```json\r\n[\r\n    {\r\n        \"Id\": 53,\r\n        \"ProductId\": 3,\r\n        \"FieldId\": 21,\r\n        \"FieldValueId\": 60,\r\n        \"Text\": \"Cotton\"\r\n    },\r\n    {\r\n        \"Id\": 54,\r\n        \"ProductId\": 3,\r\n        \"FieldId\": 21,\r\n        \"FieldValueId\": 61,\r\n        \"Text\": \"Polyester\"\r\n    }\r\n]\r\n```"
hidden: false
createdAt: "2021-12-08T16:05:42.201Z"
updatedAt: "2022-05-27T19:16:22.344Z"
---
