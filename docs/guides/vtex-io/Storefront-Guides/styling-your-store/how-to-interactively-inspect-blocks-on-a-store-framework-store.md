---
title: "Interactively inspecting storefront blocks"
slug: "how-to-interactively-inspect-blocks-on-a-store-framework-store"
hidden: false
createdAt: "2020-10-08T01:49:37.564Z"
updatedAt: "2020-10-08T01:50:59.005Z"
---

When customizing your Store Theme, it is essential to understand the structure and properties of the individual blocks that make up your storefront. To facilitate this process, VTEX provides an interactive inspection tool that allows you to analyze and gain insights into each block. You can use this tool to identify the VTEX IO app responsible for exporting a particular block, examine its name, and explore its associated classes.

## Before you begin

Before you begin inspecting the blocks on your storefront, ensure that you have set up a development workspace. If you haven't created one yet, follow the guide on [creating a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) to get started.

## Instructions

1. Open your web browser and enter the following URL: `https://{workspace}--{account}.myvtex.com/{path}/?__inspect`. Replace `{workspace}` with the name of your development workspace and `{account}` with your VTEX account name. You can also modify or remove `{path}` to access the specific store path you want to inspect. This URL will direct you to an interactive inspection tool designed to help you analyze and understand the blocks within your Store Theme.
2. To inspect a particular block, hover your mouse over it. The inspection tool will provide you with pertinent information about the block, including the VTEX IO app responsible for exporting it, the block's name, and its associated classes.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-interactively-inspect-blocks-on-a-store-framework-store-0.png)

You can use this tool to better understand the structure of your Store Theme and facilitate your [storefront customization.](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization)
