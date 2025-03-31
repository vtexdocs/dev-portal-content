---
title: "New Operational Capacity API"
slug: "2025-03-20-operational-capacity-api"
type: "added"
createdAt: "2025-03-31T14:34:56.219Z"
updatedAt: ""
hidden: false
excerpt: "The new Operational Capacity API enables merchants to efficiently manage and configure the sellers' operational capacities of their fulfillment locations, ensuring optimal order processing and resource allocation."
---

The new [**Operational Capacity API**](https://developers.vtex.com/docs/api-reference/operational-capacity-api#overview) allows merchants to manage and configure the sellers' operational capacities of their fulfillment locations. This functionality is essential for optimizing order processing, resource allocation, and maintaining accurate inventory and order records. By leveraging this API, merchants can ensure that their fulfillment operations run smoothly and efficiently.

The Operational Capacity API includes the following endpoints:

- `PUT` [Configure location capacity](https://developers.vtex.com/docs/api-reference/operational-capacity-api#put-/api/fulfillment-locations/location/-locationId-/capacities/-code-): Update the capacity settings of a specific location to control operational capacity.
- `GET` [Get locations capacities by account](https://developers.vtex.com/docs/api-reference/operational-capacity-api#get-/api/fulfillment-locations/capacity/by-parent-account-name): Retrieve the current capacities of all locations associated with a parent account.
- `GET` [List location capacities](https://developers.vtex.com/docs/api-reference/operational-capacity-api#get-/api/fulfillment-locations/locations/-locationId-/capacities): List capacity details of a specific location for the upcoming days.
- `GET` [List locations](https://developers.vtex.com/docs/api-reference/operational-capacity-api#get-/api/fulfillment-locations/location): Retrieve a paginated list of fulfillment locations based on status and search criteria.
- `PUT` [Update location status](https://developers.vtex.com/docs/api-reference/operational-capacity-api#put-/api/fulfillment-locations/locations/-locationId-/status): Update the status of a specific location to either `ACTIVE` or `MANUALLY_PAUSED`. This is essential for managing location availability and ensuring accurate order processing.

For more detailed information and implementation guidance, refer to the [Operational Capacity API](https://developers.vtex.com/docs/api-reference/operational-capacity-api#overview) documentation.
