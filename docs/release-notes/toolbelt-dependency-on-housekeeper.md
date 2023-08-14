---
title: 'VTEX IO CLI dependency on Housekeeper '
excerpt: "In order to decrease inconsistencies between apps updates, [VTEX IO CLI](https://github.com/vtex/toolbelt) now uses the __Housekeeper API__.  "
createdAt: "2019-07-03T14:47:00.000Z"
---

In order to decrease inconsistencies between apps updates, [VTEX IO CLI](https://github.com/vtex/toolbelt) now uses the __Housekeeper API__.  

> ℹ️ Housekeeper is the system responsible for automatically updating account apps.

## What has changed

Previously, our CLI (VTEX IO CLI) did not take advantage of the Housekeeper apps updater service when launching the `vtex update` command. By not taking advantage of this service, VTEX IO CLI was not able to support features such as Edition, which could have led to inconsistencies about which specific workspace apps should be updated.

> ℹ️ Edition is a feature that seeks for VTEX IO usage to fit a user’s specific requirements, through various VTEX IO editions such as VTEX IO Enterprise.

The Housekeeper API solves both issues: it is now used by VTEX IO CLI to decide which updates are to be made to a given workspace considering the necessary changes to an account edition. 

When launching the `vtex update` command, tables separated by the app installation type (if it is an infra app, an user-installed app, an edition-installed app, etc.) are displayed containing the pending updates. For example:

![vtex-io-toolbelt-using-housekeeper-api](https://user-images.githubusercontent.com/52087100/60602163-a670c700-9d89-11e9-9667-2ddb3f2db34a.png)

## Main advantages

By depending on the Housekeeper API, VTEX IO CLI has become more reliable when it comes to app updates. In addition, it is now also compatible with Editions and any other Housekeeper features.
