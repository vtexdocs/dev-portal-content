---
title: "Synchronizing product information"
slug: "synchronizing-product-information"
excerpt: "Sync product details such as name, image, price, and category."
hidden: false
createdAt: "Wed Mar 01 2023 15:38:25 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Dec 11 2024 14:36:58 GMT+0000 (Coordinated Universal Time)"
---

To send catalog information, it is necessary to provide the basic information of a product. The table below describes which fields are mandatory and which are optional in this operation:

| Field        | Description                                                                                                                                                                                                                                                                                 | Type          | Required?   |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------|
| product_sku  | Product ID to be inserted / updated.                                                                                                                                                                                                                                                        | String        | Yes         |
| parent_sku   | SKU of the parent product                                                                                                                                                                                                                                                                  | String        | No          |
| name         | Product name.                                                                                                                                                                                                                                                                               | String        | Yes         |
| url          | URL of the product page.                                                                                                                                                                                                                                                                    | String        | Yes         |
| image_url    | URL of the main product image.                                                                                                                                                                                                                                                             | String        | No          |
| categories   | List of product categories.                                                                                                                                                                                                                                                                 | Array[String] | Yes         |
| brand        | Product brand.                                                                                                                                                                                                                                                                              | String        | No          |
| gtins        | Barcode <br /><br />**For Newtail Network, sending the GTIN is mandatory**                                                                                                                                                                                                                  | Array[String] | No/Yes      |
| metadata     | Additional product information                                                                                                                                                                                                                                                             | Object        | No          |
| tags         | This is a list of "tags" that products have to be used later during ad queries to better contextualize the search. <ul><li>Maximum of 10 tags per SKU</li><li>Maximum of 64 characters per tag</li></ul><br /> **Only works for Product campaigns**                                         | Array[String] | No          |
| sellers      | List of sellers who sell that product. <br />Maximum of 64 characters per seller                                                                                                                                                                                                             | Array[String] | No          |

# Product Insertion and Update in the Catalog

To update the basic product data, the following endpoint must be used:

> 🚧 Batch Insert / Update
> 
> For each batch insert/update, a maximum of 500 objects per request and 3 simultaneous requests are allowed.
> 
> Therefore, for an initial load with the entire product base, this limit must be taken into account when sending data.

### Request

Processing will be performed asynchronously.

```http
POST https://api-retail-media.newtail.com.br/product/bulk/products HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>

[
    {
    "product_sku": "teste-120210",
    "name": "Notebook Samsung Intel Celeron-6305 NP550XDA-KP3BR 4GB 256GB SSD Tela 15,6\" Windows 11 - Cinza Chumbo",
    "url": "https://www.americanas.com.br/produto/4100903080",
    "image_url": "https://images-americanas.b2w.io/produtos/01/00/img/4100903/1/4100903143_1GG.jpg",
    "categories": ["Informática", "Notebooks"],
    "brand": "Samsung",
    "gtins": ["7898915633481"],
    "metadata": {
        "key": "value1"
    }
  },
  {
    "product_sku": "teste-120211",
    "name": "Notebook Samsung Intel Celeron-6305 NP550XDA-KP3BR 4GB 256GB SSD Tela 15,6\" Windows 11 - Cinza Chumbo",
    "url": "https://www.americanas.com.br/produto/4100903080",
    "categories": ["Informática", "Notebooks"],
    "brand": "Samsung",
    "gtins": ["7898915633481"],
    "tags": ["Mega Maio"]
  }
]
```

### Response

> The response will have HTTP code 202

```json
{
	"messages": [
		"products will be processed soon"
	]
}
```

### Response with Validation Error

For validations, we use the format defined by RFC 8927 https://datatracker.ietf.org/doc/rfc8927/

The request response will have HTTP status code 422

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
