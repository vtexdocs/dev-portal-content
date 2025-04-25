---
title: "Lazy loading components"
slug: "vtex-io-documentation-using-the-fold-blocks"
hidden: false
createdAt: "2020-06-03T16:02:44.215Z"
updatedAt: "2025-03-14T20:10:20.775Z"
seeAlso:
  - "/docs/guides/vtex-io-documentation-enabling-performance-settings"
---

In this guide, you’ll learn how to use the `__fold__` and `__fold__.experimentalLazyAssets` blocks to optimize component loading and improve store performance. Below is an overview of these blocks:

| Block                          | Description                                                                                              | Instructions |
|--------------------------------|----------------------------------------------------------------------------------------------------------|--------------|
| `__fold__`                     | Determines the loading priority of interface components, and defines which elements load first and which load dynamically as users scroll down the page. | [Using the `__fold__` block](#using-the-fold-block) |
| `__fold__.experimentalLazyAssets` | (Optional) Keeps specified components statically loaded until the user's first interaction, offering additional flexibility in load management. | [(Optional) Using the `__fold__.experimentalLazyAssets` block](#optional-using-the-fold-experimentalLazyAssets-block) |

By implementing these blocks effectively, you can enhance store initial loading time and overall user experience.

## Using the `__fold__` block

Add the `__fold__` block to any store theme templates you want, such as `store.product` and `store.home`. For example:

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

- Components above `__fold__` (for example, `carousel#home`) will load immediately.
- Components below `__fold__` (for example, `shelf#home`, `info-card#home`) will load dynamically as the user scrolls.

>ℹ️ Use `__fold__` only on scrollable pages. Non-scrollable pages don’t benefit from this optimization.

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

> ❗ This block is experimental and may cause unexpected effects, such as failing to render an interactive component in the storefront.

Add the `__fold__.experimentalLazyAssets` above the blocks you want to defer. Consider adding this block to the store homepage for optimal results. For example:

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

> ⚠️ Make sure `__fold__.experimentalLazyAssets` is below interactive components (for example, `carousel`) to avoid rendering or navigation issues.

## Best practices

- **Prioritize above-the-fold content:** Make sure that critical components, such as banners or carousels, are placed above the `__fold__` block so they load quickly and are indexed by search engines.
- **Optimize for different devices:** Use `__fold__.mobile` and `__fold__.desktop` blocks to adjust the loading sequence based on the device, optimizing the experience for both mobile and desktop users.
- **Monitor store performance:** Use tools like Google Lighthouse to evaluate the impact of lazy loading and fine-tune your configuration. Learn more in [Performance](https://developers.vtex.com/docs/guides/storefront-performance).
- **Ensure SEO visibility:** Position essential SEO elements, such as metadata and key textual content, above the `__fold__` block to ensure they are indexed by search engines. Learn more in [SEO](https://developers.vtex.com/docs/guides/storefront-seo).
- **Use `__fold__.experimentalLazyAssets` carefully:** This block is experimental and may cause rendering or interaction issues. Always test thoroughly before deploying to production.
- **Lazy load images and product information efficiently:** For scenarios where you need to [lazy load images and product information in a slider](https://developers.vtex.com/docs/guides/vtex-io-documentation-enabling-performance-settings#manual-optimizations), consider [building a carousel using Slider Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout).
