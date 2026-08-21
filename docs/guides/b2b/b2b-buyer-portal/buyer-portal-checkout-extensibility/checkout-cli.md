---
title: "Checkout CLI"
slug: "checkout-cli"
hidden: false
createdAt: "2026-06-16T00:00:00.000Z"
updatedAt: "2026-06-16T00:00:00.000Z"
excerpt: "Reference for the Checkout CLI and its available commands for developing and building Checkout extensions."
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

Although FastStore provides a main CLI as the central point for interacting with all modules, Checkout has its own CLI, which is even used internally by the FastStore CLI for all interactions related to the Checkout module.

The Checkout CLI is not a replacement for the FastStore CLI, and ideally, you should always use the FastStore CLI for commands in your storefront monorepo, such as `build`, `create`, `dev`, etc. However, the Checkout CLI may contain specific functionalities for Checkout, such as flags in certain commands that facilitate the development environment.

> ℹ️ We recommend always using the FastStore CLI and only using the Checkout CLI when you need to access a specific feature exclusive to it.

## Usage

To use the Checkout CLI directly, you can invoke the binary available in your monorepo using your package manager's runner. If you're using `yarn` or `npx`, it might look like this:

```bash
yarn checkout --help
# or
npx checkout --help
```

## Available commands

### `create`

Initializes a new Checkout extensions project.

**Args:**

- `PATH`: The path where the project will be initialized.

**Flags:**

- None

### `dev`

Run Checkout extensions in development mode.

**Args:**

- `ACCOUNT`: The account name of the store.
- `PATH`: The path where the extensions are located.
- `PORT`: The port where the Checkout will be served.

**Flags:**

- `--show-placeholders`: Show placeholders for extension points.

### `build`

Build Checkout extensions for production deployment.

**Args:**

- `ACCOUNT`: The account name of the store.
- `PATH`: The path where the extensions are located.

**Flags:**

- None

### `reset`

Resets the Checkout environment, preserving your extensions project setup while restoring internal configurations. Use this command to resolve issues without affecting your current work.

**Args:**

- None

**Flags:**

- None
