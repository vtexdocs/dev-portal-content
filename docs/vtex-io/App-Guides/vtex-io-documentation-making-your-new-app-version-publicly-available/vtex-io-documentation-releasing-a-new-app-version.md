---
title: "Releasing a new app version"
slug: "vtex-io-documentation-releasing-a-new-app-version"
hidden: false
createdAt: "2020-06-03T16:02:44.609Z"
updatedAt: "2022-12-13T20:17:44.577Z"
category: "App Development"
seeAlso:
  - "/docs/guides/vtex-io-documentation-publishing-an-app"
---

Once you have finished developing your app, you may release it as the first step toward [making your new app version public](/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available). The process of releasing an app consists of:

- Incrementing the app version in the `manifest.json` file according to the [SemVer (semantic versioning) best practices](https://semver.org/).
- Updating the app `CHANGELOG.md`.
- Creating a release commit and a release tag.
- Sending the performed changes to the app repository.

Please note that releasing a new app version does not make it available to end-users or automatically update the app on accounts that have it installed. To do so, you must finish the entire process of [making your new app version public](/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available).

## Before you start

If you are releasing an app in the [App Store](https://apps.vtex.com/), make sure that you have covered the [VTEX guidelines](/docs/guides/vtex-io-documentation-homologation-requirements-for-vtex-app-store) before proceeding.

## Step by step

1. Open the terminal and log in to the account responsible for the app development, i.e., the account specified as the app vendor in the [`manifest.json`](/docs/guides/vtex-io-documentation-manifest) file.
2. Change to the app root folder.
3. Depending on the scenario (check [SemVer best practices](https://semver.org/)), run one of the following commands to release your new app version:

- `vtex release patch stable` - Releases a **patch** stable version.
- `vtex release minor stable` - Releases a **minor** stable version.
- `vtex release major stable` - Releases a **major** stable version.

- `vtex release patch beta` - Releases a **patch** beta version.
- `vtex release minor beta` - Releases a **minor** beta version.
- `vtex release major beta` - Releases a **major** beta version.
