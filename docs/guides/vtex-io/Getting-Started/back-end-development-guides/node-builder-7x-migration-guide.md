---
title: "Node builder 7.x migration guide"
slug: "node-builder-7x-migration-guide"
excerpt: "Learn how to update your Node app to builder version 7.x."
hidden: false
createdAt: "2024-10-10T10:00:00.000Z"
updatedAt: "2024-11-01T10:00:00.000Z"
---

With the [Node builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-node-builder) update to version `7.x`, IO apps using this builder benefit from the Node.js 20 engine and TypeScript 5.x libraries, improving performance and security. However, this also means these apps need to be adjusted for the latest features.

Check the demo video below showing how to migrate your app to Node builder `7.x`.

<iframe width="100%" style="aspect-ratio: 16/9" src="https://www.youtube.com/embed/sTSf7AZLqGg?si=eM_SIxKMAgsROXf5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="allowfullscreen"></iframe>

## Instructions

To update your app to use the new builder version, follow the instructions below:

1. Update the VTEX IO CLI to version `4.1.0` or newer.
    1. In a terminal, run `vtex -v` to check your VTEX IO CLI version. If you do not have VTEX IO CLI installed, you can find the instructions in [Installing VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install).
    2. If your version is older than `4.1.0`, run `vtex autoupdate` to update your VTEX IO CLI.
2. Make sure `node/package.json` has the `typescript` property in `devDependencies`.
    3. In your app folder, open the `node/package.json` file.
    4. In the `devDependencies` property, check if the `typescript` package is declared. If it is not, add it with version `5.x`. It should look like this:

        ```json node/package.json
        "devDependencies": {
          ...
          "typescript": "5.x"
        },
        ```

        > ℹ️ If the app already has `typescript` declared in `devDependencies`, you don’t need to change its version manually. When linking the app, the package version is overwritten automatically.

3. Update the `manifest.json` with `node 7.x`.
    1. In your app folder, open the `manifest.json` file.
    2. Change the `node` builder version to `7.x`. It should look like this:

        ```json manifest.json
        "builders": {
          ...
          "node": "7.x"
        },
        ```

4. Test the app.
    1. Open a terminal in the root folder of your app.
    2. Make sure you are in a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace). You can create a new one or switch to an existing one.
    3. Run `vtex link`. You will notice that the `node/package.json` will be updated with the new versions of `typescript` (`5.5.3`) and `@node/types` (`20.x`).
    4. Check errors and fix them if they appear. Your app might not be fully compatible with the newer TypeScript and Node.js engine versions, and syntax, typing, or dependency errors might occur. See the [Troubleshooting](#heading=h.2w3bbhmrvkih) section for instructions about the most common errors.
5. Create and deploy a new app version following the steps in [Deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available).
    1. In the [Release a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version) step, we recommend creating a **minor** version since this update is not exclusively fixing issues as in a **patch**, and a **major** version would require additional work.
        > ⚠️  For apps in the [App Store](https://developers.vtex.com/docs/guides/vtex-app-store), creating a new **major** version will require the app to go through the [homologation process](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store#step-2-managing-the-homologation-process).
    2. Follow the other steps (Publish, Test, Deploy, and Promote) as needed. Some apps are used only on one account, while others should deploy the new version to multiple accounts.

If you need help migrating your app to Node builder `7.x`, open a ticket with [VTEX Support](https://help.vtex.com/en/support).

## Troubleshooting

When migrating your app to the new builder version, some issues might occur. The following sections show the most common issues and what can be done to solve them.

### Typing errors

When linking your app, you might get an error in the following format:

`Argument of type <type>| undefined' is not assignable to a parameter of type '<type>'.`

This means that the argument is being declared as a certain type and is recognized as `undefined`.

**Solution**: You must ensure the argument is not `undefined`, or update the [field type to be optional](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#optional-properties).

### "yarn lint" at the project root

Errors may occur in the following scenario:

1. There’s a lint configuration at the root of the project. It should be in files such as `.eslintrc` and `.eslintignore`.
2. The `package.json` file in the root is configured with an old version of TypeScript. For instance, the file has TypeScript version `3.9.6`, but Node builder `7.x` uses `5.5.3`.
3. Something used in the code (a class, a library, etc.) doesn’t exist in the old TypeScript version.

**Solution**: Update the TypeScript version in the root `package.json`. We recommend using version `5.5.3`, since it’s used in Node builder `7.x`.

**Side effect**: If the app uses the `eslint-config-vtex` package, you will get a warning in the console about version incompatibility.

### Alerts related to different TypeScript versions

When linking your app, you might get errors like the following examples:

- `@vtex/tsconfig@0.6.0" has incorrect peer dependency "typescript@^`
- `eslint-config-vtex@10.1.0" has incorrect peer dependency "typescript@^3.3.3333"`

These alerts may appear because some of the app's dependencies may run with an old TypeScript version.

ℹ️ Errors in this scenario might be due to some VTEX libraries not being updated with TypeScript `5.x`. They should be updated gradually over time.

**Solution**: Update the `package.json` files of the dependencies manually with the new TypeScript version. We recommend using version `5.5.3`, since it’s the same used in Node builder `7.x`.

### Error with MetricsAggregator

If you’re accessing `global.metrics` in your code, defined by the `node-vtex-api` library, you should get the error:

`Property 'metrics' does not exist on type 'typeof globalThis'.`

This happens because of a breaking change between versions `12.x` and `20.x` of `@types/node`.

**Solution:** Use `global` as `any`, replacing `global` with `(global as any)` in your code. Example: `(global as any).metrics`.
