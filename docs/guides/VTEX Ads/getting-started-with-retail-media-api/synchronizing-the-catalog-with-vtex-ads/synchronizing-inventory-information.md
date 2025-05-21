---
title: "Synchronizing inventory information"
slug: "synchronizing-inventory-information"
excerpt: "Ensure inventory availability data is kept up to date for ad display."
hidden: false
createdAt: "Thu Mar 09 2023 13:26:32 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 13 2024 19:58:32 GMT+0000 (Coordinated Universal Time)"
---

Inventory information defines the price, promotional price, and "stock." Regarding stock, we should only receive whether the product is available for sale.

| Field             | Description                                                                                          | Type    | Required? |
|-------------------|----------------------------------------------------------------------------------------------------|---------|-----------|
| product_sku       | Product ID to be inserted/updated.                                                                  | String  | Yes       |
| store_id          | Store identifier. If store_id is not sent, it will be interpreted that this inventory information will be used for all stores. | String  | No        |
| price             | Product price                                                                                       | Number  | Yes       |
| promotional_price | Promotional price of the product.                                                                   | Number  | Yes       |
| is_available      | Indicates if the product is available for sale                                                     | Boolean | Yes       |

> 🚧 Batch Insert / Update
> 
> For each batch insert/update, a maximum of 500 objects per request and 3 simultaneous requests are allowed.
> 
> Therefore, for an initial load with the entire product base, this limit must be taken into account when sending data.

### Request

Processing will be performed asynchronously.

```http
POST https://api-retail-media.newtail.com.br/product/bulk/inventories HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>

[
  {
    "product_sku": "120210",
    "store_id": "1",
    "price": 18.20,
    "promotional_price": 16.32,
    "is_available": true
  },
  {
    "product_sku": "120212",
    "price": 18.20,
    "promotional_price": 0, // this removes the promotional price
    "is_available": true
  }
]  
```

### Response with validation error

For validations, we use the RFC 8927 format https://datatracker.ietf.org/doc/rfc8927/.

The request will return HTTP status code 422. HTTP 422

```json
[
  {
    instancePath: '/0',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'product_sku'
    },
    message: "must have required property 'product_sku'"
  },
  {
    instancePath: '/0',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'promotional_price'
    },
    message: "must have required property 'promotional_price'"
  },
  {
    instancePath: '/0',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'is_available'
    },
    message: "must have required property 'is_available'"
  },
  {
    instancePath: '/1',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'price'
    },
    message: "must have required property 'price'"
  },
  {
    instancePath: '/1',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'promotional_price'
    },
    message: "must have required property 'promotional_price'"
  },
  {
    instancePath: '/1',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'is_available'
    },
    message: "must have required property 'is_available'"
  },
  {
    instancePath: '/2',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'price'
    },
    message: "must have required property 'price'"
  },
  {
    instancePath: '/2',
    schemaPath: '#/items/required',
    keyword: 'required',
    params: {
      missingProperty: 'is_available'
    },
    message: "must have required property 'is_available'"
  }
]
```
