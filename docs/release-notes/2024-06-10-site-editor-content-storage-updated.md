---
title: "Site Editor: Fixed content loss issue"
slug: "2024-06-10-site-editor-content-storage-updated"
hidden: true
createdAt: 2024-06-10T10:00:00.000Z
type: "improved"
excerpt: "Site Editor content storage received an upgrade for better performance and reliability."
---

Starting June 10th, all accounts using [Site Editor](https://help.vtex.com/tutorial/site-editor-overview--299Dbeb9mFczUTyNQ9xPe1) will automatically receive a content storage upgrade to address the previously known issue: [Intermittent Site Editor content loss](https://help.vtex.com/en/known-issues/intermitent-site-editor-content-loss--3a5MlAoD2Z7Gu6HDS8wihD). This upgrade improves storage performance, reliability and reduces the size of your content storage.

## What has changed?

Previously, frequent content changes in Site Editor could cause the `content.json` file to become excessively large, leading to content loss when [promoting a production workspace to master](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspaces-best-practices#deployment-and-workspace-promotion) or installing a new theme version in a test workspace.

We have now improved the storage architecture and file partitioning solution for Site Editor. The improvement solution stores content in smaller, template-specific files, instead of a single large file. This change reduces file size by approximately 90%, reducing storage needs per page, and enhancing overall performance and content delivery.

## What needs to be done?

No action is needed. The upgrade will be automatically implemented in all VTEX stores using Site Editor.

If you continue to experience content loss after June 10th, open a ticket with [VTEX support](https://help.vtex.com/support).
