---
title: "Update attachment"
slug: "catalog-api-put-attachment"
excerpt: "Updates a previously existing SKU attachment with new information"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-17T19:41:37.776Z"
---
## Request body has the following properties:

| Attribute          | Type             | Description                        |
| ------------------ | ---------------- | ---------------------------------- |
| Name               | string           | Attachment Name                    |
| IsRequired         | boolean          | If it is required or not           |
| IsActive           | boolean          | If the attachment is active or not |
| Domains            | array of objects | Attachment list of characteristics |
| FieldName          | string           | Attachment key Name                |
| MaxCaracters | string           | Key max number of characters       |
| DomainValues | string           | Allowed key values                 |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"Name\": \"Test\",\n   \"IsRequired\": true,\n   \"IsActive\": true,\n   \"Domains\": [\n       {\n           \"FieldName\": \"Basic test\",\n           \"MaxCaracters\": \"\",\n           \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"\n       },\n       {\n           \"FieldName\": \"teste\",\n           \"MaxCaracters\": \"\",\n           \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"\n       }\n   ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute          | Type             | Description                        |
| ------------------ | ---------------- | ---------------------------------- |
| Id                 | integer          | Attachment ID                      |
| Name               | string           | Attachment Name                    |
| IsRequired         | boolean          | If it is required or not           |
| IsActive           | boolean          | If the attachment is active or not |
| Domains            | array of objects | Attachment list of characteristics |
| FieldName          | string           | Attachment key Name                |
| MaxCaracters | string           | Key max number of characters       |
| DomainValues | string           | Allowed key values                 |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n\t \"Id\": 8,\n   \"Name\": \"Test\",\n   \"IsRequired\": true,\n   \"IsActive\": true,\n   \"Domains\": [\n       {\n           \"FieldName\": \"Basic test\",\n           \"MaxCaracters\": \"\",\n           \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"\n       },\n       {\n           \"FieldName\": \"teste\",\n           \"MaxCaracters\": \"\",\n           \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"\n       }\n   ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]