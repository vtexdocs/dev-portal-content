---
slug: "vtex-io-release-notes-novemberdecember-2020"
title: "VTEX IO Release Notes - November&December 2020"
createdAt: 2021-01-15T15:00:00.000Z
hidden: false
type: "info"
---
Weep no more, team: here we (_finally_) are 🎉

Let's make room for the VTEX IO Release Notes, this time around bringing you double the excitement from last November and December!

If 2020 made us shed some tears, our VTEX IO team worked around the clock to bring a smile back on our faces 😀 Just look at the awesome stuff they've delivered as last year came to an end:

- 🚀 Condition Layout v2
- ➕ Importing private CSS Classes
- ⚠️ Unannotated queries requested as public
- 🐛 Search results with special characters

And unlike 2020, things are looking up, okay? In addition to the tremendous deliveries the team made, we also have a special announcement regarding IO Docs and the migration of our documentation to the Developer Portal.

Believe me when I say it... you can't sit this one out! Without further ado, introducing the one and only VTEX IO Release Notes:

## Special announcement

- **New home for the VTEX IO documentation**

IO Docs has officially housed VTEX IO documentation since March 13, 2020. It was the successful result of VTEX's effort to create more in-depth and narrowly focused documentation.

With almost a year gone by, it's time to say goodbye: to better take advantage of existing and future VTEX IO documentation and to leverage the development experience of our users, **VTEX IO documentation will henceforth be stored on our [Developer Portal](https://developers.vtex.com/), starting today (January 15, 2021)!**

