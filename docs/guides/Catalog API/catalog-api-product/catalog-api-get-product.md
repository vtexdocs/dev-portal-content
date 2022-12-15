---
title: "Get Product by ID"
slug: "catalog-api-get-product"
excerpt: "Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product. \r\n> 📘 Onboarding guide \r\n>\r\n> Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey."
hidden: false
createdAt: "2020-04-01T18:13:06.495Z"
updatedAt: "2022-08-25T13:52:41.599Z"
---
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