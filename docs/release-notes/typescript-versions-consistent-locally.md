---
title: 'Typescript versions consistent locally'
excerpt: 'The VTEX IO CLI now overwrites local `package.json` dependencies to match the same Typescript version as in current Builder-Hub.'
createdAt: '2019-12-12T18:27:49.833Z'
---

The VTEX IO CLI now overwrites local `package.json` dependencies to match the same Typescript version as in current Builder-Hub.

:eyes: Builder-Hub now uses Typescript 3.5.2. It previously used version 3.4.3.

## Key advantage

As the local `Package.json` was not overwritten, there was a mismatch between its Typescript version and Builder-Hub's. Due to this inconsistency, an IDE running on the user's machine could report different type errors as the ones reported by Builder-Hub. Now, this issue is fixed. 

## What you need to do

When running the VTEX IO CLI on your app, you will see that your `package.json` might change. Commit that change to your version control.

## Side effects

Typescript 3.5.2 has differences when it comes to type checking that might cause the build of your app to fail. In that case, you will need to revisit the typing of some variables.
