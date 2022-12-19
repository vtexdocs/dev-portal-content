---
title: "Yotpo Reviews Integration"
slug: "vtex-yotpo"
excerpt: "vtex.yotpo@1.2.1"
hidden: false
createdAt: "2020-06-03T15:19:16.340Z"
updatedAt: "2022-08-17T19:40:06.760Z"
---
The Yotpo Reviews Integration app is a product review and rating integration with [Yotpo](https://www.yotpo.com/).

![yotpo-app](https://user-images.githubusercontent.com/6306265/71126858-d7b64580-21b7-11ea-8d88-c8ef90b3ad41.png)

## Configuration

1. [Install](https://vtex.io/docs/recipes/store/installing-an-app) the `yotpo` app in the desired account;
2. In the admin's account, access **Apps** and then select the **Yotpo Integration** box;

![setup-yotpo](https://user-images.githubusercontent.com/6306265/71126888-e997e880-21b7-11ea-88da-287ab588d2a6.png)

3. Once in the app's page, define the app’s configurations in the **setup** section:

![setup-yotpo](https://user-images.githubusercontent.com/6306265/71126932-016f6c80-21b8-11ea-9af5-7f6da2b3ad9b.png)

- **Yotpo App Key**: Enter the app key that you have received from Yotpo's admin interface.
- **Use Reference Id**: Check this box if you wish to use the product's reference id rather than its product id to link the product to its reviews.

:warning: This app fills the standard VTEX review blocks with content using abstract interfaces from `vtex.product-review-interfaces` . The **VTEX review blocks** are:

- `"product-reviews"`: This block can be added to the product page (`store.product`). It renders the main Yotpo widget which lists any reviews or answered questions for the product being viewed as well as a form to add a new review or ask a new question.

- `"product-rating-summary"`: This block can be added to the product page (`store.product`) and renders the average rating for the product being viewed as well as the number of reviews that have been submitted.

- `"product-rating-inline"`: Similar to the previous block, but intended to be used in product shelves.

Additional **Yotpo review blocks** are:

- `"yotpo-all-reviews"`: This block can be added to a custom page (`store.custom`). It allows you to display all your site and product reviews in one page by rendering a [Yotpo widget](https://support.yotpo.com/en/article/generic-other-platforms-adding-yotpo-reviews-to-a-dedicated-page).

This app also includes a pixel integration to send order conversation tracking data to Yotpo.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles              |
| ------------------------ |
| `reviewsContainer`       |
| `ratingSummaryContainer` |
| `ratingInlineContainer`  |
| `allReviewsContainer`    |