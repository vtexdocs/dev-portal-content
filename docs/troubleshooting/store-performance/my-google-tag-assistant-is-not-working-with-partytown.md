---
title: "My Google Tag Assistant is not working with Partytown"
slug: "my-google-tag-assistant-is-not-working-with-partytown"
excerpt: "Learn how to debug GTM and GA when Partytown is enabled and how to handle common jQuery-related errors."
hidden: false
createdAt: "2023-09-14T00:00:00.00Z"
updatedAt: "2026-03-11T00:00:00.00Z"
tags:
    - Analytics
    - Google Tag Manager
---

**Keywords:** Partytown | Google Tag Manager | Google Analytics | Tag Assistant | jQuery

> ⚠️ These troubleshooting steps are specific to [FastStore](https://developers.vtex.com/docs/guides/faststore) projects.

[Partytown](https://partytown.qwik.dev/) improves website performance by offloading third-party script execution to a web worker. However, this can introduce challenges when debugging analytics tools like Google Tag Manager (GTM) and Google Analytics (GA) or when scripts have specific dependencies. This article provides solutions for common issues, such as Google Tag Assistant not working and "jQuery is not defined" errors.

## Solutions

### Debug Google Tag Manager and Google Analytics

Google Tag Assistant can't debug GTM and GA tags when Partytown is enabled. To debug your tags and GA behavior, make GTM run outside Partytown during the debugging session.

1. Append `?gtm_debug=` to your URL. This query string ensures that GTM scripts and all injected tags run outside Partytown, allowing Tag Assistant to work. This behavior persists during [Single Page Application (SPA)](https://en.wikipedia.org/wiki/Single-page_application) navigation but not when navigating through absolute links or full page reloads.
2. When previewing a GTM container, configure it to automatically include the `gtm_debug=` query string in the URL.

![enable-gtm-debug-query-string](https://vtexhelp.vtexassets.com/assets/docs/src/enable-gtm-debug-query-string___a500fcb42a88127e93fb8c5e44ce119c.png)

3. If you use Google Analytics 4 (GA4), debug events directly in Google Analytics. Check the [official Google documentation](https://support.google.com/analytics/answer/7201382?sjid=4242037245115072180-SA) for instructions.

### See events pushed to dataLayer

When Partytown is enabled, you can't read the `dataLayer` variable directly from the browser console. To monitor events pushed to `dataLayer`, inject a custom script.

1. Open the browser developer console.
2. Execute the following JavaScript snippet:

   ```js
   window.dataLayerHistory = []
   const originalPush = dataLayer.push
   dataLayer.push = (data) => {
     console.log(data)
     dataLayerHistory.push(data)
     originalPush(data)
   }
   ```
3. After running the script, every event added to `dataLayer` is logged in the browser console. All events are also stored in the `window.dataLayerHistory` variable for review. This continues to work across [Single Page Application (SPA)](https://en.wikipedia.org/wiki/Single-page_application) navigation.

### Resolve "jQuery is not defined" or "$ is not defined" errors

If scripts running in Partytown encounter **"jQuery is not defined"** or **"$ is not defined"** errors, Partytown can't access jQuery from the web worker environment. After identifying the script causing the jQuery-related error, you can try the solutions below:

- **Remove jQuery dependency (recommended):** The most robust solution is to refactor your script to use vanilla JavaScript instead of relying on jQuery. This eliminates the dependency and ensures compatibility across different environments.
- **Break down the script:** If a full refactor isn't immediately possible, identify the parts of your script that don't depend on jQuery and make sure they run as expected. Then, address the jQuery-dependent parts separately using other solutions.
- **Define jQuery locally in the script:** In the problematic script, add the line `$ = jQuery = window.jQuery`. This explicitly defines these variables locally within the script scope, which may allow Partytown to recognize and use jQuery from the web worker.
