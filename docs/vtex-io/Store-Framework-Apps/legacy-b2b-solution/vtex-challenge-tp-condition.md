---
title: "Challenge Trade Policy Condition"
slug: "vtex-challenge-tp-condition"
hidden: true
createdAt: "2020-06-03T15:19:30.796Z"
updatedAt: "2024-01-31T13:29:19.890Z"
---

Used in B2B environments, the Challenge block is a non-rendered block responsible for checking if a user is allowed to access the store's content.

> ℹ️ This check is made according to the Condition Rule specified in the Trade Policy configuration, one of the steps needed to [**configure a B2B environment in VTEX IO**](https://developers.vtex.com/docs/guides/vtex-io-documentation-configuring-a-b2b-environment).

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

> ⚠️ Using `hidden` as the `defaultContentVisibility` value result in the entire page's content being rendered on the client side (in a scenario in which the check concludes that the user has permission to access the store). The page will not be Server Side Rendered (SSR) due to the fact that this verification process is user-based, making it impossible to cache.

## Customization

No CSS Handles are available for the app customization.
