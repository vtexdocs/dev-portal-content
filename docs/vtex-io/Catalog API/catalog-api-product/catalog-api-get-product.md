---
title: "Get Product by id"
slug: "catalog-api-get-product"
excerpt: "Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product."
hidden: false
createdAt: "2020-04-01T18:13:06.495Z"
updatedAt: "2020-09-15T23:57:46.450Z"
---
## Response body object has the following properties:

| Attribute              | Type    | Description                                                                           |
| ---------------------- | ------- | ------------------------------------------------------------------------------------- |
| Id                     | integer | Product ID                                                                            |
| Name                   | string  | Product Name                                                                          |
| DepartmentId           | integer | Product Department ID                                                                 |
| CategoryId             | integer | Product Category ID                                                                   |
| BrandId                | integer | Product Brand ID                                                                      |
| LinkId                 | string  | Text Link                                                                             |
| RefId                  | string  | Product Referecial Code                                                               |
| IsVisible              | boolean | If the Product is visible on the store                                                |
| Description            | string  | Product Description                                                                   |
| DescriptionShort       | string  | Complement Name                                                                       |
| ReleaseDate            | string  | Product Release Date                                                                  |
| KeyWords               | string  | Substitutes words for the Product                                                     |
| Title                  | string  | Tag Title                                                                             |
| IsActive               | boolean | If the Product is active or not                                                       |
| TaxCode                | string  | Product Fiscal Code                                                                   |
| MetaTagDescription     | string  | Meta Tag Description                                                                  |
| SupplierId             | integer | Product Supplier ID                                                                   |
| ShowWithoutStock       | boolean | Defines if the Product will remain being shown in the store even if it’s out of stock |
| AdWordsRemarketingCode | string  | Code specific for AdWords Remarketing                                                 |
| LomadeeCampaignCode    | string  | Code specific for Lomadee Campaign                                                    |
| Score                  | integer | Value used for Product search ordenation                                              |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"Name\": \"insert product test\",\n   \"DepartmentId\": 1,\n   \"CategoryId\": 2,\n   \"BrandId\": 2000000,\n   \"LinkId\": \"insert-prodduct-test\",\n   \"RefId\": \"310117869\",\n   \"IsVisible\": true,\n   \"Description\": \"texto de descrição\",\n   \"DescriptionShort\": \"Utilize o CEP 04548-005 para frete grátis\",\n   \"ReleaseDate\": \"2019-01-01T00:00:00\",\n   \"KeyWords\": \"teste,teste2\",\n   \"Title\": \"product de teste\",\n   \"IsActive\": true,\n   \"TaxCode\": \"\",\n   \"MetaTagDescription\": \"tag test\",\n   \"SupplierId\": 1,\n   \"ShowWithoutStock\": true,\n   \"AdWordsRemarketingCode\": null,\n   \"LomadeeCampaignCode\": null,\n   \"Score\": 1\n}\n",
      "language": "json"
    }
  ]
}
[/block]