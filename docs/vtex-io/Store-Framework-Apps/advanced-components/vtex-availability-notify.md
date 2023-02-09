---
title: "Availability Notify"
slug: "vtex-availability-notify"
hidden: false
createdAt: "2021-05-28T17:11:48.473Z"
updatedAt: "2022-10-18T20:59:10.400Z"
---

The Availability Notify component is responsible for showing a subscription form when a product SKU is not available. The form lets customers subscribe to get notified when that item gets restocked.

![store-notifier](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-availability-notify-0.png)

The app records the notification request and monitors inventory updates. This way, once the requested SKU gets back in stock, the app will email the shoppers who asked to be notified.

## Configuration

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the Availability Notify app in the desired VTEX account by running `vtex install vtex.availability-notify` in your terminal.

2. Open your store’s Store Theme app directory in your code editor.

3. Open your app's `manifest.json file` and add the Availability Notify app under the `peerDependencies` field.

>⚠️ Warning
>
> Due to changes in its peer dependencies you will need to release a new major version. Check the documentation on [How to migrate CMS settings after a theme major update](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update).

```json
  "peerDependencies": {
    "vtex.availability-notify": "1.x"
  }
```

4. Add the `availability-notify` component block to your PDP in your store theme (`store.product`). For example:

```json
{
 "store.product": {
    "children": [
      "availability-notify"
    ]
  },

```

5. Once you have added the `availability-notify` component, access your store's Admin.
6. Go to **Orders** > **Inventory & Shipping** > **Availability Notifier**.
7. Then, you will see the app's settings:

![app-settings](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-availability-notify-1.png)

| Setting field           | Description                                                                                                            |
|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| `Verify Availability`   | Runs a shipping simulation to verify that the item can be shipped to the shopper before sending a notificaiton.        |
| `Marketplace to Notify` | Allows a seller account to specify a comma separated list of marketplace account names to notify of inventory updates. |
| `Download Requests`     | Download an XLS file of all recquest records.                                                                          |
| `Process Unsent`        | Process all unsent requests and download an XLS file of the results.                                                   |

After making the desired settings in the app, set up its template according to your necessities. Check out more details about it in the next section, [Customizing the Back in stock template](#customizing-the-back-in-stock-template).

## Seller Configuration

This app needs to also be installed on the seller account

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the Availability Notify app in the desired VTEX SELLER account through the app store
2. In the app configuration enter the name of the marketplace to notify when there are any inventory changes

This will forward the inventory change to the MARKETPLACE and then trigger the `Back In Stock` email to the subscribed users of that product. 
## Customizing the Back in stock template

Once you have installed the app, you can customize the email template to send to the shoppers who asked to be notified.

1. Find the email template, named **BACK IN STOCK**, in your store's Admin in **Customer** > **Message center** > **Templates**.
2. Search for the `availability-notify` component template, named **BACK IN STOCK** and click on it.
3. After, you will see the email template and its configuration. For example:

![template-back-in-stock](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-availability-notify-2.gif)

To edit the email template's field, check the documentation on [How to create and edit transactional email templates](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/335JZKUYgvYlGOJgvJYxRO), and you will notice the **JSON Data** field, which is responsible for adding variables that allow you to dynamically add data to the email. These variables are JSON properties, and you can see more details about them in [Get SKU and context](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyid/-skuId-) and in [Including order variables in email template](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/fLMUCPArCYB9vcTZEZ6bi).

>⚠️ *JSON Data examples will only appear in templates when you complete the desired action in your store. If you have not transacted an order, recurrence or any other action, JSON Data will appear blank.*
*NOTE: notification email is only triggered when on the `master` workspace*

## Searching and Processing Availability Notify data

This app uses [Master Data V2](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview), to search for stored data you should use Master Data API - v2 endpoints with the variables `data_entity_name` and `schema` with the value `notify`.

If you want to run the services manually you can use the two endpoints below: (An authentication token is required)

- To process Unsent Requests:
`https://app.io.vtex.com/vtex.availability-notify/v1/{{accountName}}/master/_v/availability-notify/process-unsent-requests`

- To process All Requests:
`https://app.io.vtex.com/vtex.availability-notify/v1/{{accountName}}/master/_v/availability-notify/process-all-requests`

Check out the [Open API Schemas repository](https://github.com/vtex/openapi-schemas) containing several VTEX Postman Collections including Master Data API - v2.

## Customization

In order to apply CSS customizations to this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles        |
|--------------------|
| `notiferContainer` |
| `title`            |
| `notifyLabel`      |
| `form`             |
| `content`          |
| `input`            |
| `inputName`        |
| `inputEmail`       |
| `submit`           |
| `sucess`           |
| `error`            |
