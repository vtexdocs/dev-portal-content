---
title: "VTEX List"
slug: "lojadalistana-list"
excerpt: "lojadalistana.list@0.1.0"
hidden: true
createdAt: "2022-07-29T13:29:54.115Z"
updatedAt: "2022-07-29T13:41:18.519Z"
---
The repository contains code that queries VTEX APIs, describes components and their behaviors.

## Getting started

These instructions will allow you to get a copy of the running project on your local machine for the purposes of querying the VTEX APIs and integrating with app List.

## Pre-Requisites

When linking the app List in the store, there is an order to link each app and this order must be respected to avoid possible conflicts.

1. list-graphql
2. list
3. list-theme

## Components

Below is a list of all the components in our app list

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
</ul>

## Configuration

In this section, you first must **add the primary instructions** that will allow users to use the app's blocks in their store, such as:

1. Adding the app as a theme dependency in the `manifest.json` file;
2. Declaring the app's main block in a given theme template or inside another block from the theme.

Remember to add a table with all blocks exported by the app and their descriptions. You can verify an example of it on the [Search Result documentation](https://vtex.io/docs/components/all/vtex.search-result@3.56.1/).

### Setting up development Environments

To start, first clone this repo into a folder of your choice

#### Installation List

```json
 vtex install list
```


#### Creating your workspace in the store

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

#### Creating your workspace in the store

```json
vtex use `vtex0000`.
```

#### Run and preview your store

Then time has come to upload all the changes you made in your local files to the platform. For that, use the `vtex link` command.

If the process runs without any errors, the following message will be displayed: 
`App linked successfully`.

Then, run the `vtex browse` command to open a browser window having your linked store in it. This will enable you to see the applied changes in real time, through the account and workspace in which you are working.

```json
https://vtex000--vtex.myvtex.com
```


## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`


## Built with

- Node
- Typescript
- GraphQl


## Version

We use SemVer for version control.
For available versions, please note the tags and changelog file in this repository.


**Upcoming documentation:**

 - [Release/0.18.0](https://github.com/vtex-apps/list/pull/10)
 - [Release/0.17.0](https://github.com/vtex-apps/list/pull/9)
 - [Release/0.15.1](https://github.com/vtex-apps/list/pull/7)
 - [Release 0.1.0](https://github.com/vtex-apps/list/pull/1)
 - [Develop](https://github.com/vtex-apps/list/pull/3)
  
=======

- [Breadcrumb](https://github.com/vtex-apps/breadcrumb)
- [Image](https://vtex.io/docs/components/general/vtex.store-components/image)
- [Condition Layout](https://vtex.io/docs/components/all/vtex.condition-layout@1.1.6/)
- [Add To Cart Button](https://vtex.io/docs/components/content-blocks/vtex.add-to-cart-button@0.9.0/)
- [Store Form](https://vtex.io/docs/components/all/vtex.store-form@0.3.4/)

 - [add function to install automatically others apps](https://github.com/vtex-apps/list/pull/22)
 - [Feature/create user](https://github.com/vtex-apps/list/pull/23)
 - [Feature/set order form](https://github.com/vtex-apps/list/pull/24)
 - [Feature/set hook](https://github.com/vtex-apps/list/pull/25)