---
title: "PowerReviews"
slug: "vtex-powerreviews"
excerpt: "vtex.powerreviews@2.4.0"
hidden: false
createdAt: "2020-06-03T15:19:08.947Z"
updatedAt: "2022-07-15T18:57:50.604Z"
---

The PowerReviews app provides a way to bring your PowerReviews content into your VTEX store. The app also implements the PowerReviews Checkout Beacon during checkout, sending customer purchase data to the PowerReviews platform.

## Configuration

Before you can start using the app, you will need an existing [PowerReviews](https://www.powerreviews.com/) account and API key.

### Step 1 - Defining the app settings

In your VTEX account's admin, perform the following actions:

1. Access the **Apps** section and then **My Apps**.
2. Select the **PowerReviews** app box.
3. Complete the following required fields in the Settings section:

- `App Key` - The API Key provided by PowerReviews.
- `Merchant ID` - Your unique PowerReviews merchant ID.
- `Merchant Group ID` - Your PowerReviews merchant group ID.
- `Client ID` - Your PowerReviews Client ID
- `Client Secret` - Your PowerReviews Client Secret
- `Send Email After Invoicing` - Instead of sending email after checkout, we can send email after an order has been invoiced. Enabling this disables purchase pixel's ability to track checkout
- `API Unique Id` - The product field used as the identifier (or pageId) on PowerReviews.

Optionally, the `Use Legacy Review Display Component` checkbox allows you to use the PowerReviews Review Display component instead of the VTEX Reviews component.

If needed, provide a URL path to a CSS stylesheet to override the styles of the PowerReviews Write-a-Review, Questions & Answers, or Review Display components.

### Step 2 - Update your store theme

1. Add the `powerreviews` app as a `peerDependency` in your theme's `manifest.json` file:

```diff
 "peerDependencies": {
+  "vtex.powerreviews": "2.x"
 }
```

2. If not already present, add the following to your theme's `dependencies`:

```json
 "vtex.product-review-interfaces": "1.x",
 "vtex.product-summary-context": "0.x",
 "vtex.product-context": "0.x",
 "vtex.store-header": "2.x",
 "vtex.pixel-interfaces": "1.x",
 "vtex.store-image": "0.x",
```

### Step 3 - Defining the app's blocks

The PowerReviews app integrates with the following store framework blocks.

| Block name                      | Description                                                                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `product-reviews`               | Display a paginated list of reviews for the product being viewed. This must be placed on the `store.product` page. |
| `product-rating-summary`        | Display the average rating for the product being viewed. This must be placed on the `store.product` page.          |
| `product-rating-inline`         | Display the average rating for the product being viewed, intended for use on the product shelf.                    |
| `product-review-form`           | Display the PowerReviews Write-a-Review form component. This must be placed on the `product-review-form` page.     |
| `product-questions-and-answers` | Display the PowerReviews Questions & Answers component for the product being viewed.                               |

An example of the blocks above in use:

```
 "store.product": {
   "blocks": [
     "product-rating-summary",
     "product-reviews",
     "product-questions-and-answers"
   ]
 }
```

```
 "store.product-review-form": {
   "blocks": [
     "product-review-form"
   ]
 }
```
