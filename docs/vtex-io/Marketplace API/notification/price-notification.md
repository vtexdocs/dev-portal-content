---
title: "Notify marketplace of price update"
slug: "price-notification"
excerpt: "This endpoint is used by *sellers* to notify marketplaces that the price has changed for one of their SKUs. \n\nThere is no request body in this call, indicating the new price value, for instance. It only notifies a specific marketplace (`accountname`) that a seller (`sellerId`) has changed the price of an SKU (`skuId`). \n\n*Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/reference/external-seller#fulfillment-simulation) provided in the seller registration form to get the updated price information."
hidden: false
createdAt: "2020-09-14T15:26:55.388Z"
updatedAt: "2020-09-14T15:26:55.388Z"
---
