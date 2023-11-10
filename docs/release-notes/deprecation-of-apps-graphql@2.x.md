---
title: "Deprecation of apps-graphql@2.x"
slug: "deprecation-of-apps-graphql@2.x"
hidden: false
createdAt: 2023-03-02T16:18:00.000Z
type: "deprecated"
excerpt: "Aiming to improve security practices in our ecosystem, we revised the access authorization policies on our platform and have decided to deprecate version `2.x` of `apps-graphql`. Apps using this dependency must update to version `3.x` by March 10th, 2023."
---

`apps-graphql` is a GraphQL API module for VTEX IO Apps. It is frequently included as a dependency for apps that have their settings managed via Admin and on frontend applications.

Aiming to improve security practices in our ecosystem, we revised the access authorization policies on our platform and have decided to deprecate version `2.x` of `apps-graphql`. Apps using this dependency must update to version `3.x` by March 15th, 2023.

## What has changed?

On March 15th, 2023, VTEX will deprecate `apps-graphql@2.x`. As a result, unauthenticated requests to this version will return authentication errors.

## Why did we make this change?

With the update of `apps-graphql` to version 3.x, we can restrict unauthorized access to private configuration data, yield better control over sensitive actions, and, therefore, improve security for all VTEX stores. Since these features are not available on version `2.x`, we will deprecate it for security reasons.

## What needs to be done?

All customers and agencies are advised to upgrade their dependency to `apps-graphql@3.x` and explicitly declare in the app's [manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) what settings can be public.

In order to continue to have access to the public settings of a given app, use the new query `publicSettingsForApp` following this [sample Pull Request](https://github.com/vtex-apps/shopper-location/pull/57).

If for some reason the app needs a private setting (an API Key, for instance), create a new resolver in the app and make an authenticated query to `appSettings`. You can check an example in this [sample Pull Request](https://github.com/vtex-apps/shopper-location/pull/59).
