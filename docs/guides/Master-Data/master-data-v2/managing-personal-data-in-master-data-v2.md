---
title: "Managing personal data in Master Data v2"
slug: "managing-personal-data-in-master-data-v2"
hidden: false
createdAt: "2026-05-15T00:00:00.000Z"
updatedAt: "2026-05-15T00:00:00.000Z"
excerpt: "Learn how to configure, store, and retrieve personal data in Master Data v2 with encryption, masking, and data subject compliance."
---

Master Data v2 allows you to declare which fields in a data entity contain personal data. Once configured, these fields are encrypted, stored with data residency controls, and automatically participate in data subject request flows (e.g., right to be forgotten). On read operations, personal data fields are returned masked by default, and you must explicitly request unmasked access.

This guide walks through the full integration flow: configuring personal data fields, writing and reading documents, and searching.

> ℹ️ This feature is only available for Master Data v2 entities. Master Data v1 entities (e.g., CL, AD) are not supported.

## Before you begin

You must have an existing Master Data v2 data entity. If you need to create one, use the [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-) endpoint.

Personal data configuration is set at the data entity level, not within individual schemas. This avoids conflicts when multiple schemas coexist for the same entity.

Every document containing personal data must be linked to a data subject, the individual who owns the data. You define this association by mapping a field (e.g., `email`) as the data subject identifier (`SubjectIdField`).

## Configure personal data fields

Use the [Configure personal data fields](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/personalData) endpoint to declare which fields contain personal data and which field identifies the data subject.

```bash
PUT https://{accountName}.{environment}.com.br/api/dataentities/{dataEntityName}/personalData
```

> ℹ️ To inspect the current personal data configuration for an entity before changing it, use the [Get personal data configuration](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/personalData) endpoint. Inspecting first is recommended because saving a new configuration locks the endpoint for up to 12 hours (see [What happens after configuration](#what-happens-after-configuration)).

### Request body example

```json
{
  "Fields": ["email", "firstName", "document"],
  "SubjectIdField": "email"
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Fields` | array of strings | Yes | Names of fields that contain personal data. |
| `SubjectIdField` | string | Yes | Name of the field whose value identifies the data subject (owner of the personal data). |

### What happens after configuration

Saving a new configuration triggers a background process that re-tokenizes all existing documents in the entity. While this process runs, the [Configure personal data fields](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/personalData) endpoint is locked for the affected entity for up to 12 hours and returns `423 Locked` to prevent concurrent reprocessing jobs.

## Save documents

Use the standard document creation and update endpoints to save documents with personal data:

- [Create new document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#post-/api/dataentities/-dataEntityName-/documents)
- [Create document with custom ID or update entire document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/documents/-id-)
- [Update partial document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#patch-/api/dataentities/-dataEntityName-/documents/-id-)

```bash
POST https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/documents
```

```json
{
  "email": "john@example.com",
  "firstName": "John",
  "categories": ["promotions", "new_collections"]
}
```

Master Data automatically checks the personal data configuration for the entity. The values of personal data fields (`email` and `firstName` in this example) are stored separately with encryption and special data residency, while non-personal fields (`categories`) are stored normally.

> ⚠️ Every document saved in an entity with personal data configuration must contain the field declared in `SubjectIdField`.

## Read documents (masked by default)

Use the standard document retrieval endpoints to read documents:

- [Get document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/documents/-id-)
- [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search)
- [Scroll documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll)

By default, personal data fields are returned with masked values:

```bash
GET https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/documents/{id}?_fields=email,firstName,categories
```

```json
{
  "email": "j***@****.com",
  "firstName": "J***",
  "categories": ["promotions", "new_collections"]
}
```

Personal data fields are returned with characters replaced by asterisks. Non-personal fields are returned normally. The exact mask pattern shown above is illustrative and may vary by field type.

## Read documents with unmasked personal data

To retrieve the original values of personal data fields, add `_unmasked=true` to the query string:

```bash
GET https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/documents/{id}?_fields=email,firstName,categories&_unmasked=true
```

```json
{
  "email": "john@example.com",
  "firstName": "John",
  "categories": ["promotions", "new_collections"]
}
```

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `_unmasked` | boolean | No | When set to `true`, fields configured as personal data are returned with their original values instead of masked. Only takes effect if the data entity has personal data configured. Otherwise, it is ignored. Default: `false`. |

The `_unmasked` parameter also applies to [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search) and [Scroll documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll).

## Search by personal data fields

Personal data fields can be used as search filters, with two requirements. Like any other searchable field, they must be added to the schema's `v-indexed` array. Unlike other fields, they only support exact matching.

### Index the field

Add the personal data field to the `v-indexed` array in the schema, the same way you would index any other searchable field:

```bash
PUT https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/schemas/schema1
```

```json
{
  "properties": {
    "email": { "type": "string" },
    "firstName": { "type": "string" },
    "categories": { "type": "array" }
  },
  "v-indexed": ["email"]
}
```

### Search with exact match

```bash
GET https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/search?email=john@example.com&_fields=email,categories
```

The response follows the same masking rules. Personal data fields are masked by default. To retrieve them in clear text, add `_unmasked=true`.

> ⚠️ Only exact match filters are supported for personal data fields. Range filters, partial matches, and full-text search on these fields are not supported.

## Considerations

Keep the following considerations in mind when working with personal data in Master Data v2:

- **Master Data v1:** Not supported. Only v2 entities are compatible.
- **Search operators:** Personal data fields only support exact match. Range, contains, and full-text operators are not available.
- **All-or-nothing unmasking:** You cannot unmask individual fields. The `_unmasked` parameter applies to all personal data fields in the document.
- **Data subject ID required:** Every document in an entity with personal data must include the field configured in `SubjectIdField`.
