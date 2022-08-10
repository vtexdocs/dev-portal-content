---
title: "Create a Product"
slug: "postproduct"
excerpt: "The endpoint creates a new product and its variations."
hidden: true
createdAt: "2021-07-05T14:05:36.168Z"
updatedAt: "2021-08-10T17:41:57.587Z"
---
## Request body has the following properties:

| Attribute      | Type             | Description                                                                                                                                            |
| -------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id             | string           | Products unique identifier number.                                                                                                                     |
| externalId     | string           | Product reference unique identifier number in the store.                                                                                               |
| status         | string           | Status of the product. Its values can be `active` or `inactive.                                                                                   |
| condition      | string           | Condition of the product. Its values can be `new`, `used`, or `refurbished`.                                                                     |
| type           | string           | Type of the product. When selling various products, it is essential to identify if the product is `physical`, `digital`, or `service`.           |
| name           | string           | Product Name. Use simple words and avoid other languages or complex writing. This field is essential for SEO and must respect the 150 character limit. |
| description    | string           | Description of the primary information related to the product. A simple and easy-to-understand summary for the customer.                               |
| brandId        | string           | Product’s Brand unique identifier number.                                                                                                              |
| categoryIds    | array of strings | Product’s Categories unique identifier numbers. It can have multiples IDs for each Category and Sub-categories.                                        |
| salesChannels  | array of strings | An array of Trade Policies IDs that have the product included on them.                                                                                 |
| specs          | array of objects | Specifications that will differentiate the possible product variations.                                                                                |
| ↳ name         | string           | Specification name.                                                                                                                                    |
| ↳ values       | array of strings | Specification values.                                                                                                                                  |
| attributes     | array of objects | Attributes of the product. Attributes are additional properties used to create site browsing filters.                                                  |
| ↳ name         | string           | Attribute name.                                                                                                                                        |
| ↳ value        | string           | Attribute value.                                                                                                                                       |
| ↳ description  | string           | Attribute description.                                                                                                                                 |
| ↳ isFilterable | boolean          | The condition if the attribute is filterable or not.                                                                                                   |
| slug           | string           | Reference of the product in the URL of the store.                                                                                                      |
| images         | array of objects | Information of the images of the product.                                                                                                              |
| ↳ id              | string           | Image ID.                                                                                                                                             |
| ↳ url          | string           | Image URL.                                                                                                                                             |
| ↳ alt          | string           | Image alternative description.                                                                                                                         |
| skus           | array of objects | Variations of the product.                                                                                                                             |
| ↳ id           | string           | Variation unique identifier number.                                                                                                                    |
| ↳ code         | string           | Variation reference code in the store.                                                                                                                 |
| ↳ sellers      | array of objects | Information about the sellers who sell the product.                                                                                                    |
| ↳↳ id          | string           | Seller unique identifier number.                                                                                                                       |
| ↳↳ skuId       | integer          | Unique identifier number of the variation associated with the seller.                                                                                  |
| ↳ isActive     | boolean          | If the variation is active or inactive.                                                                                                                |
| ↳ weight       | float            | Variation weight.                                                                                                                                      |
| ↳ dimensions   | object           | Variation dimensions.                                                                                                                                  |
| ↳↳ width       | float            | Variation width.                                                                                                                                       |
| ↳↳ height      | float            | Variation height.                                                                                                                                      |
| ↳↳ length      | float            | Variation length.                                                                                                                                      |
| ↳ specs        | array of objects | Variation specifications.                                                                                                                              |
| ↳↳ name        | string           | Variation’s specification name.                                                                                                                        |
| ↳↳ values      | string           | Variation’s specification values.                                                                                                                      |
| ↳ images           | array of objects | Variation’s images IDs.                                                                                                                                      |
| channels       | array of objects | Information about marketplaces that sell the product.                                                                                                  |
| ↳ id           | string           | Marketplace unique identifier number.                                                                                                                  |
| ↳ productId    | string           | Marketplace’s product unique identifier number.                                                                                                       |
| ↳ categoryId   | string           | Marketplace’s category unique identifier number.                                                                                                       |
| ↳ brandId      | string           | Marketplace’s brand unique identifier number.                                                                                                          |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": null,\n    \"externalId\": \"Test\",\n    \"status\": \"active\",\n    \"condition\": \"new\",\n    \"type\": \"physical\",\n    \"name\": \"Camiseta VTEX 10\",\n    \"description\": \"Descrição camiseta VTEX\",\n    \"brandId\": \"1\",\n    \"categoryIds\": [\n        \"732\"\n    ],\n    \"salesChannels\": [\n        \"1\"\n    ],\n    \"specs\": [\n        {\n            \"name\": \"Cor\",\n            \"values\": [\n                \"Preto\",\n                \"Branco\"\n            ]\n        },\n        {\n            \"name\": \"Tamanho\",\n            \"values\": [\n                \"P\",\n                \"M\",\n                \"G\"\n            ]\n        }\n    ],\n    \"attributes\": [\n        {\n            \"name\": \"Tecido\",\n            \"value\": \"Algodão\",\n            \"description\": \"Descricao do atributo 1\",\n            \"isFilterable\": false\n        },\n        {\n            \"name\": \"Genero\",\n            \"value\": \"Masculino\",\n            \"description\": \"Descricao do atributo 2\",\n            \"isFilterable\": false\n        }\n    ],\n    \"slug\": \"/camisetaVTEX\",\n    \"images\": [\n        {\n            \"id\": \"vtex_logo.jpg\",\n            \"url\": \"https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\",\n            \"alt\": \"imagem\"\n        }\n    ],\n    \"skus\": [\n        {\n            \"id\": null,\n            \"externalId\": null,\n            \"code\": \"1234567\",\n            \"sellers\": [\n                {\n                    \"id\": \"1\"\n                }\n            ],\n            \"isActive\": true,\n            \"weight\": 300.0,\n            \"dimensions\": {\n                \"width\": 1.500,\n                \"height\": 2.100,\n                \"length\": 1.600\n            },\n            \"specs\": [\n                {\n                    \"name\": \"Cor\",\n                    \"value\": \"Branco\"\n                },\n                {\n                    \"name\": \"Tamanho\",\n                    \"value\": \"P\"\n                }\n            ],\n            \"images\": [\n                \"vtex_logo.jpg\"\n            ]\n        },\n        {\n            \"id\": null,\n            \"externalId\": null,\n            \"code\": \"1234568\",\n            \"sellers\": [\n                {\n                    \"id\": \"1\"\n                }\n            ],\n            \"isActive\": true,\n            \"weight\": 300.0,\n            \"dimensions\": {\n                \"width\": 1.500,\n                \"height\": 2.100,\n                \"length\": 1.600\n            },\n            \"specs\": [\n                {\n                    \"name\": \"Cor\",\n                    \"value\": \"Preto\"\n                },\n                {\n                    \"name\": \"Tamanho\",\n                    \"value\": \"P\"\n                }\n            ],\n            \"images\": [\n                \"vtex_logo.jpg\"\n            ]\n        }\n    ],\n    \"channels\": [\n        {\n            \"id\": \"vtxezy9960\",\n            \"productId\": null,\n            \"categoryId\": \"1000084\",\n            \"brandId\": null\n        }\n    ]\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute          | Type             | Description                                                                                                                                            |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id                 | string           | Products unique identifier number.                                                                                                                     |
| externalId         | string           | Product reference unique identifier number in the store.                                                                                               |
| status             | string           | Status of the product. Its values can be \`active\` or \`inactive\`.                                                                                   |
| condition          | string           | Condition of the product. Its values can be \`new\`, \`used\`, or \`refurbished\`.                                                                     |
| type               | string           | Type of the product. When selling various products, it is essential to identify if the product is \`physical\`, \`digital\`, or \`service\`.           |
| name               | string           | Product Name. Use simple words and avoid other languages or complex writing. This field is essential for SEO and must respect the 150 character limit. |
| description        | string           | Description of the primary information related to the product. A simple and easy-to-understand summary for the customer.                               |
| brandId            | string           | Product’s Brand unique identifier number.                                                                                                              |
| brandName          | string           | Product’s Brand Name.                                                                                                                                  |
| categoryIds        | array of strings | Product’s Categories unique identifier numbers. It can have multiples IDs for each Category and Sub-categories.                                        |
| categoryNames      | array of strings | Product’s Categories names. It can have multiples names for each Category and Sub-categories.                                                          |
| mainCategoryBranch | array of objects | General information about the Product’s Category.                                                                                                      |
| ↳ id               | string           | Category unique identifier number.                                                                                                                     |
| ↳ name             | boolean          | Category name.                                                                                                                                         |
| ↳ isActive         | boolean          | The condition defines if the category is active or inactive.                                                                                           |
| ↳ displayOnMenu    | boolean          | The condition will display the category on the store menu.                                                                                             |
| ↳ score            | integer          | The score of the product is used to set the priority on the search result page.                                                                        |
| ↳ filterByBrand    | boolean          | The condition defines if the category can be filtered by brand.                                                                                        |
| ↳ isClickable      | boolean          | The condition defines if the category is clickable or not in the store.                                                                                |
| salesChannels      | array of strings | An array of Trade Policies IDs that have the product included on them.                                                                                 |
| specs              | array of objects | Specifications that will differentiate the possible products variations.                                                                               |
| ↳ name             | string           | Specification name.                                                                                                                                    |
| ↳ values           | array of strings | Specification values.                                                                                                                                  |
| attributes         | array of objects | Attributes of the product. Attributes are additional properties used to create site browsing filters.                                                  |
| ↳ name             | string           | Attribute name.                                                                                                                                        |
| ↳ value            | string           | Attribute value.                                                                                                                                       |
| ↳ description      | string           | Attribute description.                                                                                                                                 |
| ↳ isFilterable     | boolean          | The condition if the attribute is filterable or not.                                                                                                   |
| slug               | string           | Reference of the product in the URL of the store.                                                                                                      |
| images             | array of objects | Informations of the images of the product.                                                                                                             |
| ↳ id              | string           | Image ID.                                                                                                                                             |
| ↳ url              | string           | Image URL.                                                                                                                                             |
| ↳ alt              | string           | Image alternative description.                                                                                                                         |
| skus               | array of objects | Variations of the product.                                                                                                                             |
| ↳ id               | string           | Variation unique identifier number.                                                                                                                    |
| ↳ code             | string           | Variation reference code in the store.                                                                                                                 |
| ↳ sellers          | array of objects | Information about the sellers who sell the product.                                                                                                    |
| ↳↳ id              | string           | Seller unique identifier number.                                                                                                                       |
| ↳↳ skuId           | integer          | Unique identifier number of the variation association with the seller.                                                                                 |
| ↳ isActive         | boolean          | If the variation is active or inactive.                                                                                                                |
| ↳ weight           | float            | Variation weight.                                                                                                                                      |
| ↳ dimensions       | object           | Variation dimensions.                                                                                                                                  |
| ↳↳ width           | float            | Variation width.                                                                                                                                       |
| ↳↳ height          | float            | Variation height.                                                                                                                                      |
| ↳↳ length          | float            | Variation length.                                                                                                                                      |
| ↳ specs            | array of objects | Variation specifications.                                                                                                                              |
| ↳↳ name            | string           | Variation’s specification name.                                                                                                                        |
| ↳↳ values          | string           | Variation’s specification values.                                                                                                                      |
| ↳ images           | array of objects | Variation’s images IDs.                                                                                                                                      |
| origin             | string           | Origin account of the product.                                                                                                                         |
| channels           | array of objects | Information about marketplaces that sell the product.                                                                                                  |
| ↳ id               | string           | Marketplace unique identifier number.                                                                                                                  |
| ↳ brandId          | string           | Marketplace’s brand unique identifier number.                                                                                                          |
| ↳ productId        | string           | Marketplace’s  product unique identifier number.                                                                                                       |
| ↳ categoryId       | string           | Marketplace’s category unique identifier number.                                                                                                       |
| createdAt          | string           | Date when the product was created.                                                                                                                     |
| updatedAt          | string           | Last date when the product was updated.                                                                                                                |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"189371\",\n    \"status\": \"active\",\n    \"condition\": \"new\",\n    \"type\": \"physical\",\n    \"name\": \"Camiseta VTEX 10\",\n    \"description\": \"Descrição camiseta VTEX\",\n    \"brandId\": \"1\",\n    \"brandName\": \"Givenchy\",\n    \"categoryIds\": [\n        \"732\"\n    ],\n    \"categoryNames\": [\n        \"/Categoria de teste do Leo/\"\n    ],\n    \"mainCategoryBranch\": [\n        {\n            \"id\": \"732\",\n            \"name\": \"Categoria de teste do Leo\",\n            \"isActive\": false,\n            \"displayOnMenu\": false,\n            \"score\": 0,\n            \"filterByBrand\": false,\n            \"isClickable\": false\n        }\n    ],\n    \"salesChannels\": [\n        \"1\"\n    ],\n    \"specs\": [\n        {\n            \"name\": \"Cor\",\n            \"values\": [\n                \"Preto\",\n                \"Branco\"\n            ]\n        },\n        {\n            \"name\": \"Tamanho\",\n            \"values\": [\n                \"P\",\n                \"M\",\n                \"G\"\n            ]\n        }\n    ],\n    \"attributes\": [\n        {\n            \"name\": \"Tecido\",\n            \"value\": \"Algodão\",\n            \"description\": \"Descricao do atributo 1\",\n            \"isFilterable\": false\n        },\n        {\n            \"name\": \"Genero\",\n            \"value\": \"Masculino\",\n            \"description\": \"Descricao do atributo 2\",\n            \"isFilterable\": false\n        }\n    ],\n    \"slug\": \"/camisetaVTEX\",\n    \"images\": [\n        {\n            \"id\": \"vtex_logo.jpg\",\n            \"url\": \"https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\",\n            \"alt\": \"imagem\"\n        }\n    ],\n    \"skus\": [\n        {\n            \"id\": \"182907\",\n            \"code\": \"1234567\",\n            \"sellers\": [\n                {\n                    \"id\": \"1\",\n                    \"skuId\": 0\n                }\n            ],\n            \"isActive\": true,\n            \"weight\": 300.0,\n            \"dimensions\": {\n                \"width\": 1.500,\n                \"height\": 2.100,\n                \"length\": 1.600\n            },\n            \"specs\": [\n                {\n                    \"name\": \"Cor\",\n                    \"value\": \"Preto\"\n                },\n                {\n                    \"name\": \"Tamanho\",\n                    \"value\": \"P\"\n                }\n            ],\n            \"images\": [\n                \"vtex_logo.jpg\"\n            ]\n        },\n        {\n            \"id\": \"182908\",\n            \"code\": \"1234568\",\n            \"sellers\": [\n                {\n                    \"id\": \"1\",\n                    \"skuId\": 0\n                }\n            ],\n            \"isActive\": true,\n            \"weight\": 300.0,\n            \"dimensions\": {\n                \"width\": 1.500,\n                \"height\": 2.100,\n                \"length\": 1.600\n            },\n            \"specs\": [\n                {\n                    \"name\": \"Cor\",\n                    \"value\": \"Branco\"\n                },\n                {\n                    \"name\": \"Tamanho\",\n                    \"value\": \"G\"\n                }\n            ],\n            \"images\": [\n                \"vtex_logo.jpg\"\n            ]\n        }\n    ],\n    \"origin\": \"vtxleo7778\",\n    \"channels\": [\n        {\n            \"id\": \"vtxezy9960\",\n            \"categoryId\": \"1000084\"\n        }\n    ],\n    \"createdAt\": \"2021-05-05T22:10:10.168391+00:00\",\n    \"updatedAt\": \"2021-05-06T21:17:52.598168+00:00\"\n}",
      "language": "json"
    }
  ]
}
[/block]