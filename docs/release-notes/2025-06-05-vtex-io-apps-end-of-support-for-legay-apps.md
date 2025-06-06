---
title: "VTEX IO Apps: End of official support for legacy apps"
slug: "2025-06-05-vtex-io-apps-end-of-official-support-for-legay-apps"
type: deprecated
excerpt: "VTEX no longer offers support for legacy apps."
createdAt: "2025-06-06T12:45:40.909Z"
updatedAt: ""
hidden: false
---

As part of our ongoing efforts to improve platform performance and focus on core solutions, we’re officially ending support for some legacy and third-party apps. These apps will no longer receive updates, security patches, or technical support from VTEX.

This decision allows us to focus on developing and improving other solutions that align with our future strategy and meet the market's increasing demands.

## What does it mean?

Stores currently using unsupported apps can continue to use them, but at your own risk, considering:

- VTEX no longer offers technical support for these apps.
- VTEX assumes no responsibility for issues arising from its use.
- VTEX no longer provides bug fixes, updates, or security patches.
- VTEX no longer develops new features.
- Documentation is no longer updated.

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
