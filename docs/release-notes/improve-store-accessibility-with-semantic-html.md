---
title: "Store Framework: Improve store accessibility with semantic HTML"
slug: "improve-store-accessibility-with-semantic-html"
hidden: false
type: "added"
createdAt: "2025-12-05T00:00:00.219Z"
excerpt: "Store Framework components can now be rendered with semantic HTML via a new migration flag."
---

Store Framework now supports enhanced accessibility through the new `a11ySemanticHtmlMigration` flag. When enabled, this flag updates the markup of Store Framework components to use semantic HTML elements, improving accessibility without introducing breaking changes to existing storefronts.

## What has changed?

Previously, Store Framework components used generic HTML elements, which made it difficult for screen readers and other assistive technologies to interpret the page structure and functionality.

When the new accessibility flag is enabled and implemented in your Store Framework components, semantic HTML elements are used to clearly communicate their purpose to assistive technologies, ensuring clear communication. For example:

- Form labels are correctly linked with their inputs, helping screen reader users understand what information to enter.
- Interactive elements are distinctly recognized, enhancing keyboard navigation.
- Page structure is more logical and consistent for users with disabilities.

## Why did we make this change?

This change ensures that all shoppers can successfully navigate and purchase from your store, regardless of the assistive technologies they use, including:

- **Improved customer experience:** Shoppers using screen readers, voice control software, or keyboard navigation can more easily browse products, complete forms, and make purchases.
- **Compliance readiness:** Helps your store align with WCAG 2.1 accessibility standards and legal requirements.
- **Better SEO:** Semantic HTML also improves how search engines understand and index your content.

## What needs to be done?

For detailed implementation instructions, see the [Improving store accessibility with semantic HTML migration](https://developers.vtex.com/docs/guides/vtex-io-documentation-semantic-html-migration) guide.
