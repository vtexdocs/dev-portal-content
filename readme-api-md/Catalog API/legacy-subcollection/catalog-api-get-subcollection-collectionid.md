---
title: "Get Subcollection by Collection ID"
slug: "catalog-api-get-subcollection-collectionid"
excerpt: ">⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).\n\nRetrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.\r\n## Response body example\r\n\r\n```json\r\n[\r\n    {\r\n        \"Id\": 12,\r\n        \"CollectionId\": 149,\r\n        \"Name\": \"Subcollection\",\r\n        \"Type\": \"Inclusive\",\r\n        \"PreSale\": false,\r\n        \"Release\": true\r\n    },\r\n    {\r\n        \"Id\": 13,\r\n        \"CollectionId\": 149,\r\n        \"Name\": \"Test\",\r\n        \"Type\": \"Exclusive\",\r\n        \"PreSale\": true,\r\n        \"Release\": false\r\n    },\r\n    {\r\n        \"Id\": 14,\r\n        \"CollectionId\": 149,\r\n        \"Name\": \"asdfghj\",\r\n        \"Type\": \"Inclusive\",\r\n        \"PreSale\": false,\r\n        \"Release\": false\r\n    }\r\n]\r\n```"
hidden: false
createdAt: "2020-05-20T01:33:18.040Z"
updatedAt: "2022-07-28T17:44:00.232Z"
---
