---
title: "Notify marketplace of inventory update"
slug: "inventorynotification"
excerpt: "This endpoint is used by *sellers* to notify marketplaces that the inventory level has changed for one of their SKUs. \n\nThere is no request body in this call, indicating the new inventory level, for instance. It only notifies a specific marketplace (`accountName`) that a seller (`sellerId`) has changed the inventory level of an SKU (`skuId`). \n\n*Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form to get the updated inventory  information."
hidden: false
createdAt: "2021-11-09T18:52:06.551Z"
updatedAt: "2022-02-16T15:16:45.166Z"
---
