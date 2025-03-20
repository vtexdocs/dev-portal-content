---
title: "New Operational Capacity API"
slug: "2025-03-20-new-operational-capacity-api"
type: "added"
createdAt: "2025-03-20T14:34:56.219Z"
updatedAt: ""
hidden: false
excerpt: "The new Operational Capacity API enables merchants to efficiently manage and configure the operational capacities of their fulfillment locations, ensuring optimal order processing and resource allocation."
---

The new Operational Capacity API allows merchants to manage and configure the operational capacities of their fulfillment locations. This functionality is essential for optimizing order processing, resource allocation, and maintaining accurate inventory and order records. By leveraging this API, merchants can ensure that their fulfillment operations run smoothly and efficiently.

The Operational Capacity API includes the following endpoints:

- `PUT` [Configure Location Capacity](): Update the capacity settings of a specific location to control operational capacity.
- `GET` [Get Locations Capacities By Account](): Retrieve the current capacities of all locations associated with a parent account.
- `GET` [List Location Capacities](): List capacity details of a specific location for the upcoming days.
- `GET` [List Locations](): Retrieve a paginated list of fulfillment locations based on status and search criteria.

For more detailed information and implementation guidance, refer to the [Operational Capacity API]() documentation.