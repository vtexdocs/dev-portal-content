---
title: "Enable the Manual Price"
slug: "enable-the-manual-price"
hidden: false
createdAt: "2022-05-23T20:17:42.865Z"
updatedAt: "2022-10-20T17:36:42.046Z"
---
At VTEX, stores can manually set the price of an item ([SKU](https://help.vtex.com/pt/tutorial/o-que-e-um-sku--1K75s4RXAQyOuGUYKMM68u#)) when it is in the cart, on the product page on [inStore](https://developers.vtex.com/vtex-rest-api/docs/allow-manual-prices-on-instore), or is a subscription item. This feature is called **Manual Price** and can only be performed by some Admin VTEX user profiles.

Before starting to manually set prices in your store, the following information should be considered:

- Item prices can be modified (increased/decreased) freely, without any kind of restriction. However, if the price is changed to a value that is outside the parameters defined in the [Order Authorization](https://help.vtex.com/tutorial/how-order-authorization-works--3MBK6CmKHAuUjMBieDU0pn#) feature, the order will not be invoiced.
- Users with the following roles or permission will have access to modify the price of all items registered to your account (including all stores/sub-accounts):
   - **Roles**: Owner (Admin Super) or Call Center Operator (Telesales)
   - **Permission**: Shopping Cart Full Access


## Manual Price activation

To use the Manual Price functionality in your store, you must first enable it. Then, follow the settings below:

1. Make a `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/configuration).
2. Make a `POST` request using the endpoint [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration) with the same data obtained in the GET request, just modifying the value of the `allowManualPrice` parameter from `null` to  `true`.
3. Make a new `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration) to confirm activation.

## Setting the price of an item manually

For each sales method, there is a different way of manually modifying the price. The list below describes the procedure for each of these methods:

- **Cart items:** making a `PUT` request using the endpoint [Change Price](https://developers.vtex.com/vtex-rest-api/reference/pricechange), or configuring directly on the shop cart screen, check [Change the price of an item in the shopping cart](https://help.vtex.com/pt/tutorial/modificar-o-preco-de-um-item-no-carrinho-de-compras--7Cd37aCAmtL1qmoZJJvjNf).
- **inStore items:** check [Allow manual prices on inStore](https://developers.vtex.com/vtex-rest-api/docs/allow-manual-prices-on-instore#usage).
- **Subscription items:** check [Enabling Manual Prices for Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/enabling-manual-prices-for-subscriptions-v3).

## Recording manual changes to item prices

All price changes made manually are recorded and the user responsible for the change can be identified. To verify the user responsible for modifying the price of an item, follow the steps below:

1. Makes a `GET` request using the endpoint [Get Order](https://developers.vtex.com/vtex-rest-api/reference/getorder). You will need to provide the specific `orderId` on which the price was manually modified.
2. Register the information available in the `manualPriceAppliedBy` property. It will bring up the _user ID_ or the _appKey_ used to make the change.
3. Makes a `GET` request using the endpoint [License Manager - Get User](https://developers.vtex.com/vtex-developer-docs/reference/getuser), filling in with the _user ID_ or _appKey_, to obtain the data of the person responsible for the modification.

Example of information available in `manualPriceAppliedBy` property:
![Manual price](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/enable-the-manual-price-0.PNG)
