---
title: "Integrating VTEX Ads with external marketplaces"
slug: "integrating-vtex-ads-with-external-marketplaces"
excerpt: "Learn how to integrate VTEX Ads with external marketplaces through authentication, catalog management, campaign operations, and SSO implementation."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-13T00:00:00.000Z"
---

This document describes how to integrate VTEX Ads with external marketplaces through bidirectional authentication, catalog synchronization, and unified campaign management.

## Authentication

Authentication occurs bidirectionally, both from the marketplace to VTEX Ads and from VTEX Ads to the marketplace.

### Marketplace to VTEX Ads

The connection requires adding two parameters in the request headers sent to VTEX Ads.

| Header | Description |
| --- | --- |
| `x-app-id` | The App ID identifies the API user |
| `x-api-key` | The API Key identifies the API "password" |

>ℹ️ Access credentials must be requested from our [Support](https://support.vtex.com/hc/en-us/requests) team.

### VTEX Ads to marketplace

In this scenario, the connection will be from VTEX Ads to the marketplace. To standardize this integration, we will use **Basic Authentication** format in the request.

| Authentication | Description |
| --- | --- |
| `username` | Username for authentication |
| `password` | User password |

>ℹ️ For more information about Basic Authentication functionality, see the [RFC 7617 specification](https://datatracker.ietf.org/doc/html/rfc7617).

## Catalog

The catalog API enables product synchronization between marketplaces and VTEX Ads. All product data must include the following attributes:

| Attribute | Description | Type | Required |
| --- | --- | --- | --- |
| `product_sku` | Unique identifier of the parent product | String | Yes |
| `name` | Product title | String | Yes |
| `image_url` | Public product image URL, can be just a thumbnail | String | No |
| `categories` | List of categories | String | Yes |
| `brand` | Product brand name | String | Yes |
| `gtins` | List of EANs | Array<String> | No |
| `urls` | Product URL information | Array<Object> | Yes |
| `urls.site` | Site brand name | String | No |
| `urls.url` | Product URL | String | Yes |
| `stocks` | Product stock information | Array<Object> | Yes |
| `stocks.site` | Site brand name | String | No |
| `stocks.seller_id` | Seller ID identifier | String | No |
| `stocks.quantity` | Stock quantity | Float | Yes |
| `metadata` | Information returned during ad queries without modification | Object<String, String> | No |

For this step, we need an API to query the retailer's catalog, and this catalog must contain:

|Attribute|Description|
|:--------|:----------|
|seller_id|Filter by seller identifier.|
|name|Partial search by product name.|
|skus|Filter by a list of SKUs.|
|eans|Filter by a list of EANs.|
|quantity|Number of items that should be returned.|
|page|Current page number. Starts at 0 (zero).|

```http
GET PREFIX/search?name=&seller_id=&skus=sku1,sku2,...,skuN&eans=ean1,ean2,...,eanN&quantity=&page=  
```

### Response example - Status 200

```json
[
  {
    "product_sku": "sku123",
    "name": "Red Sneakers",
    "image_url": "https://example.com/image.jpg",
    "categories": "Sports/Shoes",
    "brand": "Nike",
    "gtins": ["1234567890123"],
    "urls": [
      {
        "site": "example-store",
        "url": "https://example.com/product/red-sneakers"
      }
    ],
    "stocks": [
      {
        "site": "example-store",
        "seller_id": "seller123",
        "quantity": 10
      }
    ],
    "metadata": {
      "color": "red",
      "size": "42"
    }
  }
]
```

> ⚠️ Any status other than 200 is considered an error.

## Advertiser (seller)

The Advertiser entity manages sellers and their associated data.

| Endpoints | Description | Filters |
| --- | --- | --- |
| GET /api/v1/advertisers | Search advertisers | quantity, page, name, seller_id |
| POST /api/v1/advertisers | Create advertiser | - |
| GET /api/v1/advertisers/:seller_id | Get advertiser by seller ID | - |
| PATCH /api/v1/advertisers/:seller_id | Update advertiser by seller ID | - |

## Campaigns

The Campaigns entity manages advertising campaign creation and updates.

| Endpoints | Description | Filters |
| --- | --- | --- |
| GET /api/v1/campaigns | List campaigns | seller_id, page, quantity, name, status, ad_type |
| POST /api/v1/campaigns | Create campaign | - |
| GET /api/v1/campaigns/:campaign_id | Get campaign by ID | - |
| PATCH /api/v1/campaigns/:campaign_id | Update campaign by ID | - |

## Metrics

The Metrics entity provides macro and historical performance data for campaigns.

| Endpoints | Description | Filters |
| --- | --- | --- |
| GET /api/v1/metrics/macro/campaigns | Get macro metrics | start_at, end_at, campaign_id, seller_id |
| GET /api/v1/metrics/history/campaigns | Get historical metrics | start_at, end_at, campaign_id, seller_id |

## Credits

The Credits entity manages advertiser account balances and transactions.

| Endpoints | Description | Filters |
| --- | --- | --- |
| GET /api/v1/checking_accounts | List advertiser credit accounts | seller_id, page, quantity |
| GET /api/v1/checking_accounts/:seller_id/transactions | List credits for an account | page, quantity |
| POST /api/v1/checking_accounts/:seller_id/transactions | Add credits to an account | - |

### Credit purchase with credit card/PIX

| Endpoints | Description | Filters |
| --- | --- | --- |
| GET /api/v1/payments | List payments | seller_id, page, quantity |
| POST /api/v1/payments/:payment_type | Create a new payment that will add credits | - |
| GET /api/v1/payments/:payment_id | Query a payment | - |

## SSO (VTEX Ads authentication)

The idea is that once the customer is connected to the marketplace platform, they can reuse this login to connect to the Retail Media platform.

> ⚠️ Any status other than 200 is considered an error.

### Login

Authentication uses a JWT token with a shared secret. The token must contain:

- `publisher_id`: Retailer ID in VTEX Ads.
- `seller_id`: Seller ID in the marketplace.
- `user_id`: User ID in the marketplace.
- 24h expiration time

```http
GET https://app.newtail.com.br/login/marketplace?sso=JWT
```

### User information query

The marketplace must provide an endpoint to query user information by user ID that returns the following fields:

- `name`
- `email`

```http
GET PREFIX/users/:user_id?seller_id&=publisher_id=
```

### Seller information query

The marketplace must provide an endpoint to query seller information that returns the following fields:

- `name`
- `cnpj` (tax ID)

```http
GET PREFIX/sellers/:seller_id?publisher_id=
```

## SSO v2 (VTEX Ads authentication)

SSO v2 allows retailers to send seller and user information to the VTEX Ads authentication API. VTEX Ads returns a redirect URL for the end user.

> ⚠️ Authentication follows the same model described in the [Authentication](#authentication) section.

```http
POST https://api-retail-media.newtail.com.br/sso/marketplace
```

### Request example

```json
{
  "seller_id": "xyz",
  "seller_name": "Seller Name",
  "user_email": "user@example.com",
  "user_name": "User Name"
}
```

### Response examples

**Success** - Status 200

```json
{
  "url_redirect": "https://app.newtail.com.br/login/marketplace?token=JWT"
}
```

**Failure**

* Status 400 - Validation error

    ```json
    {
      "message": "ValidationError",
      "errors": []
    }
    ```

* Status 500 - Internal application error

    ```json
    {
      "message": "InternalServerError"
    }
    ```
