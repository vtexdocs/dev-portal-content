---
title: "I can’t install the Headless CMS plugins in my account"
excerpt: "Windows users can encounter the 'EPERM: operation not permitted' error during the installation of the Headless CMS plugin."
slug: "error-installing-headless-cms-plugins-on-windows'"
tags:
    - headless-cms
    - faststore
---

If you are a Windows user, you may find the following error after [installing the Headless CMS plugin](https://developers.vtex.com/docs/guides/faststore/headless-cms-1-configuring-the-vtex-account#step-1-setting-up-the-command-line-environment):

```sh
vtex plugins install cms
warning "@vtex/cli-plugin-cms > @vtex/api > apollo-server-core > apollo-graphql@0.9.5" has incorrect peer dependency "graphql@^14.2.1 || ^15.0.0".
Installing plugin @vtex/cli-plugin-cms... failed
    Error: EPERM: operation not permitted, symlink
    'C:\Users\LukeSkywalker\AppData\Roaming\npm\node_modules\vtex' ->
    'C:\Users\LukeSkywalker\AppData\Local\vtex\node_modules\vtex'
    Code: EPERM
```

To solve this issue, enable the [Developer Mode](https://docs.microsoft.com/en-us/windows/uwp/get-started/enable-your-device-for-development#accessing-settings-for-developers) in your machine.
Since FastStore projects rely on creating symbolic links (symlinks), this mode grants the necessary permissions and privileges, reducing the chance of errors during development.

> ⚠️ Running the FastStore project as an Administrator is not recommended.

1. To enable Developer Mode, refer to Microsoft's official guide on [Enabling your device for development](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#accessing-settings-for-developers).

2. After enabling the mode, launch the Windows Terminal and run `vtex cms`. This will allow the system to create the symlinks necessary for running commands from the Headless CMS plugin.
