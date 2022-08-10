---
title: "Update SKU Service Type"
slug: "catalog-api-put-sku-service-type"
excerpt: "Updates an existing SKU Service Type"
hidden: false
createdAt: "2020-06-08T19:47:12.381Z"
updatedAt: "2020-06-19T16:38:22.906Z"
---
## Request body has the following properties:
| Attribute             | Type    | Description                                                         |
| --------------------- | ------- | ------------------------------------------------------------------- |
| Name                  | string  | SKU Service Type Name. Maximum of 100 characters                    |
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
      "code": "{\n    \"Name\": \"Mudando nome teste\",\n    \"IsActive\": false,\n    \"ShowOnProductFront\": false,\n    \"ShowOnCartFront\": false,\n    \"ShowOnAttachmentFront\": false,\n    \"ShowOnFileUpload\": false,\n    \"IsGiftCard\": false,\n    \"IsRequired\": false\n}",
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
      "code": "{\n    \"Id\": 1,\n    \"Name\": \"Mudando nome teste\",\n    \"IsActive\": false,\n    \"ShowOnProductFront\": false,\n    \"ShowOnCartFront\": false,\n    \"ShowOnAttachmentFront\": false,\n    \"ShowOnFileUpload\": false,\n    \"IsGiftCard\": false,\n    \"IsRequired\": false\n}",
      "language": "json"
    }
  ]
}
[/block]