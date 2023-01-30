---
title: "Managing plugins"
slug: "vtex-io-documentation-vtex-io-cli-plugins"
hidden: false
createdAt: "2021-10-20T14:59:19.813Z"
updatedAt: "2022-12-13T20:17:44.761Z"
---

VTEX IO CLI 3.x has a plug-in architecture that makes it more flexible and extensible to inject new commands and functionalities. This way, you can go beyond VTEX IO's CLI default commands and add specific plugins to achieve a more comprehensive experience.

Check the [Command Reference](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-command-reference#plugins) for a detailed description of all plugins developed by VTEX.

> ℹ️ The following plugins are native to VTEX IO'S CLI. Therefore, you do not need to install them:  `abtest`, `autoupdate`, `deploy`, `deps`, `edition`, `plugins`, `whoami`, `workspace`.

## Checking plugin commands

Check all commands related to plugins by running the following command.

```shell
vtex plugins
```

![vtex-plugins-source](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-plugins-0.png)

## Listing all VTEX plugins

List all plugins available by VTEX by running the following command.

```sh
vtex plugins source
```

![vtex-plugins-source](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-plugins-1.png)

> ℹ️ If you already have downloaded a plugin, it will be highlighted in green.

## Installing a plugin

Install a new plugin by running the following command.

```sh
vtex plugins install {pluginName}
```

Replace the value between curly brackets with the name of the plugin you want to install.

- For `vtex` plugins, use just the plugin name. For example, `vtex plugins install infra`.

  > ℹ️ Tip: you can run `vtex plugins source` to check the available VTEX plugins.

- For third parties plugins, use the following format: `@{org-name}/{plugin-name}`.

![install-plugin](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-plugins-2.png)

## Listing installed plugins

List all plugins installed in your machine by running the following command.

```sh
vtex plugins list
```

![install-plugin](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-plugins-3.png)

## Updating installed plugins

Update all plugins installed in your machine by running the following command.

```sh
vtex plugins update
```

![update-plugins](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-plugins-4.png)

## Uninstalling a plugin

Delete a plugin from your machine by running the following command.

```sh
vtex plugins uninstall {pluginName}
```

> ⚠️ Replace the value between curly brackets with the name of the plugin you want to uninstall. You can run `vtex plugins list` to check which plugins are installed in your machine.

![uninstall-plugins](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-plugins-5.png)
