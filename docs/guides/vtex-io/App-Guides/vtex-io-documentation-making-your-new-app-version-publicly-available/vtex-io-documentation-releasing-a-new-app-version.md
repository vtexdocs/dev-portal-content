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

Once you have finished developing your app, you may release it as the first step toward [making your new app version public](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available). The process of releasing an app consists of:

- Incrementing the app version in the `manifest.json` file according to the [SemVer (semantic versioning) best practices](https://semver.org/).
- Updating the app `CHANGELOG.md`.
- Creating a release commit and a release tag.
- Sending the performed changes to the app repository.

Please note that releasing a new app version does not make it available to end-users or automatically update the app on accounts that have it installed. To do so, you must finish the entire process of [making your new app version public](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available).

## Before you begin

If you are releasing an app in the [App Store](https://apps.vtex.com/), make sure that you have covered the [VTEX guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-homologation-requirements-for-vtex-app-store) before proceeding.

## Instructions

1. Open the terminal and log in to the account responsible for the app development, i.e., the account specified as the app vendor in the [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file.
2. Change to the app root folder.
3. Depending on the scenario (check [SemVer best practices](https://semver.org/)), run one of the following commands to release your new app version:

   - `vtex release patch stable` - Releases a **patch** stable version.
   - `vtex release minor stable` - Releases a **minor** stable version.
   - `vtex release major stable` - Releases a **major** stable version.

   - `vtex release patch beta` - Releases a **patch** beta version.
   - `vtex release minor beta` - Releases a **minor** beta version.
   - `vtex release major beta` - Releases a **major** beta version.

For more details about the `vtex release` command, check our [VTEX IO CLI reference](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#release).

## Understanding app versioning

### Major, minor and patch

Versioning in VTEX IO follows the [SemVer standard](https://semver.org/), utilizing a format of `{major}.{minor}.{patch}`. For instance, if an app version is `2.13.5`, the **major** is `2`, the **minor** is `13`, and the **patch** is `5`.

Apps should start development with version `0.0.0`.

The recommended use cases for each version type are as follows:

- **Patch**: intended for bug fixes and minor issues.
- **Minor**: intended for changes in functionality that are not breaking changes like new features, changes in the UI, and others.
- **Major**: intended for breaking changes and changes in the endpoints. Changes in the [Billing Options](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options) always require a new **major** release.

For each new version of a type, this version type will be increased by one and turn the minor types to `0`, if applicable. For instance, if your app version is `2.13.5` and you want to:

- Release a new **patch**, your new app version will be `2.13.6`.
- Release a new **minor**, your new app version will be `2.14.0`.
- Release a new **major**, your new app version will be `3.0.0`.

### Stable and beta versions

App versions are created as **stable** by default. **Beta** versions must be explicitly declared and are identified by a dash symbol (`-`) following a sequence of alphanumeric characters after the version number. For instance, `2.13.5` is a **stable** version, and you can have a **beta** version called `2.13.5-beta1`.

The recommended use cases for stable and beta versions are:

- **Stable**: intended for wide availability and production environments.
- **Beta**: intended for tests and limited availability.

Consider the following when dealing with a **beta** version:

- **Beta** versions cannot be deployed. If you run `vtex deploy` on a beta version of an app, the accounts and workspaces with that specific app version installed will not be updated to this version.
- **Beta** versions ignore the `ttl` (time-to-live) parameter set in the [`service.json` file](https://developers.vtex.com/docs/guides/overview-of-vtex-io-services#the-servicejson-file).
