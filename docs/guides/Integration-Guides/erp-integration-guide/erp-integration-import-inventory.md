---
title: "Import inventory"
slug: "erp-integration-import-inventory"
hidden: false
createdAt: "2020-03-11T20:58:11.777Z"
updatedAt: "2022-02-10T15:59:10.915Z"
---

In this step, you will send the number of products you currently have in stock to VTEX.

## Before you begin

The **Shipping** module is where you control your store's inventory and the processes of receiving, managing, packing, and shipping orders. It includes concepts like:

- [Shipping strategy](https://help.vtex.com/en/tutorial/shipping-strategy--58vLBDbjYVQzJ6rRc5QNz3)
- [Shipping rates](https://help.vtex.com/en/tutorial/shipping-rates--1Balpg3rv0854udEPedvMM)
- [Pickup points](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R)
- [Inventory management](https://help.vtex.com/tutorial/managing-stock-items--tutorials_139)

A basic concept here is that of a **logistics route**, the path connecting your store to the customer. For an order to be placed in a store, the desired item should have stock available in at least one [warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb) connected through a [loading dock](https://help.vtex.com/en/tutorial/loading-dock--5DY8xHEjOLYDVL41Urd5qj) to a freight [carrier](https://help.vtex.com/en/tutorial/carries-on-vtex--7u9duMD5UQa2QQwukAWMcE) that delivers to the customer's address. The image below illustrates these concepts.

![shipping_strategy](https://user-images.githubusercontent.com/77292838/212991206-1605510b-9d1a-44fe-9bf2-16a17489b6e3.png)

If you would like an introduction to our Logistics module, check out the [Logistics overview](https://help.vtex.com/en/tutorial/logistics--53udnvI5eBy8DKo8FOjMoP) in our Help Center.

## Create Warehouses

The stock availability of an SKU is stored at the warehouse level. Before updating the inventory of an SKU, you must create the warehouses that will hold its stock.

If you have a small quantity of warehouses to manage, this can be done with the [warehouse management](https://help.vtex.com/en/tutorial/managing-warehouses--tutorials_137) section of your Admin panel. Otherwise, you can use the [Create/Update Warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/api/logistics/pvt/configuration/warehouses) endpoint to create them programmatically.

## Update SKU Inventory

To update an SKU inventory, you should use the [Update Inventory By SKU and Warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-) endpoint, from the Logistics API.

> ℹ️ You can find the `warehouseId` for each Warehouse using the [List All Warehouses](https://developers.vtex.com/docs/api-reference/logistics-api#get-/api/logistics/pvt/configuration/warehouses) endpoint.

You should set the total quantity of items in stock for each SKU. In between steps, you can use the [List Inventory By SKU](https://developers.vtex.com/docs/api-reference/logistics-api#get-/api/logistics/pvt/inventory/skus/-skuId-) endpoint or see how you can [Manage inventory](https://help.vtex.com/en/tutorial/managing-stock-items--tutorials_139) from your Admin panel.

## Wrapping up

If you’ve done things correctly, you should have imported your inventory information. This includes creating the warehouses needed for your logistics operation and updating the stock availability of each SKU in all warehouses.
