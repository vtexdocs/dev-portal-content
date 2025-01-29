---
title: "New Pick and Pack Order Changes API"
slug: "2025-01-29-new-pick-pack-order-changes-api"
type: "added"
createdAt: "2025-01-29T17:08:52.219Z}"
updatedAt: ""
hidden: false
excerpt: "The new Pick and Pack Order Changes API allows merchants to efficiently modify orders by adding or removing items, adjusting prices, and applying discounts, ensuring accurate inventory and order records."
---

The new [Pick and Pack Order Changes API](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#overview) enables merchants to modify [VTEX Pick and Pack](https://help.vtex.com/en/tutorial/vtex-pick-and-pack--1OOops3WrUyz7e0bnhkfXU) orders by adding or removing items, adjusting prices, and applying discounts. This functionality is essential for managing customer requests, addressing product availability issues, and implementing promotional adjustments. The API ensures that merchants can efficiently handle order modifications while maintaining accurate inventory and order records.

The Pick and Pack Order Changes API contains the following endpoints:

- `PUT` [Update order deadline](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#put-/orders/-orderId-/deadline): Extend or modify the deadline for fulfilling a specific order.
- `POST` [Update items of the order](https://developers.vtex.com/docs/api-reference/pick-and-pack-order-changes-api#post-/order/changes): Add or remove items, adjust prices, or apply discounts to an existing order.