---
title: "Update product extra information"
slug: "updateproductextrainformation"
excerpt: "The endpoint updates extra information about a product by its ID."
hidden: true
createdAt: "2021-09-28T20:47:44.085Z"
updatedAt: "2021-09-29T15:03:38.823Z"
---
## Request object has the following properties:

| Attribute          | Type             | Description                                                                                                                                            |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| productId                 | string           | Product unique identifier number.                                                                                                                     |
| seo                 | object           | SEO information about the product. This object affects how the product will be ranked in search engines, such as Google.                                                                                                                     |
| ↳ pageDescription                 | string           | Product description that will be displayed in search engines. Google only shows the first 160 characters of this description.                                                                                                                     |
| ↳ pageTitle                 | string           | To optimize your product's ranking in search results, it should not exceed 60 characters.                                                                                                                     |
| storefront                 | object           | In this object you can configure whether the product will appear in your store.                                                                                                                     |
| ↳ showOnSite                 | boolean           | Option to enable (`true`) or disable (`false`) the product display on the store. If the product is a giveaway that cannot be purchased, you must disable this option.                                                                                                                     |
| ↳ showOutOfStock                 | boolean           | If this function is enabled (`true`), the out-of-stock product will appear in your store with a Notify Me option, in which customers enter their email to be notified when the product is back in stock. If this function is disabled (`false`), the out-of-stock product will not be displayed in the store.                                                                                                                     |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"productId\":\"2\",\n    \"seo\":{\n        \"pageDescription\":\"A young prince meets with his father's ghost, who alleges that his own \nbrother, now married to his  ...\",\n        \"pageTitle\":\"Hamlet: William Shakespeare\"\n    },\n    \"storefront\":{\n        \"showOnSite\":true,\n        \"showOutOfStock\":true\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response object has the following properties:

| Attribute          | Type             | Description                                                                                                                                            |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| productId                 | string           | Product unique identifier number.                                                                                                                     |
| seo                 | object           | SEO information about the product. This object affects how the product will be ranked in search engines, such as Google.                                                                                                                     |
| ↳ pageDescription                 | string           | Product description that will be displayed in search engines. Google only shows the first 160 characters of this description.                                                                                                                     |
| ↳ pageTitle                 | string           | To optimize your product's ranking in search results, it should not exceed 60 characters.                                                                                                                     |
| storefront                 | object           | In this object you can configure whether the product will appear in your store.                                                                                                                     |
| ↳ showOnSite                 | boolean           | Option to enable (`true`) or disable (`false`) the product display on the store. If the product is a giveaway that cannot be purchased, you must disable this option.                                                                                                                     |
| ↳ showOutOfStock                 | boolean           | If this function is enabled (`true`), the out-of-stock product will appear in your store with a Notify Me option, in which customers enter their email to be notified when the product is back in stock. If this function is disabled (`false`), the out-of-stock product will not be displayed in the store.                                                                                                                     |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"productId\":\"2\",\n    \"seo\":{\n        \"pageDescription\":\"A young prince meets with his father's ghost, who alleges that his own \nbrother, now married to his  ...\",\n        \"pageTitle\":\"Hamlet: William Shakespeare\"\n    },\n    \"storefront\":{\n        \"showOnSite\":true,\n        \"showOutOfStock\":true\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]