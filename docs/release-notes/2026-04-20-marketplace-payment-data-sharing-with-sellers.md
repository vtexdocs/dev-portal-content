---
title: "Marketplace payment data sharing with sellers"
slug: "2026-04-20-marketplace-payment-data-sharing-with-sellers"
type: "improved"
createdAt: "2026-04-20T00:00:00.000Z"
updatedAt: "2026-04-20T00:00:00.000Z"
excerpt: "VTEX Marketplaces can now share native payment data with sellers, with details like payment method, card brand, and acquirer responses."
tags:
  - Orders
  - Payments
---

VTEX Marketplaces now forward native `paymentData` to seller orders, for both VTEX and external sellers. This replaces the previous approach that relied on custom fields in `customApps` to propagate payment information, as described in the [Orders API: support for NT 2025.001 fields](https://developers.vtex.com/updates/release-notes/2025-08-29-orders-api-support-for-nt-2025-001-fields) release note.

The new approach uses native VTEX payment fields, ensuring data (`tid`, `authId`, `nsu`) is consistently available and reducing custom logic in seller integrations.

## What has changed?

Previously, seller orders created from marketplace sales contained placeholder payment information. Now, VTEX sellers receive native `paymentData`, which includes the actual payment details from the marketplace transaction. The `paymentData` field is returned by the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint.

External sellers integrated through the Fulfillment flow now receive payment information in the [Authorize fulfillment](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-sellerOrderId-/fulfill) endpoint payload:

This feature also has backward compatibility. Therefore, integrations that rely on the previous seller `paymentData` behavior can detect marketplace-assumed payments by checking for `transactionId = "PAYMENT-FROM-AFFILIATE"`. This allows gradual migration without breaking existing flows.

## What needs to be done?

To request early access, contact [VTEX Support](https://supporticket.vtex.com/support) and request this feature for your account.
