---
title: "Create attachment"
slug: "catalog-api-post-attachment"
excerpt: "Creates a new SKU attachment.\r\n >⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation. \r\n## Request body example\r\n\r\n```json\r\n{\r\n  \"Name\": \"Test\",\r\n  \"IsRequired\": true,\r\n  \"IsActive\": true,\r\n  \"Domains\": [\r\n    {\r\n      \"FieldName\": \"Basic test\",\r\n      \"MaxCaracters\": \"\",\r\n      \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"\r\n    },\r\n    {\r\n      \"FieldName\": \"teste\",\r\n      \"MaxCaracters\": \"\",\r\n      \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"\r\n    }\r\n  ]\r\n}\r\n```\r\n## Response body example\r\n\r\n```json\r\n{\r\n  \"Id\": 8,\r\n  \"Name\": \"Test\",\r\n  \"IsRequired\": true,\r\n  \"IsActive\": true,\r\n  \"Domains\": [\r\n    {\r\n      \"FieldName\": \"Basic test\",\r\n      \"MaxCaracters\": \"\",\r\n      \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"\r\n    },\r\n    {\r\n      \"FieldName\": \"teste\",\r\n      \"MaxCaracters\": \"\",\r\n      \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"\r\n    }\r\n  ]\r\n}\r\n```"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-09-28T20:23:38.263Z"
---
