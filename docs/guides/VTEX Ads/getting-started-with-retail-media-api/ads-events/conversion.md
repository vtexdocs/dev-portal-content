---
title: "Conversion"
slug: "conversion"
excerpt: "Track when an ad leads to a purchase."
hidden: false
createdAt: "Wed Mar 01 2023 15:46:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Jan 13 2025 20:29:12 GMT+0000 (Coordinated Universal Time)"
---

> 🚧 The event URL must not be "constructed"; always use the URL that comes from the ad request response.  
>  
> This is very important to ensure long-term integration stability. The parameters of the event URL may change over time, but the integration itself does not need to be modified. This makes the entire process evolutionary and transparent for everyone.

# Basic Order Information

To send catalog information, it is necessary to provide the basic information of a product. The table below describes which fields are mandatory and which are optional in this operation:

### Order:

> 📘 Hash Fields  
>  
> Hash fields ensure the anonymity of user data and allow obtaining new information about the user so that segmented campaigns and reports can be more effective.  
>  
> To learn how to hash the information, see: <http://bit.ly/3WiL5ns>

| Field             | Type         | Description                                                                                   | Required?   | Recommended? |
|-------------------|--------------|-----------------------------------------------------------------------------------------------|-------------|--------------|
| publisher_id      | String       | Publisher identification                                                                     | Yes         |              |
| user_id           | String       | User identification                                                                          | Yes         |              |
| session_id        | String       | Identification of the session in which the purchase was made, to help attribute the sale to ads. | Yes         |              |
| order_id          | String       | Order identification                                                                        | Yes         |              |
| email_hashed      | String       | Hashed user email identification                                                            | Yes         |              |
| created_at        | String       | Order creation date in ISO 8601 format (UTC - no timezone)                                   | Yes         |              |
| items             | Array[Item]  | List of items purchased in the order                                                        | Yes         |              |
| channel           | String       | Identifies the conversion channel                                                           | No          | Yes          |
| is_company        | Bool         | Indicates if the sale was made to an individual or a company.  \ndefault=false                | No          | Yes          |
| gender            | String       | Indicates customer's gender.  \n\n- F: female  \n- M: male  \n- O: other  \n- null: unidentified Default=null | No          | Yes          |
| uf                | String       | Indicates the state where the order was made                                                | No          | Yes          |
| city              | String       | Indicates the name of the city where the customer bought                                    | No          | Yes          |
| phone_hashed      | String       | Hashed user phone number identification                                                     | No          | Yes          |
| social_id_hashed  | String       | Hashed user CPF or CNPJ identification                                                      | No          | Yes          |
| first_name_hashed | String       | Hashed user first name identification                                                      | No          | Yes          |
| last_name_hashed  | String       | Hashed user last name identification                                                       | No          | Yes          |

### Item:

| Field             | Description                                    | Type   | Required       |
| :---------------- | :--------------------------------------------- | :----- | :------------- |
| sku               | Product SKU identification                     | String | Yes            |
| quantity          | Quantity of product purchased                   | Double | Yes            |
| price             | Product "from" price                            | Double | Yes            |
| promotional_price | Product "for" price (discounted price)         | Double | Yes            |
| seller_id         | Seller ID identification                        | String | No             |
| product_id        | Unique product identification that includes the SKU | String | No         |

# Conversion Notification

The conversion notification should use the order integration endpoint, which can be used to notify one or more orders (sending them in a batch).

Ideally, it should be notified at the moment the order is closed, thus having a view of the placed sale.

### Request

> 🚧 The price and promotional price must not be multiplied by the quantity.

```http
POST https://newtail-media.newtail.com.br/v1/beacon/conversion HTTP/1.1
accept: application/json
content-type: application/json

{
  "channel": "ecommerce",
  "publisher_id": "xxx",
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499",
  "order_id": "123",
  "email_hashed": "xyz",
  "items": [
    {
      "sku": "12221",
      "seller_id": "1234",
      "product_id": "4567",
      "quantity": 1,
      "price": 2000.00, // note que não há multiplicação da quantidade com o valor
      "promotional_price": 1899.00 // note que não há multiplicação da quantidade com o valor
    },
    {
      "sku": "12222",
      "seller_id": null,
      "product_id": "4568",
      "quantity": 2,
      "price": 500.00, // note que não há multiplicação da quantidade com o valor
      "promotional_price": 400.00 // note que não há multiplicação da quantidade com o valor
    }
  ]
  "created_at": "2023-01-01T09:20:00Z"
}
 
```

### Response

> The successful response of the request will have HTTP status code 202

```json JSON
{
	"messages": [
		"conversion will be processed soon"
	]
}
```

> The failure response of the request will have HTTP status code 422

> The error response follows RFC 8927 https://datatracker.ietf.org/doc/rfc8927/

```json
[
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'user_id'",
        "params": {
            "missingProperty": "user_id"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'order_id'",
        "params": {
            "missingProperty": "order_id"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'publisher_id'",
        "params": {
            "missingProperty": "publisher_id"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'items'",
        "params": {
            "missingProperty": "items"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'created_at'",
        "params": {
            "missingProperty": "created_at"
        },
        "schemaPath": "#/required"
    }
]
```
