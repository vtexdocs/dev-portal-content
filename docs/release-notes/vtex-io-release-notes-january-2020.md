---
slug: "vtex-io-release-notes-january-2020"
title: "VTEX IO Release Notes - January 2020"
createdAt: 2020-02-10T13:00:00.000Z
hidden: false
type: "info"
---
![App Development](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-january-2020-0.png)

And we are back, ladies and gentlemen!

Long time no see... really missed you guys! I'm sure that you've missed us too, right? RIGHT!

2019 was a special, intense and long year, full of learnings for each and every one of us, that's for sure. But the time has come to aim above and beyond to **greatness**. Therefore, make sure to keep up-to-date with the IO Release Notes! It's the only way to keep up with everything that we're dutifully preparing for you.

2020, here we are. And here we go:

## Features 🚀

- **Minicart v2** - A brand new Minicart is up and running, much more optimized and flexible that it's former version. For a look at the reasons why you'll want to migrate asap, check out the [documentation](https://developers.vtex.com/docs/apps/vtex.minicart/).

- **Block's composition** - This one here is truly mind-blowing so listen closely: within a block's `children` array, you can now declare any block you choose. That's right! When setting a block as another's child, forget about the allowed blocks list. Declare whatever block you want. But remember: this only works for the `children` array. Blocks declared in the `blocks` array will remain limited to the allowed list of the block parent.

- **Store Link app** - An app that allows you to create and display links that automatically consume context from other blocks. Sounds confusing? It is actually simple and amazing. Just give a look at the [Store Link](https://developers.vtex.com/docs/apps/vtex.store-link/) documentation.

- **JivoChat** - Integrate your store with the JivoChat solution using the [JivoChat pixel app](https://vtex.io/docs/components/pixel/vtex.jivochat/), available now just a click away from you.

- **Listrak** - More pixel apps to come! You are now also able to natively integrate with the [Listrak](https://vtex.io/docs/components/pixel/vtex.listrak-pixel/) solution.

## Improvements ➕

- **Site Editor** - Our beloved admin's Site Editor now allows you to configure some of the many [Shelf](https://developers.vtex.com/docs/apps/vtex.shelf/) (`maxItems`, `arrows`, `showTitle`, `titleText`, `minItemsPerPage`, `itemsPerPage` and `paginationDotsVisibility`) and [Slider Layout](https://developers.vtex.com/docs/apps/vtex.slider-layout/) (`navigationStep`, `itemsPerPage` and `autoplay`) props.

- **Search Results Filters** - The new `facetsBehavior` prop only allows you to display filters with actual search results in the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result/) page. No more misleadings. Yay!

- **Product Summary image** - Choose which product image will be shown in the [Product Summary Image](https://developers.vtex.com/docs/apps/vtex.product-summary/ProductSummaryImage) block thanks to the new `mainImageLabel` prop.

- **CSS Handles** - More CSS Handles for several apps, among which: [Stack Layout](https://developers.vtex.com/docs/apps/vtex.stack-layout/), [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary), [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result/), [Menu](https://developers.vtex.com/docs/apps/vtex.menu/), [Minicart](https://developers.vtex.com/docs/apps/vtex.minicart/), [Flex Layout](https://developers.vtex.com/docs/apps/vtex.flex-layout/) and ALL [store icons](https://developers.vtex.com/docs/apps/vtex.store-icons/). We're seriously not kidding around when it comes to Handles... do not forget to check out each related documentation.

- **SKU Selector** - Previously, the `showValueNameForImageVariation` prop did not serve every scenario it is was meant to because it only indicated a variation's value if it was an image type. It was replaced with a prop, namely the `showValueForVariation`, that encompasses even more scenarios, that is, it now indicates variation's value of all types (image and others!). Do not forget to give the [documentation](https://developers.vtex.com/docs/apps/vtex.store-components/SkuSelector) a quick sneak peak to understand the prop's behavior.

- **Product Summary SKU Selector** - The possibility to add a slider in the [Product Summary SKU Selector](https://developers.vtex.com/docs/apps/vtex.product-summary/ProductSummarySkuSelector) to make user navigation easier has just become reality thanks to the new `displayMode` prop.

## Notable bug fixes 🐛

- **Search Results ordering** - It's always a good idea to improve the Search Results page. Now, sorting products by "Relevance" takes the [score field](https://help.vtex.com/tutorial/how-does-the-score-field-work--1BUZC0mBYEEIUgeQYAKcae) value set in the admin's Catalog into consideration.

- **SKU Selector ordering** - We're really putting our house in order in 2020: the SKU Selector now respects the position given to [SKU specifications](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#sku-specifications) values defined in the admin's catalog, displaying everything according to the retailer's order preference.

- **Product Impression event** - Previously, Product Impression events faced a problem: whenever the Shelf was hovered over, the event triggered the store’s Google Analytics informing that all Shelf products had been seen by the user, even those that were hidden by the SKU Selector’s slider. This is now changed: only products that are in fact displayed are sent by the event.
