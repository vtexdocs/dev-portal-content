---
slug: "styles-builder-1-x-technical-support-ends-on-february-02-2022"
title: "Styles builder 1. x: technical support ends on February 02, 2022"
createdAt: 2021-11-26T13:57:37.123Z
hidden: false
type: "deprecated"
---

<span class="badge" id="vtex-io">VTEX IO</span>

[block:html]
{
  "html": "<br>"
}
[/block]
We **strongly recommend** that accounts using the deprecated Styles Builder 1. x **migrate to the major 2. x.** before February 02, 2022. After this date, **we will no longer offer support for Styles Builder 1. x.**


## What has changed?
[Styles Builder 1.x has been deprecated since December of 2019](https://vtex.io/docs/releases/2019-week-43-44/css-selectors-deprecation/) and now VTEX is ceasing its support in favor of its most recent version.

The Styles Builder’s major 2. x is already available, and It offers better store stability when working with [CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization), avoiding potential breakdowns on store layouts.

## What needs to be done?
To successfully migrate from Styles Builder 1.x to Styles Builder 2.x, you must update the version of the `styles` builder in the `manifest.json` file of your store theme app, as the example below:

```
builders{
...
"styles": "2.x"
}
```
In the following, check the [best practices of CSS handles](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization#best-practices) to review and update every CSS customization for your store elements.