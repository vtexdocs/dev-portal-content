---
title: "Working with JSON Schemas in Master Data v2"
slug: "working-with-json-schemas-in-master-data-v2"
hidden: false
excerpt: "Learn more about how to set up your JSON schemas"
createdAt: "2022-07-05T19:36:42.104Z"
updatedAt: "2022-08-03T13:10:23.602Z"
---

A JSON Schema defines how your data will be validated. Further information can be found in [External documentation on JSON Schemas](https://json-schema.org/), this article on [Understanding JSON Schema](https://json-schema.org/understanding-json-schema), and our article about the [Master Data schema lifecycle](https://developers.vtex.com/docs/guides/master-data-schema-lifecycle).

Use the following API requests to manage your Master Data schemas:

- [Get schemas](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/schemas)
- [Get schemas by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/schemas/-schemaName-)
- [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-)

Below you can learn more about how to set up your JSON schemas, and some Master Data features you can use with them.

## Configuring a JSON Schema

A JSON Schema is composed of three main fields:

- Properties: fields with their respective types.
- Required: mandatory fields.
- Title: Schema name.

Example:

```json
{
  "title": "Basic information of SKU",
  "properties": {
    "name": { "type": "string" }
  },
  "required": ["name"]
}
```

The schema above defines the basic format of an SKU. In this case, only the `name` property. We also define this field as mandatory by adding the field name into the required array.

This JSON Schema validates the following JSON:

```json
{
  "name": "T-shirt"
}
```

You can add these examples to [JSON Schema Validator](http://www.jsonschemavalidator.net/). If you change the JSON example in the validator to an integer, you will receive an error message, like in the example below.

- Changing the name to an integer:

  ```json
  {
    "name": 1
  }
  ```

- Error message:

  ```sh
  Invalid type. Expected String but got Integer.
  ```

The JSON Schema validates only the fields configured in properties. The exceeding fields will be maintained without validation. To preserve only the fields configured in the JSON schema, see the `additionalProperties` property information in [external documentation about JSON schema](https://json-schema.org/understanding-json-schema/reference/object.html#properties).

> ⚠️ Master Data v2 data entities can have up to 60 schemas per entity.

## Indexing fields

Use the property `v-indexed` to set up indexed fields. You must add the field to the properties to generate the indexer configuration with the right type.

```json
{
  "properties": {
    "field1": { "type": "string" },
    "field2": { "type": "integer" }
  },
  "v-indexed": ["field1", "field2"]
}
```

## Default fields

Use the property `v-default-fields` to configure which fields will return without indication in the `fields` query string.

```json
{
  "v-default-fields": ["field1", "field2"]
}
```

## Inheritance of schemas

Use the property `v-canonicalto` to set up another JSON Schema in the same data entity to inheritance.

```json
{
  "v-canonicalto": "https://{host}/api/dataentities/{data-entity-name}/schemas/{my-base-schema}"
}
```

## Enabling public fields

Use the property `v-security` to set up which fields are public (request without user authentication).

```json
{
  "v-security": {
    "allowGetAll": false,
    "publicRead": ["field1"],
    "publicWrite": ["field1"],
    "publicFilter": ["field1"]
  }
}
```

## Disabling default caching

Use the property `v-cache` to disable default caching.

```json
{
  "v-cache": false
}
```

## Creating triggers

Use the property `v-triggers` to set up automatic actions that will be performed by the platform if the creation or update of a document meets certain criteria defined by you. Learn more in [Setting up triggers in Master Data v2](https://developers.vtex.com/docs/guides/setting-up-triggers-in-master-data-v2).
