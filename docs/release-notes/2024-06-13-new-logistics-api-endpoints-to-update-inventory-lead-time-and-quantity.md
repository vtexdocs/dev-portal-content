---
title: "New Logistics API endpoints to update inventory lead time and quantity"
slug: "2024-06-13-new-logistics-api-endpoints-to-update-inventory-lead-time-and-quantity"
hidden: false
type: "added"
createdAt: "2024-06-14T12:04:00.219Z"
excerpt: "Manage SKU quantity and lead time in separate endpoints."
---

In order to facilitate your [inventory management](https://help.vtex.com/en/tutorial/inventory-management--tutorials_139), we have launched new endpoints in our **Logistics API**. In addition to the previous [Update inventory by SKU and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-), you can now, if desired, use an endpoint to configure only lead time and another just to update SKU quantity.

The new routes are the following:

| **Endpoint** | **Description** |
| :--- | :--- |
| PATCH - [Update inventory lead time by SKU and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#patch-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-/lead-time) | Configure exclusively the [lead time](https://help.vtex.com/en/tutorial/lead_time-shipping-time-at-sku-level--16yv5Mkj6bTyWR1hCN2f4B) for a SKU from a warehouse. |
| PATCH - [Update inventory quantity by SKU and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#patch-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-/quantity) | Configure exclusively the quantity for a SKU from a warehouse. You can either update the SKU count or turn on the infinite inventory configuration. |
