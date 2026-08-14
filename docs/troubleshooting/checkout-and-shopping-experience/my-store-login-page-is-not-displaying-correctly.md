---
title: "My store's login page is not displaying correctly"
slug: "my-store-login-page-is-not-displaying-correctly"
hidden: false
createdAt: "2026-08-14T00:00:00.000Z"
updatedAt: "2026-08-14T00:00:00.000Z"
excerpt: "If your store's login page appears blank or has a broken layout for some customers, the cause is usually a script conflict rather than a VTEX platform bug."
domainFilters:
  - Checkout
symptomFilters:
  - Rendering mismatch
  - Loading failure
---

**Keywords:** VTEX ID | login | SSO | blank page | broken layout | script conflict

The store's [login page](https://developers.vtex.com/docs/guides/login-integration-guide) is rendered by the **VTEX ID** module and is not part of your Store Theme or FastStore code — it is redirected to from your storefront. Because it can be customized through **Admin > Account Settings > Authentication** and through scripts you or your agency inject via tag managers (e.g. GTM) or other third-party code, it may occasionally display incorrectly: showing a blank screen, a broken layout, or overlapping elements. This behavior is usually intermittent and hard to reproduce on demand.

Below are the troubleshooting checks and instructions you can use to identify and fix this kind of issue in your store.

| Issue | Troubleshooting instructions |
| ----- | ---------------------------- |
| The login page appears completely blank for some customers. | [Reproduce the issue in an incognito session](#reproducing-the-issue-in-an-incognito-session). |
| The login page layout looks broken, with overlapping elements, intermittently. | [Check the browser console for script conflicts](#checking-the-browser-console-for-script-conflicts). |
| The issue happens randomly and you can't reproduce it consistently. | [Compare successful and failed page loads using HAR files](#comparing-successful-and-failed-page-loads-using-har-files). |
| You're not sure whether the issue is caused by VTEX or by a custom script. | [Isolate the conflicting script by blocking requests](#isolating-the-conflicting-script-by-blocking-requests). |
| You confirmed a custom script is causing the issue. | [Fix the conflicting customization](#fixing-the-conflicting-customization). |

## Solution

To understand and correct each error, see the solutions below:

### Reproducing the issue in an incognito session

Reports of this issue tend to concentrate on **first-time visits** — i.e., sessions with no existing cookies or cached data for the store domain. If you can't reproduce the problem in your regular browser session, try the following:

1. Open an incognito/private browsing window.
2. Disable browser extensions that might interfere with the page, such as ad blockers (some ad blockers can incidentally hide the same requests that are causing the conflict, masking the bug).
3. Navigate to your store's home page and then to the login page (e.g., by clicking **Sign in**).
4. Repeat the navigation a few times, since the issue is intermittent by nature and may not appear on every attempt.

### Checking the browser console for script conflicts

A blank or broken login page is frequently caused by a JavaScript library being loaded more than once on the same page (for example, two different versions of jQuery), rather than by a platform bug.

1. Open your browser's Developer Tools (`F12` or `Cmd+Option+I`) and go to the **Console** tab.
2. Reload the login page a few times until you reproduce the broken state.
3. Look for errors indicating a duplicated or conflicting library, such as `$ is not a function` or similar jQuery/script conflict messages.
4. Compare the console output between a normal page load and a broken one — the broken load typically shows extra errors that don't appear otherwise.

### Comparing successful and failed page loads using HAR files

Since the issue is intermittent, capturing a HAR (HTTP Archive) file for both a working and a broken page load makes it much easier to compare what's different between the two.

1. Open Developer Tools and go to the **Network** tab.
2. Make sure **Preserve log** is enabled.
3. Reload the page until you get a normal (working) load, then export the network log as a HAR file.
4. Reload the page until you reproduce the broken state, then export a second HAR file.
5. Compare both files (or share them with your technical team) to identify requests, scripts, or initiators that are present only in the broken load.

### Isolating the conflicting script by blocking requests

Once you have one or more suspect scripts (from the console errors or HAR comparison), confirm the root cause by blocking requests one at a time.

1. Open Developer Tools and go to the **Network** tab.
2. Right-click the suspect request and select **Block request URL** (or use the **Network request blocking** panel in Chrome DevTools).
3. Reload the login page and try to reproduce the issue.
4. If blocking a specific script (e.g., a jQuery file) stops the error from happening, that script is a strong candidate for the root cause.
5. To confirm, unblock unrelated third-party requests one by one and keep only the suspect script blocked — if the page keeps working, you've isolated the conflict. If blocking a different, unrelated request has no effect while the original one does, that further confirms the specific script responsible.
6. Check the request's **Initiator** column to identify what triggered it (for example, a Google Tag Manager tag loading a custom script), so you know where the customization comes from.

### Fixing the conflicting customization

The VTEX ID login page itself is delivered by VTEX, but its content and any additional scripts are fully customizable through the **Admin > Account Settings > Authentication** settings and via tag managers or other customizations added to the store. The steps above point to a customization issue, rather than a VTEX platform issue, if:

- The issue only happens with a specific custom script or library loaded (not a native VTEX ID request), and
- Blocking that script consistently prevents the issue.

1. Using the console errors, HAR files, and the specific request(s) identified as the source of the conflict, locate the script in your codebase or tag manager configuration.
2. Check for duplicate library loads (e.g., two versions of jQuery loaded on the same page) or scripts that assume they're the only ones manipulating the login page's DOM.
3. Remove or de-duplicate the conflicting script, or scope it so it doesn't load on or affect the login page.
4. Re-test using the [incognito reproduction steps](#reproducing-the-issue-in-an-incognito-session) above to confirm the fix.

> ℹ️ For more on how the login page integrates with your store, see [Login (SSO)](https://developers.vtex.com/docs/guides/login-integration-guide) and, for Store Framework/FastStore stores specifically, [Integrating the VTEX Login](https://developers.vtex.com/docs/faststore/2-integrating-the-vtex-login).
