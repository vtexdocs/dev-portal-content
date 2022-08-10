---
title: "Store theme - Forus"
slug: "mundodasmalhas-store"
excerpt: "mundodasmalhas.store@3.10.42"
hidden: true
createdAt: "2022-08-09T10:55:14.697Z"
updatedAt: "2022-08-09T11:07:05.271Z"
---
Theme for Forus stores.
Working with GitFlow to manage branches and SASS to compile CSS files.

### First steps
- Clone this repository
- Run ```git flow init``` (accepting defaults branch names from GitFlow)
- Run ```npm install``` or ```yarn``` on the root folder to install dependencies
- Run ```npm install -g sass``` or ```yarn global add sass```

- The **react/** and **react/components/** *.css* files are in **react/styles/** and **react/styles/components/** respectively as *.scss*.
- The **styles/css/** *.css* files are in **styles/scss/** as *.scss*

#### Watching SCSS files
- After installing all dependencies and installing sass globally, run ```npm run sass``` or ```yarn run sass``` to watch your changes.

## Tutorial
To understand how things work check our tutorial [Build a store using VTEX IO](https://vtex.io/docs/getting-started/build-stores-with-vtex-io/1)

## Dependencies
The development of Forus stores, tries to use store-framework components as much as possible, so we have few extended components.

Store framework is the baseline to create any store using _VTEX IO Web Framework_.
- [Store](https://github.com/vtex-apps/store/blob/master/README.md)

## Extended components
- Accordion Custom (Institutional pages)
- Cucarda de descuento (Product Page)
- Guia de talles (Product Page)
- Locales (Tiendas Page)
- My Account Link (My account page)
- My Account Page (My account page)
- My Account Script (My account page)
- ScrollUp (All Pages - Footer)
- Side Menu (Institutional pages)
- Stock Tiendas (Product Page)