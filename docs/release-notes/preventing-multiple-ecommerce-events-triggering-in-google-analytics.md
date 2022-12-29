---
slug: "preventing-multiple-ecommerce-events-triggering-in-google-analytics"
title: "Preventing multiple ecommerce events triggering in Google Analytics"
createdAt: 2022-05-09T16:47:45.836Z
hidden: false
type: "fixed"
excerpt: "The `ecommerce` variable was fixed to prevent the same ecommerce event from being triggered to Google Analytics (GA) multiple times and resulting in a financial cost."
---

![VTEX IO App](https://img.shields.io/badge/-VTEX%20IO%20App-orange)

The `ecommerce` variable was fixed to prevent the same ecommerce event from being triggered to Google Analytics (GA) multiple times and resulting in a financial cost.

## Why did we make these changes?

Previously, users of the [VTEX Google Tag Manager app](https://developers.vtex.com/vtex-developer-docs/docs/google-tag-manager) had the same ecommerce event fired several times to Google Analytics, resulting in a financial expense because the large number of events triggered exceeded the monthly free visits of 10 million.

Now, the `ecommerce` variable passes `null` before pushing an ecommerce event to the data layer, as [Google recommends](https://developers.google.com/analytics/devguides/collection/ua/gtm/enhanced-ecommerce#clear-ecommerce#clear-ecommerce), which prevents the same event from triggering in GA and does not exceed the monthly hits of 10 million free visits.

## What needs to be done?

Nothing. This improvement is already available for all VTEX IO users.