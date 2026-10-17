---
title: "Understanding attribution windows and conversion models"
slug: "attribution-window-and-conversion-models"
hidden: false
createdAt: "2026-10-08T00:00:00.000Z"
updatedAt: "2026-10-08T00:00:00.000Z"
excerpt: "Learn how attribution windows, measurement events, billing models, and attribution rules determine which campaign receives credit for a conversion."
tags:
  - VTEX Ads
---

In this guide, you will learn how conversions are attributed to VTEX Ads campaigns and how those campaigns are billed. It covers the attribution window, the distinction between measurement and billing, the attribution decision hierarchy, how products map to attributed campaigns, and the reporting latency you should expect.

## Before you begin

This guide assumes familiarity with the VTEX Ads campaign types referenced throughout: Product Campaigns (Product Ads), Banner, Video, and Sponsored Brands. Understanding these campaign types helps you interpret the measurement-event and billing-model differences explained in the following section.

## Instructions

### Step 1 — Understand the attribution window

The attribution window, also called the conversion window, is the time period after a user interacts with an ad, either by clicking or viewing it, during which a resulting conversion can be credited to that ad.

The default attribution window is 14 days. This default applies to all campaigns, but it can be customized according to strategic needs.

For example, if a user clicks on an ad today, any purchase of the associated product made within the next 14 days can be attributed to that ad.

### Step 2 — Distinguish measurement events from billing models

It is essential to differentiate the event used to measure attribution, which determines whether a conversion counts, from the event that generates billing, which determines what the advertiser pays for.

Measurement events vary by campaign type:

- **Product Campaigns (Product Ads)** are measured by click. A conversion only counts if the user clicked on the ad before purchasing.
- **Other campaigns (Banner, Video, and Sponsored Brands)** are measured by view (impression). A conversion can count even if the user only saw the ad, following the hierarchy rules described in Step 3.

Billing models also vary by campaign type:

- **CPC (Cost Per Click)** charges the advertiser each time a user clicks on the ad. It is used in Product Campaigns and Sponsored Brands.
- **CPM (Cost Per Thousand Impressions)** charges the advertiser a fixed amount for every 1,000 times the ad is displayed. It is used in Banner, Video, and Sponsored Brands.
- **Hybrid model (CPC + CPM)** applies to Sponsored Brands campaigns, which charge for both clicks and impressions generated.

CPM defines the value for 1,000 impressions, but the actual charge is proportional to each individual impression. For example, a campaign with a CPM of $10.00 that generates 10 impressions is billed as follows: $10.00 divided by 1,000 impressions equals $0.01 per impression, and 10 impressions multiplied by $0.01 equals a total cost of $0.10.

### Step 3 — Apply the attribution decision hierarchy

Attribution is exclusive. A sold order is credited to only one campaign, never split between two.

When a user interacts with multiple ads before purchasing, the system decides which campaign receives credit using this priority order:

1. **Priority 1 — Offsite campaigns.** An active offsite campaign that was the user's last point of contact takes total preference in the attribution.
2. **Priority 2 — Last click.** In the absence of a recent offsite click, the system credits the last ad the user clicked within the 14-day attribution window.
3. **Priority 3 — Last view.** If the user did not click any ad, the system credits the last ad the user viewed, provided it belongs to a campaign type that measures by view, such as Banner or Video.

> ℹ️ For a conversion to be valid, the interaction, whether a click or a view, must have occurred before the order was finalized.

### Step 4 — Map products to attributed campaigns

A campaign can only receive attribution for products explicitly linked to it, and the mapping logic differs by campaign type.

Product Campaigns use 1:1 attribution. Each ad represents one specific product, so a click that ad can only generate a conversion for that same product.

Other campaigns, such as Banner and Video, use N:1 attribution. A single creative is linked to a list of products (SKUs), and an interaction with it, whether a click or a view, can attribute a conversion to any product in that list.

Each creative within a campaign, for example "Banner A" versus "Banner B", tracks its performance independently, which lets you analyze the individual performance of each ad piece.

### Step 5 — Account for data latency in reports

There is a natural delay between the moment an order is created and the moment that sale is attributed to the correct campaign in reports. Expect the following delays:

- **API integration:** approximately 30 minutes.
- **VTEX Platform:** up to 2 hours.

After reviewing these rules, you should be able to identify which campaign and billing model will receive credit for a given conversion, and know what reporting delay to expect before that attribution appears in your reports.
