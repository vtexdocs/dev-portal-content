---
title: "Create Category"
slug: "createcategory"
excerpt: ">📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX's discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://help.vtex.com/support). \r\n\r\n Creates a new category.\r\n\r\n## Request body example\r\n\r\n```json\r\n{\r\n  \"parentId\": \"567\",\r\n  \"Name\": \"Beauty\"\r\n}\r\n```\r\n\r\n## Response body example\r\n\r\n```json\r\n{\r\n  \"value\": {\r\n    \"id\": \"1\",\r\n    \"name\": \"Beauty\",\r\n    \"isActive\": false\r\n  },\r\n  \"children\": [\r\n    {\r\n      \"value\": {\r\n        \"id\": \"2\",\r\n        \"name\": \"Perfumes\",\r\n        \"isActive\": false\r\n      }\r\n    }\r\n  ]\r\n}\r\n```"
hidden: false
createdAt: "2021-07-05T14:05:36.183Z"
updatedAt: "2022-11-21T22:29:20.979Z"
---
