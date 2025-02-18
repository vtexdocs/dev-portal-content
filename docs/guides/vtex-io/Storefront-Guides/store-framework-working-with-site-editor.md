---
title: "Working with Site Editor"
slug: "store-framework-working-with-site-editor"
hidden: false
createdAt: "2024-09-06T14:53:36.032Z"
updatedAt: ""
excerpt: "Discover how Site Editor simplifies the customization of your Store Framework storefront."
---

[Site Editor](https://help.vtex.com/tutorial/site-editor-overview) works as a Content Management System (CMS) designed for stores developed with [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework), reflecting the blocks defined in the [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) of the VTEX account.

Based on the source code, the Site Editor displays an editable version of the website's storefront, enabling non-technical users to manage content as desired and modify components and their behavior through a friendly interface.

In your VTEX Admin, go to **Storefront > Site Editor** to see the main available tools.

![site-editor](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-site-editor-0.png)

Changes made in Site Editor are immediately reflected in the store, and every storefront block can have its properties changed there. For example, you can change the content of a rich text block and shelf properties, such as which collection is being shown, among other changes.

> ℹ️ Developers are responsible for creating components, defining the structure of the [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme), and ensuring seamless integration with Site Editor. This integration allows non-technical users to manage and update components easily, empowering store administrators to make changes to their storefronts without modifying the codebase.

Learn more in [Site Editor - Overview](https://help.vtex.com/tutorial/site-editor-overview--299Dbeb9mFczUTyNQ9xPe1).

## Before you begin

<Steps>

### Develop your Store Theme

Make sure your store has a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) developed following the [Storefront](https://developers.vtex.com/docs/guides/getting-started-3) guide.

### Check the builders

Check if the builders are properly installed in your Store Theme. To use builders, you must have at least the `vtex.builder-hub@0.293.4` version installed in your account. Also, you need to specify them in the app’s `manifest.json` file. Learn more at [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders).

You must have at least the following builders configured:

- [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder): Enables the development of Store Framework storefronts.
- [react builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder): Used to develop apps with [React](https://react.dev/) when your project requires customized frontend solutions.

### Create the store pages

Develop your store pages following the [Building pages](https://developers.vtex.com/docs/guides/store-framework-building-pages) guides.

### Configure your components

Set up your components following the [Using components](https://developers.vtex.com/docs/guides/store-framework-using-components) guides.

</Steps>

## Essential concepts

It is important to understand the concept of a Content Management System (CMS) to learn how to work with Site Editor.

A Content Management System (CMS) is a tool for creating, managing, and modifying website content. VTEX offers different CMS options based on the storefront technology used to develop your site. Store Framework uses Site Editor, Legacy CMS Portal uses [Layout](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj), and FastStore leverages [VTEX Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview).

On VTEX, these tools allow you to manage the pages that make up your store website with the autonomy to create, organize, edit, and define the entire structure of folders, files, and components to create the storefront you want.

To learn more, see [CMS - Overview](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/6OCY6S9tqBXPD5mgpbBInC).

## Guides in this section

In this section, you will find the following guides.

<Flex>

<WhatsNextCard
title="Integrating a frontend app with Site Editor"
description="Discover how to integrate a frontend app with Site Editor."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-integrating-frontend-app-with-site-editor"
linkTitle="See more"
/>

<WhatsNextCard
title="Making a custom component available in Site Editor"
description="Allow component customization directly in Site Editor."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-making-a-custom-component-available-in-site-editor"
linkTitle="See more"
/>

<WhatsNextCard
title="Site Editor schema examples"
description="Explore practical schema examples for configuring custom components in Site Editor."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-site-editor-schema-examples"
linkTitle="See more"
/>

</Flex>
