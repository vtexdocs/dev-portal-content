---
title: "Shopee public shipment label route now returns accurate HTTP status codes"
slug: "2026-03-13-shopee-public-shipment-label-route-status-codes"
type: "improved"
createdAt: "2026-03-13T15:00:00.000Z"
updatedAt: "2026-03-13T15:00:00.000Z"
excerpt: "Shopee shipment label requests now return the real HTTP status code instead of always returning 500 errors."
---

We have updated the Shopee shipment label flow to align with the new public route behavior. Requests now return accurate HTTP status codes for non-success scenarios, improving error visibility and integration reliability.

## What has changed?

The shipping label generation flow has been unified between legacy and new APIs. This ensures that both routes now follow the same processing logic and response patterns.

Previously, any failure response was incorrectly mapped to HTTP 500, masking the real cause of the problem.
Now, they return the actual integration status code (e.g., `404` when a PLP is not yet ready), instead of incorrectly signaling an internal server failure.

## What needs to be done?

If your Shopee integration is only returning the `500` error code for all labels, you need to update your error handling logic to correctly interpret the different HTTP status codes.

To update your integration, access the [VTEX Shopee Integration API](link) documentation.