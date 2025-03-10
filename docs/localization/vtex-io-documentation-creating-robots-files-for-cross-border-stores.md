---
title: "Creating robots files for cross-border stores"
slug: "vtex-io-documentation-creating-robots-files-for-cross-border-stores"
hidden: false
createdAt: "2020-09-15T12:24:38.963Z"
updatedAt: "2025-03-10T12:32:29.211Z"
---

This guide explains how to develop and release a Robots app to manage ´robots.txt´ files for cross-border stores using Store Framework.

A `robots.txt` file controls which folders or files search engines can crawl on a website. Given its impact on a store’s SEO, the following steps explain how to create `robots.txt` files for cross-border stores.

>❗ This guide applies only to cross-border stores. If your store is not cross-border, refer to [this guide](https://help.vtex.com/tutorial/google-search-console-tracking-robots-txt--tutorials_574?locale=en).

## `robots.txt` file structure
See below the basic structure of a `robots.txt` file:

- `User-agent`: Specifies the search engine robot to which the following rules apply. To apply the same rules to all robots, use `*`.
- `Disallow`:  Defines the paths (relative to the root directory) of files or folders that the search engine specified in `User-agent` must not index.
- `Allow`: Specifies the paths of files within a `Disallowed` folder that are allowed to be crawled and indexed.

You must adjust these directives according to your scenario.

## Before you begin

This feature is available for stores using `vtex.edition-store@3.x` [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app/) or newer. To check which Edition app is installed on your account, run `vtex edition get`. If your store is using an older Edition, [open a ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) with VTEX Support asking for the installation of the `vtex.edition-store@5.x`.

## Instructions

Follow the steps below to develop your Robots app:

1. Using the command below, clone the `store-theme-robots` app boilerplate repository.

```
git clone https://github.com/vtex-apps/store-theme-robots
```

2. Once successfully cloned, open the local app directory in your code editor.

3. Open the `manifest.json` file and edit the `vendor` field with the name of the developing account.

```json
{ 
  "vendor": "myaccount",
  "name": "robots",
  "version": "0.0.1",
  "builders": {
    "sitemap": "0.x"
  },
  ...
}
```

4. Inside the `sitemap/robots` folder, create a `.txt` robots file for each supported locale binding. The name of each file must be the `id` value of its respective `binding`.

>⚠️ Follow [this tutorial](https://developers.vtex.com/docs/guides/checking-your-stores-binding-id) to check your stores' `binding` `id`s.

Your app's folder may end up with a structure similar to the following:

```
store-theme-robots
├── manifest.json
├── README.md
└─┬ sitemap
  └─┬ robots
    ├── 706e9126-d0fc-47de-9o2d-5f9649e61877.txt
    └── 748aafcf-1674-456d-9ffc-7ddb3f26e43f.txt
```

5. Edit each file from the `sitemap/robots` folder with the desired content for each one of your `robots` files.

6. Once everything is set up, use the terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference/) to log in to the VTEX Account in which you are currently working in.

7. Run `vtex use {workspace}` to use a developer environment.

>⚠️ Remember to replace the values between the curly brackets according to your scenario.

8. Run `cd store-theme-robots` to go to the local app directory.

9. Run `vtex link` to [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) your new app to your development workspace.

10. Check the `robots` file generated for each store by accessing `https://{workspace}--{account}.myvtex.com/{locale}/robots.txt` on your browser.

11. Follow the guide [Deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) to test your Robots app in a [production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace) and, once you’re satisfied with the result, promote it to master.

>⚠️ The Robots app must be tested in a [production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace).

Now, you’re ready to check out your store's `robots` files by accessing `https://{account}.myvtex.com/{locale}/robots.txt` on your browser, replacing the values between the curly brackets according to your scenario.
