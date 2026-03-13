---
title: "Shopee public shipment label route now returns accurate HTTP status codes"
slug: "2026-03-13-shopee-public-shipment-label-route-status-codes"
type: "improved"
createdAt: "2026-03-13T15:00:00.000Z"
updatedAt: "2026-03-13T15:00:00.000Z"
excerpt: "Shopee shipment label requests now return the real HTTP status code instead of always returning 500 errors."
---

We updated the Shopee shipment label flow to support the new public route behavior and return accurate HTTP status codes for non-success scenarios.

## What has changed?

- The shipment label flow was centralized to reuse the same process between legacy and new APIs.
- The previous behavior that hardcoded `HTTP 500` for non-success responses was removed in the new flow.
- Requests now return the real status code from the integration (for example, `404` when a PLP is not ready yet), instead of incorrectly signaling an internal server failure.
- The rollout is controlled by feature flag, allowing a safer migration between versions.

## Why did we make this change?

The previous implementation generated false-positive internal server errors in monitoring and operations. By returning the actual HTTP status code, sellers and integrators can distinguish expected business integration scenarios from real platform failures.

## What needs to be done?

- Sellers using Shopee integration should validate and adjust ERP error-handling logic for the new status-code behavior.
- Teams should review alerting and observability rules that currently interpret all non-success responses as `500`.
- Treat this as a breaking behavior change for clients that rely on the old status-code pattern.
