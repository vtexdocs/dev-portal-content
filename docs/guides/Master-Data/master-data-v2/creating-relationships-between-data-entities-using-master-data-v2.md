---
title: "Creating relationships between data entities using Master Data v2"
slug: "creating-relationships-between-data-entities-using-master-data-v2"
excerpt: "Learn how to create relationships between data entities in Master Data v2."
hidden: false
createdAt: "2022-07-05T15:15:24.161Z"
updatedAt: "2022-07-05T15:23:31.068Z"
---

This document will teach you how to establish relationships between data entities in **Master Data v2**. Creating these relationships is vital for organizing and structuring data efficiently within your system.

## Before you begin

Before delving into the process of creating relationships, it's essential to grasp the structure of JSON Schema. If you're not familiar with JSON Schema, we recommend referring to the external documentation, [Understanding JSON Schema](https://json-schema.org/understanding-json-schema).

To learn more about schemas in Master Data v2, see [Schema lifecycle](https://developers.vtex.com/docs/guides/master-data-schema-lifecycle).

## Establishing relationships

Use the [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-) ednpoint to configure a field to link to another data entity using either the ID or a field with an associated [index](https://developers.vtex.com/docs/guides/master-data-components#index) created using the [Create index](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/indices) endpoint.

Below are examples of both methods:

<details>
<summary>Link through ID</summary>

```json
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

</details>

<details>
<summary>Link through a field with an index</summary>

```json
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

</details>

Notice that the `link` property associates a JSON Schema of the data entity with which you want to create a relationship.

## Response handling

Creating a relationship in this manner will generate a response containing a new field with the JSON of the related document.

The fields in the returned object will match those specified in the `v-default-fields`. However, if the document does not exist with the specified key, the property will be populated with `null`.

<details>
<summary>Example of a [Get document request](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/documents/-id-) without schema</summary>

`GET` `/api/dataentities/client/documents/{id}?_fields={fields}`

```json
{
    "clientEmail": "vtext@mail.com",
    "address": "1"
}
```

</details>

<details>
<summary>Example of a [Get document request](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/documents/-id-) using a schema with a link</summary>

In this request, you must use the `_schema` and the `_fields` query parameters for the linked fields to return correctly.

`GET` `/api/dataentities/client/documents/{id}?_schema={schema}&_fields={fields}`

```json
{
    "clientEmail": "vtext@mail.com",
    "address": "1"
    "address_linked": {
        "id": "1"
        "city": "Rio de Janeiro"
    }
}
```

</details>
