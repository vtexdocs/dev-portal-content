---
title: "Corebiz - Store theme - Forus"
slug: "vanscl-vansio-app"
excerpt: "vanscl.vansio-app@3.0.13"
hidden: true
createdAt: "2022-07-04T20:37:19.336Z"
updatedAt: "2022-08-08T17:20:12.899Z"
---
Corebiz Theme for Forus stores.
Working with GitFlow to manage branches and SASS to compile CSS files.

### First steps

- Clone this repository
- Run `git flow init` (accepting defaults branch names from GitFlow)
- Run `npm install` or `yarn` on the root folder to install dependencies
- Run `npm install -g sass` or `yarn global add sass`

- The **react/** and **react/components/** _.css_ files are in **react/styles/** and **react/styles/components/** respectively as _.scss_.
- The **styles/css/** _.css_ files are in **styles/scss/** as _.scss_

#### Watching SCSS files

- After installing all dependencies and installing sass globally, run `npm run sass` or `yarn run sass` to watch your changes.

## Tutorial

To understand how things work check our tutorial [Build a store using VTEX IO](https://vtex.io/docs/getting-started/build-stores-with-vtex-io/1)

## Dependencies

The development of Forus stores, tries to use store-framework components as much as possible, so we have few extended components.

Store framework is the baseline to create any store using _VTEX IO Web Framework_.

- [Store](https://github.com/vtex-apps/store/blob/master/README.md)

## Extended components

- Accordion Custom (Institutional pages)
- Cucarda de descuento (Product Page)
- FreshDesk (Contact Page)
- Guia de talles (Product Page)
- Locales (Tiendas Page)
- My Account Link (My account page)
- My Account Page (My account page)
- My Account Script (My account page)
- ScrollUp (All Pages - Footer)
- Side Menu (Institutional pages)
- Stock Tiendas (Product Page)