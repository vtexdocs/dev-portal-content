---
title: "New Pick and Pack API"
slug: "2025-04-25-pick-and-pack-api"
type: "added"
createdAt: "2025-04-25T17:08:52.219Z"
updatedAt: ""
hidden: false
excerpt: ""
---

The new [Pick and Pack API](https://developers.vtex.com/docs/api-reference/pick-and-pack-api) offers robust functionality to support end-to-end order fulfillment processes. This API enables users to manage orders, streamline picking operations, track shipments, and handle returns efficiently. With it, you can retrieve detailed order information including items, packages, and current status; access worksheet data to guide picking operations, query delivery and tracking information for shipments, and retrieve facility details to support logistical planning.

The Pick and Pack API contains the following endpoints:

- `POST` [Generate JWT token](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#post-/token?endpoint=post-/token): Generate a JWT token.
- `GET` [Get order by ID](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#get-/orders/-orderId-?endpoint=get-/orders/-orderId-): Retrieve orders by ID and see delivery details, including tracking information.
- `PATCH` [Set order delivery](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#patch-/orders/-orderId-/tracking?endpoint=patch-/orders/-orderId-/tracking): Update delivery tracking information.
- `GET` [Get worksheet by ID](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#get-/worksheets/-worksheetId-?endpoint=get-/worksheets/-worksheetId-): Retrieve worksheet data.
- `GET` [Get worksheets by order ID](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#get-/worksheets?endpoint=get-/worksheets): Retrieve all worksheets linked to a specific order.
- `GET` [Get facility by ID](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#get-/facilities/-facilityId-?endpoint=get-/facilities/-facilityId-): Retrieve facility-related information.
- `GET` [Get shipment](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#get-/shipments/-shipmentId-?endpoint=get-/shipments/-shipmentId-): Retrieve shipment tracking for individual shipments.
- `GET` [List shipments](https://developers.vtex.com/docs/api-reference/pick-and-pack-api#get-/shipments?endpoint=get-/shipments): Retrieve a list of all shipments.

For more information about the feature, refer to the [Pick and Pack](https://help.vtex.com/en/tutorial/vtex-pick-and-pack--1OOops3WrUyz7e0bnhkfXU) article.
