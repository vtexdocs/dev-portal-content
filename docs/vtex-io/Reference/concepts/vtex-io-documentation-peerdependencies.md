---
title: "Peer Dependencies"
slug: "vtex-io-documentation-peerdependencies"
excerpt: "Learn what peer dependencies are their use cases."
hidden: false
createdAt: "2020-07-21T13:18:17.298Z"
updatedAt: "2022-12-13T20:17:44.256Z"
---

Peer dependencies are specified within the `manifest.json` file of a VTEX IO app under the `peerDependencies` field. This JSON object is used to declare the set of IO apps that an app requires to function seamlessly. Unlike regular [`dependencies`](https://developers.vtex.com/docs/guides/vtex-io-documentation-dependencies), which are automatically installed when someone installs an app, peer dependencies are not automatically handled by the system. Instead, it is the responsibility of the app user to ensure that the required peer dependencies are installed in their VTEX account.

Peer dependencies become particularly useful in scenarios where an app depends on paid apps or requires a specific major version of another app.

## Example

Let's illustrate this concept with an example. Suppose you have an app named `vtex.example` with the following `manifest.json` configuration:

```json
{
  "name": "vtex.example",  
  ...
  "peerDependencies": {
      "vtex.store": "2.x",
      "vtex.paid-app-example": "1.x"
  },
  "dependencies": {
      "vtex.styleguide": "9.x"
  }
  ...
}
```

In this example, anyone who wants to install the `vtex. example` app must first manually install the exact versions of `vtex.store` and `vtex.paid-app-example` apps specified in the `peerDependencies` field.

## Use cases

### Handling paid dependencies

When your app relies on a paid app, it's crucial to specify it as a peer dependency. This ensures that users who want to use your app must manually install the required paid app. This practice not only helps maintain licensing and payment compliance but also ensures that users are aware of the additional costs associated with your app's dependencies.

### Enforcing a specific major version

Consider a situation where your app depends on another app that has multiple major versions, each with significant differences that may affect your app's functionality. Instead of specifying it under `dependencies` that would install the latest version of the app, you can use the `peerDependencies` field to declare the exact major version your app requires. Users who want to install your app must ensure that the specified major version of the dependency is already installed in their account.

## Adding a peer dependency to a Store Theme app

If you want to add a new peer dependency to a Store Theme app, it involves deploying a new major version of the app. To ensure a smooth deployment, please refer to the [Migrating CMS settings after a theme major version update](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update) guide.

## Developing an app that relies on an app with peerDependencies

Now, let's consider a development scenario where you are working on an app named `X`, and this app directly depends on the `vtex.example` app. To indicate this dependency, you list `vtex.example` in the `dependencies` field of `X`'s `manifest.json` file.

Since `vtex.example` specifies `vtex.store@2.x` and `vtex.paid-app-example@1.x` as its `peerDependencies`, this means that to develop `X` (which includes `vtex.example` in its `dependencies`), you must manually install `vtex.store@2.x` and `vtex.paid-app-example@1.x` in the VTEX account in which you are working.

>⚠️ Keep in mind: Peer dependencies are not automatically installed. You must manually install them in your working account.

If your account lacks these specific versions of `vtex.store@2.x` and `vtex.paid-app-example@1.x`, you won't be able to install the `vtex.example` and your development flow will be interrupted.

Notice that the `vtex.example` requires every account installing it also to have `vtex.store@2.x` and `vtex.paid-app-example@1.x` installed. 

Remember that these dependencies are a manual prerequisite and should be documented clearly for your users.


