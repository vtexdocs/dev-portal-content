---
title: CSS Selectors deprecation
slug: css-selectors-deprecation
excerpt: 'Starting December 18, 2019, **CSS customization will be done exclusively via CSS handles**. Selectors based on HTML structure will be blocked for new stores.'
createdAt: "2019-11-11T00:00:00.000Z"
updatedAt: "2026-05-07T15:41:30.641Z"
hidden: true
type: 'info'
---

Starting December 18, 2019, **CSS customization will be done exclusively via CSS handles** (for example, `.foo`). Selectors based on HTML structure (for example, `div > div > span[foo="bar"]`) will be blocked for new stores.

## What has changed

Previously, many VTEX IO store components didn't have their own **CSS handles**.

> Handles allow you to select and customize a specific store component using CSS classes.

Without handles, a component's CSS customization had to be based on the HTML structure.

**Since most components now have their own CSS handles, some CSS selectors will be discontinued.**

Below, you'll find the full list of CSS selectors that will **remain available** for store customization:

- Class selectors (for example, `.foo`)
- Pseudo-selectors `:hover`, `:visited`, `:active`, `:disabled`, `:focus`, `:local`, `:not`, `:target`, `:first-child`, and `:last-child`
- All pseudo-elements, such as `::before`, `::after`, and `::placeholder`
- `:nth-child(even)` and `:nth-child(odd)`
- Space combinator (for example, `.foo .bar`)
- `[data-...]`
- `:global()` for selecting global CSS classes (for example, `:global(vtex-{AppName}-{AppVersion}-{ComponentName})` for elements from different apps, `:global(.tachyons-class)` for Tachyons utilities, or any other global CSS class)

We're deprecating all selectors and combinators not mentioned on the list above, such as:

- Type/tag selectors (for example, `div`, `span`)
- Combinators, such as `>`, `+`, and `~`
- `:nth-child` with numbers
- Attribute selectors excepting `[data-...]` (e.g. `[class~="mb8 b--red"]`)

This CSS selector allowlist is flexible because the deprecation is intended to encourage robust CSS customization without risking store layout issues. If the deprecation of CSS selectors not on this list causes any unintended harm to your store, let us know immediately by opening a ticket with [VTEX Support](https://supporticket.vtex.com/support).

## Why this action is being taken

CSS customization that depends on the HTML structure can be fragile and detrimental to the **store's stability**.

This is because any change to the HTML, such as changing an attribute, changing the order of an element, or wrapping an element in a new tag, can prevent a CSS selector from targeting the correct elements, thereby breaking the desired customization.

CSS handles, on the other hand, are guaranteed to remain functional throughout the major version, making **customization much more robust**. This deprecation is intended to promote the default use of CSS handles, helping to avoid potential disruptions in store layouts.

## Side effects

### Published apps

If your store theme was previously published, meaning that your store is **already live**, you will **still be able to [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) and [publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) new versions of your theme, even when using CSS selectors not listed above**.

This prevents mature stores that have already been customized without CSS handles from suddenly being unable to update their theme due to this deprecation.

However, note that the store **will remain susceptible to the above-mentioned issues arising from customization based on the HTML structure**. It's **strongly recommended** that the CSS be updated to use only CSS handles.

### Apps not published yet

If your store project was never published, **any CSS customization performed using CSS selectors not on the above-mentioned allowlist (such as **`:nth-child`**,** `foo > bar` **and** `[alt="bar"]`**) will be blocked by VTEX IO CLI** during the linking from December 18, 2019 onward.

Although each project scenario can be evaluated individually, it's expected that stores that haven't gone live yet will adapt more quickly and effectively to the correct customization format.

## What you need to do

Regardless of whether your app is published, **it's essential to review every CSS customization for store elements** to ensure that all deprecated selectors are replaced with CSS handles.

Learn more in the guide [Using CSS handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).