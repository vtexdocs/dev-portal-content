---
title: "Optimizing performance"
slug: "vtex-io-documentation-best-practices-for-optimizing-performance"
hidden: false
createdAt: "2020-11-11T12:55:53.602Z"
updatedAt: "2022-12-13T20:17:44.632Z"
---

For ecommerce businesses, appealing offers, high-quality products, or brand recognition might not be enough to convert leads if user experience is left behind.

In the digital world, store website performance plays an essential role in the user experience, directly impacting sales conversion rate and user session time, among other important metrics.

Every millisecond counts and affects not only the consumer decision-making process but also the store website rank in search engine results.

Thus, to help you ensure the success of your online presence, this article introduces a few practices you can implement to optimize store performance and, consequently, improve customer experience.

Some actions that can boost store website performance can be enabled via the VTEX Admin under **Store Settings > Storefront > Store > Advanced**.

![cms-store-advanced](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-0.png)

These features are described and explained in the [Enabling store settings](#enabling-store-settings) section.

Additional actions are detailed in the [Manual optimizations](#manual-optimizations) section.

> ⚠️ For implementation details, read our documentation on [how to safely enable performance settings in your store.](https://developers.vtex.com/docs/guides/vtex-io-documentation-safely-enabling-performance-settings)

These practices can improve SEO by up to 80% and page loading time by over 50%. This data can be identified with leading website performance analysis tools, such as [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) and [Google Analytics](https://support.google.com/analytics/answer/1205784?hl=en).

## Enabling store settings

### Optimizing shopping cart data fetching

The `orderForm` is an object that stores and fetches data from a user order, including each item added to the cart.

To give other Store Theme blocks access to the data stored in the `orderForm` and, consequently, allow them to render it, Store Framework runs the `OrderFormProvider` object on each store page. This object exports all the necessary `orderForm` data to these blocks.

However, all stores using VTEX IO Store Framework currently have two `OrderFormProviders`: a legacy one, still consumed by native blocks such as `minicart` and `buy-button`, and a newer version, which is better suited to replace it.

As a result, we recommend that the stores that already use the new `minicart.v2` and `add-to-cart-button` blocks (instead of `minicart` and `buy-button`, respectively) discontinue `OrderFormProvider` legacy. By consuming from a single provider, you will notice performance improvements in your store.

> ℹ️ More details on how to implement this optimization can be found in the documentation on [Enabling OrderForm optimization](https://developers.vtex.com/docs/guides/vtex-io-documentation-enabling-order-form-optimization/).

### Deactivating the VTEX IO native service worker

The VTEX IO platform provides a native service worker to every store that uses Store Framework. However, since a website can only run one service worker at a time, you may face conflicts when working with a third-party service that provides its own service worker.

To successfully use a third-party solution in your store, you can deactivate the native service worker provided by VTEX IO.

> ℹ️ For more information, read our documentation on [Deactivating the VTEX IO native service worker](https://developers.vtex.com/docs/guides/vtex-io-documentation-deactivating-the-vtex-io-native-service-worker/).

### Optimizing critical CSS

The content that a user first sees when opening a web page is known as above-the-fold content. This part of the page can also be called critical because it needs to be loaded quickly to provide a better user experience.

![critical](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-1.png)

In other words, the critical part of the page must be rendered correctly and promptly before anything else.

However, by default, the browser initiates the rendering of a web page after it has finished loading, parsing, and executing all related CSS files. Consequently, the more extensive the CSS code, the greater the time required to render the critical part of the page.

To address this problem, you can enable critical CSS optimization on home pages. This feature allows the browser to identify the essential CSS code blocks required to display the critical part of the page and load the remaining CSS code asynchronously.

> ⚠️ Keep in mind that enabling this option might cause some style inconsistencies in the store layout. Test it with caution before enabling it on a production workspace. Also, if you notice any side effects on the store website, please [open a ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) and let us know!

### Improving download speed with CSS concatenation

To correctly display a web page layout, the browser needs to make multiple HTTP requests to download each CSS file. However, numerous requests might increase the time to render a single web page.

VTEX IO can avoid various download requests by concatenating multiple CSS files in one.

![concatenation](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-2.png)

Note that by combining CSS in a single file, the browser makes fewer requests and loads web pages faster, improving the performance of your ecommerce website.

### Lazy loading page metadata

Before displaying a web page, the VTEX IO service app responsible for server-side rendering (Render Runtime) interprets the page metadata script. You can see an example of this script below.

```ts
<script>
        __RUNTIME__ = {"account":"vtexstore","amp":false,"bindingChanged":false,"binding":{"id":"aacb04t3-a8fa-4bab-b5bd-2d654d20dcd8","canonicalBaseAddress":"vtexstore.vtex.com"},"culture":{"availableLocales":[],"country":"USA","currency":"USD","language":"en","locale":"en-US","customCurrencyDecimalDigits":null,"customCurrencySymbol":"$"},"production":true,"query":{},"settings":{....
```

Note that this script holds a lot of important data about a web page and can be long, indicating a long task for the browser.

Therefore, when lazy runtime is enabled, this script is broken into smaller ones to prevent the total blocking time of the store website from being compromised.

This way, long tasks will be avoided, and you will reap the benefit of a faster store.

> ⚠️ Some apps might not work as expected when you enable this option. Test it with caution, and analyze the effects on different website pages before enabling it on a production workspace. Also, if you notice any side-effects on your store, please [open a ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) and let us know!

### Lazy rendering submenu items

When you enable this option, menus containing submenus will benefit from automatically enabling the `experimentalOptimizeRendering` prop. This configuration prevents a whole chain of `submenus` from being loaded unnecessarily.

`submenus` will be loaded only if the user interacts with the parent menu (in which the prop was configured).

> ⚠️ Google will not be able to track the hidden submenu items for SEO purposes, since their content will only be loaded with user interaction. Therefore, ensure your SEO strategy is already covered with the store sitemap or the store's first meaningfully painted content.

### Lazy rendering search results and facets

If you enable this option, the scrollable facet box and search results pages will be lazily rendered.

The content inside the user viewport will be initially loaded for rendering. On the other hand, content outside the user viewport will be loaded only during scrolling.

> ⚠️ If you enable this option, you might notice unexpected behaviors, such as gaps while scrolling. If you experience any side effects on your website pages, please [open a ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) and let us know!

### Partially fetching facets

This option improves the performance of search pages by partially fetching the total number of available facets.

Once this option is enabled, users on the search results page will see a maximum of 10 facets per filter. The remaining facets, if any, will not be automatically fetched by the search query nor displayed to the end user.

Instead, a `Show more` button will be displayed below the rendered facets, allowing users to fetch the remaining ones.

> ℹ️ Remember: A facet is the filer value. For example: `Color` is a filter, and the value `Blue` is a facet of that filter.

## Manual optimizations

### Improving scrolling performance

We recommend using the `__fold__` block in scrollable pages.

With this block, you can specify which interface components will be initially loaded for rendering and which ones will be loaded during user scrolling.

This way, only the first visible blocks will be loaded, and the ones "below the fold" will be lazy-loaded during scrolling.

In addition, use the `__fold__.experimentalLazyAssets` block to indicate which theme blocks must be loaded statically when the first user interface interaction occurs.

> ℹ️ Check [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-fold-blocks/) to learn more about Fold blocks.

> ⚠️ If any of these blocks cause any side effects on your website pages, please [open a ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) and let us know!

### Reducing the number of menu blocks

In scenarios in which a Menu block does not contain submenus declared within itself, we recommend that you change its configuration to use `menu-item` blocks as props.

For instance, in the example below, the main `menu-items` (Apparel & Accessories, Home & Decor, and More) cannot have their implementation changed. They must remain as children since they have a trigger to open a `submenu`.

![menu](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-3.png)

However, the internal `menu-items` (Clothing, Accessories, and Eyeglasses) can have their implementation changed from children to props.

Note that every `menu-item` was previously configured as a children/block. With the change, the `menu-items` group declared as props is interpreted as a single block (blue square).

This way, the number of blocks is reduced from 3 to 1.

> ℹ️ Learn more about how to apply both configurations in the [Menu documentation](https://developers.vtex.com/docs/guides/vtex-menu).

### Adjusting image sizes

The size of the images displayed in your store can directly impact overall performance. To optimize image rendering on your website, we recommend that you adopt the practices detailed in [Best practices for rendering images](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-rendering-images/) regarding the media type used in your theme.

> ℹ️ Check this [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-rendering-images/) to learn more about the best practices for rendering images.

### Improving search results

If the search results page is flooded with product information, performance problems can arise when loading or rendering its data.

Fortunately, this can be changed with two props, namely `skusFilter` and `simulationBehavior`.

These props control the SKUs returned for each product in the search query and define whether the displayed search data will be up-to-date (`skusFilter`) or fetched using the cache (`simulationBehavior`).

We recommend that you only allow the first available SKU to be returned for each product (using the `FIRST_AVAILABLE` value in the `skusFilter` prop) and use cache to display the search data (using the `skip` value in the `simulationBehavior` prop).

> ℹ️ Learn more about how to properly configure this in the [Search Results app documentation](https://developers.vtex.com/docs/guides/vtex-search-result).

### Lazy loading of images and product information in a slider

We recommend you build your theme shelf and carousel blocks using Slider Layout.

Slider Layout natively lazy loads the rendered images or product information. That means that the information in a shelf or carousel built with Slider will only be loaded when components receive user interaction, decreasing the website page load time.

However, keep in mind that the more products your shelf or carousel has, the greater the impact on website performance.

> ℹ️ You can find more details on how to use Slider Layout when configuring these two blocks by reading the [Shelf documentation](https://developers.vtex.com/docs/guides/vtex-shelf/) and the recipe on [Building a Carousel using Slider Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout/).
