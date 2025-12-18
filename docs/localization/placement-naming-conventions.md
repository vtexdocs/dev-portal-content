---
title: "Placement naming conventions"
slug: "placement-naming-conventions"
excerpt: "Learn the standardized naming conventions for VTEX Ads placements to ensure accurate metrics tracking and reporting."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-13T00:00:00.000Z"
---

When implementing VTEX Ads on your storefront, placement names are essential for accurate measurement and reporting of advertising metrics for each ad region on your site.

VTEX Ads uses placement identifiers to track performance, attribution, and revenue across different locations and contexts within your store. Use the following standardized naming convention to ensure consistent tracking and analytics across your VTEX Ads implementation:

```json
{platform}_{context}_{position}_{type}
```

## Naming convention components

- **Platform**: The medium where the ad is displayed (`site`, `msite`, `app`).
- **Context**: The page or section context (`home`, `product`, `search`, `category`).
- **Position**: The specific location within the page layout.
- **Type**: The advertisement format (`banner`, `product`).

## Examples

| Platform | Context    | Position         | Type      | Complete placement name               |
| :------- | :--------- | :--------------- | :-------- | :------------------------------------ |
| `site`   | `home`     | `middle`         | `banner`  | `site_home_middle_banner`             |
| `msite`  | `product`  | `top-vitrine`    | `product` | `msite_product_top-vitrine_product`   |
| `app`    | `search`   | `top-vitrine`    | `product` | `app_search_top-vitrine_product`      |
| `app`    | `search`   | `top-vitrine`    | `banner`  | `app_search_top-vitrine_banner`       |
| `site`   | `category` | `bottom-vitrine` | `banner`  | `site_category_bottom-vitrine_banner` |
| `site`   | `product`  | `filter-bar`     | `product` | `site_product_filter-bar_product`     |
