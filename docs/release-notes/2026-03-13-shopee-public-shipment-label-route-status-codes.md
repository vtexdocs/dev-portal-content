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

- The shipment label generation flow has been unified across legacy and new APIs. This ensures that both routes now follow the same processing logic and response patterns.
- Previously, any non-success response was incorrectly mapped to HTTP 500, masking the real cause of the issue. This fallback behavior has been removed.
- Requests now return the real status code from the integration (for example, `404` when a PLP is not ready yet), instead of incorrectly signaling an internal server failure.
- The rollout is controlled by feature flag, allowing a safer migration between versions.

## Why did we make this change?

The previous implementation generated false-positive internal server errors in monitoring and operations. By returning the actual HTTP status code, sellers and integrators can distinguish expected business integration scenarios from real platform failures.

## What needs to be done?
This update requires action only if your integration depends on the previous behavior (always returning `500` for errors).

> ⚠️ If your integration already handles different HTTP status codes correctly, no action is required.

- **Sellers using Shopee integration:** Verify your ERP assumes all error responses return `500`, and update the error-handling logic to interpret different HTTP status codes correctly.
- **Operations and monitoring teams:** Review alerting and observability rules that currently interpret all non-success responses as `500`.

> ⚠️ Treat this as a breaking change if you rely on the previous status-code behavior.
