---
title: "Installing the offsite capture web script"
slug: "installing-the-offsite-capture-web-script"
hidden: false
createdAt: "2026-07-10T00:00:00.000Z"
updatedAt: "2026-07-10T00:00:00.000Z"
excerpt: "Install and configure the VTEX Ads offsite capture web script on VTEX native or independent storefronts so offsite clicks and conversions are attributed to your campaigns."
---

Offsite traffic and conversion tracking rely on a lightweight **VTEX Ads** web script that runs on your storefront. This guide explains how offsite capture works and walks you through publisher provisioning, installing the script for your store type, validating capture, and troubleshooting zeroed metrics.

The offsite capture web script is a small browser JavaScript script that detects visitors arriving from an offsite ad, captures the relevant events, and sends them to **VTEX Ads** so the click and the resulting purchase can be attributed to the campaign. For both native VTEX storefronts and independent storefronts, the script is provided and maintained by **VTEX Ads**. You add it to your store and configure your **Publisher ID**. You do not build or host the script yourself.

> ℹ️ For the broader **VTEX Ads** integration landscape, see [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads).

## Before you begin

Confirm the following before installing the script:

- Your store is registered in **VTEX Ads** as a publisher and you have a **Publisher ID** (UUID) from the VTEX Ads team. See [Request publisher provisioning](#1-request-publisher-provisioning).
- You know which installation path applies to your storefront (VTEX native or independent). Use the table below.


| Your store                                             | How the script is added                                                          | Who installs       |
| ------------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------ |
| VTEX native store (Store Framework, Portal, FastStore) | Potentially installed as a VTEX app (confirm eligibility with the VTEX Ads team) | VTEX / store admin |
| Independent store (not built on the VTEX storefront)   | A JavaScript snippet loaded from the VTEX Ads CDN                                | Your team          |


> ℹ️ VTEX native store eligibility for the VTEX Ads Agent app may vary. Confirm with the VTEX Ads team before you install.

## How offsite capture works

Offsite capture connects an ad click to a later purchase on your storefront. The flow below summarizes how attribution is established.

1. The offsite ad's destination URL carries the **VTEX Ads** annotators (URL parameters that preserve campaign and click attribution data). On VTEX native stores, the click may also pass through the intermediate URL (`/va/go`), which preserves the annotators until the user reaches the destination retailer.
2. When the user lands on the destination retailer, the web script captures the session and the page view.
3. **VTEX Ads** matches that session or journey to the offsite click and, when an order is placed, attributes the conversion to the campaign. Attribution is subject to the applicable conversion window.

For how sessions, deduplication, and conversion windows are defined in **VTEX Ads**, see [Understanding ads events](https://developers.vtex.com/docs/guides/understanding-ads-events).

### Requirements for capture to work

Capture succeeds only when all of the following are true:

1. The offsite media is served with the **VTEX Ads** parameters preserved.
2. The redirect to the destination URL provided by **VTEX Ads** is preserved (not shortened or altered).
3. The destination page actually loads for the user. Capture happens on load.

For journeys that finish inside a mobile app, the [Activity Flow Mobile SDK](https://developers.vtex.com/docs/guides/installing-activity-flow-in-mobile-apps) is also required. See [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow) for an overview of the SDK and supported platforms.

## 1. Request publisher provisioning

To run offsite campaigns that drive traffic to your store, your store must first be registered in **VTEX Ads** as a publisher. This setup is handled by the VTEX Ads team. You do not create the publisher account yourself.

As part of this one-time setup, the VTEX Ads team:

- Creates your publisher account in **VTEX Ads**.
- Issues a unique **Publisher ID** (a UUID) that identifies your store in every offsite event, so clicks and conversions are correctly attributed to your store.
- If applicable, links the publisher to your VTEX account.

At the end of this process, the VTEX Ads team shares your **Publisher ID** with you. This ID is required to configure the web script on your store:

- On VTEX native stores that are eligible to use the VTEX Ads Agent app, set the **Publisher ID** in the app settings.
- On independent stores, the **Publisher ID** is included in the tracking URLs.

If you do not have a **Publisher ID** yet, request it from your VTEX Ads contact before installing the script.

## 2. Install the offsite capture web script

Choose the installation path that matches your storefront.

### Independent stores: CDN script

Add the published bundle, hosted on the CDN, to your storefront pages:

```html
<script async src="https://cdn.newtail.com.br/retail-media/scripts/vtexrma-agent.1.0.0.js"></script>
```

> ℹ️ The URL above pins version `1.0.0`. Confirm the current version with the VTEX Ads team before publishing, and whether any additional configuration is required.

> ⚠️ The provisioning step states that the **Publisher ID** is included in the tracking URLs for independent stores. The installation snippet above does not show how the **Publisher ID** is passed. Confirm the expected configuration with the VTEX Ads team before go-live.

### VTEX native stores: VTEX Ads Agent app

For VTEX native stores, the offsite capture web script is potentially delivered through the `[vtex.ads-agent](https://developers.vtex.com/docs/apps/vtex.ads-agent)` VTEX IO app. Confirm eligibility with the VTEX Ads team before you install.

**Prerequisites:**

- Access to the store's VTEX Admin
- The VTEX IO Toolbelt (`vtex` CLI)
- The **Publisher ID** (UUID) provisioned by the VTEX Ads team

Install the app with the VTEX IO CLI:

```bash
vtex install vtex.ads-agent
```

After installing, set `publisherId` in the app settings so the script starts reporting events. For full install and configuration steps, see the `[vtex.ads-agent` app documentation](https://developers.vtex.com/docs/apps/vtex.ads-agent).

## 3. Validate your installation

Follow these checks after installing the script:

1. Access the destination retailer through an offsite URL (the parameterized URL generated for the campaign).
2. Confirm the script loads and that the offsite access event is sent. Check the network request.
3. Run a control case: an access to the same page **without** the offsite parameters should **not** be registered as an offsite click.
4. Run an end-to-end test: with a test offsite campaign, place a test order and confirm that all metrics (impression, click, and conversion) were captured. This end-to-end validation is the retailer's responsibility.

> ℹ️ The expected network endpoint, request name, or payload signature for offsite access events has not been documented here. Confirm what to look for in DevTools with the VTEX Ads team if validation is unclear.

## Troubleshooting

### Zeroed metrics

If the script is not loading on the destination pages, there is no capture and metrics come out zeroed. Confirm the script tag is present on the destination pages and that the bundle loads without errors.

## Next steps

- [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads) - Integration overview and related guides.
- [VTEX Ads Script Agent](https://developers.vtex.com/docs/guides/vtex-ads-script-agent) - On-site tracking script for Retail Media campaigns (distinct from the offsite capture web script).
- [Understanding ads events](https://developers.vtex.com/docs/guides/understanding-ads-events) - Sessions, deduplication, and conversion windows.
- [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow) and [Installing Activity Flow in mobile apps](https://developers.vtex.com/docs/guides/installing-activity-flow-in-mobile-apps) - Required for offsite journeys that complete in a mobile app.

