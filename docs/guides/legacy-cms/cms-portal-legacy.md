---
title: "CMS Portal (Legacy)"
slug: "cms-portal-legacy"
hidden: false
createdAt: "2026-07-09T18:31:00.000Z"
excerpt: "VTEX's first storefront technology for building ecommerce websites with HTML, CSS, and JavaScript."
---

CMS Portal (Legacy) is VTEX's original storefront technology for building ecommerce websites using HTML, CSS, and JavaScript. Code management is done exclusively through the VTEX Admin, using the [Layout](https://help.vtex.com/docs/tracks/legacy-cms-portal) feature to create and manage templates, folders, and files.

> ⚠️ CMS Portal (Legacy) is no longer available to newly created VTEX stores. If your store currently uses this technology, we strongly recommend [migrating to Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-storefront-from-legacy-to-io).

CMS Portal (Legacy) relies on the following characteristics:

| Aspect | Description |
| --- | --- |
| Admin-based management | Code management is done exclusively through the VTEX Admin, without the need for local development tools or version control systems. |
| Template controls | Pre-built controls simplify the implementation of common storefront features like product displays, navigation menus, and search functionality. |
| Direct deployment | Content updates are made directly through the CMS without separate development or staging environments. |
| Layout customization | Customizations are managed by creating, organizing, and editing folders, files, and components within the Layout feature. |

## Technologies

To work with CMS Portal (Legacy), you should be familiar with the following technologies:

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Quickstart

For stores using CMS Portal (Legacy), the storefront is managed entirely through the VTEX Admin. Follow these steps to get started:

### 1. Access the Layout feature

1. In the VTEX Admin, go to **Storefront > Layout**.
2. The Layout section displays the folder structure containing your store's templates, shelves, and other components.

### 2. Understand the template structure

Templates are files that contain the HTML, CSS, and JavaScript code for your website pages. The Layout feature provides standard [templates](https://help.vtex.com/docs/tutorials/what-are-templates) that you can customize for different page types, such as:

- Home page
- Product page
- Category page
- Department page
- Search results page

### 3. Work with template controls

Template controls are pre-built components that add functionality to your storefront. They handle common features like product information, shopping cart, navigation menus, and search functionality. For a comprehensive list of available controls, refer to the [List of template controls](https://developers.vtex.com/docs/guides/list-of-controls-for-templates) guide.

### 4. Configure shelves

Shelves display collections of products on your storefront. You can configure them using specific controls and variables. Learn more about shelf configuration in the [Shelf template controls](https://developers.vtex.com/docs/guides/shelf-template-controls) guide.

## Support and limitations

CMS Portal (Legacy) provides access to VTEX core commerce services and native template controls. However, as a legacy technology, it has some limitations:

- **No CLI support**: Unlike [FastStore](https://developers.vtex.com/docs/guides/faststore) and [Store Framework](https://developers.vtex.com/docs/guides/store-framework), there is no command-line interface available.
- **No development environments**: Changes are made directly in production without separate development or staging workspaces.
- **Limited modern features**: Some newer VTEX features aren't available, including [Intelligent Search](https://help.vtex.com/docs/tracks/overview-intelligent-search) integration and VTEX IO frontend apps.
- **Performance challenges**: Outdated technologies make it more difficult to maintain optimal performance, especially with extensive customizations.

For detailed feature availability, refer to the [Getting started with storefront solutions](https://developers.vtex.com/docs/guides/getting-started-with-storefront-solutions) comparison guide.

## Next steps

Explore the available resources to help you work with CMS Portal (Legacy) or migrate to a modern storefront solution:

<Flex>

<WhatsNextCard
title="Migrating to Store Framework"
description="Learn how to migrate your storefront from CMS Portal (Legacy) to Store Framework for improved performance and features."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-storefront-from-legacy-to-io"
linkTitle="See more"
/>

<WhatsNextCard
title="List of template controls"
description="Discover the complete list of controls available for creating and customizing your store templates."
linkTo="https://developers.vtex.com/docs/guides/list-of-controls-for-templates"
linkTitle="See more"
/>

<WhatsNextCard
title="Shelf template controls"
description="Learn about the controls and variables for creating and configuring product shelves."
linkTo="https://developers.vtex.com/docs/guides/shelf-template-controls"
linkTitle="See more"
/>

<WhatsNextCard
title="Creating gift lists"
description="Understand how to implement gift list functionality in your store."
linkTo="https://developers.vtex.com/docs/guides/creating-gift-lists"
linkTitle="See more"
/>

</Flex>
