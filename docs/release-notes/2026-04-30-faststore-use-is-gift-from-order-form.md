---
title: "FastStore: Gift detection with useIsGiftFromOrderForm"
slug: "2026-04-23-faststore-use-is-gift-from-order-form"
type: added
createdAt: "2026-04-23T00:00:00.000Z"
updatedAt: "2026-04-24T00:00:00.000Z"
hidden: false
excerpt: "FastStore now supports the experimental `useIsGiftFromOrderForm` flag, allowing stores to detect gift items using the Order Form `isGift` field instead of relying on a zero-price check."
tags:
  - FastStore
---

FastStore now supports the experimental `useIsGiftFromOrderForm` flag, giving stores a more reliable way to detect gift items in the cart.

## What has changed?

Previously, FastStore determined whether a cart item was a gift by checking if its price was zero (`item.price === 0`). With this change, you can now configure FastStore to use the `isGift` field directly from the VTEX Order Form item.

| Behavior | `useIsGiftFromOrderForm: false` (default) | `useIsGiftFromOrderForm: true` |
|---|---|---|
| Gift detection method | Checks if `item.price === 0` | Reads `item.isGift` from the Order Form |

## Why did we make this change?

Some stores configure gift items in the VTEX Order Form directly without setting their price to zero. In these cases, the price-based detection would fail to identify the items as gifts, causing them to be displayed and totaled incorrectly in the cart. This flag provides a more accurate alternative for stores that rely on the Order Form's `isGift` field.

## What needs to be done?

This is an opt-in experimental feature. To enable it in your store, follow the instructions in [Handling gift items in the cart](https://developers.vtex.com/docs/guides/faststore/developer-tools-use-is-gift-from-order-form).
