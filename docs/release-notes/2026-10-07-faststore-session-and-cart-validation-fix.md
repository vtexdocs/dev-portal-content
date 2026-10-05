---
title: "FastStore: Fixed session and cart validation after region changes"
slug: "2026-10-07-faststore-session-and-cart-validation-fix"
type: "fixed"
excerpt: "FastStore now keeps interface-only fields out of session and cart requests, restoring validation and Checkout synchronization after shoppers set their location."
createdAt: "2026-10-07T00:00:00.000Z"
updatedAt: "2026-10-07T00:00:00.000Z"
tags:
  - FastStore
---

FastStore now validates sessions and carts correctly after shoppers set their location through the region modal, popover, or slider. This fix restores cart synchronization with Checkout for affected shoppers.

## What has changed?

Before, setting a postal code could save the interface-only `hasValidated` field in the shopper's session. Because this field isn't part of the session input accepted by the API, subsequent `ValidateSession` and `ValidateCartMutation` requests failed with a 500 error. The invalid session remained in IndexedDB, preventing the cart from synchronizing with Checkout until the shopper cleared their browser data.

FastStore now removes interface-only fields (`isSessionReady`, `isValidating`, and `hasValidated`) before sending session data to session validation, cart validation, and reorder requests. The same normalization is applied when updating the shopper's region or storing the session.

Sessions that already contain these fields can validate again without shoppers clearing their browser data. The fields are removed from IndexedDB the next time the session is updated.

## Why did we make this change?

Interface state is used only to control storefront behavior and shouldn't be sent as part of the API session input. Keeping these fields separate prevents GraphQL validation errors and ensures that session and cart updates continue to reach Checkout after a shopper changes their location.

## What needs to be done?

Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to FastStore `v4.9.2`. No additional configuration is required.
