---
title: "Challenge Trade Policy Condition"
slug: "vtex-challenge-tp-condition"
excerpt: "vtex.challenge-tp-condition@0.6.0"
hidden: false
createdAt: "2020-06-03T15:19:30.796Z"
updatedAt: "2021-04-29T13:29:19.890Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Used in B2B environments, the Challenge block is a non-rendered block responsible for checking if a user is allowed to access the store's content. 

:information_source: This check is made according to the Condition Rule specified in the Trade Policy configuration, one of the steps needed to [**configure a B2B environment in VTEX IO**](https://vtex.io/docs/recipes/store/configuring-a-b2b-environment). 

## Configuration

1. Import the app to your theme's dependencies in `manifest.json`, for example:

```json
  "dependencies": {
    // ...
    "vtex.challenge-tp-condition": "0.x"
  }
```

2. Add the  `challenge.trade-policy-condition` block as a `parent` block to the templates of the pages you want to protect, such as:

```diff
 "store.home": {
   "blocks": [
     "shelf#home",
     "flex-layout.row#deals",
     "info-card#home",
     "rich-text#question",
     "rich-text#link",
     "newsletter"
   ],
+   "parent": {
+     "challenge": "challenge.trade-policy-condition"
+   }
 },
 
```

3. Declare the `challenge.trade-policy-condition`, using its props to define to where the store's users should be redirected according to each scenario. For example:

```json
"challenge.trade-policy-condition": {
  "props": {
    "redirectPath": "/login"
  }
},
```

| Prop name          | Type |    Description   | Default value | 
| ------------------------ | ------------- | --------------------- | ----------- | 
| `redirectPath`             | `string` | Path to which the not logged in user will be redirected      |  `/login`          | Path to which the not logged in user will be redirected                     |
| `forbiddenRedirectPath`    | `string`    | Path to which the logged in user will be redirected if not allowed access according to the Condition Rule         |   `/login`      |
| `defaultContentVisibility` |   `enum`  |  Whether the store's content should be visible (`visible`) or hidden (`hidden`) while the Challenge block is verifying the user's access permission | `visible` | 
 
:warning: Using `hidden` as the `defaultContentVisibility` value result in the entire page's content being rendered on the client side (in a scenario in which the check concludes that the user has permission to access the store). The page will not be Server Side Rendered (SSR) due to the fact that this verification process is user-based, making it impossible to cache.

## Customization

No CSS Handles are available for the app customization.

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->