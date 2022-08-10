---
title: "Associate SKU specification using specification name and group name"
slug: "put_api-catalog-pvt-stockkeepingunit-skuid-specificationvalue"
excerpt: "Associates a specification to an SKU using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.\r\n\r\n ## Request body example\r\n\r\n```json\r\n{\r\n    \"FieldName\": \"Size\",\r\n    \"GroupName\": \"Sizes\",\r\n    \"RootLevelSpecification\": false,\r\n    \"FieldValues\": [\r\n        \"M\"\r\n        ]\r\n}\r\n```\r\n \r\n \r\n## Response body example\r\n\r\n```json\r\n[\r\n    {\r\n        \"Id\": 419,\r\n        \"SkuId\": 5,\r\n        \"FieldId\": 22,\r\n        \"FieldValueId\": 62,\r\n        \"Text\": \"M\"\r\n    }\r\n]\r\n```"
hidden: false
createdAt: "2022-05-25T18:26:28.157Z"
updatedAt: "2022-05-27T19:16:25.409Z"
---
