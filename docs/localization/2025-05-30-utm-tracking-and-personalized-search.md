---
title: "FastStore: UTM tracking and personalized search"
slug: "2025-05-30-utm-tracking-and-personalized-search"
hidden: false
type: "improved"
createdAt: "2025-05-30T00:00:00.219Z"
updatedAt: ""
excerpt: "FastStore now preserves UTM and UTMi parameters throughout the customer journey, improving campaign attribution and analytics."
---

FastStore now supports [UTM (Urchin Tracking Module)](https://help.vtex.com/en/tutorial/what-are-utm-source-utm-campaign-and-utm-medium--2wTz7QJ8KUG6skGAoAQuii) and [UTMi (internal UTM)](https://help.vtex.com/en/tutorial/what-are-the-internal-utms--5Pvo8ufYWs00AUeCCEY68a) parameters across the entire customer journey, from site entry through search to checkout. This update ensures accurate campaign attribution, improved analytics, and merchants can obtain more accurate insights into campaign effectiveness and user journeys.

Additionally, searches on your storefront are more consistent and personalized, as session and segmentation cookies (like `vtex_segment`) are reliably forwarded in search requests, maintaining user context during product discovery.

## What has changed?

FastStore projects now capture and retain marketing campaign data (UTM and UTMi parameters) from a visitor’s session and attach it to their order. This includes parameters such as:

| Parameter       | Example                          | Description |  
|----------------|----------------------------------|---------|  
| `utm_source`   | `utm_source=google`           | Identifies the traffic source (e.g., Facebook, Google). |  
| `utm_medium`   | `utm_medium=email`              | Specifies the marketing medium (e.g., email, social). |  
| `utm_campaign` | `utm_campaign=spring_sale`      | Names the campaign (e.g., seasonal promotions). |  
| `utmi_cp`      | `utmi_cp=shoes/sneakers`        | Captures the category path a user visited. |  
| `utmi_p`       | `utmi_p=product123`             | Identifies a specific product detail page. |  
| `utmi_pc`      | `utmi_pc=home`                  | Tracks page types (e.g., home, category, product). |

This improvement allows merchants to launch UTM-based promotions and track the effectiveness of external campaigns (including UTM and/or UTMi data) and user journeys within the store.

Additionally, session and segmentation cookies are forwarded in search requests, ensuring a consistent and personalized searching experience.

> ⚠️Only non-identifiable marketing data is collected. No personal information is tracked or shared. Data is used strictly to improve site analytics and customer experience.

## What needs to be done?

To enable your store to capture and retain marketing campaign data (UTM and UTMi parameters) from a visitor’s session and attach it to their order, see the Implementing and validating [UTM tracking in FastStore](/TBD) guide.
