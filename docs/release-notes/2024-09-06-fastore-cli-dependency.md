---
title: "FastStore: Simplified FastStore setup with FastStore CLI dependency update"
slug: "2024-09-06-fastore-cli-dependency"
type: "added"
excerpt: "The new FastStore CLI version now depends on the FastStore Core package, simplifying the installation process and reducing potential version conflicts."
createdAt: "2024-09-03T11:00:00.000Z"
---

To simplify the installation process and reduce potential version conflicts, the [FastStore Core (`@faststore/core`)](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson) package now directly depends on [FastStore CLI (`@faststore/cli`)](https://developers.vtex.com/docs/guides/faststore/getting-started-3-faststore-cli).

## What has changed?

Previously, both [`@faststore/core`](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson) and [`@faststore/cli`](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson) packages were required dependencies in the [`package.json`](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson) file to install and run a FastStore project.

Now, the new `@faststore/cli` version depends on the `@faststore/core` package, eliminating the need for an explicit dependency of both in the `package.json` file, preventing potential version conflicts, and simplifying installation.

## What needs to be done?

If the `@faststore/cli` is already listed in your `dependencies`, no further action is needed. To check if the package is listed, open your FastStore project in a code editor, go to the `package.json` file, and check the `dependencies` property. For example:

``` package.json
 "dependencies": {
    "@faststore/cli": "^3.0.87",
    "next": "^13.5.6",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
```

If the `@faststore/cli` is not listed, follow these steps:

>⚠️ Before applying the following changes to your production environment, test them in a local development environment to ensure compatibility and avoid issues with your live store.

1. Open your FastStore project in a code editor, navigate to the `package.json` file, and locate the `dependencies` property.

2. In the `dependencies` property, replace `@faststore/core` with `@faststore/cli`. Before removing the `@faststore/core`, the `dependencies` property might look like this:

    ``` package.json
    "dependencies": {
        "@faststore/core": "^3.0.xx",
        "next": "^13.5.6",
        "react": "^18.2.0",
        "react-dom": "^18.2.0"
    },
    ```

    After replacing `@faststore/core` with `@faststore/cli`,  the `dependencies` property should look like this:

    ```diff package.json
    "dependencies": {
    +    "@faststore/cli": "^3.0.87",
        "next": "^13.5.6",
        "react": "^18.2.0",
        "react-dom": "^18.2.0"
    },
    ```

    >⚠️ Replace for a `@faststore/cli` version equals or greater than `3.0.87`. The `3.0.87` is when these package dependencies changes were applied.

3. Still on the `package.json` file, remove the `@faststore/cli` from the `devDependencies` property. After removal, it should look like this:

    ``` package.json
    "devDependencies": {
        "@cypress/code-coverage": "^3.12.1",
        "@faststore/lighthouse": "^3.0.68",
        "@lhci/cli": "^0.9.0",
        "@testing-library/cypress": "^10.0.1",
        "cypress": "12.17.4",
        "cypress-axe": "^1.5.0",
        "cypress-wait-until": "^2.0.1",
        "typescript": "^4.9.4"
    },
    ```

4. Open the terminal and run `yarn` to install the updated dependencies and update your `yarn.lock` file.

5. If no errors occur during or after running `yarn`, create a pull request with these changes to your remote repository to apply the updates to production.

> ⚠️ If you encounter any errors when updating these dependencies, please open a ticket with [VTEX Support](https://help.vtex.com/en/support).
