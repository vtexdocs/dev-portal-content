---
title: "Updating Edition apps"
slug: "vtex-io-documentation-updating-edition-apps"
excerpt: "Learn how to publish a new version of an Edition app."
hidden: false
createdAt: "2020-06-03T16:02:44.265Z"
updatedAt: "2022-12-13T20:17:44.354Z"
---

This guide explains how to release a new version of an [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) by defining new required apps for child accounts or by changing the Edition's initial settings.

## Before you begin

Before proceeding, ensure you are a [Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-sponsor-account) and have already [configured an Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-configuring-an-edition-app).

## Instructions

1. Open your Edition app's folder and access the `apps.json` file using your preferred code editor.
2. Make the desired changes to the apps and settings in the file.
   > ⚠️ Be aware that if you add an app to the Edition that is already installed on a child account, the app's installation type changes to `edition`. You can no longer remove it from the accounts or change its major version, as the Edition now enforces it. Similarly, if you remove an app from `apps.json`, VTEX will automatically uninstall it from all child accounts using this Edition. If you still need the removed app in some child accounts, you must reinstall it manually in each of those accounts.
3. Save and commit your changes.
4. [Publish and deploy](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) the new Edition version.

## Understanding the update process

After you publish the new version, VTEX automatically updates the Edition in all associated accounts. This process runs asynchronously, periodically, and individually for each child account.

> ⚠️ Note: VTEX only applies automatic updates for minor and patch version changes. If you release a new major version (a breaking change), you must update the Edition manually in each child account.
