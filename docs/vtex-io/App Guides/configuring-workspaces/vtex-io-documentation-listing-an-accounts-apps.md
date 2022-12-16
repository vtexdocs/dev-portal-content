---
title: "Listing an account’s apps"
slug: "vtex-io-documentation-listing-an-accounts-apps"
excerpt: "vtex.io-documentation@0.88.5"
hidden: false
createdAt: "2020-06-03T16:02:50.597Z"
updatedAt: "2022-08-02T00:03:05.648Z"
---
While developing in an account, we should be aware of all its installed or linked apps. With VTEX IO CLI, access to the app list is made easy by running a single command.

## Step by step

1. Using your terminal and the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installment-and-command-reference#command-reference), log into the desired account;
2. Once logged in, run the following command:

`vtex list`

VTEX IO CLI will then display a table containing the account’s installed and linked apps, in addition to their respective version, as shown in the example below:

![listing-apps](https://user-images.githubusercontent.com/52087100/67044546-dfe3fd00-f102-11e9-83d7-936f229b7b26.png)

>⚠️ Note that the table is divided into apps related to an **Edition**, apps independently installed and linked.
