---
title: "Retrieving ads"
slug: "retrieving-ads"
excerpt: "Learn how to fetch relevant ads based on context like search terms, categories, or behavior."
hidden: false
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

The available ad formats are Sponsored Products (Product Ads) and Banner Banner / Display ads.

The `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-) endpoint can return both Product and Banner ad formats, using a unified query interface.

>ℹ️ This request has a 10-minute cache.

## Request

Learn more about each field on `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-).


## Response

The response will be a dictionary where each key is the name of a placement used in the query.

Learn more about each field on `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-).

Response example:

```json
{
    "placementName1": [
        {
            "ad_id": "8771ebf0-ca93-46c7-9a40-3071d93d5ebf",
            "media_url": "https://cdn.newtail.com.br/retail_media/ads/2023/05/11/6e70ebdf2aaadcd6b6b651b2360fa920-1280x256-red.png",
            "destination_url": null,
            "type": "banner",
            "seller_id": "37582",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/8771ebf0-ca93-46c7-9a40-3071d93d5ebf?publisher_id=3b7bcd3a-fde6-42d1-8de4-47a6e41a415a&ad_type=banner",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/8771ebf0-ca93-46c7-9a40-3071d93d5ebf?publisher_id=3b7bcd3a-fde6-42d1-8de4-47a6e41a415a&ad_type=banner",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/8771ebf0-ca93-46c7-9a40-3071d93d5ebf?publisher_id=3b7bcd3a-fde6-42d1-8de4-47a6e41a415a&ad_type=banner"
        }
    ],
    "placementName2": [
        {
            "ad_id": "c9483619-773d-450c-a1c8-5cbd31cd473e",
            "product_sku": "1547471458",
            "destination_url": "iphone-14-pro-apple-256gb-roxo-profundo-tela-de-61-quot-5g-camera-tripla-de-48mp-12mp-12mp/p/1547471458",
            "type": "product",
            "seller_id": "37582",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/c9483619-773d-450c-a1c8-5cbd31cd473e?publisher_id=3b7bcd3a-fde6-42d1-8de4-47a6e41a415a&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/c9483619-773d-450c-a1c8-5cbd31cd473e?publisher_id=3b7bcd3a-fde6-42d1-8de4-47a6e41a415a&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/c9483619-773d-450c-a1c8-5cbd31cd473e?publisher_id=3b7bcd3a-fde6-42d1-8de4-47a6e41a415a&ad_type=product"
        }
    ]
}
```

## Requesting ads - examples

Below are examples of Sponsored Product ad requests:

For the requests, the `publisher_id` needs to be entered. This will be provided by your account manager.

## Search context

```http
POST https://api.ads.vtex.com/v1/rma/:publisher_id HTTP/1.1
Content-Type: application/json

{
    "context": "search",
    "term": "desodorante",
    "user_id": "6a746448-cf59-42bc-aa3d-a426844ad115",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "tags": ["Mega Maio"],
    "placements": {
        "placementName1": { "quantity": 1, "size": "desktop", "types": ["banner"] },
        "placementName3": { "quantity": 3, "size": "mobile", "types": ["product", "banner"] },
        "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
    }
}
```

**Response:**

```json
{
    "placementName1": [
        {
            "ad_id": "6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce",
            "media_url": "https://cdn.newtail.com.br/retail_media/ads/2023/05/03/f97a938660e56fe38a9c9ade21c27df8-1280x256-red.png",
            "destination_url": null,
            "type": "banner",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner"
        }
    ],
    "placementName3": [
        {
            "ad_id": "c06ef1c5-f9bb-4f53-96c2-d53769a95b9b",
            "media_url": "https://cdn.newtail.com.br/retail_media/ads/2023/05/03/d51e784c8541780b2bb53543bebd7f02-375x172-red.png",
            "destination_url": null,
            "type": "banner",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/c06ef1c5-f9bb-4f53-96c2-d53769a95b9b?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/c06ef1c5-f9bb-4f53-96c2-d53769a95b9b?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/c06ef1c5-f9bb-4f53-96c2-d53769a95b9b?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner"
        },
        {
            "ad_id": "846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7",
            "product_sku": "10001236",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        },
        {
            "ad_id": "243ad5fe-53e1-4fc1-ac86-9f5286c48a8a",
            "product_sku": "104810",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        }
    ],
    "placementName2": [
        {
            "ad_id": "846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7",
            "product_sku": "10001236",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        },
        {
            "ad_id": "243ad5fe-53e1-4fc1-ac86-9f5286c48a8a",
            "product_sku": "104810",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        }
    ]
}
```

## Category context

```http
POST https://events-api.ads.vtex.com/v1/rma/:publisher_id HTTP/1.1
Content-Type: application/json

