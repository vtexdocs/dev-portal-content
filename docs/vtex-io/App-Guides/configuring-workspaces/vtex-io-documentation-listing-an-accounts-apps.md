---
title: "Listing an account’s apps"
slug: "vtex-io-documentation-listing-an-accounts-apps"
hidden: false
createdAt: "2020-06-03T16:02:50.597Z"
updatedAt: "2022-12-13T20:17:44.074Z"
---

While developing in an account, we should be aware of all its installed or linked apps. With VTEX IO CLI, access to the app list is made easy by running a single command.

## Step by step

1. Using your terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log into the desired account;
2. Once logged in, run the following command:

```sh
vtex list
```

VTEX IO CLI will then display a table containing the account’s installed and linked apps, in addition to their respective version, as shown in the example below:

![listing-apps](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-listing-an-accounts-apps-0.png)

> ⚠️ Note that the table is divided into apps related to an **Edition**, apps independently **installed** and **linked** apps.
