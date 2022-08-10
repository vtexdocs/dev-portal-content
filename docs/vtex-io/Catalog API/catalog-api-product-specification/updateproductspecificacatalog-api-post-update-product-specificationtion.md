---
title: "Update Product Specification"
slug: "updateproductspecificacatalog-api-post-update-product-specificationtion"
excerpt: "Updates the value of a product specification by the product's ID. The ID or name can be used to identify what product specification will be updated. Specification fields must be previously created in your Catalog."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-03-12T14:18:22.618Z"
---
## Response object has the following properties:

| Attribute | Type    | Description                 |
| --------- | ------- | --------------------------- |
| `value`   | object  | Values of the Specification |
| `id`      | integer | ID of the Specification     |
| `name`    | string  | Name of the Specification   |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Value\": [\n            \"Rubber\",\n            \"Plastic\"\n        ],\n        \"Id\": 30\n    },\n    {\n        \"Value\": [\n            \"Giant\"\n        ],\n        \"Name\": \"Nickname\"\n    }\n]\n\n",
      "language": "json"
    }
  ]
}
[/block]