{
    "context": "category",
    "category_name": "Telefones e Celulares > Smartphones > iPhone",
    "user_id": "6a746448-cf59-42bc-aa3d-a426844ad115",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "placements": {
        "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
        "placementName3": { "quantity": 3, "size": "tamanho1", "types": ["product", "banner"] },
        "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
    }
}

```

## Brand context

```http
POST https://events-api.ads.vtex.com/v1/rma/:publisher_id HTTP/1.1
Content-Type: application/json

{
    "context": "brand",
    "brand_name": "iphone",
    "user_id": "6a746448-cf59-42bc-aa3d-a426844ad115",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "placements": {
        "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
        "placementName3": { "quantity": 3, "size": "tamanho1", "types": ["product", "banner"] },
        "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
    }
}

```

## Product details page (PDP) context

```http
POST https://events-api.ads.vtex.com/v1/rma/:publisher_id HTTP/1.1
Content-Type: application/json

{
  "context": "product_page",
  "product_sku": "120210",
  "product_attributes": {
    "category_name: "Telefones e Celulares > Smartphones > iPhone",
    "brand": "iphone"
  },
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499",
  "placements": {
    "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
    "placementName3": { "quantity": 3, "size": "tamanho1", "types": ["product", "banner"] },
    "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
  }
}
```

## Home context (no segmentation)

In the case of an untargeted context, such as Home, a list of ads will be displayed that are most relevant to that user_id. It's very important that we have a history and the correct user ID so that this context is more relevant.

```http
POST https://events-api.ads.vtex.com/v1/rma/:publisher_id HTTP/1.1
Content-Type: application/json

