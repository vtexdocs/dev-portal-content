---
title: "Create SKU Service Type"
slug: "catalog-api-post-sku-service-type"
excerpt: "Creates a new SKU Service Type. \r\n## Request body example\r\n\r\n```json\r\n{\r\n    \"Name\": \"Test API Sku Services\",\r\n    \"IsActive\": true,\r\n    \"ShowOnProductFront\": true,\r\n    \"ShowOnCartFront\": true,\r\n    \"ShowOnAttachmentFront\": true,\r\n    \"ShowOnFileUpload\": true,\r\n    \"IsGiftCard\": true,\r\n    \"IsRequired\": true\r\n}\r\n```\r\n\r\n## Response body example\r\n\r\n```json\r\n{\r\n    \"Id\": 2,\r\n    \"Name\": \"Teste API Sku Services\",\r\n    \"IsActive\": true,\r\n    \"ShowOnProductFront\": true,\r\n    \"ShowOnCartFront\": true,\r\n    \"ShowOnAttachmentFront\": true,\r\n    \"ShowOnFileUpload\": true,\r\n    \"IsGiftCard\": true,\r\n    \"IsRequired\": true\r\n}\r\n```"
hidden: false
createdAt: "2020-06-08T19:47:12.384Z"
updatedAt: "2022-07-15T19:54:39.063Z"
---
## Request body has the following properties:
| Attribute             | Type    | Description                                                         |
| --------------------- | ------- | ------------------------------------------------------------------- |
| Name                  | string  | SKU Service Type Name                                               |
| IsActive              | boolean | If the SKU Service Type is active or not                            |
| ShowOnProductFront    | boolean | Deprecated                                                          |
| ShowOnCartFront       | boolean | If the SKU Service Type is displayed  on the cart screen            |
| ShowOnAttachmentFront | boolean | If the SKU Service Type has an attachment                           |
| ShowOnFileUpload      | boolean | If the SKU Service Type can be associated with an attachment or not |
| IsGiftCard            | boolean | If the SKU Service Type is displayed as a Gift Card                 |
| IsRequired            | boolean | If the SKU Service type mandatory                                   |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Name\": \"Teste API Sku Services\",\n    \"IsActive\": true,\n    \"ShowOnProductFront\": true,\n    \"ShowOnCartFront\": true,\n    \"ShowOnAttachmentFront\": true,\n    \"ShowOnFileUpload\": true,\n    \"IsGiftCard\": true,\n    \"IsRequired\": true\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute             | Type    | Description                                                         |
| --------------------- | ------- | ------------------------------------------------------------------- |
| Id                    | integer | SKU Service Type ID                                                 |
| Name                  | string  | SKU Service Type Name                                               |
| IsActive              | boolean | If the SKU Service Type is active or not                            |
| ShowOnProductFront    | boolean | Deprecated                                                          |
| ShowOnCartFront       | boolean | If the SKU Service Type is displayed  on the cart screen            |
| ShowOnAttachmentFront | boolean | If the SKU Service Type has an attachment                           |
| ShowOnFileUpload      | boolean | If the SKU Service Type can be associated with an attachment or not |
| IsGiftCard            | boolean | If the SKU Service Type is displayed as a Gift Card                 |
| IsRequired            | boolean | If the SKU Service type mandatory                                   |

## Response body example:


[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 2,\n    \"Name\": \"Teste API Sku Services\",\n    \"IsActive\": true,\n    \"ShowOnProductFront\": true,\n    \"ShowOnCartFront\": true,\n    \"ShowOnAttachmentFront\": true,\n    \"ShowOnFileUpload\": true,\n    \"IsGiftCard\": true,\n    \"IsRequired\": true\n}",
      "language": "json"
    }
  ]
}
[/block]