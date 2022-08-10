---
title: "Get attachment"
slug: "catalog-api-get-attachment"
excerpt: "Gets information about a registered attachment."
hidden: false
createdAt: "2020-02-13T00:55:14.116Z"
updatedAt: "2022-05-20T22:23:43.977Z"
---
## Response body has the following properties::

| Attribute          | Type             | Description                        |
| ------------------ | ---------------- | ---------------------------------- |
| Id                 | integer          | Attachment ID                      |
| Name               | string           | Attachment Name                    |
| IsActive           | boolean          | If the attachment is active or not |
| IsRequired         | boolean          | If it is required or not           |
| Domains            | array of objects | Attachment list of characteristics |
| FieldName          | string           | Attachment key Name                |
| MaxCaracters | string           | Key max number of characters       |
| DomainValues | string           | Allowed key values                 |

## Response body has the following properties:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 1,\n    \"Name\": \"Name\",\n    \"IsRequired\": false,\n    \"IsActive\": true,\n    \"Domains\": []\n}",
      "language": "json"
    }
  ]
}
[/block]