{
  "context": "home",
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499",
  "placements": {
    "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
    "placementName3": { "quantity": 3, "size": "tamanho1", "types": ["product", "banner"] },
    "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
  }
}
```

## Response to the sponsored products request

The results will be returned in the same order as the query. Thus, the first object in the returned list corresponds to the first object in the query list.

### Response

HTTP 200

```json
{
    "placementName1": [
        {
            "ad_id": "6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce",
            "media_url": "https://cdn.newtail.com.br/retail_media/ads/2023/05/03/f97a938660e56fe38a9c9ade21c27df8-1280x256-red.png",
            "destination_url": null,
            "type": "banner",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner"
        }
    ],
    "placementName3": [
        {
            "ad_id": "c06ef1c5-f9bb-4f53-96c2-d53769a95b9b",
            "media_url": "https://cdn.newtail.com.br/retail_media/ads/2023/05/03/d51e784c8541780b2bb53543bebd7f02-375x172-red.png",
            "destination_url": null,
            "type": "banner",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/c06ef1c5-f9bb-4f53-96c2-d53769a95b9b?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/c06ef1c5-f9bb-4f53-96c2-d53769a95b9b?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/c06ef1c5-f9bb-4f53-96c2-d53769a95b9b?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner"
        },
        {
            "ad_id": "846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7",
            "product_sku": "10001236",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        },
        {
            "ad_id": "243ad5fe-53e1-4fc1-ac86-9f5286c48a8a",
            "product_sku": "104810",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        }
    ],
    "placementName2": [
        {
            "ad_id": "846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7",
            "product_sku": "10001236",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/846fbf5e-6980-4a5e-a4a1-9b2a2dcbafb7?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        },
        {
            "ad_id": "243ad5fe-53e1-4fc1-ac86-9f5286c48a8a",
            "product_sku": "104810",
            "type": "product",
            "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product",
            "view_url": "https://events-api.ads.vtex.com/v1/beacon/view/243ad5fe-53e1-4fc1-ac86-9f5286c48a8a?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=product"
        }
    ]
}
```

## Sponsored brands

![](https://files.readme.io/5a547d7-image.png)

The "sponsored_brands" campaign has some differences related to its response.

**Request**

```json
{
    "context": "search",
    "term": "smartphone",
    "placements": {
        "placement_name": { "quantity": 1, "types": ["sponsored_brand"] }
    }
}
```

**Response**

> 🚧 All events must be triggered for the ad and its products.

| Attribute                        | Description                                                                                         | Type          |
|---------------------------------|-------------------------------------------------------------------------------------------------|---------------|
| `assets`                        | Address and type of the campaign's image/video. One or more assets will be returned.            | Array<Object> |
| `assets.#.type`                 | Indicates the type of asset.  <br><br>- image  <br>- video                                       | String        |
| `assets.#.url`                  | URL of the asset                                                                                  | String        |
| `assets.#.dimension`            | Dimension of the asset.  <br>Example: 720x480                                                     | String        |
| `logo_url`                      | URL of the brand logo image                                                                       | String        |
| `brand_name`                    | Brand name                                                                                       | String        |
| `headline`                     | Description of the ad title                                                                       | String        |
| `description`                   | Additional description of the ad                                                                  | String        |
| `impression_url`                | URL for the impression event                                                                      | String        |
| `view_url`                      | URL for the view event                                                                            | String        |
| `click_url`                    | URL for the click event                                                                           | String        |
| `products`                     | List of products                                                                                  | Array<Object> |
| `products.#.image_url`         | URL of the product image                                                                          | String        |
| `products.#.seller_id`         | Unique identifier of the seller                                                                   | String        |
| `products.#.product_metadata`  | Product metadata information (provided during product registration)                              | Object        |
| `products.#.product_name`      | Product name                                                                                    | String        |
| `products.#.product_sku`       | Product SKU                                                                                     | String        |
| `products.#.destination_url`   | URL of the product destination                                                                   | String        |
| `products.#.impression_url`    | URL for product impression                                                                        | String        |
| `products.#.view_url`          | URL for product view                                                                              | String        |
| `products.#.click_url`         | URL for the click event to be triggered when the end customer clicks on the product              | String        |

```json
{
    "placement_name": [
        {
            "type": "sponsored_brand",

            "assets": [
                {
                   "type": "image|video",
                   "url": "Image URL"
                }
            ],

            "brand_url": "https://cdn.newtail.com.br/retail_media/brands/logo.jpeg",
            "brand_name": "Apple",

            "destination_url": "https://www.extra.com.br/c?Filter=D70653",

            "headline": "Titanium. Very robust, very light, very pro!",
            "description": "",

            "view_url": "VIEW URL",
            "impression_url": "IMPRESSION URL",
            "click_url": "CLICK URL",

            "products": [
                {  
                    "image_url": "PRODUCT IMAGE URL",
                    "seller_id": null,
                    "product_metadata": { },
                    "product_name": "iPhone 15 Pro MAX",
                    "product_sku": "55064355",
                    "destination_url": "PRODUCT URL",
                    "impression_url": "IMPRESSION URL for a specific PRODUCT",
                    "view_url": "VIEW URL for a specific PRODUCT",
                    "click_url": "CLICK URL for a specific PRODUCT"
                }
            ]
        }
    ]
}
```
