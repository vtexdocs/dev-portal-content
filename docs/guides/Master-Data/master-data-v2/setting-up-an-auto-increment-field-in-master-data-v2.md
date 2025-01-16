---
title: "Setting up an auto increment field in Master Data v2"
slug: "setting-up-an-auto-increment-field-in-master-data-v2"
hidden: false
createdAt: "2022-09-27T20:49:42.874Z"
updatedAt: "2022-10-04T21:56:43.466Z"
---
**Auto increment** is a Master Data feature that automatically creates unique and sequential values to `integer` type fields when new documents are created.
[block:callout]
{
  "type": "info",
  "body": "The starting value of auto increment fields is always `1`. This value can not be changed."
}
[/block]

## Set up

Auto increment fields can be set up in data entities' [JSON schemas](/docs/guides/working-with-json-schemas-in-master-data-v2).

Create an `integer` field and add its name to the `v-auto-increment` property, like in the example below:

```
{
	"properties": {
		"valueAsAutoIncrement": {
			"type": "integer"
		}
	},
	"v-auto-increment": [
		"valueAsAutoIncrement"
	]
}
```
[block:callout]
{
  "type": "warning",
  "body": "- The auto-increment field cannot be `required`.\n- The field's type has to be `integer`.",
  "title": "Keep in mind that:"
}
[/block]
## Usage

When [saving new documents](https://developers.vtex.com/vtex-rest-api/reference/createnewdocument) you must identify the corresponding JSON Schema with the query parameter `_schema`. See an example of this:

```
POST
https://{accountName}.{environment}.com.br/api/dataentities/{dataEntityName}/documents?_schema={schemaName}
```