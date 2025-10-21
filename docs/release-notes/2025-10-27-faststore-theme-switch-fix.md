---
title: "FastStore: Theme switching no longer requires local server restart" 
slug: "2025-10-27-faststore-theme-switch-fix" 
type: "fixed"
createdAt: "2025-10-24T00:00:00.000Z"
updatedAt: "2025-10-24T00:00:00.000Z"
excerpt: "FastStore theme changes are applied immediately, eliminating the need to restart the development server after modifying the theme configuration."
tags:
    - FastStore
---

Developers working with FastStore can now switch [themes](https://developers.vtex.com/docs/guides/faststore/themes-overview) without restarting the development server. This update simplifies the development process, making theme changes quicker and more efficient.

## What has changed?

Previously, when you changed the theme in the [discovery.config.js](https://developers.vtex.com/docs/guides/faststore/developer-tools-config-options#theme) file, if you were already running localhost, you had to restart the local server at localhost for the changes to take effect and for you to be able to preview them. With this fix, the [FastStore CLI](https://developers.vtex.com/docs/guides/faststore/developer-tools-faststore-cli) clears the Node.js require cache before importing the configuration file, ensuring that theme changes are applied immediately during development.

## Why did we make this change?

Automatically applying theme changes without restarting the server for those already running improves the development experience.

## What needs to be done?

To change your store's theme and see the updates immediately without restarting the server, you need to update your FastStore CLI to the latest version. Follow the instructions in the [Updating the '@faststore/cli' package](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) guide.
