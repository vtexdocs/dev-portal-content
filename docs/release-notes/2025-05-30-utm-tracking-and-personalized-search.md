---
title: "FastStore: Enhanced UTM tracking and personalized search"
slug: "2025-06-05-utm-tracking-and-personalized-search"
hidden: false
type: "improved"
createdAt: "2025-06-05T00:00:00.219Z"
updatedAt: ""
excerpt: "FastStore now preserves UTM and UTMi parameters throughout the customer journey, improving campaign attribution and analytics."
---

FastStore now supports [UTM (Urchin Tracking Module)](https://help.vtex.com/en/tutorial/what-are-utm-source-utm-campaign-and-utm-medium--2wTz7QJ8KUG6skGAoAQuii) and [UTMi (internal UTM)](https://help.vtex.com/en/tutorial/what-are-the-internal-utms--5Pvo8ufYWs00AUeCCEY68a) parameters across the entire customer journey, from site entry to search and checkout. This update ensures accurate campaign attribution, improved analytics, and more accurate insights for merchants into campaign effectiveness and user journeys.

Additionally, searches on your storefront are more consistent and personalized, as session and segmentation cookies (like `vtex_segment`) are reliably forwarded in search requests, maintaining user context during product discovery.

## What has changed?

FastStore projects now capture and retain marketing campaign data (UTM and UTMi parameters) from visitor sessions and attach it to their orders. This includes parameters such as:

| Parameter       | Example                          | Description |
|----------------|----------------------------------|---------|
| `utm_source`   | `utm_source=google`           | Identifies the traffic source (such as Facebook or Google). |
| `utm_medium`   | `utm_medium=email`              | Specifies the marketing medium (such as email, social). |
| `utm_campaign` | `utm_campaign=spring_sale`      | Names the campaign (example: seasonal promotions). |
| `utmi_cp`      | `utmi_cp=shoes/sneakers`        | Captures the category path visited by users. |
| `utmi_p`       | `utmi_p=product123`             | Identifies a specific product detail page. |
| `utmi_pc`      | `utmi_pc=home`                  | Tracks page types (such as home, category, or product). |

This improvement allows merchants to launch UTM-based promotions and track the effectiveness of external campaigns (including UTM and/or UTMi data) and user journeys within the store.

Additionally, session and segmentation cookies are forwarded in search requests, ensuring a consistent and personalized search experience.

> ⚠️Only non-identifiable marketing data is collected. No personal information is tracked or shared. Data is used strictly to improve site analytics and customer experience.

## Why did we make this change?

We implemented these changes to address the need for more accurate campaign attribution and enhanced user experience. By preserving UTM and UTMi parameters, merchants can gain deeper insights into the effectiveness of their marketing efforts. Forwarding session and segmentation cookies in search requests ensures that users receive consistent and personalized search results, improving product discovery.

## What needs to be done?

To enable your store to capture and retain marketing campaign data (UTM and UTMi parameters) from visitor sessions and attach it to their orders, check the [UTM tracking in FastStore](https://developers.vtex.com/docs/guides/faststore/seo-validating-utm-tracking-in-faststore) guide.
