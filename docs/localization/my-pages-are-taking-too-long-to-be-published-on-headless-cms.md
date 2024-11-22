---
title: "My pages are taking too long to be published on Headless CMS"
slug: "my-pages-are-taking-too-long-to-be-published-on-headless-cms"
hidden: false
createdAt: "2024-06-28T14:00:00.000Z"
updatedAt: ""
excerpt: "Releasing or publishing a page via Headless CMS or Releases can take a long build times"
tags:
    - headless-cms
    - releases
    - faststore
---

**Tags:** Headless CMS, Releases, FastStore

**Keywords:** Build, deploy, FastStore

When releasing or publishing a page via [Headless CMS](https://help.vtex.com/en/tutorial/headless-cms-overview--3U5gvhHdQL0jczYH8gjX09) or [Releases](https://help.vtex.com/en/tutorial/releases-module-beta--n2tN0WX5I6MJMbrJrS0Kb), you may experience long build times.

## Solution

Follow the steps below to identify the root cause of publishing errors with the VTEX Headless CMS and Releases module.

### Step 1: Check the release status

In the VTEX Admin, go to **Storefront > Releases**, and click **Releases**.

Check if the page release status is either **Published** or **Failed**.

Open the release and copy its identifier (e.g., `635feddd372d5fef67c4160e`) at the end of the page URL (e.g., `https://{accountname}.myvtex.com/admin/releases/calendar/?period=ONE_DAY-1708916400000&release=635feddd372d5fef67c4160e&search=&sort=LAST_MODIFIED&sort=DESC&status=ALL`). After copying the identifier, proceed to [Checking the GitHub pipeline](#step-2-checking-the-github-pipeline) to continue checking the status.

### Step 2: Check the GitHub pipeline

After [getting the Release identifier](#step-1-verifying-the-release-status), follow these steps to verify the status of the corresponding build.

1. Access the GitHub repository of your FastStore project.
2. In the repository search field, search for the code obtained in the [previous section](#step-1-verifying-the-release-status). If you find a commit with the corresponding Release identifier in its name, it indicates that the Release has undergone the CI/CD process.
3. Check the status of the **Build check** for the commit by clicking one of the following icons:

| Icon | Description |
| ---------- | ----------- |
| ✓ | The build was successful. If this status doesn't match what you see in the Admin, the communication between the Releases module and WebOps must have failed. No action is required, as this error is related to a communication issue on our end. |
| ● | The build is queued, waiting for other builds to complete. If queued for longer than 45 minutes, please [open a ticket with VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk). |
| ⨯ | The build failed. For more details, proceed to [Step 3 - Identifying the build error](#step-3 -identifying the build error). |

### Step 3 - Identify the build error

If the Release's build failed, follow these instructions to identify the root cause of the error:

1. Click the **Details** link next to the **Build** check to view the full log.

   ![Build Error](https://vtexhelp.vtexassets.com/assets/docs/src/build-error___13f243f0e4246cd103c904a4baaf3c72.png)

2. Click the **Re-run checks** button to try deploying your Release again.

    > ⚠️ If the **Re-run checks** button is not available, you might not have _write access_ to the repository. In this case, contact the repository's Admin.

3. If the error persists, review the build log, check the error, and [open a ticket with VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) with a description of the issue.