> ℹ️ All existing documentation will be redirected and automatically migrated to the new platform. No existing link will be lost during this process.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-1.png)
Home to our [API documentation](https://developers.vtex.com/docs/api-reference) and [guides](https://developers.vtex.com/docs/guides) aimed at developers working with integrations and customization, the [**Developer Portal**](https://developers.vtex.com/) - formerly known as Help Center Developer Docs - offers all the necessary resources for VTEX's most advanced users in a single place.

Such changes to the VTEX IO documentation mean a lot more than just content redistribution; trust me, they will ensure better and greater support for VTEX IO users and their specific objectives on our platform.

As to the future of our beloved Release Notes, don't worry: in addition to the [Developer Newsletter](https://forms.gle/DHo3SS7ZaGCvAMow8) bringing you all the essential updates on platform changes, the Developer Portal also has its own Release Notes section:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-2.png)
Nothing but the address will change, I promise! Everything else stays the same, with the same high-quality impactful content, working together as always, but now housed in a place that can fully encourage our potential ✨

## Features 🚀

- **Condition Layout v2:** What is better than the Condition Layout v1? It's the second and most optimized version, of course! Welcome the Condition Layout v2, bringing you features such as verification by product specification value and product availability. Learn more about the new version by checking out the new [documentation](https://developers.vtex.com/docs/apps/vtex.condition-layout/) and the specially-prepared [migration guide](https://github.com/vtex-apps/condition-layout/blob/master/docs/MIGRATION-GUIDE.md)!

- **Native integration between the Subscription module and the frontend:** Forget the messy old days when you had to develop a custom app to manage subscriptions on the frontend! The Product Customizer app is now natively compatible with the [Subscription module](https://help.vtex.com/en/tutorial/how-subscription-works--frequentlyAskedQuestions_4453), meaning you are now able to edit the name and the frequency of a product subscription through the store component in the product details page. Access the [Product Customizer app documentation](https://developers.vtex.com/docs/apps/vtex.product-customizer/) now to get more details about this new feature!

![subscription-gif](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-3.gif)

- `product-reference`: Let's greet the new `product-reference` block exported by the Product List app! The block is responsible for rendering product reference data onto components that leverage from its app, such as the [Minicart](https://developers.vtex.com/docs/apps/vtex.minicart/). Do we have your attention? Do not forget to cast your eyes on the [documentation](https://developers.vtex.com/docs/apps/vtex.product-list/) for more details!

- **Google Customer Review badge:** The Google Customer Reviews pixel app now counts on a new component to enrich your store's frontend: we're talking about the `google-customer-review-badge` block, which renders the Google Customer Review icon to the UI! Check out the [docs](https://vtex.io/docs/components/pixel/vtex.google-customer-reviews/) to better understand how to set it up!

- **Enabling automatic translation in the Messages app:** Safely and quickly enable or disable automatic Messages app translations directly from your VTEX admin account, as highlighted in the screen grab below! But please note: the toggle only defines the configuration for automatic translations, not for manual ones. If you need more info, access the recipe on [Disabling automatic translation](https://developers.vtex.com/docs/guides/vtex-io-documentation-disabling-automatic-translation/)!

![image (10)](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-4.png)

## Improvements ➕

- **Importing private CSS Classes:** Avoid external editions and customize your store components using private CSS classes, i.e., classes whose name contains a hash (unique identifier) instead of the traditional `vendor-app-major-x-classname` format that is generated when importing. For more info on how to import CSS classes (private or public, as we call the ones with the traditional format), access our documentation on [Defining styles](https://developers.vtex.com/docs/guides/vtex-io-documentation-5-defining-styles)!

- **Dynamic routes customization on CMS:** Customizing dynamic routes can now be done through the admin's CMS, thanks to a wonderful new update to the Pages GraphQL. For more on the possibilities of this customization, access this [documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-associating-a-custom-page-to-a-content-type)!

- **Catalog translation by variable** - Translating a store's catalog can be done in the blink of an eye thanks to this improvement which makes it possible to translate the desired catalog data simply by filling in the specific variables in the object of the GraphQL API. Previous translations were only enabled when all the object's variables were filled in. Caught your attention? Have a closer at our documentation on [catalog internationalization](https://developers.vtex.com/docs/guides/catalog-internationalization)!

- **Placeholders on the Store Form component** - Thanks to the new `placeholder` prop, added to the `form-input.textarea` block, the [Store Form](https://vtex.io/docs/components/content-blocks/vtex.store-form/) component now accepts placeholders for text inputs, meaning that from now on you can add descriptions as well as other desired instructions to the form's text fields.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-5.png)

- **Link building in the product brand's name** - A new prop has arrived for the [`product-brand` block](https://developers.vtex.com/docs/apps/vtex.store-components/ProductBrand) from the [Store Components app](https://developers.vtex.com/docs/apps/vtex.store-components/): the `withLink`! Replacing the former `logoWithLink` prop, the new one is here to help you create links for the product brand's website based on text strings or image icons.\
  ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-6.png)
  _take a deep breath, we're half way through already... it's been two whole months! There's a lot of information about where that came from! Check it out:_

- **Multiple gallery layouts** - Having multiple layout configurations for your search results page may sound impossible, but thanks to the Search Result's `gallery-layout-switcher` and `gallery-layout-option` new blocks, it is not! To learn how to customize the page, check out the [Building a search results page with multiple layouts recipe](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-search-results-page-with-multiple-layouts)!

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-7.png)

- **Multiple seller compatibility** - The [Add To Cart Button](https://developers.vtex.com/docs/apps/vtex.add-to-cart-button/), [Buy Button](https://developers.vtex.com/docs/apps/vtex.store-components/BuyButton) and [Product Price](https://developers.vtex.com/docs/apps/vtex.store-components/ProductPrice) now use as their default behavior the first _available_ seller's data, meaning they are able to work with multiple seller data. Previously, the components only worked with the first seller's data, regardless of their availability and ignoring the rest of the seller list - tricky, wasn't it? now, this is what our team calls an improvement!

- **Product image placeholder** - From now on, set a default image as a placeholder for your store products thanks to the new `placeholder` prop, available for the [`product-images`](https://developers.vtex.com/docs/apps/vtex.store-components@3.68.0/ProductImages) and [`product-summary-image`](https://developers.vtex.com/docs/apps/vtex.product-summary/ProductSummaryImage) blocks, respectively from the [Store Components](https://developers.vtex.com/docs/apps/vtex.store-components/) and the [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary/) apps.

- **Product list identification on Google Analytics** - Thanks to the new `listName` prop added to the [`product-summary-list` block](https://developers.vtex.com/docs/apps/vtex.product-summary/ProductSummaryList/), part of the [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary/), and additional improvements made to the [Tag Manager](https://developers.vtex.com/docs/apps/vtex.google-tag-manager/)'s `productClick` event, you can now identify which store shelf users interacted with. No more misleading results for the poor Analytics!

- **Close drawer on the UI** - A new `text` prop was added to the `drawer-close-button` block, part of the [Drawer app](https://developers.vtex.com/docs/apps/vtex.store-drawer/), responsible for closing components on the UI. Thanks to it, you can now close the Drawer using a text button, instead of the traditional `X` icon.

- **The `promoView` and `promotionClick` events** - New events for the [Google Tag Manager pixel app](https://developers.vtex.com/docs/apps/vtex.google-tag-manager/). Best of all? They all follow the official Google-enhanced commerce format! Please welcome the [`promoView`](https://developers.google.com/tag-manager/enhanced-ecommerce#promo-impressions) and the [`promotionClick`](https://developers.google.com/tag-manager/enhanced-ecommerce#promo-clicks) events, responsible for displaying a store's promotion impressions.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-novemberdecember-2020-8.png)

## Warnings ⚠️

- **Unannotated queries requested as public**

The fallback cache option for GraphQL queries that didn't have an annotation on cache policy (`@cacheControl`) has changed from the _default public scope_ to the _private_ instead, in order to solve an internal issue on the platform.

Although it does not affect functionality, changes to the query essence can impact the storefront's performance since all unannotated that were being requested as public are now automatically coming in as private.

Our team advises developers who have created custom VTEX IO GraphQL services to review their schemas closely and, if necessary, add the `@cacheControl(scope: PUBLIC)` directive for the unannotated queries. This [Pull Request](https://github.com/vtex-apps/store-graphql/pull/516) should illustrate how to code the workaround solution.

## Bug fixes 🐛

- [**Displaying modals according to URL changes**](https://github.com/vtex-apps/modal-layout/pull/43) - Previously, modals were not automatically closed according to changes in the URL, meaning that they were kept open regardless of the user's navigation. The question is: was it the best behavior our component could have for our users? We all know the answer to that, so it is time to celebrate: this behavior was fixed, and modals are now automatically closed whenever changes to the URL occur.

- [**Empty-label validation on Tab Layout**](https://github.com/vtex-apps/tab-layout/pull/16) - Still thinking of enhancing user experience, the Tab Layout app will, from now on, only display tabs (i.e., the `tab-list.item` blocks) whose `label` props have been properly filled out. In practice, it is the end of empty tabs being displayed on the UI! Cheers to that!

- [**Product ordering in the `productImpression` event**](https://github.com/vtex-apps/product-list-context/pull/10) - The `position` field, part of the `productImpression` events, was not being properly filled out with the real positioning of listed products. An accurate ordering has now been taken into account by our Product Context, and this bug (praise the Lord) has been fixed!

- [**Search results with special characters**](https://github.com/vtex-apps/store-graphql/pull/503) - Forget about the times when no results were fetched for searches with special characters: due to this magical fix, the Search Result's search bar is more cooperative, meaning that results are now properly displayed regardless of the special characters used to fetch them.

- **`productImpression`'s threshold** - The Google Tag Manager's `productImpression` event was only triggered when 75% or more of the Product Summary component was displayed. This type of threshold for sending data resulted in misleading results to the GTM since Product Summaries are usually displayed as carrousels of many products and slides. With this bug fix, the `productImpression` event no longer has a threshold, and it is being sent out as soon as the Product Summary is visible on the UI.

## Praises ✨

We would not be able to deliver so many amazing results during these last two months if it were not for the following outstanding contributors:

- [Wesly Souza](https://github.com/weslybrandao) _from ACCT_
- [Gustavo Vasconcellos](https://github.com/gustavopvasconcellos) _from ACCT_
- [Lucas Castro](https://github.com/LucasCastroAcctGlobal) _from ACCT_
- [Matheus Araujo](https://github.com/MatheusR42) _from Corebiz_
- [Luiz Eduardo](https://github.com/LEduard0)
- [Renan Guerra](https://github.com/renanguerraa1)
- [Pmarignan](https://github.com/pmarignan)

Thank you, team 💪
