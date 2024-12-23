---
title: "FastStore: Performance improvements for mobile devices"
slug: "2024-12-23-faststore-improvements"
hidden: false
type: "added"
createdAt: "2024-12-23T00:00:00.219Z"
excerpt: "Improved performance experience for FastStore stores."
---

FastStore has undergone significant optimizations to improve mobile performance, achieving a Lighthouse score improvement from 64 to 95.

## What has changed?

The main focus of these enhancements is on optimizing the homepage experience for mobile users. Below are the key changes introduced:

### Preact (experimental feature)

FastStore now supports [Preact](https://preactjs.com/), a lightweight alternative to React that improves performance by reducing the JavaScript bundle size.

[After updating your FastStore project version](#what-needs-to-be-done) to `3.0.112` or later, see the [Improving store performance with Preact](https://developers.vtex.com/docs/guides/faststore/managing-performance-improving-store-performance-with-preact) guide to enable Preact.

### Removal of unused libraries

Libraries like `chalk` and `nextjs-progressbar` have been removed from the codebase to reduce the initial bundle size.

### Lazy loading

Lazy loading has been implemented for sections outside the viewport, such as CartSidebar and RegionModal, improving initial load times. This feature currently works only for native sections.

### Optimizing website load times

Several techniques have been implemented to enhance loading speeds and responsiveness:

- **Preconnect and prefetch:** Browser directives that establish early connections to external resources (fonts, images) and prioritize their fetching, resulting in faster loading times.
- **Dynamic imports:** Using [next/dynamic](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading#nextdynamic) to load components efficiently, reducing the impact on initial page load size.
- **On-demand analytics:** Analytics scripts, triggered by the `sendAnalyticsEvent` method, are now dynamically imported from the `faststore/sdk` library. This ensures that these scripts are loaded only when needed, reducing the initial payload size.

## Why did we make this change?

This release brings significant improvements to mobile performance, ensuring FastStore delivers a consistently high-quality experience across all devices. Desktop performance remains robust, and mobile users will now benefit from enhanced speed and responsiveness.

## What needs to be done?

These improvements are available in FastStore version `3.0.112`. To take advantage of these updates, follow these steps:

1. Open your FastStore project using your preferred code editor.
2. Update your FastStore project to version `3.0.112` or later by running the following:

   ```bash
   yarn upgrade -L --scope @faststore
   ```

3. Run `yarn build`.
