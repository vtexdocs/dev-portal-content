---
title: "Synchronizing product information"
slug: "synchronizing-product-information"
excerpt: "Sync product details such as name, image, price, and category."
hidden: false
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

To send catalog information, it is necessary to provide the basic information of a product. The fields may be mandatory or optional in this operation.

Learn more about each field on `POST` [Synchronize product information](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/product/bulk/products).

# Product Insertion and Update in the Catalog

To update the basic product data, the following endpoint must be used:

> 🚧 Batch Insert / Update
> 
> For each batch insert/update, a maximum of 500 objects per request and 3 simultaneous requests are allowed.
> 
> Therefore, for an initial load with the entire product base, this limit must be taken into account when sending data.

### Request

Processing will be performed asynchronously.

```json
POST https://api.ads.vtex.com/product/bulk/products HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>

[
    {
    "product_sku": "sample-120210",
    "name": "TechBrand Laptop Model X-15 4GB 256GB SSD 15.6\" Display Windows 11 - Gray",
    "url": "https://www.example.com/product/4100903080",
    "image_url": "https://images.example.com/products/01/00/img/4100903/1/4100903143_1GG.jpg",
    "categories": ["Computers", "Laptops"],
    "brand": "TechBrand",
    "gtins": ["7898915633481"],
    "metadata": {
        "key": "value1"
    }
  },
  {
    "product_sku": "sample-120211", 
    "name": "TechBrand Laptop Model X-15 4GB 256GB SSD 15.6\" Display Windows 11 - Gray",
    "url": "https://www.example.com/product/4100903080",
    "categories": ["Computers", "Laptops"],
    "brand": "TechBrand",
    "gtins": ["7898915633481"],
    "tags": ["Mega Maio"]
  }
]
```

### Response

>ℹ️ A successful response will have HTTP code 202.

```json
{
	"messages": [
		"products will be processed soon"
	]
}
```

### Response with Validation Error

For validations, we use the format defined by [RFC 8927](https://datatracker.ietf.org/doc/rfc8927/), as exemplified below.

>ℹ️ A failed response will have HTTP code 422.

```json
[
  {
    instancePath: '/0',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: { missingProperty: 'product_sku' },
    message: "must have required property 'product_sku'",
  },
  {
    instancePath: '/0',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: { missingProperty: 'url' },
    message: "must have required property 'url'",
  },
  {
    instancePath: '/0',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: { missingProperty: 'image_url' },
    message: "must have required property 'image_url'",
  },
  {
    instancePath: '/1',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: { missingProperty: 'name' },
    message: "must have required property 'name'",
  },
  {
    instancePath: '/1',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: { missingProperty: 'url' },
    message: "must have required property 'url'",
  },
  {
    instancePath: '/1',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: { missingProperty: 'image_url' },
    message: "must have required property 'image_url'",
  },
]
```
