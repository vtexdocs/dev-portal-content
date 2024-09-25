---
title: "Enabling Manual Prices for Subscriptions v3"
slug: "enabling-manual-prices-for-subscriptions-v3"
hidden: false
createdAt: "2022-05-10T17:15:06.209Z"
updatedAt: "2022-05-24T16:48:19.459Z"
---
> ℹ The option of setting manual prices is only available for Subscriptions v3. If you are using a previous version of the Subscriptions system, check out the [Subscriptions v3 migration guide](https://developers.vtex.com/vtex-rest-api/docs/subscriptions-v3-migration-guide).

**Subscriptions** is an app developed by VTEX to facilitate recurring sales in your store. It works as an automatic scheduler, executing a repurchase at the frequency requested by the customer. Check out our article [How subscriptions work](https://help.vtex.com/en/tutorial/how-subscriptions-work--frequentlyAskedQuestions_4453) to know more.

When using subscriptions, stores might need to configure prices manually for each item. Considering that product prices can change over time, maintaining the same commercial rules for subscription orders can be a good strategy to retain clients over a longer period.

By enabling the Manual Price feature for Subscriptions v3, you can:

* Apply a manual price on each subscription item instead of the current price applied.
* Maintain the same manual price for every future recurrent order from that subscription, if desired.


## Before you begin

To enable Manual Prices for Subscriptions v3, it is first necessary to enable it in the Checkout settings. This means you must make a request to the <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration) endpoint, setting `allowManualPrices` to `true`, if you have not done this yet. For more information on how manual prices work at VTEX, we recommend reading [Enabling Manual Price in my store](https://developers.vtex.com/docs/guides/enable-the-manual-price).

Setting Manual Prices for Subscriptions generally follows the same rules as applying manual prices to items in regular orders at Checkout. Still, it requires additional configurations and actions detailed in the following sections.

To apply manual prices, users must have at least one of the following [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) or [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3):

  * Owner (Admin Super) role
  * Call Center Operator (Telesales) role
  * Shopping Cart Full Access resource

## Configuration

To enable Manual Prices for Subscriptions, you must follow the steps below:

1. Make a request using the <span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/getsettings-1) endpoint to retrieve the current settings related to Subscriptions in your store.
2. Make a request using the <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Edit Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/editsettings-1) endpoint, setting the following properties to `true`:

| **Property name** | **Type** | **Description** |
|---|---|---|
| `manualPriceAllowed` | boolean | This property enables the manual price configuration in subscription items when set to `true`. This is valid for all existing subscriptions, provided that there is a manual price configured. |
| `useItemPriceFromOriginalOrder` | boolean | This property enables using the price manually set for each item from the original subscription order when set to `true`. This is only valid for new subscriptions created after enabling this configuration. The `manualPriceAllowed` property must also be set to `true`; otherwise, this configuration will not work. |

#### Request body example

```json
{
    "slaOption": "NONE",
    "defaultSla": null,
    "isUsingV3": true,
    "onMigrationProcess": false,
    "executionHourInUtc": 9,
    "workflowVersion": "1.1",
    "deliveryChannels": [
        "delivery"
    ],
    "randomIdGeneration": false,
    "isMultipleInstallmentsEnabledOnCreation": false,
    "isMultipleInstallmentsEnabledOnUpdate": false,
    "orderCustomDataAppId": null,
    "postponeExpiration": false,
    "manualPriceAllowed": true,
    "useItemPriceFromOriginalOrder": true
}
```

## Setting a manual price in a subscription item

To apply a manual price to a subscription item, you must insert a new value into the `manualPrice` property:

| **Property name** | **Type** | **Description** |
|---|---|---|
| `manualPrice` | int32 | The manual price you want to use for the subscription item. The value follows the same format as in Checkout, which means you must send it without decimal separators. Examples: If the desired value is `29.90`, you must write `2990`. In case the value is `0.90`, you must write `90`. |

You can manually modify the price when:

  * [Adding an item to a subscription](#adding-an-item-to-a-subscription).
  * [Editing an item in a subscription](#editing-an-item-in-a-subscription).

Read the following sections for details on the endpoints you must use and their request body examples.

> 🚧 You can only apply a manual price to a subscription item if the `manualPriceAllowed` configuration is set to `true`, as described in the [Configuration](#configuration) section.


### Adding an item to a subscription 

When making a <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Add item to subscription](https://developers.vtex.com/vtex-rest-api/reference/post_api-rns-pub-subscriptions-id-items) request, you can apply a manual price by informing a new value in the `manualPrice` property in the request body.

#### Request body example

```json
{
  "skuId": "12",
  "quantity": 5,
  "manualPrice": 40
}
```

### Editing an item in a subscription

To apply a manual price when making a <span class="APIMethod APIMethod_fixedWidth APIMethod_patch">patch</span> [Edit item on subscription](https://developers.vtex.com/vtex-rest-api/reference/patch_api-rns-pub-subscriptions-id-items-itemid) request, you must inform the desired value in the `manualPrice` property in the request body.

Keep in mind that all the other editable properties — `status`, `isSkipped`, and `quantity` — remain with the same behavior and can be set in the same request to edit the subscription item as the `manualPrice`.

#### Request body example

```json
{
  "quantity": 5,
  "manualPrice": 500
}
```

### Removing a manual price in a subscription item

To remove a manual price, you must set the `manualPrice` value to `null` when making a <span class="APIMethod APIMethod_fixedWidth APIMethod_patch">patch</span> [Edit item on subscription](https://developers.vtex.com/vtex-rest-api/reference/patch_api-rns-pub-subscriptions-id-items-itemid) request. 


#### Request body example

```json
{
  "manualPrice": null
}
```

Another option is to completely remove the item from the subscription, making a request to the <span class="APIMethod APIMethod_fixedWidth APIMethod_delete">delete</span> [Remove item from subscription](https://developers.vtex.com/vtex-rest-api/reference/delete_api-rns-pub-subscriptions-id-items-itemid) endpoint.
