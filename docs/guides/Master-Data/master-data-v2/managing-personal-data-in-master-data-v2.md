---
title: "Managing personal data in Master Data v2"
slug: "managing-personal-data-in-master-data-v2"
hidden: false
createdAt: "2026-05-15T00:00:00.000Z"
updatedAt: "2026-05-15T00:00:00.000Z"
excerpt: "Learn how to configure, store, and retrieve personal data in Master Data v2 with encryption, masking, and data subject compliance."
---

Master Data v2 allows you to declare which fields in a data entity contain personal data. Once configured, these fields are encrypted, stored with data residency controls, and automatically participate in data subject request flows (e.g., right to be forgotten). On read operations, personal data fields are returned **masked** by default, and you must explicitly request unmasked access.

This guide walks through the full integration flow: configuring personal data fields, writing and reading documents, and searching.

> ℹ️ This feature is only available for Master Data v2 entities. Master Data v1 entities (e.g., CL, AD) are not supported.

## Before you begin

You must have an existing Master Data v2 data entity. If you need to create one, use the [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-) endpoint.

Personal data configuration is set at the **data entity level**, not within individual schemas. This avoids conflicts when multiple schemas coexist for the same entity.

Every document containing personal data must be linked to a **data subject,** the individual who owns the data. You define this association by mapping a field (e.g., `email`) as the data subject identifier.

## Configure personal data fields

Use the [Configure personal data fields](https://developers.vtex.com/docs/api-reference/master-data-api-v2#post-/api/dataentities/-dataEntityName-/personalData) endpoint to declare which fields contain personal data and which field identifies the data subject.

```
POST https://{accountName}.{environment}.com.br/api/dataentities/{dataEntityName}/personalData
```

### Request body example

```json
{
  "fields": ["email", "firstName", "document"],
  "data_subject_field": "email"
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `fields` | array of strings | Yes | Names of fields that contain personal data. |
| `data_subject_field` | string | Yes | Name of the field whose value identifies the data subject (owner of the personal data). |

> ⚠️ The system does not validate whether the declared fields exist in the entity's existing schemas. This supports schema-less or multi-schema scenarios.

### What happens after configuration

When you configure fields as personal data, a background process tokenizes the values of those fields in all existing documents. If you later remove a field from the configuration, the process detokenizes (restores to clear text) the values in existing documents.

## Save documents

Use the standard document creation and update endpoints to save documents with personal data:

- [Create new document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#post-/api/dataentities/-dataEntityName-/documents)
- [Create document with custom ID or update entire document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/documents/-id-)
- [Update partial document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#patch-/api/dataentities/-dataEntityName-/documents/-id-)

```
POST https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/documents
```

```json
{
  "email": "john@example.com",
  "firstName": "John",
  "categories": ["promotions", "new_collections"]
}
```

Master Data automatically checks the personal data configuration for the entity. The values of personal data fields (`email` and `firstName` in this example) are tokenized and stored securely, while non-personal fields (`categories`) are stored normally.

> ⚠️ If the entity has personal data fields configured but the document does not contain the `data_subject_field`, the write operation fails with an error.

## Read documents (masked by default)

Use the standard document retrieval endpoints to read documents:

- [Get document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/documents/-id-)
- [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search)
- [Scroll documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll)

By default, personal data fields are returned with masked values:

```
GET https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/documents/{id}?_fields=email,firstName,categories
```

```json
{
  "email": "j***@*******.com",
  "firstName": "J***",
  "categories": ["promotions", "new_collections"]
}
```

Non-personal fields are returned normally. The masking format preserves the first character and replaces the rest with asterisks. Special characters (like `@` and `.`) are kept in place.

## Read documents with unmasked personal data

To retrieve the original values of personal data fields, add `unmasked=true` and a mandatory `reason` parameter to the query string:

```
GET https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/documents/{id}?_fields=email,firstName,categories&unmasked=true&reason=customer+support+request
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
| `unmasked` | boolean | No | Set to `true` to return personal data fields in clear text. Default: `false`. |
| `reason` | string | Yes (when `unmasked=true`) | Description of the purpose of access. Required for auditing compliance. |

> ⚠️ If `unmasked=true` is sent without a `reason`, the request fails. Access to unmasked data is audited.

The `unmasked` and `reason` parameters also apply to [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search) and [Scroll documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll).

## Search by personal data fields

Personal data fields can be used as search filters, but they must be indexed and only support exact matching.

### Index the field

Add the personal data field to the `v-indexed` array in the schema, like any other searchable field:

```
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

```
GET https://{accountName}.{environment}.com.br/api/dataentities/Newsletter/search?email=john@example.com&_fields=email,categories
```

The response follows the same masking rules: personal data fields are masked by default, and you can add `unmasked=true&reason=...` to retrieve them in clear text.

> ⚠️ Only **exact match** filters are supported for personal data fields. Range filters, partial matches, and full-text search on these fields return a `400 Bad Request` error.

## Considerations

Keep the following considerations in mind when working with personal data in Master Data v2:

- **Master Data v1:** Not supported. Only v2 entities are compatible.
- **Search operators:** Personal data fields only support exact match. Range, contains, and full-text operators are not available.
- **All-or-nothing unmasking:** You cannot unmask individual fields. The `unmasked` parameter applies to all personal data fields in the document.
- **Data subject required:** Every document in an entity with personal data must include the configured `data_subject_field`.
