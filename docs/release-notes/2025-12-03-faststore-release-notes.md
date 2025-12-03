---
title: "FastStore Release Notes — Version 3.93.0" 
slug: "2025-12-03-faststore-release-notes"
type: "added"
createdAt: "2025-12-03T11:00:00.000Z"
updatedAt: "2025-12-03T11:05:00.000Z"
excerpt: "Version 3.93.0 introduces support for right-to-left (RTL) layouts and delivers a series of UI and stability fixes."
tags:
    - FastStore
---

Version 3.93.0 introduces support for right-to-left (RTL) layouts and delivers a series of UI and stability fixes.

## General

**Added Right-to-Left (RTL) Layout Support** (PR:  [\#3097](https://github.com/vtex/faststore/pull/3097))

Introduced a new direction property to the `UIProvider` context, enabling support for Right-to-Left (RTL) layouts. Components such as `Dropdown`, `SearchInput`, and `Button` will now automatically adjust their styles based on the configured direction (RTL or LTR).

### Fixes

**Footer component now renders without a logo** (PR:  [\#3094](https://github.com/vtex/faststore/pull/3094))

The Footer component will no longer fail to render if a logo image is not provided. Previously, removing the logo would cause the entire component to disappear from the page. Now, the footer will be displayed correctly without the logo image.

**Build process for different modules** (PR:  [\#3119](https://github.com/vtex/faststore/pull/3119))

Internal module export paths were refactored to resolve issues in our build pipeline. This change has no external impact on developers.

**Prevent product price flickering on PDP** (PR:  [\#3112](https://github.com/vtex/faststore/pull/3112))

Introduced a loading skeleton that now displays on the Product Details Page (PDP) while the product's price is being validated. This change improves the user experience by preventing the price from flickering during load times. The `<Price>` component now accepts a loading component as a child to manage this state.
