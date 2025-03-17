---
title: "I can’t install the Headless CMS plugins in my account"
excerpt: "Users may encounter errors related to symbolic links and node version incompatibility."
slug: "error-installing-headless-cms-plugins-on-windows"
updatedAt: "2025-02-12T14:56:25.977Z"
tags:
    - headless-cms
    - faststore
---

FastStore users may encounter the following errors after [installing the Headless CMS plugin](https://developers.vtex.com/docs/guides/faststore/headless-cms-1-configuring-the-vtex-account#step-1-setting-up-the-command-line-environment).

| Error message                                                                 | Possible cause                                                                 | Solution                                                                                       |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `Error: EPERM: operation not permitted, symlink`                              | Your device isn’t enabled for development.                                     | [Enable Developer Mode in your machine](https://developers.vtex.com/docs/troubleshooting/error-installing-headless-cms-plugins-on-windows#enable-developer-mode-in-your-machine) |
| `error @oclif/core@1.26.2: The engine "node" is incompatible with this module. Expected version ">=14.0.0". Got "12.12.0"` | The VTEX IO CLI’s node version isn’t updated. Expected version was `>=14.0.0`, but the current version is `12.12.0`. | [Update VTEX IO CLI](https://developers.vtex.com/docs/troubleshooting/error-installing-headless-cms-plugins-on-windows#update-vtex-io-cli) |

## Solutions

To solve these issues, follow the instructions below:

- [Enable Developer Mode on your machine](#enable-developer-mode-on-your-machine)
- [Update VTEX IO CLI](#update-vtex-io-cli)

### Enable Developer Mode on your machine

While running the `vtex plugins install cms`, Windows users can get the following error:

```sh
vtex plugins install cms
warning "@vtex/cli-plugin-cms > @vtex/api > apollo-server-core > apollo-graphql@0.9.5" has incorrect peer dependency "graphql@^14.2.1 || ^15.0.0".
Installing plugin @vtex/cli-plugin-cms... failed
    Error: EPERM: operation not permitted, symlink
    'C:\Users\LukeSkywalker\AppData\Roaming\npm\node_modules\vtex' ->
    'C:\Users\LukeSkywalker\AppData\Local\vtex\node_modules\vtex'
    Code: EPERM
```

FastStore projects rely on creating symbolic links (symlinks). To solve this error, you must enable [Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#accessing-settings-for-developers) on your machine. Developer Mode grants the necessary permissions and privileges to use symlinks, which reduces the probability of encountering errors during development.

> ⚠️ Running the FastStore project as an administrator isn't recommended.

Learn how to enable Developer Mode in Microsoft's official guide [Enable your device for development](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#accessing-settings-for-developers).

After enabling Developer Mode, launch Windows Terminal and run `vtex cms`. This will allow the system to create the necessary symlinks for running commands from the Headless CMS plugin.

### Update VTEX IO CLI

If you run the `vtex plugins install cms` command and get the error below, you need to update the VTEX IO CLI version you're using.

```sh
vtex plugins install cms
error @oclif/core@1.26.2: The engine "node" is incompatible with this module. Expected version ">=14.0.0". Got "12.12.0"
error Found incompatible module.
Installing plugin @vtex/cli-plugin-cms... failed
    Error: yarn add @vtex/cli-plugin-cms@latest --non-interactive --mutex=file:C:\Users\barbara.celi\AppData\Local\vtex\yarn.lock --preferred-cach
```

Even if you update the `node` version on your machine, you must also keep VTEX IO CLI updated to avoid errors.

To update VTEX IO CLI, open Windows Terminal and follow these instructions:

1. Run the `vtex autoupdate` command in Windows Terminal.
2. Run the `vtex -v` command to check if the VTEX IO CLI and `node` versions are updated.
3. Run the `vtex plugins install cms` command to install the Headless CMS plugins.
4. Check if the installation of Headless CMS plugins was successful by running `vtex cms`. You should see the following:

```sh
$ vtex cms
Syncs CMS schemas with the current workspace in use.

USAGE
     $ vtex cms COMMAND
COMMANDS
     cms sync Syncs CMS schemas with the current workspace in use.
```
