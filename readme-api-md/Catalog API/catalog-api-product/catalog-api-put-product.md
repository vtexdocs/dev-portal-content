---
title: "Update Product"
slug: "catalog-api-put-product"
excerpt: "Updates an existing Product."
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-05-25T18:33:05.111Z"
---
## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n   \"Name\": \"insert product test\",\n   \"DepartmentId\": 1,\n   \"CategoryId\": 2,\n   \"BrandId\": 2000000,\n   \"LinkId\": \"insert-product-test\",\n   \"RefId\": \"310117869\",\n   \"IsVisible\": true,\n   \"Description\": \"texto de descrição\",\n   \"DescriptionShort\": \"Utilize o CEP 04548-005 para frete grátis\",\n   \"ReleaseDate\": \"2019-01-01T00:00:00\",\n   \"KeyWords\": \"teste,teste2\",\n   \"Title\": \"product de teste\",\n   \"IsActive\": true,\n   \"TaxCode\": \"\",\n   \"MetaTagDescription\": \"tag test\",\n   \"SupplierId\": 1,\n   \"ShowWithoutStock\": true,\n   \"AdWordsRemarketingCode\": null,\n   \"LomadeeCampaignCode\": null,\n   \"Score\": 1\n}\n",
      "language": "json"
    }
  ]
}
[/block]
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"Id\": 52,\n   \"Name\": \"insert product test\",\n   \"DepartmentId\": 1,\n   \"CategoryId\": 2,\n   \"BrandId\": 2000000,\n   \"LinkId\": \"insert-product-test\",\n   \"RefId\": \"310117869\",\n   \"IsVisible\": true,\n   \"Description\": \"texto de descrição\",\n   \"DescriptionShort\": \"Utilize o CEP 04548-005 para frete grátis\",\n   \"ReleaseDate\": \"2019-01-01T00:00:00\",\n   \"KeyWords\": \"teste,teste2\",\n   \"Title\": \"product de teste\",\n   \"IsActive\": true,\n   \"TaxCode\": \"\",\n   \"MetaTagDescription\": \"tag test\",\n   \"SupplierId\": 1,\n   \"ShowWithoutStock\": true,\n   \"AdWordsRemarketingCode\": null,\n   \"LomadeeCampaignCode\": null,\n   \"Score\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]