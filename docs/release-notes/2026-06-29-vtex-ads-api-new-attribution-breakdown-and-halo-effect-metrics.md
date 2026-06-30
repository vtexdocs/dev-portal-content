---

## title: "VTEX Ads API: New attribution breakdown and halo effect metrics"

slug: "2026-06-29-vtex-ads-api-new-attribution-breakdown-and-halo-effect-metrics"
hidden: false
type: "added"
createdAt: "2026-06-29T12:00:00.000Z"
excerpt: "Starting July 1, 2026, the Ads API will return view-attributed and halo effect metric breakdowns across campaigns, ad groups, and ads. The ROAS field will reflect a consolidated click-and-view attribution model across all ad formats, and for Sponsored Products this means a change from the previous click-only model."

Starting **July 1, 2026**, the **VTEX Ads API** `metrics` object, returned in campaign, ad group, and ad responses, will include new fields that break down performance by attribution type and expose halo effect data. Additionally, the `roas` field will reflect a consolidated click-and-view attribution model across all ad formats.

## What has changed?

The following fields have been added to the `metrics` object across campaign, ad group, and ad responses:

### Conversion breakdowns

- `conversions_click`: Number of conversions attributed to clicks
- `conversions_view`: Number of conversions attributed to views

### Conversion rate breakdowns

- `conversion_rate_click`: Conversion rate attributed to clicks
- `conversion_rate_view`: Conversion rate attributed to views

### ROAS breakdowns

- `roas_click`: ROAS attributed to clicks
- `roas_view`: ROAS attributed to views
- `roas_halo`: ROAS attributed to halo effect purchases
- `roas_overall`: Overall ROAS combining all attribution types

### Halo effect metrics

- `halo_revenue`: Revenue generated from halo effect purchases
- `halo_orders`: Number of orders from halo effect purchases
- `halo_items`: Number of items from halo effect purchases

The `roas` field will reflect a consolidated click-and-view attribution model across all ad formats. 

## What needs to be done?

- If your integration reads the `roas` field for Sponsored Products campaigns, expect higher values starting July 1, 2026. The increase reflects the addition of view-attributed revenue, not a change in ad performance.
- Optionally, update your dashboards or analytics pipelines to consume the new granular fields (`roas_click`, `roas_view`, `roas_halo`, `roas_overall`, `conversion_rate_click`, `conversion_rate_view`) for attribution-level breakdowns.
- No action is required to receive the new fields: they are returned automatically in existing API responses.

> ℹ️ Learn more about the VTEX Ads metrics change in the announcement: [New ROAS calculation methodology for Sponsored Products](https://help.vtex.com/announcements/2026-07-01-new-roas-calculation-methodology-for-sponsored-products).

