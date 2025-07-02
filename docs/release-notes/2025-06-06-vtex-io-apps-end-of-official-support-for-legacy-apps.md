---
title: "VTEX IO Apps: End of official support for legacy apps"
slug: "2025-06-06-vtex-io-apps-end-of-official-support-for-legacy-apps"
type: deprecated
excerpt: "VTEX no longer offers support for legacy apps."
createdAt: "2025-06-06T12:45:40.909Z"
updatedAt: "2025-06-27T18:50:17.810Z"
hidden: false
---

As part of our efforts to optimize platform performance and focus on core solutions, VTEX will officially end support for some legacy and third-party apps. These apps will no longer receive updates, security patches, or technical support.

This decision allows us to focus on developing and improving other solutions that align with our future strategy and meet the market's increasing demands.

## What does it mean?

Stores that use deprecated apps can continue using them at their own risk, keeping in mind that:

- VTEX no longer provides technical support for these apps.
- VTEX is not liable for issues arising from their use.
- VTEX will not provide bug fixes, updates, or security patches.
- VTEX will not develop new features.
- The documentation will not be updated.

## What needs to be done?

### Review dependencies

Review any [dependencies](https://developers.vtex.com/docs/guides/vtex-io-documentation-dependencies) your store may have:

1. Open the app's project using the code editor of your choice.
2. Open the [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file.
3. Under the `dependencies` object, check the apps listed.

### Check the apps installed

Check the apps installed in your account:
 
1. Open the terminal and run the `vtex list` command.
2. Check the apps installed.

### Take action

If you’re using any deprecated apps, take appropriate action to remove or replace them with supported alternatives to ensure ongoing stability and security.

## List of deprecated apps

See the list of deprecated apps in [VTEX IO deprecated apps](https://developers.vtex.com/docs/guides/vtex-io-deprecated-apps).
