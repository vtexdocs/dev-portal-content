---
title: "How to identify the store and sales associate in an inStore order"
slug: "how-to-identify-the-store-and-sales-associate-in-an-instore-order"
hidden: false
createdAt: "2022-09-14T16:48:16.604Z"
updatedAt: "2022-09-14T20:36:41.517Z"
---

It is common for ecommerce operations that adopt [unified commerce strategies](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv) to quantify the sales impact of integrating physical stores. In [Endless Aisle](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/40KMlmGI5tN0r0KPCDWgGn) orders, where products unavailable in the physical store are retrieved from other inventories, it may be desirable to identify the source and ordering party.

This article explains how to use the information recorded in an inStore order to identify the seller and the physical store where the order was placed.

## Getting the details of an order

To access the details of a specific order, simply select the desired order under **Orders** > **Order Management** > **All Orders**. This path is recommended for individual queries by users of the ecommerce operation.

To send order data to external systems, such as dashboards and data lakes, we recommend performing an [API integration using the order feed](https://developers.vtex.com/vtex-developer-docs/docs/erp-integration-set-up-order-integration). This also allows you to capture order details that are not displayed in the VTEX admin UI, such as the seller's email address.

## Seller identification

When an order is closed in inStore, the ID of the user logged into the application is visible at the top of the order details screen in Admin. In the example below, the user name is `A123456`.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/how-to-identify-the-store-and-sales-associate-in-an-instore-order-0.png)
When the order details are retrieved by [Orders API](https://developers.vtex.com/vtex-developer-docs/reference/orders), the user name is available in the `callCenterOperatorData.userName` field. You can also access the email address of this user in `callCenterOperatorData.email`.

```json
"callCenterOperatorData": {
       "id": "CallCenterOperatorAttachment",
       "email": "joao.silva@exemplo.com",
       "userName": "A123456"
   }
```

If the user logged into the application is shared between salespeople in the same store, it is also possible to include the salesperson's ID in the **Customer information** field.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/how-to-identify-the-store-and-sales-associate-in-an-instore-order-1.png)
When the order details are fetched from the Orders API, this information is available in the `openTextField.value` field.

```json
"openTextField": {
       "value": "A123456 - JOAO RAMOS SILVA"
   }
```

## Store identification

When an order is closed in inStore, the store ID is visible in the **Sales and Marketing** section of the order details screen in Admin. In the example below, the store identifier is `8fc9d8df-5961-11ea-8311-0a43926dcc3d`.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/how-to-identify-the-store-and-sales-associate-in-an-instore-order-2.png)
When the order details are obtained from the [Orders API](ref:orders-api-overview), this information is available in the `marketingData.utmSource` field.

```json
"marketingData": {
       "id": "marketingData",
       "utmSource": "8b4d5ea1-2055-11ea-82fa-0ad725bc7b4f",
       "utmPartner": null,
       "utmMedium": null,
       "utmCampaign": null,
       "coupon": null,
       "utmiCampaign": null,
       "utmipage": null,
       "utmiPart": null,
       "marketingTags": [
           "instore"
       ]
   }
```

## Query Registration Data

The merchant and store identifier can be used to query the registration data at `https://{accountName}.myvtex.com/admin/vtable`.
![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/how-to-identify-the-store-and-sales-associate-in-an-instore-order-3.png)

[block:callout]
{
  "type": "info",
  "body": "The instructions below explain how to perform these queries using the identifiers that appear in an order. If necessary, however, you can search using any field in the store and vendor master data."
}
[/block]

### Search by seller

To do this search, follow the instructions below:

1. Click on the search bar.
2. Select the option **Nome**.
3. Select the equal sign `=`.
4. Paste the store ID (`callCenterOperatorData.userName`).
5. Press the `Enter` key on your keyboard.

When you complete step 4, the search filter expression should be in the format `Nome:=:A123456`. This will allow you to find the salesperson in the salesperson listing, as seen in the image below.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/how-to-identify-the-store-and-sales-associate-in-an-instore-order-4.png)
If you prefer to do this query by API, just use the [Search Documents](https://developers.vtex.com/vtex-developer-docs/reference/search#searchdocuments) endpoint of the [Master Data API - V2](https://developers.vtex.com/reference/master-data-api-v2-overview) to search for the store identifier in the `vendors` data entity.

### Search by store

To do this search, follow the instructions below:

1. Click on the search bar.
2. Select the option **Id do Documento**.
3. Select the equal sign (`=`).
4. Paste the store ID (`marketingData.utmSource`).
5. Press the `Enter` key on your keyboard.

When you complete step 4, the search filter expression should be in the format `DocumentId:=: "c2a0b3ee-03f3-11eb-8367-128fa24166a9"`. This will allow you to find the store in the store list, as seen in the image below.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/how-to-identify-the-store-and-sales-associate-in-an-instore-order-5.png)
If you prefer to do this query by API, just use the [Search Documents](https://developers.vtex.com/vtex-developer-docs/reference/search#searchdocuments) endpoint of the [Master Data API - V2](https://developers.vtex.com/reference/master-data-api-v2-overview) to search for the store identifier in the `stores` data entity.
