---
title: "I can’t install the Headless CMS plugins in my account"
excerpt: "Windows users may encounter the 'EPERM: operation not permitted' error during the installation of the Headless CMS plugin."
slug: "error-installing-headless-cms-plugins-on-windows"
updatedAt: "2025-02-12T14:56:25.977Z"
tags:
    - headless-cms
    - faststore
---

If you are a Windows user, you may encounter the following errors after [installing the Headless CMS plugin](https://developers.vtex.com/docs/guides/faststore/headless-cms-1-configuring-the-vtex-account#step-1-setting-up-the-command-line-environment).

<table>
<tr>
<th>Error message</th>
<th>Possible cause</th>
<th>Solution</th>
</tr>
<tr>
<td>
`Error: EPERM: operation not permitted, symlink`
</td>
<td>
Your device isn’t enabled for development.
</td>
<td>
<a href="https://developers.vtex.com/docs/troubleshooting/error-installing-headless-cms-plugins-on-windows#enable-developer-mode-in-your-machine">Enable Developer Mode in your machine</a>
</td>
</tr>
<tr>
<td>
`error @oclif/core@1.26.2: The engine "node" is incompatible
with this module. Expected version ">=14.0.0". Got "12.12.0"`
</td>
<td>
The VTEX IO CLI’s node version isn’t updated. See that the expected version was `>=14.0.0`, but, in this case, the node version in the VTEX IO CLI was `12.12.0`.
</td>
<td>
<a href="https://developers.vtex.com/docs/troubleshooting/error-installing-headless-cms-plugins-on-windows#update-vtex-io-cli">Update VTEX IO CLI</a>
</td>
</tr>
</table>

## Solutions

To solve these issues, see the following instructions:

- [Enable Developer Mode on your machine](#enable-developer-mode-on-your-machine)
- [Update VTEX IO CLI](#update-vtex-io-cli)

### Enable Developer Mode on your machine

If you run the `vtex plugins install cms` and receive the error below, you must enable the Developer Mode on your machine.

```sh
vtex plugins install cms
warning "@vtex/cli-plugin-cms > @vtex/api > apollo-server-core > apollo-graphql@0.9.5" has incorrect peer dependency "graphql@^14.2.1 || ^15.0.0".
Installing plugin @vtex/cli-plugin-cms... failed
    Error: EPERM: operation not permitted, symlink
    'C:\Users\LukeSkywalker\AppData\Roaming\npm\node_modules\vtex' ->
    'C:\Users\LukeSkywalker\AppData\Local\vtex\node_modules\vtex'
    Code: EPERM
```

FastStore projects rely on creating symbolic links (symlinks), and the [Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#accessing-settings-for-developers) grants the necessary permissions and privileges to use them, which reduces the probability of encountering errors during development.

> ⚠️ Running the FastStore project as an Administrator isn’t recommended.

Learn how to enable Developer Mode in the Microsoft's official guide [Enable your device for development](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#accessing-settings-for-developers).

After enabling Developer Mode, launch Windows Terminal and run `vtex cms`. This will allow the system to create the necessary symlinks for running commands from the Headless CMS plugin.

### Update VTEX IO CLI

If you run the `vtex plugins install cms` command and receive the error below, it means you need to update the VTEX IO CLI version you're working.

```sh
vtex plugins install cms
error @oclif/core@1.26.2: The engine "node" is incompatible with this module. Expected version ">=14.0.0". Got "12.12.0"
error Found incompatible module.
Installing plugin @vtex/cli-plugin-cms... failed
    Error: yarn add @vtex/cli-plugin-cms@latest --non-interactive --mutex=file:C:\Users\barbara.celi\AppData\Local\vtex\yarn.lock --preferred-cach
```

Even if you update the `node` version on your machine, you must also keep VTEX IO CLI updated to avoid errors.

To update VTEX IO CLI, open the Windows Terminal and follow these instructions:

1. Run the `vtex autoupdate` command in the Windows Terminal.
2. Run the `vtex -v` command to verify if the VTEX IO CLI and `node` versions are updated.
3. Run the `vtex plugins install cms` command to install the Headless CMS plugins.
