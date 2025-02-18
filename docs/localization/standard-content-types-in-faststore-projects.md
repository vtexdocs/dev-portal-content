---
title: "Standard Content Types in FastStore projects"
createdAt: "2025-02-18T19:02:14.003z"
---

Headless CMS [Content Types](https://developers.vtex.com/docs/guides/faststore/headless-cms-3-adding-content-types-and-sections#step-2-adding-content-types-to-the-headless-cms) are the building blocks for creating a scalable and maintainable storefront in FastStore. After onboarding via the [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) app, these Content Types are pre-implemented in your starter store, enabling you to quickly build pages like the Home, Product Listing, and Custom Landing.

Content Types are organized by [Scopes](https://developers.vtex.com/docs/guides/faststore/headless-cms-managing-content-with-scopes-and-requiredscopes#scopes), which define the context in which each Content Type can be used. They categorize Content Types based on their functionality. For example, a Content Type with a `pdp` scope can only be used on PDPs.

The following table provides an overview of the standard Content Types, their IDs, scopes, and their respective purposes.

> ℹ These standard Content Types are natively implemented. You can view their structure in the [content-types.json](https://github.com/vtex/faststore/blob/main/packages/core/cms/faststore/content-types.json) file.

| **Content Type** | **ID** | **Scopes** | **Purpose** |
| ------------------------------- | -------- | --------------- | --------------- |
| Global Sections | `globalSections` | `global` | Defines reusable sections that appear across pages. |
| Global Header Sections | `globalHeaderSections` | `global` | Defines the content for the global header, displayed at the top of every page. |
| Global Footer Sections | `globalFooterSections` | `global` | Defines the content for the global footer, displayed at the bottom of every page. |
| Landing Page | `landingPage` | `landing` and `custom` | Creates custom landing pages with SEO optimization. |
| Home | `home` | `home` | Defines the structure and SEO metadata for the home page. |
| Product Page | `pdp` | `pdp` | Defines the structure and template for Product Detail Pages (PDP). |
| Product List Page | `plp` | `plp` | Defines the structure and settings for Product Listing Pages (PLP). |
| Search Page | `search` | `plp` and `search` | Defines the structure and settings for search results pages. |
| Login | `login` | - | Defines the structure for the login page. |
| Error 500 | `500` | - | Defines the structure for the 500 Internal Server Error page. |
| Error 400 | `400` | - | Defines the structure for the 400 pages, including the 404 Not Found Error page. |
