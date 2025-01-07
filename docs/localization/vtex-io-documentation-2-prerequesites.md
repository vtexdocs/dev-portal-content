---
title: "2. Configuring your account"
slug: "vtex-io-documentation-2-prerequesites"
hidden: false
createdAt: "2020-08-11T07:03:18.428Z"
updatedAt: "2024-11-21T20:12:49.926Z"
category: "Storefront Development"
excerpt: "Set up your account Edition to get started with Store Framework."
---

Once you have completed the set up of your development workspace, configure your account to leverage the full power of the VTEX Store Framework. This guide will walk you through two essential prerequisites:

- [Setting your account's Edition app](#step-1---setting-your-accounts-edition-app)
- [Implementing the VTEX Intelligent Search](#step-2---implementing-the-vtex-intelligent-search)

## Instructions

### Step 1 - Setting your account's Edition app

The [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app/) plays a pivotal role in your VTEX account by installing a bundle of settings and basic configurations. To check which Edition app is currently installed in your account, use the following command:

```sh
vtex edition get
```

If the current edition differs or is older than `vtex.edition-store@3.x`, [open a support ticket](https://help.vtex.com/support?/cultureInfo=en-us) and request the installation of the `vtex.edition-store@3.x` or a newer one in your VTEX account.

Learn more about the available versions and find the one that best fits your needs in the [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) guide.

>ℹ Both new VTEX accounts and those previously using the [Legacy CMS Portal](https://help.vtex.com/tutorial/what-is-cms--EmO8u2WBj2W4MUQCS8262) must formally request the installation of the `vtex.edition-store@3.x` or a more recent version of the Edition app. This is necessary as every VTEX account is configured by default with the `vtex.edition-business` version, which is the Legacy CMS Portal Edition app.

### Step 2 - Implementing the VTEX Intelligent Search

Before start building your storefront with Store Framework, configure [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb), which is an advanced search engine designed to assist shoppers throughout their entire purchasing journey.

It is an alternative to the platform's legacy native search engine, but it requires the installation of two apps on your VTEX account:

- `admin-search`: Allows stores to configure every functionality made available by the search solution, including initial catalog indexing.
- `search-resolver`: Serves as the main backend app for Intelligent Search, handling all search queries.

>ℹ️ If you use the `vtex.edition-store@3.x` version, you must also [install the Search apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-2-prerequesites#step-2---implementing-the-vtex-intelligent-search). If you use the `vtex.edition-store@5.x`, you must start the Search Integration process directly, as the Intelligent Search is already configured by default in this version.

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

After installing the Intelligent Search apps, follow these steps to index your store's catalog and integrate it with Intelligent Search:

1. In the VTEX Admin, go to **Store Settings > Intelligent Search > Integrations**.
2. Click `START INTEGRATION`.
   ![start-integration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-2-prerequesites-0.png)

The indexing process will start, and you will receive a link to the Indexing Status screen. Once completed, your store will be fully prepared to use the Store Framework effectively.
