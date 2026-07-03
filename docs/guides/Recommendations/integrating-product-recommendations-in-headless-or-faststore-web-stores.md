---
title: "Integrating product recommendations in headless or FastStore web stores (Beta)"
slug: "integrating-product-recommendations-in-headless-or-faststore-web-stores"
hidden: false
excerpt: "Learn how to integrate product recommendations in headless and FastStore web storefronts using the Recommendations BFF API and Activity Flow."
createdAt: "2026-05-15T12:00:00.000Z"
updatedAt: "2026-05-15T12:00:00.000Z"
---

> ℹ️ This feature is in beta, and we're actively working to improve it. If you have questions about enablement, account configuration, or campaigns, contact [our Support](https://help.vtex.com/en/support).

This guide explains how to integrate [product recommendations](https://help.vtex.com/en/docs/tutorials/product-recommendations-beta) in headless or FastStore web stores using the VTEX [Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api).

![shelf-recommendation](https://vtexhelp.vtexassets.com/assets/docs/src/shelf-recommendation___403f15739cf14318a5b9ad8f16582d71.gif)

> ℹ️ For mobile apps, see [Integrating product recommendations in mobile stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-mobile-stores).

## Before you begin

Before implementing recommendations in a headless or FastStore web store, make sure you have:

* A headless or FastStore web frontend capable of making authenticated HTTPS requests.
* Requested and received approval for the product recommendations feature for the account.
* Recommendation campaigns created and their respective VRNs.
* Automatic cart and order event capture through [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow) configured for your headless or FastStore web store. For custom headless web storefronts, follow [Installing Activity Flow in headless stores](https://developers.vtex.com/docs/guides/installing-activity-flow-in-headless-stores). FastStore includes Activity Flow natively.

## Step 1: Initial setup

After the feature is approved, the VTEX team prepares the recommendations environment for the account. This setup includes:

* Creating and configuring the recommendations workspace.
* Synchronizing the product catalog with the recommendation service.
* Configuring the access credentials used by the integration.
* Configuring automatic cart and order event capture for your headless or FastStore web store through [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow).

* Cart events, such as `add_to_cart` and `remove_from_cart`, are consumed from the Data Layer and sent to the recommendations platform.
* Completed orders are automatically processed and transformed into transactions used to train and improve the models.
* When the order contains the recommendations identifier saved in the orderForm, the purchase can be associated with the user who browsed the store anonymously.

Once these configurations are complete, you can proceed with the implementation steps below.

## Step 2: Start the user session

Your headless or FastStore web store must call the `POST` [Start session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/users/start-session) endpoint.

This endpoint starts or updates the user's recommendations session. It associates the `userId` used during browsing with the current `orderFormId`, stores this identifier in the orderForm custom data, and returns the `recommendationsUserId` that must be used in subsequent requests.

> ℹ️ Sending `orderFormId` in the JSON body is optional for web storefronts when the request forwards the `checkout.vtex.com` cookie: the API can resolve the order form from that cookie when it isn't in the body. If the client can't send cookies (for example, some server-only calls), include `orderFormId` in the body manually. For FastStore, the recommended approach is to forward cookies on the `start-session` request.

Call `POST` [Start session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/users/start-session):

* On the first session load where an order form is available (via the request body or the `checkout.vtex.com` cookie).
* Every time the `vtex-rec-user-start-session` cookie expires.

The endpoint also sets the `vtex-rec-user-id` cookie with the returned `recommendationsUserId`, and the `vtex-rec-user-start-session` cookie, which controls when a new `start-session` call must be made. The `recommendationsUserId` must be sent as `userId` in recommendation and event endpoints.

`start-session` is important because it allows navigation and interaction events collected during the session to be linked later to the completed purchase. When the order is processed, the service uses the `recommendationsUserId` saved in the orderForm to associate the anonymous browsing behavior with the VTEX user who completed the purchase.

**Request example with `checkout.vtex.com` cookie**:

When the request includes the shopper's `checkout.vtex.com` cookie, you can omit the JSON body. That applies to FastStore and to headless storefronts that forward the browser's checkout cookies.

In tools like `curl`, explicitly pass that cookie, as in the example below. In the browser, it's forwarded automatically. The cookie value includes the cart identifier (for example, `_ofid` and the `orderFormId`), as described in [Get cart information by ID](https://developers.vtex.com/docs/guides/get-cart-information-by-id).

In tools like `curl`, explicitly pass that cookie, as shown below. In the browser, it's forwarded automatically. The cookie value includes the cart identifier, for example, `_ofid={orderFormId}`, as described in [Get cart information by ID](https://developers.vtex.com/docs/guides/get-cart-information-by-id).

```bash
curl --request POST \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/users/start-session?an=apiexamples' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'host: apiexamples.vtexcommercestable.com.br' \
  --header 'x-forwarded-host: www.apiexamples.com' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x' \
  --cookie 'checkout.vtex.com=_ofid=d761924de4254f6883a8ec2e9a28597d'
```

**Request example with `orderFormId`**:

When the request can't send checkout cookies (for example, some server-side calls), include `orderFormId` in the body.

```bash
curl --request POST \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/users/start-session?an=apiexamples' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'host: apiexamples.vtexcommercestable.com.br' \
  --header 'x-forwarded-host: www.apiexamples.com' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x' \
  --data '{"orderFormId":"d761924de4254f6883a8ec2e9a28597d"}'
```

**Response example**:

```json
{
  "recommendationsUserId": "198e0f50-acf8-42f7-998a-5cd125464749"
}
```

The returned `recommendationsUserId` is the same value persisted in the `vtex-rec-user-id` cookie. The endpoint also sets the `vtex-rec-user-start-session` cookie.

## Step 3: Implement the recommendation flow

To display recommendations in your headless or FastStore web store:

1. Start the session by calling `POST` [Start session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/users/start-session).
2. Use the returned `recommendationsUserId`, which is the same value stored in the `vtex-rec-user-id` cookie, while the `vtex-rec-user-start-session` cookie is valid.
3. Fetch recommendations for each shelf using the campaign VRN.
4. Render the returned products.

### Fetch recommendations

Use the `GET` [Fetch recommendations](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#get-/api/recommend-bff/v2/recommendations) endpoint whenever a page contains a recommendation shelf.

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

```bash
curl --request GET \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/recommendations?an=apiexamples&campaignVrn=vrn%3Arecommendations%3Aapiexamples%3Arec-top-items-v2%3A123e4567-e89b-12d3-a456-426614174000&userId=198e0f50-acf8-42f7-998a-5cd125464749&salesChannel=1&locale=en-US' \
  --header 'Accept: application/json' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x'
```

For campaigns that require product context, include `products`:

```bash
curl --request GET \
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

## Step 4: Track product view events

To measure performance and improve recommendations, your headless or FastStore web store must send `product-view` events when the user opens a product detail page.

> ⚠️ For accurate tracking, ensure that you always use the same session `recommendationsUserId` in the `userId` field.

Use the `POST` [Product view](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/events/product-view) endpoint when the user views a product detail page.

**Request example**:

```curl
curl --request POST \
  --url 'https://api.vtexcommercestable.com.br/api/recommend-bff/v2/events/product-view?an=apiexamples' \
  --header 'Content-Type: application/json' \
  --header 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  --header 'x-vtex-rec-origin: apiexamples/storefront/vtex.recommendation-shelf@2.x' \
  --data '{
    "userId": "198e0f50-acf8-42f7-998a-5cd125464749",
    "product": "1234",
    "source": "WEB_DESKTOP"
  }'
```

The response returns `202 Accepted`.

The `source` field accepts values, such as `WEB_DESKTOP` and `WEB_MOBILE`. When `source` isn't sent, the BFF tries to infer the value from the `user-agent`.

## Step 5: Configure shelf event tracking through Activity Flow

Recommendation shelf view events and recommended product click events are automatically captured through [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow).

To capture view events, render the following attributes on the recommendation shelf parent container:

```jsx
<div
  data-af-element="recommendation-shelf"
  data-af-onimpression={shouldAddAFAttr}
  data-af-onview={shouldAddAFAttr}
  data-af-correlation-id={shouldAddAFAttr && correlationId}
  data-af-campaign-id={shouldAddAFAttr && campaignId}
  data-af-products={shouldAddAFAttr && productIds}
>
  {/* Recommendation shelf products */}
</div>
```

To capture click events, render the following attributes on each product in the recommendation shelf:

```jsx
<div
  data-af-element="recommendation-shelf-product"
  data-af-correlation-id={correlationId}
  data-af-campaign-id={campaignId}
  data-af-product-id={product?.productId}
  data-af-onclick={!!product?.productId}
  data-af-product-position={(index ?? 0) + 1}
>
  {/* Product card content */}
</div>
```

Use the `correlationId` returned in the recommendation response, the `campaignId` returned in `campaign.id`, and the list of rendered product IDs in `productIds`.

**Implementation example**:

```html
<div class="recommendations-embedded-shelf">
  <div
    class="recommendationShelfContainer"
    data-af-element="recommendation-shelf"
    data-af-onimpression="true"
    data-af-onview="true"
    data-af-correlation-id="d2e8c706-e67c-45d7-8de9-b80976960f89"
    data-af-campaign-id="ca2acae8-41a4-4bcd-9ffd-0ac40b7c0a57"
    data-af-products="14,12"
  >
    <div class="rs-title">Complementary products</div>
    <div class="rs-track">
      <div
        class="rs-card"
        data-af-element="recommendation-shelf-product"
        data-af-correlation-id="d2e8c706-e67c-45d7-8de9-b80976960f89"
        data-af-campaign-id="ca2acae8-41a4-4bcd-9ffd-0ac40b7c0a57"
        data-af-product-id="14"
        data-af-onclick="true"
        data-af-product-position="1"
      >
        <img class="rs-card-img" alt="" loading="lazy" src="https://biggy.vtexassets.com/arquivos/ids/155412/images.png?v=637528820142830000">
        <a class="rs-card-name" href="/standard-sunglasses/p">Standard Sunglasses</a>
        <div class="rs-card-price">$330.00</div>
        <button type="button" class="rs-btn-add">Add to cart</button>
      </div>

      <div
        class="rs-card"
        data-af-element="recommendation-shelf-product"
        data-af-correlation-id="d2e8c706-e67c-45d7-8de9-b80976960f89"
        data-af-campaign-id="ca2acae8-41a4-4bcd-9ffd-0ac40b7c0a57"
        data-af-product-id="12"
        data-af-onclick="true"
        data-af-product-position="2"
      >
        <img class="rs-card-img" alt="" loading="lazy" src="https://biggy.vtexassets.com/arquivos/ids/155410/mochila-para-trilha-thule-alltrail-25l-masc-01.jpg?v=637528813555100000">
        <a class="rs-card-name" href="/trail-backpack/p">Trail Backpack</a>
        <div class="rs-card-price">$121.00</div>
        <button type="button" class="rs-btn-add">Add to cart</button>
      </div>
    </div>
  </div>
</div>
```
