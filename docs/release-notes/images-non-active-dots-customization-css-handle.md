---
slug: "images-non-active-dots-customization-css-handle"
title: "Image's non-active dots customization [CSS Handle]"
createdAt: 2020-08-20T15:38:00.000Z
hidden: false
type: "improved"
---

![Store Framework](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/images-non-active-dots-customization-css-handle-0.png)

Previously, there were no CSS handles to enable users to select and customize non-active dots in the `product-images` block (from [Store Components app](https://developers.vtex.com/docs/apps/vtex.store-components/)).

> ℹ️ The non-active dot represents the image that is not currently being hovered on by users.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/images-non-active-dots-customization-css-handle-1.png)

In the image above only the first image dot, which was currently selected (or _active_), had both `vtex-store-components-3-x-swiperBullet` and `vtex-store-components-3-x-swiperBullet--active` CSS classes. The second image dot, which was not active, did not have any CSS class which basically means that users were not able to select it for customization.

Thanks to the new `swiperBullet` and `swiperBullet--active` CSS Handles, the image's non-active dots can now be selected and customized. For more on this, do not forget to access the [Product Images block documentation](https://developers.vtex.com/docs/apps/vtex.store-components/ProductImages/) and our documentation or [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).
