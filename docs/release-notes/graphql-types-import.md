---
title: GraphQL types imports
excerpt: "Save your precious time while developing! From now on, easily import GraphQL types from one app to another."
createdAt: "2019-09-26T14:47:00.000Z"
---

GraphQL types can now be easily imported from one app to another, as was already the case with React types, by running the `vtex setup` command.

## What has changed 

Before this improvement, there was no way to automatically import needed GraphQL types from an app to another. The developer had to highlight in the typescript code each GraphQL type needed for an app's (which dependeded on another app types) proper functioning. 

The good new is that now, based on schema files in app's  `graphql` folder,  **GraphQL types can easily be imported to your typescript code.**. 

### How it works

In your terminal, simply run the  `vtex setup`  or  `vtex link --setup`  command in order to add all the dependencies types your app needs in its node and react `package.json`.

Suppose you want to use app's `A` GraphQL and React types in app `B`. After adding app `A` as an dependency of app `B` and running  `vtex setup` or `vtex link --setup`, you'll be able to import A types to B by simply using typescript imports:

```
import {GraphQLType}, {ComponentType} from {{Vendor}.{AppName}} 
```


> ⚠️ Remember to replace the values above in {} with values compatible with your scenario.


## Main advantages 

This feature removes the need to incessantly define an app's every GraphQL type to another. This makes the app building process easier and simpler for the developer. 

## What you need to do 

This feature is available to stores running VTEX IO CLI version **2.74.0** or higher and **Builder-hub** version **0.171.0** or higher.

> ℹ️ You can run `vtex -v` in your VTEX IO CLI in order to check its version and `npm i -g vtex` or `yarn global add vtex` in order to update it. The Builder-hub update should occur automatically.
