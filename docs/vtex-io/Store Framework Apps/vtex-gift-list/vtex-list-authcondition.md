---
title: "Auth Condition"
slug: "vtex-list-authcondition"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.833Z"
updatedAt: "2022-12-01T16:44:24.195Z"
---
The `auth-condition` performs validation that the user is logged in to render different layouts.

![AuthCondition](https://user-images.githubusercontent.com/67066494/190255470-dda6e057-0a38-480c-8e10-31e6a93acca1.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `auth-condition` block for conditional validation in a template, like the one from home. For example:

```diff
   "store.home": {
    "blocks": [
+     "auth-condition",
    ]
  }
```

3. Add the rendering condition you want by passing the blocks via props. For example:

```diff
"auth-condition": {
    "props": {
      "Then": "flex-layout.row#home-with-user",
      "Else": "flex-layout.row#home-without-user"
    }
  }
```

### Props

| Prop Name | Type  | Description                                                     | Default value |
| --------- | ----- | --------------------------------------------------------------- | ------------- |
| Then      | block | Name of the block to be rendered if the conditions are met.     | undefined     |
| Else      | block | Name of the block to be rendered if the conditions are not met. | undefined     |