---
title: "Working with schemas in the Profile System"
slug: "working-with-schemas-in-the-profile-system"
hidden: false
createdAt: "2022-02-22T22:28:50.366Z"
updatedAt: "2022-08-19T18:42:00.613Z"
seeAlso:
 - "/docs/guides/profile-system"
 - "/docs/guides/data-protection-plus"
---

>⚠️ [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus) is in closed beta phase, only available in select regions.<br /><br />
> This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh). If you are already a VTEX customer and want to adopt VTEX Shield for your business, please contact [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ). Additional fees may apply. If you are not yet a customer but are interested in this solution, please complete our [contact form](https://vtex.com/us-en/contact/).

A JSON Schema defines the structure of data stored in the [Profile System](https://developers.vtex.com/docs/guides/profile-system). It determines, for example, which fields a profile has and their respective formats. To learn more about JSON Schemas, read the [JSON Schema external documentation](http://json-schema.org/).

The following endpoints in the [Profile System API](https://developers.vtex.com/docs/guides/profile-system) allow you to interact with the profile schema:

| Endpoint name | Description |
| - | - |
| `GET` [Get full schema](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/schemas/profileSystem) | Retrieves the full profile schema, including default and custom fields. |
| `GET` [Get custom fields](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/schemas/profileSystem/custom) | Retrieves custom fields in the profile schema. |
| `PUT` [Create or delete custom fields](https://developers.vtex.com/docs/api-reference/profile-system#put-/api/storage/profile-system/schemas/profileSystem/custom) | Allows you to customize fields. Learn more about possible customizations in [Customizing the profile schema](#customizing-the-profile-schema). |

## Customizing the profile schema

Using the `PUT` [Create or delete custom fields](https://developers.vtex.com/docs/api-reference/profile-system#put-/api/storage/profile-system/schemas/profileSystem/custom) endpoint allows you to customize the schema for the profile entity in the Profile System by:

- [Adding custom fields](#adding-custom-fields)
- [Defining PII and sensitive custom fields](#defining-pii-and-sensitive-custom-fields)
- [Configuring TTL](#configuring-ttl)
- [Deleting custom fields](#deleting-custom-fields)
- [Restrictions](#restrictions)

>⚠ Make sure you check the applicable [Restrictions](#restrictions).

### Adding custom fields

Extend the profile schema with custom fields by making a request to `PUT` [Create or delete custom fields](https://developers.vtex.com/docs/api-reference/profile-system#put-/api/storage/profile-system/schemas/profileSystem/custom), with a request body structured as in the following example.

**Request body example**

```json
{
    "customField1": {
        "type": ["string", "null"],
        "sensitive": true,
        "pii": true
    },
    "customField2": {
        "type": ["string", "null"],
        "sensitive": false,
        "pii": false
    }
}
```

> ⚠️ Every time you add new custom properties or edit existing ones, you must pass all custom properties in the request body, or they will be replaced by those present in the most recent request body used. For example, to edit `customField2` later on, you need to include `customField1` in the request body even if it has not changed.

### Defining PII and sensitive custom fields

Properties marked as Personally Identifiable Information (PII) or sensitive are the ones that are masked by default and must be audited when accessed by a user for legal reasons.

Set the `sensitive` and/or `pii` properties as `true` inside the JSON Schema property definition to determine that they must follow this behavior, as exemplified below.

**Request body example - PII and sensitive field**

```json
{
    "document": {
        "type": "string",
        "sensitive": true,
        "pii": true
    }
}

```

### Configuring TTL

The TTL (Time To Live) property is a value expressed in days used to schedule the deletion of the document in the future. When this time expires, the document is automatically deleted.

**Example**

```json
"documentTTL": 1825,
```

### Deleting custom fields

If you want to delete all custom fields, make a request to `PUT` [Create or delete custom fields](https://developers.vtex.com/docs/api-reference/profile-system#put-/api/storage/profile-system/schemas/profileSystem/custom) with an empty JSON as the request body.

To delete only one or more fields, but not all, make this request including every custom field in the request body except the ones to be removed.

### Restrictions

The following restrictions apply when working with custom fields in the profile schema:

- You cannot use `oneOf`, `anyOf`, `allOf,` or `not` [keywords](https://swagger.io/docs/specification/data-models/oneof-anyof-allof-not/).
- The schema is valid per account.
- You cannot remove or edit required fields. Custom fields cannot be mandatory, so the existing documents will still be compatible with the new schema.
- Default fields cannot be changed.
- Custom fields cannot be in `v-indexed` or in `v-unique`.
