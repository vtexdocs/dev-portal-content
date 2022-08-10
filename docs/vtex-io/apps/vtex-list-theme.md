---
title: "List Theme"
slug: "vtex-list-theme"
excerpt: "vtex.list-theme@1.2.0"
hidden: true
createdAt: "2022-07-11T22:06:58.591Z"
updatedAt: "2022-08-08T11:25:56.635Z"
---
The basic theme to use the Gift List

## Preview

**Initial Page**

<img width="1440" alt="Captura de Tela 2022-08-03 às 14 18 36" src="https://user-images.githubusercontent.com/80836180/182934559-c06e37e9-ec91-4509-ad7c-0de299870088.png">

**User Page**

<img width="1440" alt="Captura de Tela 2022-08-03 às 17 12 51" src="https://user-images.githubusercontent.com/80836180/182934493-c73f81a1-2fc8-410a-904a-ae4d47165f47.png">

**Wallet User Page**

<img width="1440" alt="Captura de Tela 2022-08-03 às 14 55 29" src="https://user-images.githubusercontent.com/80836180/182934554-3f32efd8-4ec8-48bb-afc8-6071a752c41a.png">

**List Page**
![Captura de Tela 2022-08-03 às 17 09 16 (2)](https://user-images.githubusercontent.com/80836180/182934546-f53ab5be-6504-4380-860b-85e3f1382a91.png)

## Dependencies

To use this template it's necessary to use the

```bash
  "peerDependencies": {
    "vtex.list": "1.x"
  }
```

to be able to access these essential components to create the list store theme:

<ul>
<li>Add To Cart</li>
<li>Add To List</li>
<li>Auth Condition</li>
<li>BreadCrumbs</li>
<li>Content Loader</li>
<li>Create List</li>
<li>Edit List</li>
<li>Gifted List</li>
<li>List Info</li>
<li>List Items Gallery</li>
<li>List Items OrderBy</li>
<li>Page Wrapper</li>
<li>Page wrappers</li>
<li>Product Summary Quantity</li>
<li>Quantity Selector</li>
<li>Search List</li>
<li>Search List Item</li>
<li>Share List</li>
<li>User Lists</li>
<li>Wallet</li>
</ul>

Another store components are used like:

- [Header](https://github.com/vtex-apps/store-header/blob/master/docs/README.md)
- [Footer](https://github.com/vtex-apps/store-footer/blob/master/docs/README.md)
- [Slider Layout](https://github.com/vtex-apps/slider-layout/blob/master/docs/README.md)
- [Shelf](https://github.com/vtex-apps/shelf/blob/master/docs/README.md)
- [Login](https://github.com/vtex-apps/login/blob/master/docs/README.md)
- [Minicart](https://github.com/vtex-apps/minicart/blob/master/docs/README.md)
- [Breadcrumb](https://github.com/vtex-apps/breadcrumb/blob/master/docs/README.md)
- [Search Result](https://github.com/vtex-apps/search-result/blob/master/docs/README.md)
- [Product Details](https://github.com/vtex-apps/product-details/blob/master/docs/README.md)

To use this components remember to add the dependencies in manifest (see more [here](https://github.com/vtex-apps/list-theme/blob/master/manifest.json#L17-L60))

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

It is common to already have an another theme installed when you start the store's front development process.

Therefore, if you find it in the app's list, copy its name and use it together with the command `vtex uninstall`. For example:

```json
vtex uninstall vtex.store-theme
```

### Step 4 - Creating your workspace in the store

Login and access the store
Access the project folder in terminal / cmd

```json
vtex login accountName
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

We recomend use the `vtex.edition-store@5.x`, to you can use the Store Framework and work on your store theme.

To confere if you are using this app, run `vtex edition get` and check if this apps is already installed and is in the version bigger or equal a 5.

If there isn't, please open an call to support team and request to install this version.