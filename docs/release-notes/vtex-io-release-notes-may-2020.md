---
slug: "vtex-io-release-notes-may-2020"
title: "VTEX IO Release Notes - May 2020"
createdAt: 2020-06-18T18:12:00.000Z
hidden: false
type: "info"
---
![App Development](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-may-2020-0.png)

Welcome to the May 2020 VTEX IO Release Notes, team!

The VTEX IO Release Notes is marking it's **first anniversary** online and we've decided to celebrate this first year by doing what we do best: introducing our users to eagerly awaited configs.

Some of the key highlights are:

- ➕ Layout conditioned by product specifications;
- ❌ Product Summary Price and Product Price blocks deprecation;
- 🐛 Links working in Brand component.

Shall we then start reading this Release Notes gem for May?

## Improvements ➕

- **Product prices with tax** - Blocks exported by the [Product Price](https://developers.vtex.com/docs/guides/vtex-product-price) app are now able to render their text messages and price variables with tax values considered.

- **Infocard's new** `callToActionLinkTarget` **prop** - The `callToActionLinkTarget` prop from the [Infocard](https://developers.vtex.com/docs/guides/vtex-store-components-infocard/) block is now available for the Edition in the admin's Site Editor.

- **CSS Handles** - New CSS Handles always herald good news. Let's rejoice: `firstVisible` and `lastVisible` have arrived to the [Slider Layout app](https://developers.vtex.com/docs/guides/vtex-slider-layout), allowing you to customize the first and the last visible item on a slide. In addition, the [Rich Text](https://developers.vtex.com/docs/guides/vtex-rich-text/) and the [Search Results](https://developers.vtex.com/docs/guides/vtex-search-result/) also gained new Handles: namely the `wrapper` and the `accordionFilterOpen` for mobile devices.

- **Product Specifications block and Search Results filters customization** - It is now possible to independently customize each of the UI product specifications and the search filters. All this thanks to adding modifiers and new attributes linked to HTML elements. For more info, access the [Search Results app](https://developers.vtex.com/docs/guides/vtex-search-result/) and [Product Specifications block](https://developers.vtex.com/docs/guides/vtex-store-components-productspecifications/) documentation, in addition to going through the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

- **Add to Cart button message** - Define which message will be displayed on the [Add to Cart Button](https://developers.vtex.com/docs/guides/vtex-add-to-cart-button) thanks to the block's new `text` prop. In addition, you can define a text message that will be rendered when the product is not available for purchase - thanks to another new prop called `unavailableText`.

- **Newsletter in Site Editor** - The [Newsletter](https://developers.vtex.com/docs/guides/vtex-store-components-newsletter/) is finally in Site Editor! The component can now be edited using your account's admin.

- **Layout conditioned by product specifications** - The [Condition Layout](https://developers.vtex.com/docs/guides/vtex-condition-layout) now works with product specifications, thanks to the new value `specificationProperties` for the `subject` prop. That's right: you can now define which product specifications should trigger the rendering of predefined content! Cheers to that!

- **CSS subfolders** - The folder where your theme's app CSS files are stored (called `css` and allocated in the main `styles` folder) now supports subfolder organization, which means that you can organize your CSS files as you wish from now on!

- **Empty Minicart state** - This one should be a good surprise to users: The Minicart empty state was improved. What was merely a rich text gave way to more user friendly UI, having an empty cart icon.

- `remove-button`**'s new props** - The [Product List](https://developers.vtex.com/docs/apps/vtex.product-list/) app's `remove-button` block received two new strategically important props: `displayMode` and `variation`. The first defines whether the block should be displayed as an icon or as a text (allowing you to [create confirmation modals when displayed as an icon](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-modals-using-icons)). In turn, the second prop defines the remove button visual prominence when it is displayed as a text based on the [VTEX Styleguide](https://styleguide.vtex.com/#/Components/Forms/Button).

## Deprecations ❌

- **Product Summary Price and Product Price blocks** - The Product Summary Price and the Product Price blocks, respectively, pertaining to the [Product Summary](https://developers.vtex.com/docs/guides/vtex-product-summary) and the [Store components](https://developers.vtex.com/docs/guides/vtex-store-components) apps, were deprecated in favor of the [**Product Price**](https://developers.vtex.com/docs/guides/vtex-product-price/) app. Although support for these blocks is still granted, it is strongly recommended to update your Store Theme with the Product Price's blocks in order to keep up with the component's evolution.

## Bug fixes 🐛

- **Minicart item list** - When more than 1 SKU with attachments was added to the [Minicart](https://developers.vtex.com/docs/guides/vtex-minicart) (version 1 and 2), the component interpreted that only 1 should receive the chosen attachment, while the other SKUs would not receive it. This bug was now fixed in both versions and the Minicart lists the correct SKU number with their respective attachment.

- [**Slider Layout dots on mobile**](https://github.com/vtex-apps/slider-layout/pull/21) - The pagination dots, located below the component built using [Slider Layout](https://vtex.io/docs/components/layout-blocks/vtex.slider-layout), were not rendering slides when clicked on using a mobile device - contrary to the Slider's arrows. The pagination dots are now working as expected and users can click on them to change slides.

- [**Image link editing in Site Editor**](https://github.com/vtex-apps/store-image/pull/15) -  
  When an image link was added to the Image component ([Store Image](https://developers.vtex.com/docs/guides/vtex-store-image/) app) using the admin's Site Editor, an unexpected error took place: the `newTab` toggle button was not working properly. This was now fixed and users can correctly configure image links to open in new tabs when editing the Image component in Site Editor.

- [**Links in Brand component**](https://github.com/vtex-apps/store-components/pull/774) - The Store Component's [Product Brand block](https://developers.vtex.com/docs/guides/vtex-store-components-productbrand/) allowed the creation of links in the brand product icon, by using the `logoWithLink` prop. The prop was not functioning properly, which led to this functionality being forgotten. Thanks to a fix, the prop is now 100% available and ready for use!

## Praises ✨

- [pgrimaud](https://github.com/pgrimaud) _from Big Youth_
- [LucasCastroAcctGlobal](https://github.com/LucasCastroAcctGlobal) _from ACCT_
- [BeatrizMiranda](https://github.com/BeatrizMiranda) _from ACCT_
