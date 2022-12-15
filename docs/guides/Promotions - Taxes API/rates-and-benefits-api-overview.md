---
title: "Promotions & Taxes API - Overview"
slug: "rates-and-benefits-api-overview"
hidden: false
createdAt: "2020-01-15T00:07:21.427Z"
updatedAt: "2022-08-11T20:46:55.138Z"
---
[block:callout]
{
  "type": "info",
  "body": "Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Promotions and is organized by focusing on the developer's journey."
}
[/block]
The Promotions & Taxes API allows you to manage and retrieve all promotions, coupons and tax rules from your VTEX store.

## Index

### Coupons
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Create multiple coupons](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-multiple-coupons)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Create coupon](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-coupon)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/getbycouponcode)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get archived coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/getarchivedbycouponcode)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Archive coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/archivebycouponcode)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Update coupon](https://developers.vtex.com/vtex-rest-api/reference/update)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get all coupons](https://developers.vtex.com/vtex-rest-api/reference/getall)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Coupon Massive Generation](https://developers.vtex.com/vtex-rest-api/reference/massivegeneration)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get coupon usage](https://developers.vtex.com/vtex-rest-api/reference/getusage)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Unarchive coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/unarchivebycouponcode)

### Promotions and Taxes
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get All Promotions](https://developers.vtex.com/vtex-rest-api/reference/getallbenefits)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get All Taxes](https://developers.vtex.com/vtex-rest-api/reference/getalltaxes)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get Promotion or Tax By ID](https://developers.vtex.com/vtex-rest-api/reference/getcalculatorconfigurationbyid)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Create or Update Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/createorupdatecalculatorconfiguration)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Create Multiple SKU Promotion](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-import-calculatorconfiguration)
<span class="APIMethod APIMethod_fixedWidth APIMethod_put">put</span> [Update Multiple SKU Promotion](https://developers.vtex.com/vtex-rest-api/reference/put_api-rnb-pvt-import-calculatorconfiguration-promotionid)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Archive Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/archivepromotion-1)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Unarchive Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/unarchivepromotion-1)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [List archived Promotions](https://developers.vtex.com/vtex-rest-api/reference/getarchivedpromotions)
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [List archived Taxes](https://developers.vtex.com/vtex-rest-api/reference/getarchivedtaxes)


### Campaign Audiences
<span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> [Get campaign audience configuration](https://developers.vtex.com/vtex-rest-api/reference/getcampaignconfiguration)
<span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Create campaign audience](https://developers.vtex.com/vtex-rest-api/reference/setcampaignconfiguration)