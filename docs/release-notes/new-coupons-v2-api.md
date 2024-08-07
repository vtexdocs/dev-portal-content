---
title: New Coupons v2 API
slug: "new-coupons-v2-api"
hidden: false
type: "added"
excerpt: "We've released  the new coupon list experience and corresponding API that displays additional strategic information, and provides more settings when creating new coupons."
createdAt: "2023-04-26T14:47:00.000Z"
---

A [coupon](https://help.vtex.com/en/tutorial/cupons-beta--1aAEN3ADpz19ss5JCIEBdL) consists of a promotional code composed of a sequence of letters and numbers. Coupons may be used to apply promotions to the shopping cart price. By entering a coupon code at checkout, your customers may get discounts on the order price.

VTEX provides [single coupons](https://help.vtex.com/en/tutorial/coupons-beta--1aAEN3ADpz19ss5JCIEBdL#single-coupons) and [coupon batches](https://help.vtex.com/en/tutorial/coupons-beta--1aAEN3ADpz19ss5JCIEBdL#coupon-batches), however there were no routes to enable you to create coupons in bulk, edit and archive all coupons in the same batch. Thinking about this improvement, we updated the Coupons module.

We added the following routes for creating, managing coupons batches:

- [GET: Get Archived Coupons](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#get-/coupon/group/archived)
- [GET: Get coupon batch codes](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#get-/coupon/group/-groupingKey-/codes)
- [PUT: Archive a coupon batch](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#put-/coupon/group/-groupingKey-/archive)
- [POST: Create coupon batches](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#post-/coupon/group)
- [PUT: Unarchive a coupon batch](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#put-/coupon/group/-groupingKey-/unarchive)
- [GET: Get usage coupon for a coupon batch](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#get-/coupon/usage-count/group/-groupingKey-)
- [GET: Get coupon batch information](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#get-/coupon/group/-groupingKey-)
- [PUT: Edit coupon batch configuration](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api-v2#put-/coupon/group/-groupingKey-)
