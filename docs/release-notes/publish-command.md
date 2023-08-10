---
title: Publish command
excerpt: "If you take a deep breath, you can catch a whiff the A/B tests in the air. That’s because the Publish command from 01/02/2020 on will change its functionality and more steps will be added to the process of publishing an app on the platform. Everything to say goodbye to potential instabilities and to foster a culture of tests among our beloved devs."
createdAt: "2019-12-19T14:47:00.000Z"
git: "https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-47-48-49-50-51/publish-command.md"
---

> ⚠️ Updated January 13, 2020: `vtex validate` command is deprecated. Use `vtex deploy` instead.

The `vtex publish` command, responsible for publishing new app versions, will change its platform behavior on 01/02/2020.

> ⚠️ This release is merely a notice about the impending change to the app publishing process, meaning that **this release is not yet live** and **will only be in effect as of January 2, 2020**. 

## What will change

Presently, the `vtex publish` command automatically publishes the new version of an app, whether it was in beta or not.

From January 2, `vtex publish` will become just one of the **three steps** needed to effectively publish an app in the VTEX IO's infrastructure.

![Publish-process](https://user-images.githubusercontent.com/52087100/71118909-c0775800-21b7-11ea-9e17-226badbc30c3.png)

The new process will be as follows:

1. When running the `vtex publish` command in your terminal, a **candidate release version** will be generated. The candidate release will be nothing more than a **test phase**, that is, the new version in probation mode. Because of this state, Housekeeper won't automatically install it on any account. To install it, you must order VTEX IO CLI to [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the exact version.
2. After the installation, it is recommended to manually **perform** [**A/B tests**](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) on the new version, checking and confirming its stability.
3. Once the necessary testing is completed, the third and last step is to **validate the candidate release** as a version that's ready to become stable on the infrastructure (having the `validated` status) and to be automatically installed by Housekepper. This is achieved using the `vtex validate` command. 

## Why will this action be taken 

According to the command's current behavior, you can release a new stable version and publish it as fast as possible and enable it on the platform, without any of the VTEX IO CLI requisites.

The new publication process steps strengthen the culture of these tests in addition to their validation during the development process, bringing **test discipline** and **greater stability** to the platform's apps.

## Side effects

There are not deleterious app development side effects. The consequence of this release is merely the **extra steps** added to the publish process from January 2, 2020, on. 

## What you need to do

For more on this topic and to better understand the steps related to the publish process, access our recipe on [**Publishing an app**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app).
