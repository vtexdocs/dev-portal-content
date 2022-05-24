---
slug: "region-v2-release"
title: "Region v2"
createdAt: 2022-02-07T20:00:47.067Z
hidden: false
type: "improved"
---

The Region feature allows marketplaces to [display different prices and availability according to the regions](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc) catered to by the white label sellers of that store.

VTEX has launched a new and improved version of this feature, which is now the default for new stores.


## What changed?

The previous version took into consideration availability and price information of up to 15 sellers, even if more sellers were available for the same region. Region v2 does not have that limitation. Because of that, the new version tends to display more accurate information and reduces the likelihood of items being shown as sold out in marketplaces with many sellers.



## What needs to be done?

All accounts already have Region v2 active by default. However, accounts that were already using the Region feature may not have been automatically migrated. If that is your case and you would like to migrate get in touch with [VTEX support](https://help.vtex.com/en/support) in order to activate this feature. 

You can check the version active in your account by seeing the `regionId` string. This string contains `v2.{id}` for accounts using Region v2 and no version indication for Region v1.

We recommend that you validate your implementation of this feature in a separate [test environment](https://help.vtex.com/en/tutorial/requesting-a-test-environment--2nmZAHlfQoGsCWmEWGIoGy).

This improvement also means that Region v2 does not support some customizations done with v1 by stores. Below we go into more detail on how you should adapt your store in case you use one or both of these customizations.


### Getting sellers by region

Region v1 uses a base64 encode to register and some stores created customizations in order to decode this and get the list of sellers for a given region.

This will not work For Region v2, the best way to get sellers by region is using the [Get sellers by region](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion) API request.


### Forcing sellers onto regions

We recommend that you do not do this at all. All seller data processing and selection should be done solely by VTEX Checkout from localization data provided by the shopper.

Instead, we recommend that you make sure all configurations regarding [seller regions](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc#) and [comprehensive sellers](https://help.vtex.com/en/tutorial/comprehensive-seller--5Qn4O2GpjUIzWTPpvLUfkI?&utm_source=autocomplete#) suit the needs of your operation.