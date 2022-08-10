---
title: "List Theme"
slug: "lojadalistana-list-theme"
excerpt: "lojadalistana.list-theme@0.0.1"
hidden: true
createdAt: "2022-07-29T13:31:10.616Z"
updatedAt: "2022-07-29T13:31:10.616Z"
---
This repository contains code for querying the VTEX api

## Getting started

These instructions will allow you to get a copy of the running project on your local machine for the purposes of querying the vtex api and integrating with app List.

While Store Theme gives developers a ready-to-go default store front structure, the Minimum Boilerplate Theme will enable you to build you store freely from scratch.

## Pre-Requisites

When linking the app List Theme in the store, there is an order to link each app and this order must be respected to avoid possible conflicts.

- list-graphql
- list
- list-theme
- list-checkout

## Configuration

### Step 1 - Installation or Cloning App List-Theme

#### Installation List Theme

```json
 vtex install list-theme
```

#### Cloning

To start the installation, you need to clone the GitLab project into a directory of your choice:

```json
 cd "directory of your choice"
```

SSH clone

```json
 git clone git@gitlab.com:acct.global/acct.firstpartyapps/list/list-theme.git
```

or

HTTPS clone

```json
  git clone https://gitlab.com/acct.global/acct.firstpartyapps/list/list-theme.git
```

Once the clone is done, now let's login, create the workspace and get it running in the store.

Tip: whenever you login, always check the 'manifest.json' file to get the correct name of the store.

### Step 2 - Editing the `Manifest.json`

Once in the repository directory, it is time to edit the Minimum Boilerplate `manifest.json` file.

Once in are in the file, you must replace the `vendor` and `account` values. `vendor` is the account name you are working on and `account` is anything you want to name your theme. For example:

```json
{
  "vendor": "vtex",
  "name": "list-theme"
}
```

### Step 3 - Uninstalling any existing theme

By running `vtex list`, you can verify if any theme is installed.

It is common to already have a `vtex.store-theme` installed when you start the store's front development process.

Therefore, if you find it in the app's list, copy its name and use it together with the command `vtex uninstall`. For example:

```json
vtex uninstall vtex.store-theme
```

### Step 4 - Creating your workspace in the store

Login and access the store
Access the project folder in terminal / cmd

```json
vtex login acountName
```

#### Check VTEX account and workspace

To verify the VTEX account and workspace in use, just type

```json
vtex whoami
```

##### Creating your workspace in the store

```json
vtex use `vtex0000`.
```

### Step 5 - Run and preview your store

Then time has come to upload all the changes you made in your local files to the platform. For that, use the `vtex link` command.

If the process runs without any errors, the following message will be displayed:
`App linked successfully`.

Then, run the `vtex browse` command to open a browser window having your linked store in it. This will enable you to see the applied changes in real time, through the account and workspace in which you are working.

```json
https://vtex000--vtex.myvtex.com
```

### Step 6 - Installing required apps

In order to use Store Framework and work on your store theme, it is needed to have both `vtex.store-sitemap` and `vtex.store` installed.

Run `vtex list` and check whether those apps are already installed.

If they aren't, run the following command to install them:
`vtex install vtex.store-sitemap vtex.store -f`

### Built with

Mention the tools you used to create your project

- Node
- Typescript
- GraphQl

### Version

We use SemVer for version control.
For available versions, please note the tags in this repository.


**Upcoming documentation:**

 - [Feature/remove node](https://github.com/vtex-apps/list-theme/pull/19)