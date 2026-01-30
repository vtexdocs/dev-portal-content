---
title: "FastStore: Cart and session management improvements"
slug: "2026-01-30-faststore-cart-and-session-management-fixes"
type: "fixed"
createdAt: "2026-01-30T00:00:00.000Z"
updatedAt: "2026-01-30T00:00:00.000Z"
excerpt: "FastStore now ensures carts are cleared after checkout, logout fully removes all browser storage and cookies, and several internal fixes improve cart validation and address shipping address errors. These changes enhance session security, cart consistency, and developer experience."
tags:
    - FastStore
---

Store using FastStore now receives improvements to cart and session management with fixes that enhance security and data consistency. These updates ensure carts are properly cleared after checkout, logout removes all browser storage and cookies, and cart validation no longer causes infinite loops when using regionalization with logged-in users.

## What has changed?

### Cart cleared after checkout

The cart now automatically clears after an order is successfully placed. If the checkout cookie is missing or invalid, FastStore creates a new cart instead of reusing stale data.

This prevents purchased items from remaining in the cart and ensures a clean post-checkout experience, avoiding any purchased items lingering in the cart between orders.

### Complete logout storage cleanup

Logging out now performs comprehensive cleanup of all client-side and server-side storage:

- **Client-side storage:**
  - `sessionStorage` (including FastStore-specific keys)
  - `localStorage`
  - `IndexedDB` (`keyval-store` database)
  - All VTEX-related cookies via JavaScript

- **Server-side cookies (via `/api/fs/logout` endpoint):**
  - All HttpOnly cookies containing "vtex"
  - `CheckoutOrderFormOwnership` cookie
  - `vid_rt` cookie (when refresh token is enabled)

This closes security gaps and prevents data leakage between sessions by ensuring no residual cart, session, or shopper data remains after logout, providing complete session isolation for better security and privacy.

### Cart validation infinite loop fix

The cart validation logic was updated to prevent infinite revalidation loops when:

- A user is logged in
- Regionalization (`postalCode`) is active

The fix ensures that only meaningful cart changes trigger updates, and shipping simulation is always refreshed when actually needed. This reduces confusing errors, prevents unnecessary API calls, and eliminates UI flickering from repeated validation, resulting in a smoother cart experience for logged-in users in regionalized stores.

### Shipping address robustness

The shipping resolver now safely handles missing `neighborhood` fields in addresses using optional chaining (`address?.neighborhood`).

Some addresses may not include a neighborhood value, which previously caused GraphQL errors. This change enables more reliable shipping calculations and fewer edge-case errors.

## Why did we make these changes?

These changes address the following:

- **Cart and session consistency:** Ensuring carts are cleared after checkout and all storage is removed on logout prevents stale or sensitive data from persisting, improving security and user trust.
- **Developer experience:** The cart validation and shipping resolver fixes reduce confusing errors and unnecessary UI updates, making integrations more predictable and robust.

## What needs to be done?

These fixes are backward-compatible. However, review the following if your store has customizations:

### Cart and checkout integrations

If your custom code reads cart data from IndexedDB or sessionStorage after checkout, assumes the cart will persist after order placement, or has tests that expect cart items to remain after checkout:

- Update your logic to expect an empty cart after order placement.
- Update tests to reflect the new cart clearing behavior.
- Verify that your checkout success page doesn't rely on cart data.

### Custom logout flows

If you have custom session management logic, custom storage mechanisms for user data, or integrations that depend on specific cookies or storage keys:

- Test your logout flow to ensure all custom storage is cleared.
- Verify that your custom cookies are included in the cleanup.
- Check that no sensitive data persists after logout.

### Shipping address handling

If your custom code assumes the `neighborhood` field is always present in addresses, formats or displays address information, or performs validation on address fields:

- Update your code to handle missing or empty `neighborhood` values.
- Use optional chaining: `address?.neighborhood`.
- Test with addresses that don't include neighborhood data.
