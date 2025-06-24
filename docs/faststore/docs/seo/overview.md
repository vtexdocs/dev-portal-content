---
title: "SEO"
---

Search Engine Optimization (SEO) is one of the most essential strategies for improving your site's visibility in organic search engine results. Well-optimized pages are more likely to appear in prominent positions on search engines, leading to higher traffic and better conversion rates.

>ℹ Learn about best practices for improving your store SEO in the [SEO](https://developers.vtex.com/docs/guides/storefront-seo) guide.

FastStore provides configuration options, such as editable meta tags (title, description, author, and templates), which help search engines understand and index your content. You can define these settings during the [project onboarding](#setting-seo-during-the-project-onboarding) or [updated later](#managing-seo-for-plps-and-pdps) in the `discovery.config.js` file.

## Setting SEO during the project onboarding

When [starting a new FastStore project](https://developers.vtex.com/docs/guides/faststore/1-onboarding-starting-the-project), you should configure your website's SEO tags by setting values for the **Title Tag**, **Description Tag**, **Title Template**, and **Site Author**. These tags are part of your site's optimization strategy.

![seo-onboarding-fs](https://vtexhelp.vtexassets.com/assets/docs/src/seo-onboarding-fs___62053a279d984f508761d22b56c03ac7.png)

### Default SEO settings

The default SEO values are defined in the [`discovery.config.js`](https://developers.vtex.com/docs/guides/faststore/project-structure-config-options) file of your store. When you configure these settings in WebOps during the onboarding process, this file is automatically updated. Example:

```javascript
 seo: {
    title: 'FastStore Starter',
    description: 'Fast Demo Store',
    titleTemplate: '%s | FastStore',
    author: 'Store Framework',
  },
```

## Managing SEO for PLPs and PDPs

After completing the onboarding process, you can update the SEO settings using the [`discovery.config.js`](https://developers.vtex.com/docs/guides/faststore/project-structure-config-options). In this file, you can update the title and description templates for both Product Listing Pages (PLPs) and Product Detail Pages (PDPs).
For detailed instructions, see the [Configuring SEO for PLPs and PDPs](https://developers.vtex.com/docs/guides/faststore/seo-configuring-seo-for-plp-and-pdp) guide.

Additionally, you can improve performance and SEO by controlling lazy loading for custom sections. Learn more in [Optimizing SEO by managing lazy loading on PLPs and PDPs](https://developers.vtex.com/docs/guides/faststore/seo-optimizing-seo-by-managing-lazy-loading-on-plp-and-pdp).
