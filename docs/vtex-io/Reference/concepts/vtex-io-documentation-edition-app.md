---
title: "Edition App"
slug: "vtex-io-documentation-edition-app"
excerpt: "vtex.io-documentation@0.88.24"
hidden: false
createdAt: "2020-06-03T16:02:44.317Z"
updatedAt: "2022-12-13T20:17:44.705Z"
---

An Edition App consists of a bundle of settings, policies, back-end and front-end apps encapsulated and exported by a [Sponsor Account](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-sponsor-account).

Its main objective is to facilitate the installation of numerous apps that might be considered essential to set up one specific environment.

![EditionApp](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Reference/concepts/91470034-927c0480-e86a-11ea-866e-54575f3c0975_13.png)

For example, consider the following two Edition Apps developed by the `vtex` account:

- The Edition Business (`vtex.edition-business@0.x`) - installs all the necessary apps to build a store with our legacy [CMS](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/6OCY6S9tqBXPD5mgpbBInC).

- The Edition Store (`vtex.edition-store@5.x`) - installs all the necessary apps to develop a store with the [Store Framework](https://developers.vtex.com/vtex-developer-docs/docs/getting-started-3).

In fact, any VTEX account that meets the [requirements needed to be a Sponsor Account](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-becoming-a-sponsor-account) can develop and release its own Edition Apps.

Notice that this can be especially useful for complex account families, such as those under the same brand or holding.

That's because, besides the fundamental development environment set up by a `vtex` native Edition App, a Sponsor Account can extend an Edition App by creating a new and customized one that meets its account family needs.

> ℹ️ To change the Edition App installed in an account, you must [open a support ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk). This is required to avoid critical issues that its misconfiguration could cause.

Note that all Edition apps must depend, directly or indirectly, on either `vtex.edition-business` or `vtex.edition-store`.

The apps that are part of the Edition App included as a dependency are considered inherited apps.

Despite these, all apps of an Edition App must have the same vendor as the Edition App that bundles them.

Keep in mind that Sponsored Accounts cannot change the apps and configurations installed through an Edition App. Only the Sponsor Account is authorized to do that, by releasing a new version of its Edition App and requiring it to be reinstalled.

To sum it up, by encapsulating all the necessary settings, policies, back-, and front-end apps, an Edition App provides all the essential functionalities to set up one desired environment.
