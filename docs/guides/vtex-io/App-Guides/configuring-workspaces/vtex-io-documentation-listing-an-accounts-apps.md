---
title: "Listing an account’s apps"
slug: "vtex-io-documentation-listing-an-accounts-apps"
hidden: false
createdAt: "2020-06-03T16:02:50.597Z"
updatedAt: "2022-12-13T20:17:44.074Z"
---

Understanding the apps installed or linked to an account is pivotal for effective development and account management. The [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) simplifies this task by providing a straightforward command to access the list of apps associated with a specific account and workspace.

## Instructions

1. Open the terminal and log into the desired account using the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference). If applicable, switch to the desired [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace).
2. Run the following command:

    ```sh
    vtex list
    ```

Upon executing this command, the VTEX IO CLI will display a detailed list of installed and linked apps within the account. This list includes vital information such as app names and their respective versions.

**Example output:**

```terminal
$ vtex list

Edition Apps in mystore at workspace master
vtex.admin                        4.56.3 
vtex.admin-account-details        1.0.3  
vtex.admin-apps                   4.3.1  
vtex.admin-audit                  2.13.5 
...
vtex.workspace-analytics          0.1.7  

Installed Apps in mystore at workspace master
vtex.affiliates                             1.8.0 
vtex.app-store-seller                       0.12.9
vtex.availability-notify                    1.12.1
...
vtex.social-selling                         0.8.0 

Linked Apps in mystore at workspace master
You have no linked apps
```

Note that the list is organized into three categories:

- **Edition Apps**: Apps installed by an [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app). Modifying these app versions and configurations is restricted to the [Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-sponsor-account).
- **Installed Apps**: Independently [installed apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app).
- **Linked Apps**: Apps [linked](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) in a [development workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace).
