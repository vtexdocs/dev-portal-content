---
title: "Create partial document"
slug: "createorupdatepartialdocument"
excerpt: "This request allows you to partially update a document corresponding to a given data entity.\r\n\r\n> You can use this request to create documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.\r\n\r\n## Example use cases\r\n\r\n### Client profile\r\n\r\nIn order to create a customer profile's `phone` and `isNewsletterOptIn` fields, choose the `CL` data entity and send a request similar to this:\r\n\r\nPATCH\r\n```\r\nhttps://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents\r\n```\r\n\r\nRequest body\r\n```json\r\n{\r\n    \"phone\": \"+12025550195\",\r\n    \"isNewsletterOptIn\": false\r\n }\r\n```\r\n\r\n### Client address\r\n\r\nIn order to update the `receiverName` of an existing address, the data entity is `AD` and the request would look like this:\r\n\r\nPATCH\r\n```\r\nhttps://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents\r\n```\r\n\r\nRequest body\r\n```json\r\n{\r\n    \"receiverName\": \"Lois Lane\"\r\n}\r\n```"
hidden: false
createdAt: "2019-12-16T06:09:28.493Z"
updatedAt: "2022-07-28T17:32:29.581Z"
---
