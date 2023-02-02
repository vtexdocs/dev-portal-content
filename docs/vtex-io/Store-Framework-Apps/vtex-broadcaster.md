---
title: "Broadcaster Adapter"
slug: "vtex-broadcaster
hidden: false
createdAt: "2022-07-08T07:17:48.371Z"
updatedAt: "2022-10-27T19:47:24.537Z"
---

The Broadcaster adapter is designed to adapt broadcaster catalog changes to an event in IO's Events system.

With the catalog changes being broadcasted to IO, you can have apps that listen to the catalog changes and do tasks according to the changes. For example, the [Availability Notify](https://developers.vtex.com/vtex-developer-docs/docs/vtex-availability-notify) app uses the Broadcaster Adapter to monitor inventory updates. Once the requested SKU gets back in stock, the app will email shoppers who asked to be notified.

![broadcaster-architecture](https://user-images.githubusercontent.com/67270558/158252905-3480125a-fabe-4db3-bb4d-7c7dea74f8ef.png)

The broadcaster adapter receives a POST request with the data of the SKU that changed, and then it will push an event to the Event system to broadcast to apps that want to listen to these changes.

> ⚠️
>
> The Broadcaster Adapter app receives catalog changes from the same account where the app is installed and not from sellers.

## SKU Data

When the Broadcaster Adapter app sends an event, it contains a payload with the following fields.

| Field Name                                | Description                                                                                                                                                  | Type    |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `IdSku`                                   | SKU ID in VTEX                                                                                                                                               | string  |
| `ProductId`                               | Product ID in VTEX                                                                                                                                           | long    |
| `An`                                      | Account Name in VTEX, shown in the store’s VTEX Admin url.                                                                                                   | string  |
| `IdAffiliate`                             | Affiliate ID generated automatically in the configuration.                                                                                                   | string  |
| `DateModified`                            | Date when the item was updated.                                                                                                                              | string  |
| `IsActive`                                | Identifies whether the product is active or not. If `true` the product/SKU is active                                                                         | boolean |
| `StockModified`                           | Identifies that the inventory level has been altered. If `false`, the inventory level has not been changed.                                                  | boolean |
| `PriceModified`                           | Identifies that the price has been altered. If `false`, the product/SKU price has not been changed.                                                          | boolean |
| `HasStockKeepingUnitModified`             | Identifies that the product/SKU registration data has changed, such as name, description, weight, etc. If `true`, the product/SKU registration data changed. | boolean |
| `HasStockKeepingUnitRemovedFromAffiliate` | Identifies that the product is no longer associated with the trade policy. If `true`, the trade policy has changed.                                          | boolean |

## Regarding Franchise Accounts

When attempting to listen for catalog change notifications in a **[franchise account](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl)** (sometimes referred to as a **"subaccount"**), you will likely find that notifications are not being received by your app. This is because by default, catalog change notifications are only sent to the Broadcaster Adapter in the **main account**.

### "Notify Subaccounts" setting

The app installed in the main account can be configured to push a notification event to all of the associated franchise accounts / subaccounts.

To access this setting, search for `My Apps` in the VTEX Admin, then search the list of installed apps for `Broadcaster Adapter`. Click on `Settings`. Finally, activate the checkbox for `Notify Subaccounts` and click `Save`.

## Testing the app

By default, when the Broadcaster Adapter app sends events, these events are only sent in each account's master workspace. If you work in a **[Development workspace](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-workspace)**, there are two ways to receive events there:

### "Notify Target Workspace" setting

The app installed in the master workspace can be configured to push a notification event to a target workspace of your choice in addition to pushing it in the master workspace.

To access this setting, search for `My Apps` in the VTEX Admin, then search the list of installed apps for `Broadcaster Adapter`. Click on `Settings`. Finally, input the name of the workspace you wish to notify in the `Notify Target Workspace` field and click `Save`.

### Event simulation via REST API

You can simulate an event by making a `POST` request to `app.io.vtex.com/vtex.broadcaster/v0/{{account}}/{{workspace}}/notify`
with the body:

```
{
	"HasStockKeepingUnitModified": true,
	"IdSku": {{SKU id}}
}
```

This endpoint requires a `VtexidClientAutCookie` header for authentication.
