---
title: "FastStore: New global Content Types"
slug: "2025-03-07-faststore-new-content-types"
type: added
excerpt: "FastStore introduces two new Content Types in Headless CMS, enabling better organization and scalability for headers and footers across all store pages."
createdAt: "2025-03-07T00:00:00.000Z"
updatedAt: ""
hidden: false
---

FastStore projects now include two new Content Types available in the Headless CMS: **Global Header Sections** or **Global Footer Sections**. These Content Types provide a more organized way to manage global headers and footers across the store.

| Global Header Sections with the banner **Everything you need to tidy up your home!** | Global Footer Sections with the alert **Enjoy the new arrivals!** |
| -------------------------------- | ------------------------------ |
|  ![header-content-type](https://vtexhelp.vtexassets.com/assets/docs/src/new-section___861ccac1997461c0e5a7fd06bd460cb0.png)  |    ![footer-content-type](https://vtexhelp.vtexassets.com/assets/docs/src/new-section-footer___568b53489a6345f82ce8089dab53f16a.png)                            |

Now headers and footers can be customized independently, improving performance by reducing the data load associated with global sections.

## What has changed?

These new Content Types are available for global sections, meaning they can be applied to all store pages:

- **Global Header Sections:** Defines the content for the global header, which appears at the top of every page.
- **Global Footer Sections:** Defines the content for the global footer, which appears at the bottom of every page.

The existing [global sections](https://docs.google.com/document/d/1im0qARU2cy8VBOhgNYUQKHSbAnqvcV_Osl0tr2ThIEc/edit?tab=t.0) still remain in place. However, with this update, Global Header Sections will now appear immediately before the Children section in the header area, and Global Footer Sections will appear immediately after the Children section in the footer area.

> ℹ The Children section is a specific feature that separates the header and footer sections. While it is visible and configurable in the CMS, it does not appear on the storefront. Its purpose is to organize and structure content within the CMS, ensuring headers and footers are clearly separated from other page content.

## Why did we make this change?

As stores grow, managing global content becomes more complex. The introduction of Global Header Sections and Footer Sections simplifies the process by making content management more organized and scalable.

## What needs to be done?

To start using the new Content Types, follow these steps:

1. Open the terminal and navigate to your FastStore project folder.
2. In the terminal, log into your account by running `vtex login {accountName}`.

    > ⚠ Change `{accountName}` for your account name, for example, `vtex login mystore`.

3. Updating the `@fastore/cli` package version by running `yarn add @faststore/cli@latest`.
4. Run `yarn cms-sync` to update your project with the new Content Types.
5. Go to your store VTEX Admin, and access **Storefront > Headless CMS**.
6. Click `Create document` and select either Content Types, **Global Header Sections** or **Global Footer Sections**.

    ![headless-cms-ui](https://vtexhelp.vtexassets.com/assets/docs/src/new-content-types___f6dfa0fbca91bc23f88a6f022a686596.gif)

7. Add the desired sections (e.g., Banner Text) to the new Content Type.
8. Click `Save`.
9. Click `Preview` to see and review the new section. In the example below, the new section is the **Everything you need to tidy up your home!** banner.

    ![new-banner-header](https://vtexhelp.vtexassets.com/assets/docs/src/new-section___861ccac1997461c0e5a7fd06bd460cb0.png)

10. To publish your changes, return to the Content Type page in the Headless CMS and click `Publish`.
