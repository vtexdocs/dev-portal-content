---
title: "Why are the UTMs not being applied to the cart?"
slug: "why-are-the-utms-not-being-applied-to-the-cart"
hidden: false
createdAt: "2022-07-21T18:11:14.994Z"
updatedAt: "2022-07-21T18:13:29.320Z"
---
When adding products to the cart through the VTEX Checkout API, it is also necessary to inform the marketing tags (UTMs) for each item.

If a URL is created using information from UTMs that have not been previously informed, the purchase will be closed without the application of these UTMs.

To add UTMs to the cart, go to the [Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata) endpoint or enter the `marketingData` information via the [sendAttachment](https://developers.vtex.com/vtex-rest-api/docs/vtexjs-for-checkout#sendattachmentattachmentid-attachment-expectedorderformsections).