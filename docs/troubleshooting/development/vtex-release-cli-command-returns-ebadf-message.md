---
title: "`vtex release` CLI command returns an EBADF message"
slug: "vtex-release-cli-command-returns-ebadf-message"
hidden: false
createdAt: "2024-08-09T13:00:00.000Z"
updatedAt: "2024-08-09T13:00:00.000Z"
excerpt: "Creating an app release using the VTEX IO CLI returns an EBADF error."
tags:
  - vtex-io
  - cli
  - release
---

**Keywords:** Release | CLI

When running the [VTEX IO CLI command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#release) [vtex release](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#release), it returns an EBADF (error bad file descriptor) message. This happens because a file descriptor variable does not correctly point to a file during command execution.

The `vtex release` command creates a new version of a VTEX IO app by rewriting the `CHANGELOG.md` and the `manifest.json` files. For more details about this process, see [Releasing a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).

The `vtex release` command creates a release commit and a release tag and sends the changes to the app repository. Thus, a possible cause of the EBADF message could be improper GitHub configuration. For more details, see the [external GitHub documentation](https://docs.github.com/en/enterprise-cloud@latest/get-started/getting-started-with-git/set-up-git#setting-up-git).

## Solution

Instead of depending on the `vtex release` command to make the changes in the app files for a new version, make the changes manually and continue [deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available).

Consider your app was at version `0.1.0` and a new version `0.1.1` was created on July 15, 2024. Follow the steps below to create a new app version without using the `vtex release` command:

1. Open the `CHANGELOG.md` file of your app.

2. Update the version header from `## [Unreleased]` to `## [0.1.1] - 2024-07-15`, as follows:

    ```diff
    - ## [Unreleased]
    + ## [0.1.1] - 2024-07-15
    +
    + ### Added
    +
    + * New feature

    ## [0.1.0] - 2024-06-03

    ### Fixed

    * Bug fixes
    ```

3. Open the `manifest.json` file of your app and change the app version to the new version. In this example, we are changing the version from `0.1.0` to `0.1.1`.

    ```json
    "version": “0.1.1”
    ```

4. Open a terminal in the root folder of your app.

5. Run the [`vtex publish` command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#publish). This command creates a release candidate version of the app and makes it available for installation using the [`vtex install` command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#install). For more details, see [Publishing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app).
