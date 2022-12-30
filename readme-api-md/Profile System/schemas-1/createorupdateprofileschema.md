---
title: "Create or update profile schema"
slug: "createorupdateprofileschema"
excerpt: "Creates or updates profile schema.\n\r\n\r> Each account has one profile schema. Updating it with this request will substitute the previous version.\n\r\n\r> Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints."
hidden: true
createdAt: "2022-02-24T18:18:32.602Z"
updatedAt: "2022-11-04T18:42:05.388Z"
---
[block:callout]
{
  "type": "info",
  "body": "Learn more about [JSON schemas](https://json-schema.org)."
}
[/block]

##### EXAMPLE REQUEST BODY

```json
{
    "title": "Profile System Client Schema",
    "type": "object",
    "description": "The schema that describes a b2c profile",
    "required": [
        "firstName",
        "lastName",
        "email",
        "document",
        "documentType"
    ],
    "properties": {
        "firstName": {
            "type": "string",
            "sensitive": true,
            "pii": true
        },
        "lastName": {
            "type": "string",
            "sensitive": true,
            "pii": true
        },
        "email": {
            "type": "array",
            "items": {
                "type": "string"
            }
            "sensitive": true,
            "pii": true
        },
        "document": {
            "type": "string",
            "sensitive": true,
            "pii": true
        },
        "documentType": {
            "type": "string",
            "sensitive": false,
            "pii": false
        },
        "phone": {
            "type": "string",
            "sensitive": true,
            "pii": true
        },
        "gender": {
            "type": "string",
            "sensitive": true,
            "pii": false
        },
        "birthdate": {
            "type": "string",
            "sensitive": true,
            "pii": true
        }
    },
    "documentTTL": 1825,
    "version": 1,
    "v-indexed": [
        "email",
        "document"
    ],
    "v-unique": [
        "email",
        "document"
    ]
}
```