---
title: "Internationalization"
slug: "vtex-io-multi-language-stores"
hidden: false
createdAt: "2020-08-31T17:15:01.754Z"
updatedAt: "2021-03-17T13:43:00.948Z"
excerpt: "Get to know the internationalization process for creating a multi-language e-commerce store using Store Framework."
---

This document outlines the internationalization process for creating a multi-language e-commerce store using Store Framework. Internationalization is crucial for reaching global markets and providing a seamless shopping experience for customers from different locales. This guide covers how Store Framework handles internationalization for both storefront content and catalog data, highlighting the tools and libraries used for translations.

## Before you start

Before delving into the internationalization process, it's essential to understand the distinction between frontend app messages and catalog data. In general, **storefront content** can be sourced from either **frontend React apps** or the **[Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview)**. More precisely, app messages are translatable strings defined within a frontend app, while catalog messages comprise external data from the Catalog API. Therefore, it is crucial to consider these differences when translating storefront content, as internationalization is handled differently for each case. 

## Frontend app messages

A Store Framework storefront consists of multiple frontend apps built with VTEX IO and React. For translations, Store Framework uses the [react-intl](https://www.npmjs.com/package/react-intl) library and the VTEX IO Messages app. 

Moreover, when developing a frontend app, developers can designate text components as translatable messages using the `<Formatted*>` component from the `react-intl` library. This enables translatable messages to be automatically translated by an automatic translation service based on the user's locale.

### Automatic translations

The Messages app can automatically translate frontend app messages based on the user's locale using the automatic translation service. In such cases, the current locale and the corresponding set of translated messages obtained from the automatic translation system become accessible at the root of the component tree and made available to each component. 

However, automatic translations may not always be culturally accurate. To address this, the Messages app provides functionalities to manage custom translations.

### Customizing automatic translations

To address potential cultural inaccuracies in automatic translations, the Messages app provides functionalities to manage custom translations. Developers can overwrite an automatic translation with more specific or representative content for their store, such as providing a special login message for Spanish-speaking users from Argentina.

Custom translations can be implemented at either the app or account level:

- **App-level translations**: Developers can set personalized translations for each locale within the `/messages` folder of the frontend app. These translations are applied, by default, to any store using the app. To learn how to set messages during the development of a React app, please follow this [guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-8-translating-the-component).
- **Account-level translations**: Developers can overwrite a message imported from a frontend app with a completely customized message making the appropriate GraphQL API request to the Messages app. To learn how to overwrite a message from a storefront app, please follow this [guide](https://developers.vtex.com/docs/guides/storefront-content-internationalization).

> The Messages app is a standalone translation application and should not be confused with a string repository. It requires providing a source language, source content, and destination language. The output will be the translation of the source content from the source language to the destination language.

### Translation decision flow

When translating a message, the Messages app follows a specific decision flow:

1. Check for custom account-level translations.
2. If no custom definitions are found, it checks for storefront app translations in the `/messages` folder of the app.
3. If a specific translation is still not found, the Messages app falls back to the automatic translation service.

As translating an app to every language can be a daunting task, it is recommended to structure precise translations for the target audience and rely on automatic translation for other languages.

Note that, after detecting a user locale, every message from your storefront components set as translatable will be automatically translated either by the automatic translation service, the storefront app's messages, or custom content personalized through a GraphQL mutation at the account level.

## Catalog data

So far, we've discussed app messages, which are text messages exported from a frontend app. However, we must also consider catalog messages, which include messages related to a product name or product description from the store catalog.

Every data from the Catalog API is already set as translatable. Therefore, it is possible to overwrite an automatic catalog translation by sending the appropriate GraphQL query either to the Catalog API or to the Messages app.

To learn how to overwrite a catalog message via the Catalog API, please follow this [guide](https://developers.vtex.com/docs/guides/catalog-internationalization).
