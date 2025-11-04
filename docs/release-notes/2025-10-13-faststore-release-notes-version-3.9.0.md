---
title: "FastStore Release Notes — Version 3.90.0" 
slug: "2025-10-13-faststore-release-notes-version-3.9.0" 
type: "fixed"
createdAt: "2025-10-13T11:00:00.000Z"
updatedAt: "2025-10-13T11:05:00.000Z"
excerpt: "Version 3.90.0 delivers improvements on analytics tracking, reliable Master Data authentication, faster UI responses, and improved B2B components."
tags:
    - FastStore
---

Starting with **version 3.90.0**, FastStore is adopting a **new release cadence**. From now on, every new **minor version** will include a **dedicated release note** highlighting key improvements, fixes, and notable changes.

Version 3.90.0 focuses on improving analytics tracking, fixing authentication issues for Master Data requests, enhancing UI responsiveness, and refining B2B components. Check out the highlights below.

## General

**Improved Analytics tracking in `SearchDropdown (`**PR: [\#3057](https://github.com/vtex/faststore/pull/3057)**`)`**  
The `SearchDropdown` component now ensures that analytics events for search suggestions are sent before navigation occurs, fixing a race condition. This results in more reliable tracking of autocomplete click events.

**Refactored ProductShelf component loading (**PR: [\#3059](https://github.com/vtex/faststore/pull/3059)**)**  
The `ProductShelf` component import was refactored from dynamic to static. This internal change resolves an intermittent loading error and does not impact existing project functionality.

## My Account B2B (experimental)

### Added

**FastStore CLI support for `/pvt` page prefix (PR: [\#3052](https://github.com/vtex/faststore/pull/3052))**  
The FastStore CLI now supports the `/pvt` prefix for custom pages. This allows developers to create private pages within the context of the experimental **My Account** for B2B under paths like `/pvt/account`. Documentation: [Enabling My Account](https://developers.vtex.com/docs/guides/faststore/my-account-overview)

**New My Account components and UI improvements (PR: [\#3040](https://github.com/vtex/faststore/pull/3040))**  
Introduced new `MyAccountTable` and `MyAccountHeader` components to standardize layouts and reduce code duplication in the **My Account** section. This update also includes several UI fixes for navigation, alignment, and spacing across the `OrdersList` and `OrderDetails` pages. Developers building or customizing **My Account** pages can now leverage these new components for a more consistent user experience.

### Improvements

**B2B: Organization Drawer displays `corporateName (`**PR: [\#3062](https://github.com/vtex/faststore/pull/3062)**`)`**  
In B2B stores, the Organization Drawer now displays the organization’s `corporateName`, ensuring consistency with the experimental **My Account B2B** menu. This change updates the `useOrganizations` hook in the FastStore SDK to fetch and return the `corporateName` alongside the organization name.

**B2B: contract name source updated (PR: [\#3051](https://github.com/vtex/faststore/pull/3051))**  
The B2B contract name is now sourced from the `corporateName` field in the user's session data (`session.person.corporateName`), which is retrieved from the Master Data CL entity. This change removes the `accountName` field from the `StoreSession` GraphQL type. 

>⚠️ Developers should update any custom components previously using `session.accountName` to use `session.person.corporateName`.

**Removed “Placed by” column from Orders Page (**PR: [\#3064](https://github.com/vtex/faststore/pull/3064)**)**  
The Placed by column and its corresponding filter have been removed from the Orders list page in the experimental My Account for B2B. As a result, the purchaser parameter is no longer available for filtering in the `useSearchOrders` hook and the `searchOrders` function.

### Fixes

**App Key/Token authentication for Master Data requests (**PR: [\#3055](https://github.com/vtex/faststore/pull/3055)**)**  
A new utility automatically adds the `X-VTEX-API-AppKey` and `X-VTEX-API-AppToken` headers to Master Data (MD) API requests. This ensures proper authentication when fetching data from entities that require app-level credentials, resolving previous `403 Forbidden` errors on pages like experimental **My Account for B2B**.

**Search Filter Badge visibility (**PR: [\#3061](https://github.com/vtex/faststore/pull/3061)**)**  
Fixed an issue where the Badge in the experimental My Account for B2B did not display when the count was `0`. The Badge now correctly appears in all cases, ensuring consistent UI behavior.

**Table component responsiveness (**PR: [\#3066](https://github.com/vtex/faststore/pull/3066)**)**  
Fixed an issue where the `Table` component from `@faststore/ui` would overflow and break the page layout on smaller viewports. The component now includes horizontal scrolling for wide tables (e.g., the experimental **My Account for B2B** orders page), ensuring a responsive and user-friendly experience across all screen sizes.  