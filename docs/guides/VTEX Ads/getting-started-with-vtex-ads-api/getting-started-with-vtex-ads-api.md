---
title: "Getting started with VTEX Ads API"
slug: "getting-started-with-vtex-ads-api"
hidden: false
excerpt: "Learn how to integrate VTEX Ads into your store."
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2026-11-26T03:35:25.400Z"
tags:
  - VTEX Ads
---

The **VTEX Ads API** serves as the central point of integration between VTEX Ads and the retailer's platform, enabling the display of advertisements to consumers.

## Instructions

Built using REST architecture, this API allows your platform to:

- Synchronize the product catalog with VTEX Ads to ensure up-to-date product and inventory data.
- Request ads to be displayed on your ecommerce, marketplace, or app.
- Send event notifications such as impressions, views, clicks, and conversions to help track ad performance and attribute results.

Currently, VTEX Ads supports three ad formats:

- **Sponsored Products (Product Ads)**: Ads that highlight individual SKUs, typically shown in search or category pages.
- **Sponsored Brands**: [GAP: a description of this ad format is not stated. Expected source: the Retrieving ads API guide's format descriptions. That guide was not among the sources provided for this draft.]
- **Banner Display (Banner Ads)**: Visual ads that promote brands or campaigns in designated areas of your site.

The JavaScript SDK does not yet support banners or sponsored brands. See [VTEX Ads JavaScript SDK](https://developers.vtex.com/docs/guides/vtex-ads-javascript-sdk).

For a simplified Banner and Video ads setup, see [Implementing transparent integration for VTEX Ads](https://developers.vtex.com/docs/guides/implementing-transparent-integration-for-vtex-ads).
