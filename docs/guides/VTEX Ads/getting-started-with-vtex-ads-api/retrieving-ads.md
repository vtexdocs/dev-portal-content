---
title: "Retrieving ads"
slug: "retrieving-ads"
excerpt: "Learn how to fetch relevant ads based on context like search terms, categories, or behavior."
hidden: false
createdAt: "2025-05-21T13:27:20.000Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

The VTEX Ads API allows you to retrieve three types of ad formats:

- Sponsored products (Product ads)
- Sponsored brands
- Banner / Display ads

Use the `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-) endpoint to fetch both formats through a unified interface.

>ℹ️ Responses are cached for 10 minutes.

All ad requests require:

- A context (search, category, brand, product, or home)
- User identification (`user_id` and `session_id`)
- Placement configuration

Learn more about each field in the [API Reference](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-).

### Search context

Used when retrieving ads for search results pages.

```json
{
    "context": "search",
    "term": "desodorante",
    "user_id": "6a746448-cf59-42bc-aa3d-a426844ad115",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "tags": ["Mega Maio"],
    "placements": {
        "placementName1": { "quantity": 1, "size": "desktop", "types": ["banner"] },
        "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
    }
}
```

### Category context

Used for category pages.

```json
{
    "context": "category",
    "category_name": "Telefones e Celulares > Smartphones > iPhone",
    "user_id": "6a746448-cf59-42bc-aa3d-a426844ad115",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "placements": {
        "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
        "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
    }
}
```

### Brand context

Used for brand-specific pages.

```json
{
    "context": "brand",
    "brand_name": "iphone",
    "user_id": "6a746448-cf59-42bc-aa3d-a426844ad115",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "placements": {
        "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
        "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
    }
}
```

### Product context (PDP)

Used on product detail pages.

```json
{
  "context": "product_page",
  "product_sku": "120210",
  "product_attributes": {
    "category_name": "Telefones e Celulares > Smartphones > iPhone",
    "brand": "iphone"
  },
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499",
  "placements": {
    "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
    "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
  }
}
```

### Home context

Used for homepage or non-targeted contexts. Shows ads most relevant to the user based on their history.

```json
{
  "context": "home",
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499",
  "placements": {
    "placementName1": { "quantity": 1, "size": "tamanho1", "types": ["banner"] },
    "placementName2": { "quantity": 2, "size": "tamanho3", "types": ["product"] }
  }
}
```

## Response structure

>ℹ️ Successful responses return HTTP code 200.

The response is a dictionary where:

- Each key corresponds to a placement name from the request.
- Results maintain the same order as the query.
- Each ad includes tracking URLs for clicks, impressions and views.

### Standard ad response example

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
    ]
}
```

### Sponsored brands example

Sponsored brands campaigns have a different response format that includes brand information and related products.

> 🚧 All events must be triggered for both the ad and its products.

Request example:

```json
{
    "context": "search",
    "term": "smartphone",
    "placements": {
        "placement_name": { "quantity": 1, "types": ["sponsored_brand"] }
    }
}
```

Response example:

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