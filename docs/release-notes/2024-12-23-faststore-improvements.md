---
title: "FastStore: Performance improvements for mobile devices"
slug: "2024-12-23-faststore-improvements"
hidden: false
type: "added"
createdAt: "2024-12-23T00:00:00.219Z"
excerpt: "Improved performance experience for FastStore stores."
---

To boost mobile performance, the FastStore team made several optimizations, which resulted in higher Lighthouse performance scoring for FastStore stores from  64 to 95 after the improvements.

## What has changed?

The main focus of performance improvements was to optimize the homepage on mobile devices. Below are the key changes introduced:

### Preact (experimental feature)

[Preact](https://preactjs.com/) is a lightweight alternative to React that improves performance by reducing the size of the JavaScript bundle.

For implementation details, see the [Improving store performance with Preact](https://developers.vtex.com/docs/guides/faststore/managing-performance-improving-store-performance-with-preact) guide.

### Removal of unused libraries

Libraries like `chalk` and `nextjs-progressbar` have been removed from the codebase to reduce the initial bundle size.

### Lazy loading

Lazy loading has been implemented for sections outside the viewport, such as CartSidebar and RegionModal, improving initial load times. This feature currently works only for native sections.

### Optimizing website load times

To enhance website responsiveness and speed, we implemented the following:

- **Preconnect & Prefetch:** Browser directives that establish early connections to external resources (fonts, images) and prioritize their fetching, resulting in faster loading times.
- **Dynamic Imports:** Using [next/dynamic](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading#nextdynamic) to load components efficiently, reducing the impact on initial page load size.
- **On-demand Analytics:** Analytics events (triggered by the `sendAnalyticsEvent` method) are now dynamically imported from the `faststore/sdk` library, meaning that these analytics scripts are only loaded when an event is triggered, reducing the initial payload and improving load performance.

## Why did we make this change?

Performance is crucial for a positive user experience. While desktop performance was strong, mobile performance needed improvement. This release aims to bridge this gap and ensure a consistent, high-performance experience across all devices.

## What needs to be done?

These improvements are available in FastStore version `3.0.112`. To take advantage of these updates, follow these steps:

1. Open your FastStore project using your preferred code editor.
2. Update your FastStore project to version `3.0.112` or later by running the following:

   ```bash
   yarn upgrade -L --scope @faststore
   ```

3. Run `yarn build`.
