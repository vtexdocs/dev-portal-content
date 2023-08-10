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

Now that you have completed the VTEX IO basic setup, it is time to:

- [1. Set your account's Edition app.](#step-1---setting-your-accounts-edition-app)
- [2. Implement the VTEX Intelligent Search.](#step-2---implementing-the-vtex-intelligent-search)

By meeting these two prerequisites, your store is apt to use the VTEX Store Framework, free from any technical issues that could emerge due to flaws during the implementation steps.

## Step 1 - Setting your account's Edition app

An [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app/) is a mandatory app that exports a bundle of settings and basic configurations to the VTEX account in which it is installed.

By default, every VTEX store comes with the Edition app for building storefronts with [Legacy CMS Portal](https://help.vtex.com/tutorial/what-is-cms--EmO8u2WBj2W4MUQCS8262) installed. To use the [VTEX Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework) instead, get in touch with our [Customer Care team](https://help.vtex.com/support?/cultureInfo=en-us) and request the installation of the `vtex.edition-store@3.x` app in your VTEX account.

> ⚠️ Whether you are a new VTEX account or a former account using [Legacy CMS Portal](https://help.vtex.com/tutorial/what-is-cms--EmO8u2WBj2W4MUQCS8262), installing the `vtex.edition-store@3.x` Edition app is necessary to implement the Store Framework solution successfully.

## Step 2 - Implementing the VTEX Intelligent Search

So you can start customizing your storefront with VTEX Store Framework, you first need to configure the [VTEX Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb).

VTEX Intelligent Search is an intelligent search engine for e-commerce that aims to assist customers throughout their entire purchasing journey.

The solution is an alternative to the platform's old native search engine and requires the installation of the following two apps on your VTEX account:

- `admin-search` - Allows stores to configure every functionality made available by the search solution, including first-time catalog indexing.
- `search-resolver` - Solves all search queries, being the main back-end app from the Intelligent Search.

### Installing the Search apps

1. Log in to your VTEX account using your terminal:

```sh
vtex login {account}
```

> ⚠️ Replace the value between curly braces according to your scenario.

2. Once logged in, run the following command to list the apps already installed on your account:

```sh
vtex list
```

3. If any of the two apps is missing from the list, install them using the VTEX IO CLI at the `master` workspace as in the following:

```sh
vtex install vtex.admin-search vtex.search-resolver@1.x
```

### Starting the Search Integration process

After installing the Search apps, you will need to start indexing and integrate VTEX Intelligent Search with your store's Catalog.

1. Go to your VTEX store's admin.
2. In the side menu, go to *Store Setup > Search > [Integration settings](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V)*.
3. Press the *Start integration* button to start integration.

![start-integration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-2-prerequesites-0.png)

The indexing process will start, and you will then see a link to the Indexing Status screen.

Once the indexing is finished, you'll be ready to start using VTEX Store Framework successfully. Time to get busy! Let's go?
