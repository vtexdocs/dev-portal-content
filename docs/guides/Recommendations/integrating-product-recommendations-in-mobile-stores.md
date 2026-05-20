---
title: "Integrating product recommendations in mobile stores (Beta)"
slug: "integrating-product-recommendations-in-mobile-stores"
hidden: false
excerpt: "Learn how to integrate product recommendations in mobile apps using the Recommendations BFF API."
createdAt: "2026-05-15T12:00:00.000Z"
updatedAt: "2026-05-15T12:00:00.000Z"
---

> ℹ️ This feature is in beta, and we are actively working to improve it. If you have questions about enablement, account configuration, or campaigns, please contact [our Support](https://help.vtex.com/en/support).

This guide explains how to integrate [product recommendations](https://help.vtex.com/tutorial/product-recommendations-beta--2QIexbD2FSXBxELUnFtg7g) in mobile stores using the VTEX [Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api).

> ℹ️ For web storefronts, see [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores).

## Before you begin

Before implementing recommendations in a mobile store, make sure you have:

* A mobile app capable of making authenticated HTTPS requests.
* Requested and received approval for the product recommendations feature for the account.
* Recommendation campaigns created and their respective VRNs.
* Automatic cart and order event capture configured for the mobile store. To set this up, see [Installing Activity Flow in mobile apps](https://developers.vtex.com/docs/guides/installing-activity-flow-in-mobile-apps) and [VTEX Activity Flow](https://developers.vtex.com/docs/guides/activity-flow).

## Step 1: Initial setup

After the feature is approved, the VTEX team prepares the recommendations environment for the account. This setup includes:

* Creating and configuring the recommendations workspace.
* Synchronizing the product catalog with the recommendation service.
* Configuring the access credentials used by the integration.
* Completed orders are automatically processed and transformed into transactions used to train and improve the models.
* When the order contains the recommendations identifier saved in the orderForm, the purchase can be associated with the user who browsed the store anonymously.

Once these configurations are complete, you can proceed with the implementation steps below.

## Step 2: Start the user session

The mobile store must call the `POST` [Start session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/users/start-session) endpoint.

This endpoint starts or updates the user's recommendations session. It associates the `userId` used during browsing with the current `orderFormId`, saves this identifier in the orderForm custom data, and returns the `recommendationsUserId` that must be used in subsequent requests.

In mobile integrations, `userId` and `orderFormId` are required in the `start-session` request body.

Call `POST` [Start session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/users/start-session):

* On the first session load where an `orderFormId` exists.
* Every time the `orderFormId` changes.

The endpoint also sets the `vtex-rec-user-id` cookie with the returned `recommendationsUserId`. The `recommendationsUserId` must be sent as `userId` in recommendation and event endpoints.

In mobile integrations, make sure the HTTP client preserves the cookies returned by the endpoint or stores the required values so they can be reused in subsequent calls.

`start-session` is important because it allows navigation and interaction events collected during the session to be linked later to the completed purchase. When the order is processed, the service uses the `recommendationsUserId` saved in the orderForm to associate the anonymous browsing behavior with the VTEX user who completed the purchase.

**Request example**:

```curl
curl --request post \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/users/start-session?an=apiexamples' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'host: apiexamples.vtexcommercestable.com.br' \
  --header 'x-forwarded-host: www.apiexamples.com' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x' \
  --data '{
    "orderFormId": "d761924de4254f6883a8ec2e9a28597d",
    "userId": "198e0f50-acf8-42f7-998a-5cd125464749"
  }'
```

**Response example**:

```json
{
  "recommendationsUserId": "198e0f50-acf8-42f7-998a-5cd125464749"
}
```

The returned `recommendationsUserId` is the same value persisted in the `vtex-rec-user-id` cookie.

## Step 3: Implement the recommendation flow

To display recommendations in the mobile store:

1. Start the session by calling `POST` [Start session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/users/start-session).
2. Use the returned `recommendationsUserId`, which is the same value stored in the `vtex-rec-user-id` cookie, while the `vtex-rec-user-start-session` cookie is valid.
3. Fetch recommendations for each shelf using the campaign VRN.
4. Render the returned products.

### Fetch recommendations

Use the `GET` [Fetch recommendations](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#get-/api/recommend-bff/v2/recommendations) endpoint whenever a screen contains a recommendation shelf.

The `campaignVrn` is the VRN (Virtual Resource Name) that identifies the recommendation strategy. It follows the `vrn:recommendations:{store-name}:{campaignType}:{campaignId}` format.

The full VRN can be obtained through [our Support](https://help.vtex.com/en/support) or from the store Admin in **Storefront > Recommendations**. In the shelf list, click the three dots on the right side of the shelf and then click **Copy ID**.

Available campaign types:

* `rec-top-items-v2`: Best Sellers
* `rec-persona-v2`: For You
* `rec-similar-v2`: Similar Products
* `rec-cross-v2`: Who Viewed Also Bought
* `rec-cross-v2`: Buy Together
* `rec-last-v2`: Recently Viewed
* `rec-visual-v2`: Visually Similar Products
* `rec-search-v2`: Manual collection or search
* `rec-next-v2`: Next Interaction

Main parameters:

* `an`: VTEX account name.
* `campaignVrn`: Campaign VRN.
* `userId`: `recommendationsUserId` returned by `start-session`.
* `products`: Comma-separated product IDs. Required for contextual campaigns, such as similar products, who viewed also bought, visually similar products, next interaction, and cart recommendations.
* `salesChannel`: Store sales channel.
* `locale`: User locale, for example `en-US`.

**Request example**:

```curl
curl --request GET \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/recommendations?an=apiexamples&campaignVrn=vrn%3Arecommendations%3Aapiexamples%3Arec-top-items-v2%3A123e4567-e89b-12d3-a456-426614174000&userId=198e0f50-acf8-42f7-998a-5cd125464749&salesChannel=1&locale=en-US' \
  --header 'Accept: application/json' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x'
```

For campaigns that require product context, include `products`:

```curl
curl --request get \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/recommendations?an=apiexamples&campaignVrn=vrn%3Arecommendations%3Aapiexamples%3Arec-similar-v2%3A123e4567-e89b-12d3-a456-426614174000&userId=198e0f50-acf8-42f7-998a-5cd125464749&products=product-id-1&salesChannel=1&locale=en-US' \
  --header 'Accept: application/json' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x'
```

**Response example**:

```json
{
  "products": [
    {
      "brand": "Mizuno",
      "productId": "14",
      "productName": "Standard Sunglasses",
      "link": "/standard-sunglasses/p",
      "items": [
        {
          "itemId": "31",
          "nameComplete": "Standard Sunglasses",
          "images": [
            {
              "imageUrl": "https://biggy.vtexassets.com/arquivos/ids/155412/images.png?v=637528820142830000"
            }
          ],
          "sellers": [
            {
              "sellerId": "1",
              "commertialOffer": {
                "Price": 330,
                "ListPrice": 330,
                "AvailableQuantity": 10000
              }
            }
          ]
        }
      ]
    },
    {
      "brand": "Google",
      "productId": "12",
      "productName": "Trail Backpack",
      "link": "/trail-backpack/p",
      "tags": ["advertisement"],
      "items": [
        {
          "itemId": "29",
          "nameComplete": "Trail Backpack - variant 2",
          "images": [
            {
              "imageUrl": "https://biggy.vtexassets.com/arquivos/ids/155410/mochila-para-trilha-thule-alltrail-25l-masc-01.jpg?v=637528813555100000"
            }
          ],
          "sellers": [
            {
              "sellerId": "1",
              "commertialOffer": {
                "Price": 121,
                "ListPrice": 121,
                "AvailableQuantity": 10000
              }
            }
          ]
        }
      ]
    }
  ],
  "correlationId": "d2e8c706-e67c-45d7-8de9-b80976960f89",
  "campaign": {
    "id": "ca2acae8-41a4-4bcd-9ffd-0ac40b7c0a57",
    "title": "Complementary products",
    "type": "CROSS_SELL"
  }
}
```

> ℹ️ When the shelf returns a sponsored product, the product will be marked with the `advertisement` tag. In this case, render the card with a sponsored label.

Render the returned products as product cards on the shelf.

## Step 4: Track recommendation events through the API

To measure performance and improve recommendations in mobile, the store must send three event types through the API:

* `recommendation-view`: when the recommendation shelf enters the viewport.
* `recommendation-click`: when the user clicks a recommended product.
* `product-view`: when the user opens a product detail page.

For accurate tracking, ensure that:

* All events include the same session `recommendationsUserId` in the `userId` field.
* You send `recommendation-view` only when the shelf becomes visible, for example, when at least 50% of the shelf is visible for 1 second.
* Events are properly debounced to prevent duplicates.
* View and click events include the `correlationId` returned by the recommendation request.
* You send `campaignId` when available; it is returned in `campaign.id`.

### Recommendation views

Use the `POST` [Recommendation view](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/events/recommendation-view) endpoint when a shelf enters the viewport.

**Request example**:

```curl
curl --request post \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/events/recommendation-view?an=apiexamples' \
  --header 'Content-Type: application/json' \
  --data '{
    "userId": "198e0f50-acf8-42f7-998a-5cd125464749",
    "correlationId": "d2e8c706-e67c-45d7-8de9-b80976960f89",
    "products": ["14", "12"],
    "campaignId": "ca2acae8-41a4-4bcd-9ffd-0ac40b7c0a57"
  }'
```

The response returns `202 Accepted`.

### Recommendation clicks

Use the `POST` [Recommendation click](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/events/recommendation-click) endpoint when the user clicks a recommended product.

**Request example**:

```curl
curl --request post \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/events/recommendation-click?an=apiexamples' \
  --header 'Content-Type: application/json' \
  --data '{
    "userId": "198e0f50-acf8-42f7-998a-5cd125464749",
    "correlationId": "d2e8c706-e67c-45d7-8de9-b80976960f89",
    "product": "14",
    "campaignId": "ca2acae8-41a4-4bcd-9ffd-0ac40b7c0a57"
  }'
```

The response returns `202 Accepted`.

### Product views

Use the `POST` [Product view](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/events/product-view) endpoint when the user views a product detail page.

**Request example**:

```curl
curl --request post \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/events/product-view?an=apiexamples' \
  --header 'Content-Type: application/json' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x' \
  --data '{
    "userId": "198e0f50-acf8-42f7-998a-5cd125464749",
    "product": "14",
    "source": "WEB_MOBILE"
  }'
```

The response returns `202 Accepted`.

The `source` field accepts values such as `WEB_DESKTOP` and `WEB_MOBILE`. For mobile integrations, send `WEB_MOBILE`.
