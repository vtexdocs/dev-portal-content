---
title: "2. Configuring your account"
slug: "vtex-io-documentation-2-prerequesites"
hidden: false
createdAt: "2020-08-11T07:03:18.428Z"
updatedAt: "2022-12-13T20:17:46.410Z"
category: "Storefront Development"
excerpt: "Set up your account Edition to get started with Store Framework."
seeAlso:
 - "/docs/guides/vtex-io-documentation-3-settingyourstoretheme"
---

Now that you have completed the basic setup for VTEX IO, it is time to configure your account to leverage the full power of the VTEX Store Framework. This guide will walk you through two essential prerequisites: [Setting your account's Edition app](#step-1---setting-your-accounts-edition-app) and [Implementing the VTEX Intelligent Search](#step-2---implementing-the-vtex-intelligent-search).

By fulfilling these prerequisites, you will ensure your store is ready to harness the VTEX Store Framework's capabilities, avoiding potential technical issues during the implementation process.

## Instructions

### Step 1 - Setting your account's Edition app

The [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app/) plays a pivotal role in your VTEX account by installing a bundle of settings and basic configurations. To check which Edition app is currently installed in your account, use the following command:

```sh
vtex edition get
```

If the current edition differs or is older than `vtex.edition-store@3.x`, [open a support ticket](https://help.vtex.com/support?/cultureInfo=en-us) and request the installation of the `vtex.edition-store@3.x` or a newer one in your VTEX account.

>ℹ Note that both new VTEX accounts and accounts previously using the [Legacy CMS Portal](https://help.vtex.com/tutorial/what-is-cms--EmO8u2WBj2W4MUQCS8262) need to formally request the installation of the `vtex.edition-store@3.x` or a more recent version of this Edition app. This is necessary, as every VTEX account is configured by default with the [Legacy CMS Portal](https://help.vtex.com/tutorial/what-is-cms--EmO8u2WBj2W4MUQCS8262) Edition app (`vtex.edition-business`).

Refer to the [Edition App article](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) to know more about its different versions and identify the most suitable version for your specific scenario.

### Step 2 - Implementing the VTEX Intelligent Search

Before you can begin building your storefront with Store Framework, you need to configure [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb).

>ℹ️ If you use the `vtex.edition-store@3.x` version, you must also [install the Search apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-2-prerequesites#step-2---implementing-the-vtex-intelligent-search). If you use the `vtex.edition-store@5.x`, you must start the Search Integration process directly, as the Intelligent Search is already configured by default in this version.

Intelligent Search is an advanced search engine designed to assist shoppers throughout their entire purchasing journey. It serves as an alternative to the platform's legacy native search engine, but it requires the installation of two apps on your VTEX account:

- `admin-search` - Allows stores to configure every functionality made available by the search solution, including initial catalog indexing.
- `search-resolver` - Serves as the main backend app for Intelligent Search, handling all search queries.

#### Installing the Search apps

1. Open the terminal and log in to your VTEX account:

    ```sh
    vtex login {accountName}
    ```

    >⚠️ Replace `{accountName}` with your account name.

2. After successfully logging in, run the following command to install the `admin-search` and `search-resolver` apps at the `master` workspace:

    ```sh
    vtex install vtex.admin-search vtex.search-resolver@1.x
    ```

#### Starting the Search Integration process

After successfully installing the Intelligent Search apps, follow these steps to [index and integrate](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V) Intelligent Search with your store's catalog:

1. Access the Admin.
2. Go to **Store Settings > Intelligent Search > Integrations**.
3. Click the `Start integration` button to initiate the integration process.

   ![start-integration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-2-prerequesites-0.png)

The indexing process will start, and you will receive a link to the Indexing Status screen.

Once the indexing is complete, it will fully equip you to begin using Store Framework successfully.
