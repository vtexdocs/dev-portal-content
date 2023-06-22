---
title: "Allow manual prices on VTEX Sales App"
slug: "allow-manual-prices-on-vtex-sales-app"
hidden: false
createdAt: "2022-01-10T13:45:56.934Z"
updatedAt: "2022-04-28T23:00:12.510Z"
---

The manual prices feature allows VTEX Sales App sales associates to change prices directly on the product page on inStore and in the shopping cart on the ecommerce website.

## Configuration

To make this feature available to sales associates using VTEX Sales App, it is necessary to enable it using the Checkout API. You must place a request to the [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration) endpoint, setting the `allowManualPrice` property to `true`.

> ❗ This configuration also changes the behavior of the ecommerce, allowing any user with a role that contains the **Telesales** resource to insert manual prices in the ecommerce shopping cart, as described in the [Telesales features](https://help.vtex.com/en/tutorial/telesales-features--UqhiccIRIK2KD0OqkzJaS#manual-pricing) article on VTEX Help Center.

Since VTEX Sales App sales associates are automatically created with the VTEX Sales App Salesperson role, as explained in [Managing physical stores and sales reps on VTEX Sales App](https://help.vtex.com/en/tracks/vtex-sales-app-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc/5PSjRstg7UU4lOm0s8aqKN), they already have the **Telesales** resource associated with their account. This means that once the configuration is enabled on the Checkout API, they will automatically be able to edit prices on VTEX Sales App or in the ecommerce shopping cart.

## Usage

After enabling manual prices, to change a product price on VTEX Sales App, sales associates can follow the steps below.

1. On VTEX Sales App, search for any product using the search bar.
2. Click on `More details`.
3. Click on the desired variation of the product.
4. Click on `Change`, an option that will appear next to the product price. When you click this component, you will see a modal that allows you to set a new price, as shown below.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/allow-manual-prices-on-instore-0.png)
5. Enter a new value to change the product price. There are no restrictions to increase or reduce prices.
6. Click on `Change price` to confirm. The altered price will be applied only on this purchase.

After that, they can proceed with the remaining steps to place the order.
