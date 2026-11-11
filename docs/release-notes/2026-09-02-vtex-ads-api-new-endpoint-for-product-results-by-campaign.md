---
title: "VTEX Ads API: New endpoint for product results by campaign"
slug: "2026-09-02-vtex-ads-api-new-endpoint-for-product-results-by-campaign"
hidden: false
type: "added"
createdAt: "2026-09-02T12:00:00.000Z"
excerpt: "The VTEX Ads API now offers the Get product results by campaign endpoint, which returns per-product (SKU) impressions, clicks, views, conversions, and attributed ad spend for a single campaign over a date range."
---

The **[VTEX Ads API](https://developers.vtex.com/docs/api-reference/vtex-ads-api)** now offers a new operation, Get product results by campaign (`GET /product/results`), documented in the API Reference. It returns performance metrics for each SKU linked to a campaign, aggregated over an inclusive date range.

## What has changed?

- The new operation is `GET /product/results` (with `campaign_id` as a query parameter), listed under the `Reports` tag.
- Each item in the response carries product identity fields, including `product_sku`, which identifies the product, and performance metrics, including `impressions`, `clicks`, and `conversions_value`.
- Metric values are returned as numeric strings, not as numbers.
- The `start_date` and `end_date` parameters are inclusive and both default to the current date when omitted, so a call without them returns data for that date only.
- Results are paginated and sorted with the `page`, `quantity`, `order_by`, and `order_direction` parameters. Setting `count=false` returns a bare array of products instead of the `total`, `pages`, `currentPage`, and `data` envelope.
- This operation returns results per product (SKU) for one campaign, unlike [Get ads performance report](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/ad/results/v2), which returns results per ad across campaigns, and unlike [Get campaign details](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/campaign/-campaign_id-), which returns campaign-level totals.

## What needs to be done?

No action is required for existing integrations, because this is a new endpoint and no existing endpoint changed behavior.

To adopt it, call the operation with the campaign UUID in the `campaign_id` query parameter, authenticating with the same `X-App-Id` and `X-Api-Key` headers used by the other `Reports` endpoints.

## Learn more

- [Exporting ads reports](https://developers.vtex.com/docs/guides/exporting-ads-reports) guide, for general `Reports` context.
- [VTEX Ads API](https://developers.vtex.com/docs/api-reference/vtex-ads-api) reference.
- [Get product results by campaign](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/product/results) in the API Reference.
