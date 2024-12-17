---
title: "Enabling performance settings"
slug: "vtex-io-documentation-enabling-performance-settings"
hidden: false
createdAt: "2024-12-17T18:14:07.068Z"
updatedAt: ""
---

This guide outlines some practices you can implement to optimize store performance.

For ecommerce businesses, appealing offers, high-quality products, or brand recognition might not be enough to convert leads if the user experience falls short. Store website performance is essential to the user experience, directly impacting sales conversion rate, user session time, and other important metrics.

Every millisecond counts and affects the consumer decision-making process and your store's website rank in search engine results.

You can enable actions to boost your store's website performance directly in the Admin by going to **Store Settings > Storefront > Store > Advanced**.

![cms-store-advanced](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-0.png)

Additionally, you can implement manual optimization by changing the project source code, as described in the [Manual optimizations](#manual-optimizations) section.

These actions can improve SEO by up to 80% and page loading time by over 50%. This data can be identified with leading website performance analysis tools, such as [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) and [Google Analytics](https://support.google.com/analytics/answer/1205784?hl=en). Learn more in the **Monitoring tools** section within the [Performance](LINK) guide.

This guide presents the following sections:

- [Instructions](#instructions): Implementation details.
- [Optimization options](#optimization-options): Methods to enhance store performance.
  - [Store settings](#store-settings): Actions that can be performed directly in the VTEX Admin.
  - [Manual optimizations](#manual-optimizations): Additional manual actions that can be made directly in the project source code.

## Instructions

### (Optional) Step 1 - Applying manual optimizations

If you have implemented [manual optimizations](#manual-optimizations), make sure you use a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) to test these changes before making your new app version publicly available. Learn more about this process in the guide [Deploying a new app version(https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available).

### Step 2 - Applying changes in a production workspace

1. Using the terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference/), log in to the desired account by running `vtex login {account}`.
2. Run the command `vtex use {productionWorkspace} --production` to create and use a **new** [Production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/).

  >⚠️ Replace the values between the curly braces based on your scenario.

3. Using your browser, access the Admin for that workspace.
4. From the account's Admin panel, go to Store Settings > Storefront > Store > Advanced.
5. Follow the instructions in the [Store-settings](#store-settings) section to activate the desired features, then save the changes.
6. Access your store in the workspace you're using and check if the performance improvements were applied.

  > ℹ️ Changes may take some time to reflect.

### Step 3 - Testing and analyzing performance

1. Review and test all your store main pages, ensuring the changes didn't cause any side effects, such as style inconsistencies or undesired behaviors.
2. Access [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights).
3. Using the following URL pattern: `https://{account}.myvtex.com/?workspace={productionWorkspace}`, check your store's performance in the production workspace you're currently working in.

  > ⚠️ Using the standard URL pattern `https://{workspace}--{account}.myvtex.com/` won't show your store performance score in the specified workspace. To analyze performance in a workspace, **you must use the `?workspace={productionWorkspace}` query string** as shown in Step 2.3.

### Step 4: Making your changes publicly available

If you're satisfied with the results, run `vtex promote` to promote your workspace and benefit from a faster store. Before promoting your workspace to master, measure the performance improvements by comparing the performance scores in the production and master workspaces.

## Optimization options

### Store settings

Store settings are actions you can take directly in the VTEX Admin to improve your store performance. The available options are listed below:

#### orderForm optimization

This action disables the legacy orderForm provider.

The `orderForm` is an object that stores and retrieves data from a user's order, including each item added to the cart.

To give other Store Theme blocks access to the data stored in the `orderForm` and allow them to render it, Store Framework runs the `OrderFormProvider` object on each store page. This object exports all the necessary orderForm data to these blocks.

However, all stores using VTEX IO Store Framework currently have two `OrderFormProviders`: a legacy version, still consumed by native blocks such as `minicart` and `buy-button`, and a newer version, which is better suited for replacement.

We recommend that stores already using the new `minicart.v2` and `add-to-cart-button` blocks (instead of `minicart` and `buy-button`, respectively) discontinue the `OrderFormProvider` legacy. By consuming a single provider, you'll notice improvements in your store performance.

> ℹ️ Learn more in the guide [Enabling OrderForm optimization](https://developers.vtex.com/docs/guides/vtex-io-documentation-enabling-order-form-optimization/).

#### Service worker

This action adds the default Service Worker provided by VTEX.

The VTEX IO platform provides a native service worker to every store using Store Framework. However, since a website can only run one service worker at a time, you may face conflicts when working with a third-party service that provides its own service worker.

To resolve this, you can deactivate the native service worker provided by VTEX to successfully use a third-party solution in your store. Learn more in the guide [Deactivating the VTEX IO native service worker](https://developers.vtex.com/docs/guides/vtex-io-documentation-deactivating-the-vtex-io-native-service-worker/).

#### Critical CSS optimization

This action enables CSS optimizations on homepages to boost performance and improve Lighthouse scores. It does so by allowing the browser to identify essential CSS blocks needed to display critical page content, loading the remaining CSS code asynchronously.

The content a user first sees when opening a web page is above the fold. This part of the page can also be called critical because it must load quickly to provide a better user experience.

![critical](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-1.png)

However, by default, the browser initiates the rendering of a web page after it has finished loading, parsing, and executing all related CSS files. Consequently, the more extensive the CSS code, the longer it takes to render the critical part of the page.

> ⚠️ Enabling this option might cause some style inconsistencies in the store layout. Hence, test it with caution before enabling it on a production workspace. Also, if you notice any side effects on the store website, [open a ticket with VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).

#### Enable CSS concatenation

This action concatenates a page CSS in a single file for faster download, reducing the multiple HTTP requests typically required to load each CSS file separately.

![concatenation](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-2.png)

By combining CSS in a single file, the browser makes fewer requests and loads web pages faster, improving the performance of your ecommerce website.

#### Enable lazy runtime

This action enables lazy loading of page metadata.

Before displaying a web page, the VTEX IO service app that renders server-side (Render Runtime) interprets the page metadata script. See the example below:

```ts
<script>
        __RUNTIME__ = {"account":"vtexstore","amp":false,"bindingChanged":false,"binding":{"id":"aacb04t3-a8fa-4bab-b5bd-2d654d20dcd8","canonicalBaseAddress":"vtexstore.vtex.com"},"culture":{"availableLocales":[],"country":"USA","currency":"USD","language":"en","locale":"en-US","customCurrencyDecimalDigits":null,"customCurrencySymbol":"$"},"production":true,"query":{},"settings":{....
```

This script holds a lot of important data about a web page, and it can be long, making it a demanding task for the browser. When lazy runtime is enabled, the script is broken into smaller ones to prevent the total blocking time of the store website from being compromised.

This feature helps to avoid lengthy tasks, leading to a faster store experience.

> ⚠️ Some apps might not work as expected when this option is enabled. Hence, test it with caution before enabling it on a production workspace. Also, if you notice any side effects on the store website, [open a ticket with VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).

#### Enable lazy rendering of submenu items

By enabling this option, menus containing submenus will automatically apply the `experimentalOptimizeRendering` prop. This configuration prevents the entire chain of `submenus` from loading unnecessarily, as `submenus` will only load when the user interacts with the parent menu where the prop is set.

> ⚠️ Google won't be able to track the hidden submenu items for SEO since their content only loads with user interaction. Therefore, make sure your SEO strategy is already covered with the store sitemap or the store's first meaningfully painted content.

#### Enable lazy rendering of search results and facets

When you enable this option, the scrollable facet box and search results pages will be lazily rendered.

The content within the user’s viewport loads initially, while the content outside the viewport loads only as the user scrolls.

> ⚠️ Enabling this option might cause unexpected behaviors, such as gaps while scrolling. If you notice any side effects on the store website, [open a ticket with VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).

#### Enable fetching filters partially

When you enable this option, search result pages will display a maximum of 10 facets per filter.

The search query won't automatically retrieve any additional facets or show them to the user. Instead, a `Show more` button will be displayed below the rendered facets, allowing users to load the remaining ones.

> ℹ️ A facet is a filter value. For example: `Color` is a filter, and the value `Blue` is a facet of that filter.

### Manual optimizations

In addition to the features configured in the VTEX Admin, you can apply manual optimizations directly in the project source code to enhance store performance, such as the following:

#### Improve scrolling performance

We recommend using the `__fold__` block for scrollable pages. This block allows you to specify which interface components load initially and which load as the user scrolls. Only the first visible blocks are loaded initially, while the ones _below the fold_ are lazy-loaded during scrolling.

Use the `__fold__.experimentalLazyAssets` block to specify which theme blocks should load statically upon the first user interaction.

> ℹ️ Learn more about fold blocks in the guide [Lazy loading components](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-fold-blocks).

> ⚠️ If you notice any side effects on the store website, [open a ticket with VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).

#### Reduce the number of menu blocks

In cases where a menu block doesn't have submenus declared within it, configure it to use `menu-item` blocks as props.

In the example below, the main `menu items` (Apparel & Accessories, Home & Decor, and More) can't be modified in their implementation. They must remain as children since they have a trigger to open a `submenu`.

![menu](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-optimizing-performance-3.png)

However, the internal `menu-items` (Clothing, Accessories, and Eyeglasses) can be reconfigured from children to props.

Previously, each `menu-item` was set up as an individual child/block. With the change, the `menu-items` group, declared as props, is treated as a single block, represented by a blue square.

This approach reduces the number of blocks from 3 to 1.

> ℹ️ Learn more about applying both configurations in the [Menu](https://developers.vtex.com/docs/apps/vtex.menu) guide.

#### Adjust image sizes

The size of images displayed in your store may directly impact overall performance. To optimize image rendering, follow the practices outlined in the guide [Optimizing image rendering](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-rendering-images/), focusing on the media types used in your theme.

#### Improve search results

Performance issues may occur during data loading and rendering if the search results page is overloaded with product information.

To address this, use the `skusFilter` and `simulationBehavior` props. These props control the SKUs returned for each product in the search query, determining if the displayed search data will be current (`skusFilter`) or retrieved from the cache (`simulationBehavior`).

We recommend setting `skusFilter` to `FIRST_AVAILABLE` to return only the first available SKU for each product, and `simulationBehavior` to `skip` to display search data from the cache.

> ℹ️ Learn more about prop configuration in the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app guide.

#### Use lazy loading for images and product information in sliders

We recommend building your theme's shelf and carousel blocks using the native component [Slider Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout).

Slider Layout uses lazy loading to automatically load images and product information only when users interact with shelves or carousels, reducing overall page load time. However, having more products in these components may negatively impact website performance.

> ℹ️ Learn more about using Slider Layout in the guides [Shelf](https://developers.vtex.com/docs/guides/vtex-shelf/) and [Building a Carousel using Slider Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout/).