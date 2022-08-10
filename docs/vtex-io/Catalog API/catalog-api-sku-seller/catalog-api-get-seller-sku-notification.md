---
title: "Change Notification"
slug: "catalog-api-get-seller-sku-notification"
excerpt: "The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request./n/nWith this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.\n\nThere are two information expected by the marketplace in this request: the `sellerId`, which identifies the seller, and the `skuId`, which identifies the SKU.\n\nBoth information are passed through the request URL. The body of the request should be empty."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-09-01T13:44:48.540Z"
---
## Example

Let's say your seller has the ID `123` in the marketplace and you want to inform the marketplace that has been a change in the SKU with ID `700`.

In this case, you would have to replace the `sellerId` parameter with the value `123` and the `skuId` parameter with the value `700`. The URL of the request would be the following.

```
https://{{accountName}}.vtexcommercestable.com.br/api/catalog_system/pvt/skuseller/changenotification/123/700
```

## Response codes

The following response codes are possible for this request.

* 404: the SKU was not found in the marketplace. The body of the response, in this case, should follow this format: "Seller StockKeepingUnit {{skuId}} not found for this seller id {{sellerId}}". This means that the seller can now proceed with sending an offer to the marketplace in order to suggest that this SKU is sold there.
* 200: the SKU whose ID was informed in the URL already exists in the marketplace and was found. The marketplace can now proceed with a fulfillment simulation in order to get updated information about this SKU's inventory and price.

* 429 - Failure due to too many requests.
* 403 - Failure in the authentication.

## Authentication

This is a private API and needs credentials with viewer access.

> Learn more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations) with VTEX private APIs.