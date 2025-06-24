---
title: "Pick and Pack: New API Endpoints for Managing BIN Locations"
slug: "2025-06-18-pick-pack-bin-location-management-api"
type: "added"
excerpt: "The Pick and Pack Order Changes API now supports BIN location management with new endpoints for creating, updating, retrieving, and deleting BIN locations, enhancing warehouse inventory precision and control."
createdAt: "2025-06-18T00:00:00.219Z"
updatedAt: ""
hidden: false
---

The [Pick and Pack Order changes API](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api) was updated to include new endpoints that manage BIN locations. The BIN location is a specific, designated storage location within a warehouse. This location isn't necessarily a physical container. Each BIN is typically assigned a unique identifier or code, facilitating precise tracking and retrieval of items within the warehouse. These endpoints allow you to manage your warehouse inventory with greater precision and control.

## What has changed?

The following endpoints were added to the Pick and Pack Order Changes API:

- [`GET` Get BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#get-/-skuId-/warehouses/-warehouseId-): Retrieves details of a specific BIN location.
- [`POST` Create BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#post-/-skuId-/warehouses/-warehouseId-): Creates a new BIN location.
- [`PUT` Update BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#put-/-skuId-/warehouses/-warehouseId-): Updates an existing BIN location.
- [`DELETE` Delete BIN location](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#delete-/-skuId-/warehouses/-warehouseId-): Deletes a BIN location.

## Why did we make this change?

These new endpoints were introduced to provide greater control and precision over warehouse inventory management. By enabling the creation, modification, and deletion of BIN locations via API, users can seamlessly integrate their inventory management systems with VTEX, improving efficiency and reducing errors in order fulfillment. This enhancement addresses the need for more granular control over inventory tracking, especially for businesses with complex warehouse operations.

## What needs to be done?

No immediate actions are required. You can start using the new endpoints to manage BIN locations in your warehouse. For more information, refer to the [Pick and Pack Order Changes API documentation](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api).
