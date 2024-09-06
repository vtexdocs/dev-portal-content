---
title: "Site Editor"
slug: "site-editor"
hidden: false
createdAt: "2024-08-15T12:58:16.587Z"
updatedAt: ""
excerpt: "Discover how Site Editor simplifies the customization of your Store Framework storefront."
---

Site Editor works as a Content Management System (CMS) designed for stores developed with [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework), reflecting the blocks defined in the [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) of the VTEX account.

Based on the source code, the Site Editor section on the VTEX Admin displays an editable version of the website's storefront, enabling non-technical users to manage content as desired and modifying components and their behavior through a friendly interface.

In your VTEX Admin, go to **Storefront > Site Editor** to see the main available tools.

![site-editor](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-site-editor-0.png)

Changes made in Site Editor are immediately reflected in the store, and every storefront block can have its properties changed there. For example, you can change the content of a rich text block and shelf properties, such as which collection is being shown, among other changes.

In this context, developers are responsible for building custom components tailored to specific needs, defining the structure and behavior of these components within the Store Theme, and ensuring seamless integration with Site Editor. This integration allows non-technical users to manage and update components easily, empowering store administrators to make changes to their storefronts without modifying the codebase.

Learn more in [Site Editor - Overview](https://help.vtex.com/tutorial/site-editor-overview--299Dbeb9mFczUTyNQ9xPe1).

## Before you begin

- Make sure your store has a Store Theme developed with VTEX IO and Store Framework, following the Storefront guide.
- Check if the builders are properly installed in your Store Theme.
- Build your store pages, following the [Building pages](https://developers.vtex.com/docs/guides/building-pages) guides.
- Configure your components, following the [Using components](https://developers.vtex.com/docs/guides/using-components) guides.

## Essential concepts

It is important to understand the concept of a Content Management System (CMS) to learn how to work with Site Editor.

A Content Management System (CMS) is a tool for creating, managing, and modifying website content. VTEX offers different CMS options based on the storefront technology used to develop your site. Store Framework uses Site Editor, Legacy CMS Portal uses [Layout](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj), and FastStore leverages [VTEX Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview).

On VTEX, these tools allow you to manage the pages that make up your store website, with the autonomy to create, organize, edit, and define the entire structure of folders, files, and components to create the storefront you want.

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
