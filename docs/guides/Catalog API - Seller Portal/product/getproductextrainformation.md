---
title: "Get product extra information"
slug: "getproductextrainformation"
excerpt: "The endpoint retrieves extra information about a product by its ID."
hidden: true
createdAt: "2021-09-28T20:47:44.084Z"
updatedAt: "2021-09-29T15:00:41.459Z"
---
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
      "code": "{\n\t\"productId\":\"2\",\n\t\"seo\":{\n\t\t\"pageDescription\":\"A young prince meets with his father's ghost, who alleges that his own \nbrother, now married to his  ...\",\n\t\t\"pageTitle\":\"Hamlet: William Shakespeare\"\n\t},\n\t\"storefront\":{\n\t\t\"showOnSite\":true,\n\t\t\"showOutOfStock\":true\n\t}\n}",
      "language": "json"
    }
  ]
}
[/block]