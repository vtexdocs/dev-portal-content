---
slug: "persist-campaign-data-throughout-a-user-session"
title: "Persist campaign data throughout a user session"
createdAt: 2021-10-11T14:01:20.262Z
hidden: false
type: "fixed"
---

![VTEX IO App](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/persist-campaign-data-throughout-a-user-session-0.png)

To persist campaign data throughout a user session and avoid providing inconsistent campaign data to Google Analytics, you must add the variable `OriginalLocation` to your [Google Tag Manager (GTM) container](https://tagmanager.google.com/) and configure your store’s Google Analytics tags.

Learn how to add the variable `OriginalLocation` to your GTM container and configure your store’s Google Analytics tags in the [Setting up Google Tag Manager documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-up-google-tag-manager#creating-the-original-location-and-original-referrer-variables).
