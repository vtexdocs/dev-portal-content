---
title: "Integrating product recommendations in headless stores (Beta)"
slug: "integrating-product-recommendations-in-headless-stores"
hidden: false
excerpt: "Learn how to integrate product recommendations in headless stores."
createdAt: "2025-10-23T12:00:00.000Z"
updatedAt: "2025-10-23T12:00:00.000Z"
---

> ℹ️ This feature is in beta, and we are actively working to improve it. If you have any questions, please contact [our Support](https://help.vtex.com/en/support).

This guide describes how to integrate [product recommendations](https://help.vtex.com/tutorial/product-recommendations-beta--2QIexbD2FSXBxELUnFtg7g) to headless stores using the VTEX [Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api).

## Before you begin

Before implementing headless recommendations, make sure you have:

* A frontend capable of adding third-party scripts and making authenticated HTTPS requests
* Requested and received approval for the product recommendations feature setup from [VTEX Support](https://help.vtex.com/support).

## Step 1: Initial setup

After you request and receive approval for using the product recommendations feature, the [VTEX Support](https://help.vtex.com/support) team will prepare your environment by:

* Creating a workspace for recommendations
* Synchronizing your product catalog with the recommendation service
* Setting up API keys for secure access
* Generating a custom integration script for your store.

Once these configurations are complete, you can proceed with the implementation steps below.

## Step 2: Script implementation in the store

After receiving the integration script from VTEX Support, implement it in your headless store:

1. Create a dedicated component or module in your codebase for third-party integrations.
2. Implement the script based on your framework's best practices for third-party script management. Check an example of implementation in [FastStore: Third-party Scripts](https://developers.vtex.com/docs/guides/faststore/storefront-features-handling-third-party-scripts)
3. Ensure the script runs on all pages where you want to enable recommendations or track user behavior.

  The script handles:
    * User tracking initialization
    * Browsing and behavioral data collection
    * Model training data gathering.

4. Save the `_snrs_uuid` in the user's order form, so that when the order is placed, you can associate that sale with the user identified during navigation.

  When the ID is generated, you must save the user's ID in the orderForm during navigation using `PUT` [Set multiple custom field values](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orderForm/-orderFormId-/customData/-appId-) as shown below:

   ```javascript
   fetch(`/api/checkout/pub/orderForm/${orderForm.id}/customData/synerise`, {
       method: 'PUT',
       body: JSON.stringify({
         uuid: snrsUuidCookie,
         source: isMobile() ? 'WEB_MOBILE' : 'WEB_DESKTOP',
       }),
   })
   ```

  To validate that it worked, request to retrieve the orderForm using `GET` [Get current cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm). The `customData` field returned should contain the added information.

5. Send the `POST` [Product View](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/events/product-view/v2) event following the API reference.

## Step 3: Model training and configuration

Once the tracking script collects enough browsing data, the VTEX Support team will train and configure the recommendation models. The available strategies are:

| Name | Description |
| :---- | :---- |
| Best sellers | Returns the top-selling or most popular items in the store. |
| Recommended for you | Provides recommendations tailored to the user's profile and behavior. |
| Similar products | Returns items similar to a specified product. |
| Buy together | Suggests complementary items to a specified product. |
| Recently viewed | Returns the most recently viewed products for the given user. |
| Visually similar products | Returns visually similar items to a specified product. |
| Manual collection | Returns recommendations from a collection defined manually. |
| Next interaction | Predicts and suggests products the user is likely to interact with next. |

After the models are trained, they will be available for API-based recommendation displays in your store.

## Step 4: Product recommendations implementation flow

To implement product recommendations in your headless store, follow these steps:

1. [Start a user session to get a unique identifier](#starting-the-user-session)
2. [Fetch recommendations for your shelves](#implementing-recommendation-shelves).
3. [Track user interactions with the recommendations](#tracking-recommendation-events).

> ⚠️ Use the same user identifier (`recommendationsUserId`) across all requests in a session.

### Starting the user session

Use the `POST` [Start Session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/users/start-session/v2) endpoint to create a unique user ID for recommendations. This endpoint:

* Creates a unique user ID (`recommendationsUserId`) for the session.
* Links it to the provided order form ID.
* Stores the ID in the `vtex-rec-user-id` cookie for session continuity.
* Initializes recommendation tracking and personalization.

> ℹ️ Call this endpoint on the first page view of each visit, before displaying any recommendations, and only if the `_snrs_uuid` is not already present. If `orderFormId` is not provided in the request body, the API attempts to retrieve it from the `checkout.vtex.com` cookie.

**Request example**:

```curl
curl --request post \
  --url https://api.vtexcommercestable.com.br/api/recommend-bff/v2/users/start-session \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'host: apiexamples.vtexcommercestable.com.br' \
  --header 'x-forwarded-host: www.apixamples.com' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x' \
  --data '{"orderFormId":"d761924de4254f6883a8ec2e9a28597d"}'
```

**Response example**:

```json
{
  "recommendationsUserId": "198e0f50-acf8-42f7-998a-5cd125464749"
}
```

Persist the returned `recommendationsUserId` as `_snrs_uuid` and include it in all subsequent requests.

### Implementing recommendation shelves

Use the `GET` [Fetch recommendations](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#get-/api/recommend-bff/recommendations/v2) endpoint to fetch products for each shelf whenever a page contains a recommendation component (homepage, PDP, cart, PLP, etc.).

The campaign determines the type of recommendations returned, such as personalized recommendations, similar items, cross-sell, and others.

This endpoint retrieves a list of recommended products based on:

* Campaign VRN (Virtual Resource Name) identifying the recommendation strategy. The VRN follows the pattern `vrn:recommendations:{store-name}:{campaignType}:{campaignId}`. Contact [our Support](https://help.vtex.com/en/support) to obtain the `campaignId`

  Available campaign types:

  * `rec-top-items-v2`: Best sellers
  * `rec-persona-v2`: Personalized recommendations
  * `rec-similar-v2`: Similar items
  * `rec-cross-v2`: Cross-sell
  * `rec-cart-v2`: Cart-based recommendations
  * `rec-last-v2`: Last seen
  * `rec-interactions-v2`: Recent interactions
  * `rec-visual-v2`: Visual similarity
  * `rec-search-v2`: Search-based recommendations
  * `rec-next-v2`: Next interaction

* User context (from `recommendationsUserId`)
* Page context (product ID, cart items, etc.).

**Request example**:

```curl
curl --request get \
 --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/recommendations?an=apiexamples&campaignVrn=vrn%3Arecommendations%3Aapiexamples%3Arec-top-items-v2%3A123e4567-e89b-12d3-a456-426614174000&userId=198e0f50-acf8-42f7-998a-5cd125464749&products=product-id-1%2Cproduct-id-2%2Cproduct-id-3&salesChannel=1&locale=en-US' \
 --header 'Accept: application/json' \
 --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x'
```

**Response example**:

```json
{
  "products": [
    "1234",
    "5678",
    "91011"
  ],
  "correlationId": "rec-123e4567-e89b-12d3-a456-426614174000",
  "campaign": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "title": "Most Popular Items",
    "type": "TOP_ITEMS"
  }
}
```

Render the returned items as product cards on the shelf. After rendering, proceed to event tracking.

### Tracking recommendation events

To improve recommendation accuracy and measure effectiveness, you need to track how users interact with the recommended products. There are three types of events to track:

* [Recommendation views](#recommendation-views): When recommendation shelves become visible to users.
* [Recommendation clicks](#recommendation-clicks): When users click recommended products.
* [Product views](#product-views): When users visit product detail pages.

⚠️ For accurate tracking, ensure that:

* All events include the same `recommendationsUserId`.
* Events are properly debounced to prevent duplicates.
* View events are triggered only when shelves enter the viewport.

#### Recommendation views

Use the `POST` [Recommendation view](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/events/recommendation-view/v2) endpoint when a recommendation shelf becomes visible. This endpoint:

* Records when recommendations are shown to users.
* Provides data for click-through rate (CTR) analysis.
* Helps train and improve recommendation models.
* Should be called when shelves enter the viewport.

**Request example**:

```curl
curl --request post \
 --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/events/recommendation-view?an=apiexamples' \
 --header 'Content-Type: application/json' \
 --data '{"userId":"user-id","correlationId":"correlation-id--from-recommendation-request","products":["product-id-1","product-id-2","product-id-3"]}'
```

#### Recommendation clicks

Use the `POST` [Recommendation click](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/events/recommendation-click/v2) endpoint when users interact with recommended products. This endpoint tracks user engagement with recommendations and should be called for each click on a product card.

**Request example**:

```curl
curl --request post \
 --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/events/recommendation-click?an=apiexamples' \
 --header 'Content-Type: application/json' \
 --data '{"userId":"user-id","correlationId":"correlation-id--from-recommendation-request","product":"product-id"}'
```

#### Product views

Use the `POST` [Product View](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/events/product-view/v2) endpoint when users view product details. This endpoint tracks all product detail page views.

⚠️ VTEX automatically tracks product views once the Recommendations feature is set up in your store’s website as instructed in [Step 2](#step-2-script-implementation-in-the-store). This event is only required for app implementations or other channels. Track product views for all sources to ensure comprehensive data collection for the recommendation models.

**Request example**:

```curl
curl --request post \
 --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/events/product-view?an=apiexamples' \
 --header 'Content-Type: application/json' \
 --header 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
 --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x' \
 --data '{"userId":"user-id","product":"product-id-1","source":"WEB_DESKTOP"}'
```

## Learn more

* [Recommendations BFF API Reference](https://developers.vtex.com/docs/api-reference/recommendations-bff-api)
* [Product Recommendations Overview](https://help.vtex.com/tutorial/product-recommendations-beta--2QIexbD2FSXBxELUnFtg7g)
