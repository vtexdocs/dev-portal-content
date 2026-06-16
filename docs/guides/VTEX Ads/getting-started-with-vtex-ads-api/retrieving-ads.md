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

## Request best practices

- **HTTP persistence:** Prefer persistent connections (`Connection: keep-alive`).
- **Timeout:** Apply a 500–600 ms timeout to the ad query.

## Context and ad eligibility rules

>⚠️ It's not possible to filter by specific `placement`. Ad selection is based on `context` and request parameters.

Understanding which ad types are eligible for each context is crucial for setting up your ad requests correctly.

### Search context

Used when retrieving ads for search results pages.

Eligible ad types:

- **Banner/Video/Sponsored Brands Ads** that are **keyword-based**.
- **Sponsored Products** (any product campaign).

>⚠️ Keyword matching in the `search` context is exact (no stemming/synonyms). This means the advertiser must specify exactly which keywords they want to use in Banner/Video/Sponsored Brands campaigns. If a user searches for "nike shoes", the ad will only be eligible if the advertiser registered exactly the keyword "nike shoes". There is no approximate matching or similar word matching.

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

Eligible ad types:

- **Banner/Video/Sponsored Brands Ads** that use the corresponding **category**.
- **Sponsored Products** from the category.

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

Eligible ad types:

- **Banner/Video/Sponsored Brands Ads** for the brand.
- **Sponsored Products** from the brand.

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

Eligible ad types:

- **Sponsored Products** related to the viewed product.

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

Eligible ad types:

- **Banner/Video/Sponsored Brands Ads** that use **category** as a targeting criterion.
- **Sponsored Products**.

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
            "click_url": "https://events.newtail-media.newtail.com.br/v1/beacon/click/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "impression_url": "https://events.newtail-media.newtail.com.br/v1/beacon/impression/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner",
            "view_url": "https://events.newtail-media.newtail.com.br/v1/beacon/view/6d2d8837-bf5a-4ba4-90d2-5546cb18d5ce?publisher_id=0d675bf6-03f6-4b81-9617-e79dffddc3ab&ad_type=banner"
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

## Best practices

### Placement naming

Adopt a clear standard, such as `{channel}_{context}_{position}_{type}` (e.g., `msite_search_top-shelf_product`).

Examples:

- `site_home_middle_banner`
- `msite_product_top-shelf_product`
- `app_search_top-shelf_product`
- `site_category_bottom-shelf_banner`

### IAB standard image sizes

For banner-type ads, use images in the standard formats defined by the IAB (Interactive Advertising Bureau) to ensure compatibility and a better visual experience:

- **Medium Rectangle:** 300x250 pixels
- **Leaderboard:** 728x90 pixels
- **Wide Skyscraper:** 160x600 pixels
- **Mobile Leaderboard:** 320x50 pixels
- **Billboard:** 970x250 pixels
- **Half Page:** 300x600 pixels

### Video size options

For video ad requests, specify the size parameter to filter by video resolution:

- **1080p** (1920x1080 pixels) - Recommended only for full-screen videos
- **720p** (1280x720 pixels) - Recommended only for full-screen videos
- **480p** (854x480 pixels)
- **360p** (640x360 pixels)
- **320p** (568x320 pixels) - Recommended for mobile devices

>⚠️ Use only the resolution identifier (e.g., `"720p"`) in the size parameter, not the full dimensions.

## Ad targeting

Target ads to specific audiences to increase relevance by sending demographic or audience data directly in the body of the ad query using the `segmentation` field.

The `segmentation` field is an array of objects, where each object contains:

- `key`: The type of segmentation (e.g., "STATE", "CITY", "GENDER").
- `values`: Array of values for the segmentation.

### Segmentation example

```json
{
  "context": "search",
  "term": "smartphone",
  "segmentation": [
    {
      "key": "STATE",
      "values": ["CA"]
    },
    {
      "key": "CITY",
      "values": ["San Francisco"]
    },
    {
      "key": "GENDER",
      "values": ["M"]
    }
  ],
  "placements": {
    "site_search_top_product": {
      "quantity": 5,
      "types": ["product"]
    }
  }
}
```

**Available segmentation types:**

- `STATE` - User's state (e.g., "CA", "NY", "TX").
- `CITY` - User's city (e.g., "San Francisco", "New York").
- `GENDER` - User's gender (e.g., "M", "F").
- `AGE` - User's age (e.g., "22", "35").
- `AUDIENCES` - Custom audience (e.g., "high_value_customers", "cart_abandoners").
- `NBO_CATEGORIES` - Possible categories the user intends to buy (e.g., "Electronics", "Books").

## Response codes and errors

- **200 OK:** Query processed successfully (returns JSON per placement).
- **422 Unprocessable Entity:** Field validation error.
- **400 Bad Request / 404 Not Found:** Invalid request or resource not found.
- **429 Too Many Requests:** Rate limit exceeded.
- **5xx:** Internal errors.
