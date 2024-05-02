---
title: "Uninstalling VTEX IO's CLI"
slug: "vtex-io-documentation-vtex-io-cli-uninstall"
excerpt: "Learn how to uninstall VTEX IO's CLI from your computer."
hidden: false
createdAt: "2021-10-20T14:59:19.807Z"
updatedAt: "2022-12-13T20:17:44.708Z"
---

To uninstall VTEX IO's CLI from your system, run the command relative to your operating system or package manager.

>⚠️ This will also remove all [plugins](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) from your system.

## MacOS

```sh
brew uninstall vtex
```

## Linux

```sh
curl -L https://vtex.io/vtexcli/uninstall | sh
```

> ℹ️ The standalone is a tarball with a binary that contains its node.js binary.

## Windows

Follow the [Windows uninstall tutorial](https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-10-4b55f974-2cc6-2d2b-d092-5905080eaf98) to remove the VTEX IO's CLI from your programs list.

## Uninstalling VTEX IO's CLI via NPM

If you have [installed VTEX IO's CLI via NPM](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install), to uninstall it on your machine, run the following command:

```sh
yarn global remove vtex
```
