---
title: "FastStore: Cart and session management fixes"
slug: "2026-02-04-faststore-cart-and-session-management-fixes"
type: "fixed"
createdAt: "2026-02-04T00:00:00.000Z"
updatedAt: "2026-02-04T00:00:00.000Z"
excerpt: "FastStore clears carts after checkout, fully removes storage and cookies on logout, and fixes cart validation."
tags:
    - FastStore
---

Stores using FastStore now benefit from fixes to cart and session management that improve security and data consistency. These updates ensure carts are properly cleared after checkout, logout removes all browser storage and cookies, and cart validation no longer causes infinite loops when using the location-based behavior for logged-in users.

## What has changed?

### Cart cleared after checkout

The cart now automatically clears after an order is successfully placed. If the checkout cookie is missing or invalid, FastStore creates a new cart instead of reusing stale data.

This prevents purchased items from remaining in the cart and ensures a clean post-checkout experience and avoids items left in the cart between orders.

### Complete logout storage cleanup

Logging out now clears all client-side and server-side storage:

- **Client-side storage:**
  - `sessionStorage`
  - `localStorage`
  - `IndexedDB`
  - All VTEX-related cookies via JavaScript.

- **Server-side cookies:** All relevant server-side cookies.

This improves security by ensuring no cart, session, or shopper data remains after logout, preventing data from carrying between sessions.

### Cart validation infinite loop

The cart validation logic was updated to prevent infinite revalidation loops when:

- A user is logged in.
- Location-based behavior using `postalCode` is active.

The fix updates the cart only when changes affect totals or shipping (for example, changing item quantity) and refreshes shipping simulation only when needed. This reduces errors and prevents interface flicker for logged-in users in stores that base cart and shipping information on the shopper's postal code.

## Why did we make these changes?

These updates improve security, data consistency, and developer experience by keeping carts and sessions clean and preventing unnecessary cart revalidation.

## What needs to be done?

These fixes should not break existing setups. To receive these fixes, update the FastStore packages to the latest version by running `yarn upgrade -L --scope @faststore`.

If your store has customizations, review the following:

### Cart and checkout integrations

If your custom code reads cart data from `IndexedDB` or `sessionStorage` after checkout, assumes the cart will persist after order placement, or has tests that expect cart items to remain after checkout:

- Update your logic to expect an empty cart after order placement.
- Update tests to reflect the new cart clearing behavior.
- Verify that your checkout success page doesn't rely on cart data.

### Custom logout flows

If you have custom session management logic, custom storage mechanisms for user data, or integrations that depend on specific cookies or storage keys:

- Test your logout flow to ensure all custom storage is cleared.
- Verify that your custom cookies are included in the cleanup.
- Check that no sensitive data persists after logout.
