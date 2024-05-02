---
title: "Lazy loading components"
slug: "vtex-io-documentation-using-the-fold-blocks"
hidden: false
createdAt: "2020-06-03T16:02:44.215Z"
updatedAt: "2022-12-13T20:17:44.156Z"
seeAlso:
  - https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-optimizing-performance
---

Store Framework provides two key blocks, `__fold__` and the `__fold__.experimentalLazyAssets`, designed to enhance your website's performance. These blocks significantly influence the initial loading performance of the configured page, ultimately enhancing the overall user experience on your storefront.

- `__fold__`: determines the priority of loading interface components, specifying which ones render first and which load concurrently with user scrolling.
- `__fold__.experimentalLazyAssets` (optional): specifies components that remain statically loaded until the initial user interaction occurs, offering flexibility in optimizing the loading strategy.

This guide will walk you through the effective use of these blocks.

## Using the `__fold__` block

Add the `__fold__` block to your store theme's desired templates, such as `store.product` and `store.home`. For example:

```diff
"store.home": {
  "blocks": [
    "carousel#home",
+   "__fold__",
    "shelf#home",
    "info-card#home",
    "rich-text#question",
    "rich-text#link",
    "newsletter"
  ]
},
```

Once added, all blocks below the `__fold__` block will load components only with user scrolling. Hence, this block should be used only when your page is scrollable.

### Device-specific configuration

You can customize scenarios for mobile and desktop modes using `__fold__.mobile` and `__fold__.desktop`:

```diff
"store.home": {
  "blocks": [
    "carousel#home",
+   "__fold__.mobile",
    "shelf#home",
+   "__fold__.desktop",
    "info-card#home",
    "rich-text#question",
    "rich-text#link",
    "newsletter"
  ]  
},
```

In this example, the `carousel` and the `shelf`  will be displayed with the first meaningful paint on desktop mode, while for mobile users, only the `carousel` will load initially.

> ⚠️ Google may not track content under the `__fold__` block for SEO purposes. Hence, make sure to place all SEO-relevant information above the `__fold__` block.

## Optional: Using the `__fold__.experimentalLazyAssets` block

> ⚠️ Use the `__fold__.experimentalLazyAssets` block with caution as it's experimental and may cause side effects, such as failing to render an interactive component in the storefront. For scenarios where you need to [lazy load images and product data in a slider](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-optimizing-performance#lazy-loading-images-and-products-data-in-a-slider), consider [building a carousel using Slider Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout).

In the template's block list, add the `__fold__.experimentalLazyAssets` above the blocks whose loading will be static until the user's first interaction. Consider adding this block to your store's home page for optimal results. For example:

```diff
"store.home": {
  "blocks": [
    "carousel",
+   "__fold__.experimentalLazyAssets", 
    "flex-layout.row#homeBrands",
    "flex-layout.row#homeBanner",
    "__fold__",
    "tab-layout#home",
    "tab-layout#home2",
    "carousel#homeFooter"
  ]
},
```

> ⚠️ Ensure adding it below blocks with interactive components like the `carousel` to prevent potential issues with proper functioning and user navigation.
