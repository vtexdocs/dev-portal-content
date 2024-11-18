---
title: "Lazy loading components"
slug: "vtex-io-documentation-using-the-fold-blocks"
hidden: false
createdAt: "2020-06-03T16:02:44.215Z"
updatedAt: "2022-12-13T20:17:44.156Z"
seeAlso:
  - "/docs/guides/vtex-io-documentation-best-practices-for-optimizing-performance"
---

Store Framework provides two key blocks, `__fold__` and the `__fold__.experimentalLazyAssets`, to improve your store’s performance by optimizing how components are loaded. By implementing these blocks effectively, you can enhance your store’s initial loading time and overall user experience.

- `__fold__`: determines the priority of loading interface components, defining which elements load first and which load dynamically as users scroll down the page.
- `__fold__.experimentalLazyAssets` (optional): keeps specified components statically loaded until the user's first interaction, offering additional flexibility in load management.

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

In this configuration:

- Components above `__fold__` (e.g., `carousel#home`) will load immediately.
- Components below `__fold__` (e.g., `shelf#home`, `info-card#home`) will load dynamically as the user scrolls.

> Note: Use `__fold__` only on scrollable pages. Non-scrollable pages do not benefit from this optimization.

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

In this configuration:

- On mobile, only `carousel#home` loads initially.
- On desktop, both `carousel#home` and `shelf#home` load initially.

> ⚠️ **SEO considerations:** Google may not index content under the `__fold__` block. Ensure all critical SEO-relevant components are placed above the `__fold__` block.

## (Optional) Using the `__fold__.experimentalLazyAssets` block

> ❗ This block is experimental and may cause side effects, such as failing to render an interactive component in the storefront. 

Add the `__fold__.experimentalLazyAssets` above the blocks you want to defer. Consider adding this block to your store's home page for optimal results. For example:

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

> ⚠️ Ensure `__fold__.experimentalLazyAssets` is below interactive components (e.g., `carousel`) to avoid rendering or navigation issues. 

## Best practices

- **Prioritize above-the-fold content**: Ensure that critical components, such as banners or carousels, are placed above the `__fold__` block so they load quickly and are indexed by search engines.
- **Separate mobile and desktop configurations**: Use `__fold__.mobile` and `__fold__.desktop` blocks to adjust the loading sequence based on the device, optimizing the experience for both mobile and desktop users.
- **Monitor store performance**: Use tools like Google Lighthouse to evaluate the impact of lazy loading and fine-tune your configurations.
- **SEO awareness**: Keep SEO-critical components, such as metadata and key textual content, above the `__fold__` block to ensure they are indexed by search engines.
- **Use `__fold__.experimentalLazyAssets` carefully**: This block is experimental and may cause rendering or interaction issues. Always test thoroughly before deploying to production.
- **Lazy load images and product data**: For scenarios where you need to [lazy load images and product data in a slider](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-optimizing-performance#lazy-loading-images-and-products-data-in-a-slider), consider [building a carousel using Slider Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout).
