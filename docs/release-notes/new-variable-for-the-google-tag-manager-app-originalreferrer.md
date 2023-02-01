---
slug: "new-variable-for-the-google-tag-manager-app-originalreferrer"
title: "New variable for the Google Tag Manager app - Original Referrer"
createdAt: 2021-11-16T12:35:57.934Z
hidden: false
type: "improved"
---

![VTEX IO App](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/new-variable-for-the-google-tag-manager-app-originalreferrer-0.png)

We have added the variable `originalReferrer` to the VTEX Google Tag Manager (GTM) app to help Google Analytics (GA) identify and maintain correct campaign data when a user, throughout their session, does not have an explicit `utm_source` in the URL.  

## What has changed?

Before, [to persist campaign data throughout a user session](https://developers.vtex.com/updates/release-notes/persist-campaign-data-throughout-a-user-session), you have added the variable `originalLocation` to the VTEX Google Tag Manager app. However, Google Analytics could not identify and maintain correct campaign data when a user came from a Google search, for example, but does not have an explicit `utm_source` in the URL.

With the variable `originalReferrer`, Google Analytics can identify and maintain the campaign data, from the user's first login to a store to their checkout navigation.

## What needs to be done?

Go to the [Setting up Google Tag Manager documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-up-google-tag-manager#creating-the-original-location-and-original-referrer-variables) and see how you can create the variable `originalReferrer`.
