---
title: "Change Notification with Seller ID and Seller SKU ID"
slug: "post_api-catalog-system-pvt-skuseller-changenotification-sellerid-sellerskuid"
excerpt: "> ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.\n\nThe seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.\n\nWith this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.\n\nThere are two information expected by the marketplace in this request: the `sellerId`, which identifies the seller, and the `sellerSkuId`, which identifies the binding of the seller with the SKU.\n\nBoth information are passed through the request URL. The body of the request should be empty."
hidden: false
createdAt: "2021-03-25T19:08:22.998Z"
updatedAt: "2022-07-28T19:11:30.192Z"
---
