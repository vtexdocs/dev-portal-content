---
title: "Ads API: attribution and halo effect metrics in report responses"
slug: "2026-07-01-ads-api-attribution-and-halo-effect-metrics"
hidden: false
type: "added"
createdAt: "2026-07-01T12:00:00.000Z"
excerpt: "The Ads API now returns attribution breakdowns by click and view, plus halo effect metrics, in campaign, ad group, and ad report responses."
---

Starting July 1, 2026, the **Ads API** returns new attribution and halo effect metrics in the campaign, ad group, and ad report responses of the [Get ads](https://developers.vtex.com/docs/api-reference/ads-api) endpoint group. This release accompanies the launch of view attribution for product ads (Sponsored Products).

## What has changed?

- Product ads now support view attribution in addition to click attribution. Click conversions use a 7-day window and view conversions use a 1-day window.
- The `roas` field is now a consolidated metric that combines click-attributed and view-attributed revenue.
- New attribution breakdown fields: `roas_click`, `roas_view`, `conversion_rate_click`, and `conversion_rate_view`.
- New halo effect fields: `roas_halo`, `roas_overall`, `halo_revenue`, `halo_orders`, and `halo_items`.

All metric fields, including `halo_orders` and `halo_items`, are returned as strings.

## What needs to be done?

1. No action is required. The new fields are additive and existing integrations keep working.
2. If your integration compares ROAS across periods, note that data before July 1, 2026 keeps the previous click-only calculation for product ads.

## Learn more

- [Understanding ads events](https://developers.vtex.com/docs/guides/understanding-ads-events)
- [Ads API reference](https://developers.vtex.com/docs/api-reference/ads-api)
