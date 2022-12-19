---
slug: "images-non-active-dots-customization-css-handle"
title: "Image's non-active dots customization [CSS Handle]"
createdAt: 2020-08-20T15:38:00.000Z
hidden: false
type: "improved"
---

![https://img.shields.io/badge/-VTEX%20Store%20Framework-red](https://img.shields.io/badge/-VTEX%20Store%20Framework-red) 

Previously, there were no CSS handles to enable users to select and customize non-active dots in the `product-images` block (from [Store Components app](https://vtex.io/docs/app/vtex.store-components/)).

:information-source: *The non-active dot represents the image that is not currently being hovered on by users.*

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/220187b-image-dot-non-active_17.png)

In the image above only the first image dot, which was currently selected (or *active*), had both `vtex-store-components-3-x-swiperBullet`  and `vtex-store-components-3-x-swiperBullet--active` CSS classes. The second image dot, which was not active, did not have any CSS class which basically means that users were not able to select it for customization.

Thanks to the new `swiperBullet` and `swiperBullet--active` CSS Handles, the image's non-active dots can now be selected and customized. For more on this, do not forget to access the [Product Images block documentation](https://vtex.io/docs/components/all/vtex.store-components/product-images/) and our documentation or [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization/).
