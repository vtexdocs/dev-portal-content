---
title: "Notify marketplace of inventory update"
slug: "inventory-notification"
excerpt: "This endpoint is used by *sellers* to notify marketplaces that the inventory level has changed for one of their SKUs. \n\nThere is no request body in this call, indicating the new inventory level, for instance. It only notifies a specific marketplace (`accountname`) that a seller (`sellerId`) has changed the inventory level of an SKU (`skuId`). \n\n*Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/reference/external-seller#fulfillment-simulation) provided in the seller registration form to get the updated inventory  information."
hidden: false
createdAt: "2020-09-14T15:26:55.390Z"
updatedAt: "2020-09-14T15:26:55.390Z"
---
