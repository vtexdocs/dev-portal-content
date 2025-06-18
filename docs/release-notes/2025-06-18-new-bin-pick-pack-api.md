---
title: "Pick and Pack: new BIN locations endpoints"
slug: "2025-06-18-new-bin-pick-pack-api"
type: "added"
excerpt: "The Pick and Pack Order Changes API now supports BIN location management with new endpoints for creating, updating, retrieving, and deleting BIN locations, enhancing warehouse inventory precision and control."
createdAt: "2025-06-18T00:00:00.219Z"
updatedAt: ""
hidden: false
---

The [Pick and Pack Order changes AP](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api) was updated to include new endpoints that manage BIN locations. The BIN location is a specific, designated storage location within a warehouse. This location isn't necessarily a physical container. Each BIN is typically assigned a unique identifier or code, facilitating precise tracking and retrieval of items within the warehouse.

## What has changed?

The following endpoints were added:

- [`GET` Get BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#get-/-skuId-/warehouses/-warehouseId-)
- [`POST` Create BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#post-/-skuId-/warehouses/-warehouseId-)
- [`PUT` Update BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#put-/-skuId-/warehouses/-warehouseId-)
- [`DELETE` Delete BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#delete-/-skuId-/warehouses/-warehouseId-)

## What needs to be done?

No actions need to be done.
