---
title: "Create Subcollection"
slug: "catalog-api-post-subcollection"
excerpt: ">⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).\n\nCreates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).\r\n## Request body example\r\n\r\n```json\r\n{\r\n    \"CollectionId\": 149,\r\n    \"Name\": \"Test\",\r\n    \"Type\": \"Exclusive\",\r\n    \"PreSale\": true,\r\n    \"Release\": false\r\n}\r\n```\r\n## Response body example\r\n\r\n```json\r\n{\r\n    \"Id\": 13,\r\n    \"CollectionId\": 149,\r\n    \"Name\": \"Test\",\r\n    \"Type\": \"Exclusive\",\r\n    \"PreSale\": true,\r\n    \"Release\": false\r\n}\r\n```"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-07-28T17:44:00.560Z"
---
