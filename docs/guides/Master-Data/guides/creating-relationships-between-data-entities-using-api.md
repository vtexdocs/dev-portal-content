---
title: "Creating relationships between data entities using API"
slug: "creating-relationships-between-data-entities-using-api"
hidden: false
createdAt: "2022-07-05T15:15:24.161Z"
updatedAt: "2022-07-05T15:23:31.068Z"
---
This document shows how to create a relationship between data entities in Master Data v2.

It is important to know the structure of the JSON Schema. If you don't know what that is, please check out the external documentation [Understanding JSON Schema](https://spacetelescope.github.io/understanding-json-schema). To learn more about schemas in Master Data v2, see [Schema lifecycle](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

When [setting up a JSON Schema](https://developers.vtex.com/vtex-rest-api/reference/saveschemabyname), you may configure a field to link to another data entity using the ID or a field to which there is some associated index.

Example of link through ID:
```
{
	"properties": {
		"clientEmail": { "type": "string" },
		"address": {
			"type": "string",
			"link": "https://vtexaccount.vtexcommercestable.com.br/api/dataentities/address/schemas/address-schema-v1"
		}
	}
}
```

Example of link through a field with an index:
```
{
	"properties": {
		"clientEmail": { "type": "string" },
		"addressName": {
			"type": "string",
			"link": "https://vtexaccount.vtexcommercestable.com.br/api/dataentities/address/schemas/address-schema-v1",
			"linked_field": "addressName"
		}
	}
}
```

As you may have noticed, in the `link` property we associate a JSON Schema of the data entity with which we want to create a relationship.

This will create in the response a new field with the JSON of the related document. If the document doesn't exist with that key, the property will be filled with `null`. 

The fields of the returned object will be same that are specified in the `v-default-fields`.

Example of a [Get document request](https://developers.vtex.com/vtex-rest-api/reference/getdocument) without schema:

PATH: `/api/dataentities/client/documents/{id}`
```
{
	"clientEmail": "vtext@mail.com",
	"address": "1"
}
```

Example of a [Get document request](https://developers.vtex.com/vtex-rest-api/reference/getdocument) using schema with link:

PATH: `/api/dataentities/client/documents/{id}`
```
{
	"clientEmail": "vtext@mail.com",
	"address": "1"
	"address_linked": {
		"id": "1"
		"city": "Rio de Janeiro"
	}
}
```